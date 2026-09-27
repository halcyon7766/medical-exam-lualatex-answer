# Medical Exam LuaLaTeX Answer

日本語の医学系試験を、LuaLaTeX で組版できる解答・解説冊子にまとめる Codex Skill です。Markdown、テキスト PDF、スキャン PDF、ページ画像を入力として扱います。

## 主な機能

- 設問、選択肢、表、図の対応を保ちながら、読みやすい日本語の解答・解説冊子を作成
- スキャン PDF や複雑なレイアウトでは YomiToku を使った OCR・図表抽出を支援
- 科目に合わせた色テーマ付きの LaTeX テンプレートを同梱
- 医学的な根拠を確認し、ウェブ資料はページ名や資料名をクリックできるリンクとして引用
- 解答・解説の体裁や画像参照などを確認する補助スクリプトを同梱

## 対応入力と出力

対応入力は Markdown、PDF、スキャン PDF、ページ画像です。出力は編集可能な <code>.tex</code> ファイルと、LuaLaTeX でコンパイルした PDF を想定しています。

## 必要な環境

- Codex の Skills に対応した環境
- LuaLaTeX と日本語フォント（同梱テンプレートは Noto Sans CJK JP、Noto Sans JP、IPAexGothic を順に探します）
- スキャン資料の OCR を行う場合は YomiToku CLI
- 同梱スクリプトを使う場合は Python 3

PDF の文字抽出やページ画像化には <code>pdftotext</code>、<code>pdfinfo</code>、<code>pdftoppm</code> などの Poppler ツールを利用できます。これらは OCR や PDF の確認が必要な場合に使います。

## インストール

GitHub リポジトリを Codex の Skills ディレクトリにクローンします。<code>OWNER/REPOSITORY</code> は公開先に合わせて置き換えてください。

### Windows PowerShell

~~~powershell
$skills = if ($env:CODEX_HOME) {
  Join-Path $env:CODEX_HOME 'skills'
} else {
  Join-Path $env:USERPROFILE '.codex\skills'
}
New-Item -ItemType Directory -Force -Path $skills | Out-Null
git clone https://github.com/OWNER/REPOSITORY.git (Join-Path $skills 'medical-exam-lualatex-answer')
~~~

### macOS / Linux

リポジトリを <code>$CODEX_HOME/skills/medical-exam-lualatex-answer</code> に配置します。<code>CODEX_HOME</code> が未設定なら、<code>~/.codex/skills/medical-exam-lualatex-answer</code> を使います。

インストール後、Codex で <code>$medical-exam-lualatex-answer</code> を呼び出してください。Skill が認識されない場合は Codex を再起動してください。

## 使い方

試験ファイルを添付し、たとえば次のように依頼します。

~~~text
$medical-exam-lualatex-answer
添付した試験PDFから、問題文・選択肢を再現した解答・解説冊子を作ってください。
~~~

スキャン PDF では原ページ画像を照合し、OCR の曖昧さや判読不能箇所を明示します。公式解答や採点基準が提供されている場合はそれらを優先します。診断基準、治療指針、薬剤、統計など更新されうる医学情報は、必要に応じて信頼できる一次情報・公式情報で確認します。

## 同梱スクリプト

### YomiToku OCR

~~~powershell
python scripts/run_yomitoku_ocr.py path/to/exam.pdf --device cpu --lite
~~~

既定では Markdown、JSON、HTML の OCR 出力を入力ファイルの隣に作成します。出力先や形式は <code>--outdir</code>、<code>--formats</code> で指定できます。YomiToku が必要です。

### LaTeX 出力の確認

~~~powershell
python scripts/validate_answer_tex.py path/to/answer.tex --expected 20
lualatex -interaction=nonstopmode -halt-on-error path/to/answer.tex
~~~

<code>--expected</code> には設問数を指定します。検証スクリプトは各設問のボックス数、画像参照、旧式の解説記法、ファイルパスなどを確認します。PDF の組版確認には LuaLaTeX を実行してください。

## ファイル構成

~~~text
medical-exam-lualatex-answer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── mdAnswer_example.tex
├── references/
│   ├── answer-explanation-policy.md
│   ├── color-patterns.md
│   ├── medical-sourcing.md
│   ├── pdf-yomitoku-workflow.md
│   ├── strict-output-contract.md
│   ├── subject-theme-map.md
│   └── source-registries/
└── scripts/
    ├── run_yomitoku_ocr.py
    └── validate_answer_tex.py
~~~

## プライバシーと資料の取り扱い

この Skill の配布ファイルには、実際の試験原本、生成済み解答、特定大学名、個人名、連絡先を含めていません。テンプレートの学年・担当欄は汎用の編集用プレースホルダーです。

試験 PDF、画像、OCR 結果、生成した解答ファイルには、著作権で保護された内容や個人情報が含まれる場合があります。公開リポジトリには追加せず、資料の利用・共有権限を確認して管理してください。

## 医学情報について

この Skill は試験学習用の解答・解説の作成を支援します。生成された内容は、臨床上の診断・治療判断の代替ではありません。最新の推奨や法令を扱う場合は、該当する公式情報を確認してください。