#!/usr/bin/env python
"""Run YomiToku exports for Japanese medical exam PDFs/images."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="PDF or image file to OCR")
    parser.add_argument("-o", "--outdir", default=None, help="Output directory")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda", "mps"])
    parser.add_argument("--lite", action="store_true", help="Use YomiToku lite mode")
    parser.add_argument("--figure-letter", action="store_true", help="Extract text inside figures")
    parser.add_argument(
        "--formats",
        default="md,json,html",
        help="Comma-separated YomiToku formats, usually md,json,html,csv,pdf",
    )
    args = parser.parse_args()

    if shutil.which("yomitoku") is None:
        raise SystemExit("yomitoku command was not found. Install or use fallback OCR.")

    src = Path(args.input).resolve()
    if not src.exists():
        raise SystemExit(f"Input does not exist: {src}")

    out_root = Path(args.outdir).resolve() if args.outdir else src.with_suffix("").parent / f"{src.stem}_assets" / "yomitoku"
    out_root.mkdir(parents=True, exist_ok=True)

    for fmt in [x.strip() for x in args.formats.split(",") if x.strip()]:
        fmt_out = out_root / fmt
        fmt_out.mkdir(parents=True, exist_ok=True)
        cmd = ["yomitoku", str(src), "-f", fmt, "-o", str(fmt_out), "-v", "--figure", "-d", args.device]
        if args.lite:
            cmd.append("--lite")
        if args.figure_letter:
            cmd.append("--figure_letter")
        run(cmd)

    print(f"YomiToku artifacts written to: {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
