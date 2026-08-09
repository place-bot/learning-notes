#!/usr/bin/env python3
"""Translate MkDocs Markdown with Apple's on-device Translation framework.

The script writes translations to a staging directory. It preserves paths,
code spans, URLs, HTML tags, and LaTeX while translating prose and headings.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


CJK_RE = re.compile(r"[\u3400-\u9fff]")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$")
PROTECTED_PATTERNS = [
    re.compile(r"`[^`\n]+`"),
    re.compile(r"\\\(.+?\\\)"),
    re.compile(r"\]\([^)]+\)"),
    re.compile(r"https?://[^\s)>]+"),
    re.compile(r"<[^>]+>"),
    re.compile(r"\{#[^}]+\}"),
]
PLACEHOLDER_RE = re.compile(r"ZXQPH\d{6}QXZ")
LATEX_TEXT_RE = re.compile(r"\\text\{([^{}]*)\}")
ASCII_RUN_RE = re.compile(r"[^\u3400-\u9fff\n]*[A-Za-z][^\u3400-\u9fff\n]*")


@dataclass
class Segment:
    file_index: int
    line_index: int
    cell_index: int | None
    source: str
    protected: dict[str, str]
    prefix: str = ""


def load_glossary(path: Path) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        source, target = raw.split("\t", 1)
        pairs.append((source, target))
    return sorted(pairs, key=lambda pair: len(pair[0]), reverse=True)


def apply_glossary(text: str, glossary: list[tuple[str, str]]) -> str:
    for source, target in glossary:
        text = text.replace(source, target)
    return text


def protect_inline(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        if PLACEHOLDER_RE.fullmatch(match.group(0)):
            return match.group(0)
        key = f"ZXQPH{len(protected):06d}QXZ"
        protected[key] = match.group(0)
        return key

    cjk_count = len(CJK_RE.findall(text))
    ascii_letter_count = len(re.findall(r"[A-Za-z]", text))
    patterns = PROTECTED_PATTERNS
    if ascii_letter_count > 80 and ascii_letter_count > cjk_count * 3:
        patterns = [ASCII_RUN_RE, *PROTECTED_PATTERNS]

    for pattern in patterns:
        text = pattern.sub(replace, text)
    return text, protected


def restore_inline(text: str, protected: dict[str, str]) -> str:
    for key, value in reversed(protected.items()):
        text = text.replace(key, value)
    return text


def polish_translation(text: str) -> str:
    replacements = {
        "Item Response Theory (Item Response Theory, IRT)": "Item Response Theory (IRT)",
        "Classical Test Theory (Classical Test Theory, CTT)": "Classical Test Theory (CTT)",
        "cognitive diagnosis model (Cognitive Diagnosis Model, CDM)": (
            "Cognitive Diagnosis Model (CDM)"
        ),
        "computerized adaptive testing (Computerized Adaptive Testing, CAT)": (
            "Computerized Adaptive Testing (CAT)"
        ),
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\s+\]\(", "](", text)
    return text


def split_table_row(line: str) -> list[str]:
    return line.split("|")


def compile_translator(source: Path, binary: Path) -> None:
    binary.parent.mkdir(parents=True, exist_ok=True)
    if binary.exists() and binary.stat().st_mtime >= source.stat().st_mtime:
        return
    subprocess.run(
        [
            "swiftc",
            "-parse-as-library",
            "-target",
            "arm64-apple-macosx26.4",
            str(source),
            "-o",
            str(binary),
        ],
        check=True,
    )


def translate_segments(
    binary: Path,
    segments: list[Segment],
    batch_size: int,
    group_segments: int,
    group_chars: int,
    backend: str,
    workers: int,
) -> list[str]:
    grouped_sources: list[str] = []
    current: list[str] = []
    current_chars = 0

    for index, segment in enumerate(segments):
        marked = f"ZXQSEG{index:06d}QXZ\n{segment.source}"
        if current and (
            len(current) >= group_segments or current_chars + len(marked) > group_chars
        ):
            grouped_sources.append("\n".join(current))
            current = []
            current_chars = 0
        current.append(marked)
        current_chars += len(marked) + 1
    if current:
        grouped_sources.append("\n".join(current))

    if backend == "apple":
        payload = json.dumps(
            {"texts": grouped_sources, "batchSize": batch_size},
            ensure_ascii=False,
        ).encode("utf-8")
        result = subprocess.run(
            [str(binary)],
            input=payload,
            stdout=subprocess.PIPE,
            check=True,
        )
        grouped_translations = json.loads(result.stdout)["translations"]
    else:
        def translate_group(index_and_source: tuple[int, str]) -> tuple[int, str]:
            index, source = index_and_source
            data = urllib.parse.urlencode(
                {
                    "client": "gtx",
                    "sl": "zh-CN",
                    "tl": "en",
                    "dt": "t",
                    "q": source,
                }
            ).encode("utf-8")
            request = urllib.request.Request(
                "https://translate.googleapis.com/translate_a/single",
                data=data,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            for attempt in range(6):
                try:
                    with urllib.request.urlopen(request, timeout=60) as response:
                        payload = json.load(response)
                    translated = "".join(
                        part[0] for part in payload[0] if part and part[0]
                    )
                    return index, translated
                except Exception:
                    if attempt == 5:
                        raise
                    time.sleep(2**attempt)
            raise RuntimeError("unreachable")

        grouped_translations = [""] * len(grouped_sources)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(translate_group, item)
                for item in enumerate(grouped_sources)
            ]
            completed = 0
            for future in concurrent.futures.as_completed(futures):
                index, translated = future.result()
                grouped_translations[index] = translated
                completed += 1
                if completed % 25 == 0 or completed == len(futures):
                    print(
                        f"Translated {completed}/{len(futures)} batches",
                        file=sys.stderr,
                    )
    translations: list[str | None] = [None] * len(segments)
    marker_re = re.compile(
        r"ZXQSEG(\d{6})QXZ\s*(.*?)(?=ZXQSEG\d{6}QXZ|\Z)",
        re.DOTALL,
    )
    for group in grouped_translations:
        for match in marker_re.finditer(group):
            translations[int(match.group(1))] = match.group(2).strip()
    missing = [index for index, value in enumerate(translations) if value is None]
    if missing:
        preview = ", ".join(map(str, missing[:10]))
        raise RuntimeError(f"Translation response is missing segment(s): {preview}")
    return [value for value in translations if value is not None]


def collect_files(source_root: Path, only: list[str]) -> list[Path]:
    if only:
        files = [source_root / item for item in only]
    else:
        files = sorted(source_root.rglob("*.md"))
    return [path for path in files if not path.name.endswith(".en.md")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--glossary", type=Path, required=True)
    parser.add_argument("--swift-source", type=Path, required=True)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--backend", choices=["apple", "google"], default="google")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=96)
    parser.add_argument("--group-segments", type=int, default=32)
    parser.add_argument("--group-chars", type=int, default=3500)
    parser.add_argument("--only", nargs="*", default=[])
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    output_root = args.output_root.resolve()
    glossary = load_glossary(args.glossary)
    files = collect_files(source_root, args.only)
    if args.shard_count < 1 or not 0 <= args.shard_index < args.shard_count:
        parser.error("--shard-index must be within --shard-count")
    files = files[args.shard_index :: args.shard_count]
    if args.backend == "apple":
        compile_translator(args.swift_source, args.binary)

    file_lines: list[list[str]] = []
    table_cells: dict[tuple[int, int], list[str]] = {}
    segments: list[Segment] = []

    for file_index, path in enumerate(files):
        lines = path.read_text(encoding="utf-8").splitlines()
        file_lines.append(lines)
        fence_marker: str | None = None
        fence_language = ""
        math_block = False

        for line_index, raw_line in enumerate(lines):
            stripped = raw_line.strip()
            fence_match = FENCE_RE.match(raw_line)
            if fence_match:
                marker = fence_match.group(1)[0]
                if fence_marker == marker:
                    fence_marker = None
                    fence_language = ""
                else:
                    fence_marker = marker
                    fence_language = raw_line[fence_match.end() :].strip().lower()
                continue
            if fence_marker is not None:
                if fence_language not in {"text", "mermaid"} or not CJK_RE.search(raw_line):
                    continue
                leading = raw_line[: len(raw_line) - len(raw_line.lstrip())]
                content = raw_line[len(leading) :]
                prepared = apply_glossary(content, glossary)
                prepared, protected = protect_inline(prepared)
                segments.append(
                    Segment(file_index, line_index, None, prepared, protected, leading)
                )
                continue
            if stripped in {r"\[", "$$"}:
                math_block = True
                continue
            if math_block:
                if stripped in {r"\]", "$$"}:
                    math_block = False
                    continue
                for match in LATEX_TEXT_RE.finditer(raw_line):
                    content = match.group(1)
                    if CJK_RE.search(content):
                        prepared = apply_glossary(content, glossary)
                        prepared, protected = protect_inline(prepared)
                        segments.append(
                            Segment(file_index, line_index, match.start(1), prepared, protected)
                        )
                continue
            if not stripped or TABLE_SEPARATOR_RE.match(raw_line):
                continue

            if "|" in raw_line and stripped.startswith("|"):
                cells = split_table_row(raw_line)
                table_cells[(file_index, line_index)] = cells
                for cell_index, cell in enumerate(cells):
                    if CJK_RE.search(cell):
                        prepared = apply_glossary(cell, glossary)
                        prepared, protected = protect_inline(prepared)
                        segments.append(
                            Segment(file_index, line_index, cell_index, prepared, protected)
                        )
                continue

            if CJK_RE.search(raw_line):
                leading = raw_line[: len(raw_line) - len(raw_line.lstrip())]
                content = raw_line[len(leading) :]
                prepared = apply_glossary(content, glossary)
                prepared, protected = protect_inline(prepared)
                segments.append(Segment(file_index, line_index, None, prepared, protected, leading))

    print(f"Translating {len(files)} files and {len(segments)} prose segments", file=sys.stderr)
    translations = translate_segments(
        args.binary,
        segments,
        args.batch_size,
        args.group_segments,
        args.group_chars,
        args.backend,
        args.workers,
    )

    latex_replacements: dict[tuple[int, int], list[tuple[int, str]]] = {}
    for segment, translated in zip(segments, translations):
        translated = segment.prefix + polish_translation(
            restore_inline(translated, segment.protected)
        )
        key = (segment.file_index, segment.line_index)
        if segment.cell_index is None:
            file_lines[segment.file_index][segment.line_index] = translated
        elif key in table_cells:
            table_cells[key][segment.cell_index] = translated
        else:
            latex_replacements.setdefault(key, []).append((segment.cell_index, translated))

    for (file_index, line_index), cells in table_cells.items():
        file_lines[file_index][line_index] = "|".join(cells)

    for (file_index, line_index), replacements in latex_replacements.items():
        line = file_lines[file_index][line_index]
        matches = list(LATEX_TEXT_RE.finditer(line))
        by_start = {start: text for start, text in replacements}
        for match in reversed(matches):
            replacement = by_start.get(match.start(1))
            if replacement is not None:
                line = line[: match.start(1)] + replacement + line[match.end(1) :]
        file_lines[file_index][line_index] = line

    for path, lines in zip(files, file_lines):
        relative = path.relative_to(source_root)
        output = output_root / relative.parent / f"{relative.stem}.en.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote staged translations to {output_root}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
