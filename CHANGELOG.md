# Change log

Each released version of the note is pinned to an analysis commit in
`zjkjsd/inclusive_R_D`, tracked here and by the `external-code` submodule.

## Version 0.1 (draft) — unreleased

Pinned analysis commit: `dd520a5` ("start tracking gitignore").

First structured draft. The note previously consisted of the unmodified
Belle II note template.

Added:
- Section 7.6 (Constraining power of the tuning region): all eight stored
  BBbar fits sit on a parameter bound, always on an unmeasured n-body weight
  and never on the measured-hadronic weight, with unmeasured-family
  correlations of 0.64-0.93. Argues that the tuning region cannot separate
  the unmeasured families, and marks the scan that would confirm it.
- Section 8 (Signal Extraction), documenting the generated workspace and the
  decision to constrain rather than float the generic-BBbar normalisations.
- Section 3 (Event Reconstruction), drafted from
  `Recon_scripts/2_Reconstruction.py`, with a complete cut-to-code table.
- Section 4 (Truth Classification), drafted from
  `utilities.classify_mc_dict()`, including an explicit exclusivity and
  exhaustiveness discussion.
- Skeletons with stable labels for Sections 1, 2, 5–12 and four appendices.
- Result-status macros `\AnalysisTBD`, `\PreliminaryResult`, `\Superseded`,
  `\InProgress`.
- The provenance convention and `scripts/check_provenance.py`.
- Sections 2 and 6 filled in: ntuple layout, the generic-MC luminosity
  factor and its scope, and the fake-D single-application rule.

Changed:
- `note.tex` now typesets `body.tex`, not the template's `instructions.tex`.
- `AGENTS.md`: source hierarchy no longer refers to a manifest or results
  registry (see the Provenance section for what replaced them); the
  "preserve the inclusive B decay rate" safeguard was removed as unphysical
  for this analysis.
- `docs/ANALYSIS_CONTEXT.md` removed; the analysis repository's copy, reached
  through the submodule, is the single source.

Removed:
- Journal drivers and template scaffolding not used by a B2Note
  (`prd.tex`, `prl.tex`, `jhep.tex`, `epjc.tex`, `draft.tex`, `pacs.tex`,
  `svjour.cls`, `svepj.clo`, `jheppub.sty`, `JHEP.bst`, `wordcount.*`,
  `create_paper`, `addref`, template fork screenshots, Jupyter checkpoints).

Overleaf helpers (`update`, `connect_overleaf`, `sync_from_overleaf`) are
retained.
