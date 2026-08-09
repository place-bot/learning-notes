#!/usr/bin/env python3
"""Generate English nav_translations for mkdocs-static-i18n."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

import yaml


CJK_RE = re.compile(r"[\u3400-\u9fff]")


def collect_labels(value: object, labels: list[str]) -> None:
    if isinstance(value, list):
        for item in value:
            collect_labels(item, labels)
    elif isinstance(value, dict):
        for label, child in value.items():
            if CJK_RE.search(label) and label not in labels:
                labels.append(label)
            collect_labels(child, labels)


def load_glossary(path: Path) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        source, target = line.split("\t", 1)
        pairs.append((source, target))
    return sorted(pairs, key=lambda pair: len(pair[0]), reverse=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--glossary", type=Path, required=True)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    labels: list[str] = []
    collect_labels(config["nav"], labels)
    glossary = load_glossary(args.glossary)

    prepared: list[str] = []
    for label in labels:
        value = label
        for source, target in glossary:
            value = value.replace(source, target)
        prepared.append(value)

    payload = json.dumps(
        {"texts": prepared, "batchSize": 96},
        ensure_ascii=False,
    ).encode("utf-8")
    result = subprocess.run(
        [str(args.binary)],
        input=payload,
        stdout=subprocess.PIPE,
        check=True,
    )
    translations = json.loads(result.stdout)["translations"]
    mapping = dict(zip(labels, translations))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.safe_dump(
            mapping,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(mapping)} navigation translations to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
