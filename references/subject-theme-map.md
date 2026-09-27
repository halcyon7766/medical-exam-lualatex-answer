# Subject Theme Map

Use this reference when inferring `\ExamSubject` and choosing the subject color theme. Palette values are stored in [color-patterns.md](color-patterns.md).

## Inference Priority

1. Explicit user instruction
2. Cover, header, footer, or subject field in the source
3. File name
4. Parent folder name
5. Question content
6. `医学一般` when uncertain or mixed

Preserve the visible source subject text in transcription. Normalize only the document metadata value used in `\ExamSubject`.

## Standard Subjects and Colors

| Group | Standard `\ExamSubject` | Variants | Color |
|---|---|---|---|
| General | 医学一般 | 医学総論, 総合医学, 医療系総合 | SkyBlue |
| General | 症候学 | 症候・病態学, 症候・病態学演習 | SlateGray |
| General | 検査診断学 | 臨床検査医学, 診断学 | Gold |
| Basic | 解剖学 | 解剖学I, 解剖学II | Brown |
| Basic | 組織細胞生物学 | 組織学, 発生学, 遺伝学 | Purple |
| Basic | 生理学 | 生理学I, 生理学II | SkyBlue |
| Basic | 生化学 | 生化学I, 生化学II, 分子生物学 | Gold |
| Basic | 薬理学 | 薬理学I, 薬理学II | Orange |
| Basic | 病理学 | 病理学総論, 病理学各論 | Brown |
| Basic | 微生物学 |  | Teal |
| Basic | 免疫学 |  | Emerald |
| Basic | 寄生虫学 |  | Lime |
| Basic | 法医学 |  | Brown |
| Internal | 内科学 | 内科, 総合内科学 | Navy |
| Internal | 循環器病学 | 循環器内科学, 循環器内科 | Red |
| Internal | 呼吸器病学 | 呼吸器内科学, 呼吸器内科 | Teal |
| Internal | 消化器病学 | 消化器内科学, 消化器内科 | Emerald |
| Internal | 腎臓病学 | 腎臓内科学, 腎臓内科 | Navy |
| Internal | 内分泌・代謝病学 | 内分泌代謝学, 糖尿病・内分泌代謝内科 | Orange |
| Internal | 血液学 | 血液内科学 | Magenta |
| Internal | 腫瘍学 | 腫瘍・血液学 | Red/Magenta |
| Internal | 感染症学 | 感染症内科学 | Emerald |
| Internal | 膠原病学 | リウマチ・膠原病学 | Purple |
| Internal | 神経内科学 | 脳神経内科学, 脳神経病学 | Navy |
| Surgery | 外科学 | 外科, 一般外科学, 消化器外科学 | Red |
| Surgery | 整形外科学 |  | Emerald |
| Surgery | 麻酔科学 |  | Orange |
| Surgery | 救急医学 | 救命救急医学, 集中治療医学 | Red |
| Surgery | リハビリテーション医学 |  | Lime |
| Specialty | 小児科学 | 小児医学, 小児科 | SkyBlue |
| Specialty | 産婦人科学 | 産科婦人科学, 産婦人科, 産科学, 婦人科学 | Magenta |
| Specialty | 精神医学 | 精神科 | Purple |
| Specialty | 皮膚科学 | 皮膚科, 皮膚・形成外科学 | Brown |
| Specialty | 眼科学 | 眼科 | SkyBlue |
| Specialty | 耳鼻咽喉科学 | 耳鼻咽喉科, 頭頸部病学 | Teal |
| Specialty | 泌尿器科学 | 泌尿器科 | Navy |
| Specialty | 放射線医学 | 放射線科学, 放射線科 | SlateGray |
| Social | 公衆衛生学 | 社会医学, 衛生学, 疫学 | Lime |
| Social | 医療情報学 | 医療情報社会学 | SlateGray |
| Social | 医療倫理学 |  | Navy |
| Social | 医療安全学 |  | SlateGray |
| Healthcare | 看護学 |  | SkyBlue |
| Healthcare | 保健学 |  | Lime |

## Layout Rule

Only the color theme should vary by subject. Set the subject with `\SetExamSubject{...}` so the theme is reapplied after subject changes. Keep the same `QuestionBox`, `AnswerBox`, `ExplanationBox`, `ExplainHeading`, `\ChoiceExplanation`, and `BasicMatterBox` layout across all subjects.
