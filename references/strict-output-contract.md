# Strict Output Contract

Read this before drafting the final `.tex`.

## Template

- Use a user-provided style sample first; otherwise use `assets/mdAnswer_example.tex`.
- Preserve the template preamble, color theme logic, title macros, `QuestionBox`, `AnswerBox`, `ExplanationBox`, `ChoiceList`, `\SafeIncludeGraphics`, `\ExamFigure`, `\ExplainHeading`, `\ChoiceExplanation`, `BasicMatterBox`, and `\BasicMatterTitle`.
- Preserve scaffold order: `\maketitle`, `\tableofcontents`, `\newpage`.
- Set the subject with `\SetExamSubject{...}` from the user-specified or inferred subject. The template also reapplies `\ApplySubjectColorTheme` at `\begin{document}`; do not hard-code content colors.

## Source Fidelity

- Preserve all source content needed to answer: question numbers, lead-ins, instructions, options, tables, labels, visible notes, and figure/table relationships.
- Do not mechanically preserve source line breaks in question stems. Reflow OCR text into natural Japanese paragraphs and LaTeX-readable formatting while preserving meaning, order, instructions, values, units, and option boundaries.
- Treat original PDF/page images as the transcription authority. Use OCR/YomiToku outputs as aids.
- Correct obvious OCR typos, dropped characters, and mojibake only when the intended text is unambiguous from context or the original page image. If the correction could change medical meaning, numbers, units, polarity, or an option's truth value, do not guess; mark `【判読不能】` or add a note.
- If required answer data are missing, keep the gap explicit and answer `不明（根拠不足）`.

## Question Boxes

- Create exactly one `QuestionBox`, one `AnswerBox`, and one `ExplanationBox` for every question.
- Use `ChoiceList` for choice questions; strip synthetic labels only when clearly separate from option text. Reflow option text for readability, but keep every option as a distinct item and preserve negations, qualifiers, values, and units.
- Preserve instructions such as `2つ選べ`, `誤っているもの`, `最も`, `まず行う`, and `禁忌`.
- For mixed exams, section by source grouping, subject area, organ system, or exam part without changing question order.

## Images and Tables

- Convert image references to basename-only paths.
- Place question-critical figures immediately below the relevant question text.
- Do not use full-page screenshots as a substitute for OCR transcription. Include full-page or cropped page images only when the question depends on an image/table/layout, or when an explicitly marked OCR ambiguity needs visual context.
- Use `\ExamFigure` for new bundled-template output; otherwise use `\SafeIncludeGraphics`.
- Never emit absolute image paths or raw `\includegraphics`. Do not print image filenames or paths in missing-image placeholders, captions, or visible body text unless the source document itself contains that text.
- Copy or generate YomiToku-extracted figures next to the `.tex` file before referencing them.
- Reproduce table cells completely. Prefer YomiToku HTML/CSV/JSON for scanned table recovery, then verify against the page image.

## Answer and Explanation

- State correct letters explicitly, for example `\textbf{正解：} b, d`.
- For descriptive questions, provide a compact model answer with key scoring terms.
- Follow `references/answer-explanation-policy.md` for official-answer priority, question-type handling, subject emphasis, exam-date differences, labs/units, figures, and confidence.
- Use this explanation pattern unless the user or template requires another:

```tex
% 画像・病理・検査値問題の場合のみ
\ExplainHeading{画像・病理・検査所見の読み取り}
...

\ExplainHeading{解法の要点}
...

\ExplainHeading{選択肢解説}
\ChoiceExplanation{a}{wrong}{選択肢本文}{...}
\ChoiceExplanation{b}{correct}{選択肢本文}{...}

\begin{BasicMatterBox}
  \BasicMatterTitle{基本事項}
  \begin{itemize}[leftmargin=1.2em]
    \item ...
    \item ...
    \item ...
  \end{itemize}
\end{BasicMatterBox}
```

- Add `画像・病理・検査所見の読み取り` only for image, pathology, or lab-value interpretation questions. Focus on findings that directly support the diagnosis or answer.
- In `解法の要点`, explain the essence of the question in 2 to 4 Japanese sentences. Make clear why the selected answer follows; do not only state a memorized fact. Do not use the old headings `概要/病態生理` or `正解の根拠` in new output.
- In `選択肢解説`, review choices in source order and include correct choices as well as incorrect choices unless there is a strong reason not to. Use `correct` for the response that answers the prompt and `wrong` for the others.
- Keep each option explanation concise. Do not restate the option text in prose, and do not waste a sentence on `この選択肢は正しい/誤りである` when the `○`/`×` already shows the judgment. Start with the reason, then add the necessary explanation of the disease, pathology, test, treatment, or term represented by that option.
- For positive-polarity questions, mark true answer choices as `correct` and explain the decisive reason they fit. For wrong choices, explain what they actually indicate and what clue would make them correct.
- For negative-polarity questions (`誤っているもの`, `適切でないもの`, etc.), mark the selected false/non-indicated statement as `correct` because it is the correct response to the prompt, and state clearly that the statement itself is false or inappropriate.
- Do not copy-paste the same generic sentence across options. Each option needs a specific, careful explanation.
- Never use vague option-review boilerplate such as `本問の決定的条件から外れる`, `示す病態・所見・処置に一致する内容へ置き換える必要がある`, or `別疾患・別部位・別段階の知識としては重要`. Replace it with concrete teaching: when that option would be correct, what disease/condition it describes, and which clue would indicate it.
- In `BasicMatterBox`, organize the surrounding knowledge needed to solve the problem as concise bullets. Emphasize CBT/national-board testable points, differences from similar diseases/findings/terms, and common exam traps. Keep all explanations in Japanese at medical-school CBT level; define difficult terms briefly and explain mechanisms/pathophysiology when useful.
- For image questions, explicitly connect the answer to visible findings.
- For old or guideline-sensitive exams, separate `試験上の正答` from current recommendations when needed.

## Research and Citation

- Verify medical claims before finalizing. Browse when recommendations, laws, statistics, guidelines, drugs, vaccines, or diagnostic criteria may have changed.
- Prefer official/public, society guideline, and primary/authoritative sources. Use source registries when helpful.
- For website sources, make the displayed page or document title itself a clickable link to its verified, specific URL (for example, \footnote{\href{URL}{ページ名}}). Keep the title visible instead of showing only a bare URL. Ensure hyperref is loaded; preserve the existing declaration or add it near the end of the preamble if absent. For non-web sources, use a concise source name. Do not invent guideline years, titles, or URLs.
- Use web research for explanations only, never to alter the original problem statement.

## LaTeX Safety

- Escape special characters in transcribed text: `& % _ $ # { } ~ ^ \`.
- Do not escape legitimate template commands.
- Keep environments and braces balanced.
- Avoid malformed `\footnote` and broken URLs.

## Compile Check

Run when available:

```powershell
lualatex -interaction=nonstopmode -halt-on-error output.tex
```

Before finalizing, confirm:

- all boxes exist and counts match the source
- no raw `\includegraphics`
- no absolute image paths and no visible filesystem paths
- no missing referenced figures
- no dropped question numbers or sections
- no unresolved `【判読不能】` unless reported
- no unsupported answer certainty
- bundled-template output uses `\ExplainHeading`, `\ChoiceExplanation`, and optional `BasicMatterBox`
