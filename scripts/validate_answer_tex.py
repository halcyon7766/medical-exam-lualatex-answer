#!/usr/bin/env python
"""Validate a generated medical exam LuaLaTeX answer file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BOXES = ["QuestionBox", "AnswerBox", "ExplanationBox"]
LOG_PATTERNS = [
    "画像が見つかりません",
    "LaTeX Error",
    "Fatal error",
    "Emergency stop",
]
GENERIC_OPTION_REVIEW_PATTERNS = [
    "本問の決定的条件から外れる",
    "示す病態・所見・処置に一致する内容へ置き換える必要がある",
    "示す病態・所見・処置に一致する内容へ置き換える必要がある",
    "別疾患・別部位・別段階の知識としては重要",
    "別疾患・別部位・別段階の知識としては重要",
]


def strip_latex_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        out: list[str] = []
        escaped = False
        for ch in line:
            if ch == "%" and not escaped:
                break
            out.append(ch)
            escaped = ch == "\\" and not escaped
            if ch != "\\":
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", help="Generated .tex file")
    parser.add_argument("--expected", type=int, default=None, help="Expected question count")
    parser.add_argument("--log", default=None, help="Optional LaTeX .log file")
    args = parser.parse_args()

    tex_path = Path(args.tex).resolve()
    if not tex_path.exists():
        print(f"missing tex: {tex_path}", file=sys.stderr)
        return 2

    raw_text = tex_path.read_text(encoding="utf-8")
    text = strip_latex_comments(raw_text)
    body_text = text.split(r"\begin{document}", 1)[1] if r"\begin{document}" in text else text
    ok = True

    counts = {box: count(r"\\begin\{" + re.escape(box) + r"\}", text) for box in BOXES}
    for box, n in counts.items():
        print(f"{box}: {n}")
        if args.expected is not None and n != args.expected:
            print(f"expected {args.expected} {box}, got {n}", file=sys.stderr)
            ok = False

    if len(set(counts.values())) != 1:
        print(f"box counts differ: {counts}", file=sys.stderr)
        ok = False

    explain_heading_count = count(r"\\ExplainHeading\{", text)
    choice_explanation_count = count(r"\\ChoiceExplanation\{", text)
    basic_matter_count = count(r"\\begin\{BasicMatterBox\}", text)
    old_option_table_count = count(r"\\begin\{OptionReviewTable\}", text)
    old_pearl_box_count = count(r"\\begin\{PearlBox\}", text)
    old_option_review_count = count(r"\\OptionReview\{", text)
    old_heading_count = count(r"\\ExplainHeading\{(?:概要/病態生理|正解の根拠|選択肢別検討)\}", text)
    print(f"ExplainHeading: {explain_heading_count}")
    print(f"ChoiceExplanation: {choice_explanation_count}")
    print(f"BasicMatterBox: {basic_matter_count}")
    print(f"old OptionReviewTable: {old_option_table_count}")
    print(f"old PearlBox: {old_pearl_box_count}")
    print(f"old OptionReview: {old_option_review_count}")
    print(f"old explanation headings: {old_heading_count}")
    if old_option_table_count or old_pearl_box_count or old_option_review_count or old_heading_count:
        ok = False

    raw_include = count(r"(?<!Safe)\\includegraphics", body_text)
    print(f"raw includegraphics: {raw_include}")
    if raw_include:
        ok = False

    unreadable = text.count("【判読不能】")
    print(f"unreadable markers: {unreadable}")

    generic_option_reviews = [p for p in GENERIC_OPTION_REVIEW_PATTERNS if p in text]
    print(f"generic option-review phrases: {len(generic_option_reviews)}")
    for phrase in generic_option_reviews:
        print(f"  {phrase}", file=sys.stderr)
    if generic_option_reviews:
        ok = False

    image_arg_patterns = [
        r"\\SafeIncludeGraphics(?:\[[^\]]*\])?\{([^}]+)\}",
        r"\\ExamFigure(?:\[[^\]]*\])?\{([^}]+)\}",
    ]
    abs_image_paths: list[str] = []
    visible_path_like = re.findall(r"(?:[A-Za-z]:\\\\|[A-Za-z]:/|/Users/|/home/|/tmp/|C:\\\\|D:\\\\)[^\s{}]+", body_text)
    for pattern in image_arg_patterns:
        for m in re.finditer(pattern, body_text):
            name = m.group(1)
            if re.search(r"(?:^[A-Za-z]:[\\/]|^/|[\\/])", name):
                abs_image_paths.append(name)
    print(f"absolute image paths: {len(abs_image_paths)}")
    print(f"visible filesystem paths: {len(visible_path_like)}")
    if abs_image_paths or visible_path_like:
        ok = False

    missing_images: list[str] = []
    for m in re.finditer(r"\\SafeIncludeGraphics(?:\[[^\]]*\])?\{([^}]+)\}", body_text):
        name = m.group(1)
        if not (tex_path.parent / name).exists():
            missing_images.append(name)
    print(f"missing referenced images: {len(missing_images)}")
    for name in missing_images[:20]:
        print(f"  {name}", file=sys.stderr)
    if missing_images:
        ok = False

    log_path = Path(args.log).resolve() if args.log else tex_path.with_suffix(".log")
    if log_path.exists():
        log_text = log_path.read_text(encoding="utf-8", errors="replace")
        hits = [p for p in LOG_PATTERNS if p in log_text]
        print(f"log fatal patterns: {len(hits)}")
        for hit in hits:
            print(f"  {hit}", file=sys.stderr)
        if hits:
            ok = False
    else:
        print("log fatal patterns: skipped (log not found)")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
