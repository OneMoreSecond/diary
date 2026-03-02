#!/usr/bin/env python3

from __future__ import annotations

import argparse
import calendar
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class DiaryTarget:
    root: Path
    day: date

    @property
    def year_dir(self) -> Path:
        return self.root / f"{self.day.year:04d}"

    @property
    def month_dir_name(self) -> str:
        # Match existing repo convention: English month abbreviation (e.g. "Mar").
        return calendar.month_abbr[self.day.month]

    @property
    def month_dir(self) -> Path:
        return self.year_dir / self.month_dir_name

    @property
    def filename(self) -> str:
        return f"{self.day.isoformat()}.md"

    @property
    def path(self) -> Path:
        return self.month_dir / self.filename

    @property
    def title_line(self) -> str:
        return f"# {self.day.isoformat()}\n"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create today's diary markdown file under YYYY/Mon/YYYY-MM-DD.md"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Diary repo root (default: directory containing init.py)",
    )
    parser.add_argument(
        "--date",
        dest="day",
        type=date.fromisoformat,
        default=date.today(),
        help="Override date (ISO format: YYYY-MM-DD). Default: today.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    target = DiaryTarget(root=args.root, day=args.day)
    target.month_dir.mkdir(parents=True, exist_ok=True)

    if target.path.exists():
        print(target.path)
        return 0

    target.path.write_text(f"{target.title_line}\n", encoding="utf-8")
    print(target.path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
