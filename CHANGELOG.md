# Change log

Each released version of the note is pinned to an analysis commit in
`zjkjsd/inclusive_R_D`, tracked here and by the `external-code` submodule.

## Version 0.2 (draft) — unreleased

Pinned analysis commit: `ad2f2ec` ("add comments in utilities.py"), moved
forward from `dd520a5`.

This update closes or narrows a large fraction of the open items recorded
against `dd520a5`, from analyst answers cross-checked against the analysis
repository at the new pinned commit. Affected sections: 1, 2, 3, 4, 5, 6, 7,
8, 9, 11, and the appendices on selections, categories and the classifier.
Section 7 in particular required a substantive rewrite rather than a
narrowing: the `BBbkg_weights/` results it described (eight
single-run-period fits, several under a superseded `poisson-2d` objective
name) no longer exist in the repository and have been replaced by six
regenerated `run1+run2` fits with MINOS enabled. See the Open Items appendix
for the updated open-item count (83, up from 80 -- several TBDs were
narrowed to a stated plan and reclassified as in-progress, and the BBbar
rewrite added new, more specific open items even as it closed others).

Added or closed:
- Section 1: physics motivation for R(D)/R(D*), why R(D) is more sensitive
  than R(D*) to charged-Higgs-like couplings, and why inclusive tagging is
  complementary to (not a refinement of) the existing FEI-based
  measurements. Two external ICHEP-2026-preliminary status figures added,
  with provenance recorded from their embedded PDF metadata.
- Section 2: the three signal-enriched MC samples (D tau nu, D* tau nu,
  eight D** tau nu modes) and their role in template building versus BDT
  training; the generic/signal-enriched MC luminosity-scaling relationship;
  a preliminary Run 1/Run 2 luminosity figure; the sample-overlap risk that
  arises once signal-enriched MC is used for both BDT training and its own
  fit template.
- Section 3: motivation for the hadron- and lepton-identification working
  points (Belle II PID convention, not a scan); the electron and muon
  momentum thresholds; the nominal best-candidate method (`vtx`) and the
  resulting multiplicity of 1; confirmed the p_lepton<4 omission from the
  BBbar tuning region is intentional and small in effect. Table 1's
  Motivation column removed in favour of the narrative above it, per
  request.
- Section 4: resolved the merged-D**/gap-mode template configuration; the
  distinction between the two placeholder catch-all categories (expected
  empty) and bkg_fakeTracks (populated, excluded pending a fit treatment);
  a preliminary BDT-class sample-size reference point, flagging a run-period
  inconsistency between the signal-enriched and generic-MC input globs found
  while checking it.
- Section 5: BDT training-class sizes and the training_weight=1 scheme; v3
  confirmed nominal; history of the hyperparameter tuning and the tuner's
  current binary-only limitation.
- Section 6: the correction tables are now version-controlled in the
  repository (MC16_sys_tables/); disposition of pi0_eff50_corr.csv (MC15rd,
  testing only) and the unused slow_pi0/ folder;
  create_naive_data_mc_correction kept deliberately for now; form-factor and
  tracking-efficiency corrections deferred as minor; a concrete proposal for
  extending the branching-fraction correction beyond the generic-BBbar
  families, which requires a new generator-level branch identifying the
  companion-B decay mode for every event.
- Section 7: rewritten against the six regenerated run1+run2 BBbar-weight
  fits with MINOS enabled. kinematic-2d (no ROE term) adopted as nominal;
  MINOS found to give a usable width for three of five family weights but
  not to resolve the persistent 2-body/4-body pinning.
- Section 8: the planned 2D MC histogram and binning-in-utilities.py items;
  the R(D)-as-POI question deferred with a proposed intermediate step; a
  partial MINOS-based width for the generic-BBbar normsys (three of five
  families); the MC-statistical-uncertainty sharing scheme confirmed as
  intended for same-production templates, with the signal-enriched-MC case
  flagged as an unquantified approximation.
- Section 9: confirmed the fake-D normalisation is no longer a systematic
  (determined in situ by the sideband channel); updated the BBbar
  eigen-systematic obstacle with the regenerated fit's HESSE/MINOS
  discrepancy and covariance condition number.
- Section 11: recorded the analyst's preliminary ~12% sensitivity figure as
  indicative, pending the Asimov study of Section 8.

Also added, from cross-checking a sibling Belle II analysis note supplied as
an organisational reference (the hadronic-FEI R(D*)/R(D) measurement,
BELLE2-NOTE-PH-2024-056) -- used only for methodological context, per
AGENTS.md; no number, selection or conclusion from it is an input to this
analysis:
- Section 6: cited the HAMMER form-factor parameterisations (BLPRXP for
  B -> D(*) l/tau nu, BLR for B -> D** l/tau nu) that sibling note uses, as an
  external example to weigh when this analysis makes its own form-factor
  decision; noted its GenMCTagTool-based approach to generator-level
  hadronic-B decay-mode tagging as a possible reusable precedent for the
  companion-B branching-fraction correction proposed in the same section.
- Section 4: noted, as external context only, that the same sibling note
  (and another Belle II analysis it cites) independently found its own
  gap-mode yield substantially below the generic-MC expectation -- different
  final state, not evidence about this analysis, but relevant precedent
  should the same pattern appear here.
- Section 9: cross-checked the completeness of this note's systematics
  category list against that note's, and noted its bootstrap-resampling
  method for the MC-statistics systematic as a candidate for this analysis's
  own toy machinery.

Further cross-checked against four more sibling Belle II reference notes
recovered from this repository's own git history (docs/B2N_*.pdf, not
tracked in git per .gitignore) -- again organisational/methodological
context only, no numbers imported:
- Section 3: added a plot-layout template (efficiency/fake-rate vs. cut
  value, per particle species) for the planned PID working-point plots, from
  the inclusive B -> Xu l nu / |Vub| note; added a three-step ROE-mask
  optimisation template (FOM scan, data/MC tie-break, robustness re-check)
  for if the mask is ever re-optimised, from the B -> tau nu note.
- Section 5: added a two-stage BDT-input/fit-variable data-MC-agreement
  check (pre-training input check, post-selection fit-variable check in a
  sideband) from the semileptonic-tag R(D)/R(D*) note; added an alternative
  to the planned classifier working-point optimisation -- building
  decorrelation from the fit variables into the training objective itself,
  rather than checking it afterward -- from the B -> tau nu note.
- Section 7: cited the B -> K(*) nu nu-bar note's response to a
  shape-degenerate background grouping (external/PDG constraint per group,
  rather than continued in-situ fitting) as a concrete precedent for one of
  the three explanations in the degeneracy discussion; cited its
  independent-validation experience (needed one relaxed normalisation to
  reach acceptable closure) as context for interpreting an imperfect
  validation result here.
- Section 8: cited the semileptonic-tag R(D)/R(D*) note's stated reasons for
  moving from per-bin-per-template to per-bin ("lite Beeston-Barlow")
  MC-statistical nuisance parameters as independent support for this
  analysis's existing per-channel \texttt{staterror} choice; added a
  concrete toy/pull/linearity-check template (toy count, pull definition,
  linearity-scan range, tornado plot) drawn from several sibling notes'
  fit-validation sections.
- Appendix (fit): added a modifier-taxonomy table structure (type,
  constraint, region, sidedness) as a template for the still-required
  complete fit-parameter table.

## Version 0.1 (draft) — unreleased

Pinned analysis commit: `dd520a5` ("start tracking gitignore").

First structured draft. The note previously consisted of the unmodified
Belle II note template.

Added:
- Figure 1, the analysis flow, and the two ordering constraints it makes
  explicit: the classifier is trained after the offline selection, and the
  generic-BBbar weights are derived in a classifier-defined region.
- Appendix: Open Items, consolidating the 80 markers by section and by what
  would close each, with the artifacts ranked by how much they unblock.
- A region-nomenclature table. Three different selections had been called
  "the BDT sideband"; two are in active use for different purposes and the
  third matches neither and is marked superseded.
- scripts/check_build.py, which validates its own patterns against the log
  before reporting a count.
- Sections 7 and 9 no longer cite the BBbar diagnostic scripts as if they were
  part of the analysis: they were held back from the analysis-repo PR and live
  on a separate branch, unvalidated and never run on real ntuples. The note
  now says so rather than pointing at paths that do not exist at the pinned
  commit.
- Section 7.6 now poses the generic-BBbar problem as a three-way question,
  not two-way: bounds too tight, families degenerate, or a data-preferred
  weight outside the physical range. The last mimics a flat direction in the
  deviance and calls for the opposite response, so no merging decision should
  be made before the profile scan distinguishes them.
- Section 7.6 (Constraining power of the tuning region): all eight stored
  BBbar fits sit on a parameter bound, always on an unmeasured n-body weight
  and never on the measured-hadronic weight, with unmeasured-family
  correlations of 0.64-0.93. Argues that the tuning region cannot separate
  the unmeasured families, and marks the scan that would confirm it.
- Section 8 (Signal Extraction), documenting the generated workspace and the
  decision to constrain rather than float the generic-BBbar normalisations.
- Section 3 records two reconstruction findings raised while writing that
  narrative. The electron momentum cut is applied before the bremsstrahlung
  correction deliberately, to keep every candidate inside the coverage of the
  PID tables, which the performance group produces without brems correction;
  the note now gives that justification rather than the diagnostic one. And
  the tight ROE track mask mis-parses: basf2 binds "and" more tightly than
  "or", so the acceptance and pValue requirements apply only to the lowest-pT
  branch. Fixing it requires reprocessing and invalidates ROE-derived results.
- Section 3 gains narrative for every selection that previously appeared only
  in the cut table: track quality, hadron and lepton identification,
  bremsstrahlung recovery, the vertex fits, the D* veto photon requirements,
  the three-stage ROE mask construction, and the tag-side requirements. The
  table is unchanged in scope and remains the literal code reference.
- Section 3 (Event Reconstruction), drafted from
  `Recon_scripts/2_Reconstruction.py`, with a complete cut-to-code table.
- Section 4 (Truth Classification), drafted from
  `utilities.classify_mc_dict()`, including an explicit exclusivity and
  exhaustiveness discussion.
- Skeletons with stable labels for Sections 1, 2, 5–12 and four appendices.
- Result-status macros `\AnalysisTBD`, `\PreliminaryResult`, `\Superseded`,
  `\InProgress`.
- The provenance convention and `scripts/check_provenance.py`.
- Sections 5 (MVA) and 10 (Validation and box opening) drafted, then Section 5
  and the appendices filled from the stored artifacts: the LightGBM
  hyper-parameters and training schedule, the four target-class definitions,
  the recorded train/validation metrics for the three stored models, and the
  anatomy of the generated pyhf workspaces in Fit_toys/.
- Recorded that the stored workspaces are superseded: they are single-channel,
  constrain fake-D at +-5% where the current generator floats it, fix the
  continuum normalisation, and contain no generic-BBbar templates at all.
- Corrected a misidentified state: PDG 10431 is D_s0*(2317)+, not D_s1(2536).
  The four branching-fraction corrections apply to D_s0*(2317) modes and
  reduce the generator rates by factors of 7 to 19.
- Recorded two decisions: the [-5,5] normalisation bounds are deliberate,
  to let the minimiser traverse the negative region so the reported minimum
  is global rather than boundary-pushed; and the continuum constraint is
  one-sided +15%/-0%, superseding the symmetric value in earlier docs.
- Sections 2 and 6 written out in full. Section 2 covers the data and MC
  samples, the three distinct basf2 release roles, the ntuple and offline
  sample naming, and the event-weight chain. Section 6 separates corrections
  that are applied, applied only in validation plots, implemented but never
  called, and not implemented at all, with a table that lists the
  "not applied" cases deliberately.

Changed:
- Corrected the LaTeX build reporting. A hand-rolled grep for overfull boxes
  had a double-escaped pattern that matched nothing, so several commits
  reported a clean build that was not clean. The true count at the time was
  15 boxes, worst 130pt. All are now fixed and the check is a script that
  fails loudly if its patterns stop matching.
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
