---
name: medical-exam-lualatex-answer
description: "日本語の医学系試験全般（基礎医学、臨床医学、社会医学、公衆衛生、看護・医療系科目を含む）のMarkdown、PDF、スキャンPDF、ページ画像を、LuaLaTeXでコンパイル可能な解答・解説冊子に変換する。設問、選択肢、表、図を漏れなく再現し、科目別カラーテーマ、根拠付き医学解説、引用、画像所見に基づく考察を追加する。日本語のスキャンPDFやレイアウトが複雑なPDFでは、作成前にYomiTokuでOCR、図表抽出、レイアウト解析を行う。"
---

# Medical Exam LuaLaTeX Answer

日本語の医学系試験ファイルを、LuaLaTeXでコンパイルできる単一の解答・解説冊子に変換する。対象はMarkdown、テキストPDF、スキャンPDF、ページ画像。既定テンプレートは `assets/mdAnswer_example.tex`。

## Core Workflow

1. 入力を判定する。
   - Markdown: 直接読む。
   - テキストPDF: 抽出テキストの読み順を確認する。
   - スキャンPDF、図表が多いPDF、日本語レイアウトが複雑なPDF、ページ画像: [references/pdf-yomitoku-workflow.md](references/pdf-yomitoku-workflow.md) に従い、YomiTokuでOCR、図表抽出、レイアウト確認を行う。
2. ソース索引を作る: セクション、設問、選択肢、表、画像、判読不能箇所。
3. テンプレートを解決する: ユーザー提供のスタイル見本を優先し、なければ `assets/mdAnswer_example.tex` を使う。テンプレート未提供で停止しない。
4. 科目名を推定して `\SetExamSubject{...}` で設定する。推定順と色テーマは [references/subject-theme-map.md](references/subject-theme-map.md) を使い、色値は [references/color-patterns.md](references/color-patterns.md) に従う。
5. 出力前に [references/strict-output-contract.md](references/strict-output-contract.md) を読む。
6. 解答・解説方針は [references/answer-explanation-policy.md](references/answer-explanation-policy.md) を使う。医学情報の確認と引用は [references/medical-sourcing.md](references/medical-sourcing.md) と必要な source registry を使う。ウェブサイトを根拠に示す場合は、ページ名・資料名自体をリンクにする。
7. 画像依存問題では、抽出図だけでなく元ページ文脈も確認する。見えた所見を `解法の要点` と `選択肢解説` に反映する。
8. 設問数が多い、OCRを使う、抽出図表がある場合は、再現可能な `generate_<exam>_answer.py` で `.tex` を生成する。
9. `lualatex -interaction=nonstopmode -halt-on-error output.tex` でコンパイルし、エラーを修正する。
10. `scripts/validate_answer_tex.py` でbox数、画像参照、生の `\includegraphics`、LaTeX致命エラー、判読不能表示を検査する。

## Output Requirements

- 元資料の設問順、設問番号、指示文、選択肢、表、画像の対応関係を保つ。ただし問題文は元資料の改行位置を機械的に再現せず、読み取った文を自然な段落・句読点・LaTeX上読みやすい形式に整える。意味を変える要約はしない。
- OCR本文の代替として全問に元ページ画像を貼らない。問題文・選択肢・表は本文として整形して記載し、ページ全体または切り出し画像は画像・図表依存問題、OCR判読不能箇所の照合、レイアウト保持が必要な場合に限って添える。
- 各設問に `QuestionBox`、`AnswerBox`、`ExplanationBox` を1つずつ置く。
- 多肢選択は `ChoiceList` を使い、`2つ選べ`、`誤っているもの`、`禁忌` などの指示を回答に反映する。
- 解説は原則として `画像・病理・検査所見の読み取り`（画像・病理・検査値問題のみ）、`解法の要点`、`選択肢解説`、`基本事項` の構成にする。
- `画像・病理・検査所見の読み取り` では、画像や検査値から診断に直結する所見を中心に何が読み取れるかを説明する。画像・病理・検査値を読ませる問題でない場合はこの見出しを省略する。
- `解法の要点` では、この問題で問われている本質を2〜4文で説明し、単なる暗記ではなく「なぜその選択肢になるのか」が分かるようにする。
- `選択肢解説` では正答も誤答も原則として全選択肢を扱い、正答には `○`、誤答には `×` を付ける。選択肢本文の再記載や「〜だから正しい」のような冗長な言い換えを避け、正しい理由・誤りである理由を最初に簡潔に述べ、その選択肢が指す疾患・病態・検査・治療・用語について必要な解説を補う。誤答では、必要に応じて「これは〇〇でみられる」「△△と混同しやすい」のように補足する。
- `基本事項` では、この問題を解くために必要な周辺知識をCBT・国試で問われやすいポイント中心に箇条書きで整理する。似ている疾患・所見・用語との違い、試験で間違えやすいポイントを明確にする。
- 解説は医学部CBTレベルの日本語で書く。専門用語は使ってよいが、難しい用語には意味が分かる補足を入れ、暗記だけでなく機序・病態から理解できるようにする。過度に冗長にせず、試験直前に読み返しやすい密度にする。
- 新規作成では `\ExplainHeading`、`\ChoiceExplanation`、`BasicMatterBox`、`\BasicMatterTitle`、`\ExamFigure` を使う。旧 `OptionReviewTable`、`\OptionReview`、`PearlBox` は新規出力では使わない。
- 画像は `.tex` と同じディレクトリに置き、basenameだけを `\SafeIncludeGraphics` または `\ExamFigure` で参照する。絶対パスと生の `\includegraphics` は使わない。PDF本文、キャプション、欠落画像プレースホルダーにも画像パスを表示しない。
- 表はYomiTokuのHTML/CSV/JSON/Markdownを元ページ画像と照合し、全セルを再現する。
- 公式解答、採点基準、講義資料がある場合は一般医学知識より優先する。年度差がある内容は、試験上の正答と現在の補足を分ける。解説で用いたウェブサイトは、ページ名・資料名を該当ページへのクリック可能なリンクとして示す。
- 検査値、単位、基準範囲、計算過程は元の表記と有効数字を保つ。
- OCRの明らかな誤字・脱字・文字化けは、文脈または元ページ画像から一意に判断できる場合に修正する。医学的内容・数値・選択肢の意味が変わりうる場合は勝手に補正せず、`【判読不能】` または注記で曖昧さを残す。根拠不足、画像欠落、OCR曖昧箇所は明示し、必要なら `不明（根拠不足）` を使う。
- 科目ごとの見た目は `\SetExamSubject{...}` とテンプレートの `\ApplySubjectColorTheme` だけで変える。本文やboxに個別色を直書きしない。

## Subject and Source Selection

科目推定順:

1. ユーザー指定
2. 表紙、ヘッダー、フッター、試験名欄
3. ファイル名
4. 親フォルダ名
5. 設問内容
6. 不明または混合なら `医学一般`

source registry:

- `references/source-registries/general-medicine.md`
- `references/source-registries/basic-medicine.md`
- `references/source-registries/internal-medicine.md`
- `references/source-registries/surgery.md`
- `references/source-registries/specialties.md`
- `references/source-registries/public-health.md`

## YomiToku Output Layout

スキャンPDFでは、原則として次の構成にする。

```text
<exam>_assets/
  yomitoku/
    md/
    json/
    html/
    figures/
    vis/
  generate_<exam>_answer.py
  <exam> 解答解説.tex
  <exam> 解答解説.pdf
```

`scripts/run_yomitoku_ocr.py` が使える場合は、Markdown/JSON/HTML、図表抽出、可視化を一括実行する。

## Final Check

- 全設問に `QuestionBox`、`AnswerBox`、`ExplanationBox` がある。
- `\maketitle`、`\tableofcontents`、`\newpage` の順序が残っている。
- `\SetExamSubject{...}` または `\ExamSubject` と科目色テーマが妥当。
- 選択肢数、正答数、否定問題の極性が一致している。
- 図表、検査値、単位、引用、脚注、画像ファイルが破綻していない。
- YomiToku出力と元ページ画像を照合した。
- LuaLaTeXで清潔にコンパイルできる。
