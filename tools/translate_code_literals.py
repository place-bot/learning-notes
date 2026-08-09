#!/usr/bin/env python3
"""Translate Chinese comments and string literals inside fenced code blocks."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


CJK_RE = re.compile(r"[\u3400-\u9fff]")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)(.*)$")
ESCAPE_RE = re.compile(r"\\(?:n|r|t|\\|\"|')")


def quoted_ranges(line: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    quote: str | None = None
    start = 0
    escaped = False
    for index, char in enumerate(line):
        if quote is None:
            if char in {'"', "'"}:
                quote = char
                start = index + 1
        elif escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == quote:
            ranges.append((start, index))
            quote = None
    return ranges


def comment_start(line: str) -> int | None:
    quote: str | None = None
    escaped = False
    for index, char in enumerate(line):
        if quote is None:
            if char in {'"', "'"}:
                quote = char
            elif char == "#":
                return index + 1
        elif escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == quote:
            quote = None
    return None


def protect_escapes(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        key = f"ZXQESC{len(protected):04d}QXZ"
        protected[key] = match.group(0)
        return key

    return ESCAPE_RE.sub(replace, text), protected


def translate(binary: Path, texts: list[str]) -> dict[str, str]:
    prepared: list[str] = []
    escapes: list[dict[str, str]] = []
    for source in texts:
        value, protected = protect_escapes(source)
        prepared.append(value)
        escapes.append(protected)
    payload = json.dumps(
        {"texts": prepared, "batchSize": 96},
        ensure_ascii=False,
    ).encode("utf-8")
    result = subprocess.run(
        [str(binary)],
        input=payload,
        stdout=subprocess.PIPE,
        check=True,
    )
    outputs = json.loads(result.stdout)["translations"]
    mapping: dict[str, str] = {}
    for source, output, protected in zip(texts, outputs, escapes):
        for key, value in protected.items():
            output = output.replace(key, value)
        mapping[source] = output.strip()
    return mapping


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--binary", type=Path, required=True)
    args = parser.parse_args()

    files = sorted(args.root.rglob("*.en.md"))
    pieces: set[str] = set()
    locations: dict[Path, list[tuple[int, int, int, str]]] = {}

    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        marker: str | None = None
        language = ""
        for line_index, line in enumerate(lines):
            fence = FENCE_RE.match(line)
            if fence:
                current = fence.group(1)[0]
                if marker == current:
                    marker = None
                    language = ""
                else:
                    marker = current
                    language = fence.group(2).strip().lower()
                continue
            if marker is None or language in {"text", "mermaid"} or not CJK_RE.search(line):
                continue

            spans = quoted_ranges(line)
            comment = comment_start(line)
            if comment is not None:
                spans.append((comment, len(line)))
            if language == "csv" and not spans:
                spans = [(0, len(line))]

            for start, end in sorted(set(spans)):
                source = line[start:end]
                if CJK_RE.search(source):
                    pieces.add(source)
                    locations.setdefault(path, []).append(
                        (line_index, start, end, source)
                    )

    ordered = sorted(pieces)
    print(f"Translating {len(ordered)} unique code comments or strings")
    mapping = translate(args.binary, ordered)

    for path, edits in locations.items():
        lines = path.read_text(encoding="utf-8").splitlines()
        by_line: dict[int, list[tuple[int, int, str]]] = {}
        for line_index, start, end, source in edits:
            by_line.setdefault(line_index, []).append(
                (start, end, mapping[source])
            )
        for line_index, replacements in by_line.items():
            line = lines[line_index]
            for start, end, translated in sorted(replacements, reverse=True):
                line = line[:start] + translated + line[end:]
            lines[line_index] = line
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
