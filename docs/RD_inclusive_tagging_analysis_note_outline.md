# $R(D^\pm)$ Inclusive Tagging Analysis Note — Outline

## 1. Introduction and Analysis Overview
- Definition and physics motivation of $R(D)$.
- Why an inclusive tagging approach is complementary to Full Event Interpretation (FEI)-based approaches.
- Analysis signature and conceptual event partition (signal side vs. rest-of-event tag side).
- One-page summary of the analysis flow.

## 2. Data, Simulated Samples, and Software Versions
- Run 1 and Run 2 data samples.
- Generic $B\bar{B}$, continuum, signal, and special-purpose (signal-enriched) MC samples.
- MC production campaign, basf2 release, global tags, SysVar, pyhf/cabinetry, and HAMMER (if applicable).
- Luminosity normalization and sample-overlap rules.

## 3. Event Reconstruction
- Track, photon, lepton, kaon, and pion selection criteria.
- $D^+ \to K^- \pi^+ \pi^+$ reconstruction.
- Signal $D$-mass window and sidebands.
- $B^0 \to D^- \ell^+$ candidate construction.
- $D^*$ veto.
- Rest-of-event (ROE) / inclusive-tag construction and associated kinematic variables.
- Candidate multiplicity and best-candidate selection.

## 4. Truth Classification and Simulated Sample Composition
- Precise definitions of signal, normalization, feed-down, and background categories.
- Correctly reconstructed vs. fake-$D$, fake-lepton, combinatorial, and secondary-lepton components.
- $D^{**}$, gap modes, single-charm, and double-charm categories.
- Mutually exclusive classification ordering.
- Explicit checks that categories are exhaustive and non-overlapping.

## 5. Multivariate Background Suppression
- Classifier architecture and training samples.
- Target classes (multiclass classification BDT, LightGBM library).
- Input variables, and variables deliberately excluded due to data/MC mismodeling or correlation with fit observables.
- Training/testing independence.
- Working-point optimization.
- BDT input/output validation.

## 6. Corrections and Calibrations
- Luminosity and generator-level normalization.
- Tracking, momentum-scale, PID, fake-rate, and $\pi^0$ corrections.
- Branching-fraction and form-factor updates.
- Continuum treatment.
- Generic-$B\bar{B}$ composition treatment.
- Correction ordering and safeguards against double-applying a weight.

## 7. Generic-$B\bar{B}$ Background Modeling and Validation
- Physics origin of the data/MC disagreement.
- Hierarchical $B$-decay classification scheme.
- Family normalization vs. internal composition.
- Measured vs. unmeasured hadronic modes.
- $n$-body grouping and treatment of 5+-body modes.
- Run dependence.
- Fake-$D$ normalization for Run 1 and Run 2 data.
- Wrong-charge control sample: background-composition plots and justification for why it is not used for MC tuning.
- $D$-mass sidebands and BDT sidebands.
- Closure in the eventual fit bins.
- Residual shape uncertainties and correlations.

## 8. Signal Extraction
- Fit observables: $M_{\rm miss}^2$ and $|\vec{p}_D| + |\vec{p}_\ell|$.
- Motivation for a 2D fit given correlations between the two variables.
- Signal-region and $D$-mass-sideband channels.
- Template definitions.
- Free and constrained normalizations.
- Relationship between signal/normalization yields and $R(D)$.
- pyhf modifiers and correlation model.
- Likelihood definition.
- Bin-merging / coverage requirements (bin choice defined in `utilities.py`).
- Asimov sensitivity, toy studies, pulls, and linearity checks.

## 9. Systematic Uncertainties
- Experimental efficiency uncertainties.
- Form factors and branching fractions.
- Generic-$B\bar{B}$ composition and residual shape uncertainties.
- Fake-$D$ extrapolation.
- Continuum.
- MC statistics.
- Fit bias and finite-template effects.
- Correlations across Run 1/Run 2, $e/\mu$, and signal/sideband channels.

## 10. Validation and Box-Opening Strategy
- Control samples and their intended tests.
- Prefit and postfit closure criteria.
- Split-sample comparison: $e$ vs. $\mu$ channels.

## 11. Expected Sensitivity and Results
- Asimov-only material presented first.
- Data results for the signal region shown only when explicitly authorized.
- No speculative numbers.

## 12. Summary and Analysis Status

## Appendices
- Exhaustive variable lists and selection tables.
- Decay-category definitions.
- MVA diagnostics.
- Correction tables.
- Fit-parameter tables.
- Alternative binnings.
- Complete postfit projections (after box opening).
