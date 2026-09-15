# Belle II note: inclusive-tag $R(D^{\pm})$

The Belle II internal analysis note for the inclusive-tagging measurement of
$R(D^{\pm})$, using $B^{0} \to D^{-} \ell^{+}$ with
$D^{-} \to K^{+} \pi^{-} \pi^{-}$ and a rest-of-event tag side.

**The analysis is ongoing. Every section, number, plot and method in this
note is preliminary.**

## Building

```bash
make note          # -> note.pdf
make clean
```

Requires a LaTeX installation with `latexmk`. On Overleaf the project builds
from `note.tex` with no extra configuration.

## Layout

| Path | Purpose |
|---|---|
| `note.tex` | Document driver: title page, TOC, `body.tex`, bibliography, appendices |
| `body.tex` | Inputs the numbered sections in order |
| `sections/` | One file per section, plus appendices |
| `definitions.tex` | Packages, macros, and the result-status macros |
| `figures/` | Figures, organised by section |
| `docs/` | Reference B2Notes from other analyses, and the note outline |
| `scripts/check_provenance.py` | Enforces the provenance convention |
| `CHANGELOG.md` | Note version to analysis commit mapping |

## Before editing

Read `AGENTS.md`. The two rules that matter most:

1. **Nothing is written as prose unless it has a source.** Missing content
   gets `\AnalysisTBD{what is missing}`, not an invented value.
2. **Every figure, table and number carries a provenance block.** Run
   `python3 scripts/check_provenance.py` before committing.

The analysis repository's `docs/ANALYSIS_CONTEXT.md` at the pinned commit is
the single source for the analysis strategy. It is not vendored into this
repository (no submodule); the analysis repository is referenced by commit
SHA only, recorded in `CHANGELOG.md` and in each provenance block. Do not
copy it into this repository.

To move the note to a newer analysis commit, record the new commit in
`CHANGELOG.md` and check which sections' claims are affected before
rewriting anything.

## Overleaf

`connect_overleaf <overleaf-git-url>` links the project; `sync_from_overleaf`
pulls Overleaf edits and pushes them here. `update` refreshes the Belle II
author list and template files.
