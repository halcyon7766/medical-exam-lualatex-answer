# Color Patterns

Use these palettes for subject color themes. Keep layout fixed; only the theme colors change by subject.

| Set | Name | Macro | primaryColor | boxBgProblem | boxFrameProblem | boxBgAnswer | boxFrameAnswer | boxBgExplain | boxBarExplain |
|---:|---|---|---|---|---|---|---|---|---|
| 01 | Sky Blue | `\UseColorSetSkyBlue` | `0078C8` | `FFFFFF` | `000000` | `EBF5FF` | `B4E1FF` | `F5F5F5` | `646464` |
| 02 | Teal | `\UseColorSetTeal` | `0096A0` | `FFFFFF` | `000000` | `EBFAFA` | `B4EBEE` | `F5F5F5` | `646464` |
| 03 | Emerald | `\UseColorSetEmerald` | `00965A` | `FFFFFF` | `000000` | `ECFAF2` | `B9F0D2` | `F5F5F5` | `646464` |
| 04 | Lime | `\UseColorSetLime` | `5AAA00` | `FFFFFF` | `000000` | `F5FCEB` | `DCF5BE` | `F5F5F5` | `646464` |
| 05 | Purple | `\UseColorSetPurple` | `785AC8` | `FFFFFF` | `000000` | `F5F0FF` | `DCCDFA` | `F5F5F5` | `646464` |
| 06 | Magenta | `\UseColorSetMagenta` | `C83C96` | `FFFFFF` | `000000` | `FFEEFA` | `FAC8EB` | `F5F5F5` | `646464` |
| 07 | Orange | `\UseColorSetOrange` | `E67800` | `FFFFFF` | `000000` | `FFF4EB` | `FFD7B4` | `F5F5F5` | `646464` |
| 08 | Red | `\UseColorSetRed` | `DC3C3C` | `FFFFFF` | `000000` | `FFEEEE` | `FFC8C8` | `F5F5F5` | `646464` |
| 09 | Brown | `\UseColorSetBrown` | `AA643C` | `FFFFFF` | `000000` | `FCF5F0` | `EBD2C3` | `F5F5F5` | `646464` |
| 10 | Slate Gray | `\UseColorSetSlateGray` | `5A6E82` | `FFFFFF` | `000000` | `F2F6FA` | `D2DCE6` | `F5F5F5` | `646464` |
| 11 | Navy | `\UseColorSetNavy` | `1E46A0` | `FFFFFF` | `000000` | `ECF2FF` | `BED2FF` | `F5F5F5` | `646464` |
| 12 | Gold | `\UseColorSetGold` | `C89600` | `FFFFFF` | `000000` | `FFFAEB` | `FFEBA0` | `F5F5F5` | `646464` |

## Usage Rules

- Use only these palette macros for bundled-template subject themes.
- Do not hard-code colors in individual `QuestionBox`, `AnswerBox`, `ExplanationBox`, `\ChoiceExplanation`, or `BasicMatterBox` content.
- If adding a new subject, map it to the nearest existing palette in `\ApplySubjectColorTheme` and document it in `subject-theme-map.md`.
- Keep `boxBgProblem` white and `boxFrameProblem` black unless the user explicitly asks for a full redesign.
- Keep `boxBgExplain` and `boxBarExplain` stable across subjects so long explanations remain readable.
