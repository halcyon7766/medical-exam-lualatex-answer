# PDF and YomiToku Workflow

Use this reference when the source exam is a PDF or page image, especially a Japanese scanned exam.

## Decision Flow

1. Inspect the input:
   - `pdfinfo input.pdf` for page count and metadata.
   - `pdftotext -layout input.pdf -` to check embedded text.
2. If the PDF is scanned, layout-heavy, table-heavy, or contains figures, run YomiToku.
3. If YomiToku is unavailable, use page image extraction plus fallback OCR and state the fallback in the final report.

## Output Layout

Create a deterministic asset directory near the source:

```text
<exam>_assets/
  yomitoku/
    md/
    json/
    html/
    figures/
    vis/
  pages/
  generate_<exam>_answer.py
  <exam> 解答解説.tex
  <exam> 解答解説.pdf
```

Keep final figures next to the generated `.tex` or copy them there before compiling.

## YomiToku Commands

Preferred GPU/normal mode:

```powershell
yomitoku input.pdf -f md -o .\yomitoku\md -v --figure
yomitoku input.pdf -f json -o .\yomitoku\json -v --figure
yomitoku input.pdf -f html -o .\yomitoku\html -v --figure
```

CPU-friendly mode:

```powershell
yomitoku input.pdf -f md --lite -d cpu -o .\yomitoku\md -v --figure
yomitoku input.pdf -f json --lite -d cpu -o .\yomitoku\json -v --figure
yomitoku input.pdf -f html --lite -d cpu -o .\yomitoku\html -v --figure
```

Add `--figure_letter` when text inside figures is important and extraction quality is acceptable.

## Reconciliation Rules

- Use YomiToku Markdown for reading order, then reflow question stems into readable paragraphs instead of preserving arbitrary OCR/source line breaks. Verify option labels and question numbering against the page image.
- Use JSON/HTML/CSV when tables are present because Markdown may flatten cells.
- Use extracted figures for LaTeX, but inspect the original page when labels, captions, surrounding question text, or orientation matter.
- Correct obvious OCR typos, dropped characters, and mojibake when the intended text is unambiguous from context or the original page image. Do not guess corrections that could alter medical meaning, numbers, units, polarity, or option truth value.
- Mark unresolved text as `【判読不能】`.

## Fallback

If YomiToku is unavailable or fails:

1. Extract page images with `pdftoppm -r 220 -png`.
2. OCR with another tool only as an aid.
3. Inspect page images directly for all ambiguous text, tables, and figures.
4. Report the fallback and any remaining uncertainty.
