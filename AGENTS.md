# Inclusive-tag R(D) B2Note instructions

## Purpose

This repository contains the evolving Belle II B2Note for the inclusive-tag
R(D) analysis. The analysis is ongoing. Assume that every section,
number, plot, or method is preliminary.

## Source hierarchy

When sources disagree, use this precedence:

1. Explicit instructions in the current task.
2. The analysis repository's `docs/ANALYSIS_CONTEXT.md` at the pinned commit.
   The analysis repository is not vendored into this one (no submodule); it
   is referenced by commit SHA only, recorded in `CHANGELOG.md` and in each
   provenance block.
3. Current executable analysis code at the pinned commit.
4. Reference B2Notes in `docs/`, for organization and methodological
   examples only.  Their selections, correction factors, uncertainties and
   conclusions are never inputs to this analysis.
5. Inference.

Never silently resolve a disagreement. Report it and insert a marked TODO.

There is deliberately no separate manifest or results-registry file. A second
copy of the analysis state is a second thing to keep in sync, and it will
drift. Provenance lives next to the content it describes instead; see
"Provenance" below.

## Provenance

Every figure, table, or quoted number in the note carries a provenance
comment block immediately above it in the LaTeX source:

```latex
% PROVENANCE
%   status      : CODE_FACT | ANALYSIS_DECISION | VALIDATED_RESULT |
%                 PRELIMINARY_RESULT | PLANNED
%   produced-by : <path in the analysis repository>
%   commit      : <analysis commit SHA>
%   sample      : <data/MC scope, run period, channel>
%   selection   : <named selection or configuration>
%   corrections : <list>
\begin{figure}...
```

Sections whose claims all share one source may carry a single section-level
block at the top of the file instead.

`scripts/check_provenance.py` enforces this: it walks every `figure` and
`table` environment and fails if the block above it is missing or incomplete.
Run it before committing.

The pinned commit SHA is the single analysis-state anchor. `CHANGELOG.md`
records which analysis commit each note version corresponds to.

## Scientific safeguards

- Do not invent numerical results, efficiencies, yields, uncertainties,
  selections, correction factors, or software versions.
- Do not infer a nominal method from commented-out, deprecated, notebook-only,
  or exploratory code.
- Do not copy correction values from another Belle II analysis.
- Distinguish code facts from physics interpretation.
- Distinguish implemented, validated, planned, and superseded methods.
- Treat signal-region data as blinded unless the task explicitly says otherwise.
- Preserve the distinction between family normalization and internal decay
  composition in generic-BB background modeling.
- Do not require the generic-BB reweighting to preserve the inclusive B decay
  rate. The data/MC normalization genuinely differs in the tuning region, and
  forcing the total to stay fixed would push that discrepancy into the
  composition, which is the quantity being measured. Require instead that the
  resulting normalization change be validated in an independent region.
- Check that truth categories are mutually exclusive and exhaustive.
- Check for double application of corrections or overlapping MC samples.

## Writing conventions

- Use stable labels for every section, figure, table, and equation.
- Put detailed diagnostic plots and large tables in appendices.
- State the dataset, channel, run period, selection, weight configuration,
  and source commit for every numerical result.
- Use \AnalysisTBD{} for missing content, \PreliminaryResult{} for non-final
  values, \InProgress{} for known-incomplete work actively being addressed,
  and \Superseded{} for retained but obsolete material.
- Do not remove TODO markers without evidence that the item is resolved.

## Workflow

Before editing:

1. Read relevant analysis files.
2. Report discrepancies or missing inputs.
3. Propose the exact sections and files to change.
4. Edit only after the scope is clear.

After editing:

1. Compile the note.
2. Check for undefined references, missing citations, and LaTeX warnings.
3. Review the diff for numerical or scientific claims not tied to a source.
4. Summarize changed claims and their provenance.