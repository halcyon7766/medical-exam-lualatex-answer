# Medical Sourcing

Use this reference to keep citations current, authoritative, and efficient.

## Source Priority

Prefer sources in this order:

1. Japanese government and public-health pages for law, statistics, vaccination, notification, and public programs.
2. Japanese academic society guidelines and official guideline PDFs.
3. International guideline bodies when Japanese guidance is unavailable or not current.
4. Peer-reviewed reviews or major institutional references for stable disease mechanisms.
5. Tertiary summaries only when no better source is practical, and never for unstable recommendations.

## What Must Be Rechecked

Always browse for:

- guidelines, diagnostic criteria, treatment algorithms, resuscitation algorithms
- vaccination schedules, contraindications, and public funding rules
- epidemiology, survival rates, population statistics, child abuse statistics
- disease definitions that have changed in DSM/ICD or guideline revisions
- medication indications, emergency dosing, and contraindications

## Efficient Reuse

- Reuse the same authoritative source across related questions when it supports the claim.
- Keep a small citation registry in the generator script or notes, keyed by topic, for repeated footnotes.
- Do not attach a source to a claim it does not actually support.

## Citation Style

For website sources, make the displayed page or document title itself a clickable link to the verified, specific source URL. Keep the source name visible in the PDF; do not show only a bare URL or leave the website title unlinked. When the source name appears in explanation text, link that name directly. When citing in a footnote, make the displayed title the link text as well. Prefer the exact page or document over a site homepage.

The template already loads hyperref. If a user-provided template does not, add \usepackage{hyperref} near the end of its preamble, checking for an existing declaration first. Keep printed link text readable, and use a LaTeX-safe/percent-encoded URL when needed. For non-web sources, a plain source name remains appropriate.

Use concise LaTeX footnotes:

```tex
\footnote{\href{https://example.jp/guideline.pdf}{表示するページ名}}
```

Link the source name inline when citing it in the explanation text:

```tex
\href{確認済みURL}{表示するページ名}
```

Do not invent guideline years, publication titles, or URLs.
