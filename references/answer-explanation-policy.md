# Answer and Explanation Policy

Use this when deciding answers and writing explanations. It consolidates subject tuning, answer heuristics, exam-date handling, labs, figures, question formats, evidence strength, and official-answer priority.

## Evidence Order

Resolve answers in this order:

1. official answer, rubric, or model answer
2. course handout, lecture slide, teacher comment, or local syllabus
3. original problem text, table, and visible image findings
4. guideline, law, classification, or system valid at the exam date
5. current authoritative medical source
6. stable medical mechanism or clinical inference

If these conflict, put the exam answer in `AnswerBox` and explain the difference as `試験上は...` vs `現在の補足として...`. Use `不明（根拠不足）` only when the source is insufficient to answer safely.

## Question Format

- `正しいもの`: choose statements matching the exact disease, stage, population, or mechanism.
- `誤っているもの` / `適切でないもの`: answer the false or non-indicated option and restate the polarity in the explanation.
- `2つ選べ` / `3つ選べ`: keep the requested answer count and list every correct letter.
- `最も`: choose the best, most common, first-line, or most urgent option, not merely a possible option.
- `まず行う`: prioritize ABCDE, stabilization, standard sequence, and safety.
- `禁忌`: choose the action to avoid in the stated condition, even if useful elsewhere.
- Combination questions: preserve both component choices and final combination choices; explain both levels.
- Calculations: preserve units and conditions, show the formula, and round according to the prompt.
- Fill-in/descriptive: give a compact model answer with required scoring terms; note common acceptable synonyms when useful.

## Explanation Structure

Use this three-part structure in every `ExplanationBox` unless the user asks otherwise:

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
  \end{itemize}
\end{BasicMatterBox}
```

`画像・病理・検査所見の読み取り` is optional and should appear only for image, pathology, or lab-value interpretation questions. Explain what can be read from the image or values, focusing on findings that directly support the diagnosis or answer.

`解法の要点` explains the essence of the question in 2 to 4 Japanese sentences. It should make clear why the answer follows, not merely state a memorized fact. Use mechanism and pathophysiology when they help understanding.

`選択肢解説` reviews the choices in source order. Include the correct option as well as incorrect options unless there is a strong reason not to. Mark correct options with `correct` and incorrect options with `wrong`; the template renders these as `○` and `×`. For multiple-answer questions, mark every correct option with `correct`. For negative-polarity questions such as `誤っているもの` or `適切でないもの`, the exam answer is the false/non-indicated option; mark that selected answer as `correct` because it is the correct response to the prompt, and explicitly say that the statement itself is false or inappropriate.

Each option explanation should be concise and explanatory, not a restatement of the option. Do not begin by repeating the option text in prose, and avoid filler such as `この選択肢は正しい` or `この選択肢は誤りである` when the symbol already shows the judgment. Start with the reason: the key definition, mechanism, finding, exception, or mismatch. Then add one short teaching point about the disease, pathology, test, treatment, or term represented by that option.

Preferred shape:

```tex
\ChoiceExplanation{b}{correct}{脂肪変性}{肝細胞内の白く抜けた空胞は脂肪滴に相当する。アルコール性肝障害やNAFLDでみられる可逆的変化である。}
\ChoiceExplanation{c}{wrong}{硝子様変性}{硝子様変性はHE染色で均質な好酸性物質としてみえる変化で、脂肪滴の空胞形成とは異なる。動脈硬化や糖尿病性細動脈硬化で問われやすい。}
```

`基本事項` is optional. Add it when the problem naturally supports reusable learning such as definitions, classifications, mechanisms, image/pathology findings, criteria, treatment rules, contraindications, or a compact table/list. Omit it when it would merely repeat `解法の要点` or the option explanations.

Avoid copy-pasted generic explanations in all sections; each explanation should be specific and useful for future questions.

Forbidden generic option-review phrasing:

- `本問の決定的条件から外れる`
- `正しくするには、...が示す病態・所見・処置に一致する内容へ置き換える必要がある`
- `別疾患・別部位・別段階の知識としては重要だが、この設問の答えにはならない`

Instead, name the concrete concept behind the option and give a usable correction. A good incorrect-option explanation answers at least one of these:

- What disease, hormone, drug, anatomy, pathogen, imaging finding, or procedure does this option actually describe?
- What stem would make this option correct?
- Which lab pattern, symptom, image sign, age group, stage, or treatment indication would point to this option?
- What is the exam trap or common confusion?

Example: do not write `副甲状腺ホルモンは本問の決定的条件から外れる`. Write the useful version: `副甲状腺ホルモンが正解になるのは、低Ca刺激や原発性/続発性副甲状腺機能亢進症、骨吸収促進、腎でのCa再吸収増加・P再吸収低下、活性型ビタミンD産生促進が問われる場合である。本問がインスリン、甲状腺ホルモン、ADHなど別の内分泌軸を示す所見ならPTHは合わない。`

Subject emphasis:

- Basic medicine: definitions, anatomy, pathways, feedback, mechanisms, histology, molecular links.
- Pharmacology: target, mechanism, PK, adverse effects, contraindications, interactions, antidotes.
- Pathology/microbiology/immunology: morphology or organism, mechanism, diagnostic test, clinical correlation.
- Clinical medicine: age, time course, vital signs, lab pattern, imaging, diagnostic criteria, severity, treatment.
- Surgery/emergency: initial stabilization, indication, contraindication, operative/procedural logic, complications.
- Pediatrics: age-specific normals, development, vaccination, congenital disease, family/social context.
- Obstetrics/gynecology: gestational age, maternal/fetal risk, contraindicated drugs, monitoring, delivery timing.
- Psychiatry: diagnostic criteria, duration, exclusion, risk assessment, therapy, legal/safety points.
- Radiology: modality, window/sequence, density/signal, contrast pattern, anatomy, differential.
- Public health/social medicine: exam year, law/program, denominator, rate/risk/odds, bias, notification category.

## Basic Matter

Use `基本事項` to add exam-useful knowledge beyond the immediate answer. Do not repeat the same sentence as `解法の要点`.

Default format:

```tex
\begin{BasicMatterBox}
  \BasicMatterTitle{基本事項}
  \begin{itemize}[leftmargin=1.2em]
    \item ...
    \item ...
    \item ...
  \end{itemize}
\end{BasicMatterBox}
```

Write `基本事項` mainly as concise bullets. Organize the surrounding knowledge needed to solve the problem, especially points commonly tested in CBT and national board-style exams. Include differences from similar diseases, findings, or terms, and make common exam traps explicit. For very simple one-step questions, keep this short or omit it if it would only repeat the explanation.

All explanations must be in Japanese at medical-school CBT level. Difficult medical terms are acceptable, but add enough context for the meaning to be clear. Keep the density useful for last-minute review: concise, mechanism-aware, and not overly verbose.

Good `基本事項` topics include:

- definition or classification that anchors the concept
- diagnostic criterion, threshold, required duration, staging, severity, or scoring point
- decisive image finding, waveform pattern, lab combination, pathology phrase, or physical sign
- common look-alike and the clue that separates it
- first-line treatment, next step, contraindication, emergency action, or follow-up
- mechanism that explains a symptom, lab, adverse effect, or complication
- exam-date note for older guideline, law, vaccine schedule, diagnostic category, or public health rule
- age/context note for pediatrics, pregnancy, renal/hepatic impairment, immunosuppression, or frailty

Subject-specific priorities:

- Basic medicine: pathway rate-limiting steps, innervation/blood supply, receptor/enzyme, stain, mutation, organism feature.
- Clinical medicine: diagnostic criteria, red flags, first-line test, first-line therapy, complications, monitoring.
- Surgery/emergency: initial action, timing, operative indication, contraindication, complication, perioperative risk.
- Pediatrics: age-dependent normals, developmental milestones, congenital patterns, vaccine timing, abuse/safety red flags.
- Obstetrics/gynecology: gestational week thresholds, teratogenic drugs, fetal monitoring clues, delivery indications.
- Psychiatry: duration criteria, exclusion criteria, suicide/violence risk, capacity/consent, medication adverse effects.
- Radiology/pathology: modality/stain, named sign, distribution, key negative, classic differential.
- Public health: denominator, bias, law/reporting category, screening index, prevention level, exam-year system.

Avoid vague bullets such as `鑑別が重要である`. Make each item usable for a future exam answer.

## Exam-Date and Current Guidance

Check dates for guidelines, diagnostic criteria, vaccine schedules, drug indications, legal systems, statistics, and public health programs. Prefer the exam-date rule for the exam answer; add current guidance only as a clearly separated supplement.

## Labs, Units, and Tables

- Preserve source units, significant figures, table cells, and reference ranges.
- Use source-provided reference ranges before general ranges.
- Do not apply adult defaults to pediatric, neonatal, pregnancy, renal, hepatic, or endocrine contexts without checking.
- Convert units only when useful; keep the original value visible.
- Interpret patterns, not isolated values: acid-base/electrolytes, CBC, renal, liver, endocrine axes, coagulation, ABG, drug levels.
- If local ranges are absent, use cautious wording such as `一般に` or `代表的には`.

## Images and Figures

- Inspect available local images, extracted figures, and page context before answering image-dependent questions.
- Visible findings override filename hints and generic disease probability.
- For radiology, state modality/sequence, side, distribution, density/signal, contrast, and key negatives when relevant.
- For microscopy/pathology, state magnification/stain if available, architecture, cell type, atypia, necrosis, inflammation, and distribution.
- For ECG/waveforms/graphs, state axis labels, scale, rhythm/intervals, trend, and the physiologic relation being tested.
- Put question-critical figures immediately under the question, not only in the explanation.

## Confidence

Use confidence internally:

- High: official/course source or decisive problem clue agrees with medical knowledge.
- Medium: defensible inference but no official key, or minor ambiguity remains.
- Low: OCR ambiguity, missing image, absent condition, guideline-date conflict, or ambiguous options affect the answer.

Only show uncertainty when it affects reliability. Do not state unseen image findings, invented citations, or unsupported guideline years.
