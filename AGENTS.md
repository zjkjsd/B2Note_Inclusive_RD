# Inclusive-tag R(D) B2Note instructions

## Purpose

This repository contains the evolving Belle II B2Note for the inclusive-tag
R(D) analysis. The analysis is ongoing. Assume that every section,
number, plot, or method is preliminary.

## Source hierarchy

When sources disagree, use this precedence:

1. Explicit instructions in the current task.
2. Approved entries in analysis_snapshot/results_registry.yaml.
3. Decisions recorded in analysis_snapshot/source_manifest.yaml and
   the analysis repository documentation.
4. Current executable analysis code at the pinned commit.
5. Reference B2Notes, for organization and methodological examples only.
6. Inference.

Never silently resolve a disagreement. Report it and insert a marked TODO.

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
- Check that truth categories are mutually exclusive and exhaustive.
- Check for double application of corrections or overlapping MC samples.

## Writing conventions

- Use stable labels for every section, figure, table, and equation.
- Put detailed diagnostic plots and large tables in appendices.
- State the dataset, channel, run period, selection, weight configuration,
  and source commit for every numerical result.
- Use \AnalysisTBD{} for missing content and \PreliminaryResult{} for
  non-final values.
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