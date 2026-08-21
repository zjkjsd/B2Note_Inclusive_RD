Belle
BELLE2-NOTE-PH-2024-031
Version 1.7
January 19, 2026
Measurement and combined analysis of
```
B → K(∗)ν ¯ν decays using Belle II run I data
```
Valerio Bertacchi8, Yulan Fan1, Lorenz G¨artner4. Eldar Ganiev7, Alexander Glazov1,
Yubo Han6, Danylo Kulakov3, Arsenii Kucher3, Meihong Liu5,1 Yuriy Onishchuk3,
Sebastiano Raiz1 Niharika Rout1, Caspar Schmitt4, Slavomira Stefkova2,
1 DESY
2 Bonn
3 Kyiv
4 LMU
5 Jilin
6 Hawaii
7 Ljubljana
8 Pisa
Abstract
We search for rare decays B+ → K+ν ¯ν, B0 → K0S ν ¯ν, B+ → K∗+ν ¯ν and1
```
B0 → K∗0ν ¯ν in a 365 fb−1 sample of electron-positron collisions at the Υ (4S) res-2
```
onance collected with the Belle II detector at the SuperKEKB collider. We use3
```
the inclusive properties of the accompanying B meson in Υ (4S) → BB events to4
```
suppress background from other decays of the signal B candidate and light-quark5
pair production by exploiting distinct signal features with machine learning meth-6
ods. The signal-reconstruction efficiency and background suppression are validated7
through various control channels. The branching fraction is extracted in a maximum8
likelihood fit. We determine the branching fractions of the decays B+ → K+ν ¯ν,9
B0 → K0S ν ¯ν, B+ → K∗+ν ¯ν and B0 → K∗0ν ¯ν to be xx, xx, xx and xx, respectively,10
providing the first/no evidence for this decay at xx standard deviations.11
Changes with respect to previous version
Included in version 1.7
• Check of total B width in Sec. 5.6
• Update on D → K0L weights in Sec. 5.7
• Update in the Asimov fit results with assigning 50% uncertainty to the untagged
events only in Sec. 14
• Validation of total weight in the sidebands in Appendix N
• PXD and CDC hit efficiency check in Appendix F
• Trigger efficiency study for B0 → K0S ν ¯ν in Appendix P
Included in version 1.6
• Update of the unblinding strategy in Sec. 15
• Uniform definition of unmatched neutral cluster energy throughout the note
• References [21,22] to the data-simulation comparison in BDT2 and mass sidebands
• Unblinded results of the control sample B0 → ϕK0 in Sec. 15.1
Included in version 1.5
• Addressed RC comments to version 1.4
• Effect of B → Xsν ¯ν background modeling updates propagated to final result
• Fine-tuning of leading branching fraction background leading to improved coverage
for the high sensitivity regions, see Appendix I
Included in version 1.4
```
• Updated treatment of leading branching fractions (similar with FEI modes tuning
```
```
for rel8), details in Appendix I
```
• Updated treatment of B → Kn¯n backgrounds, details in Appendix L
• Updated treatment of B → Xsν ¯ν background, details in Appendix K
• Improved treatment of fake background, details in Appendix M
• Updated treatment of B → K∗K0 ¯K0 backgrounds, details in Sec. 10.5 and Ap-
pendix H
```
• Fit results are up-to-date (including the new 4-channels-correlated fit in Sec. 14.8).
```
1
Included in version 1.3
```
• Plots in B+ → K∗+(π+K0S )ν ¯ν are updated with soft pionID (>0.05) cut. The cut
```
is applied before BDT2 training and applies to the plots thereafter.
• BDT2 in B+ → K∗+νν was retrained and applied excluding two inputs for which
```
the MC/Data agreement was poor (extra ECL energy of ROE & energy of the muon
```
in D0 →

K+sigµν

```
). The fit section in this version is not up-to-date with this new
```
BDT2.
• A few plots/numbers still need to be updated with the new B+ → K∗+ν ¯ν. Those
are highlighted in red in respective figures and tables.
Included in version 1.2
• Fit section Sec. 14 is complete for Asimov fit
```
• Corrections related to K(∗)K0 ¯K0 are now implemented
```
• Removed accidentally double-applied form factor weights from B0 → K0S ν ¯ν channel,
which reduced the uncertainty on µ further
```
• Various missing systematics, such as, uncertainty related to K(∗)K0 ¯K0 treatment,
```
form factor uncertainties, now added in the fit
```
• Implemented placeholder for fake K∗ systematics (10%).
```
```
• For the B+ → K∗+(π+K0S )ν ¯ν channel, a soft cut on pionID > 0.05 introduced. Only
```
results section is updated for this change as of now.
Contents
1 Introduction 6
2 Treatment of B+ → K+ν ¯ν 8
3 Data and Simulated samples 9
4 Event selection 9
4.1 Tracks and cluster selections . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.2 Signal candidate selection . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2.1 B0 → K0S ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2.2 B0 → K∗0ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.2.3 B+ → K∗+ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.3 Event-level selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2
5 Corrections to simulated and data samples 14
5.1 Charged particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.2 Neutral particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.3 K0S / K0L efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
5.4 Leading B meson branching fractions . . . . . . . . . . . . . . . . . . . . . 15
5.5 B → D∗∗X branching fractions . . . . . . . . . . . . . . . . . . . . . . . . 15
5.6 Check of total B meson width . . . . . . . . . . . . . . . . . . . . . . . . . 16
5.7 D → K0L background correction . . . . . . . . . . . . . . . . . . . . . . . . 16
6 Background suppression 17
```
6.1 First-level filter (BDT1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
```
6.1.1 B0 → K0S ν ¯ν and B0 → K∗0ν ¯ν . . . . . . . . . . . . . . . . . . . . . 17
6.1.2 B+ → K∗+ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
```
6.2 Second-level filter (BDT2) . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
```
7 Signal region definition 24
8 Signal validation 30
8.1 Signal efficiency validation . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
8.2 Signal BDT inputs validation . . . . . . . . . . . . . . . . . . . . . . . . . 30
9 Continuum background validation using off-resonance data 34
10 Background composition and validation 39
10.1 Background composition in the signal region . . . . . . . . . . . . . . . . . 39
10.2 Validation in BDT2 sideband . . . . . . . . . . . . . . . . . . . . . . . . . 39
10.3 Validation in mass sideband . . . . . . . . . . . . . . . . . . . . . . . . . . 40
```
10.4 Validation using D → K(∗)X control sample . . . . . . . . . . . . . . . . . 40
```
10.4.1 B+ → K+ν ¯ν decays . . . . . . . . . . . . . . . . . . . . . . . . . . 47
10.4.2 B0 → K0S ν ¯ν decays . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
10.4.3 B0 → K∗0ν ¯ν decays . . . . . . . . . . . . . . . . . . . . . . . . . . 47
10.4.4 B+ → K∗+ν ¯ν decays . . . . . . . . . . . . . . . . . . . . . . . . . . 49
```
10.5 Updates to the B → K(∗)K0 ¯K0 modeling . . . . . . . . . . . . . . . . . . 50
```
10.5.1 B0 → K0S K0 ¯K0 modeling . . . . . . . . . . . . . . . . . . . . . . . . 50
10.5.2 B → K∗K0 ¯K0 modeling . . . . . . . . . . . . . . . . . . . . . . . . 51
11 Signal crossfeed 53
12 Sample composition in signal region 54
13 Systematic uncertainties 56
14 Signal extraction 60
14.1 Statistical model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
14.2 Fit setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
14.3 Asimov fit results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
14.4 Impact of systematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
3
14.5 Likelihood scan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
14.6 Toys and signal injection studies . . . . . . . . . . . . . . . . . . . . . . . . 71
14.7 Isospin averaged fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
14.8 4-channels averaged fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
15 Tests before box opening 78
15.1 Cross check measurement of B0 → ϕK0L decay . . . . . . . . . . . . . . . . 79
15.2 Half-split studies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
15.3 Studies of individual fits . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
15.4 Checks of combined fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
References 84
A Variable lists 87
B Distributions of BDT1 and BDT2 inputs 93
B.1 Distributions for B0 → K0S ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . 93
B.2 Distributions for B0 → K∗0ν ¯ν . . . . . . . . . . . . . . . . . . . . . . . . . 98
B.3 Distributions for B → K∗+νν . . . . . . . . . . . . . . . . . . . . . . . . . 102
C Optimization of photon selection for ROE 111
D Low-multiplicity events suppression 114
E KaonID > 0.9 and KaonID > 0.75 and PionID > 0.05 tables 118
F nPXDHits> 0 tables 122
G π0 Reconstruction Efficiency Correction Tables 125
H B → K∗K0S K0S control channels 126
H.1 B0 → K∗0K0S K0S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
H.2 B+ → K∗+K0S K0S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
I Leading branching fractions of B-decays 130
I.1 Corrections to the central values of branching fractions . . . . . . . . . . . 130
I.2 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
I.3 Treatment of the systematical uncertainty . . . . . . . . . . . . . . . . . . 139
J B → D∗∗X backgrounds studies 140
K Treatment of B → Xhs ν ¯ν background 142
L Treatment of B → Kn¯n background 143
M Fake K∗ background investigations 145
M.1 Fake K∗0 background investigation . . . . . . . . . . . . . . . . . . . . . . 145
M.2 Fake K∗+ background investigation . . . . . . . . . . . . . . . . . . . . . . 147
4
N Validation of total weight in sidebands 150
O D veto studies for B+ → K+ν ¯ν decays 153
O.1 Normalization factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
O.1.1 Constrain on each component . . . . . . . . . . . . . . . . . . . . . 156
O.2 Inclusion in the likelihood . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
```
O.3 BDT2 bias correction in M (Kπ) . . . . . . . . . . . . . . . . . . . . . . . . 158
```
P Trigger study for the B0 → K0S ν ¯ν channel 160
Q Deep Neural Network Architectures 162
Q.1 Performance Comparison with BDT . . . . . . . . . . . . . . . . . . . . . . 162
```
Q.2 Multi-Layer Perceptron (MLP) Architecture . . . . . . . . . . . . . . . . . 162
```
Q.3 Transformer Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Q.4 Training Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
Q.5 Optimized Data Loading . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
R Exploration of Lorentz Equivariant Neural Net 168
5
1 Introduction12
```
Flavor-changing neutral-current (FCNC) transitions, such as b → sν ¯ν and b → sℓℓ, where13
```
```
ℓ represents a charged lepton, are suppressed in the Standard Model (SM) of particle14
```
```
physics due to the Glashow–Iliopoulos–Maiani (GIM) mechanism [1]. These transitions15
```
can only occur at higher orders in SM perturbation theory, involving weak-interaction16
amplitudes that require the exchange of at least two gauge bosons.17
Predictions for the rates of b → sℓℓ carry significant theoretical uncertainties due to18
the breakdown of factorization caused by photon exchange [2]. This complication does not19
affect b → sν ¯ν decays, leading to relatively precise rate predictions for these processes.20
b s
ν
ν
u u
u, c, t
W +
Z0
b s
ν ν
u u
u, c, t
ℓ+
W + W −
```
a) b)
```
b
u ντ
τ +
ντ
W +
s
u
W +
```
c)
```
```
Figure 1: Lowest-order quark-level diagrams for the B → K(∗)ν ¯ν decay in the SM are
```
```
either of the penguin (a), or box type (b). The long-distance double-charged-current
```
```
diagram (c) arising at tree level in the SM also contributes to the B+ → K+(∗)ν ¯ν decay.
```
The b → sν ¯ν transition provides the leading amplitudes for the B+ → K+ν ¯ν decay21
```
in the SM, as shown in Fig. 1. The short-distance (SD) contributions from diagrams22
```
of the penguin and box type, involving W + and Z0 bosons, dominate the branching23
fraction. Decays of charged B mesons include a contribution from the long-distance24
```
(LD) double-charged-current B+ → τ +(→ K+ ¯ν)ν decay that is dominated by on-shell25
```
τ -lepton production. Due to charge conservation, this contribution is absent for neutral26
B meson decays. Theoretical uncertainties arise from two main sources: uncertainties in27
the hadronic form factors and in the CKM matrix elements. The latter are particularly28
influenced by the discrepancies in the experimental determinations of the matrix element29
6
Decay SM total LD contribution SD contribution Experimental value
B+ → K+ν ¯ν 5.22 ± 0.32 0.63 ± 0.06 4.59 ± 0.32 13 ± 4 [3]
```
B0 → K0S ν ¯ν 2.12 ± 0.15 — 2.12 ± 0.15 < 13 (90% CL) [4]
```
```
B+ → K∗+ν ¯ν 11.27 ± 1.51 1.07 ± 0.10 10.20 ± 1.51 < 40 (90% CL) [5]
```
```
B0 → K∗0ν ¯ν 9.47 ± 1.40 — 9.47 ± 1.40 < 18 (90% CL) [4]
```
Table 1: In units of 10−6, Standard Model predictions from [6] and experimental results
for the branching fractions of the four B → Kν ¯ν decays. The experimental results treat
the LD contribution as background. For B+ → K+ν ¯ν, an average branching fraction
evaluated in Ref. [3] is given.
```
|Vcb| (6% uncertainty). For decays involving a pseudoscalar in the final state, which30
```
```
are described by a single form factor (3% uncertainty), the CKM uncertainties tend to31
```
dominate. Conversely, for decays with a vector meson in the final state, the uncertainties32
```
on the form factors (10% uncertainty) play a more significant role.33
```
The study of B → Kν ¯ν decays is experimentally challenging as the final state contains34
two neutrinos that are not reconstructed. This prevents the full reconstruction of the kine-35
matic properties of the events, hindering the differentiation of signal from the background.36
The recent B+ → K+ν ¯ν measurement performed by the Belle II collaboration provides37
```
the first evidence for this decay [3] reporting a branching fraction of (23 ± 7) × 10−6. The38
```
paper combines the result with previous measurements, yielding a combined branching39
```
fraction of (13 ± 4) × 10−6. Previous analyses of other decay modes have only provided40
```
upper limits, with the best results obtained by the Belle collaboration using hadronic and41
semileptonic tagging methods [5, 4]. A summary of the Standard Model expectations and42
experimental results is shown in Table 1.43
The first evidence of B+ → K+ν ¯ν decays observed by Belle II has generated significant44
interest from the community. Several models were proposed that can describe the tensions45
with the Standard Model. These include models involving leptoquarks and additional46
bosons, right-handed neutrinos, light dark matter, the Higgs portal, and other models47
```
(see, e.g., Refs. [7, 8, 9, 10, 11]). The papers highlight the importance of more accurate48
```
experimental measurements. In particular, the tension between the branching fractions49
of the B+ → K+ν ¯ν decay, where the first evidence is observed, and the B → K∗ν ¯ν decay,50
where only upper limits exist, is often discussed. This underscores the importance of51
new measurements on the B → K∗ν ¯ν and B0 → K0S ν ¯ν channels, which would provide52
additional information also on B+ → K+ν ¯ν.53
The analysis presented in this note extends the existing B+ → K+ν ¯ν analysis to54
the B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channels. The measurement is55
based on the Run I Belle II data sample comprising 365 fb−1 of data collected at the56
```
Υ (4S) resonance and 42 fb−1 at 60 MeV below it. An inclusive tagging analysis method57
```
exploiting inclusive properties of the signal B meson, along with the pair-produced B-tag58
meson, is employed. Special care is taken to preserve correlations among the channels59
and with the B+ → K+ν ¯ν published analysis. We perform a combined analysis of the60
four decay channels to measure their branching fractions. The K∗ channels have a sizable61
```
contamination from states with a higher hadron multiplicity, B → Xsν ¯ν (Further study62
```
```
is shown in Appendix K). This contamination is treated as background, following the63
```
7
prescription in BELLE2-PUB-PH-2025-005. Finally, an investigation is performed within64
the effective field theory approach and simplified dark-mediator model, following the65
methodology outlined in Ref. [12].66
The analysis commences with the reconstruction of charged and neutral particles, fol-67
lowed by the signal candidates selection. A single candidate is selected for the K0S channel68
while several candidates are kept for the decays involving K∗, due to higher combinatorial69
background for these decays. Subsequently, relevant quantities are computed using the70
signal candidate, along with the remaining particles in the event, to discriminate between71
signal and background processes. These quantities are used in boosted decision trees72
```
(BDTs) [13, 14] that are optimized and trained using simulated data. A signal region73
```
is defined afterwards, and for the K∗ channels a single candidate per event is selected74
at this point. A binned profile-likelihood sample-composition fit is carried out in data75
using simulated samples to provide predictions and determine the branching fraction of76
the B → Kν ¯ν decays along with the rates of background processes. The fit incorporates77
systematic uncertainties arising from detector and physics-modelling imperfections as nui-78
sance parameters. Fits are also performed to investigate the impact on the beyond-SM79
models. To validate the modelling of signal and background processes in simulation, sev-80
eral control channels are employed. As part of the background validation, measurements81
are performed for the decays B0 → K∗0K0S K0S and B+ → K∗+K0S K0S . The branching82
fractions of these decays, along with the invariant mass distribution of the K0S K0S pair,83
are determined for the first time.84
The note is organized as follows. Sec. 3 describes data and simulated samples used in85
the analysis. Sec. 4 specifies particle and signal candidate selection for the three signal86
modes. Corrections applied to the data and simulated samples are discussed in Sec. 5.87
The background suppression is discussed in Sec. 6. Sec. 7 describes the definition of the88
signal region, where the fit is performed. Signal, continuum background, and generic89
background composition and validation using control data are described in Sec. 8, Sec. 9,90
and Sec. 10, respectively. Studies on crossfeed contributions between signal channels are91
presented in Sec. 11, while the sample composition in the signal region is shown in Sec. 12.92
Sec. 13 describes the treatment of systematic uncertainties, and Sec. 14 introduces the93
statistical analysis configuration used to extract the signal branching fractions.94
2 Treatment of B+ → K+ν ¯ν95
For the B+ → K+ν ¯ν channel, the selection criteria and analysis flow are kept the same as96
of the published version [3]. However, in the combined fit, the other three signal channels97
are treated as cross-feed rather than background. Additionally, an improved constraint98
```
on the dominant background (using charm decays) is also performed for the standalone99
```
B+ → K+ν ¯ν channel, as described in Appendix O. This constraint has not yet been100
```
applied in the combined fit; it will be studied for the other channels and incorporated at101
```
a later stage.102
Here, we summarize the main selections for B+ → K+ν ¯ν:103
```
• Tracks: transverse momentum pT > 0.1 GeV, E < 5.5 GeV and CDC acceptance;104
```
```
|dz| < 3.0 cm and dr < 0.5 cm are imposed on all tracks, except for K0S daughters;105
```
8
at least one deposit in pixel detector.106
• Photons: 100 MeV < E < 5.5 GeV, CDC acceptance and do not match tracks.107
• Kaons: KaonID> 0.9 and at least 20 charged deposits in CDC.108
• Event-level criteria: number of ROE tracks 3 ≤ nROETracks ≤ 8, visible energy109
```
Evis > 4, GeV, and missing momentum polar angle θpmiss ∈ (0.3, 2.8).110
```
• Best candidate selection: lowest q2.111
• Two consecutive BDTs: BDT1 is trained with 12 input variables to suppress the112
continuum background. BDT2 is then trained on events satisfying BDT1 > 0.9,113
using 35 input variables, and is used for the final event selection.114
3 Data and Simulated samples115
This analysis uses data produced between the years 2019 and 2022 from Run I. The116
```
sample comprises 365 fb−1 of data collected at Υ (4S) resonance (on-resonance data) and117
```
```
42 fb−1 at 60 MeV below it (off-resonance data). The number of BB pairs in on-resonance118
```
```
sample is (387 ± 6) × 106. The analysis uses proc13 and prompt release6 processing119
```
for the data. The signal and background templates are produced using run-dependent120
```
simulated samples from MC15 production (MC15RD). Background suppression classifiers121
```
```
are trained using 400 fb−1 of run-independent samples (MC15RI). The MC15rd sample122
```
has four times the data luminosity and is used for validation and signal extraction. We123
```
use 10 (2), 10 (4), and 40 (4) million RI (RD) signal simulation events for the channels124
```
B0 → K0ν ¯ν, B0 → K∗0ν ¯ν and B+ → K∗+ν ¯ν, respectively. K0 and K∗ particles are125
decayed generically, including non-signal modes.126
The simulated B → Kν ¯ν signal decays are generated according to the SM form factor127
```
calculation from Ref. [15]. The long-distance contribution, B+ → τ +(→ K∗+ ¯ν)ν, is128
```
simulated within the generic B+B− backgrounds.129
The reconstruction code is based on the software release light-2311-nebelung, and it130
is available at https://gitlab.desy.de/belle2/physics/ewp/b2hnunubar ITA.131
4 Event selection132
4.1 Tracks and cluster selections133
All tracks in the event are required to have transverse momentum pT > 0.1 GeV, energy134
E < 5.5 GeV and acceptance within CDC. Additionally, impact parameter requirements135
of |dz| < 3.0 cm and dr < 0.5 cm are imposed on all tracks, except for K0S daughters.136
Photons are reconstructed using the standard photon list gamma:all, and are required137
to lay inside CDC acceptance, have energy in the range 60 MeV < E < 5.5 GeV and138
be separated from the nearest track by at least 20 cm. An optimization of the photon139
selection is discussed in Appendix C.140
9
4.2 Signal candidate selection141
First, we select or reconstruct the signal composite particles using tracks and clusters. The142
selection criteria for these particles are detailed in the respective channel sub-sections of143
this section.144
For each signal candidate, a selection on the reconstructed dineutrino invariant mass145
squared q2rec > −1 GeV/c2 is required. This ensures that the candidates are in the kinemat-146
ically allowed region while allowing for smearing effects. The q2rec observable is computed147
based on the signal candidate recoil energy as148
```
q2rec = s/(4c4) + M 2K(∗) −
```
√
```
sE∗K /c4 (1)149
```
```
assuming the signal B meson to be at rest in the e+e− c.m. frame. MK(∗) is the known150
```
mass of the signal meson, and E∗K is the reconstructed energy of the signal meson in the151
c.m. system.152
For B0 → K0S ν ¯ν decays, the K0S reconstruction is highly pure, allowing for the selec-153
tion of a single candidate per event after basic selection with high efficiency. Conversely,154
for B → K∗ν ¯ν decays, the large multiplicity of tracks near the interaction point and the155
significant width of the K∗ resonances result in a high candidate multiplicity. Therefore,156
multiple candidates per event are allowed in these cases until final selection steps.157
The signal candidate selection details for each channel are outlined in the following sub-158
sections. 1159
4.2.1 B0 → K0S ν ¯ν160
K0S candidates are selected from the KS0:merged list. In this list, candidates are required161
to have a dipion reconstructed mass between 0.485 and 0.51 GeV/c2, vertex p-value greater162
```
than 0.001, and flight time greater than 0.007 ns (corresponding to about 2 mm displace-163
```
```
ment from the primary vertex). Additionally, the cosine of the angle between the K0S164
```
momentum direction and the direction extrapolated from the K0S vertex to the IP must165
be greater than 0.98. After all these selections, the signal candidate with the lowest q2rec166
is kept as a best candidate.
B0 → K0S ν ¯ν
cuts signalefficiency [%]avg. signalmultiplicityavg. backgroundmultiplicity
Track clean up 47.5% 2.6 7.5
K0S Mass 45.3% 1.5 3.0
```
cos(PK0S , VK0S ) > 0.98 44.3% 1.2 1.6
```
q2 best candidate selection 43.6% 1.0 1.0
Table 2: Efficiency and multiplicity of signal and background for B0 → K0S ν ¯ν channel
after each selection step. Reference includes K0S → π0π0.
167
1All shown signal efficiencies are truth-matched.
10
4.2.2 B0 → K∗0ν ¯ν168
K∗0 is reconstructed from a charged kaon and a pion. The K∗0 → K0S π0 channel is not169
considered due to low reconstruction efficiency and poor purity. The charged kaon and170
pion are required to have at least one PXD hit, and satisfy basic selection described171
in Sec. 4.1. In addition, kaon is identified by the global likelihood probability LKPi Li >172
```
0.75, (i = e, µ, K, π, p, d), while pion is identified by the global pion likelihood probability173
```
above 0.05. Both the PID selections are optimized to provide maximum signal significance.174
Then, a vertex fitting algorithm, Treefit[16], is applied to determine the decay vertex175
location and momentum of the K∗0 meson. The mass of K∗0 resonance is constrained176
between 0.8 and 1.0 GeV/c2.177
An initial signal-candidate selection is performed using a MVA classifier, also known178
as BDTCA. It is trained using simulated signal K∗0 events to distinguish between correct179
and random combinatorial combinations of K+ and π− mesons. The classifier uses the180
three variables constructed using the K+ and π− pair: invariant mass of the pair, q2rec,181
and the decay vertex distance from the interaction point in X − Y plane. Two candidates182
with the highest BDTCA are kept at this stage. Table 3 summarizes the signal efficiency,183
signal multiplicity and background multiplicity at different selection steps.184
B0 → K∗0ν ¯ν
cuts signalefficiency [%]avg. signalmultiplicityavg. backgroundmultiplicity
K∗0 Mass 39.8 5.2 10.5
K+ PXD hits and PID 30.2 1.8 2.4
π− PXD hits and PID 26.2 1.5 1.9
MVA-two-candidate selection 26.1 1.3 1.5
Table 3: Efficiency and multiplicity of signal and background for B0 → K∗0ν ¯ν channel
after each selection step. Reference includes K∗0 → K0S π0.
4.2.3 B+ → K∗+ν ¯ν185
We reconstruct the K∗+ candidate in two decay channels: K∗+ → K+π0 and K∗+ →186
π+K0S . For K∗+ → K+π0 mode, the kaon is selected with tighter cuts compared to187
Sec. 4.1: |dz| < 0.3 cm, dr < 0.05 cm, E < 3.0 GeV, kaonID > 0.9, and more than 10 and 0188
hits in CDC and PXD sub-detectors, respectively. Neutral π0 candidates are reconstructed189
from the photon list eff50 May2020, inside the windows [0.105 < Mπ0 < 0.15 ] GeV/c2190
and [0.06 < Eγ < 5.5 ] GeV, using the standard stdPi0 list. They are subsequently191
```
mass-constrained in a vertex fit (KFit).192
```
For K∗+ → π+K0S , the pion is selected in the same manner as the kaon, but with a193
PID requirement of pionID > 0.05.2 K0S are selected using the same selection criteria as194
of the signal K0S in B0 → K0S ν ¯ν channel, described in Sec. 4.2.1. Table 5 and 4 summarize195
the residual signal efficiencies, as well as background and signal multiplicities.196
2The requirement on pionID was lately added to improve π+ purity. It is applied before BDT2
training.
11
```
B+ → K∗+(K+π0)ν ¯ν
```
cuts signaleff. [%]avg. signalmult.avg. bkg.mult.
K∗+ mass 28.5 4.32 6.3
K+ PID and PXD hits 24.8 4.11 5.98
q2 five candidate selection 23 2.29 2.36
```
Table 4: Efficiency and multiplicity of signal and background for B+ → K∗+(K+π0)ν ¯ν
```
channel after each selection step.
```
B+ → K∗+(π+K0S )ν ¯ν
```
cuts signaleff. [%]avg. signalmult.avg. bkg.mult.
K∗+ mass 26.2 2.21 2.72
π+ PXD hits 24.1 1.96 2.39
```
cos(PK0S , VK0S ) > 0.98 23.5 1.87 2.21
```
q2 five candidate selection 22.6 1.65 1.65
```
Table 5: Efficiency and multiplicity of signal and background for B+ → K∗+(π+K0S )ν ¯ν
```
channel after each selection step. Reference includes K0S → π0π0.
The reconstructed K∗+ from both decay channels are combined, while keeping track197
of the decay modes and requiring their mass to lay in a window [0.8 < M < 1.0] GeV/c2.198
For K∗+ → K+π0, a single track is not sufficient for vertex fitting without additional199
constraints. Hence, we decided not to perform any vertex fit to the K∗+ candidates. As200
an initial selection, five candidates with lowest q2rec are kept per event.201
4.3 Event-level selection202
All charged and neutral particles remaining after the signal candidate selection are as-203
```
signed to the rest of the event (ROE). The charged particles, apart from pions from K0S204
```
decays, are given the most likely mass hypotheses based on their PID likelihoods and the205
```
known abundances of particle species in Υ(4S) events. The number of tracks in the ROE206
```
is required to be within 3 and 9 for B+ → K∗+ν ¯ν and within 2 and 9 for B0 → K0S ν ¯ν and207
B0 → K∗0ν ¯ν. The ROE vertex is fitted using the KFit algorithm without any constraint,208
and the tracks that contribute to the maximum reduced chi-squared value are kept3.209
For each B-meson signal candidate, continuum suppression variables are computed210
using the signal and ROE particles. For the event-shape variables, the signal B meson is211
```
treated as a single composite particle (e.g. the pion and kaon from the signal-candidate212
```
```
K∗0 are not treated separately). This approach results in distinct values for each signal213
```
candidate, thereby making the reconstruction of different channels more uniform and214
comparable. Further imposed selections require the hlt hadron software skim and a215
total charge Q2net ≤ 4. Low-multiplicity events such as those originating from e.g. γγ216
3This corresponds to default behaviour of earlier versions of basf2, as used in B+ → K+ν ¯ν analysis,
by accepting fits with large value of χ2 using kFitReqReducedChi2=1e10 parameter.
12
scattering processes, have not yet been simulated. We suppress these events by applying217
selections on the visible energy of the event, Evis > 4 GeV, and on the angle of the218
```
missing momentum direction, 0.3 < θ(pmiss) < 2.8, which are discussed in Appendix D.219
```
For B0 → K0S ν ¯ν, we also study the trigger efficiency, as discussed in Appendix P.220
All the event selections for all three channels are summarized in Table 6.221
Category Selections Channels
B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
Tracks
pt > 0.1 GeV ✓ ✓ ✓
```
E ∈ (0.1, 5.5) GeV ✓ ✓ ✓
```
CDC acceptance ✓ ✓ ✓
Tracks excluding
K0S daughters
|dz| < 3 cm ✓ ✓ ✓
dr < 0.5 cm ✓ ✓ ✓
Neutrals
```
E ∈ (0.06, 5.5) GeV ✓ ✓ ✓
```
minC2TDistance > 20 cm ✓ ✓ ✓
CDC acceptance ✓ ✓ ✓
Low multiplicity
event veto
Evis > 4 GeV ✓ ✓ ✓
```
θpmiss ∈ (0.3, 2.8) ✓ ✓ ✓
```
q2 q2 > −1 GeV/c2 ✓ ✓ ✓
Total charge Q2net ≤ 4 ✓ ✓ ✓
nROETracks ∈ [2, 9] ∈ [2, 9] ∈ [3, 9]
K0S
```
KS0:merged ✓ ✓
```
```
cos(pK0S , K0S vertex) > 0.98 ✓ ✓
```
```
M ∈ (0.485, 0.51) GeV/c2 ✓ ✓
```
K∗0
```
M ∈ (0.8, 1.0) GeV/c2 ✓
```
nPXDHits > 0 ✓
kaonID > 0.75 ✓
pionID > 0.05 ✓ ✓
K∗+
std π0:eff50 ✓
nCDCHits > 10 ✓
|dz| < 0.3 cm ✓
dr < 0.05 cm ✓
nPXDHits > 0 ✓
track E < 3.0 GeV ✓
kaonID > 0.9 ✓
pionID > 0.05 ✓
```
M ∈ (0.8, 1.0) GeV/c2 ✓
```
Table 6: Summary of basic event selections for all the channels. Cuts for signal selection
are added on top of basic selection.
13
5 Corrections to simulated and data samples222
5.1 Charged particles223
Charged-particle identification performance may differ between data and simulation. To224
account for these discrepancies, we apply corrections obtained with the Systematics225
```
Framework [17] for each charged-particle type (wherever there is a PID selection, i.e.,226
```
```
K+ and π− of K∗0, and K+ of K∗+) in the two-dimensional space of momentum and227
```
polar angle, as PID depends on both of these quantities. We correct both the efficiency228
and fake-rate. Appendix E details the dependencies of corrections on momentum and229
polar angle.230
Selections on the number of hits in the PXD or CDC detectors can also introduce231
data/simulation discrepancies. We quantified this difference using the Systematics Frame-232
work. For the CDC hits requirement, the difference is negligible, and we don’t apply any233
correction. For the PXD hit requirement, we observe a data/simulation difference of234
about 2/3% for each track. Hence, we correct the track efficiency and fake-rates as a235
```
function of momentum and polar angle. Appendix F details the dependencies of PXD236
```
hits corrections for efficiencies and kaon/pion fake rates on these two quantities.237
The track momenta are scaled using the recommended scale factors [18] in data. Un-238
certainties on these scale factors have a negligible impact on the analysis.239
5.2 Neutral particles240
The photon energy bias between data and MC has to be taken into account. We correct241
the data samples by using PhotonEnergyBiasCorrection MC15rd June2023 payloads. We242
```
evaluate the effect of the discrepancy in the systematic uncertainty (see Sec. 13). In MC,243
```
```
we vary the neutral cluster (associated to photons) energy by 0.5% and compare the244
```
obtained sample with the nominal one.245
At the previous iteration of the analysis, we observed a discrepancy in the distributions246
```
of energy of the ROE photons in data and MC (see Appendix K in [19]). This discrepancy247
```
is caused by the mismodeling of neutral clusters that are not associated to the photons in248
MC. We found that reducing the energy of such clusters by 10% improves the data-MC249
agreement. Since we switched to run-dependent MC in this iteration, we want to make250
sure whether the correction should be changed. We repeat the study using run-dependent251
MC and find that the correction of 10% applied on the energy of the neutral clusters252
not associated to photons still improves the data-MC agreement. Hence, we apply this253
correction to the nominal sample and assign a 100% systematic uncertainty.254
```
For the B+ → K∗+(→ K+π0)ν ¯ν channel, the official π0 efficiency corrections for the255
```
photon selection eff50 May2020 do not include a correction for π0 mesons reconstructed256
```
with a momentum within [0, 0.5] GeV/c and cos θ within [-1, -0.6] range (Appendix G).257
```
Therefore, we correct their efficiency by 50% and we assign a 100% uncertainty, i.e.258
0.5±0.5.259
14
5.3 K0S / K0L efficiency260
We use the recommended K0S reconstruction efficiency corrections and their uncertain-261
ties [20]. The corrections are provided in a three-dimensional binning based on the 3D262
```
flight distance(d), momentum(p), and cosTheta(θ), as a ratio of the data and MC yields,263
```
re-scaled by the ratio in the first distance bin, which are extracted from the ratio of signal264
yields from the D∗+-tagged D0 → K0S π+π− decays. For the K0S with d < 0.5 cm, the265
correction is determined based on the momentum of the daughters following the recom-266
mendations from the performance group.267
Another data-simulation discrepancy that we take into account brought by the mod-268
eling of the K0L detection efficiency in the ECL. Since we changed our ECL cluster se-269
lection with respect to the previous iteration, and we use run-dependent simulation, we270
```
re-evaluate the size of the discrepancy using radiative ϕ-meson production (see Appendix271
```
```
V in [19]). Figure 2 shows the K0L detection efficiency in the ECL as a function of energy.272
```
The data-simulation discrepancy has a similar level to the previous iteration. Hence, we273
reduce the simulated K0L detection efficiency by 17% and assign a 50% uncertainty on the274
correction.275
2.0 2.5 3.0 3.5 4.0
K0L energy [GeV]
0.0
0.2
0.4
0.6
0.8
1.0
K
0L efficiency
Belle II preliminary
L dt = 362 fb-1
Data
Simulation
Figure 2: K0L reconstruction efficiency in the ECL as a function of energy, obtained with
the radiative ϕ process reconstructed in data and simulation.
5.4 Leading B meson branching fractions276
Several of the branching fractions of leading B meson decays are corrected in the MC277
following the most recent measurements. More details are provided in Appendix I, in-278
cluding the list of 104 B meson decays that are considered as the leading B meson decays.279
280
5.5 B → D∗∗X branching fractions281
The branching fractions of the main B → D∗∗X decays are corrected in the MC according282
to the most recent measurements. More details are provided in Appendix. J283
284
15
5.6 Check of total B meson width285
We study the impact of the leading-B and D∗∗ corrections on the total B meson width286
using generator-level B+B− and B0 ¯B0 background samples.The total B meson width is287
preserved by scaling untagged events with the weight,288
```
w =
```
Ntotal − SumWTagged
Nuntagged
.289
Here, Ntotal is the generation-level yield, SumWTagged is the yield after applying the290
leading-B and D∗∗ corrections to the tagged events, and Nuntagged is the yield of events291
not tagged by the leading-B and D∗∗.292
The resulting weights are 1.09 and 1.13 for B0 and B+ events, respectively.293
5.7 D → K0L background correction294
The D → K0L branching fraction correction was determined to be 1.3±0.1 in the published295
K+ analysis using pionID and leptonID sideband samples. The corresponding fit includes296
three components: q ¯q, D → K0L, and other B ¯B backgrounds. The q ¯q and D → K0L297
yields are floated in the fit, while the remaining B ¯B background contribution is fixed. In298
the present analysis, the leading-B, D∗∗, and untagged event weights are applied to the299
nominal selection. To ensure consistency, these weights are also applied to the pionID,300
electronID, and muonID sideband samples to extract D → K0L correction. The correction301
factors are re-derived by repeating the fits in each sideband, as shown in Figs. 3 and 4.302
The resulting corrections are 1.30 ± 0.02, 1.41 ± 0.01, and 1.38 ± 0.01 for the pionID,303
electronID, and muonID sidebands, respectively. The correction factor obtained from the304
pionID sideband is adopted as the nominal value. The difference between the pionID and305
leptonID sideband results is assigned as the systematic uncertainty.306
The final D → K0L correction factor is therefore 1.30 ± 0.10, consistent with the307
published result.308
Figure 3: q2rec fit to pionID sideband sample.
16
Figure 4: q2rec fit to electronID and muonID sideband samples.
6 Background suppression309
Background suppression is performed through a multi-step process. Initially, a first-level310
```
Boosted Decision Tree (BDT1) filter is applied, designed to be efficient for the signal and311
```
to reduce the data volume for subsequent ntuple-based analysis. The final background312
```
reduction is achieved with an optimized second-level BDT (BDT2). This two-tiered ap-313
```
proach ensures robust background suppression, enhancing the overall signal purity and314
analysis accuracy.315
Variables used as inputs of both BDTs to discriminate signal and background events316
are based on event, ROE, signal-side, and combination of ROE and signal-side properties.317
The ROE is reconstructed using objects passing the selection, including pion tracks from318
K0S s present in ROE. For tracks from IP, most likely particle identification hypothesis319
is used. For some dedicated D suppression variables, a dedicated simplified ROE is320
reconstructed that uses pion only hypothesis for all tracks.321
After the basic selection described in Section 4 and using the corrections described in322
Section 5, all variables are inspected to ensure that they are correctly described in the323
Monte Carlo simulation. Furthermore, only variables which offer visible discrimination324
between signal and background simulation are considered. The full list of background325
suppresion input variables for each decay mode is given in Appendix B.326
```
6.1 First-level filter (BDT1)327
```
6.1.1 B0 → K0S ν ¯ν and B0 → K∗0ν ¯ν328
The low branching fraction and presence of two neutrinos in the final state make it chal-329
```
lenging to reconstruct and observe B → K(∗)(S)ν ¯ν signals. Therefore, a powerful classifier330
```
is needed to suppress large backgrounds coming from continuum and other B decays.331
```
We combine non-linearly discriminating variables in a FastBDT (fast-boosted-decision-332
```
```
tree classifier). The separation power (or importance) of all the input variables is listed333
```
in Appendix A. For the first classifier, BDT1, one per decay channel, we choose a shared334
set of the twelve most powerful event-shape discriminating variables: difference between335
the ROE energy in the CMS and
√
s/2, magnitude of the ROE momentum, polar angle of336
17
the ROE momentum, cosine of the angle between the kaon track and the ROE thrust axis337
in the CMS, modified Fox-Wolfram moments calculated in the CMS Roo0 , Roo2 , Hsom,2, Hsom,4,338
cosine of the polar angle of the thrust axis in the CMS, normalized Fox-Wolfram moment339
R1, zeroth-order and second-order harmonic moments with respect to the thrust axis in340
the CMS. The distributions of 12 variables for all decay modes of interests are shown in341
Appendix B. The chosen variables do not only separate signal and background, but also342
their distributions in data are well reproduced in simulation.343
The choice of the classifier parameters used for the training are listed in Table 7.344
Fig. 5 shows that with the chosen classifier parameters, the overfitting is under control.345
The BDT1 > 0.9 requirement is applied and all candidates passing this requirement are346
kept. The signal efficiency after applying this selection is 32% and 18% for B0 → K0S ν ¯ν347
and B0 → K∗0ν ¯ν decays, respectively.
Parameter Values
B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
Number of trees 4000 2000 2000
Tree depth 4 2 3
Subsample 0.87 0.5 0.3
Learning rate 0.2 0.2 0.01
Table 7: FastBDT parameters used for BDT1 training.
348
0.0 0.2 0.4 0.6 0.8 1.0
BDT1
102
103
104
105
106
107
Events
Belle II simulation
```
B 0→K 0S ν¯ν Signal (train)Background (train)
```
```
Signal (test)
```
```
Background (test)
```
0.0 0.2 0.4 0.6 0.8 1.0
BDT1
103
104
105
106
Events
```
B 0→K ∗0ν¯ν Signal (train)Background (train)
```
```
Signal (test)
```
```
Background (test)
```
```
Figure 5: BDT1 output for the train and test samples for (left) B0 → K0S ν ¯ν and (right)
```
B0 → K∗0ν ¯ν channel.
6.1.2 B+ → K∗+ν ¯ν349
For the first classifier, BDT1, we employ an iterative procedure to select the variables350
with highest feature importance in the xgboost framework. After each iteration of the351
training, the number of training variable is halved, keeping only the variables with higher352
feature importance. In each iteration the random seed for training is modified. The353
training parameters are summarized in Table 7.354
18
We converge on the 11 most discriminating variables for both K∗+ decay channels.355
They are the K∗+ mass and multiplicity, the π0 mass before vertex fit and angle between356
its daughters, the momenta of the K0S and π0 in the K∗+ rest frame, the beam-constrained357
mass, transverse momentum and number of tracks and photons in the ROE, the modified358
Fox-Wolfram moment Hoo0 and the squared momenta transfer assuming semileptonic B359
```
decays (weQ2lnuSimple). We train BDT1 simultaneously for both K∗+ decay channels360
```
using the combined set of variables and observed no loss in performance.361
The B candidate selection is further restricted among the remaining five candidates.362
We compare selections according to maximal BDT1 output and minimal q2 and observe363
```
a higher signal efficiency for BDT1 (Figure 6). We choose to select two B candidates364
```
according to maximal BDT1 values.365
1 2 3 4 5
number of candidates
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
signal efficiency
signal
1 2 3 4 5
number of candidates
0.0
0.5
1.0
1.5
2.0
2.5
3.0
number events [arb. units]
×107 background
selected by max. BDT1selected by min. q2
Figure 6: Signal efficiencies and background suppression for candidate selection according
to maximal BDT1 output or minimal q2 before background suppression cut.
0.0 0.2 0.4 0.6 0.8 1.0
BDT1
101
102
103
104
105
106
Events
K* +
```
Signal (train)
```
```
Signal (test)
```
```
Background (train)
```
```
Background (test)
```
Figure 7: BDT1 output for the train and test samples for B+ → K∗+ν ¯ν channel.
```
6.2 Second-level filter (BDT2)366
```
BDT1 alone is not sufficient to separate signal and background. We apply another clas-367
sifier, BDT2, to boost the background suppression performance. First, we apply a loose368
19
requirement on the BDT1 output > 0.9. Then, we reconstruct train and test samples369
```
for each of the decay modes; both train and test samples correspond to 200 fb−1 of inte-370
```
grated luminosity. The BDT2 variables are different for each channel, they are all listed371
in Appendix A. There are 56, 40, and 73 input variables for B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν,372
and B+ → K∗+ν ¯ν, respectively. Figure 8 shows the distributions of the three most dis-373
criminating observables used in the BDT2 for each channel, reconstructed in data and374
simulation.375
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.9875 0.9900 0.9925 0.9950 0.9975 1.0000Kshort_cosAngleBetweenMomentumAndVertexVector0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.4 0.6 0.8 1.0cosTBTO0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0weMissPTheta_ipMask_00.8
1.01.2DATARDMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.85 0.90 0.95B_sig_Kstar0_M0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.00 0.05 0.10B_sig_KSFWVariables_hso020.75
1.001.25DATAMC
0
1
2
3
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.01 0.02 0.03B_sig_KSFWVariables_hoo20.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
2.0 1.5 1.0 0.5 0.0 0.5 1.0roeDeltae0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
6
7
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.2 0.4 0.6 0.8cosTBTO0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.000 0.025 0.050 0.075 0.100 0.125 0.150KSFWVariables_hso220.8
1.0
1.2
Data/Sim.
```
Figure 8: Most discriminating BDT2 input variables for (top) B0 → K0S ν ¯ν, (middle) B0 →
```
```
K∗0ν ¯ν, and (bottom) B+ → K∗+ν ¯ν candidates reconstructed in (dots) data and (solid
```
```
histograms) run-dependent simulation. The signal region is kept blinded by applying
```
BDT1 < 0.99 selection.
The distributions of all BDT2 input variables for all decay modes are in Appendix B.376
All the selected variables have small correlation with q2rec and good data-simulation agree-377
ment. The variable selection was done by iteratively removing variables from the training378
while checking the classification performance.379
We use XGBoost library to train the BDT2 classifier. The classifier parameters are380
given in Table 8. Figure 9 shows that with the chosen classifier parameters, the overfit-381
20
ting is under control. Figure 10 shows the expected significance as a function of signal382
efficiency when selecting with BDT1 alone and with the use of BDT2 on top of BDT1.383
The expected significance is given for 365 fb−1 of integrated luminosity. We see a good384
performance for B0 → K0S ν ¯ν and B0 → K∗0ν ¯ν decays, and a slightly worse performance385
for B+ → K∗+ν ¯ν decay mode due to large combinatorial background coming from neutral386
pion and its low reconstruction efficiency. The right-most points on Figure 10 correspond387
to the state of the selection after the requirement BDT1 > 0.9 : a signal efficiency of388
approximately 32% for B0 → K0S ν ¯ν, 18% for B0 → K∗0ν ¯ν, and 11.1% for B+ → K∗+ν ¯ν.389
390
Parameter Values
B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
Number of trees 4000 2000 2895
Tree depth 4 3 5
Subsample 0.87 0.5 0.36
Variable sampling rate - - 0.93
Learning rate 0.2 0.2 0.07
Table 8: XGBoost parameters used for BDT2 training.
Instead of BDT2, two deep neural network architectures are considered as described391
in Appendix Q. They use an identical set of input variables as the BDT2. The neural392
```
networks show similar or better performance compared to BDTs; at the moment, we393
```
consider them a cross-check for the BDT-based analysis.394
21
0.0 0.2 0.4 0.6 0.8 1.0
BDT2
104
105
Events
```
K0S Background (train)
```
```
Background (test)
```
```
Signal (train)
```
```
Signal (test)
```
0.0 0.2 0.4 0.6 0.8 1.0
BDT2
103
104
105
Events
```
B 0→K ∗0ν¯ν Signal (train)Background (train)
```
```
Signal (test)
```
```
Background (test)
```
0.0 0.2 0.4 0.6 0.8 1.0
BDT2
103
104
105
106
Events
K* +
```
Signal (train)Signal (test)
```
```
Background (train)Background (test)
```
Figure 9: BDT2 output for two independent samples of same size for the different channels.
The samples are restricted to BDT1 > 0.9 range.
22
0.0 0.1 0.2 0.3
Efficiency
0.0
0.2
0.4
0.6
S/
√
S + B
B 0→K 0S ν¯ν
BDT1
BDT2
0.00 0.02 0.04 0.06 0.08 0.10
Efficiency
0.0
0.2
0.4
0.6
S/√
S + B
B + →K ∗ + ν¯ν
BDT1
BDT2
Figure 10: Signal significance as a function of efficiency for the different channels after
the requirement BDT1 > 0.9. The expectation is for 365 fb−1.
23
7 Signal region definition395
To work with a more physical variable than the BDT2 output, the upper threshold on396
```
the classifier output is mapped into an expected signal efficiency εsig (Figure 11). Using397
```
the simulated signal sample, the BDT2 variable is mapped to the complement of the398
integrated signal-selection efficiency,399
```
η(BDT2) ≡ 1 −
```
Z 1
BDT2
```
ϵ(b)db , (2)400
```
```
where ϵ(b) is the total signal-selection efficiency density for the BDT2 value b. In this way401
```
```
the distribution of η(BDT2) for simulated signal events is uniform. As an example, the402
```
requirement η > 0.92 defines the region where 8% of the true signal events are expected403
to survive the BDT2 selection, as shown in Fig. 11.404
```
The signal region (SR) is divided into different intervals (bins) in η(BDT2) × q2rec space405
```
as specified in Table 9. The SR and bin boundaries vary between channels. For the406
B0 → K0S ν ¯ν channel, we choose them to be the same as in the B+ → K+ν ¯ν analysis. For407
```
the B → K∗νν channels, we optimize the η(BDT2) selection requirement and binning by408
```
minimizing the expected statistical uncertainty on the physics parameter of interest, the409
signal strength µ, using Asimov samples.410
At this stage, the final selection of the best candidate is performed. Only the candidate411
with the best BDT2 for a given event is selected.412
Decay Bin boundaries
```
(η(BDT2) × q2)
```
B0 → K0S ν ¯ν [[0.92, 0.94, 0.96, 0.98, 1.00] × [-1, 4, 8, 25]]
B0 → K∗0ν ¯ν [[0.95, 0.96, 0.97, 0.98, 0.99, 1.00] × [-1, 4, 8, 25]]
B+ → K∗+ν ¯ν [[0.97 , 0.975, 0.98 , 0.985, 0.99 , 0.995, 1.00] × [-1, 4, 8, 25]]
Table 9: Definition of the signal region.
Table 10 and Table 11 shows the signal efficiency and purity for the three channels413
at each selection point, and the efficiency as a function of q2 and cos θ [Cosine of angle414
```
between the K∗ flight direction in the B rest frame and the K (that is the K∗ daughter)415
```
flight direction in the Kπ rest frame] for each channel are demonstrated in Fig. 13. The416
q2 resolution in the signal region across all channels is presented in Fig. 15, showing a417
broader resolution at lower q2 values.418
We also evaluate the self-crossfeed fraction in the signal region for all channels. Self-419
crossfeed events are defined as those in the signal MC that are not truth-matched. The420
fractions, relative to the total signal efficiency in the signal region, are found to be 1%,421
8.7%, and 10.9% for the B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channels, respec-422
tively.423
```
4The requirement on pionID was lately added in B+ → K∗+(→ K0S π+)νν to improve π+ purity. It is
```
applied before BDT2 training.
24
0.0 0.2 0.4 0.6 0.8 1.0
BDT2
0.0
0.1
0.2
0.3
0.4
Signal efficiency
B 0→K 0S ν¯ν
Belle II simulation
Expectation
Fit
Figure 11: Mapping from threshold on the BDT2 output to signal efficiency for the
B0 → K0S ν ¯ν channel.
1 4 8 25
q2rec[GeV2/c4]
0.92
0.94
0.96
0.98
1.00
```
(BDT
```
```
2)
```
1 2 3
4 5 6
7 8 9
10 11 12
1 4 8 25
q2rec[GeV2/c4]
0.95
0.96
0.97
0.98
0.99
1.00
```
(BDT
```
```
2)
```
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
1 4 8 25q2
rec[GeV2/c4]
0.970
0.975
0.980
0.985
0.990
0.995
1.000
```
(BDT
```
```
2)
```
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
16 17 18
```
Figure 12: η(BDT2) × q2 binning in the signal region for the (left) B0 → K0S ν ¯ν, (middle)
```
```
B0 → K∗0ν ¯ν, and (left) B+ → K∗+ν ¯ν channels.
```
Selection stage B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
Basic event selection 43.6% 19.5% 12.8%
BDT1 > 0.9 32% 18% 11.1%
pionID > 0.054 - - 10.6%
```
Signal search region (BDT2) 8% 5% 3%
```
Highest purity signal search region 2% 1% 0.5%
Table 10: Signal selection efficiency at various stages of the selection. Reference for
B+ → K∗+ν ¯ν and B0 → K0S ν ¯ν include K0S → π0π0 and K0 → K0L.
Selection stage B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
BDT1 > 0.9 0.008% 0.0075% 0.00158%
pionID > 0.054 - - 0.00172%
```
Signal search region (BDT2) 0.548% 0.4122% 0.165%
```
Highest purity signal search region 2.608% 2.4577% 0.876%
```
Table 11: Purity ( ss+b ) at various stages of the selection for all channels.
```
25
0 2 4 6 8 10 12 14 16 18 20
q2 [GeV2/c4]
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Signal efficiency [%]
Belle II preliminary simulation
B 0→K 0S ν¯ν
Statistical uncertainty
1 1 3 5 7 9 11 13 15 17 19 21
q2 [GeV2/c4]
0
2
4
6
8
10
Signal efficiency [%]
Belle II preliminary simulationB 0→K ∗0ν¯ν
Statistical uncertainty
1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 1.0
cos
0
2
4
6
8
Signal efficiency [%]
Belle II preliminary simulationB 0→K ∗0ν¯ν
Statistical uncertainty
0 2 4 6 8 10 12 14 16 18 20
q2 [GeV2/c4]
0
1
2
3
4
5
6
Signal efficiency [%]
Belle II preliminary simulation
B + →K ∗ + ν¯ν
Statistical uncertainty
1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 1.0
cosθ
0
1
2
3
4
5
Signal efficiency [%]
Belle II preliminary simulation
B + →K ∗ + ν¯ν
Statistical uncertainty
Figure 13: Signal efficiency as a function of q2 and cos θ for all channels, determined from
the signal region selection. The cos θ distributions are provided for vector mesons only.
26
1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 1.0
```
cos (K* + K + 0 mode)
```
0
2
4
6
8
Signal efficiency [%]
Belle II preliminary simulationB + →K ∗ + ν¯ν
Statistical uncertainty
1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 1.0
```
cos (K* + K0S + mode)
```
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Signal efficiency [%]
Belle II preliminary simulationB + →K ∗ + ν¯ν
Statistical uncertainty
Figure 14: Signal efficiency as a function of cos θ shown separately for the two B+ →
K∗+ν ¯ν modes.
We also analyzed the two K∗+ decay modes separately. The signal efficiency as a424
```
function of q2 appears nearly identical for both K∗+ channels and is consistent with the425
```
combined result shown in Fig. 13. However, when checking efficiency as a function of426
cos θ, we observed notable differences, as shown in Fig. 14.427
Here, cos θ is defined as the cosine of the angle between the K∗+ momentum in the428
B rest frame and the kaon momentum in the Kπ rest frame. At the generator level, the429
cos θ distributions are symmetric about zero and consistent across both K∗+ modes.430
After reconstruction, however, we observed that the K∗+ → K+π0 mode becomes431
more asymmetric: the efficiency for cos θ < 0 is significantly higher than for cos θ > 0,432
shown in Fig. 16. This asymmetry arises because when cos θ < 0, the kaon is emitted433
opposite to the B direction, causing the π0 to be boosted along the B direction, resulting434
in higher energy. High-energy π0s are more likely to pass BDT selection, as low-energy435
π0s have reduced purity and are more likely to be rejected.436
In contrast, for the K∗+ → K0S π+ mode, the selection efficiency for the π+ is less437
sensitive to its energy, regardless of boost direction. As a result, the efficiency vs. cos θ438
distribution for this mode remains more symmetric.439
27
5 0 5 10 15 20 25
q2rec [GeV2/c4]
5
0
5
10
15
20
25
q2gen
[GeV
2/c
4]
B 0→K 0S ν¯ν
Belle II simulation
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×104
4 2 0 2 4
q2rec q2gen [GeV2/c4]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×104
B 0→K 0S ν¯ν
Belle II simulation
0 5 10 15
q2rec
2.5
5.0
7.5
10.0
12.5
15.0
17.5
q2gen
B + K* +
0
25
50
75
100
125
150
175
Events
4 3 2 1 0 1 2 3 4
q2rec q2gen
0
500
1000
1500
2000
2500
3000
3500
4000
Events
B + K* +
```
Figure 15: Resolution of q2 in the signal region for (top) B0 → K0S ν ¯ν, (middle) B0 →
```
```
K∗0ν ¯ν and (bottom) B+ → K∗+ν ¯ν channels, respectively.
```
28
Figure 16: Energy of pions in the two B+ → K∗+ν ¯ν modes for different cos θ regions:
```
(left) B+ → K∗+(K+π0)ν ¯ν and (right) B+ → K∗+(π+K0S )ν ¯ν.
```
29
8 Signal validation440
8.1 Signal efficiency validation441
All the analyses are developed using simulated samples. However, small but potentially442
harmful discrepancies are known to exist between the data and simulation. In order to443
ensure a reliable estimation of the desired parameters in data, it is essential to identify444
and correct such discrepancies. We study the efficiency of signal selection using modified445
```
B → K(∗)J/ψ events reconstructed in data and simulation. We use MC15RI samples for446
```
simulation.447
The data and simulation samples are modified at the UDST level, using dedicated448
J/ψ and signal simulated sample skims. The steps of the method are enumerated below:449
1. A skim is used to select events containing B → K(∗)J/ψ(→ ℓℓ) decays and to tag450
them in both data and simulated samples.451
2. For the tagged decay, the vertex and momentum information are stored in text files452
using the HepMCv2 format, while tracks, calorimeter energy deposits, and other453
objects are removed from the mdst files.454
3. The signal B decays are simulated using EVTGEN, with the kinematic information455
taken from the HepMCv2 file. The simulated B mesons are forced to decay at the456
stored decay vertex by setting the B-meson lifetime to zero.457
4. The ROE file from step 2 and the simulated signal B meson from step 3 are merged458
to create the embedded sample.459
The signal embedding procedure is applied to both data and simulation and the num-460
ber of events used in both are summarized in Table 12.461
Channel Number of events in embedded sample
MC Data
B0 → K0S ν ¯ν 13803+9549 K0S J/ψ[→µ+µ−] 2031 + K∗0J/ψ[→µ+µ−] 3981
B0 → K∗0ν ¯ν 90000 K∗0J/ψ [→µ+µ−] 3985 + K∗0J/ψ [→e+e−] 2245
B+ → K∗+ν ¯ν 9629 K+J/ψ[→µ+µ−] 7258
Table 12: Number of events in embedded samples.
The embedded samples undergo standard event reconstruction for each channel. Signal462
efficiency after all selection criteria is validated for both embedded data and simulation.463
The resulting data-to-simulation ratios for all channels are summarized in Table 13. For464
the B0 → K∗0ν ¯ν channel, additional J/ψ → ee events are included in the embedding465
procedure to enhance statistical precision.466
8.2 Signal BDT inputs validation467
We validate the ROE-related input observables used in the BDT2 for the signal component468
by comparing their distributions, q2rec, and BDT2 inefficiency, in embedded data, embed-469
30
```
Mode Efficiency (%) Data-MC ratio
```
Data Simulation
B0 → K0S ν ¯ν 8.33 ± 0.36 8.10 ± 0.23 1.03 ± 0.05
B0 → K∗0ν ¯ν 4.05 ± 0.07 4.03 ± 0.25 0.99 ± 0.06
B+ → K∗+ν ¯ν 3.54 ± 0.22 3.60 ± 0.19 0.98 ± 0.08
Table 13: Ratio of selection efficiency in the signal region for the embedded data and MC
samples.
```
ded simulation, and signal simulation (Fig. 17). We observe good agreement between470
```
embedded data and embedded simulation for all observables.471
For the B0 → K∗0ν ¯ν channel, we investigate possible data-simulation discrepancies in472
K∗0-related observables, e.g. the K∗0 χ2 vertex probability distribution.473
We employ a method similar to signal embedding, referred to as pruning, in which474
```
modified B+ → ¯D0(→ K+π−)µν events reconstructed from both data and simulation are475
```
used. In this procedure, the muon is removed from the skimmed event. Assuming that476
the ¯D0 → K+π− decay shares similar kinematic properties with the K∗0 → K+π− decay,477
we compare the χ2 vertex probability and BDT2 inefficiency distributions between the478
pruned data and pruned simulation. To enable a fair comparison, the D mass distribution479
is adjusted to mimic that of the K∗0. Figure 18 shows the comparisons. We do not observe480
any discrepancy.481
31
0 5 10 15 20 25
q2rec
0
25
50
75
100
125
Candidates
Embedded MC
Signal MC
Embedded data
0.75 0.80 0.85 0.90 0.95 1.00
BDT2 inefficiency
0
10
20
30
40
50
60
Candidates
Embedded MC
Signal MC
Embedded data
0
10
20
30
40
50
60
Events
```
(BDT2)>0.85
```
B0 K*0
Embedding MC
Embedding DATA
0 5 10 15
B_sig_H_reconstructed_q2
0
1
2
embeddingdataembeddingMC
0
10
20
30
40
50
Events
```
(BDT2)>0.85
```
B0 K*0
Embedding MC
Embedding DATA
0.875 0.900 0.925 0.950 0.975
BDT2_Bzero2KstarZero_v53_signal_inefficiency
0
1
2
embeddingdataembeddingMC
0 5 10 15 20
reconstructed q2
0
20
40
60
80
counts [arb. units]embedded MC
signal MC, isSignal
embedded Data, normalized
0.90 0.92 0.94 0.96 0.98 1.00
```
(BDT2)
```
0
20
40
60
80
100
120
counts [arb. units]
embedded MC
signal MC, isSignal
embedded Data, normalized
```
Figure 17: Distribution of (left) q2rec and (right) BDT2 inefficiency or ROE Mbc for embed-
```
```
ded data, embedded simulation and signal simulation for the (top) B0 → K0S ν ¯ν, (middle)
```
```
B0 → K∗0ν ¯ν, and (bottom) B+ → K∗+ν ¯ν channel.
```
32
0.0 0.2 0.8 1.00.4 0.6K*0 vertex probability0
500
1000
1500
2000
2500
Candidates
```
-pruned MC (B + D0( K + ) + )
```
```
Signal MC (B0 K*0( K + ) )
```
```
-pruned data (B + D0( K + ) + )
```
0.95 1.000.96 0.97 0.98 0.990
250
500
750
1000
1250
1500
1750
Candidates
```
-pruned MC (B + D0( K + ) + )
```
```
Signal MC (B0 K*0( K + ) )
```
```
-pruned data (B + D0( K + ) + )
```
```
η(BDT 2)
```
```
Figure 18: Distribution in the signal region of (left) χ2 vertex probability and (right)
```
```
BDT2 inefficiency for (dots) pruned B+ → ¯D0(→ K+π−)µν data, (blue) pruned B+ →
```
```
¯D0(→ K+π−)µν simulation, and (red) B0 → K∗0ν ¯ν signal simulation.
```
33
9 Continuum background validation using off-resonance482
data483
We check whether the continuum simulation provides a good description of the off-484
resonance data. For the study, we use off-resonance data corresponding to 42.3fb−1 of485
integrated luminosity and simulation corresponding to four times that of the data lumi-486
```
nosity. From a comparison of all the relevant variable distributions (BDT2 input variables487
```
```
+BDT2 output +q2rec ) obtained in off-resonance data with those obtained in continuum488
```
simulation, we observe partial discrepancies. We also observe that the data-to-simulation489
```
normalization ratio exceeds one (1.14, 1.09, and 1.03 for B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and490
```
```
B+ → K∗+ν ¯ν channels, respectively).491
```
To correct the distribution mismodelings, we reweight the continuum simulation us-492
ing a multivariate classifier, BDTc, based on XGBoost. We train BDTc with an off-493
```
resonance simulation corresponding to 170 fb−1 of integrated luminosity (four times as494
```
```
of off-resonance data) and off-resonance data corresponding to 42.3 fb−1 of integrated495
```
```
luminosity. Both samples are restricted to the BDT1 > 0.9 and η (BDT2) > 0.75, > 0.85,496
```
> 0.9 region for the B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channels, respectively.497
The BDTc parameters, listed in Table 14, are chosen to minimize overfitting, since the498
number of data events are limited. The classifier is trained taking simulation as back-499
```
ground and data as signal. Given the output p of the classifier, the event weight p/(1 − p)500
```
is applied to the simulated continuum events.501
Parameter Value
Number of trees 2000
Tree depth 2
Subsample 0.1
Learning rate 0.01
Table 14: BDTc parameter values
Figure 19 shows the output of the BDTc classifier, which is trained with the BDT2502
input variables, the BDT2 output, and q2rec. The data distribution is shifted with respect503
```
to the simulation (Figure 19, left). However, by applying the weight p/(1 − p) to the504
```
```
simulation, the difference between the simulation and the data is reduced (Figure 19,505
```
```
right).506
```
After reweighting of the continuum simulation, an overall better data-simulation agree-507
```
ment is observed for all variables; some examples are shown in Figures 20, 21 and 22.508
```
Figure 23 shows the distributions of candidates reconstructed in the off-resonance509
data and in the reweighted continuum simulation in the signal search region. Data and510
simulation distributions are in a good agreement for all the three channels, but we observe511
a normalization factor between data and simulation of 1.23 ± 0.07, 1.1 ± 0.03, and 0.950 ±512
0.033 in the signal region, for the B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channel,513
respectively. These normalization discrepancies are corrected for in the figure. At this514
stage, the normalization factor for B+ → K+ν ¯ν was 1.40 ± 0.05.515
34
0.0 0.2 0.4 0.6 0.8 1.0
BDTc
0
1
2
3
4
5
A.U.
```
K0S Data (train)
```
```
Data (test)
```
```
MC (train)
```
```
MC (test)
```
0.0 0.2 0.4 0.6 0.8 1.0
BDTc
0
1
2
3
4
A.U.
```
K0S Data (train)
```
```
Data (test)
```
```
MC (train)
```
```
MC (test)
```
```
Figure 19: BDTc classifier outputs for training and testing samples (normalized) for
```
the B0 → K0S ν ¯ν channel. Here, the signal is the data sample and the background is
the simulated sample. On the right, the simulated samples are reweighted according to
```
p/(1 − p), where p is the output of BDTc.
```
0
1000
2000
3000
4000
Candidates
Belle II preliminary L dt = 42.6 fb 1
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
foxWolframR2
0.8
1.0
1.2
DATARDMC
0
1000
2000
3000
4000
Candidates
Belle II preliminary L dt = 42.6 fb 1
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
foxWolframR2
0.8
1.0
1.2
DATARDMC
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary L dt = 42.6 fb 1
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0 5 10 15 20 25
q2rec
0.8
1.0
1.2
DATARDMC
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary L dt = 42.6 fb 1
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0 5 10 15 20 25
q2rec
0.8
1.0
1.2
DATARDMC
```
Figure 20: Distribution of (top) Fox-Wolfram R2 moment and (bottom) q2rec obtained
```
```
for B0 → K0S ν ¯ν decays reconstructed in (black dots) off-resonance data and (colored
```
```
histograms) continuum simulation. The left figures obtained before reweighting of the
```
continuum simulation, the plots on the rights obtained after reweighting of the continuum
simulation. A 14% normalization factor is applied to all the distributions.
35
0
1000
2000
3000
Event density
Belle II preliminary L dt = 42.3 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15
B_sig_H_reconstructed_q2
0.75
1.00
1.25
DATAMC
0
1000
2000
3000
Event density
Belle II preliminary L dt = 42.3 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15
B_sig_H_reconstructed_q2
0.75
1.00
1.25
DATAMC
```
Figure 21: Distribution of (top) Fox-Wolfram R2 moment and (bottom) q2rec obtained
```
```
for B0 → K∗0ν ¯ν decays reconstructed in (black dots) off-resonance data and (colored
```
```
histograms) continuum simulation. The left figures obtained before reweighting of the
```
continuum simulation, the plots on the rights obtained after reweighting of the continuum
simulation.
36
0.00
0.25
0.50
0.75
1.00
1.25
Entries
×104 Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6
foxWolframR2
0.8
1.0
1.2
Data/Sim.
0.00
0.25
0.50
0.75
1.00
1.25
Entries
×104 Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6
foxWolframR2
0.8
1.0
1.2
Data/Sim.
0
2000
4000
6000
8000
Entries
Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15
q2rec
0.8
1.0
1.2
Data/Sim.
0
2000
4000
6000
8000
Entries
Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15
q2rec
0.8
1.0
1.2
Data/Sim.
```
Figure 22: Distribution of (top) Fox-Wolfram R2 moment and (bottom) q2rec obtained
```
```
for B+ → K∗+ν ¯ν decays reconstructed in (black dots) off-resonance data and (colored
```
```
histograms) continuum simulation. The left figures obtained before reweighting of the
```
continuum simulation, the plots on the rights obtained after reweighting of the continuum
simulation. A 3% normalization factor is applied to all the distributions.
37
0
50
100
150
200
Entries
Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 2 4 6 8 10 12
signal region bin number
0.75
1.00
1.25
DataPred.
0
100
200
300
Entries
Belle II preliminary L dt = 42.6 fb 1
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15
signal region bin number
0.75
1.00
1.25
DataPred.
```
Figure 23: Distribution of (top left) B0 → K0S ν ¯ν, (top right) B0 → K∗0ν ¯ν, and (bottom)
```
```
B+ → K∗+ν ¯ν candidates reconstructed in the signal search region obtained in (black dots)
```
```
off-resonance data and (colored histograms) reweighted continuum simulation. Simulation
```
is scaled up by a factor of 1.23 ± 0.07, 1.10 ± 0.03, and 0.950 ± 0.033 respectively to correct
for the observed normalization discrepancies.
38
10 Background composition and validation516
```
We use signal sideband, mass sideband and control samples, such as, D → K(∗)(S)X, where517
```
```
K(∗)(S) is the signal candidate, to validate our main backgrounds.518
```
10.1 Background composition in the signal region519
We check the final background composition in the signal region for all the channels.520
Table 15 and 16 show the fraction of each background type present in the signal region and521
```
high sensitive regions, respectively. The high sensitive regions are defined as η(BDT2) >522
```
```
0.98, η(BDT2) > 0.99 and η(BDT2) > 0.995 for the channels B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν523
```
and B+ → K∗+ν ¯ν, respectively. We observe a reduction of the continuum component in524
the high-sensitivity region.525
```
Background type Fraction(%)
```
B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
B+B− 13.6 30.4 32.0
B0B0 28.6 31.8 30.3
cc 30.0 19.5 20.6
ss 17.6 9.4 8.2
dd 3.6 2.7 2.3
uu 4.9 5.1 6.2
τ +τ − 1.7 1.1 0.5
Table 15: Background composition in the signal region.
```
Background type Fraction(%)
```
B0 → K0S ν ¯ν B0 → K∗0ν ¯ν B+ → K∗+ν ¯ν
B+B− 18.8 40.5 51.0
B0B0 38.8 43.3 31.7
cc 16.8 7.6 8.2
ss 15.7 4.6 4.6
dd 2.6 1.1 0.9
uu 3.2 2.4 3.2
τ +τ − 4.2 0.5 0.2
Table 16: Background composition in the high sensitivity region.
10.2 Validation in BDT2 sideband526
We perform a validation study in a BDT2 sideband near the signal region, dominated by527
background and containing only a negligible amount of signal events. The background528
composition is different from the signal region composition, having a larger continuum529
39
component with respect to B ¯B backgrounds. The sideband region corresponds to the530
```
efficiency quantile interval (0.75, 0.92), (0.85, 0.95), and (0.90, 0.97) for the B0 → K0S ν ¯ν,531
```
B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channel, respectively. We compare data and simulation532
distributions of the BDT2 training variables and of the observables chosen for the final533
```
fit. Figure 24 shows the latter: q2rec and η (BDT2). In these plots, we correct continuum534
```
for the remaining normalization discrepancy seen in the off-resonance after continuum535
correction.536
For the B0 → K0S ν ¯ν channel, we observe good agreement between data and simulation537
for all the observables. For the B0 → K∗0ν ¯ν, we observe a residual 5% discrepancy be-538
tween data and simulation. For the B+ → K∗+ν ¯ν, we observe a residual 3.5% discrepancy539
between data and simulation. We show the data-MC agreement of four most discriminat-540
ing BDT2 variables for all channels in Fig. 25, Fig. 26 and Fig. 27. Distributions of all541
other variables are given in Ref. [21].542
10.3 Validation in mass sideband543
For the B0 → K0S ν ¯ν channel, we observe that almost all the reconstructed K0S candidates544
are real K0S mesons. For the B0 → K∗0ν ¯ν and B+ → K∗+ν ¯ν channels, we observe instead545
```
a large component of misreconstructed (fake) K∗0,+ mesons due to wrong combinations546
```
of kaons and pions, that can come from the same B meson, from both B mesons in the547
```
Υ(4S) decay, or from the continuum. To validate this fake K∗0,+ component, that is548
```
possibly not well reproduced in MC, we compare data and simulation distributions of the549
observables of interest in mass-sideband control regions, defined as [0.75 − 0.8] GeV and550
[1.0 − 1.05] GeV for the B0 → K∗0ν ¯ν channel, and [0.7 − 0.8] GeV and [1.0 − 1.1] GeV551
for the B+ → K∗+ν ¯ν channel. Before applying the BDTs, we fix the K∗0,+ mass value552
of each reconstructed candidate to the corresponding PDG mass, as the Kπ invariant553
mass is one of the inputs used in the neural network. Figure 28 shows the distributions554
```
of η (BDT2) and K∗0,+ reconstructed mass (applied η (BDT2) > 0.95 for K∗0 channel) for555
```
candidates reconstructed in the mass sidebands. Distributions of all other variables are556
given in Ref. [22].557
We correct continuum for the remaining normalization discrepancy seen in the off-558
resonance after continuum correction. We observe a 2.5% excess in simulation with respect559
to data for the B0 → K∗0ν ¯ν channel. For B+ → K∗+ν ¯ν we observe a residual 1.5% excess560
```
(data over simulation) after applying PID and continuum corrections.561
```
```
10.4 Validation using D → K(∗)X control sample562
```
Studies of the signal-enriched regions show that large fraction of background originates563
```
from D-meson decays. The D meson decaying into D → K(∗)X can produce the signal-564
```
candidate kaon in B+ → K+ν ¯ν and B0 → K0S ν ¯ν decays as well as K∗ or a kaon that is565
combined with a pion from other B decays to form K∗ in B+ → K∗+ν ¯ν and B0 → K∗0ν ¯ν566
decays. In the published B+ → K+ν ¯ν analysis, these decays are suppressed by the567
dedicated D-meson veto variables, which are based on pairing of the signal candidate K+568
with one or two charged tracks from the rest of event. We validate these backgrounds by569
40
0
2
4
6
Candidates
×104 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.750 0.775 0.800 0.825 0.850 0.875 0.900
BDT2 inefficiency
0.75
1.00
1.25
DATARDMC
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0 5 10 15 20 25
q2rec
0.75
1.00
1.25
DATARDMC
0
2
4
6
8
Events
×105 Belle II preliminary L dt = 89.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.90 0.91 0.92 0.93 0.94 0.95 0.96 0.97
```
(BDT2)
```
0.8
1.0
1.2
Data/MCrd
0
1
2
3
Events
×105 Belle II preliminary L dt = 89.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 5 10 15 20
q2rec
0.8
1.0
1.2
Data/MCrd
```
Figure 24: Distributions of BDT2 signal inefficiency (left) and q2rec (right) for (top) B0 →
```
```
K0S ν ¯ν, (middle) B0 → K∗0ν ¯ν, and (bottom) B+ → K∗+ν ¯ν candidates reconstructed in
```
the BDT2 sideband. We correct continuum for the remaining normalization discrepancy
seen in the off-resonance after continuum correction.
41
0
1
2
3
4
Candidates
×105 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.992 0.994 0.996 0.998 1.000
Kshort_cosAngleBetweenMomentumAndVertexVector
0.75
1.00
1.25
DATARDMC
0
1
2
3
Candidates
×104 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
cosTBTO
0.75
1.00
1.25
DATARDMC
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
weMissPTheta_ipMask_0
0.75
1.00
1.25
DATARDMC
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×105 Belle II preliminary L dt = 365 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Model stat. unc.
Data
25 26 27 28
weQ2lnuSimple_ipMask_2
0.75
1.00
1.25
DATARDMC
Figure 25: Data-MC comparison of four most discriminating BDT2 variables in the BDT2
side-band region for the B0 → K0S ν ¯ν channel.
42
Figure 26: Data-MC comparison of four most discriminating BDT2 variables in the BDT2
side-band region for the B0 → K∗0ν ¯ν channel.
43
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 365.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
2.5 2.0 1.5 1.0 0.5 0.0 0.5
E
0.8
1.0
1.2
Data/MCrd
0.0
0.5
1.0
1.5
Events
×106 Belle II preliminary L dt = 365.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0 1 2 3 4
Q2tot
0.8
1.0
1.2
Data/MCrd
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 365.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.2 0.4 0.6 0.8
cosTBTO
0.8
1.0
1.2
Data/MCrd
0
1
2
3
Events
×105 Belle II preliminary L dt = 365.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.00 0.05 0.10 0.15
Hso22
0.8
1.0
1.2
Data/MCrd
Figure 27: Data-MC comparison of four most discriminating BDT2 variables in the BDT2
side-band region for the B+ → K∗+ν ¯ν channel.
44
0
1000
2000
3000
4000
5000
6000
Candidates
Belle II preliminary
L dt = 365 fb-1
B 0→K ∗0ν¯ν
B 0→K ∗0ν¯ν
B 0B0
B + B −
Continuum
Sim. stat. unc.
Data
0.95 0.96 0.97 0.98 0.99 1.00
```
η(BDT2)
```
0.5
1.0
1.5
DATAMC
Kstar0_M
0
1000
2000
3000
4000
5000
Events
Belle II preliminary L dt = 365 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.75 0.80 0.85 0.90 0.95 1.00 1.050.75
1.00
1.25
data/MCRD
0
100
200
300
400
500
Events
Belle II preliminary L dt = 89.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.970 0.975 0.980 0.985 0.990 0.995 1.000
```
(BDT2)
```
0.8
1.0
1.2
Data/MCrd
0
100
200
300
400
500
Events
Belle II preliminary L dt = 89.0 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Model stat. unc.
Data
0.8 0.9 1.0
K* + mass
0.8
1.0
1.2
Data/MCrd
```
Figure 28: Distributions of BDT2 signal inefficiency (left) and K∗0,+ reconstructed mass
```
```
(right) for (top) B0 → K∗0ν ¯ν and (bottom) B+ → K∗+ν ¯ν candidates reconstructed in
```
the mass sideband. We correct continuum for the remaining normalization discrepancy
seen in the off-resonance after continuum correction.
45
comparing yields of D candidates, formed using signal K0S or K∗ and tracks from ROE,570
in both data and simulation.571
```
The D0 and D+ decays are built using the signal-candidate kaon (K+ or K0S ) or the572
```
kaon from the signal-candidate K∗ decay. The charged pions are based on all tracks from573
the ROE assuming pion mass hypothesis without PID requirements. For the K∗ modes574
and three-body D meson decays, the pion from the signal-candidate K∗ meson is also575
considered. The π0 candidates are selected using the standard list pi0:eff40 May2020.576
For the semileptonic D decays, the corresponding mass hypothesis and a PID cut of > 0.9577
are used.578
The fully reconstructed hadronic decays are refined by applying an invariant mass579
selection, using a mass window approximately equivalent to 5 standard deviations of the580
mass resolution. For leptonic decays, a loose requirement on a maximum of the invariant581
mass is applied. The decays are summarized in Table 17. The multiple candidates in the582
selected region are removed by selecting a single candidate with the best probability of a583
common vertex fit pvtx.584
Decay Charged particle selection π0 selection Mass range
MeV/c2
D0 → K−π+ ROE pion — |M − MD0 | < 20
D0 → K−π+π0 ROE+SIG pion eff40 May2020 |M − MD0 | < 50
D0 → K−e+νe ROE electron PID> 0.9 — M < 2100
D0 → K−µ+νµ ROE muon PID> 0.9 — M < 2100
D+ → K−π+π+ ROE+SIG pion — |M − MD+ | < 20
D+ → K∗0e+νe ROE electron PID> 0.9 — 1000 < M < 2100
D+ → K∗0µ+νµ ROE muon PID> 0.9 — 1000 < M < 2100
D0 → K−π+π+π− ROE+SIG pion — |M − MD0 | < 20
D+ → K0S e+νe ROE electron PID> 0.9 —
D+ → K0S µ+νµ ROE muon PID> 0.9 —
D0 → K0S π0 ROE pion eff40 May2020 |M − MD0 | < 50
D0 → K0S π+π− ROE pions — |M − MD0 | < 20
D+ → K0S π+ ROE pion — |M − MD+ | < 20
D+ → K0S π+π0 ROE pions eff40 May2020 |M − MD+ | < 40
D+s → K0S π+ ROE pion — 1948 < M < 1988
K∗ → K0S π+ ROE pion — 842 < M < 942
Table 17: D0 and D+ decay modes considered for D-veto suppression variables. SIG
```
pion stands for the pion from the signal-candidate K∗ decay (applicable to K∗ channels
```
```
only). MD0 and MD+ stand for the world-average mass values.
```
Based on these selections, several variables—such as multiplicity, invariant mass, and585
daughter kinematic information—are considered for use in BDT2. Some of these vari-586
ables are retained during the optimization procedure, as detailed in Appendix A and587
Appendix B.588
The invariant mass distributions for D0 and D+ decays are also used to control the589
background induced by charm decays. In the following, these studies are presented for all590
46
four decay modes. For the published B+ → K+ν ¯ν channel, the studies extend into the591
```
signal region. For the other channels, they are performed in a η(BDT2) sideband. These592
```
will be extended to the signal regions as part of the initial box-opening steps.593
10.4.1 B+ → K+ν ¯ν decays594
See Appendix O.595
10.4.2 B0 → K0S ν ¯ν decays596
The primary background for K0S channel in signal region is from mixed B-meson decays,597
where the B meson decays semi-leptonically with D meson in the final state. A detailed598
check of the mixed sample shows that 60% of the K0S originate from D+ decays and 12%599
from D0 decays, both of which mimic the signal.600
601
To validate these main backgrounds, we perform a one-dimensional maximum like-602
```
lihood fit to the invariant masses of D0(K0S π+π−) and D+(K0S π+) candidates in both603
```
```
data and simulation. The fit is performed in the η(BDT2) sideband region, i.e., 0.75 <604
```
```
η(BDT2) < 0.92, and the fit projections are shown in Figs. 29 and 30. We use a double605
```
Gaussian PDF to model the signal and 1st order polynomial to model the background606
```
components, respectively. The mean and the resolution (σ) are free parameters in the fit.607
```
The biasness of the fit is checked by comparing the fitted yield with the true yield, and608
no bias is observed.609
1.85 1.86 1.87 1.88
```
M(K0S + ) [GeV/c2]
```
0
2000
4000
6000
8000
Candidates
Belle II L dt = 1.5 ab 1
totalbackground
signalMC15rd
1.85 1.86 1.87 1.88
```
M(K0S + ) [GeV/c2]
```
0
1000
2000
3000
Candidates
Belle II preliminary L dt = 365 fb 1
totalbackground
signalData
```
Figure 29: Fit projections of D0 → K0S π+π− in simulation (left) and data (right) where
```
K0S is signal K0S while π+ and π− are from the ROE in the B0 → K0S ν ¯ν analysis for the
```
signal sideband region 0.75 < η(BDT2) < 0.92.
```
The yields obtained from the fit are summarized in the Table 18. Since the data-to-610
simulation ratio is close to unity, the validation of these backgrounds is deemed successful.611
10.4.3 B0 → K∗0ν ¯ν decays612
Similar fits are also performed for the B0 → K∗0ν ¯ν analysis. The data and simulation613
```
are restricted to the close-to-signal sideband region with 0.93 < η(BDT2) < 0.95. The614
```
47
1.85 1.86 1.87 1.88 1.89
```
M(K0S + ) [GeV/c2]
```
0
2000
4000
6000
8000
Candidates
Belle II L dt = 1.5 ab 1
totalbackground
signalMC15rd
1.85 1.86 1.87 1.88 1.89
```
M(K0S + ) [GeV/c2]
```
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb 1
totalbackground
signalData
```
Figure 30: Fit projections of D+ → K0S π+ in simulation (left) and data (right) where K0S
```
is signal K0S while π+ is from the ROE in the B0 → K0S ν ¯ν analysis for the signal sideband
```
region 0.75 < η(BDT2) < 0.92.
```
```
Mode Yield Ratio (data/mc)
```
Data MC
D0 → K0S π+π− 8850 ± 295 9418 ± 136 0.94 ± 0.03
D+ → K0S π+ 9275 ± 240 9269 ± 111 1.00 ± 0.03
Table 18: Fit yields in data, simulation and their ratio together with statistical uncer-
```
tainties for D0 → K0S π+π− and D+ → K0S π+ decays in the signal sideband (0.75 <
```
```
η(BDT2) < 0.92) for the B0 → K0S ν ¯ν analysis. The fitted signal yields in simulation are
```
scaled to the data luminosity.
1.85 1.86 1.87 1.88
```
M(K −sig π + ) [GeV/c2]
```
0
20
40
60
80
100
120
140
160
Events/2 MeV/
c2
```
Yield = 608 ± 38
```
total
background
signal
Data
1.85 1.86 1.87 1.88
```
M(K −sig π + ) [GeV/c2]
```
0
100
200
300
400
500
600
Events/2 MeV/
c2
```
Yield = 516 ± 17
```
total
background
signal
MC
```
Figure 31: Fit projections of D0 → K−π+ in data (left) and simulation (right) where K−
```
is a kaon from a K∗0 decay while π+ is from the ROE in the B0 → K∗0ν ¯ν analysis for
```
the close-to-signal sideband region 0.93 < η(BDT2) < 0.95. The fitted signal yields in
```
simulation are scaled to the data luminosity.
48
1.85 1.86 1.87 1.88
```
M(K −sig π + π + ) [GeV/c2]
```
0
50
100
150
200
250
300
Events/2 MeV/
c2
```
Yield = 732 ± 67
```
total
background
signal
Data
1.85 1.86 1.87 1.88
```
M(K −sig π + π + ) [GeV/c2]
```
0
200
400
600
800
1000
1200
1400
Events/2 MeV/
c2
```
Yield = 810 ± 30
```
total
background
signal
MC
```
Figure 32: Fit projections of D+ → K−π+π+ in data (left) and simulation (right) where
```
K− is a kaon from a K∗0 decay and π+ is from the signal or ROE in the B0 → K∗0ν ¯ν
```
analysis for the close-to-signal sideband region 0.93 < η(BDT2) < 0.95. The fitted signal
```
yields in simulation are scaled to the data luminosity.
entire data and simulation samples are used. The decays are formed using K− from615
```
the signal-candidate K∗0 decay and π+ from the ROE (for D0 → K−π+) or both ROE616
```
```
and the signal-candidate decay (for D+ → K−π+π+). The signal and background are617
```
modeled by a Gaussian and first-order polynomial, respectively, with all parameters varied618
independently in data and simulation fits. The fit projections are summarized in Fig. 31619
and Fig. 32 for D0 → K−π+ and D+ → K−π+π+, respectively. The signal yields and620
their ratio in data and simulation with corresponding statistical uncertainties are given in621
Table 19. The data and simulation are in agreement at 2.3 and 1.1 standard deviations.
```
Mode Data yield MC yield Ratio (data/mc)
```
D0 → K−π+ 608 ± 38 516 ± 17 1.18 ± 0.08
D+ → K−π+π+ 732 ± 67 810 ± 30 0.90 ± 0.09
Table 19: Fit yields in data, simulation and their ratio together with statistical uncer-
tainties for D0 → K−π+ and D+ → K−π+π+ decays in the close-to-signal sideband of
the B0 → K∗0ν ¯ν analysis. The fitted signal yields in simulation are scaled to the data
luminosity.
622
10.4.4 B+ → K∗+ν ¯ν decays623
In the B+ → K∗+ν ¯ν channel, the decays are formed using K∗+ from the signal-candidate624
```
K∗+ and π− from the ROE (for D0 → K∗+π−). The signal and background are modeled625
```
by a Gaussian and first-order polynomial, respectively, with all parameters varied inde-626
49
pendently in data and simulation fits. The fit projections are shown in Fig. 33 and the627
signal yields and their ratio in data and simulation with corresponding statistical uncer-628
tainties are given in Table 20. The data and simulation are in agreement at 3.0 standard629
deviations.630
1.84 1.85 1.86 1.87 1.88 1.89
```
M(K* + ) [GeV/c2]
```
0.0
0.5
1.0
1.5
Candidates
×104 Belle II L dt = 1460 fb 1
totalbackground
signalMC15rd
1.84 1.85 1.86 1.87 1.88 1.89
```
M(K* + ) [GeV/c2]
```
0
1000
2000
3000
4000
Candidates
Belle II preliminary L dt = 365 fb 1
totalbackground
signalData
```
Figure 33: Fit projections of D0 → K∗+π− in simulation (left) and data (right) where
```
K∗+ is signal K∗+ while π− is from the ROE in the B+ → K∗+ν ¯ν analysis for the signal
```
sideband region 0.90 < η(BDT2) < 0.95.
```
```
Mode Data yield MC yield Ratio (data/mc)
```
D0 → K∗+π− 8956 ± 307 7808 ± 116 1.15 ± 0.05
Table 20: Fit yields in data, simulation and their ratio together with statistical uncer-
```
tainties for D0 → K∗+π− decay in the close-to-signal sideband (0.90 < η(BDT2) < 0.95)
```
of the B+ → K∗+ν ¯ν analysis.The fitted signal yields in simulation are scaled to the data
luminosity.
```
10.5 Updates to the B → K(∗)K0 ¯K0 modeling631
```
10.5.1 B0 → K0S K0 ¯K0 modeling632
The decay mode B0 → K0S K0L K0L constitutes one of the most significant backgrounds to633
the signal channel B0 → K0S ν ¯ν. Accurate modeling of this background is therefore essen-634
tial for this analysis. In the current Belle II simulation, there are known mismodelings635
of this and related background channels, including B0 → K0S K0S K0L and B0 → K0S K0S K0S .636
These decays are generated according to phase-space distributions based on upper-limit637
```
(UL) branching fractions, which may not reflect realistic dynamics. Additionally, we638
```
identified a bug in the official decay file of release-06, where the B0 → K0K0K0 mode639
was incorrectly enabled. This mode was correctly disabled in release-08. Its inclusion in640
release-06 leads to double-counting and further mismodeling of the background. We quan-641
tified the contributions from these background modes in both RI and RD mixed samples,642
selecting events within the signal region defined by BDT2. The estimated fractions of643
```
these backgrounds in one MC15ri mixed samples (200f b−1) are summarized in Table 21.644
```
50
Background mode Before correction [%] After correction [%]
B0 → K0K0K0 5.60 None
B0 → K0S K0L K0L 1.16 0.581
B0 → K0S K0S K0L 1.09 0.00
B0 → K0S K0S K0S 0.527 0.342
Total number of events 2847 2626
Table 21: Fractions of B0 → K0K0K0 backgrounds in MC15ri mixed samples within a
```
preliminary SR (η(BDT2) > 0.92) before and after correction.
```
The Dalitz distributions for the B0 → K0S K0L K0L and B0 → K0S K0L K0S decays are645
modeled as a combination of the non-resonant B0 → K0S K0S K0S distribution from Ref.[23]646
```
and a resonant contribution from B0 → ϕ(→ K0S K0L )K0. The branching fraction for647
```
the non-resonant decay is reported in Ref.[24] as 2.4+2.7−2.5 ± 0.6 × 10−6. This value aligns648
```
with expectations based on isospin symmetry, which predicts B(B0 → K0S K0L K0L ) ≈ 13 ×649
```
```
B(B0 → K0S K0S K0S )[25, 26]. Given the measured branching fraction of B0 → K0S K0S K0S650
```
as 6.0 ± 0.5 × 10−6[27], the isospin-based estimate for B0 → K0S K0L K0L is approximately651
2.0 × 10−6, in good agreement with the reported non-resonant value. The branching652
fraction for B0 → ϕK0 is also updated based on the latest value from the PDG. To653
improve the modeling of these decays in simulation, all instances of B0 → K0K0K0,654
B0 → K0S K0S K0L , B0 → K0S K0S K0S , and B0 → K0S K0L K0L in both the MC15ri and MC15rd655
samples are identified and replaced using a new implementation in EvtGen. Updated656
background fractions after this correction are summarized in Table 21.657
10.5.2 B → K∗K0 ¯K0 modeling658
In the current Belle II simulation, B+ → K∗+K0 ¯K0 and B0 → K∗0K0 ¯K0 decays are659
generated by using the phase-space model and several intermediate resonances. The660
branching fraction values are guessed because both modes have not been measured before.661
To get a more consistent model, we study the B+ → K∗+K0S K0S and B0 → K∗0K0S K0S662
decays in the MC15ri simulation and data corresponding to 400 fb−1 and 365 fb−1 of663
integrated luminosity, respectively. All the details are in Appendix H.664
We find that the B0 → K∗0K0S K0S decay can be described by the phase-space generated665
simulation. For the B+ → K∗+K0S K0S decay, we do not observe a significant signal. We666
remove B → K∗f ′2 and B → K∗f2 decays from the generic simulation and keep only the667
phase-space contribution. Table 22 summarizes how we treat the B → K∗K0 ¯K0 decays668
in the generic simulation.669
51
Mode Generic simulation Fix
B → K∗f ′2, B → K∗f2 Present Remove
B → K∗K0L K0L , B → K∗K0S K0S Phase space, BF 10−5 Keep as it is
B → K∗K0S K0L Phase space Keep only
and intermediate resonances intermediate resonances
e.g. ϕ
Table 22: Summary of the treatment of B → K∗K0 ¯K0 background in the generic simu-
lation.
52
11 Signal crossfeed670
Given that the four signal channels have similar topology, it is expected that there should671
be sizeable crossfeed among them. The crossfeed is studied using simulated signal samples,672
with all corrections applied. Events are passed through BDT1 and BDT2 selection and673
compared to the corresponding signal mode in Figure 34. The crossfeed contribution is674
not negligible, and it is equivalent to 41.4%, 8.6%, 27.7%, and 24.5% of the number of675
signal events for B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, B+ → K+ν ¯ν, and B+ → K∗+ν ¯ν respectively,676
with smaller contributions at higher BDT2 values. The treatment of these crossfeeds is677
described in Sec. 14.678
0 1 2 3 4 5 6 7 8 9 10 11 12
Signal region bin number
0
2
4
6
8
Entries
B 0→K 0S ν¯ν Belle II simulation
B0 K*0
B + K+
B + K* +
B0 K0S
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```
(BDT2) × q2
```
0
5
10
15
Entries
B 0→K ∗0ν¯ν Belle II simulation
B + K* +
B0 K0s
B + K +
Signal[x100]
0 1 2 3 4 5 6 7 8 9 10 11 12
Signal region bin number
0
5
10
15
20
Entries
Belle II preliminary L dt = 365 fb-1
B0 K*0
B0 K0S
B + K* +
B + K+
0 5 10 15
signal region bin number
0
2
4
6
8
Entries
Belle II preliminary L dt = 365 fb 1
B0 K*0
B0 K0S
B + K +
B + K* +
Figure 34: Distribution of candidates in the signal search region obtained for signal simu-
```
lations: (top left) B0 → K0S ν ¯ν, (top right) B0 → K∗0ν ¯ν, (bottom left) B+ → K+ν ¯ν and
```
```
(bottom right) B+ → K∗+ν ¯ν.
```
Crossfeed contributions can arise from signatures targeted by reconstruction, such as679
```
B+ → K∗+(→ K0S (→ π+π−)π+)ν ¯ν, as well as from other signatures like B+ → K∗+(→680
```
```
K0L π+)ν ¯ν. Therefore, simple truth-matching is not sufficient to isolate these contribu-681
```
```
tions in the generic background; instead, generator-level decay information is used. The682
```
identified contributions are replaced by dedicated simulated samples.683
Additionally, there is a contribution from B → Xsν ¯ν decays, where Xs denotes final684
states with net strangeness S = 1 and include additional particles in the final state. These685
53
contributions are particularly relevant for the K∗ channels. Their treatment is discussed686
in Appendix K.687
In background simulation, crossfeed events–where a single event is reconstructed in688
multiple signal channels–can lead to double counting. For instance, an event originating689
from B+ → K∗+ν ¯ν with K∗+ → K0s π+ may also satisfy the selection criteria for B0 →690
K0s ν ¯ν. Such overlaps result in the same event being counted in more than one signal691
category. To quantify this effect, an investigation was conducted using all simulated692
background samples within the signal regions. The contribution of overlapping events693
were found to be approximately 5%, 5%, 4% and 2% in B+ → K+ν ¯ν, B0 → K0s ν ¯ν,694
B+ → K∗+ν ¯ν and B0 → K∗0ν ¯ν, respectively. Given the relatively small magnitude of695
these contributions, the effect of background crossfeed can be considered negligible for696
the purposes of this analysis.697
12 Sample composition in signal region698
By using corresponding simulated samples, we inspect the distribution of the expected699
```
backgrounds and signal in the signal search region (defined at Fig. 12). Figure 35 shows700
```
such distribution for all four decay modes of interest. We increase signal contribution by701
an arbitrary factor such that its distribution is visible. In the high sensitivity region, we702
expect the background from neutral or charged B to dominate the high-sensitive bins.703
54
0 1 2 3 4 5 6 7 8 9 10 11 12
Signal region bin number
0
500
1000
1500
2000
2500
3000
Entries
B 0→K 0S ν¯ν Belle II simulation
Neutral B
Charged B
cc
ss
uu
dd
Signal[x100]
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Signal region bin number
0
2000
4000
6000
8000
Entries
B 0 → K ∗0ν¯ν Belle II preliminary L dt = 365 fb 1
Neutral B
Charged B
cc
ss
uu
dd
Signal[x100]
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
0
1000
2000
3000
4000
Candidates
Belle II preliminarySimulationB 0 ¯B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B + →K + ν¯ν × 50
0.92 0.94 0.96 0.98 1.0
```
η(BDT2)
```
0 5 10 15
signal region bin number
0
2000
4000
6000
Entries
Belle II preliminary L dt = 365 fb 1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
signal x 100.0
```
Figure 35: Distribution of (top left) B0 → K0S ν ¯ν, (top right) B0 → K∗0ν ¯ν, (bottom left)
```
```
B+ → K+ν ¯ν and (bottom right) B+ → K∗+ν ¯ν candidates in the signal search region
```
```
obtained in simulated (filled histograms) generic background and (red line) corresponding
```
signal samples. The expectations are provided for L = 365 fb−1. The signal expectation
is magnified by an arbitrary factor for better visibility.
55
13 Systematic uncertainties704
The following systematic uncertainties are considered for all channels unless specified705
otherwise. The impact of these uncertainties on the signal strength µ is presented in706
Table 27.707
• 50% normalization uncertainty for the seven background components: τ ¯τ , u¯u, d ¯d, s¯s,708
c¯c. This is the largest source of systematic uncertainty. It is based on data to709
simulation comparison for off-resonance data. The normalization uncertainties will710
be constrained using reconstructed D decays in the signal region, as discussed in711
Sec. 10.4. The uncertainty is modelled by using seven nuisance parameters for each712
of the four channels leading to in total 20 parameters in the fit. These sources have713
the largest contribution to the systematic uncertainty on µ, ranging between 0.7714
and 1.9 for the K+ and K0S channel.715
• MC statistical uncertainty, which also includes small contributions of uncorrelated716
uncertainty arising from covariance matrix decomposition for PID, K0S , and π0 effi-717
ciency. The uncertainty is modelled by an independent nuisance parameter for each718
```
analysis bin (98 nuisance parameters in total). This is the second largest uncertainty719
```
of the analysis, ranging between 0.5 and 1.2.720
• Leading branching fractions of B0 and B+ decays, contributing to the background721
most, are varied according to their PDG uncertainties, leading to 97 correlated722
nuisance parameters. See appendix I for details. The uncertainties on µ range723
between 0.2 and 0.5.724
• Modeling of B+ → K+K0K0 decays has been studied in [3]. We follow the same725
prescription to estimate the effect of this background on all channels and model726
it using two nuisance parameters. The uncertainties for B+ → K+K0L K0L decays727
introduce sizable systematics for the K+ channel.728
```
• The modeling of B → K(∗)K0 ¯K0 decays is corrected in simulation (see Sec. 10.5).729
```
We assign a systematic uncertainty due to the precision of the branching fraction730
of B0 → K∗0K0S K0S decay which is used to model B0 → K∗0K0L K0L and B+ →731
K∗+K0L K0L decays. For the B0 → K∗0K0L K0L decay, we assign a 15% uncertainty732
that corresponds to the precision of our measurement of B0 → K∗0K0S K0S decay.733
While for the B+ → K∗+K0L K0L decay, we assign a 30% uncertainty. Because we do734
not find a significant signal in data and use an assumption of isospin relation with735
the B0 → K∗0K0S K0S decay to estimate the B+ → K∗+K0L K0L branching fraction.736
For the B0 → K0K0K0 decay, which are important for the K0S channel in particular,737
we assign the uncertainty according to the existing measurements, we also assign738
the uncertainty to B0 → ϕK0 according to the PDG.739
```
• B → K(∗)n¯n backgrounds while contributing at small level have shape in BDT2740
```
similar to signal, Their modeling is corrected in simulation using measured B →741
```
K(∗)p¯p decays. Similar to the B+ → K+ν ¯ν analysis, we assign 100% uncertainty742
```
on the branching fractions to cover isospin breaking effects and uncertainties in743
56
```
the M (n¯n) modeling. More details are given in Appendix L. The impact of this744
```
uncertainty on µ is at about 0.2.745
• KaonID and pionID uncertainties are modeled following prescription from the per-746
```
formance group (not applicable for B0 → K0S ν ¯ν). See Ref. [28] appendix M and747
```
N for more details on the method. While different working points are selected for748
B0 → K∗0ν ¯ν and B+ → K∗+ν ¯ν channels, and B+ → K+ν ¯ν channel used differ-749
ent MC sample, the corrections are treated as correlated across the channels in the750
nominal fit. It is based on the study of the samples that are used in the calibration751
```
framework (large overlap of events with KaonID>0.75 and KaonID>0.9) and the752
```
fact that correction factors are dominated by data statistics. As an alternative,753
uncertainties are treated as uncorrelated across the channels.754
• Three additional experimental sources of uncertainty: tracking efficiency modelling,755
```
energy scale for match and un-matched (to MC truth photons) photon candidates.756
```
The corrections are discussed in Sec. 5.1 and Sec. 5.2. See also Ref. [28] appendix757
O and in Ref. [29] appendix K for more details.758
• A global normalization uncertainty associated with the corrections for the PXD759
requirements, ranging from 0.3% to 1.1% depending on the decay mode, is modeled760
using a single nuisance parameter.761
• In simulation, we correct the K0L detection efficiency in ECL by -17±8%. For more762
details, see Sec. 5 and Ref. [19] appendix V.763
• Branching fraction of D meson decays involving K0L is corrected by 30%± 10%. See764
Ref. [29] appendix X for more details on how the corrections were extracted.765
```
• Branching fractions of B decays involving higher-order excitation of D-mesons ( D∗∗,766
```
```
Dsj ) contributing to the backgrounds. The central value of the known branching767
```
fractions is corrected in MC with the most recent measurements and uncertainty. A768
100% systematic uncertainty is assigned on the branching fractions when they are769
not known and thus generated by Pythia. The individual modes are grouped in770
4 categories to assign 4 nuisance parameters to control the systematic uncertainty771
related to these branching fractions. See Appendix J for more details.772
• The number of B ¯B events estimated by the B counting group is used and it corre-773
sponds to 387.1×106 pairs with an uncertainty of 2.0%. The luminosity uncertainty774
affects continuum background normalization and is modeled by a single nuisance pa-775
rameter.776
• f +−/f 00: to obtain number of B+ and B0 mesons in the samples, we use two nui-777
sance parameters: one for the ratio f +−/f 00, constrained to 1.052 ± 0.031 [30], and778
```
another for the fraction of non-B ¯B decays of the Υ(4S), f̸B = 0.0027+0.0138−0.0002 [30],779
```
where f +− + f 00 + f̸ B = 1. Given that the corresponding uncertainties have sub-780
leading contribution to the result, we followed b2help-recommendations and con-781
sidered summetrized values for the uncertainties: f 00 = 0.4861 ± 0.0080, f +− =782
0.5113 ± 0.0108783
57
• A 5% uncertainty is introduced on the difference in normalization between on- and784
off-resonance data, which accounts for potential run dependence of the efficiency.785
It is estimated using a continuum-enriched region in a π sideband of the published786
B+ → K+ν ¯ν analysis.787
• Effect of BDTc reweigthing is used as 100% shape systematics for continuum source.788
• The correction and its uncertainty associated with π0 reconstruction are provided789
```
by the neutrals performance group (see Sec. 5).790
```
• The uncertainty associated with the K0S reconstruction are modeled following the791
guidelines from the tracking performance page. Both statistical and systematic792
uncertainties are considered, with the statistical component being the dominant793
contribution. For the statistical uncertainties, we use the same procedure as for794
the KaonID efficiency. We use 500 toys to determine the covariance matrix, then795
we decompose it, and the 11 most significant eigenvectors are retained and incor-796
porated into the template as Correlated Shape, each represented by an individual797
nuisance parameter. The remaining part is merged into the MC statistical uncer-798
```
tainty (staterror ). For systematic uncertainty, the impact is determined from the799
```
variation corresponding to ±1σ, and is represented by a single Correlated Shape,800
modeled by 1 nuisance parameter.801
• A significant fraction of K∗ candidates in the signal region originates from the wrong802
```
combination of reconstructed K and π mesons (“fake K∗”). Fake K∗ candidates803
```
```
can be formed by tracks from particles originating from different B mesons (Υ (4S)804
```
```
fakes), from the same B meson (B fakes), and from a D meson (D0 and D+ fakes).805
```
```
We assign 10%, 20%, and 30% uncertainty for Υ (4S), D,p and D0 fakes, respectively.806
```
To avoid double counting, this uncertainty is not assigned for decays that are already807
covered by the leading branching fraction uncertainty. Please see Appendix M for808
detailed information.809
• The decays B → Xhs ν ¯ν where Xhs corresponds to all final states containing strangeness810
excluding K and K∗ have signal-like signature. They are modeled by a sum of811
```
B → K1(1270)ν ¯ν and B → K1(1400)ν ¯ν contributions with 50% uncertainty on the812
```
total contribution and 50% uncertainty on the relative fraction of the two contribu-813
tions. Details on the modeling are provided in Appendix K.814
• A global 50% uncertainty is assigned to the B background decays that are not815
covered by branching fraction uncertainty of leading B decays modes. These include816
dominant backgrounds contributions in the SR as well as signal-like backgrounds817
such as B → KK0K0 decays, where K denotes K+,K∗+, K∗0 or K0, baryonic B818
decays, and B → Xhs ν ¯ν decays.819
• Since the studies with embedded samples show very good agreement between data820
and simulation, no correction is applied to the signal simulation and statistical821
uncertainty on the embedded data to simulation yield ratio is taken as a global822
normalization factor for the signal.823
58
```
• Form factor uncertainties follow Ref. [2] (Ref. [28] appendix F for details). See also824
```
Appendix A of Ref. [31] for K∗ channels.825
59
14 Signal extraction826
14.1 Statistical model827
```
The aim of the statistical analysis is to extract the signal strength (µc) of the four channels828
```
```
(c) under analysis: B+ → K+νν, B0 → K0S νν, B+ → K∗+νν, and B− → K∗0νν. This829
```
is realized with a binned maximum likelihood fit to the data distributions simultaneously830
```
in the four channels. The fit is performed on events in signal regions (SRs) of the four831
```
```
channels as defined in Sec. 7, for Υ(4S) data sample. The events in off-resonance regions,832
```
defined in Sec. 9 are fitted simultaneously to control the backgrounds. The events in833
validation regions, both for on and off-resonance regions as defined in Sec. 10.2, are used834
to constrain the backgrounds, and they are fitted simultaneously to the signal region.835
```
We call template nexpc,p the binned distribution of the signal region variables (η(BDT2), q2)836
```
of the expected events for the physical process p reconstructed in the fitting region of chan-837
```
nel c. For each channel, the data distribution of (η(BDT2), q2) is fitted to the sum of the838
```
```
templates considered processes. The processes (or samples) are:839
```
• The four signal processes B+ → K+νν, B0 → K0S νν, B+ → K∗+νν, and B− →840
K∗0νν841
```
• The continuum backgrounds (5 different processes): u¯u, d ¯d, c¯c, s¯s, τ +τ −842
```
```
• The B ¯B backgrounds (2 different processes): B+B− or charged, and B0 ¯B0 or mixed843
```
The likelihood function is:844
```
L =
```
channelsY
c
binscY
i
P
 
```
nobsc,i |nexpc,i (µ, θ)
```
 constraintsY
χ
```
Cχ(θ), (3)845
```
846
```
nexpc,i (µ, θ) =
```
X
p∈processes
Y
k
```
κc,i,p,k(µ, θ)
```
!
nexpc,i,p +
X
d
```
∆c,i,p,d(θ)
```
!
```
. (4)847
```
The index c runs over the channels, the index i runs over the bin of the specific848
channel. The P stands for Poisson distribution and nobsc,i is the number of observed events849
for the channel c in the bin i. The index χ runs over the list of constraints applied to850
the nuisance parameters θ. The functions Cχ depend on the specific constraint and they851
are described later on. The index p runs over the processes, nexpc,i is number of expected852
event per channel per bin while nexpc,i,p is number of expected event per channel per bin per853
process. The index d runs over the additive modifiers to the number of expected events854
∆c,i,p,d. The index k runs over the multiplicative modifiers κc,i,p,k.855
```
The Parameters Of Interest (POIs) of the fit are the signal strength multipliers µc,p of856
```
```
the signal processes. Within Eq. 4, they are κc,i,p,k(µ, θ) = µc i.e. they are freely floating857
```
```
in the fit (Unconstrained normalization) and they are shared between all the bins858
```
and, for each signal process, between all the channels.859
The θ is the set of nuisance parameters, usually related to a specific modifier, which860
encodes the systematic uncertainties in the likelihood. The following types of modifiers861
and nuisance parameters constraints are considered:862
60
```
• Normalization Uncertainty. κc,i,p,k(µ, θ) = gc,p,k(θk|κc,i,p,θk =−1, κc,i,p,θk =1), where863
```
```
g is an interpolation function such as g(θ = 0) = 1, and g(θ = ±1) correspond to864
```
the specified normalization uncertainty. The Cχ is a Gaussian with mean θk and865
width 1.866
```
• Correlated shape. ∆c,i,p,k(µ, θ) = fc,p,k(θk|∆c,i,p,θk =−1, ∆c,i,p,θk =1), where f is an867
```
```
interpolation function such as f (θ = 0) = 0, and f (θ = ±1) correspond to the868
```
specified shape uncertainty. The Cχ is a Gaussian with mean θk and width 1.869
```
• MC Statistical Uncertainty. κc,i,p,k(θk) = θc,i,k and Cχ is the products on the870
```
bins i of Gaussian with mean θc,i,k and width σc,i,k =
qP
p δc,i,p,k/
P
p n
exp
c,i,p, where871
δc,i,p,k is the individual MC statistical uncertainty of the channel c, process p, bin i.872
The summary of the modifiers functions κ, ∆, the corresponding constraint functions873
C, and the required external inputs are summarized in Table 25.874
The signal strength modifiers of the background process are included in the nuisance875
parameters as normalization uncertainties. The remaining systematic uncertainties, but876
MC statistical uncertainty, are included as nuisance parameters as correlated shape. Some877
of these nuisance parameters are correlated between different channels and/or regions, as878
described in Sec. 13.879
In addition, the likelihood function includes explicit constraints from the auxiliary880
measurement of the D meson rates in the signal region, which allows us to reduce back-881
ground normalization uncertainties.882
Description Modification Constraint Term Cχ Input
```
Unconstr. Normalization κc,i,p,k(µc) = µc
```
```
Normalization Unc. κc,i,p,k(θk) = gp(θk| κc,i,p,θk =−1, κc,i,p,θk =1) Gaus(0| θ, σ = 1) κc,i,p,θk =±1
```
```
Correlated Shape ∆c,i,p,k(θk) = fc,p,k(θk|∆c,i,p,θk =−1, ∆c,i,p,θk =1) Gaus(0| θ, σ = 1) ∆c,i,p,θk =±1
```
```
MC Stat. Uncertainty κc,i,p,k(θk) = θc,i,kQi Gaus(1| θc,i,k, σc,i,k) δc,i,k = Pp δc,i,p,k
```
Table 23: Implementation of rate modifiers and corresponding constraints in pyhf. In the
last column, the required input is specified.
14.2 Fit setup883
The fit is performed using the package PyHF [32] a Python implementation of the HistFactory884
statistical models. The fit proceeds in two steps. A first fit is performed using scipy as885
```
minimizer. Then, a second fit is performed, using Minuit (Migrad) as minimizer and the886
```
result of the first fit as a initial condition for the fit. The covariance matrices for the POIs887
and nuisance parameters are obtained using the Hesse algorithm. This approach, thanks888
```
to the robustness of the first fit, prevents failing fits from appearing (also in extended889
```
```
tests like in Sec.s 14.6, 14.5.).890
```
The results are validated using the sgHF fitter [33]. The latter uses a Gaussian ap-891
proximation in the minimization, and the covariance matrix is evaluated analytically. The892
main advantage of sgHF that it is significantly faster and allows for detailed tests using893
toy MC methods. However the final result will be obtained using PyHF.894
61
Both fitter uses as an input a json file containing the fit configuration.895
The SM expectations for the signal branching fractions used as references are given896
```
in Table 1 (SD contribution). It is noteworthy that the SM expectation value for the897
```
B+ → K+ν ¯ν decay is lower compared to the value used in the previously published898
result, 4.97 × 10−6.899
The expected signal and background yields in the SR for each channel are summarized900
in Tab. 24.901
Decay channel SR HSR
Signal/Background Signal/Background
B+ → K+ν ¯ν 137/15209 34/882
B0 → K0S ν ¯ν 60/14601 15/739
B+ → K∗+ν ¯ν 104/39848 18/731
B0 → K∗0ν ¯ν 148/37572 31/1285
Table 24: Expected signal and background yields in the SR and HSR for the three decay
modes. Poissonian uncertainties are assumed.
The full list of POI and nuisance parameters of the fit is described in Table 25.902
62
Parameter

Modifier

Process

Channel

N. of pars & Correlation scheme
µB
+→
K+
ν ¯ν
Unconstr.Normalization

B+
→
K
+ν
¯ν
all

1, shared between channels
µB
0→
K0S
ν ¯ν

Unconstr.Normalization

B0
→
K
0S ν
¯ν
all

1, shared between channels
µB
+→
K∗
+ν
¯ν
Unconstr.Normalization

B+
→
K
∗+
ν ¯ν

all

1, shared between channels
µB
0→
K∗
0ν
¯ν
Unconstr.Normalization

B0
→
K
∗0ν
¯ν
all

1, shared between channels
µu
¯u
##### Normalization Unc. (50%)

u¯u

all

4, uncorrelated, one per channel
µd
¯d
##### Normalization Unc. (50%)

d ¯d

all

4, uncorrelated, one per channel
µc
¯c
##### Normalization Unc. (50%)

c¯c
all

4, uncorrelated, one per channel
µs
¯s
##### Normalization Unc. (50%)

s¯s
all

4, uncorrelated, one per channel
µτ
+τ
−
##### Normalization Unc. (50%)

τ +
τ −

all

4, uncorrelated, one per channel
# NBB

##### Normalization Unc.

signals,
B
+B
−,
B
0 ¯B
0
all

1, shared between processes and channels
f 00
/±

##### Normalization Unc.

signals,
B
+B
−,
B
0 ¯B
0
all

1, shared between processes and channels
Luminosity

##### Normalization Unc.

u¯u, d
¯d, c
¯c, s
¯s, τ
+τ
−
all

1, shared between channels
Leading branching fractions

correlated shape

B+
B−
, B
0 ¯B
0
all

97 nuisance parameter, shared between channels.
```
B(
```
B
→
D
∗∗
```
X)
```

correlated shape

B+
B−
, B
0 ¯B
0
all

4, shared between processes and channels
```
B(
```
B0
→
Kn
```
¯n),
```
```
B(
```
KK
0LK
```
0L)...
```

correlated shape

B+
B−
, B
0 ¯B
0
all

4 ×
N
decays
, uncorrelated, shared between processe
```
B(
```
D
→
K
LX
```
)
```
correlated shape

B+
B−
, B
0 ¯B
0
all

1, shared between processes and channels
```
Continuum modelling (BDT
```
```
c)
```
correlated shape

all

all

4, one per channel channel
Off-resonance normalization

##### Normalization Unc. (5%)

all

all

1, shared between continuum processes and channe
PXD efficiency

##### Normalization Unc.

signals,
B
+B
−,
B
0 ¯B
0
all

1, shared between processes and channels
Efficiency - tracking

correlated shape

all

all

1, shared between processes and channels
Efficiency - signal
K, π
# PID

correlated shape

all

all

2 ·
11, shared between processes and channels
Unmatched neutral cluster energy scale

correlated shape

all

all

1, shared between processes and channels
Matched neutral cluster energy scale

correlated shape

all

all

1, shared between processes and channels
Efficiency -
π0

correlated shape

all

B+
→
K
∗+
ν ¯ν

11+1, shared between processes and channels
Efficiency -
K
0L in ECL

correlated shape

all

all

1, shared between processes and channels
Efficiency -
K
0S
correlated shape

all

B0
→
K
0S ν
¯ν,
B+
→
K
∗+
ν ¯ν

11+1, shared between processes and channels
Signal efficiency

##### Normalization Unc.

signals

all

4, one per channel
Fake
K
∗ from
Υ
```
(4S
```
```
)
```
```
correlated shape (10%)
```

B+
B−
, B
0 ¯B
0,
u¯u, d
¯d, c
¯c, s
¯s, τ
+τ
−
B0
→
K
∗0ν
¯ν,
B+
→
K
∗+
ν ¯ν

2, shared between processes
Fake
K
∗ from
D
0
```
correlated shape (30%)
```

B+
B−
, B
0 ¯B
0,
u¯u, d
¯d, c
¯c, s
¯s, τ
+τ
−
B0
→
K
∗0ν
¯ν,
B+
→
K
∗+
ν ¯ν

2, shared between processes
Fake
K
∗ from
D
+
```
correlated shape (20%)
```

B+
B−
, B
0 ¯B
0,
u¯u, d
¯d, c
¯c, s
¯s, τ
+τ
−
B0
→
K
∗0ν
¯ν,
B+
→
K
∗+
ν ¯ν

2, shared between processes
Untagged
B
events

##### Normalization Unc. (50%)

B+
B−
and
B
0 ¯B
0
all

1, uncorrelated, one per channel
```
Signal form factors (pseudo scalar)
```

correlated shape

signals

B+
→
K
+ν
¯ν,
B0
→
K
0S ν
¯ν
3, correlated between processes
```
Signal form-factors (vector)
```

correlated shape

signals

B0
→
K
∗0ν
¯ν,
B+
→
K
∗+
ν ¯ν

9, correlated between processes
MC sample size

MC Stat. Uncertainty

all

all

114, one per SR bin
Table 25: POIs and nuisance parameters of the fit. The description of the modifier meaning is discussed in Sec. 14.1.
63
14.3 Asimov fit results903
The fit has been performed on the Asimov dataset. The Asimov dataset is defined as the904
dataset with the number of observed events equivalent to the number of expected events905
for every bin of the fitting variables distribution. The Asimov dataset is obtained as the906
```
sum of all the process templates (signals and backgrounds) considered in the fit.907
```
The information gained from this procedure, are estimates of the uncertainties and908
correlations of the fit parameters.909
The results obtained with sgHF and pyHF are shown in Table 26 in terms of uncertainty910
```
on the signal strength multiplier (σµ) or uncertainty on the SM branching fraction (σB =911
```
```
σµBSM ). The world’s best results are also reported for reference (obtained by Belle with912
```
```
semileptonic tag on the full dataset). Results of sgHF and pyHF are compatible. The913
```
expected sensitivity is slightly worse than the world’s best results in all the channels.914
In Fig. 37 the correlation matrix of the Asimov fit is shown. Only the subset of the915
matrix including the normalization parameter is reported.916
In Fig. 38 the pulls for all the nuisance parameters of the Asimov fit are shown. The917
```
pulls are defined as (ˆθ − θ)/σˆθ, where ˆθ, σˆθ are the predicted value of the parameter and918
```
its uncertainty respectively, and θ is the expected value. The best-fit parameters of an919
```
Asimov fit are expected to be the nominal (initial) model parameters. Hence, all pulls920
```
are expected to be zero, which is confirmed. The pulls are shown only for PyHF fit.921
```
The post-fit yields are shown in Fig. 36 for the four channels in Υ(4S) and off-resonance922
```
regions.923
Channel pyHF pyHF sgHF sgHF World’s best
```
σµ σ(B) [10−6] σµ σ(B) [10−6] σ(B) [10−6]
```
B+ → K+ν ¯ν 1.16 5.01 1.16 5.01 5.7
B0 → K0S ν ¯ν 2.67 5.34 2.66 5.32 6.5
B+ → K∗+ν ¯ν 2.03 18.98 2.03 18.96 17
B0 → K∗0ν ¯ν 1.54 13.32 1.55 13.38 11
```
Table 26: Fit uncertainties on POIs in term of µ or branching fractions (B) obtained
```
```
with PyHF of sgHF. The world’s best results are from Ref. [4] (The Belle II result from
```
```
Ref. [3] is excluded).
```
64
0
50
100
150
200
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1
```
ContinuumData
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.92 0.94 0.96 0.98 1.0η(BDT2)
```
0
500
1000
1500
2000
2500
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1B + →K + ν¯νCross-feed
```
B 0 ¯B0B + B −
ContinuumData
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.92 0.94 0.96 0.98 1.0η(BDT2)
```
0
50
100
150
200
250
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1
```
ContinuumData
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.92 0.94 0.96 0.98 1.0η(BDT2)
```
0
500
1000
1500
2000
2500
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1B
```
0→K 0S ν¯ν
Cross-feedB 0 ¯B0
B + B −Continuum
Data
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.92 0.94 0.96 0.98 1.0η(BDT2)
```
0
50
100
150
200
250
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1
```
ContinuumData
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.97 0.975 0.98 0.985 0.99 0.995 1.0η(BDT2)
```
0
2000
4000
6000
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1B + →K ∗ + ν¯νCross-feed
```
B 0 ¯B0B + B −
ContinuumData
-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25||-1 4 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.97 0.975 0.98 0.985 0.99 0.995 1.0η(BDT2)
```
0
50
100
150
200
250
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1
```
ContinuumData
-1 4 8 25||-14 8 25||-14 8 25||-14 8 25||-14 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.95 0.96 0.97 0.98 0.99 1.0η(BDT2)
```
0
2000
4000
6000
8000
Candidates
```
Belle II preliminaryL dt = (362 + 42) fb-1B 0→K ∗0ν¯νCross-feed
```
B 0 ¯B0B + B −
ContinuumData
-1 4 8 25||-14 8 25||-14 8 25||-14 8 25||-14 8 25
q2rec [GeV2/c4]
5
0
5
Pull
```
0.95 0.96 0.97 0.98 0.99 1.0η(BDT2)
```
Figure 36: Post fit distribution for the Asimov fit for the four channels, in the off resonance
```
region (left) and Υ(4S) region (right). For each signal channel, the cross-feed indicates
```
the events from the other three signal channels combined.
65
```
(sig
```
, K+
```
)
```
```
(sig
```
, K* +
```
)
```
```
(sig
```
, KS
```
)
```
```
(sig
```
, K*0
```
)
```
```
(cc,
```
```
K+)
```
```
(charged
```
```
)
```
```
(dd
```
, K+
```
)
```
```
(mixed
```
```
)
```
```
(ss,
```
```
K+)
```
```
( +
```

, K+
```
)
```
```
(uu
```
, K+
```
)
```
```
(cc,
```
K* +
```
)
```
```
(dd
```
, K* +
```
)
```
```
(ss,
```
K* +
```
)
```
```
( +
```

, K* +
```
)
```
```
(uu
```
, K* +
```
)
```
```
(cc,
```
```
KS)
```
```
(dd
```
, KS
```
)
```
```
(ss,
```
```
KS)
```
```
( +
```

, KS
```
)
```
```
(uu
```
, KS
```
)
```
```
(cc,
```
K*0
```
)
```
```
(dd
```
, K*0
```
)
```
```
(ss,
```
K*0
```
)
```
```
( +
```

, K*0
```
)
```
```
(uu
```
, K*0
```
)
```
```
(uu, K*0)
```
```
( + , K*0)
```
```
(ss, K*0)
```
```
(dd, K*0)
```
```
(cc, K*0)
```
```
(uu, KS)
```
```
( + , KS)
```
```
(ss, KS)
```
```
(dd, KS)
```
```
(cc, KS)
```
```
(uu, K* + )
```
```
( + , K* + )
```
```
(ss, K* + )
```
```
(dd, K* + )
```
```
(cc, K* + )
```
```
(uu, K+)
```
```
( + , K+)
```
```
(ss, K+)
```
```
(mixed)
```
```
(dd, K+)
```
```
(charged)
```
```
(cc, K+)
```
```
(sig, K*0)
```
```
(sig, KS)
```
```
(sig, K* + )
```
```
(sig, K+) 1.00 -0.10 0.08 -0.08 0.03 -0.15 -0.04 -0.01 -0.03 0.01 -0.03 -0.04 -0.01 0.06 -0.05 -0.03 0.02 -0.01
```
-0.10 1.00 -0.12 0.12 0.07 -0.08 -0.02 -0.04 0.27 0.05 -0.16 -0.01 0.02 0.03 0.02 0.05 0.02
0.08 -0.12 1.00 -0.04 -0.05 0.02 -0.02 0.01 0.39 0.01 -0.05 -0.34 0.02 -0.03 0.02
-0.08 0.12 -0.04 1.00 -0.08 -0.03 -0.01 -0.02 0.06 0.28 -0.30 -0.01 -0.02
0.03 0.07 1.00 -0.06 -0.12 -0.02 -0.60 -0.22 -0.44 0.02 0.05 0.05 0.02 0.05 0.02 -0.04 0.03
-0.15 -0.08 -0.08 -0.06 1.00 -0.03 0.02
-0.04 -0.12 1.00 -0.04 0.02 -0.02
-0.01 -0.02 -0.05 -0.03 -0.02 -0.03 1.00 -0.04 0.03
-0.03 -0.04 0.02 -0.01 -0.60 0.02 -0.04 1.00 0.02 -0.16 -0.01 -0.04 -0.03 -0.01 0.03 -0.02
0.01 -0.22 0.02 0.02 1.00
-0.03 -0.44 -0.02 -0.16 1.00
-0.04 0.27 -0.02 -0.02 0.02 -0.01 1.00 -0.11 -0.59 -0.06 -0.37 0.03 0.03 -0.03
-0.01 0.05 -0.11 1.00 -0.14 -0.04
-0.16 0.01 0.06 0.05 -0.04 -0.59 -0.14 1.00 0.02 -0.19 0.01 0.02 0.01 0.03 0.02
-0.01 -0.06 0.02 1.00
0.02 -0.37 -0.04 -0.19 1.00 0.01
0.06 0.39 0.05 -0.04 0.03 0.01 0.01 1.00 -0.17 -0.37 -0.07 -0.36 0.01 -0.03
0.01 -0.17 1.00 -0.03 -0.05
-0.05 0.03 -0.05 0.03 0.02 -0.37 -0.03 1.00 0.02
-0.34 -0.07 0.02 1.00 -0.04
0.02 0.02 -0.36 -0.05 -0.04 1.00 0.01 -0.02
-0.03 -0.03 0.28 0.05 -0.03 0.03 0.01 0.01 1.00 -0.13 -0.53 -0.13 -0.47
0.02 0.02 -0.01 0.01 -0.13 1.00 -0.31 0.01 -0.04
0.02 0.05 0.02 -0.30 -0.04 0.03 -0.03 0.03 -0.03 -0.02 -0.53 -0.31 1.00 -0.02 -0.15
-0.01 -0.13 0.01 -0.02 1.00
-0.01 0.02 -0.02 0.03 -0.02 0.02 -0.47 -0.04 -0.15 1.00
Belle II preliminary simulation
0.4
0.2
0.0
0.2
0.4
0.6
0.8
1.0
Correlation Coefficient
Figure 37: Correlation matrix of the Asimov fit performed with pyHF. Only the subset
of the matrix including the normalization parameter is reported. The numerical value is
omitted when the absolute value of the correlation coefficient is below 0.01.
66
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0
```
( ) /
```
```
(cc, K+)
```
```
(charged)
```
```
(dd, K+)
```
```
(mixed)
```
```
(ss, K+)
```
```
( + , K+)
```
```
(uu, K+)
```
```
(cc, K* + )
```
```
(dd, K* + )
```
```
(ss, K* + )
```
```
( + , K* + )
```
```
(uu, K* + )
```
```
(cc, KS)
```
```
(dd, KS)
```
```
(ss, KS)
```
```
( + , KS)
```
```
(uu, KS)
```
```
(cc, K*0)
```
```
(dd, K*0)
```
```
(ss, K*0)
```
```
( + , K*0)
```
```
(uu, K*0)
```
Belle II preliminary simulation
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0
```
( ) /
```
lead.BF charged 521--10311--211lead.BF charged 521--15--16
lead.BF charged 521--20213--421lead.BF charged 521--213--421--22
lead.BF charged 521--213--421lead.BF charged 521--2212--2212--321
lead.BF charged 521--311--211lead.BF charged 521--311--321--22
lead.BF charged 521--311--321lead.BF charged 521--3122--3122--321
lead.BF charged 521--3122--3122--323lead.BF charged 521--321--323--321
lead.BF charged 521--321--333lead.BF charged 521--323--22
lead.BF charged 521--323--311lead.BF charged 521--323--421
lead.BF charged 521--333--321--22lead.BF charged 521--333--321
lead.BF charged 521--413--111--211--211lead.BF charged 521--421--11--12--22--22
lead.BF charged 521--421--11--12--22lead.BF charged 521--421--11--12
lead.BF charged 521--421--13--14--22lead.BF charged 521--421--13--14
lead.BF charged 521--421--15--16lead.BF charged 521--421--211--211--211
lead.BF charged 521--421--211--22lead.BF charged 521--421--211
lead.BF charged 521--421--223--211lead.BF charged 521--421--321--311
lead.BF charged 521--421--321lead.BF charged 521--421--431
lead.BF charged 521--423--11--12--22--22lead.BF charged 521--423--11--12--22
lead.BF charged 521--423--11--12lead.BF charged 521--423--13--14--22
lead.BF charged 521--423--13--14lead.BF charged 521--423--15--16
lead.BF charged 521--423--20213lead.BF charged 521--423--211--211--211--111
lead.BF charged 521--423--211--22lead.BF charged 521--423--211
lead.BF charged 521--423--213lead.BF charged 521--423--321--311
lead.BF charged 521--423--321--313lead.BF charged 521--423--321
lead.BF charged 521--423--323--22lead.BF charged 521--423--323
lead.BF charged 521--423--431lead.BF charged 521--433--421
lead.BF charged 521--433--423lead.BF charged 521--441--321
lead.BF charged 521--441--323lead.BF charged 521--443--321
lead.BF charged 521--443--323lead.BF charged 521--311--311--211
Belle II preliminary simulation
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0
```
( ) /
```
PXDcontinuum_4Scorr_BDTc_Kplus_c1
corr_DKL_c1corr_K1_comp_c1corr_K1_norm_c1
corr_KLeff_c1corr_Knnbar_c1corr_Kstar0K0K0_c1
corr_KstarPlusK0K0_c1corr_kaonID_c1corr_kaonID_c10
corr_kaonID_c11corr_kaonID_c2corr_kaonID_c3
corr_kaonID_c4corr_kaonID_c5corr_kaonID_c6
corr_kaonID_c7corr_kaonID_c8corr_kaonID_c9
corr_neutralGamma_c1corr_neutralUnmatched_c1corr_trackingEff_c1
corr_untagged_LB_c1_Bplus2KplusB+BB
corr_Dexo_cDexoDscorr_Dexo_cDexoDsjcorr_Dexo_cDexoLight
corr_Dexo_cDexoSLcorr_KplusKLKL_c1corr_KplusKLKS_c1
B0corr_FF_c1corr_FF_c10
corr_FF_c11corr_FF_c12corr_FF_c2
corr_FF_c3corr_FF_c4corr_FF_c5
corr_FF_c6corr_FF_c7corr_FF_c8
corr_FF_c9signal_embedd_eff_Bplus2Kpluscorr_BDTc_KstarPlus_c1
corr_K0K0K0_c1corr_KsStat_c1corr_KsStat_c10
corr_KsStat_c11corr_KsStat_c2corr_KsStat_c3
corr_KsStat_c4corr_KsStat_c5corr_KsStat_c6
corr_KsStat_c7corr_KsStat_c8corr_KsStat_c9
corr_KsSyst_c1corr_Pi0Stat_c1corr_Pi0Stat_c10
corr_Pi0Stat_c11corr_Pi0Stat_c2corr_Pi0Stat_c3
corr_Pi0Stat_c4corr_Pi0Stat_c5corr_Pi0Stat_c6
corr_Pi0Stat_c7corr_Pi0Stat_c8corr_Pi0Stat_c9
corr_Pi0Syst_c1corr_fake_dplus_kstar_c1_Bplus2KstarPluscorr_fake_dzero_kstar_c1_Bplus2KstarPlus
corr_fake_kstar_c1_Bplus2KstarPluscorr_phiK0_c1corr_pionID_c1
corr_pionID_c10corr_pionID_c11corr_pionID_c2
corr_pionID_c3corr_pionID_c4corr_pionID_c5
corr_pionID_c6corr_pionID_c7corr_pionID_c8
corr_pionID_c9corr_untagged_LB_c1_Bplus2KstarPlussignal_embedd_eff_Bplus2KstarPlus
corr_BDTc_Kshort_c1corr_untagged_LB_c1_Bzero2Kshortsignal_embedd_eff_Bzero2Kshort
corr_BDTc_KstarZero_c1corr_fake_dplus_kstar_c1_Bzero2KstarZerocorr_fake_dzero_kstar_c1_Bzero2KstarZero
corr_fake_kstar_c1_Bzero2KstarZerocorr_untagged_LB_c1_Bzero2KstarZerosignal_embedd_eff_Bzero2KstarZero
continuum_offresBelle II preliminary simulation
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0
```
( ) /
```
lead.BF mixed 511--20213--411lead.BF mixed 511--211--11--12
lead.BF mixed 511--213--13--14lead.BF mixed 511--213--411--22
lead.BF mixed 511--213--411lead.BF mixed 511--213--413
lead.BF mixed 511--3122--3122--313lead.BF mixed 511--313--22
lead.BF mixed 511--313--311lead.BF mixed 511--321--321--311
lead.BF mixed 511--323--411--22lead.BF mixed 511--323--411
lead.BF mixed 511--411--11--12--22--22lead.BF mixed 511--411--11--12--22
lead.BF mixed 511--411--11--12lead.BF mixed 511--411--13--14--22
lead.BF mixed 511--411--13--14lead.BF mixed 511--411--15--16
lead.BF mixed 511--411--211--211--211lead.BF mixed 511--411--211--22--22
lead.BF mixed 511--411--211--22lead.BF mixed 511--411--211
lead.BF mixed 511--411--311--211lead.BF mixed 511--411--321--22
lead.BF mixed 511--411--321--311--22lead.BF mixed 511--411--321--311
lead.BF mixed 511--411--321--313lead.BF mixed 511--411--321
lead.BF mixed 511--411--431lead.BF mixed 511--413--11--12--22--22
lead.BF mixed 511--413--11--12--22lead.BF mixed 511--413--11--12
lead.BF mixed 511--413--13--14--22lead.BF mixed 511--413--13--14
lead.BF mixed 511--413--15--16lead.BF mixed 511--413--20213
lead.BF mixed 511--413--211--111lead.BF mixed 511--413--211--211--211--111
lead.BF mixed 511--413--211lead.BF mixed 511--413--321--311
lead.BF mixed 511--413--321lead.BF mixed 511--413--323
lead.BF mixed 511--413--413--311lead.BF mixed 511--413--413--313
lead.BF mixed 511--413--431lead.BF mixed 511--421--311
lead.BF mixed 511--431--321lead.BF mixed 511--433--411
lead.BF mixed 511--433--413lead.BF mixed 511--441--130
lead.BF mixed 511--441--310lead.BF mixed 511--441--311
lead.BF mixed 511--441--313lead.BF mixed 511--443--130
lead.BF mixed 511--443--310lead.BF mixed 511--443--313
lead.BF mixed 511--311--311lead.BF mixed 511--310--310
lead.BF mixed 511--311--111Belle II preliminary simulation
Figure 38: Pulls for all the nuisance parameters of the Asimov fit performed with pyHF.
The nuisance parameters related to finite MC statistics are not shown.
67
14.4 Impact of systematics924
There are several approaches to estimate impact of the systematic uncertainties. At this925
stage, it is interesting to check by how much a particular systematic source increases926
the uncertainty on µ. This is done be removing them from the fit and subtracting total927
uncertainties in quadrature. The results are reported in Table 27.928
68
Uncertainty on µ
Source B+ → K+ν ¯ν B0 → K0S ν ¯ν B+ → K∗+ν ¯ν B0 → K∗0ν ¯ν
Continuum normalizations 0.16 1.45 0.73 0.54
MC stats 0.42 1.08 0.89 0.61
Leading BF 0.13 0.19 0.42 0.25
B+ → K+K0L K0L 0.45 0.03 0.03 0.03
B+ → K+K0S K0L 0.02 0.00 0.00 0.00
B → K∗K0L K0L 0.01 0.02 0.01 0.27
B0 → K0K0K0 0.00 0.53 0.01 0.00
```
B → K(∗)n¯n 0.23 0.25 0.17 0.10
```
Kaon ID 0.11 0.01 0.03 0.10
Pion ID 0.00 0.00 0.00 0.00
Matched neutral cluster energy 0.01 0.12 0.29 0.10
Unmatched neutral cluster energy 0.10 0.22 0.57 0.15
Tracking 0.14 0.09 0.27 0.02
K0L efficiency 0.14 0.11 0.29 0.35
D → K0L 0.29 0.07 0.26 0.03
D∗∗ 0.10 0.06 0.27 0.19
B counting 0.14 0.15 0.17 0.14
f +−, f 00 0.17 0.14 0.18 0.13
Luminosity 0.00 0.01 0.01 0.00
Offresonance luminosity 0.02 0.16 0.23 0.03
BDTc 0.10 0.63 0.58 0.45
```
π0 efficiency (total) 0.06 0.09 0.24 0.01
```
```
K0S efficiency (stat) 0.00 0.06 0.01 0.00
```
```
K0S efficiency (syst) 0.08 0.65 0.15 0.02
```
PXD efficiency 0.00 0.05 0.06 0.07
```
Fake K∗ (from Υ(4S)) 0.16 0.20 0.20 0.04
```
```
Fake K∗ (from D+) 0.00 0.01 0.02 0.01
```
```
Fake K∗ (from D0) 0.00 0.01 0.03 0.10
```
Xhs normalization 0.02 0.02 0.10 0.16
Xhs composition 0.01 0.01 0.03 0.07
Untagged 0.28 0.75 0.29 0.54
Signal efficiency 0.03 0.05 0.08 0.06
Signal form factors 0.05 0.06 0.12 0.13
Table 27: The impact of systematic uncertainties is estimated using an Asimov sample
using sghf, where groups of systematic uncertainties are removed from the fit. The
uncertainty on µ is then determined by subtracting, in quadrature, the uncertainty of the
modified fit from that of the nominal fit.
69
14.5 Likelihood scan929
A profiled likelihood scan is performed for the Asimov fit with pyHF, profiling indepen-930
dently the four µ of the signal. The results are shown in Fig. 39. The negative-log-931
likelihood curve is highly symmetric in all cases which indicates expected asymptotic932
behaviour. From the profiled likelihood scan we can calculate parameter uncertainties933
through the relative change in the value of the negative log likelihood, compared to the934
best fit point,935
```
−2 ln L(ˆµ ± σµ) + 2 ln L(ˆµ) = 1. (5)936
```
The resulting uncertainties are shown in Tab. 28.937
4 2 0 2 4 6
parameter scan
0
1
2
3
4
5
2

```
log(
```
```
L)
```
68.3% CL
95.5% CL
mu_Bzero2Kshort
mu_Bplus2Kplus
mu_Bzero2KstarZero
mu_Bplus2KstarPlus
Figure 39: Profiled likelihood scan of the pyHF Asimov fit for the four channels.
Channel σµ symmetric ±σµ profiled
B+ → K+ν ¯ν 1.16 + 1.17 - 1.15
B0 → K0S ν ¯ν 2.67 + 2.73 - 2.63
B+ → K∗+ν ¯ν 2.03 + 2.11 - 2.01
B0 → K∗0ν ¯ν 1.54 + 1.54 - 1.46
Table 28: Fit uncertainties on POIs obtained with PyHF. We show both the symmetric
uncertainty, obtained through the Hessian error matrix and the uncertainty obtained
through the profiled likelihood scan.
70
14.6 Toys and signal injection studies938
103 MC-toys experiments are generated by randomizing the expected number of events939
for each bin with Poissonian fluctuations. The resulting distributions are fitted with the940
nominal templates. For each fit the POI are extracted. The results of the test are shown941
```
in terms of the distribution of the pulls for each POI. The pulls defined as (ˆµ − µ)/σˆµ,942
```
where ˆµ, σˆµ are the predicted value of the parameter and its uncertainty respectively, and943
µ is the expected value.944
The distributions of the pulls are fitted with a Gaussian. The mean value of the945
distribution of the pull is compatible with 0 and the width of the distribution with 1, as946
expected for an unbiased fit.947
To test the robustness of the fit in the presence of a signal different from the SM ones,948
a study injecting µ = 5 or µ = 20 is performed. The signal is injected simultaneously949
in the four channels. The MC-toys experiment are generated again the two additional950
scenarios and the pull distributions are built.951
The pulls distributions for the four channels for µ = [1, 5, 20] are shown in Fig. 40 and952
Fig. 41 for the fit perfomed with sgHF and pyHF respectively. The results are stable for953
the different injected signals.954
4 2 0 2 4
```
( - in)/
```
0
25
50
75
100
125
150
175
200
Entries
B + →K + ν¯ν Belle II preliminary simulation
```
in = 1, = - 0.01 ± 0.02, = 0.96 ± 0.02
```
```
in = 5, = - 0.01 ± 0.03, = 1.03 ± 0.03
```
```
in = 20, = - 0.03 ± 0.02, = 1.00 ± 0.02
```
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
Entries
B 0→K 0S ν¯ν Belle II preliminary simulation
```
in = 1, = 0.02 ± 0.03, = 0.97 ± 0.03
```
```
in = 5, = 0.01 ± 0.03, = 0.96 ± 0.03
```
```
in = 20, = - 0.06 ± 0.02, = 0.99 ± 0.02
```
4 2 0 2 4
```
( - in)/
```
0
25
50
75
100
125
150
175
200
Entries
B 0→K ∗0ν¯ν Belle II preliminary simulation
```
in = 1, = - 0.04 ± 0.02, = 1.00 ± 0.02
```
```
in = 5, = - 0.02 ± 0.03, = 1.00 ± 0.03
```
```
in = 20, = - 0.02 ± 0.03, = 1.02 ± 0.03
```
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
Entries
B + →K ∗ + ν¯ν Belle II preliminary simulation
```
in = 1, = - 0.01 ± 0.03, = 0.95 ± 0.03
```
```
in = 5, = - 0.01 ± 0.02, = 1.01 ± 0.02
```
```
in = 20, = - 0.01 ± 0.03, = 0.97 ± 0.03
```
Figure 40: Pulls distributions of the sgHF fit results on 103 toys, injecting a signal with
µ = [1, 5, 20], for the four channels. The distributions are fitted with a Gaussian.
71
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
250
300
Entries
B + →K + ν¯ν Belle II preliminary simulation
```
in = 1, = 0.06 ± 0.03, = 1.03 ± 0.03
```
```
in = 5, = 0.02 ± 0.03, = 0.98 ± 0.03
```
```
in = 20, = - 0.02 ± 0.01, = 0.85 ± 0.01
```
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
250
300
Entries
B 0→K 0S ν¯ν Belle II preliminary simulation
```
in = 1, = 0.07 ± 0.03, = 0.98 ± 0.03
```
```
in = 5, = 0.02 ± 0.03, = 0.90 ± 0.03
```
```
in = 20, = 0.01 ± 0.02, = 0.83 ± 0.02
```
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
250
300
350
Entries
B 0→K ∗0ν¯ν Belle II preliminary simulation
```
in = 1, = 0.07 ± 0.03, = 1.00 ± 0.03
```
```
in = 5, = 0.03 ± 0.03, = 0.91 ± 0.03
```
```
in = 20, = 0.10 ± 0.02, = 0.68 ± 0.02
```
4 2 0 2 4
```
( - in)/
```
0
50
100
150
200
250
300
350
Entries
B + →K ∗ + ν¯ν Belle II preliminary simulation
```
in = 1, = 0.08 ± 0.02, = 0.95 ± 0.02
```
```
in = 5, = 0.18 ± 0.03, = 0.88 ± 0.03
```
```
in = 20, = 0.08 ± 0.02, = 0.71 ± 0.02
```
Figure 41: Pulls distributions of the pyHF fit results on 103 toys, injecting a signal with
µ = [1, 5, 20], for the four channels. The distributions are fitted with a Gaussian.
72
14.7 Isospin averaged fit955
A fit is performed to an isospin average of the K and K∗ modes. In this case, a single956
```
parameter of interest µ(B → Kν ¯ν) is used for a K+ and K0S modes and a second µ(B →957
```
```
K∗ν ¯ν) is used for K∗+ and K∗0. The resulting uncertainties are σ(µB→Kν ¯ν ) = 1.09958
```
```
and σ(µB→K∗ν ¯ν ) = 1.30 for sghf and σ(µB→Kν ¯ν ) = 1.09 and σ(µB→K∗ν ¯ν ) = 1.30 for959
```
pyhf. This corresponds to a 6.0% and a 18.0% improvement in accuracy compared to960
using B+ → K+ν ¯ν and B0 → K∗0ν ¯ν decays alone. The resulting branching fraction961
uncertainties are reported in the table 29. The correlation matrix is reported in Fig. 43.962
Channel pyHF pyHF sgHF sgHF World’s best
```
σµ σ(B) [10−6] σµ σ(B) [10−6] σ(B) [10−6]
```
B+ → K+ν ¯ν 1.09 4.71 1.09 4.72 5.7
B0 → K0S ν ¯ν 1.09 2.18 1.09 2.19 6.5
B+ → K∗+ν ¯ν 1.30 12.16 1.30 12.12 17
B0 → K∗0ν ¯ν 1.30 11.25 1.30 11.22 11
```
Table 29: Fit uncertainties on POIs in term of µ or branching fractions (B) obtained
```
with PyHF of sgHF assuming isospin average. The world’s best results are from Ref. [4]
```
(The Belle II result from Ref. [3] is excluded).
```
As a test for sensitivity and symmetry of the parameter distributions, 1-dimensional963
profiled likelihood scans for each of the two parameters are performed on Asimov data,964
with pyHF. The results are shown in Fig. 42. The negative-log-likelihood curve is highly965
symmetric in all cases which indicates expected asymptotic behaviour. From the profiled966
likelihood scan we can calculate parameter uncertainties through the relative change in967
```
the value of the negative log likelihood (see Eq. 5). The resulting uncertainties are shown968
```
in Tab. 30.969
Channel σµ symmetric ±σµ profiled
B+ → K+ν ¯ν 1.09 + 1.10 - 1.09
B0 → K0S ν ¯ν 1.09 + 1.10 - 1.09
B+ → K∗+ν ¯ν 1.30 + 1.31 - 1.25
B0 → K∗0ν ¯ν 1.30 + 1.31 - 1.25
Table 30: Fit uncertainties on POIs obtained with PyHF. We show both the symmetric
uncertainty, obtained through the Hessian error matrix and the uncertainty obtained
through the profiled likelihood scan.
14.8 4-channels averaged fit970
A fit is performed assuming a full correlation between the four K modes, thus a single971
```
parameter of interest µ(B → Kν ¯ν) is used in all the modes. The resulting uncertainties972
```
```
are σ(µB→Kν ¯ν ) = 0.78 for sghf and σ(µB→Kν ¯ν ) = 0.78 pyhf. This corresponds to973
```
a 49.0% improvement in accuracy compared to using B+ → K+ν ¯ν decays alone. The974
73
1 0 1 2 3
parameter scan
0
1
2
3
4
5
2

```
log(
```
```
L)
```
68.3% CL
95.5% CL
mu_V
mu_PS
```
Figure 42: Profiled likelihood scans for the pseudoscalar POI µP S = µ(B → Kν ¯ν) and
```
```
vector POI µV = µ(B → K∗ν ¯ν) of the isospin averaged model, fit on Asimov data.
```
resulting branching fraction uncertainties are reported in the table 31. The correlation975
matrix is reported in Fig. 45.976
As a test for sensitivity and symmetry of the parameter distributions, 1-dimensional977
profiled likelihood scans for each of the one parameter are performed on Asimov data,978
with pyHF. The results are shown in Fig. 44. The negative-log-likelihood curve is highly979
symmetric which indicates expected asymptotic behaviour. From the profiled likelihood980
scan we can calculate parameter uncertainties through the relative change in the value of981
```
the negative log likelihood (see Eq. 5). The resulting uncertainties are shown in Tab. 32.982
```
Channel pyHF pyHF sgHF sgHF World’s best
```
σµ σ(B) [10−6] σµ σ(B) [10−6] σ(B) [10−6]
```
B+ → K+ν ¯ν 0.78 3.37 0.78 3.35 5.7
B0 → K0S ν ¯ν 0.78 1.56 0.78 1.55 6.5
B+ → K∗+ν ¯ν 0.78 7.29 0.78 7.26 17
B0 → K∗0ν ¯ν 0.78 6.75 0.78 6.71 11
```
Table 31: Fit uncertainties on POIs in term of µ or branching fractions (B) obtained
```
with PyHF of sgHF assuming all signal strengths to be correlated. The world’s best results
```
are from Ref. [4] (The Belle II result from Ref. [3] is excluded).
```
74
```
(PS
```
```
)(V)
```
```
(cc,
```
```
K+)
```
```
(charged
```
```
)
```
```
(dd
```
, K+
```
)
```
```
(mixed
```
```
)
```
```
(ss,
```
```
K+)
```
```
( +
```

, K+
```
)
```
```
(uu
```
, K+
```
)
```
```
(cc,
```
K* +
```
)
```
```
(dd
```
, K* +
```
)
```
```
(ss,
```
K* +
```
)
```
```
( +
```

, K* +
```
)
```
```
(uu
```
, K* +
```
)
```
```
(cc,
```
```
KS)
```
```
(dd
```
, KS
```
)
```
```
(ss,
```
```
KS)
```
```
( +
```

, KS
```
)
```
```
(uu
```
, KS
```
)
```
```
(cc,
```
K*0
```
)
```
```
(dd
```
, K*0
```
)
```
```
(ss,
```
K*0
```
)
```
```
( +
```

, K*0
```
)
```
```
(uu
```
, K*0
```
)
```
```
(uu, K*0)
```
```
( + , K*0)
```
```
(ss, K*0)
```
```
(dd, K*0)
```
```
(cc, K*0)
```
```
(uu, KS)
```
```
( + , KS)
```
```
(ss, KS)
```
```
(dd, KS)
```
```
(cc, KS)
```
```
(uu, K* + )
```
```
( + , K* + )
```
```
(ss, K* + )
```
```
(dd, K* + )
```
```
(cc, K* + )
```
```
(uu, K+)
```
```
( + , K+)
```
```
(ss, K+)
```
```
(mixed)
```
```
(dd, K+)
```
```
(charged)
```
```
(cc, K+)
```
```
(V)
```
```
(PS) 1.00 -0.14 0.03 -0.14 -0.03 -0.03 -0.03 -0.03 -0.03 -0.01 0.20 -0.06 -0.12 0.01 -0.05 0.04 -0.01
```
-0.14 1.00 0.04 -0.10 -0.04 -0.03 0.14 0.02 -0.04 0.02 -0.01 0.22 0.01 -0.21 -0.01
0.03 0.04 1.00 -0.06 -0.12 -0.02 -0.60 -0.22 -0.44 0.06 0.06 -0.01 0.02 0.06 0.01 -0.06 0.02
-0.14 -0.10 -0.06 1.00 -0.03 0.02 0.01 -0.03 0.02
-0.03 -0.12 1.00 -0.04 0.02 -0.02
-0.03 -0.04 -0.02 -0.03 1.00 -0.03 0.03 -0.02
-0.03 -0.03 -0.60 0.02 -0.04 1.00 0.02 -0.16 -0.05 -0.01 -0.03 0.04 -0.02
-0.22 0.02 0.02 1.00
-0.03 -0.44 -0.02 -0.16 1.00
-0.03 0.14 0.01 1.00 -0.12 -0.58 -0.06 -0.39 0.02 0.07 -0.09
0.02 -0.12 1.00 -0.13 -0.04 0.01 -0.02
-0.01 -0.04 0.06 -0.05 -0.58 -0.13 1.00 0.02 -0.19 0.03 -0.03 0.01 0.07 0.03
-0.06 0.02 1.00
-0.39 -0.04 -0.19 1.00 0.01 -0.01
0.20 0.06 -0.03 -0.03 -0.01 0.02 0.01 1.00 -0.18 -0.38 0.04 -0.39 0.02 -0.04
-0.18 1.00 -0.03 -0.05
-0.06 0.02 -0.01 0.03 0.03 -0.38 -0.03 1.00
-0.12 -0.01 0.02 -0.02 0.04 1.00 -0.03
0.01 0.02 -0.39 -0.05 -0.03 1.00 0.01 -0.02
-0.05 0.22 0.06 -0.03 0.07 0.01 -0.03 0.02 0.01 1.00 -0.13 -0.50 -0.13 -0.48
0.01 0.01 0.01 -0.13 1.00 -0.32 0.01 -0.04
0.04 -0.21 -0.06 0.04 -0.09 -0.02 0.07 -0.01 -0.04 -0.02 -0.50 -0.32 1.00 -0.02 -0.16
-0.01 -0.13 0.01 -0.02 1.00
-0.01 0.02 -0.02 0.03 -0.48 -0.04 -0.16 1.00
Belle II preliminary simulation
0.4
0.2
0.0
0.2
0.4
0.6
0.8
1.0
Correlation Coefficient
Figure 43: Correlation matrix of the Asimov fit performed with pyHF for isospin averaged
fit. Only the subset of the matrix including the normalization parameter is reported. The
numerical value is omitted when the absolute value of the correlation coefficient is below
0.01.
Channel σµ symmetric ±σµ profiled
B+ → K+ν ¯ν 0.78 + 0.79 - 0.77
B0 → K0S ν ¯ν 0.78 + 0.79 - 0.77
B+ → K∗+ν ¯ν 0.78 + 0.79 - 0.77
B0 → K∗0ν ¯ν 0.78 + 0.79 - 0.77
Table 32: Fit uncertainties on POIs obtained with PyHF. We show both the symmetric
uncertainty, obtained through the Hessian error matrix and the uncertainty obtained
through the profiled likelihood scan.
75
0.5 0.0 0.5 1.0 1.5 2.0 2.5
parameter scan
0
1
2
3
4
5
2

```
log(
```
```
L)
```
68.3% CL
95.5% CL
mu
Figure 44: Profiled likelihood scans for the fully correlated signal strength across all
channels, fit on Asimov data.
76
```
(cc,
```
```
K+)
```
```
(charged
```
```
)
```
```
(dd
```
, K+
```
)
```
```
(mixed
```
```
)
```
```
(ss,
```
```
K+)
```
```
( +
```

, K+
```
)
```
```
(uu
```
, K+
```
)
```
```
(cc,
```
K* +
```
)
```
```
(dd
```
, K* +
```
)
```
```
(ss,
```
K* +
```
)
```
```
( +
```

, K* +
```
)
```
```
(uu
```
, K* +
```
)
```
```
(cc,
```
```
KS)
```
```
(dd
```
, KS
```
)
```
```
(ss,
```
```
KS)
```
```
( +
```

, KS
```
)
```
```
(uu
```
, KS
```
)
```
```
(cc,
```
K*0
```
)
```
```
(dd
```
, K*0
```
)
```
```
(ss,
```
K*0
```
)
```
```
( +
```

, K*0
```
)
```
```
(uu
```
, K*0
```
)
```
```
(uu, K*0)
```
```
( + , K*0)
```
```
(ss, K*0)
```
```
(dd, K*0)
```
```
(cc, K*0)
```
```
(uu, KS)
```
```
( + , KS)
```
```
(ss, KS)
```
```
(dd, KS)
```
```
(cc, KS)
```
```
(uu, K* + )
```
```
( + , K* + )
```
```
(ss, K* + )
```
```
(dd, K* + )
```
```
(cc, K* + )
```
```
(uu, K+)
```
```
( + , K+)
```
```
(ss, K+)
```
```
(mixed)
```
```
(dd, K+)
```
```
(charged)
```
```
(cc, K+)
```
1.00 0.06 -0.18 -0.03 -0.05 -0.04 -0.03 0.07 -0.04 0.16 -0.04 -0.10 0.12 -0.11 -0.01
0.06 1.00 -0.06 -0.12 -0.02 -0.60 -0.22 -0.44 0.06 0.06 -0.01 0.02 0.06 0.01 -0.06 0.02
-0.18 -0.06 1.00 -0.03 0.02 0.01 -0.02 0.01
-0.03 -0.12 1.00 -0.04 0.02 -0.02
-0.05 -0.02 -0.03 1.00 -0.03 0.03 -0.02
-0.04 -0.60 0.02 -0.04 1.00 0.02 -0.16 -0.05 -0.01 -0.03 0.04 -0.02
-0.22 0.02 0.02 1.00
-0.03 -0.44 -0.02 -0.16 1.00
0.07 0.01 1.00 -0.13 -0.58 -0.06 -0.39 0.04 0.01 0.05 -0.07
-0.13 1.00 -0.13 -0.04 -0.01
-0.04 0.06 -0.05 -0.58 -0.13 1.00 0.02 -0.19 0.03 -0.03 0.01 0.07 0.03
-0.06 0.02 1.00
-0.39 -0.04 -0.19 1.00 0.01 -0.01
0.16 0.06 -0.02 -0.03 -0.01 0.04 0.01 1.00 -0.18 -0.38 0.05 -0.39 0.05 -0.06
-0.18 1.00 -0.03 -0.05
-0.04 -0.01 0.03 0.03 -0.38 -0.03 1.00 0.01
-0.10 0.01 -0.02 0.05 1.00 -0.03 -0.02
0.02 0.01 -0.39 -0.05 -0.03 1.00 0.01 -0.02
0.12 0.06 -0.03 0.05 -0.03 0.05 -0.02 0.01 1.00 -0.13 -0.49 -0.13 -0.49
0.01 0.01 -0.13 1.00 -0.32 0.01 -0.04
-0.11 -0.06 0.04 -0.07 -0.01 0.07 -0.01 -0.06 0.01 -0.02 -0.49 -0.32 1.00 -0.02 -0.16
-0.13 0.01 -0.02 1.00
-0.01 0.02 -0.02 0.03 -0.49 -0.04 -0.16 1.00
Belle II preliminary simulation
0.4
0.2
0.0
0.2
0.4
0.6
0.8
1.0
Correlation Coefficient
Figure 45: Correlation matrix of the Asimov fit performed with pyHF assuming all signal
strengths to be correlated. Only the subset of the matrix including the normalization
parameter is reported. The numerical value is omitted when the absolute value of the
correlation coefficient is below 0.01.
77
15 Tests before box opening983
Several tests will be performed before the box opening. We will not proceed to the next984
step until the previous step is passed.985
1. Cross check measurement of B0 → ϕK0L – passed.986
2. Perform blind tests using half-split samples:987
```
(a) Generate splits samples, following the splits as for the published B+ → K+ν ¯ν988
```
channel with some additional channel-specific splits.989
```
(b) For each half split and each channel, perform an independent fit. For each990
```
independent fit, fix the cross-feed contribution to the SM expectation. Keep µ991
values blind.992
```
(c) Start by checking the total uncertainties. Make sure that they are approxi-993
```
mately similar for each half-split pair.994
```
(d) For each half-split s, Check ∆µs = |µ< − µ>|. Estimate uncertainty on ∆µs by995
```
```
adding individual uncertainties in quadrature: σ(∆µs) =
```
p
```
σ(µ<)2 + σ(µ>)2.996
```
This is justified by the fact that the leading uncertainties from global normal-997
izations are constrained by the data and floated independently.998
```
(e) Compute global pv for each channel assuming χ2 distribution with Nsplit degrees999
```
of freedom with χ2 =
PNsplit
```
s (∆µs/σ(∆µs))
```
2.1000
```
(f) Perform additional checks for half-splits s for which ∆µs/σ(∆µs) > 21001
```
```
(g) Consider test passed if global pv for each channel is acceptable and no sys-1002
```
tematic effects are observed for half-splits with tensions larger than 2 standard1003
deviation.1004
3. Blind checks of fits to individual channels (cross-feed fixed to SM expectations):1005
```
(a) Check that SGHF and PYHF agree.1006
```
```
(b) Check fit pv, using SGHF and toys. Start the check with off-resonance data1007
```
only.1008
```
(c) Check that systematic uncertainties are not shifted by more than 3σ. Check1009
```
only the absolute value of this shift.1010
```
(d) Check updates of B+ → K+ν ¯ν: generate bootstrap replicas to estimate the1011
```
expected standard deviation of µ. Check |∆µ| vs this uncertainty.1012
```
(e) Check D-mesons induced background yields in data and simulation, in the SR,1013
```
as discussed in Appendix O.11014
4. Checks of the combined fit:1015
```
(a) Check |∆µ| for the individual minus combined fit, compare it to the uncertainty1016
```
difference in quadrature.1017
```
(b) Estimate pv of the global fit.1018
```
78
```
(c) Log-likelihood scan of µ around minimum, to validate the uncertainty estimate1019
```
for both PYHF and SGHF.1020
```
(d) Check if |µK+ −µK0S | < 6 (2σ). Same check for K∗ channels, using uncertainties1021
```
and taking into account small correlation.1022
15.1 Cross check measurement of B0 → ϕK0L decay1023
The analysis is validated by performing a measurement of the branching fraction of the1024
```
B0 → ϕK0L decay. The PDG reports a value of (7.3 ± 0.7) × 10−6, based on the measure-1025
```
ments using the B0 → ϕK0S channel.1026
This channel has similar properties to the B0 → K∗0νν channel. The measurement1027
is performed using selections and multivariate classifiers as similar as possible to the K∗01028
channel. We change the PID requirement for the pion candidate to kaon-likelihood-based1029
ID > 0.75, while other selection criteria remain same as in the nominal analysis. The1030
PID selection efficiency and fake rates are corrected using the systematics framework as a1031
```
function of momentum and azimuthal angle. Global charge-dependent correction factors1032
```
are used for the pion, muon, electron, and proton fake rates. As the K∗0 reconstructed1033
mass is an input for the BDT2, for each reconstructed candidate we fix its value to the1034
```
PDG K∗0 mass, for the η(BDT2) calculation only. We use the full collision data and1035
```
MCrd samples.1036
Modeling of the continuum background is checked using off-resonance data. We find1037
```
that the default BDTC correction yields an adequate description of the q2rec and η(BDT2)1038
```
distributions. Therefore, BDTC is not re-trained. The data-simulation normalization ratio1039
for the continuum background is found to be 1.08. The B0 → ϕK0 channel corresponds1040
to a similar working point compared to the nominal analysis. According to simulation,1041
```
92% of selected K0 originate from K0L. The signal reconstruction efficiency for η(BDT2) >1042
```
```
0.95(0.99) is 5%(1.9%).1043
```
The measurement of the branching fraction is performed with the SGHF framework.1044
The fit is kept as close as possible to the nominal analysis. It is performed in two-1045
```
dimensions, q2rec and η(BDT2), with the same binning apart from a bin boundary between1046
```
first and second bin in q2rec which is changed from 4 to 2 GeV2/c4. The fitted compo-1047
```
nents are: i) B0 → ϕK0; ii) continuum background; iii) mixed background; iv) charged1048
```
```
background; v) B0 → ϕKX background, where KX includes higher resonances, such as,1049
```
K∗0, K∗0 , etc. We added this component, even if very small, because the included decay1050
```
channels have similar q2rec and η(BDT2) distributions as the signal, and their measured1051
```
```
branching fractions have uncertainties up to 20% (from PDG). The fit is performed to1052
```
on-resonance data only. The normalization uncertainties for all background components1053
are set to 50%, no other systematic uncertainties are considered.1054
The fit has a very good quality with p-value of 7%. It yields a relatively small adjust-1055
ment of the background normalization factors of -2.5%, -4.1%, and -3.7% for the contin-1056
uum, mixed, and charged background, respectively, and a large normalization factor of1057
34% for the B0 → ϕKX background.1058
```
We consider possible interference between ϕ and the f0(980) resonance, that could1059
```
enhance the number of signal-like events in our high-sensitivity region. To estimate the1060
expected number of these events we use a data-driven approach, as this effect is not1061
79
present in simulation. We fully reconstruct B0 → K+K−K0S decays in collision data, and1062
we subtract background based on a fit to ∆E. We compare the background-subtracted1063
data distribution of the K+K− invariant mass with the simulated sample of p-wave B0 →1064
K+K−K0S events and with the distribution in data of B+ → K+K0S K0S decays, correcting1065
for the different acceptances. This contribution has in good approximation a similar effect1066
```
as the f0(980). We extrapolate the number of expected B0 → K+K−K0S events in our1067
```
```
analysis (including ϕ – f0(980) interference) by correcting for the acceptances and different1068
```
```
invariant mass window. The estimated number of events in simulation (extrapolated to1069
```
```
data luminosity) is 84 ± 5, to be compared with the actual number of B0 → ϕK0 events1070
```
in data, that is 65 ± 14. The results are compatible within uncertainty, so the possible1071
interference effect is smaller than the expected precision and therefore is neglected.1072
The fit yields µB0→ϕK0 = 1.34 ± 0.48, which corresponds to a branching fraction of1073
```
(9.75 ± 3.50)×10−6, consistent with the PDG value. A comparison of the data and post-1074
```
fit predictions is shown in Fig. 46. Good overall agreement is observed. The contribution1075
of the signal is better seen in the data minus background figure on the top right.1076
To summarize, we study B0 → ϕK0 decays using the nominal configuration of the1077
B0 → K∗0νν analysis demonstrates that the inclusive tagging method is capable to per-1078
form measurements of the signal with similar branching fraction to the signal decay chan-1079
nel. The analysis is performed in the conditions close to the nominal, in terms of the1080
signal efficiency and purity . The resulting branching fraction is consistent with the PDG1081
average. The uncertainty on the branching fraction is similar to the uncertainty for the1082
nominal analysis.1083
Since K0L mesons correspond to 92% of the K0 mesons, this measurement represents1084
a first determination of the B0 → ϕK0 decay branching fraction dominated by the K0L1085
channel.1086
15.2 Half-split studies1087
The goal of the half-splits studies is to check the stability of the fit while performing it1088
on two samples for which the same results are expected. The two samples are obtained1089
by splitting the full data sample with a cut on a variable which is not correlated with1090
the signal. Thus, we expect the same signal strength in the two samples. If the signal1091
strengths in the two samples are different, it is a hint of a possible mismodelling in the1092
fit templates, which deserves further investigation.1093
We split the full data sample in two approximately equal-sized sub-sample, which we1094
call ”left” and ”right” for each variable. The list of the variables and the value of the cuts1095
is reported in table 33. We used the same set of variables used in B+ → K+ν ¯ν published1096
analysis, adding some interesting dedicated variables in the new channels.1097
```
We perform the fits on half-splits samples fixing individually for the tree channels (we1098
```
```
do not repeat the study on B+ → K+ν ¯ν). The cross-feed signal strengths are fixed to1099
```
the pre-fit value. We keep the results of these fit blind.1100
The first check we perform is the comparison between the uncertainties of the signal1101
```
strength between left and right half-split (step 2.c of the list of Sec 15), as the absolute1102
```
difference between the two uncertainties. Observing no large discrepancies, we unblind1103
the individual uncertainties of the two halves, confirming that the uncertainties are similar1104
80
0.0 2.5 5.0 7.5 10.0 12.5 15.0
Bin number
0
500
1000
1500
2000
2500
Events
Continuum
Mixed
Charged
B KX
Signal
Data
0.0 2.5 5.0 7.5 10.0 12.5 15.0
Bin number
150
100
50
0
50
100
150B0 K0
data-background
0
200
400
600
800
1000
1200
```
Candidates/(1 GeV
```
2/c
```
4) Belle II preliminary L dt = 365 fb-1B 0→φ 0K 0
```
B 0→φ 0K X
Mixed
Charged
Continuum
Model stat. unc.
Data
0 5 10 15 20 25
q2rec [GeV2/c4]
5
0
5
Pull
0
2000
4000
6000
Candidates
Belle II preliminary L dt = 365 fb-1
B 0→φ 0K 0
B 0→φ 0K X
Mixed
Charged
Continuum
Model stat. unc.
Data
0.95 0.96 0.97 0.98 0.99 1.00
BDT2
5
0
5
Pull
Figure 46: On the top: results of the fit to the kaon-kaon enriched data sample to de-
```
termine B(B0 → ϕK0) with (left) data and predictions for the 15 fit bins and (right)
```
data minus the sum of background compared to the post-fit signal yield. On the bottom:
```
distribution of (left) q2rec and (right) η(BDT2) for candidates in the kaon-kaon enriched
```
sample. The yields of simulated background and signal components are normalized based
on the fit results to determine the branching fraction of the B0 → ϕK0 decay. The pull
distribution is shown in the bottom panel.
Table 33: Half-split variable for each channel
Variables Cut value B0 → K0S ν ¯ν B+ → K∗+ν ¯ν B0 → K∗0ν ¯ν
K∗ decay channel π0K+ / K0S π+ – ✓ –
Charge K −/+ – ✓ –
```
cos(θK0S ) ≥ 0.22 / < 0.22 ✓ – –
```
```
D(K0S ) [cm] ≥ 6.2 / < 6.2 ✓ – –
```
DataSet ≥ July 2021 / < July 2021 ✓ ✓ ✓
θmiss ≥ 1.5 / < 1.5 ✓ ✓ ✓
PROE [GeV/c] ≥ 1.5 / < 1.5 ✓ ✓ ✓
Nγ ≥ 6 / < 6 ✓ ✓ ✓
Nleptons > 0 / = 0 ✓ ✓ ✓
N ROEtracks ≥ 5 / < 5 ✓ ✓ ✓P
```
(charges)̸ = 0 / = 0 ✓ ✓ ✓
```
81
30 20 10 0 10
µ
```
Sum(charges) 0/ = 0
```
NROEtracks ≥ 5/ < 5
Nleptons > 0/ = 0
Nγ ≥ 6/ < 6
PROE ≥ 1.5 GeV/c/ < 1.5 GeV/c
θmiss ≥ 1.5/ < 1.5
DataSet July 2021/ < July 2021
```
D(K 0S ) 6.2cm< 6.2cm
```
```
cos( K 0S ) 0.22/ < 0.22
```
B 0→K 0S ν¯ν
30 20 10 0 10
µ
```
Sum(charges) 0/ = 0
```
NROEtracks ≥ 5/ < 5
Nleptons > 0/ = 0
Nγ ≥ 6/ < 6
PROE ≥ 1.5 GeV/c/ < 1.5 GeV/c
θmiss ≥ 1.5/ < 1.5
DataSet July 2021/ < July 2021
B 0→K ∗0ν¯ν
30 20 10 0 10
µ
```
Sum(charges) 0/ = 0
```
NROEtracks ≥ 5/ < 5
Nleptons > 0/ = 0
Nγ ≥ 6/ < 6
PROE ≥ 1.5 GeV/c/ < 1.5 GeV/c
θmiss ≥ 1.5/ < 1.5
DataSet July 2021/ < July 2021
Kcharge - /+
B + →π0K +/B + →K 0S π +
B + →K ∗ + ν¯ν
Figure 47: µ of the individual fit on half-splits samples, shifting the average of the two
fits at zero, with completely uncorrelated nuisance parameters.
for all the fits. The results are reported in table 34.1105
The second check we perform is the absolute difference between the signal strengths1106
```
of the two half-splits: ∆µs = |µLs − µRs |. We estimated the uncertainty σ(∆µs) =1107 p
```
```
σ(µLs )2 + σ(µRs )2, which assume the uncertainties not correlated. This is justified by1108
```
the fact that the leading uncertainties from global normalisations are constrained by the1109
data and floated independently. However, this is an approximation which neglects all the1110
correlated parts of the nuisance parameters. The results are reported in table 34. The re-1111
sults are also presented for the three channels in Fig. 47 as the individual signal strengths1112
of the two halves centering the average between two µ at zero, to keep them blind. The1113
global χ2 =
PNsplit
```
s (∆µs/σ(∆µs))
```
2 is χ2/ndf = 14.71/25 and the three single-channel χ21114
```
are:χ2K0S/ndf = 8.79/9, χ2K∗+ /ndf = 3.01/9, χ2K∗0 /ndf = 2.19/7,1115
```
In conclusion, we are satisfied with the half-split tests.1116
15.3 Studies of individual fits1117
The main changes for the B+ → K+ν ¯ν channel are due to updated treatment of the lead-1118
ing B background and background from D∗∗. There is a sizable reduction in uncertainty1119
due to this updated treatment, suggesting a significant statistical component for uncer-1120
tainty on the change in µ since the distribution of background events in the signal region1121
is modified. Other changes, related to updated cross-feed treatment and Xhs background,1122
are small. An update from treating B+ → K+ν ¯ν in a combined fit is discussed in the1123
next section.1124
We estimate the standard deviation of the expected change in µ using the bootstrap1125
method. For that, replicas of the MC samples are produced a hundred times using Pois-1126
```
son(1) weight for each event. The analysis is repeated for each replica using the published1127
```
and updated prescriptions, and a standard deviation of the differences is determined to1128
```
be σ(µ) = XX.1129
```
15.4 Checks of combined fit1130
82
Table 34: Half-split uncertainties and signal strenght differences for each variable and
channel, with completely uncorrelated nuisance parameters.
Channel Variable σL σR ∆µ ± σ∆µ
```
B0 → K0S ν ¯ν cos(θK0S ) 4.99 4.41 8.47 ± 6.66
```
B0 → K0S ν ¯ν θmiss 4.75 4.72 7.28 ± 6.69
B0 → K0S ν ¯ν N ROEtracks 3.83 6.39 −13.62 ± 7.45
B0 → K0S ν ¯ν Nleptons 4.66 4.66 7.34 ± 6.59
B0 → K0S ν ¯ν PROE 5.01 4.39 4.29 ± 6.67
B0 → K0S ν ¯ν Nγ 5.18 5.54 −7.32 ± 7.59
B0 → K0S ν ¯ν DataSet 4.41 4.87 −0.22 ± 6.57
```
B0 → K0S ν ¯ν P(charges) 4.13 4.95 −1.38 ± 6.45
```
```
B0 → K0S ν ¯ν D(K0S ) [cm] 4.94 4.48 −0.58 ± 6.66
```
B+ → K∗+ν ¯ν K∗ decay channel 3.59 2.66 −2.42 ± 4.47
B+ → K∗+ν ¯ν θmiss 3.04 3.07 4.19 ± 4.32
B+ → K∗+ν ¯ν N ROEtracks 2.99 3.27 4.10 ± 4.43
B+ → K∗+ν ¯ν Nleptons 3.01 3.25 −1.03 ± 4.43
B+ → K∗+ν ¯ν PROE 3.28 2.71 −2.05 ± 4.25
B+ → K∗+ν ¯ν Nγ 2.39 3.73 0.11 ± 4.43
B+ → K∗+ν ¯ν DataSet 2.73 3.41 −2.29 ± 4.37
```
B+ → K∗+ν ¯ν P(charges) 2.90 4.52 1.88 ± 5.38
```
B+ → K∗+ν ¯ν Charge K 2.86 3.26 −2.09 ± 4.34
B0 → K∗0ν ¯ν θmiss 2.43 3.04 −5.69 ± 3.89
B0 → K∗0ν ¯ν N ROEtracks 2.25 3.28 −2.59 ± 3.97
B0 → K∗0ν ¯ν Nleptons 2.77 2.69 1.65 ± 3.86
B0 → K∗0ν ¯ν PROE 2.73 2.63 0.15 ± 3.79
B0 → K∗0ν ¯ν Nγ 2.30 3.66 −0.11 ± 4.32
B0 → K∗0ν ¯ν DataSet 2.47 2.82 −1.30 ± 3.75
```
B0 → K∗0ν ¯ν P(charges) 2.25 3.02 −0.84 ± 3.77
```
83
References1131
[1] S. L. Glashow, J. Iliopoulos, and L. Maiani, Weak interactions with lepton-hadron1132
```
symmetry, Phys. Rev. D 2 (1970) 1285.1133
```
```
[2] A. J. Buras, J. Girrbach-Noe, C. Niehoff, and D. M. Straub, B → K(∗)νν decays in1134
```
```
the Standard Model and beyond, JHEP 02 (2015) 184, arXiv:1409.4557.1135
```
[3] Belle-II, I. Adachi et al., Evidence for B+ → K+ν ¯ν decays, Phys. Rev. D 1091136
```
(2024) 112006, arXiv:2311.14647.1137
```
[4] Belle, J. Grygier et al., Search for B → hν ¯ν decays with semileptonic tagging at1138
```
Belle, Phys. Rev. D 96 (2017) 091101, arXiv:1702.03224, [Addendum:1139
```
```
Phys.Rev.D 97, 099902 (2018)].1140
```
```
[5] Belle, O. Lutz et al., Search for B → h(∗)ν ¯ν with the full Belle Υ(4S) data sample,1141
```
```
Phys. Rev. D 87 (2013) 111103, arXiv:1303.3719.1142
```
```
[6] D. Beˇcirevi´c, G. Piazza, and O. Sumensari, Revisiting B → K(∗)ν ¯ν decays in the1143
```
```
Standard Model and beyond, Eur. Phys. J. C 83 (2023) 252, arXiv:2301.06990.1144
```
```
[7] L. Allwicher et al., Understanding the first measurement of B(B→Kνν¯), Phys.1145
```
```
Lett. B 848 (2024) 138411, arXiv:2309.02246.1146
```
[8] C.-H. Chen and C.-W. Chiang, Flavor anomalies in leptoquark model with gauged1147
```
U(1)Lµ-Lτ , Phys. Rev. D 109 (2024) 075004, arXiv:2309.12904.1148
```
[9] T. Felkl, A. Giri, R. Mohanta, and M. A. Schmidt, When energy goes missing: new1149
```
physics in b → sνν with sterile neutrinos, Eur. Phys. J. C 83 (2023) 1135,1150
```
```
arXiv:2309.02940.1151
```
[10] X.-G. He, X.-D. Ma, and G. Valencia, Revisiting models that enhance B+→K+νν¯1152
```
in light of the new Belle II measurement, Phys. Rev. D 109 (2024) 075019,1153
```
```
arXiv:2309.12741.1154
```
[11] D. McKeen, J. N. Ng, and D. Tuckler, Higgs portal interpretation of the Belle II1155
```
B+→K+νν measurement, Phys. Rev. D 109 (2024) 075006, arXiv:2312.00982.1156
```
[12] L. G¨artner et al., Constructing model-agnostic likelihoods, a method for the1157
```
reinterpretation of particle physics results, Eur. Phys. J. C 84 (2024) 693,1158
```
```
arXiv:2402.08417.1159
```
[13] T. Keck, FastBDT: A Speed-Optimized Multivariate Classification Algorithm for the1160
```
Belle II Experiment, Comput. Softw. Big Sci. 1 (2017) 2.1161
```
[14] T. Chen and C. Guestrin, XGBoost: A scalable tree boosting system, in Proceedings1162
of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and1163
```
Data Mining, KDD ’16, (New York, NY, USA), pp. 785–794, ACM, 2016.1164
```
```
doi: 10.1145/2939672.2939785.1165
```
84
[15] HPQCD, W. G. Parrott, C. Bouchard, and C. T. H. Davies, Standard Model1166
predictions for B→Kℓ+ℓ-, B→Kℓ1-ℓ2+ and B→Kνν¯ using form factors from1167
```
Nf=2+1+1 lattice QCD, Phys. Rev. D 107 (2023) 014511, arXiv:2207.13371,1168
```
```
[Erratum: Phys.Rev.D 107, 119903 (2023)].1169
```
[16] Belle-II analysis software Group, J.-F. Krohn et al., Global decay chain vertex1170
```
fitting at Belle II, Nucl. Instrum. Meth. A 976 (2020) 164269, arXiv:1901.11198.1171
```
[17] Belle-II, Systematic Corrections Framework, https:1172
//gitlab.desy.de/belle2/performance/systematic_corrections_framework.1173
```
Accessed: 2025-02-26.1174
```
[18] Belle-II, Correction for tracking momentum bias based on invariant mass peak1175
```
studies, BELLE2-NOTE-PH-2020-030 (2020).1176
```
[19] Belle-II, Studies of B+ → K+ν ¯ν decay using inclusive and hadronic tagging1177
```
methods based on data collected berfore LS1, BELLE2-NOTE-PH-2022-045 (2022).1178
```
[20] Belle-II, K0S efficiency calibration on Run1 data vs MC15,1179
```
BELLE2-NOTE-TE-2023-023 (2023).1180
```
[21] Belle II Collaboration, Event 16302, https://indico.belle2.org/event/16302/,1181
n.d. Accessed: 2025-10-24.1182
[22] Belle II Collaboration, Event 16509, https://indico.belle2.org/event/16509/,1183
n.d. Accessed: 2025-10-24.1184
[23] BaBar, J. P. Lees et al., Amplitude analysis and measurement of the time-dependent1185
```
CP asymmetry of B0 → K0S K0S K0S decays, Phys. Rev. D 85 (2012) 054023,1186
```
```
arXiv:1111.3636.1187
```
[24] BaBar, B. Aubert et al., Search for the decay B0 → K0s K0s K0L, Phys. Rev. D 741188
```
(2006) 032005, arXiv:hep-ex/0606031.1189
```
[25] M. Gronau and J. L. Rosner, Symmetry relations in charmless B —> PPP decays,1190
```
Phys. Rev. D 72 (2005) 094031, arXiv:hep-ph/0509155.1191
```
[26] T. Gershon and M. Hazumi, Time dependent CP violation in B0 —> P0 P0 X01192
```
decays, Phys. Lett. B 596 (2004) 163, arXiv:hep-ph/0402097.1193
```
[27] Particle Data Group, R. L. Workman et al., Review of Particle Physics, PTEP1194
```
2022 (2022) 083C01.1195
```
[28] Belle-II, Studies of B+ → K+ν ¯ν decay using inclusive tagging method.,1196
```
BELLE2-NOTE-PH-2020-057 (2020).1197
```
[29] Belle-II, Studies of B+ → K+νν decays using inclusive and hadronic tagging1198
```
methods based on data collected before LS1, BELLE2-NOTE-PH-2022-045 (2022).1199
```
85
[30] Heavy Flavor Averaging Group, Y. Amhis et al., Averages of b-hadron, c-hadron,1200
and τ -lepton properties as of 2021, arXiv:2411.18639, updated results and plots1201
available at https://hflav.web.cern.ch/.1202
```
[31] Belle-II, Studies of B → K(∗)νν using inclusive tagging method based on data1203
```
```
collected in 2019-2021 Summer, BELLE2-NOTE-PH-2021-047 (2021).1204
```
[32] L. Heinrich, M. Feickert, and G. Stark, scikit-hep/pyhf: v0.7.0, Sept., 2022.1205
```
https://doi.org/10.5281/zenodo.7110486, doi: 10.5281/zenodo.7110486.1206
```
[33] Belle-II, F. Abudin´en et al., Search for B+→K+νν¯ Decays Using an Inclusive1207
```
Tagging Method at Belle II, Phys. Rev. Lett. 127 (2021) 181802,1208
```
```
arXiv:2104.12624.1209
```
[34] ARGUS Collaboration, Albrecht. et al., First observation of γγ → K∗0K∗0, Physics1210
```
Letters B 198 (1987) 255.1211
```
[35] ARGUS Collaboration, Albrecht. et al., First observation of γγ → K∗+K∗+,1212
```
Physics Letters B 212 (1988) 528.1213
```
[36] CELLO, H. J. Behrend et al., The K0S K0S Final State in γγ Interactions, Z. Phys. C1214
```
43 (1989) 91.1215
```
[37] LHCb, R. Aaij et al., First observations of the rare decays B+ → K+π+π−µ+µ−1216
```
and B+ → ϕK+µ+µ−, JHEP 10 (2014) 064, arXiv:1408.1137.1217
```
[38] Belle, H. Guler et al., Study of the K+π+π− Final State in B+ → J/ψK+π+π− and1218
```
B+ → ψ − primeK+π+π−, Phys. Rev. D 83 (2011) 032005, arXiv:1009.5256.1219
```
[39] Belle, J. T. Wei et al., Study of B+ —> p anti-p K+ and B+ —> p anti-p pi+,1220
```
Phys. Lett. B 659 (2008) 80, arXiv:0706.4167.1221
```
[40] Belle, J. H. Chen et al., Observation of B0 —> p anti-p K*0 with a large K*01222
```
polarization, Phys. Rev. Lett. 100 (2008) 251801, arXiv:0802.0336.1223
```
[41] BaBar, B. Aubert et al., Evidence for the B0 —-> p anti-p K*0 and B+ —>1224
```
eta(c) K*+ decays and Study of the Decay Dynamics of B Meson Decays into p1225
```
```
anti-p h final states, Phys. Rev. D 76 (2007) 092004, arXiv:0707.1648.1226
```
[42] HEP ML Living Review, https://iml-wg.github.io/HEPML-LivingReview.1227
Accessed 11.12.2024.1228
[43] S. Gong et al., An efficient Lorentz equivariant graph neural network for jet tagging,1229
```
Journal of High Energy Physics 2022 (2022) .1230
```
86
A Variable lists1231
Tables 35 and 36 show the importance of the input variable candidates for BDT1. We1232
use 12 most powerful common variables for all channels except for B+ → K∗+ν ¯ν. These1233
12 variables are highlighted in the table.1234
Tables 37 list the BDT2 input variables for each channel. The variable importance is1235
```
given by the model itself: in FastBDT (BDT1), the importance of a variable is the sum1236
```
```
of the information gain across all splits the variable is used in; in XGBoost (BDT2), the1237
```
importance is the average of this information gain across all splits the variable is used in.1238
In both cases, the importance is normalised so that the total sum is 1.0.1239
```
Variable Ranking for B0 → K0S ν ¯ν Ranking for B0 → K∗0ν ¯ν (%)
```
∆EROE 100 59.5
Modified Fox-Wolfram Hsom,2 21 7.8
Modified Fox-Wolfram Hsom,4 10 6.9
Harmonic Moment B0 5 6.6
pROE 10 4.0
Modified Fox-Wolfram Roo2 7 3.8
Modified Fox-Wolfram Roo0 9 2.7
Fox-Wolfram Moment R1 6 2.5
```
cos(thrustB , thrustROE) 2 2.5
```
```
θ(pROE) 1 1.6
```
```
cos(θ(thrust)) 2 1.4
```
Harmonic Moment B2 0 1.0
Table 35: Variables and their importance in BDT1 classifier for B0 → K0S ν ¯ν and B0 →
K∗0ν ¯ν decays.
```
Variable Ranking for B+ → K∗+ν ¯ν (%)
```
Modified Fox-Wolfram Hoo0 41.1
π0 mass before vertex fit 12.6
```
weQ2lnuSimple(0) 12.1
```
pROEt 10.0
angle between π0, K0S daughter momenta 8.8
K∗+ candidate multiplicity 5.5
```
weQ2lnuSimple(2) 5.1
```
K∗+ mass 2.0
K+, π+ momentum in K∗+ rest frame 1.4
number of tracks and photons in ROE 0.72
M ROEbc 0.71
Table 36: Variables and their importance in BDT1 classifier for B+ → K∗+ν ¯ν decays.
87
Variable Importance
```
cos(pK0S , K0S vertex vector)) 0.090
```
```
cos(thrustB , thrustROE) 0.054
```
θ angle of missing momentum 0.047
```
Squared momentum transfer q2 = (pl + pν )2 0.04
```
Evisible 0.034
```
D+(K0S ℓ) multiplicity 0.033
```
M ROEbc 0.032
Nelectrons 0.03
Modified Fox-Wolfram Hso1,2 0.03
```
D+(K0S ℓ):cos(pK0S , line(IP, K0S vertex)XY ) 0.028
```
Fox-Wolfram R2 0.028
```
dr(pK0S ) with re-sampled vertex distribution 0.027
```
Modified Fox-Wolfram Hoo2 0.026
```
dr(π+) with re-sampled vertex distribution 0.025
```
Modified Fox-Wolfram Hso0,2 0.025
```
dr(π−) with re-sampled vertex distribution 0.022
```
```
p-value (Tag vertex) 0.021
```
```
cos(thrustB, z) 0.020
```
```
pℓ(D+(K0S ℓ)) 0.020
```
```
dr(K0S ) with re-sampled vertex distribution 0.019
```
Nlepton 0.018
Aplanarity 0.017
Total charge squared 0.0168
Fox-Wolfram R4 0.016
NROETracks and Photons 0.016
Fox-Wolfram R3 0.015
```
χ2 probability (K0S ) 0.014
```
dzK0S with respect to tag vertex momentum line 0.014
```
Median(dzπROE ) 0.013
```
NROE charged 0.012
Sphericity 0.012
EExtra 0.0116
x component of vector from IP to tag vertex 0.0115
```
M (K0S ) 0.011
```
K0S flight time 0.010
∆EROE 0.010
Number of tracks in tag vertex 0.010
z component of vector from IP to tag vertex 0.010
Modified Fox-Wolfram Hoo4 0.009
Harmonic moment B4 0.007
NK0S 0.007
ROE pt 0.007
χ2 probability of tag vertex 0.006
88
Variable Importance
drK0S with respect to tag vertex momentum line 0.006
```
cos(θ(thrust)) 0.006
```
z-Thrust axis 0.006
```
Average(ptπROE ) 0.006
```
```
Median(drπROE ) 0.006
```
dz of K∗+ with re-sampled vertex distribution, extrapolated along momentum 0.006
```
Standard deviation(ptπROE ) 0.005
```
Mass of particles flying in opposite direction of thrust axis 0.005
ROE mass 0.004
Modified Fox-Wolfram Hso0,0 0.004
Thrustsig 0.004
Mass of particles flying in same direction of thrust axis 0.004
pz of particles flying in opposite direction of thrust axis 0.004
Table 37: 56 BDT2 input variables for channel B0 → K0S ν ¯ν.
Variable Importance
K∗0 mass 18.1
Modified Fox-Wolfram Hsom,2 6.9
Modified Fox-Wolfram Roo2 4.4
Number of photons in ROE 4.3
```
χ2 vertex probability of D−(→ K+ (from K∗0)π−π− 4.2
```
Distance between the POCAS of K+ and π− in the transverse plane 4.0
Modified Fox-Wolfram Hson,2 3.7
Modified Fox-Wolfram Hsoc,2 3.4
drK0 with re-sampled vertex distribution 3.2
Cosine of angle between thrust axis of K0 and z-axis 3.1
Number of leptons 3.0
Beam constraint mass of ROE 3.0
Cosine of angle between signal K and signal π 2.9
Polar angle of the missing momentum 2.7
dzK0 with respect to tag vertex momentum line 2.7
```
Momentum transfer squared, calculated in CMS as q2 = (pl + pν )2 2.6
```
Square of total charges 2.6
Number of electrons 2.1
Transverse momentum of the second daughter with respect to the K∗0 1.9
Distance along the z-axis between the POCAS of two signal track 1.8
Transverse momentum of the first daughter with respect to the K∗0 1.8
Longitudinal distance between the POCA of the particle K0 and the Tag vertex 1.8
Fox-Wolfram Moment R2 1.4
Cosine of angle between momentum and vertex in XY plane
```
of D−(→ K+ (from K∗0)π−π− 1.3
```
Radial distance between the POCA of the particle of K0 and the Tag vertex 1.3
89
Variable Importance
Number of all charged particles in ROE 1.2
```
Mean dz of π from D−(→ K+ (from K∗0)π−π− 1.2
```
```
dr with re-sampled vertex distribution of D−(→ K+ (from K∗0)π−π− 1.0
```
dz with re-sampled vertex distribution of signal π 1.0
Missing mass squared over missing energy 1.0
Modified Fox-Wolfram Hsom,0 0.9
Modified Fox-Wolfram Hsoc,0 0.9
∆EROE 0.8
z component of the total momentum of the particles flying
in the same direction of the thrust axis 0.8
dz with re-sampled vertex distribution of K0 0.6
Transverse component of momentum of ROE 0.6
Radial distance between the momentum line of the particle of K0 and the Tag vertex 0.6
Angle between signal B and lepton in W rest frame 0.5
Energy of the missing momentum 0.4
Table 38: 39 BDT2 input variables for the B0 → K∗0ν ¯ν channel.
90
Variable Used in K∗+ → π+K0S K∗+ → K+π0 Importance
∆EROE ✓ ✓ 0.088
```
cos(thrustB , thrustROE) ✓ ✓ 0.078
```
Modified Fox-Wolfram Hso22 ✓ ✓ 0.066
Q2tot ✓ ✓ 0.055
Modified Fox-Wolfram Hoo2 ✓ ✓ 0.049
thrustzB ✓ ✓ 0.036
K∗+ mass ✓ ✓ 0.035
Modified Fox-Wolfram Hso12 ✓ ✓ 0.034
Modified Fox-Wolfram Hso24 ✓ ✓ 0.031
```
cos(K∗+ daughter momenta) ✓ ✓ 0.029
```
M ROEbc ✓ ✓ 0.027
Fox-Wolfram R1 ✓ ✓ 0.022
number of tracks and photons in ROE ✓ ✓ 0.021
θ angle of missing momentum ✓ ✓ 0.020
Number of leptons ✓ ✓ 0.018
```
cosK0S [∡(p, vertex)] ✓ 0.016
```
D0 → K∗+X− mass ✓ ✓ 0.015
drK0S along momentum line ✓ 0.014
2nd harmonic moment wrt. thrustB ✓ ✓ 0.014
Median p value of D0 → K∗+X− ✓ ✓ 0.014
K0S flight time ✓ 0.014
```
cos(thrustB, z) ✓ ✓ 0.013
```
dz[π+,K+] to tag vertex ✓ ✓ 0.011
Distance between γ1 cluster and nearest track ✓ 0.011
Distance between γ0 cluster and nearest track ✓ 0.011
⟨pt⟩ROE ✓ ✓ 0.011
Extra ROE neutral cluster energy ✓ ✓ 0.010
pROEt ✓ ✓ 0.010
Modified Fox-Wolfram ET ✓ ✓ 0.010
```
σ(⟨dz⟩ROE) ✓ ✓ 0.010
```
```
χ2 probability for D+ → (K∗+π+π−) ✓ ✓ 0.009
```
Modified Fox-Wolfram Hso02 ✓ ✓ 0.009
```
cos(π0 or K0S daughter momenta) ✓ ✓ 0.009
```
z component of forward hemisphere ✓ ✓ 0.009
median dzROE ✓ ✓ 0.008
K0S flight distance ✓ 0.008
4th harmonic moment wrt. thrustB ✓ ✓ 0.007
Number of ROE photons ✓ ✓ 0.007
Fox-Wolfram R3 ✓ ✓ 0.007
σ of p value of D0 → K∗+X− ✓ ✓ 0.007
π0 mass before vertex fit ✓ 0.006
Modified Fox-Wolfram Hoo0 ✓ ✓ 0.006
χ2 probability of π0, K0S ✓ ✓ 0.006
91
Variable Used in K∗+ → π+K0S K∗+ → K+π0 Importance
```
σ(⟨pt⟩ROE) ✓ ✓ 0.006
```
Tag vertex x ✓ ✓ 0.006
Fox-Wolfram R2 ✓ ✓ 0.005
Tag vertex z ✓ ✓ 0.005
K0S flight distance error ✓ 0.005
χ2 probability of D0 → K∗+X− ✓ ✓ 0.005
0th harmonic moment wrt. thrustB ✓ ✓ 0.005
```
cos[∡(p, vertex] of D0 → K∗+X− in xy-plane ✓ ✓ 0.004
```
dz of K0S along momentum line ✓ 0.004
Number of D+ → K∗+X+X− candidates ✓ ✓ 0.004
dz of π+, K+ ✓ ✓ 0.004
Number of ROE tracks ✓ ✓ 0.004
```
Cosine of helicity K∗+ angle (cms) ✓ ✓ 0.004
```
```
cos[∡(p, vertex] of D0 → K∗+π− ✓ ✓ 0.004
```
thrustB ✓ ✓ 0.004
dr to tag vertex of π0, K0S ✓ 0.004
Modified Fox-Wolfram Hso20 ✓ ✓ 0.003
Modified Fox-Wolfram Hso01 ✓ ✓ 0.003
pROE ✓ ✓ 0.003
Sphericity ✓ ✓ 0.003
θ angle of pROE ✓ ✓ 0.003
pT of first daughter with respect to the K∗+ ✓ ✓ 0.003
mass of D0 → K∗+π− ✓ ✓ 0.003
σ of p value of D+ → K∗+X+X− ✓ ✓ 0.003
Visible energy of event in CMS ✓ ✓ 0.002
Median p value of D+ → K∗+X+X− ✓ ✓ 0.002
z component of backward hemisphere ✓ ✓ 0.002
K0S flight time error ✓ 0.002
Modified Fox-Wolfram Hso00 ✓ ✓ 0.002
⟨dz⟩ROE ✓ ✓ 0.002
Table 39: Training variables used in both B+ → K∗+νν decay channels for BDT2 training.
Variables related to impact parameters and vertex vectors are blinded for any photons
and π0.
92
B Distributions of BDT1 and BDT2 inputs1240
B.1 Distributions for B0 → K0S ν ¯ν1241
The distributions of the 12 variables used as input for BDT1 training for B0 → K0S ν ¯ν1242
channel are shown in Fig.48. The comparison corresponds to 1% of total data and run-1243
independent simulation.
0.000
0.025
0.050
0.075
0.100
0.125
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
```
0.0 0.2 0.4 0.6 0.8 1.0cos(thrust
```
```
B, thrustROE)
```
0
2
DataSim.
0.00
0.02
0.04
0.06
0.08
0.10
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.00 0.05 0.10 0.15 0.20Modified Fox-Wolfram Roo
0
0
2
DataSim.
0.0
0.1
0.2
0.3
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.05 0.00 0.05 0.10 0.15Modified Fox-Wolfram Roo
2
0
2
DataSim.
0.00
0.05
0.10
0.15
0.20
0.25
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.2 0.1 0.0 0.1 0.2 0.3 0.4Modified Fox-Wolfram Hso
m, 2
0
2
DataSim.
0.00
0.05
0.10
0.15
0.20
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.2 0.1 0.0 0.1 0.2 0.3Modified Fox-Wolfram Hso
m, 4
0
2
DataSim.
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
5.0 2.5 0.0 2.5 5.0 7.5 10.0E
ROE [GeV]
0
2
DataSim.
0.00
0.02
0.04
0.06
0.08
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0 1 2 3 4 5p
ROE [GeV/c]
0
2
DataSim.
0.000
0.025
0.050
0.075
0.100
0.125
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
```
0.0 0.5 1.0 1.5 2.0 2.5 3.0(p
```
```
ROE)
```
0
2
DataSim.
0.0
0.1
0.2
0.3
0.4
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.0 0.1 0.2 0.3 0.4 0.5 0.6Fox-Wolfram Moment R
1
0
2
DataSim.
0.00
0.02
0.04
0.06
0.08
0.10
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0 1.2Harmonic Moment B00
2
DataSim.
0.00
0.02
0.04
0.06
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0Harmonic Moment B20
2
DataSim.
0.00
0.02
0.04
0.06
Event density
Belle II preliminary L dt = 3.62 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K 0S ν¯νData
Sim. stat. unc.
```
1.0 0.5 0.0 0.5 1.0cos(θ(thrust))0
```
2
DataSim.
Figure 48: BDT1 input variables for the channel B0 → K0S ν ¯ν. The comparison corre-
sponds to 1% of total data and run-independent simulation.
1244
The distributions of the additional variables used as input for BDT2 training for B0 →1245
93
K0S ν ¯ν channel are shown in Figs.49,50,51 and 52. The comparison corresponds to 90 fb−11246
of total data and run-dependent simulation. The signal region is kept blinded by applying1247
BDT1 < 0.99 selection. Among the variables, we use charm suppression variables to1248
decrease background contributions from D0 and D+decays. We construct D+and D01249
candidates by combining K0S candidate with a single and two charged pions from the1250
rest-of-event, respectively, as described in Sec. 10.4.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20aplanarity0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0backwardHemisphereMass0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
2 1 0backwardHemisphereZ0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.4 0.6 0.8 1.0cosTBTO0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.4 0.6 0.8cosTBz0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0forwardHemisphereMass0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.1 0.2 0.3 0.4 0.5foxWolframR20.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20 0.25 0.30 0.35foxWolframR30.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.10 0.15 0.20 0.25 0.30 0.35foxWolframR40.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.1 0.0 0.1 0.2 0.3harmonicMomentThrust40.8
1.01.2DATARDMC
0
1
2
3
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.000 0.005 0.010 0.015 0.020KSFWVariables_hoo20.8
1.01.2DATARDMC
0
1
2
3
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.00500.00250.00000.00250.00500.00750.0100KSFWVariables_hoo40.8
1.01.2DATARDMC
Figure 49: BDT2 input variables for the channel B0 → K0S ν ¯ν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
1251
94
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.10 0.15 0.20KSFWVariables_hso000.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.050 0.025 0.000 0.025 0.050 0.075KSFWVariables_hso020.8
1.01.2DATARDMC
0
1
2
3
4
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.02 0.00 0.02 0.04 0.06KSFWVariables_hso120.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8Kshort_chiProb0.8
1.01.2DATARDMC
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.9875 0.9900 0.9925 0.9950 0.9975 1.0000Kshort_cosAngleBetweenMomentumAndVertexVector0.8
1.01.2DATARDMC
0
1
2
3
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.00 0.25 0.50 0.75 1.00 1.25 1.50Kshort_dr_to_TagV_momentum_line0.8
1.01.2DATARDMC
0
1
2
3
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2Kshort_drS_momentum_line0.8
1.01.2DATARDMC
0.0
0.2
0.4
0.6
0.8
1.0
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0 10 20 30 40Kshort_drS0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.0 0.2 0.4 0.6Kshort_dz_to_TagV_momentum_line0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.0 0.2 0.4 0.6Kshort_dzS_momentum_line0.8
1.01.2DATARDMC
0
2
4
6
8
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.1 0.2 0.3 0.4Kshort_flightTime0.8
1.01.2DATARDMC
0.00
0.25
0.50
0.75
1.00
1.25
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.485 0.490 0.495 0.500 0.505 0.510Kshort_M0.8
1.01.2DATARDMC
0.00
0.25
0.50
0.75
1.00
1.25
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0 1 2 3Kshort_Pi1_drS0.8
1.01.2DATARDMC
0.00
0.25
0.50
0.75
1.00
1.25
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0 1 2 3Kshort_Pi2_drS0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.992 0.994 0.996 0.998 1.000kshortDp_Kslepton_Ks_cosAngleBetweenMomentumAndVertexVectorInXYPlane0.8
1.01.2DATARDMC
Figure 50: BDT2 input variables for the channel B0 → K0S ν ¯ν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
95
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.25 0.50 0.75 1.00 1.25 1.50kshortDp_Kslepton_lepton_p0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
1.0 1.2 1.4 1.6 1.8 2.0kshortDp_Kslepton_Multiplicity0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
2 3 4 5 6 7nROE_Charged_ipMask0.8
1.01.2DATARDMC
0
2
4
6
8
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
6 8 10 12 14 16 18nROETracksandPhotons0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
2.5 2.0 1.5 1.0 0.5 0.0roeDeltae_ipMask0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
2.5 3.0 3.5 4.0 4.5 5.0 5.5roeM_ipMask0.8
1.01.2DATARDMC
0
1
2
3
4
5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
5.00 5.05 5.10 5.15 5.20 5.25roeMbc_ipMask0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0roeNeextra_ipMask0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.3 0.4 0.5 0.6 0.7 0.8 0.9roePi_avg_pt0.8
1.01.2DATARDMC
0
2
4
6
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.00 0.01 0.02 0.03 0.04roePi_med_dr0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.06 0.04 0.02 0.00 0.02 0.04 0.06roePi_med_dz0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.1 0.2 0.3 0.4 0.5roePi_std_pt0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.25 0.50 0.75 1.00 1.25 1.50roePt_ipMask0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6 0.7sphericity0.8
1.01.2DATARDMC
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0 2000 4000 6000TagVChi20.8
1.01.2DATARDMC
Figure 51: BDT2 input variables for the channel B0 → K0S ν ¯ν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
96
0.0
0.5
1.0
1.5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
2 3 4 5 6 7TagVNTracks0.8
1.01.2DATARDMC
0
1
2
3
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8TagVpVal0.8
1.01.2DATARDMC
0
2
4
6
8
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.04 0.02 0.00 0.02 0.04TagVxBeam0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.050 0.025 0.000 0.025 0.050 0.075TagVzBeam0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.65 0.70 0.75 0.80 0.85 0.90thrust0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.2 0.0 0.2 0.4 0.6 0.8thrustAxisZ0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.65 0.70 0.75 0.80 0.85thrustOm0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
5 6 7visibleEnergyOfEventCMS0.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0weMissPTheta_ipMask_00.8
1.01.2DATARDMC
0.0
0.5
1.0
1.5
Events
×104 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
30 40 50 60weQ2lnuSimple_ipMask_00.8
1.01.2DATARDMC
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0nElectronNoSVD0.8
1.01.2DATARDMC
0
2
4
6
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
1.0 1.2 1.4 1.6 1.8 2.0nKs0allevent0.8
1.01.2DATARDMC
0
1
2
3
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0nLepton_eNoSVDNoTOP_muNoSVD0.8
1.01.2DATARDMC
0
1
2
3
Events
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000Model stat. unc.
Data
0 1 2 3 4total_charge20.8
1.01.2DATARDMC
Figure 52: BDT2 input variables for the channel B0 → K0S ν ¯ν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
97
B.2 Distributions for B0 → K∗0ν ¯ν1252
The distributions of the 12 variables used as input for BDT1 training for B0 → K∗0ν ¯ν1253
channel are shown in Fig.53.
0.0
0.5
1.0
1.5
2.0
×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0B_sig_cosTBTO0
2
DataSim.
0
2
4
6
8×105 Belle II preliminary L dt = 1.8 fb
-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0.00 0.05 0.10 0.15 0.20 0.25 0.30B_sig_foxWolframR10
2
DataSim.
0
1
2
3
4×10
5 Belle II preliminary L dt = 1.8 fb-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0.2 0.4 0.6 0.8 1.0 1.2 1.4B_sig_harmonicMomentThrust00
2
DataSim.
0
1
2
3
4
×105 Belle II preliminary L dt = 1.8 fb-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0.0 0.2 0.4 0.6 0.8 1.0
B_sig_harmonicMomentThrust2
0
2
DataSim.
0
1
2
3
4 ×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
0.00 0.05 0.10 0.15 0.20B_sig_KSFWVariables_hoo00
2
DataSim.
0
2
4
6
×105 Belle II preliminary L dt = 1.8 fb-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0.00 0.02 0.04 0.06 0.08
B_sig_KSFWVariables_hoo2
0
2
DataSim.
0
1
2
3
×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
0.10 0.05 0.00 0.05 0.10 0.15 0.20 0.25B_sig_KSFWVariables_hso220
2
DataSim.
0
1
2
3
4
5×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
0.10 0.05 0.00 0.05 0.10 0.15 0.20 0.25B_sig_KSFWVariables_hso240
2
DataSim.
1
2
3
4
×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
6 4 2 0 2 4 6
B_sig_roeDeltae_ipMask
0
2
DataSim.
0
1
2
3
4
5
×105 Belle II preliminary L dt = 1.8 fb-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0 2 4 6
B_sig_roeP_ipMask
0
2
DataSim.
0
1
2
3
4×10
5 Belle II preliminary L dt = 1.8 fb-1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−B 0→K ∗0ν¯ν
Model stat. unc.Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0B_sig_roePTheta_ipMask0
2
DataSim.
0.0
0.5
1.0
1.5
×105 Belle II preliminary L dt = 1.8 fb-1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
B 0→K ∗0ν¯νModel stat. unc.
Data
1.0 0.5 0.0 0.5 1.0B_sig_thrustAxisCosTheta0
2
DataSim.
Figure 53: BDT1 input variables for the channel B0 → K∗0ν ¯ν. The comparison corre-
```
sponds to 1% of exp18 data (89 fb−1)and run-independent simulation (200 fb−1).
```
1254
The distributions of the 39 variables used as input for BDT2 training for B0 → K∗0νν1255
channel are shown in Fig.54 55 56.1256
98
0
2
4
6
8
Event density
×104 Belle II preliminary L dt = 89 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000
Model stat. unc.Data
0.2 0.4 0.6 0.8B_sig_cosTBz0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
1 0 1 2 3B_sig_forwardHemisphereZ0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.2 0.4 0.6B_sig_foxWolframR20.75
1.001.25DATAMC
0
1
2
3
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.01 0.02 0.03B_sig_KSFWVariables_hoo20.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20 0.25B_sig_KSFWVariables_hso000.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.00 0.05 0.10B_sig_KSFWVariables_hso020.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.025 0.000 0.025 0.050 0.075 0.100B_sig_KSFWVariables_hso120.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20B_sig_KSFWVariables_hso200.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.05 0.10 0.15 0.20B_sig_KSFWVariables_hso220.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20 0.25 0.30 0.35B_sig_Kstar0_ArmenterosDaughter1Qt0.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.05 0.10 0.15 0.20 0.25 0.30 0.35B_sig_Kstar0_ArmenterosDaughter2Qt0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.5 0.0 0.5B_sig_Kstar0_cos_p1_p20.75
1.001.25DATAMC
Figure 54: BDT2 input variables for the channel B0 → K∗0νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
99
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.02 0.04 0.06 0.08 0.10B_sig_Kstar0_deltaRho_d1d20.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.02 0.04 0.06 0.08 0.10B_sig_Kstar0_deltaZ_d1d20.75
1.001.25DATAMC
0
1
2
3
4
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.0 0.2 0.4 0.6 0.8B_sig_kstar0_DpKpipi_update_chiProb0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.5 0.0 0.5B_sig_kstar0_DpKpipi_update_cosAngleXYPlane0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.02 0.04 0.06 0.08 0.10B_sig_kstar0_DpKpipi_update_drS0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10B_sig_kstar0_DpKpipi_update_mean_dz_pion_to_SigV0.75
1.001.25DATAMC
0
2
4
6
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.05 0.10 0.15 0.20B_sig_Kstar0_dr_to_TagV_momentum_line0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10B_sig_Kstar0_dz_to_TagV_momentum_line0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.05 0.10 0.15 0.20B_sig_Kstar0_dr_to_TagV0.75
1.001.25DATAMC
0
1
2
3
4
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10B_sig_Kstar0_dz_to_TagV0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.00 0.02 0.04 0.06 0.08 0.10B_sig_Kstar0_drS0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.1 0.0 0.1 0.2B_sig_Kstar0_dzS0.8
1.0
1.2
DATAMC
Figure 55: BDT2 input variables for the channel B0 → K∗0νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
100
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.85 0.90 0.95B_sig_Kstar0_M0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10 0.15 0.20B_sig_Kstar0_pi_dzS0.75
1.001.25DATAMC
0
1
2
3
4
5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
2 3 4 5 6 7 8 9B_sig_nROE_Charged_ipMask0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
2.0
2.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0 5 10 15B_sig_nROE_Photons_ipMask0.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
3 2 1 0B_sig_roeDeltae_ipMask0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.5 1.0 1.5 2.0B_sig_roePt_ipMask0.75
1.001.25DATAMC
0.0
0.2
0.4
0.6
0.8
1.0
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
3 4 5 6B_sig_weMissE_ipMask_00.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0B_sig_weMissM2OverMissE_ipMask0.75
1.001.25DATAMC
0
2
4
6
Event density
×104 Belle II preliminary L dt = 89 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000
Model stat. unc.Data
0.5 1.0 1.5 2.0 2.5B_sig_weMissPTheta_ipMask_00.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
30 40 50 60 70B_sig_weQ2lnuSimple_ipMask_00.75
1.001.25DATAMC
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.2 0.0 0.2 0.4 0.6B_sig_weXiZ_ipMask0.75
1.001.25DATAMC
0.0
0.5
1.0
1.5
Event density
×106 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0nElectronNoSVD0.75
1.001.25DATAMC
0.0
0.2
0.4
0.6
0.8
1.0
Event density
×106 Belle II preliminary L dt = 89 fb 1B 0B0
B + B −c¯c
s¯su¯u
d¯dτ+τ−
Signal x 10000Model stat. unc.
Data
0 1 2 3 4nLepton_eNoSVDNoTOP_muNoSVD0.75
1.001.25DATAMC
0
2
4
6
8
Event density
×105 Belle II preliminary L dt = 89 fb 1
B 0B0B + B −
c¯cs¯s
u¯ud¯d
τ+τ−Signal x 10000
Model stat. unc.Data
0 1 2 3 4total_charge20.75
1.001.25DATAMC
Figure 56: BDT2 input variables for the channel B0 → K∗0νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
101
B.3 Distributions for B → K∗+νν1257
The distributions of the 11 variables used as input for BDT1 training for B → K∗+νν1258
channel are shown in Fig.57.1259
The distributions of the 73 variables used as input for BDT2 training for B → K∗+νν1260
channel are shown in Fig.58 59 60 61 62 63 64.1261
102
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.04 0.06 0.08 0.10 0.12 0.14KSFWVariables_hoo00.0
0.5
1.0
1.5
2.0
Data/Sim.
0
1
2
3
4
5
6
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
10 20 30 40 50Kstar_candidate_multiplicity0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.24 0.26 0.28 0.30 0.32 0.34 0.36K+,Pi+ p_inKstarFrame0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.825 0.850 0.875 0.900 0.925 0.950 0.975Kstar_M0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.5 1.0 1.5 2.0 2.5Kshort,Pi0 daughterAngle_0_10.0
0.5
1.0
1.5
2.0
Data/Sim.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.110 0.115 0.120 0.125 0.130 0.135 0.140 0.145Pi0 mass before vertex fit0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0nROETracksandPhotons0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
Event Density
×106 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
4.2 4.4 4.6 4.8 5.0 5.2roeMbc0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.5 1.0 1.5 2.0 2.5roePt0.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Event Density
×105 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0 10 20 30 40weQ2lnuSimple_00.0
0.5
1.0
1.5
2.0
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
Event Density
×106 Belle II preliminary L dt = 0.899 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
18 20 22 24 26weQ2lnuSimple_20.0
0.5
1.0
1.5
2.0
Data/Sim.
Figure 57: BDT1 input variables for the channel B → K∗+νν. The comparison corre-
```
sponds to 1% of exp18 data (89 fb−1)and run-independent simulation (200 fb−1).
```
103
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
3.0 2.5 2.0 1.5 1.0 0.5 0.0 0.5 1.0backwardHemisphereZ0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
6
7
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.2 0.4 0.6 0.8cosTBTO0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1
B0B0B + B
ccss
uudd
K* +Sim. stat. unc.
Data
0.2 0.4 0.6 0.8cosTBz0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
1.0 0.5 0.0 0.5 1.0 1.5 2.0 2.5 3.0forwardHemisphereZ0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
6
7
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.05 0.10 0.15 0.20 0.25 0.30 0.35foxWolframR10.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6 0.7foxWolframR20.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.05 0.10 0.15 0.20 0.25 0.30foxWolframR30.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.4 0.5 0.6 0.7 0.8harmonicMomentThrust00.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6harmonicMomentThrust20.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.0 0.1 0.2 0.3 0.4harmonicMomentThrust40.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
3 4 5 6 7KSFWVariables_et0.8
1.0
1.2
Data/Sim.
Figure 58: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
104
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.02 0.04 0.06 0.08 0.10KSFWVariables_hoo00.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.00 0.01 0.02 0.03 0.04 0.05KSFWVariables_hoo20.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.10 0.15 0.20 0.25 0.30KSFWVariables_hso000.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.15 0.10 0.05 0.00 0.05 0.10KSFWVariables_hso010.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.05 0.00 0.05 0.10 0.15KSFWVariables_hso020.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
6
7
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.02 0.00 0.02 0.04 0.06 0.08 0.10 0.12KSFWVariables_hso120.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.02 0.04 0.06 0.08 0.10 0.12 0.14 0.16 0.18KSFWVariables_hso200.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.000 0.025 0.050 0.075 0.100 0.125 0.150KSFWVariables_hso220.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.025 0.000 0.025 0.050 0.075 0.100 0.125 0.150KSFWVariables_hso240.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.10 0.15 0.20 0.25 0.30Kstar_ArmenterosDaughter1Qt0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75Kstar_cosHelicityAnglePrimary0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8Kstar_cos_p1_p20.8
1.0
1.2
Data/Sim.
Figure 59: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
105
0.0
0.5
1.0
1.5
2.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8Kstar_D0_pValue_med0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40Kstar_D0_pValue_std0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75Kstar_D0simpleVeto_angleV0rP_20.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00Kstar_D0simpleVeto_M0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.2 0.4 0.6 0.8Kstar_D0veto_chiProb0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00Kstar_D0veto_cosAngleXYPlane0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00 3.25Kstar_D0veto_M0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8Kstar_DP_pValue_med0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35Kstar_DP_pValue_std0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.2 0.4 0.6 0.8Kstar_DPsimpleVeto_chiProb0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.06 0.04 0.02 0.00 0.02 0.04 0.06 0.08K+,Pi+ dzS0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.15 0.10 0.05 0.00 0.05 0.10K+,Pi+ dz_to_TagV0.8
1.0
1.2
Data/Sim.
Figure 60: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
106
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.825 0.850 0.875 0.900 0.925 0.950 0.975Kstar_M0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0 1 2 3 4 5 6 7 8Kstar_nDP0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.2 0.4 0.6 0.8Kshort,Pi0 chiProb0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.9825 0.9850 0.9875 0.9900 0.9925 0.9950 0.9975 1.0000Kshort,Pi0 cosAngleBetweenMomentumAndVertexVector0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00Kshort,Pi0 daughterAngle_0_10.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0Kshort,Pi0 drS_momentum_line0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
10 20 30 40 50 60 70 80Kshort,Pi0 dr_to_TagV0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
2 1 0 1 2 3Kshort,Pi0 dzS_momentum_line0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0 10 20 30 40 50 60 70 80Kshort,Pi0 flightDistance0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6Kshort,Pi0 flightDistanceErr0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.5 1.0 1.5 2.0Kshort,Pi0 flightTime0.8
1.0
1.2
Data/Sim.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0025 0.0050 0.0075 0.0100 0.0125 0.0150 0.0175Kshort,Pi0 flightTimeErr0.8
1.0
1.2
Data/Sim.
Figure 61: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
107
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
25 50 75 100 125 150 175 200Kshort,Pi0 Gamma0_minC2TDist0.8
1.0
1.2
Data/Sim.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
25 50 75 100 125 150 175Kshort,Pi0 Gamma1_minC2TDist0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.115 0.120 0.125 0.130 0.135 0.140 0.145Pi0 mass before vertex fit0.8
1.0
1.2
Data/Sim.
0
2
4
6
8
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
2 4 6 8 10 12 14 16nROE_Photons0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
6
7
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
6 8 10 12 14 16 18 20 22nROETracksandPhotons0.8
1.0
1.2
Data/Sim.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
3 4 5 6 7 8 9nROE_Tracks0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
2.0 1.5 1.0 0.5 0.0 0.5 1.0roeDeltae0.8
1.0
1.2
Data/Sim.
0
2
4
6
8
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
4.90 4.95 5.00 5.05 5.10 5.15 5.20 5.25roeMbc0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0roeNeextra0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
1.0 1.5 2.0 2.5roeP0.8
1.0
1.2
Data/Sim.
0
2
4
6
8
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.2 0.1 0.0 0.1 0.2 0.3roePi_avg_dz0.8
1.0
1.2
Data/Sim.
Figure 62: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
108
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0roePi_avg_pt0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.06 0.04 0.02 0.00 0.02 0.04 0.06 0.08roePi_med_dz0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8roePi_std_dz0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6roePi_std_pt0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.25 0.50 0.75 1.00 1.25 1.50 1.75roePTheta0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6roePt0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.1 0.2 0.3 0.4 0.5 0.6 0.7sphericity0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.075 0.050 0.025 0.000 0.025 0.050 0.075 0.100TagVxBeam0.8
1.0
1.2
Data/Sim.
0
1
2
3
4
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.05 0.00 0.05 0.10TagVzBeam0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.65 0.70 0.75 0.80 0.85 0.90thrust0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.4 0.2 0.0 0.2 0.4 0.6 0.8thrustAxisZ0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Events
×105 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
5 6 7 8visibleEnergyOfEventCMS0.8
1.0
1.2
Data/Sim.
Figure 63: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
109
0.0
0.5
1.0
1.5
2.0
Events
×105 Belle II preliminary L dt = 89 fb 1
B0B0B + B
ccss
uudd
K* +Sim. stat. unc.
Data
0.5 1.0 1.5 2.0 2.5weMissPTheta_00.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0nLepton_eNoSVDNoTOP_muNoSVD0.8
1.0
1.2
Data/Sim.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Events
×106 Belle II preliminary L dt = 89 fb 1B0B0
B + Bcc
ssuu
dd
K* +Sim. stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0total_charge20.8
1.0
1.2
Data/Sim.
Figure 64: BDT2 input variables for the channel B → K∗+νν. The comparison corre-
sponds to 90 fb−1 of total data and run-dependent simulation. The signal region is kept
blinded by applying BDT1 < 0.99 selection.
110
C Optimization of photon selection for ROE1262
In the published B+ → K+ν ¯ν analysis, we include in the ROE only photons with a min-1263
imum energy of 100 MeV. For this analysis, we studied the possibility of including low-1264
energy neutral clusters by lowering the energy threshold to 60 MeV. This implies including1265
```
also a large number of misreconstructed (fake) photons, typically having low energy. A1266
```
previous study on ECL clusters not matched to photons using B+ → K+Jψ→µ+µ− events1267
```
(Appendix K in [29]) shows that a large fraction of them has a small distance from the1268
```
nearest charged track, indicating the presence of an hadronic split-off process. We require1269
```
the minimum distance from the center of cluster to the nearest charged track (minC2TDist)1270
```
longer than 20 cm to suppress these misreconstructed photons while retaining the major-1271
ity of the matched photons. Figure 65 shows the distributions of ROE-related observables1272
with the E > 100 MeV requirement and with the E > 60 MeV requirement, in addition to1273
the fake photon suppression selection. We observe an improvement in the data-MC agree-
0
1
2
3
4
5
Event density
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
5.0 2.5 0.0 2.5 5.0 7.5 10.0
B_sig_roeDeltae_ipMask
0.8
1.0
1.2
DATA, E > 100MeVMCrd, E > 100MeV
0
2
4
6
Event density
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
5.0 2.5 0.0 2.5 5.0 7.5 10.0
B_sig_roeDeltae_ipMask
0.8
1.0
1.2
DATA, E > 60MeVMCrd, E > 60MeV
0
2
4
6
Event density
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10 0.15 0.20
B_sig_KSFWVariables_hso22
0.8
1.0
1.2
DATA, E > 100MeVMCrd, E > 100MeV
0
2
4
6
Event density
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0.10 0.05 0.00 0.05 0.10 0.15 0.20
B_sig_KSFWVariables_hso22
0.8
1.0
1.2
DATA, E > 60MeVMCrd, E > 60MeV
```
Figure 65: Data and simulation distributions of (top) ∆E(ROE) and (bottom) Hso22 for
```
```
B0 → K∗0ν ¯ν reconstructed candidates after applying (left) the selection E > 100 MeV
```
```
and (right) the selection E > 60 MeV and minC2TDist > 20 cm.
```
1274
111
0.0050.0000.005d
B_sig_roeDeltae_ipMaskB_sig_KSFWVariables_hso22
B_sig_roeP_ipMaskB_sig_KSFWVariables_hso24
B_sig_foxWolframR1B_sig_KSFWVariables_hoo0
B_sig_roePTheta_ipMaskB_sig_harmonicMomentThrust0
B_sig_KSFWVariables_hoo2B_sig_cosTBTO
B_sig_harmonicMomentThrust2B_sig_thrustAxisCosTheta
shift
0.005 0.010 0.015 0.020 0.025Data vs. MCrd distance
E>100MeVE>60MeV
0.020.00 0.02
```
d * (dE > 100MeV)
```
B_sig_roeDeltae_ipMaskB_sig_KSFWVariables_hso22
B_sig_roeP_ipMaskB_sig_KSFWVariables_hso24
B_sig_foxWolframR1B_sig_KSFWVariables_hoo0
B_sig_roePTheta_ipMaskB_sig_harmonicMomentThrust0
B_sig_KSFWVariables_hoo2B_sig_cosTBTO
B_sig_harmonicMomentThrust2B_sig_thrustAxisCosTheta
shift
0.1 0.2 0.3 0.4 0.5 0.6 0.7MCri background vs. signal distance
E>100MeVE>60MeV
```
Figure 66: Jensen-Shannon distances between (left) data and MC and (right) signal and
```
background distributions for the BDT1 training inputs.
```
ment of the ∆E(ROE) distribution, and better (worse) consistency in the peak (edges)1275
```
of Hso22 . We quantify the data-MC agreement and the signal-background discriminating1276
power with the two sets of selections by calculating the corresponding Jensen-Shannon1277
distances. The left plot in Fig. 66 shows the distance between data and MC for the BDT11278
training variables, for both the nominal and new selections, along with their difference1279
∆d. The right plot shows the distance between signal and background distributions in1280
```
simulation, along with the relative difference ∆d × dist(E > 100MeV). We observe similar1281
```
results for both selections, with no clear indication on which choice is optimal. Neverthe-1282
less, we observe a large improvement in the data-MC agreement when looking at events1283
with a large number of neutral clusters. Figure 67 shows the distributions of the number1284
of ECL clusters in the ROE and of the total number of tracks and neutral clusters in1285
the ROE with the two sets of selections. The looser energy requirement shows better1286
data-simulation agreement, in particular when the number of photons is larger than 10.1287
112
0.0
0.5
1.0
1.5
Event density
×105 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 5 10 15 20
B_sig_nROE_NeutralECLClusters_ipMask
0.8
1.0
1.2
DATA, E > 100MeVMCrd, E > 100MeV
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 5 10 15 20
B_sig_nROE_NeutralECLClusters_ipMask
0.8
1.0
1.2
DATA, E > 60MeVMCrd, E > 60MeV
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 10 20 30 40
B_sig_nROETracksandPhotons
0.8
1.0
1.2
DATA, E > 100MeVMCrd, E > 100MeV
0.00
0.25
0.50
0.75
1.00
1.25
Event density
×105 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 10 20 30 40
B_sig_nROETracksandPhotons
0.8
1.0
1.2
DATA, E > 60MeVMCrd, E > 60MeV
```
Figure 67: Data-MC distributions of (top) number of ECL neutral clusters in the ROE
```
```
and (bottom) number of tracks and photons in the ROE for B0 → K∗0ν ¯ν reconstructed
```
```
candidates after applying (left) the selection E > 100 MeV and (right) the selection
```
E > 60 MeV and minC2TDist > 20 cm.
113
D Low-multiplicity events suppression1288
The presence of a large data-simulation discrepancy in the low-ROE mass and ROE1289
```
missing angle distributions (Fig. 68) indicates that some physics processes are missing1290
```
in the simulation. The discrepancy is particularly large in the low-visible energy region,1291
indicating the presence of low-multiplicity processes with similar topology as the B0 →1292
```
K(∗)ν ¯ν events.
```
0
2
4
6
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 2 4 6 8 10 12
B_sig_roeM_ipMask
0.8
1.0
1.2
DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
B_sig_weMissPTheta_ipMask_0
0.8
1.0
1.2
DATARDMC
2
4
6
×104 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 2 4 6 8 10 12
B_sig_visibleEnergyOfEventCMS
0.8
1.0
1.2
DATARDMC
0.0
0.5
1.0
1.5
2.0
2.5 ×10
5 Belle II preliminary L dt = 0.9 fb-1
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
2 3 4 5 6 7 8 9
B_sig_nROE_Tracks_ipMask
0.8
1.0
1.2
DATARDMC
```
Figure 68: Distributions of B0 → K∗0ν ¯ν candidates reconstructed in (dots) 0.9 fb−1 of
```
```
Belle II data and (solid histogram) 3.6 fb−1 of Belle II simulation. Different colors indicate
```
different contributions to the simulation.
1293
The Belle II simulation does not include low-multiplicity γγ processes such as γγ →1294
KπKπ, K∗Kπ or K∗ ¯K∗, K0S K0S , ρϕ, and ρω. The cross section for these processes is large1295
```
([34, 35, 36]), as shown in Tab. 40, and the presence of a KK(∗)-like particle in the final1296
```
state makes these processes similar to the signal events. We investigate the contribution1297
```
of two-photon processes by focusing on the low-ROE mass region (< 3.5 GeV) in the1298
```
B0 → K∗0ν ¯ν channel. In the di-photon process e+e− → e+e−γγ, γγ → X, with X1299
114
```
Decay cross-section (nb)
```
γγ → K−π+K−π+ 2.4±0.9
γγ → K∗0K−π+ 2.0±0.7
γγ → K∗0 ¯K∗0 1.3±0.4
γγ → K0S K0S ππ 1.2 ± 0.6
γγ → K0S Kππ0 1.8 ± 0.8
γγ → K+ ¯K∗+ 7.8±3.1±2.0
γγ → K0S K0S 0.7 ± 0.3
Table 40: Cross sections of di-photon processes, taken from [34, 35, 36].
```
decaying to four charged particles (along with at most 2 neutral particles), the scattered1300
```
electron-positron pair is deflected at small angles, thus remaining within the beam pipe1301
and not reaching the detector. This causes an excess in the missing-momentum angle1302
```
distribution at small and high values, that is, along the beam axis (Fig. 69). We suppress1303
```
these low-multiplicity events by requiring 0.3 < θpmiss < 2.8 and Evisible >4 GeV, as shown1304
in Fig. 70. The low multiplicity events affect distributions of observables used in the1305
BDT2, so we apply these selections before its training phase.1306
The signal efficiency loss with the low multiplicity event rejection is 4.8%, 4%, and1307
6% for the B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channel, respectively.1308
115
0
500
1000
1500
2000
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
B_sig_roeM_ipMask
0.8
1.0
1.2
DATARDMC
0
500
1000
1500
2000
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
B_sig_weMissPTheta_ipMask_0
0.8
1.0
1.2
DATARDMC
0
1000
2000
3000
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 1000
Model stat. unc.
Data
0 1 2 3 4 5 6 7
B_sig_visibleEnergyOfEventCMS
0.8
1.0
1.2
DATARDMC
```
Figure 69: Distributions of B0 → K∗0ν ¯ν candidates reconstructed in (dots) 0.9 fb−1 of
```
```
Belle II data and (solid histogram) 3.6 fb−1 of Belle II simulation in the low-multiplicity
```
```
background-dominated region, (mROE < 3.5 GeV). Different colors indicate different con-
```
tributions to the simulation.
116
0
250
500
750
1000
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 500
Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
B_sig_roeM_ipMask
0.8
1.0
1.2
DATARDMC
0
250
500
750
1000
1250
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 500
Model stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
B_sig_weMissPTheta_ipMask_0
0.8
1.0
1.2
DATARDMC
0
500
1000
1500
2000
Belle II preliminary L dt = 0.9 fb-14 tracks
B 0B0
B + B −
c¯c
s¯s
u¯u
d¯d
τ+τ−
Signal x 500
Model stat. unc.
Data
0 1 2 3 4 5 6 7
B_sig_visibleEnergyOfEventCMS
0.8
1.0
1.2
DATARDMC
```
Figure 70: Distributions of B0 → K∗0ν ¯ν candidates reconstructed in (dots) 0.9 fb−1 of
```
```
Belle II data and (solid histogram) 3.6 fb−1 of Belle II simulation in the low-multiplicity
```
```
background-dominated region, (mROE < 3.5 GeV), after requiring 0.3 < θpmiss < 2.8 and
```
Evisible >4 GeV. Different colors indicate different contributions to the simulation.
117
E KaonID > 0.9 and KaonID > 0.75 and PionID > 0.051309
tables1310
Fig. 71, Fig. 72 and Fig. 73 represent the PID efficiency and fake-rate corrections applied1311
to different channels.1312
118
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.96±0.02 0.97±0.02 1.01±0.03 1.00±0.03 1.01±0.04 1.01±0.05 1.00±0.06 1.00±0.070.46±0.03 0.85±0.01 0.99±0.01 0.97±0.01 0.98±0.01 0.98±0.01 0.98±0.02 0.96±0.02
0.00±nan 0.97±0.01 0.99±0.01 0.98±0.01 0.96±0.01 0.98±0.01 0.96±0.01 1.01±0.011.00±0.01 0.99±0.01 0.96±0.01 0.95±0.01 0.97±0.01 0.99±0.01 1.24±0.02
1.02±0.02 0.99±0.01 0.96±0.01 0.92±0.01 0.95±0.01 1.00±0.01 1.37±0.021.05±0.02 0.97±0.00 0.94±0.01 0.89±0.01 0.94±0.01 0.99±0.01 1.10±0.01
1.06±0.02 0.97±0.01 0.92±0.01 0.88±0.01 0.92±0.01 0.96±0.01 1.06±0.011.07±0.02 0.94±0.01 0.91±0.01 0.86±0.01 0.91±0.01 0.95±0.01 1.04±0.01
1.08±0.02 0.92±0.01 0.91±0.01 0.81±0.01 0.87±0.01 0.94±0.01 1.06±0.01
K ratio table for cut "kaonID > 0.9"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(a) K− ratio table for cut kaonID > 0.9.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.93±0.02 0.98±0.02 1.00±0.03 1.01±0.03 1.00±0.04 1.01±0.05 1.01±0.06 0.97±0.060.44±0.03 0.84±0.01 0.99±0.01 0.97±0.01 0.97±0.01 0.98±0.01 0.97±0.02 0.96±0.01
0.12±0.36 0.94±0.01 0.99±0.01 0.97±0.01 0.97±0.01 0.97±0.01 0.97±0.01 1.00±0.010.00±nan 0.98±0.01 0.99±0.01 0.96±0.01 0.95±0.01 0.96±0.01 0.99±0.01 1.22±0.01
1.01±0.01 0.98±0.01 0.95±0.01 0.92±0.01 0.95±0.01 0.98±0.01 1.31±0.021.05±0.02 0.98±0.00 0.95±0.01 0.91±0.01 0.92±0.01 0.98±0.01 1.09±0.01
1.07±0.02 0.96±0.01 0.94±0.01 0.86±0.01 0.90±0.01 0.96±0.01 1.06±0.011.09±0.02 0.94±0.01 0.92±0.01 0.85±0.01 0.89±0.01 0.95±0.01 1.05±0.01
0.00±nan 1.08±0.02 0.92±0.01 0.91±0.01 0.87±0.01 0.87±0.01 0.93±0.01 1.05±0.01
K ratio table for cut "kaonID > 0.9"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(b) K+ ratio table for cut kaonID > 0.9.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
1.32±0.59 1.45±0.44 3.53±2.28 2.45±1.24 1.75±0.37 2.10±0.690.21±1.05 2.84±0.54 105.06±98.83 6.78±3.21 3.17±1.45 1.17±0.10 0.40±0.19
0.99±0.17 1.24±0.13 1.33±0.08 1.43±0.07 1.27±0.11 0.79±0.08 0.58±0.070.00±nan 2.37±0.14 0.95±0.14 1.38±0.10 1.47±0.07 1.53±0.06 0.68±0.08 0.52±0.11
5.08±0.10 1.05±0.19 1.27±0.11 1.38±0.07 1.40±0.06 1.53±0.08 0.89±0.196.14±0.08 1.42±0.16 1.14±0.12 1.29±0.07 1.52±0.05 1.38±0.08 1.32±0.17
5.03±0.06 1.29±0.44 1.19±0.17 1.21±0.07 1.44±0.05 1.78±0.08 1.10±0.223.99±0.07 1.62±0.26 1.57±0.27 0.98±0.09 1.45±0.05 1.67±0.08 1.00±0.20
3.04±0.07 1.30±0.19 1.25±0.18 1.05±0.09 1.25±0.07 1.32±0.09 1.00±0.27
pi ratio table for cut "kaonID > 0.9"
0
20
40
60
80
100
```
(c) Fake π− ratio table for cut kaonID > 0.9.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
5.81±3.76 4.67±3.18 3.59±2.28 1.39±0.68 1.44±0.27 2.02±0.710.65±0.54 9.16±4.75 13.42±9.99 14.07±11.99 0.79±0.15 0.46±0.17
0.34±1.13 0.94±0.18 1.11±0.16 1.20±0.09 1.35±0.08 1.37±0.11 0.77±0.08 0.59±0.072.08±0.13 1.17±0.17 1.26±0.10 1.52±0.07 1.34±0.07 0.79±0.08 0.52±0.09
6.35±0.22 1.41±0.15 1.14±0.11 1.33±0.07 1.49±0.06 1.13±0.10 0.96±0.175.93±0.08 1.49±0.15 1.39±0.10 1.33±0.07 1.40±0.06 1.54±0.11 1.61±0.18
4.73±0.07 1.25±0.38 1.47±0.18 1.12±0.08 1.49±0.05 1.76±0.10 1.76±0.174.05±0.07 1.28±0.28 1.36±0.40 1.04±0.09 1.36±0.07 1.48±0.08 1.20±0.28
2.85±0.06 1.20±0.16 1.22±0.17 0.84±0.10 1.19±0.08 1.37±0.09 1.04±0.24
pi ratio table for cut "kaonID > 0.9"
0
2
4
6
8
10
12
14
```
(d) Fake π+ ratio table for cut kaonID > 0.9.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.00 1.01±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.94±0.00 0.94±0.011.03±0.00 1.05±0.00 0.97±0.00 0.98±0.00 0.99±0.00 1.00±0.00 0.99±0.01 1.03±0.01
1.02±0.00 1.02±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.02±0.01 1.03±0.011.01±0.00 1.00±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.99±0.00 1.02±0.01 1.07±0.01
1.02±0.00 0.99±0.00 0.99±0.00 0.99±0.00 0.99±0.00 0.99±0.00 1.00±0.00 1.04±0.011.01±0.00 0.96±0.00 0.99±0.00 0.98±0.00 0.99±0.00 0.97±0.00 1.00±0.00 1.08±0.01
1.00±0.01 0.92±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.97±0.00 1.00±0.00 1.05±0.011.00±0.01 0.91±0.01 0.98±0.01 0.99±0.01 0.99±0.00 0.97±0.00 1.00±0.00 1.06±0.01
1.01±0.01 0.90±0.01 0.98±0.01 0.99±0.00 0.99±0.01 0.97±0.01 1.01±0.01 1.06±0.01
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
```
(e) π− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.99±0.01 1.01±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.95±0.00 0.94±0.011.03±0.00 1.05±0.00 0.98±0.00 0.99±0.00 1.00±0.00 0.99±0.00 1.00±0.01 1.01±0.01
1.02±0.00 1.03±0.00 0.98±0.00 0.99±0.00 1.00±0.00 0.99±0.00 1.02±0.01 1.04±0.011.02±0.00 1.01±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.00±0.01 1.06±0.01
1.02±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.00 1.00±0.00 1.06±0.011.00±0.01 0.96±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.06±0.01
1.00±0.01 0.92±0.01 0.98±0.01 0.98±0.00 0.99±0.00 0.97±0.00 0.99±0.00 1.04±0.010.99±0.01 0.90±0.01 0.98±0.01 0.98±0.01 0.99±0.00 0.97±0.00 1.00±0.00 1.05±0.01
1.01±0.02 0.88±0.01 0.99±0.01 0.99±0.01 0.99±0.00 0.97±0.01 1.01±0.01 1.06±0.01
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
```
(f) π+ ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.42±1.08 0.64±2.24 0.44±2.081.62±0.03 1.50±0.04 1.03±0.15 1.24±0.11 1.23±0.11 1.26±0.20 1.42±0.41 1.80±0.71
1.13±0.00 1.07±0.01 1.01±0.05 1.05±0.03 1.17±0.03 1.12±0.04 1.36±0.07 1.48±0.131.06±0.00 1.02±0.01 1.05±0.04 1.12±0.03 1.19±0.03 1.18±0.03 1.26±0.05 1.39±0.13
1.01±0.00 0.99±0.01 1.01±0.03 1.13±0.02 1.24±0.02 1.23±0.03 1.35±0.04 1.31±0.131.01±0.00 0.96±0.01 1.11±0.03 1.19±0.02 1.25±0.01 1.18±0.02 1.32±0.03 1.46±0.09
1.00±0.00 0.95±0.01 1.15±0.03 1.17±0.02 1.15±0.01 1.20±0.01 1.36±0.03 1.31±0.121.00±0.00 0.92±0.01 1.29±0.03 1.17±0.02 1.13±0.01 1.14±0.01 1.37±0.03 1.56±0.11
1.01±0.01 0.92±0.01 1.37±0.03 1.12±0.02 1.11±0.01 1.13±0.01 1.39±0.03 1.20±0.11
K ratio table for cut "pionID > 0.05"
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
(g) Fake K− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.88±1.01 1.11±2.02 0.80±2.08 0.12±2.96 0.75±3.12 1.55±3.931.59±0.02 1.51±0.04 1.07±0.16 1.17±0.11 1.29±0.13 1.31±0.20 1.46±0.49 2.37±0.47
1.08±0.00 1.08±0.01 1.05±0.06 1.06±0.04 1.13±0.03 1.23±0.05 1.34±0.10 1.65±0.151.05±0.00 1.04±0.01 1.08±0.04 1.15±0.03 1.19±0.02 1.23±0.03 1.24±0.06 1.41±0.13
1.02±0.00 1.00±0.01 1.02±0.03 1.17±0.03 1.28±0.02 1.27±0.02 1.47±0.04 1.27±0.111.00±0.00 0.96±0.01 1.12±0.03 1.16±0.02 1.18±0.01 1.24±0.02 1.28±0.04 1.32±0.10
0.99±0.00 0.93±0.01 1.18±0.03 1.13±0.02 1.15±0.01 1.24±0.01 1.46±0.03 1.19±0.141.00±0.01 0.91±0.01 1.29±0.03 1.14±0.02 1.12±0.01 1.16±0.01 1.40±0.03 1.24±0.12
1.01±0.01 0.90±0.01 1.34±0.03 1.12±0.02 1.04±0.01 1.12±0.01 1.48±0.03 1.28±0.11
K ratio table for cut "pionID > 0.05"
0.0
0.5
1.0
1.5
2.0
```
(h) Fake K+ ratio table for cut pionID > 0.05.
```
Figure 71: PID tables for run-dependent samples, generated with cuts: nPXDHits >
0 and pt > 0.1 and |dz| < 0.3 and dr < 0.05 and E < 3.0 and nCDCHits > 10.
These corrections are applied to B+ → K∗+ν ¯ν channel.
119
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.96±0.02 0.98±0.02 0.99±0.02 0.98±0.03 0.99±0.03 0.99±0.04 0.98±0.05 1.00±0.070.65±0.02 0.86±0.01 0.98±0.01 0.96±0.01 0.97±0.01 0.97±0.01 0.98±0.02 0.95±0.02
0.09±0.11 0.83±0.01 0.97±0.01 0.97±0.01 0.94±0.01 0.97±0.01 0.97±0.01 0.98±0.010.91±0.01 0.98±0.01 0.96±0.01 0.95±0.01 0.96±0.01 0.99±0.01 1.11±0.02
0.13±1.10 0.93±0.01 0.98±0.01 0.96±0.01 0.92±0.01 0.95±0.01 1.00±0.01 1.27±0.020.00±nan 0.93±0.01 0.97±0.01 0.94±0.01 0.88±0.01 0.94±0.01 1.01±0.01 1.15±0.01
0.12±1.08 0.97±0.02 0.96±0.01 0.92±0.01 0.87±0.01 0.92±0.01 0.98±0.01 1.07±0.010.98±0.02 0.94±0.01 0.90±0.01 0.86±0.01 0.91±0.01 0.97±0.01 1.06±0.01
1.01±0.02 0.91±0.01 0.89±0.01 0.82±0.01 0.87±0.01 0.96±0.01 1.05±0.010.00±nan 0.93±0.03 0.89±0.01 0.87±0.01 0.81±0.01 0.86±0.01 0.95±0.01 1.06±0.01
0.86±0.06 0.85±0.02 0.84±0.02 0.83±0.02 0.85±0.01 0.96±0.01 1.05±0.020.90±0.08 0.84±0.02 0.82±0.02 0.85±0.01 0.87±0.01 0.93±0.01 1.04±0.01
0.87±0.09 0.89±0.04 0.87±0.02 0.87±0.01 0.93±0.01 1.04±0.02
K ratio table for cut "kaonID > 0.75"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(a) K− ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.94±0.02 0.98±0.02 0.98±0.02 0.98±0.02 0.99±0.03 1.00±0.04 0.99±0.05 0.91±0.060.61±0.02 0.86±0.01 0.99±0.01 0.95±0.01 0.97±0.01 0.98±0.01 0.98±0.01 0.96±0.02
0.14±0.10 0.82±0.01 0.98±0.01 0.96±0.01 0.96±0.01 0.97±0.01 0.96±0.01 0.96±0.010.00±nan 0.92±0.01 0.98±0.01 0.96±0.01 0.95±0.01 0.95±0.01 0.98±0.01 1.09±0.01
0.40±0.65 0.94±0.01 0.98±0.01 0.95±0.01 0.92±0.01 0.95±0.01 0.98±0.01 1.23±0.020.95±0.37 0.96±0.01 0.97±0.00 0.94±0.01 0.89±0.01 0.91±0.01 1.00±0.01 1.14±0.02
0.99±0.31 0.96±0.02 0.96±0.01 0.93±0.01 0.87±0.01 0.90±0.01 0.96±0.01 1.11±0.010.72±0.33 0.98±0.02 0.94±0.01 0.90±0.01 0.85±0.01 0.88±0.01 0.97±0.01 1.06±0.01
0.73±0.36 0.98±0.02 0.91±0.01 0.90±0.01 0.86±0.01 0.87±0.01 0.94±0.01 1.05±0.010.73±0.54 0.97±0.03 0.88±0.01 0.87±0.01 0.81±0.01 0.84±0.01 0.91±0.01 1.05±0.01
0.70±0.81 0.90±0.06 0.88±0.02 0.84±0.02 0.82±0.02 0.84±0.01 0.92±0.01 1.03±0.011.24±1.46 0.99±0.08 0.82±0.02 0.81±0.02 0.85±0.02 0.85±0.01 0.92±0.01 1.04±0.01
4.79±3.74 0.74±0.10 0.85±0.05 0.85±0.02 0.83±0.01 0.93±0.01 1.03±0.01
K ratio table for cut "kaonID > 0.75"
0
1
2
3
4
```
(b) K+ ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
10.29±5.73 1.33±0.07 1.67±0.10 1.56±0.11 1.49±0.10 1.14±0.02 1.73±0.05 3.56±0.300.40±0.06 1.04±0.05 1.83±0.08 1.67±0.07 1.73±0.08 1.36±0.05 0.95±0.02 0.58±0.02
0.06±0.19 0.62±0.05 1.11±0.07 1.23±0.05 1.37±0.04 1.34±0.05 0.87±0.03 0.62±0.031.92±0.14 1.29±0.12 1.43±0.08 1.63±0.06 1.49±0.05 0.87±0.04 0.60±0.05
0.00±nan 3.53±0.11 1.01±0.14 1.50±0.09 1.62±0.06 1.70±0.05 1.55±0.07 0.86±0.100.00±nan 4.94±0.15 1.92±0.13 1.37±0.10 1.42±0.06 1.59±0.04 1.68±0.08 1.50±0.16
5.55±0.19 1.51±0.23 1.44±0.12 1.29±0.06 1.70±0.05 2.10±0.09 1.38±0.204.00±0.08 1.97±0.18 1.74±0.15 1.10±0.06 1.36±0.04 2.00±0.08 1.85±0.25
2.65±0.08 1.74±0.14 1.08±0.10 0.99±0.07 1.32±0.05 1.97±0.09 1.48±0.242.47±0.12 1.44±0.14 0.81±0.11 0.82±0.07 1.15±0.05 1.95±0.10 1.57±0.40
2.24±0.22 1.37±0.21 0.87±0.15 0.75±0.09 0.95±0.06 2.01±0.11 1.72±1.290.99±0.38 1.54±0.26 0.94±0.13 0.72±0.07 1.05±0.05 1.93±0.08 4.88±1.15
1.02±0.27 0.86±0.12 1.17±0.09 1.87±0.11 35.68±26.18
pi ratio table for cut "kaonID > 0.75"
0
5
10
15
20
25
30
35
```
(c) Fake π− ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
22.74±17.82 1.31±0.06 1.52±0.09 1.66±0.13 1.36±0.09 1.12±0.02 1.73±0.07 3.04±0.270.35±0.08 1.08±0.06 1.78±0.09 1.90±0.10 1.77±0.11 1.39±0.06 0.84±0.02 0.58±0.02
0.08±0.19 0.68±0.06 1.09±0.08 1.18±0.06 1.35±0.05 1.42±0.05 0.82±0.03 0.63±0.030.09±1.04 1.91±0.12 1.14±0.12 1.38±0.08 1.53±0.06 1.58±0.05 0.83±0.05 0.60±0.04
3.64±5.93 5.29±0.17 1.43±0.11 1.24±0.08 1.45±0.06 1.55±0.05 1.30±0.07 0.88±0.105.84±0.19 1.50±0.12 1.52±0.09 1.47±0.06 1.52±0.05 1.84±0.08 1.90±0.16
0.01±22.35 4.76±0.14 1.51±0.19 1.63±0.11 1.14±0.06 1.50±0.05 1.86±0.09 1.48±0.173.41±0.08 1.93±0.19 1.34±0.19 1.12±0.06 1.49±0.05 1.81±0.09 1.51±0.26
1.41±1.35 2.67±0.08 1.35±0.13 1.42±0.10 0.81±0.07 1.17±0.05 1.70±0.08 2.19±0.280.80±1.35 1.92±0.11 1.17±0.14 1.03±0.11 0.69±0.07 0.96±0.06 1.54±0.12 2.72±0.36
1.81±0.20 1.22±0.21 1.03±0.14 0.68±0.09 0.96±0.07 1.55±0.13 0.78±0.860.89±0.48 1.35±0.29 0.82±0.12 0.71±0.07 0.88±0.06 1.36±0.09 9.53±4.62
0.83±0.33 0.79±0.13 1.18±0.10 1.45±0.11 9.75±4.66
pi ratio table for cut "kaonID > 0.75"
0
5
10
15
20
```
(d) Fake π+ ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
2.18±0.93 2.57±0.95 0.74±2.14 6.06±3.48 1.50±2.291.72±0.02 1.63±0.04 1.24±0.12 1.43±0.08 1.31±0.07 1.38±0.14 1.73±0.26 3.79±0.53
1.10±0.01 1.10±0.01 1.08±0.05 1.10±0.03 1.25±0.03 1.17±0.04 1.36±0.06 1.33±0.111.03±0.00 1.08±0.01 1.09±0.04 1.18±0.03 1.26±0.02 1.28±0.03 1.30±0.05 0.99±0.11
1.01±0.00 1.06±0.01 1.10±0.04 1.23±0.02 1.40±0.02 1.38±0.03 1.36±0.04 1.03±0.111.00±0.00 1.02±0.01 1.16±0.03 1.32±0.02 1.42±0.02 1.33±0.02 1.37±0.04 1.04±0.09
1.00±0.00 0.99±0.01 1.27±0.04 1.37±0.02 1.31±0.01 1.39±0.02 1.38±0.04 0.99±0.111.00±0.01 0.96±0.01 1.39±0.04 1.31±0.02 1.24±0.01 1.27±0.02 1.36±0.03 1.11±0.11
1.01±0.01 0.94±0.01 1.56±0.03 1.26±0.02 1.18±0.01 1.19±0.01 1.38±0.03 0.91±0.131.01±0.01 0.95±0.02 1.49±0.04 1.22±0.02 1.13±0.01 1.19±0.01 1.35±0.03 1.13±0.12
1.03±0.03 0.90±0.04 1.66±0.06 1.28±0.02 1.12±0.02 1.19±0.02 1.33±0.05 0.97±0.231.05±0.13 0.90±0.05 1.50±0.05 1.22±0.02 1.08±0.01 1.21±0.02 1.31±0.03 1.07±0.11
1.50±0.18 1.06±0.04 1.07±0.03 1.18±0.03 1.25±0.03 1.07±0.06
K ratio table for cut "pionID > 0.05"
0
1
2
3
4
5
6
```
(e) Fake K− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
4.47±1.28 6.85±3.34 30.57±27.98 1.38±1.35 9.59±5.411.69±0.03 1.59±0.03 1.13±0.12 1.32±0.08 1.33±0.09 1.39±0.13 1.48±0.28 2.39±0.23
1.06±0.01 1.14±0.01 1.12±0.05 1.14±0.03 1.20±0.03 1.30±0.04 1.44±0.07 1.46±0.111.03±0.00 1.08±0.01 1.15±0.04 1.26±0.03 1.30±0.02 1.36±0.03 1.28±0.06 1.15±0.10
1.01±0.00 1.06±0.01 1.12±0.04 1.29±0.03 1.44±0.02 1.39±0.03 1.49±0.04 1.05±0.101.00±0.00 1.02±0.01 1.20±0.03 1.32±0.02 1.42±0.02 1.51±0.02 1.39±0.04 0.99±0.11
0.99±0.01 0.99±0.01 1.32±0.04 1.29±0.02 1.28±0.01 1.39±0.02 1.57±0.04 0.80±0.120.99±0.01 0.96±0.01 1.43±0.04 1.29±0.02 1.23±0.01 1.32±0.02 1.40±0.04 0.99±0.13
0.99±0.01 0.94±0.02 1.52±0.04 1.24±0.02 1.11±0.01 1.20±0.01 1.46±0.03 1.08±0.121.01±0.02 0.88±0.02 1.53±0.04 1.24±0.02 1.09±0.01 1.19±0.01 1.57±0.03 1.19±0.12
1.06±0.05 0.83±0.04 1.51±0.05 1.21±0.03 1.09±0.02 1.25±0.02 1.42±0.04 1.21±0.151.02±0.23 0.87±0.06 1.57±0.05 1.18±0.02 1.09±0.01 1.26±0.02 1.48±0.03 1.17±0.07
0.24±1.38 1.22±2.55 1.52±0.16 1.10±0.04 1.10±0.03 1.38±0.03 1.26±0.03 1.10±0.06
K ratio table for cut "pionID > 0.05"
0
5
10
15
20
25
30
```
(f) Fake K+ ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.00 1.00±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.93±0.00 0.91±0.001.01±0.00 1.05±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.01±0.00 0.99±0.00 0.97±0.00
1.01±0.00 1.03±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.02±0.00 1.00±0.001.01±0.00 1.01±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.01±0.00 1.01±0.01
1.01±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.99±0.00 1.01±0.011.00±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.99±0.00 0.98±0.00 1.00±0.00 1.04±0.01
1.00±0.01 0.91±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.97±0.00 1.00±0.00 1.03±0.011.00±0.01 0.91±0.01 0.98±0.01 0.98±0.01 0.99±0.00 0.97±0.00 0.99±0.00 1.04±0.01
1.01±0.01 0.91±0.01 0.97±0.01 0.99±0.00 1.00±0.00 0.97±0.01 1.01±0.01 1.03±0.011.05±0.02 0.90±0.02 1.00±0.01 1.00±0.01 0.99±0.00 0.97±0.01 1.00±0.01 1.03±0.02
0.95±0.09 0.84±0.04 1.00±0.01 1.01±0.01 1.00±0.01 0.98±0.01 1.00±0.01 1.05±0.020.57±0.44 0.81±0.10 0.99±0.02 1.00±0.01 1.00±0.01 0.98±0.01 1.01±0.01 1.03±0.02
0.50±4.88 0.95±0.47 0.97±0.03 1.00±0.01 0.97±0.01 1.03±0.01 1.05±0.02
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
```
(g) π− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.00 1.01±0.00 0.98±0.00 0.97±0.00 0.99±0.00 0.97±0.00 0.93±0.00 0.92±0.001.01±0.00 1.05±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.00±0.00 1.00±0.00 0.97±0.00
1.01±0.00 1.04±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.02±0.00 1.01±0.001.01±0.00 1.01±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.98±0.00 1.01±0.00 1.02±0.01
1.01±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.02±0.011.00±0.01 0.96±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.99±0.00 1.03±0.01
0.99±0.01 0.92±0.01 0.98±0.01 0.97±0.00 0.99±0.00 0.97±0.00 1.00±0.00 1.02±0.010.99±0.01 0.90±0.01 0.97±0.01 0.98±0.01 0.98±0.00 0.97±0.00 1.00±0.00 1.03±0.01
1.00±0.02 0.89±0.01 0.99±0.01 0.99±0.01 1.00±0.00 0.97±0.00 1.00±0.01 1.04±0.011.09±0.05 0.93±0.02 0.99±0.01 0.99±0.01 1.00±0.00 0.97±0.01 1.01±0.01 1.03±0.01
1.21±0.22 0.89±0.05 0.99±0.01 1.00±0.01 1.00±0.01 1.00±0.01 1.01±0.01 1.03±0.020.30±1.15 0.73±0.17 0.95±0.03 0.99±0.01 1.00±0.01 0.99±0.01 1.01±0.01 1.04±0.01
0.56±1.36 1.06±0.04 1.02±0.01 0.98±0.01 1.02±0.01 1.03±0.01
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(h) π+ ratio table for cut pionID > 0.05.
```
Figure 72: PID tables for run-independent samples, generated with cuts: nPXDHits >
0 and pt > 0.1 and E < 5.5. These corrections are applied to B0 → K∗0ν ¯ν channel.
120
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.03 0.99±0.03 1.00±0.03 1.00±0.03 1.01±0.04 1.01±0.05 0.99±0.06 1.01±0.080.66±0.02 0.88±0.01 1.00±0.01 0.97±0.01 0.98±0.02 0.98±0.02 0.98±0.02 0.96±0.02
0.12±0.11 0.85±0.01 0.99±0.01 0.98±0.01 0.96±0.01 0.98±0.01 0.97±0.01 1.00±0.010.00±nan 0.99±0.02 0.99±0.01 0.97±0.01 0.96±0.01 0.98±0.01 0.99±0.01 1.15±0.02
0.38±1.12 1.02±0.02 1.00±0.01 0.97±0.01 0.94±0.01 0.96±0.01 1.01±0.01 1.28±0.020.00±nan 1.02±0.02 0.97±0.01 0.96±0.01 0.91±0.01 0.95±0.01 1.00±0.01 1.08±0.01
0.19±1.05 1.04±0.02 0.97±0.01 0.94±0.01 0.91±0.01 0.94±0.01 0.98±0.01 1.05±0.011.06±0.02 0.95±0.01 0.93±0.01 0.89±0.01 0.94±0.01 0.97±0.01 1.04±0.01
0.00±nan 1.07±0.02 0.92±0.01 0.92±0.01 0.86±0.01 0.90±0.01 0.96±0.01 1.06±0.011.00±0.03 0.91±0.01 0.89±0.01 0.85±0.01 0.89±0.01 0.96±0.01 1.06±0.01
1.01±0.05 0.89±0.02 0.90±0.02 0.87±0.02 0.88±0.01 0.96±0.01 1.08±0.020.95±0.07 0.87±0.02 0.87±0.02 0.89±0.01 0.89±0.01 0.94±0.01 1.06±0.01
0.86±0.07 0.95±0.04 0.94±0.02 0.90±0.01 0.93±0.01 1.06±0.02
K ratio table for cut "kaonID > 0.75"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(a) K− ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.96±0.03 0.99±0.03 0.99±0.03 1.00±0.03 1.00±0.04 1.00±0.05 0.99±0.06 0.92±0.070.62±0.02 0.88±0.01 1.00±0.01 0.97±0.01 0.97±0.02 0.98±0.02 0.98±0.02 0.96±0.02
0.16±0.09 0.85±0.01 0.98±0.01 0.97±0.01 0.98±0.01 0.97±0.01 0.97±0.01 0.98±0.010.00±nan 0.98±0.02 0.99±0.01 0.97±0.01 0.97±0.01 0.97±0.01 0.99±0.01 1.14±0.01
0.88±0.63 1.01±0.01 0.99±0.01 0.96±0.01 0.94±0.01 0.96±0.01 0.99±0.01 1.25±0.021.74±0.36 1.05±0.02 0.98±0.00 0.96±0.01 0.93±0.01 0.94±0.01 0.99±0.01 1.09±0.01
1.01±0.26 1.06±0.02 0.97±0.01 0.95±0.01 0.90±0.01 0.92±0.01 0.97±0.01 1.06±0.010.96±0.31 1.08±0.02 0.95±0.01 0.93±0.01 0.89±0.01 0.91±0.01 0.97±0.01 1.06±0.01
0.92±0.34 1.07±0.02 0.93±0.01 0.93±0.01 0.90±0.01 0.90±0.01 0.94±0.01 1.06±0.011.06±0.51 1.02±0.03 0.90±0.01 0.91±0.01 0.85±0.01 0.87±0.01 0.92±0.01 1.04±0.01
1.78±0.81 0.99±0.06 0.91±0.02 0.88±0.02 0.86±0.02 0.87±0.01 0.92±0.01 1.04±0.013.29±1.76 1.01±0.07 0.85±0.02 0.85±0.02 0.90±0.01 0.88±0.01 0.93±0.01 1.04±0.01
-0.00±nan 0.76±0.09 0.86±0.04 0.89±0.02 0.86±0.01 0.92±0.01 1.04±0.01
K ratio table for cut "kaonID > 0.75"
0.0
0.5
1.0
1.5
2.0
2.5
3.0
```
(b) K+ ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
4.66±1.57 1.40±0.07 1.53±0.07 1.67±0.13 1.54±0.10 1.34±0.03 1.92±0.06 2.56±0.150.35±0.06 1.03±0.04 1.80±0.06 1.74±0.06 1.91±0.08 1.46±0.05 0.88±0.02 0.53±0.02
0.07±0.19 0.60±0.05 1.13±0.06 1.24±0.04 1.46±0.04 1.31±0.03 0.80±0.03 0.61±0.020.00±nan 1.88±0.10 0.92±0.11 1.35±0.07 1.46±0.05 1.45±0.04 0.77±0.04 0.58±0.04
0.00±nan 3.43±0.11 1.08±0.16 1.26±0.09 1.44±0.05 1.46±0.04 1.29±0.05 0.89±0.090.00±nan 4.63±0.06 1.33±0.13 1.22±0.09 1.30±0.05 1.58±0.04 1.52±0.06 1.24±0.12
0.00±nan 4.35±0.05 1.32±0.36 1.20±0.12 1.23±0.05 1.50±0.04 1.86±0.07 1.16±0.183.59±0.05 1.59±0.20 1.48±0.19 1.02±0.06 1.45±0.04 1.66±0.06 1.05±0.17
2.97±0.07 1.27±0.14 1.21±0.12 0.98±0.07 1.32±0.05 1.44±0.07 1.17±0.242.01±0.08 1.09±0.11 0.88±0.10 0.84±0.06 1.19±0.04 1.27±0.10 1.28±0.54
2.41±0.17 1.11±0.16 0.86±0.14 0.80±0.08 1.01±0.06 1.10±0.09 0.65±1.031.00±0.33 1.39±0.20 0.85±0.11 0.78±0.06 1.00±0.05 0.90±0.06 1.09±0.50
0.00±4.67 1.01±0.23 0.80±0.11 1.12±0.08 0.65±0.07 1.77±0.49
pi ratio table for cut "kaonID > 0.75"
0
1
2
3
4
```
(c) Fake π− ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
37.70±32.50 1.54±0.08 1.53±0.09 1.64±0.12 1.30±0.07 1.30±0.03 1.80±0.07 2.37±0.160.30±0.07 1.00±0.05 1.73±0.07 1.80±0.07 1.75±0.08 1.58±0.07 0.79±0.02 0.52±0.02
0.09±0.19 0.64±0.05 1.07±0.07 1.24±0.05 1.35±0.04 1.33±0.04 0.75±0.03 0.58±0.020.13±1.02 1.82±0.10 1.14±0.13 1.23±0.08 1.44±0.05 1.46±0.04 0.78±0.04 0.56±0.04
0.64±1.77 4.84±0.10 1.43±0.12 1.20±0.08 1.42±0.05 1.49±0.04 1.10±0.06 0.80±0.094.97±0.06 1.41±0.12 1.34±0.08 1.35±0.05 1.48±0.04 1.47±0.08 1.47±0.13
0.02±22.35 4.27±0.06 1.28±0.29 1.35±0.13 1.10±0.05 1.48±0.04 1.74±0.08 1.41±0.153.63±0.06 1.26±0.22 1.20±0.23 1.02±0.06 1.42±0.05 1.53±0.07 1.17±0.21
1.80±1.04 2.75±0.06 1.17±0.13 1.17±0.10 0.83±0.07 1.18±0.05 1.36±0.07 1.13±0.220.46±1.09 1.96±0.08 1.03±0.13 0.98±0.10 0.74±0.06 0.97±0.06 1.08±0.12 1.80±0.56
1.86±0.17 1.05±0.17 0.88±0.12 0.71±0.08 1.05±0.06 0.81±0.10 1.06±1.180.84±0.39 1.01±0.20 0.80±0.10 0.67±0.06 0.90±0.05 0.75±0.07 1.19±0.68
0.65±0.28 0.67±0.11 1.08±0.08 0.59±0.08 2.21±1.21
pi ratio table for cut "kaonID > 0.75"
0
5
10
15
20
25
30
35
```
(d) Fake π+ ratio table for cut kaonID > 0.75.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.71±1.13 1.05±1.97 0.30±2.31 0.54±1.75 0.23±2.04 0.27±2.81 0.52±3.531.64±0.03 1.50±0.05 1.06±0.16 1.25±0.11 1.21±0.11 1.26±0.19 1.48±0.38 2.32±0.77
1.12±0.01 1.07±0.01 0.99±0.06 1.04±0.04 1.14±0.04 1.09±0.05 1.32±0.07 1.51±0.131.05±0.00 1.02±0.01 1.04±0.05 1.10±0.03 1.17±0.03 1.15±0.04 1.23±0.05 1.41±0.13
1.01±0.00 0.99±0.01 1.00±0.04 1.11±0.02 1.23±0.02 1.22±0.03 1.32±0.04 1.32±0.141.00±0.00 0.96±0.01 1.10±0.04 1.18±0.02 1.25±0.01 1.16±0.02 1.29±0.04 1.45±0.10
1.00±0.00 0.95±0.01 1.13±0.04 1.17±0.02 1.14±0.01 1.20±0.02 1.33±0.03 1.34±0.141.00±0.01 0.92±0.01 1.28±0.03 1.17±0.02 1.13±0.01 1.13±0.01 1.35±0.03 1.56±0.13
1.01±0.01 0.92±0.01 1.38±0.03 1.12±0.02 1.10±0.01 1.12±0.01 1.37±0.03 1.11±0.131.01±0.01 0.92±0.02 1.34±0.03 1.15±0.01 1.08±0.01 1.11±0.01 1.32±0.03 1.43±0.14
1.03±0.03 0.87±0.03 1.41±0.04 1.14±0.02 1.07±0.01 1.10±0.02 1.36±0.04 0.86±0.211.01±0.13 0.88±0.04 1.30±0.04 1.12±0.02 1.03±0.01 1.10±0.02 1.45±0.02 1.13±0.10
0.49±0.78 1.14±0.13 0.99±0.03 1.02±0.02 1.12±0.02 1.51±0.03 1.26±0.05
K ratio table for cut "pionID > 0.05"
0.0
0.5
1.0
1.5
2.0
```
(e) Fake K− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
1.09±1.04 1.26±1.92 0.99±1.77 0.49±1.64 0.73±2.23 0.45±4.42 4.39±1.731.60±0.03 1.49±0.04 1.05±0.16 1.17±0.11 1.27±0.13 1.29±0.20 1.51±0.44 2.63±0.52
1.07±0.01 1.08±0.01 1.03±0.06 1.05±0.04 1.11±0.04 1.21±0.06 1.31±0.10 1.66±0.151.04±0.00 1.04±0.01 1.07±0.05 1.13±0.04 1.17±0.03 1.20±0.04 1.24±0.06 1.46±0.12
1.01±0.00 1.00±0.01 1.02±0.04 1.16±0.03 1.27±0.02 1.24±0.03 1.47±0.05 1.26±0.121.00±0.00 0.96±0.01 1.11±0.03 1.15±0.02 1.18±0.01 1.23±0.02 1.28±0.04 1.28±0.11
0.99±0.01 0.93±0.01 1.16±0.03 1.13±0.02 1.15±0.01 1.23±0.02 1.46±0.03 1.24±0.140.99±0.01 0.91±0.01 1.28±0.03 1.14±0.02 1.12±0.01 1.16±0.01 1.38±0.03 1.27±0.14
1.00±0.01 0.90±0.01 1.31±0.03 1.11±0.02 1.04±0.01 1.11±0.01 1.48±0.03 1.32±0.121.00±0.02 0.87±0.02 1.31±0.03 1.11±0.02 1.03±0.01 1.12±0.01 1.59±0.02 1.53±0.12
1.04±0.05 0.85±0.04 1.35±0.04 1.11±0.02 1.02±0.01 1.14±0.02 1.54±0.03 1.38±0.140.94±0.21 0.83±0.05 1.37±0.04 1.10±0.02 1.03±0.01 1.15±0.01 1.54±0.02 1.35±0.07
0.77±2.14 3.03±5.13 1.46±0.13 1.03±0.04 1.07±0.02 1.21±0.02 1.52±0.03 1.19±0.05
K ratio table for cut "pionID > 0.05"
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
```
(f) Fake K+ ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.00 1.00±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.00 0.92±0.001.01±0.00 1.04±0.00 0.97±0.00 0.99±0.00 1.00±0.00 1.00±0.00 0.99±0.00 1.00±0.00
1.01±0.00 1.02±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.00±0.00 1.02±0.00 1.03±0.001.01±0.00 1.00±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.99±0.00 1.01±0.00 1.05±0.01
1.01±0.00 0.99±0.00 0.99±0.00 0.99±0.00 0.99±0.00 0.99±0.00 1.00±0.00 1.03±0.011.01±0.00 0.96±0.00 0.99±0.00 0.98±0.00 0.99±0.00 0.97±0.00 1.00±0.00 1.07±0.01
1.00±0.01 0.92±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.97±0.00 1.00±0.00 1.04±0.011.00±0.01 0.91±0.01 0.98±0.01 0.99±0.01 0.99±0.00 0.97±0.00 1.00±0.00 1.06±0.01
1.02±0.01 0.90±0.01 0.98±0.01 0.98±0.01 0.99±0.01 0.97±0.01 1.01±0.01 1.05±0.011.05±0.02 0.90±0.01 1.00±0.01 0.99±0.01 0.99±0.00 0.97±0.01 1.02±0.01 1.06±0.02
0.98±0.08 0.83±0.04 1.01±0.01 1.01±0.01 1.00±0.01 0.97±0.01 1.02±0.01 1.07±0.020.57±0.49 0.86±0.10 0.99±0.02 1.00±0.01 1.00±0.01 0.98±0.01 1.04±0.01 1.06±0.02
0.50±4.88 0.93±0.44 1.01±0.03 1.03±0.01 0.98±0.01 1.08±0.01 1.09±0.02
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
```
(g) π− ratio table for cut pionID > 0.05.
```
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.98±0.00 1.00±0.00 0.98±0.00 0.97±0.00 0.99±0.00 0.97±0.00 0.94±0.00 0.93±0.001.02±0.00 1.04±0.00 0.98±0.00 0.99±0.00 1.00±0.00 0.99±0.00 1.00±0.00 1.00±0.00
1.01±0.00 1.03±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.99±0.00 1.02±0.00 1.05±0.001.01±0.00 1.01±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 1.00±0.00 1.06±0.00
1.01±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.00 1.00±0.00 1.05±0.011.00±0.01 0.96±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00 1.06±0.01
0.99±0.01 0.92±0.01 0.98±0.01 0.98±0.00 0.99±0.00 0.97±0.00 0.99±0.00 1.04±0.010.99±0.01 0.90±0.01 0.98±0.01 0.98±0.01 0.99±0.00 0.97±0.00 1.01±0.00 1.05±0.01
1.00±0.02 0.89±0.01 0.99±0.01 0.99±0.01 0.99±0.01 0.97±0.01 1.01±0.01 1.06±0.011.10±0.05 0.92±0.02 0.99±0.01 0.99±0.01 1.00±0.00 0.98±0.01 1.02±0.01 1.05±0.02
1.28±0.24 0.89±0.04 0.99±0.01 0.99±0.01 1.00±0.01 0.99±0.01 1.03±0.01 1.06±0.020.45±0.83 0.74±0.17 0.95±0.03 1.00±0.01 1.00±0.01 0.99±0.01 1.05±0.01 1.06±0.02
0.11±18.87 1.03±0.03 1.00±0.01 0.99±0.01 1.07±0.01 1.06±0.02
pi ratio table for cut "pionID > 0.05"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(h) π+ ratio table for cut pionID > 0.05.
```
Figure 73: PID tables for run-dependent samples, generated with cuts: nPXDHits >
0 and pt > 0.1 and E < 5.5. These corrections are applied to B0 → K∗0ν ¯ν channel.
121
F nPXDHits> 0 tables1313
Fig. 74, Fig. 75 and Fig. 76 show the PXD hits selection efficiency and fake-rate corrections1314
for kaons and pions applied to different channels. Muon and electron fake rates are also1315
implemented but not shown here.1316
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.93±0.05 0.91±0.02 0.94±0.01 0.94±0.01 0.92±0.01 0.90±0.02 0.81±0.04 0.69±0.130.95±0.01 0.96±0.00 0.96±0.00 0.97±0.00 0.97±0.00 0.96±0.00 0.92±0.01 0.87±0.02
0.97±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.90±0.011.02±0.01 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.93±0.01
0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.96±0.010.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.96±0.01
0.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.000.99±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.99±0.01 0.97±0.00 0.97±0.00 0.96±0.00 0.98±0.00 0.98±0.00 0.98±0.000.96±0.02 0.98±0.01 0.96±0.01 0.97±0.01 0.98±0.01 0.98±0.00 0.98±0.00
1.00±0.02 0.98±0.01 0.99±0.01 0.97±0.01 0.98±0.00 0.98±0.00 0.98±0.000.87±0.15 1.02±0.01 0.95±0.02 0.96±0.01 0.97±0.01 0.98±0.00 0.98±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(a) Positive-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.82±0.06 0.90±0.02 0.93±0.01 0.90±0.01 0.90±0.01 0.89±0.02 0.82±0.04 0.65±0.160.95±0.01 0.96±0.00 0.96±0.00 0.96±0.00 0.98±0.00 0.95±0.00 0.91±0.01 0.89±0.02
0.96±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.90±0.010.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.96±0.010.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.97±0.01
0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.000.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.97±0.00
0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.001.00±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.98±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.96±0.02 0.97±0.01 0.97±0.01 0.97±0.01 0.99±0.01 0.98±0.00 0.99±0.00
1.00±0.02 0.98±0.01 0.98±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.000.99±0.02 0.98±0.01 0.96±0.01 0.99±0.01 0.98±0.00 0.97±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(b) Negative-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
1.18±0.54 1.15±0.09 0.83±0.12 1.83±0.67 0.57±0.610.93±0.03 0.98±0.04 0.98±0.06 1.01±0.08 0.91±0.04 0.93±0.05 1.12±2.27
1.05±0.02 0.94±0.03 0.96±0.02 0.95±0.02 0.96±0.02 0.99±0.02 0.97±0.02 0.95±0.031.00±0.00 0.94±0.03 1.02±0.02 0.98±0.02 0.98±0.01 1.01±0.02 0.97±0.01 0.94±0.02
1.01±0.03 0.97±0.03 0.97±0.02 0.97±0.02 0.98±0.02 0.98±0.01 0.94±0.021.00±0.02 0.98±0.02 0.95±0.02 0.97±0.01 1.03±0.02 0.97±0.02 0.92±0.05
0.99±0.01 0.95±0.03 0.99±0.02 0.97±0.01 0.97±0.02 0.98±0.01 1.01±0.031.01±0.01 0.94±0.03 0.99±0.02 1.02±0.01 1.00±0.02 1.01±0.01 0.95±0.04
1.00±0.01 0.92±0.03 0.97±0.03 0.98±0.02 0.97±0.02 0.99±0.01 0.95±0.071.00±0.01 0.93±0.03 1.01±0.03 0.95±0.02 1.01±0.02 0.97±0.02 0.98±0.05
1.00±0.02 1.02±0.04 0.93±0.03 1.00±0.02 0.95±0.02 0.97±0.02 1.07±0.061.04±0.04 0.93±0.05 0.96±0.04 0.92±0.04 0.99±0.03 0.95±0.02 1.06±0.24
1.00±0.06 0.93±0.07 1.00±0.04 0.95±0.02 0.99±0.02 0.99±0.01 0.88±0.111.00±0.00 1.06±0.04 1.01±0.04 1.03±0.04 0.98±0.02 2.30±14.38
pi ratio table for cut "nPXDHits > 0"
0.0
0.5
1.0
1.5
2.0
```
(c) Positive-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.89±0.07 0.90±0.09 1.13±0.41 0.22±2.43 0.21±3.770.99±0.03 0.93±0.04 0.97±0.05 0.89±0.08 0.96±0.04 0.92±0.06 1.02±1.06
1.05±0.02 1.01±0.02 0.96±0.02 0.97±0.01 0.96±0.02 1.01±0.02 0.98±0.01 0.97±0.030.98±0.03 0.99±0.02 0.96±0.02 0.97±0.01 0.98±0.02 0.98±0.01 0.94±0.02
0.97±0.03 0.94±0.03 0.93±0.02 0.99±0.01 1.01±0.02 0.99±0.01 0.97±0.020.97±0.03 0.94±0.03 0.99±0.02 0.99±0.01 0.98±0.02 0.98±0.01 0.98±0.03
1.00±0.02 0.95±0.02 0.95±0.02 1.00±0.01 0.99±0.01 1.00±0.01 0.97±0.021.01±0.01 0.97±0.03 0.96±0.02 0.98±0.01 0.98±0.02 0.97±0.01 1.02±0.04
0.98±0.01 0.94±0.03 0.96±0.03 0.98±0.02 1.00±0.01 1.00±0.01 0.99±0.021.01±0.02 0.98±0.03 0.97±0.03 0.98±0.02 0.97±0.02 1.00±0.01 1.00±0.04
1.05±0.02 0.94±0.03 0.99±0.04 0.96±0.02 0.99±0.02 0.97±0.01 0.98±0.060.96±0.04 0.97±0.04 1.02±0.04 1.00±0.03 0.98±0.02 1.01±0.02 6.03±14.76
1.04±0.11 0.95±0.06 0.96±0.05 0.98±0.02 0.97±0.02 0.98±0.01 0.97±0.051.50±0.96 0.86±0.11 1.00±0.04 0.93±0.04 1.00±0.01 1.11±0.12
pi ratio table for cut "nPXDHits > 0"
0
1
2
3
4
5
6
```
(d) Negative-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K+νν preselections applied.
Figure 74: PXD tables for run-dependent samples, generated with cuts: kaonID >
0.9 and pt > 0.1 and |dz| < 0.3 and dr < 0.05 and nCDCHits > 10. These
corrections are applied to B+ → K+νν channel.
122
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.88±0.04 0.91±0.02 0.94±0.01 0.94±0.01 0.92±0.01 0.90±0.02 0.80±0.04 0.71±0.110.94±0.01 0.96±0.00 0.96±0.00 0.97±0.00 0.97±0.00 0.96±0.00 0.92±0.01 0.88±0.02
0.96±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.90±0.011.02±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.96±0.010.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.97±0.01
0.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.000.99±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.99±0.01 0.97±0.00 0.97±0.00 0.96±0.00 0.98±0.00 0.98±0.00 0.98±0.000.96±0.02 0.98±0.01 0.96±0.01 0.97±0.01 0.98±0.01 0.98±0.00 0.98±0.00
1.00±0.02 0.98±0.01 0.98±0.01 0.97±0.01 0.98±0.00 0.98±0.00 0.98±0.000.87±0.15 1.02±0.01 0.95±0.02 0.96±0.01 0.97±0.01 0.98±0.00 0.98±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(a) Positive-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.85±0.05 0.89±0.02 0.93±0.01 0.90±0.01 0.92±0.01 0.88±0.02 0.80±0.04 0.71±0.120.94±0.01 0.96±0.00 0.96±0.00 0.96±0.00 0.98±0.00 0.95±0.00 0.91±0.01 0.87±0.02
0.96±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.89±0.010.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.96±0.010.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.97±0.01
0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.000.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.97±0.00
-0.00±nan 0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.001.00±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.98±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.96±0.02 0.97±0.01 0.97±0.01 0.97±0.01 0.99±0.01 0.98±0.00 0.98±0.00
1.00±0.02 0.98±0.01 0.98±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.000.99±0.02 0.98±0.01 0.96±0.01 0.99±0.01 0.98±0.00 0.97±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(b) Negative-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.40±2.76 1.10±0.64 1.14±0.09 0.85±0.10 1.75±0.56 0.62±0.531.48±0.44 0.94±0.03 0.98±0.03 0.98±0.05 1.02±0.07 0.92±0.04 0.93±0.05 2.38±5.06
1.10±0.06 0.94±0.03 0.96±0.02 0.96±0.02 0.96±0.02 0.99±0.02 0.97±0.02 0.95±0.031.00±0.00 0.94±0.03 1.01±0.02 0.98±0.02 0.98±0.01 1.01±0.02 0.97±0.01 0.94±0.02
1.01±0.03 0.97±0.03 0.97±0.02 0.97±0.02 0.98±0.02 0.98±0.01 0.94±0.021.00±0.02 0.98±0.02 0.95±0.02 0.97±0.01 1.03±0.02 0.97±0.02 0.92±0.05
0.99±0.01 0.95±0.02 0.99±0.02 0.97±0.01 0.97±0.02 0.98±0.01 1.03±0.031.01±0.01 0.94±0.03 0.99±0.02 1.02±0.01 1.00±0.02 1.00±0.01 0.96±0.03
1.00±0.01 0.91±0.03 0.97±0.03 0.98±0.02 0.97±0.02 0.99±0.01 0.95±0.061.00±0.01 0.93±0.03 1.01±0.03 0.95±0.02 1.01±0.02 0.98±0.02 1.00±0.05
1.00±0.02 1.02±0.04 0.93±0.03 1.01±0.02 0.95±0.02 0.97±0.02 1.09±0.061.04±0.04 0.93±0.05 0.96±0.04 0.92±0.04 0.99±0.03 0.95±0.02 1.07±0.25
1.00±0.06 0.93±0.07 1.00±0.04 0.95±0.02 0.99±0.02 0.99±0.01 0.80±0.121.00±0.00 1.00±0.00 1.07±0.04 1.01±0.04 1.03±0.04 0.98±0.02 1.66±1.20
pi ratio table for cut "nPXDHits > 0"
0.0
0.5
1.0
1.5
2.0
```
(c) Positive-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.18±6.31 0.66±2.06 0.90±0.07 0.93±0.08 1.08±0.40 0.58±0.60 2.71±5.17 0.20±2.790.03±21.78 0.98±0.03 0.92±0.03 0.97±0.04 0.92±0.07 0.95±0.04 0.90±0.06 0.55±0.87
1.12±0.08 1.01±0.02 0.96±0.01 0.97±0.01 0.96±0.02 1.01±0.02 0.98±0.01 0.95±0.030.98±0.03 0.99±0.02 0.96±0.02 0.97±0.01 0.98±0.02 0.98±0.01 0.93±0.02
0.97±0.03 0.94±0.02 0.93±0.02 0.99±0.01 1.01±0.02 0.99±0.01 0.98±0.020.97±0.03 0.94±0.03 0.99±0.02 0.99±0.01 0.98±0.02 0.98±0.01 1.00±0.03
1.00±0.02 0.95±0.02 0.95±0.02 1.00±0.01 0.99±0.01 0.99±0.01 0.94±0.031.01±0.01 0.97±0.03 0.96±0.02 0.98±0.01 0.98±0.02 0.98±0.01 1.01±0.04
0.98±0.01 0.94±0.03 0.96±0.03 0.98±0.02 1.00±0.01 1.00±0.01 1.04±0.041.01±0.02 0.98±0.03 0.97±0.03 0.98±0.02 0.97±0.02 1.00±0.01 1.02±0.04
1.05±0.02 0.94±0.03 0.98±0.04 0.96±0.02 0.99±0.02 0.97±0.01 0.96±0.060.96±0.04 0.97±0.04 1.02±0.04 1.00±0.03 0.98±0.02 1.01±0.02
1.04±0.11 0.95±0.06 0.97±0.05 0.98±0.02 0.97±0.02 0.98±0.01 0.99±0.061.50±0.96 0.86±0.11 1.00±0.04 0.92±0.04 1.00±0.01 1.12±0.13
pi ratio table for cut "nPXDHits > 0"
0.0
0.5
1.0
1.5
2.0
2.5
```
(d) Negative-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.90±0.02 0.94±0.01 0.96±0.01 0.95±0.01 0.97±0.01 0.94±0.01 0.85±0.03 0.90±0.080.96±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.97±0.00 0.95±0.01 0.86±0.01
0.97±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.91±0.010.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.96±0.000.99±0.00 0.98±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.97±0.00
0.99±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.000.99±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.00
0.99±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.000.98±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.00
1.00±0.02 0.99±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.95±0.05 0.99±0.02 0.97±0.01 0.97±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.61±0.48 0.97±0.03 0.98±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.001.06±0.29 0.96±0.01 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.00
pi ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(e) Positive-charge pion efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.91±0.02 0.92±0.01 0.95±0.01 0.95±0.01 0.97±0.01 0.96±0.01 0.85±0.03 0.70±0.110.95±0.01 0.97±0.00 0.96±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.93±0.01 0.87±0.02
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.92±0.010.98±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.95±0.01
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.96±0.000.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.97±0.00
0.98±0.00 0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.98±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00
0.98±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.001.00±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00
0.99±0.02 0.97±0.01 0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.001.06±0.09 0.97±0.02 0.97±0.01 0.97±0.01 0.97±0.00 0.98±0.01 0.98±0.00 0.98±0.01
0.29±2.06 1.01±0.04 0.97±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.00-0.00±nan 3.32±2.00 0.99±0.09 0.99±0.01 0.97±0.01 0.98±0.01 0.98±0.00 0.98±0.00
pi ratio table for cut "nPXDHits > 0"
0.0
0.5
1.0
1.5
2.0
2.5
3.0
```
(f) Negative-charge pion efficiency ratio table
```
for the selection nPXDHits > 0 with B+ →
K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.84±0.71 2.82±2.52 1.19±6.20 0.23±3.83 2.27±1.49 0.64±0.50 0.26±1.441.26±0.31 0.99±0.16 1.14±0.18 4.62±6.61 0.67±0.49 1.61±0.71 3.32±3.18 0.09±1.62
0.97±0.01 0.98±0.01 0.95±0.02 0.99±0.01 0.98±0.01 0.99±0.02 0.95±0.04 0.93±0.080.98±0.00 0.98±0.00 0.97±0.01 0.97±0.01 0.98±0.01 0.99±0.01 0.97±0.01 0.95±0.03
0.98±0.00 0.98±0.00 0.94±0.01 0.98±0.01 0.98±0.01 0.99±0.01 0.98±0.01 0.94±0.020.98±0.00 0.97±0.00 0.98±0.01 1.00±0.01 1.00±0.00 0.98±0.01 0.99±0.01 0.94±0.02
0.98±0.00 0.98±0.00 0.97±0.01 0.97±0.00 0.98±0.00 0.99±0.01 0.98±0.01 0.98±0.020.98±0.01 0.98±0.00 0.96±0.01 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.01 1.00±0.02
0.98±0.01 0.99±0.00 0.97±0.01 0.97±0.00 0.98±0.00 0.97±0.00 0.97±0.01 0.95±0.030.97±0.01 0.99±0.00 0.96±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.01 1.00±0.03
0.99±0.01 0.98±0.01 0.97±0.01 0.97±0.01 0.98±0.00 0.99±0.01 0.98±0.01 0.95±0.020.98±0.02 1.00±0.01 0.97±0.01 0.98±0.01 0.99±0.00 0.97±0.01 0.99±0.01 1.01±0.03
1.01±0.05 0.99±0.02 0.99±0.01 0.97±0.01 0.98±0.00 0.97±0.01 0.98±0.01 1.00±0.020.14±86.11 2.87±3.39 1.03±0.02 0.95±0.01 0.98±0.01 0.98±0.01 0.98±0.01 0.98±0.01
K ratio table for cut "nPXDHits > 0"
0
1
2
3
4
```
(g) Positive-charge kaon-as-pion fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K∗+νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.57±1.53 1.17±1.42 1.09±3.08 1.25±0.80 0.93±0.69 1.30±0.630.76±0.34 1.22±0.42 0.75±0.39 1.11±0.57 0.77±0.92 1.16±1.99
0.97±0.01 0.98±0.01 0.96±0.01 0.99±0.01 0.99±0.01 1.00±0.02 1.00±0.05 0.92±0.090.98±0.00 0.98±0.00 0.97±0.01 0.97±0.01 0.98±0.01 0.98±0.01 0.98±0.01 0.92±0.03
0.98±0.00 0.98±0.00 0.97±0.01 0.98±0.01 0.99±0.00 0.99±0.01 0.97±0.01 0.96±0.030.98±0.00 0.97±0.00 0.96±0.01 0.96±0.01 0.97±0.00 0.97±0.01 0.98±0.01 0.94±0.02
0.98±0.00 0.98±0.00 0.96±0.01 0.97±0.00 0.99±0.00 0.97±0.01 0.97±0.01 0.99±0.020.99±0.00 0.98±0.00 0.97±0.01 0.96±0.00 0.99±0.00 0.98±0.01 0.97±0.01 1.00±0.02
0.98±0.01 0.98±0.00 0.97±0.01 0.97±0.00 0.98±0.00 0.98±0.01 0.98±0.01 0.98±0.020.99±0.01 0.98±0.00 0.97±0.01 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.01 0.99±0.03
0.99±0.01 0.97±0.01 0.96±0.01 0.97±0.00 0.99±0.00 0.99±0.01 0.97±0.01 0.96±0.020.94±0.02 0.98±0.01 0.97±0.01 0.96±0.01 0.98±0.00 0.99±0.01 0.98±0.01 0.89±0.05
0.96±0.06 1.00±0.02 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.01 0.98±0.01 0.98±0.020.97±5.36 2.14±0.70 0.96±0.03 0.96±0.01 0.97±0.01 0.97±0.01 0.98±0.01 0.97±0.01
K ratio table for cut "nPXDHits > 0"
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
```
(h) Negative-charge kaon-as-pion fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B+ → K∗+νν preselections applied.
Figure 75: PXD tables for run-dependent samples, generated with cuts: pt >
0.1 and |dz| < 0.3 and dr < 0.05 and and nCDCHits > 20 and kaonID > 0.9 or
pionID > 0.05. These corrections are applied to B+ → K∗+ν ¯ν channel.
123
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.89±0.04 0.92±0.02 0.94±0.01 0.94±0.02 0.93±0.01 0.90±0.02 0.84±0.04 0.79±0.090.95±0.01 0.96±0.00 0.96±0.00 0.97±0.00 0.97±0.00 0.96±0.00 0.92±0.01 0.90±0.02
0.97±0.01 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.91±0.010.97±0.03 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.96±0.010.74±0.29 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.97±0.00
1.05±0.05 0.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.001.01±0.08 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.99±0.09 0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.97±0.001.02±0.02 0.99±0.01 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.92±0.10 0.99±0.01 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.001.04±0.05 0.97±0.02 0.98±0.01 0.97±0.01 0.97±0.01 0.98±0.01 0.98±0.00 0.98±0.00
0.95±1.35 1.01±0.02 0.98±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.87±0.15 1.02±0.01 0.95±0.01 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(a) Positive-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B0 →
K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.89±0.04 0.90±0.02 0.93±0.01 0.91±0.02 0.93±0.01 0.90±0.02 0.85±0.04 0.84±0.090.94±0.01 0.96±0.00 0.96±0.00 0.96±0.00 0.98±0.00 0.95±0.00 0.92±0.01 0.91±0.02
0.97±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.92±0.011.01±0.02 0.99±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.96±0.010.34±0.93 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.97±0.00 0.97±0.01
-0.00±nan 0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.000.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.97±0.00
0.07±1.57 0.99±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.98±0.00-0.00±nan 1.00±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00
0.98±0.01 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.96±0.02 0.97±0.01 0.97±0.01 0.98±0.01 0.99±0.00 0.98±0.00 0.99±0.00
1.00±0.02 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.99±0.02 0.98±0.01 0.96±0.01 0.99±0.01 0.98±0.00 0.98±0.00
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
```
(b) Negative-charge kaon efficiency ratio table
```
for the selection nPXDHits > 0 with B0 →
K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
1.22±0.49 1.84±0.69 1.11±0.09 0.92±0.11 1.45±0.32 0.43±0.93 0.30±4.600.93±0.15 0.93±0.03 0.98±0.03 0.94±0.04 1.07±0.06 0.91±0.04 0.93±0.05 1.08±0.24
1.01±0.02 0.93±0.02 0.95±0.01 0.96±0.01 0.97±0.01 0.98±0.02 0.96±0.02 0.94±0.030.96±0.07 0.99±0.01 0.99±0.02 0.97±0.01 0.98±0.01 1.01±0.02 0.97±0.01 0.95±0.02
0.97±0.03 1.00±0.03 0.96±0.02 0.96±0.02 0.97±0.01 0.98±0.02 0.98±0.01 0.95±0.021.33±0.22 1.00±0.02 0.99±0.02 0.95±0.02 0.98±0.01 1.02±0.01 0.97±0.01 0.98±0.02
1.01±0.57 0.99±0.01 0.96±0.02 0.98±0.01 0.98±0.01 0.99±0.01 0.98±0.01 1.03±0.030.97±0.07 1.00±0.01 0.95±0.02 0.97±0.02 1.01±0.01 1.00±0.01 0.99±0.01 0.96±0.03
1.00±0.00 0.99±0.01 0.93±0.03 0.95±0.02 0.98±0.01 0.99±0.01 0.98±0.01 0.99±0.050.97±0.04 0.99±0.01 0.95±0.03 1.00±0.02 0.96±0.02 1.01±0.01 0.97±0.01 1.00±0.05
0.44±0.79 1.00±0.02 1.01±0.03 0.97±0.02 0.99±0.02 0.95±0.02 0.98±0.02 1.07±0.051.02±0.04 0.96±0.04 0.97±0.03 0.97±0.02 1.00±0.02 0.95±0.02 1.16±0.24
0.99±0.07 0.96±0.06 0.97±0.03 0.96±0.02 1.00±0.02 1.00±0.01 0.86±0.081.00±0.00 1.00±0.00 0.98±0.05 1.00±0.03 1.00±0.03 0.97±0.02 1.23±0.23
pi ratio table for cut "nPXDHits > 0"
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
(c) Positive-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B0 → K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
3.55±35.23 4.12±21.35 0.88±0.07 0.96±0.09 1.09±0.40 0.81±0.76 2.45±1.370.62±0.47 0.98±0.03 0.93±0.03 0.95±0.04 0.94±0.06 0.94±0.04 0.85±0.06 0.80±0.30
1.01±0.02 0.98±0.01 0.97±0.01 0.98±0.01 0.97±0.01 0.99±0.02 0.97±0.01 0.95±0.031.00±0.03 0.99±0.01 0.98±0.02 0.97±0.01 0.97±0.01 0.97±0.01 0.98±0.01 0.93±0.02
0.97±0.03 0.94±0.02 0.94±0.02 0.99±0.01 1.01±0.02 0.98±0.01 0.97±0.020.96±0.02 0.95±0.02 0.97±0.01 0.98±0.01 0.98±0.01 0.97±0.01 1.03±0.02
0.99±0.01 0.95±0.02 0.95±0.02 0.99±0.01 0.99±0.01 0.99±0.01 0.95±0.031.01±0.01 0.97±0.03 0.95±0.02 0.99±0.01 0.98±0.01 0.98±0.01 0.99±0.04
0.99±0.01 0.94±0.02 0.94±0.02 0.97±0.01 0.99±0.01 0.99±0.01 0.97±0.041.01±0.02 0.98±0.02 0.96±0.02 0.99±0.01 0.98±0.01 1.00±0.01 1.00±0.03
1.04±0.02 0.94±0.03 0.95±0.03 0.97±0.01 0.99±0.01 0.98±0.01 0.98±0.050.96±0.04 0.98±0.03 1.03±0.03 0.98±0.02 0.98±0.02 1.00±0.02 1.46±0.54
1.01±0.10 0.98±0.05 0.99±0.03 0.97±0.02 0.99±0.01 0.99±0.01 1.00±0.071.66±1.31 0.98±0.05 1.00±0.03 0.94±0.03 0.98±0.01 1.03±0.09
pi ratio table for cut "nPXDHits > 0"
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
```
(d) Negative-charge pion-as-kaon fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B0 → K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.92±0.04 0.94±0.01 0.97±0.01 0.95±0.01 0.97±0.01 0.95±0.01 0.85±0.03 0.89±0.140.96±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.97±0.00 0.95±0.01 0.88±0.02
0.97±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.91±0.010.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.94±0.01
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.96±0.000.98±0.00 0.98±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.97±0.00
0.99±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.000.99±0.02 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.00
1.00±0.03 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.97±0.000.97±0.03 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.00
1.14±0.07 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.001.26±0.26 1.00±0.02 0.97±0.01 0.97±0.01 0.97±0.00 0.98±0.01 0.98±0.00 0.98±0.01
0.96±0.04 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.33±1.41 0.96±0.02 0.97±0.01 0.98±0.01 0.98±0.00 0.98±0.01
pi ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(e) Positive-charge pion efficiency ratio table
```
for the selection nPXDHits > 0 with B0 →
K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.93±0.03 0.93±0.01 0.95±0.01 0.96±0.01 0.97±0.01 0.96±0.01 0.86±0.04 0.83±0.230.95±0.01 0.97±0.00 0.96±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.93±0.01 0.90±0.02
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.96±0.00 0.93±0.010.98±0.00 0.97±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.97±0.00 0.95±0.01
0.98±0.00 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.96±0.000.98±0.00 0.98±0.00 0.98±0.00 0.97±0.00 0.99±0.00 0.98±0.00 0.98±0.00 0.96±0.00
0.98±0.01 0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.000.99±0.01 0.98±0.00 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00
0.98±0.02 0.98±0.00 0.97±0.00 0.97±0.00 0.98±0.00 0.99±0.00 0.98±0.00 0.98±0.000.95±0.03 0.98±0.01 0.97±0.00 0.97±0.00 0.99±0.00 0.99±0.00 0.98±0.00 0.98±0.00
1.07±0.08 0.97±0.01 0.98±0.00 0.97±0.00 0.98±0.00 0.98±0.00 0.98±0.00 0.98±0.001.07±0.36 0.96±0.02 0.97±0.01 0.97±0.01 0.97±0.00 0.98±0.01 0.98±0.00 0.98±0.01
0.81±1.10 1.03±0.06 0.96±0.01 0.98±0.01 0.98±0.00 0.98±0.00 0.98±0.00 0.99±0.001.27±0.36 0.99±0.02 0.97±0.01 0.98±0.01 0.98±0.00 0.99±0.00
pi ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(f) Negative-charge pion efficiency ratio table
```
for the selection nPXDHits > 0 with B0 →
K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
0.85±1.72 0.29±1.86 1.40±0.34 0.64±1.20 1.33±0.41 0.71±0.771.28±0.32 1.01±0.13 1.04±0.12 1.29±0.41 0.78±0.24 0.10±40.27 0.40±1.36 0.34±0.57
0.97±0.01 0.98±0.01 0.96±0.01 0.99±0.01 0.98±0.01 1.00±0.02 0.97±0.03 0.92±0.070.98±0.00 0.98±0.00 0.97±0.01 0.98±0.01 0.98±0.01 0.99±0.01 0.97±0.01 0.96±0.03
0.98±0.00 0.98±0.00 0.95±0.01 0.98±0.01 0.98±0.01 0.99±0.01 0.98±0.01 0.94±0.020.98±0.00 0.97±0.00 0.99±0.01 1.00±0.01 1.00±0.00 0.98±0.01 0.99±0.01 0.94±0.02
0.98±0.01 0.98±0.00 0.97±0.01 0.96±0.01 0.98±0.00 0.98±0.01 0.98±0.01 0.99±0.020.98±0.01 0.98±0.00 0.96±0.01 0.97±0.01 0.98±0.00 0.99±0.00 0.98±0.01 1.00±0.02
0.98±0.01 0.99±0.00 0.97±0.01 0.97±0.01 0.98±0.00 0.97±0.00 0.97±0.01 0.95±0.030.98±0.01 0.99±0.00 0.96±0.01 0.97±0.01 0.98±0.00 0.98±0.00 0.98±0.01 1.01±0.03
1.01±0.02 0.98±0.01 0.97±0.01 0.97±0.01 0.98±0.00 0.99±0.01 0.98±0.01 0.97±0.030.96±0.04 1.00±0.01 0.97±0.01 0.97±0.01 0.99±0.00 0.97±0.01 0.99±0.01 1.04±0.04
0.99±0.14 0.98±0.02 0.99±0.01 0.97±0.01 0.99±0.00 0.97±0.01 0.98±0.01 1.00±0.020.82±3.89 1.32±4.51 1.06±0.04 0.95±0.02 0.98±0.01 0.98±0.01 0.98±0.01 0.98±0.01
K ratio table for cut "nPXDHits > 0"
0.0
0.2
0.4
0.6
0.8
1.0
1.2
```
(g) Positive-charge kaon-as-pion fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B0 → K∗0νν preselections applied.
-0.866 -0.682 -0.4226 -0.1045 0.225 0.5 0.766 0.8829 0.9563cosTheta bins
0.10.3
0.60.9
1.21.5
1.82.1
2.42.7
3.03.3
3.54.0
4.5
p bins
6.86±6.03 0.96±2.23 0.97±0.42 0.50±0.90 0.97±0.30 1.33±0.44 0.32±0.980.94±0.20 1.08±0.22 0.47±0.73 0.89±0.16 0.97±0.37 0.99±0.55 1.30±0.95
0.98±0.01 0.99±0.01 0.96±0.01 0.99±0.01 0.99±0.01 1.00±0.02 0.99±0.04 0.96±0.080.98±0.00 0.98±0.00 0.97±0.01 0.97±0.01 0.98±0.01 0.98±0.01 0.98±0.01 0.92±0.03
0.98±0.00 0.98±0.00 0.97±0.01 0.98±0.01 0.99±0.00 0.99±0.01 0.97±0.01 0.96±0.030.98±0.00 0.97±0.00 0.96±0.01 0.96±0.01 0.97±0.00 0.97±0.01 0.98±0.01 0.95±0.02
0.98±0.00 0.98±0.00 0.96±0.01 0.97±0.00 0.99±0.00 0.97±0.01 0.97±0.01 0.98±0.020.99±0.01 0.98±0.00 0.97±0.01 0.96±0.00 0.99±0.00 0.98±0.01 0.97±0.01 1.00±0.02
0.98±0.01 0.98±0.00 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.01 0.98±0.01 0.99±0.020.99±0.01 0.98±0.00 0.97±0.01 0.97±0.01 0.98±0.00 0.99±0.00 0.97±0.01 0.99±0.03
0.98±0.01 0.97±0.01 0.96±0.01 0.97±0.01 0.99±0.00 0.99±0.01 0.97±0.01 0.97±0.020.96±0.03 0.98±0.01 0.97±0.01 0.96±0.01 0.98±0.00 0.99±0.01 0.98±0.01 0.89±0.05
1.03±0.23 0.99±0.02 0.97±0.01 0.97±0.01 0.98±0.00 0.98±0.01 0.98±0.01 0.97±0.020.64±0.76 1.01±0.06 0.96±0.01 0.97±0.01 0.97±0.01 0.97±0.01 0.97±0.01
K ratio table for cut "nPXDHits > 0"
0
1
2
3
4
5
6
```
(h) Negative-charge kaon-as-pion fake rate ra-
```
tio table for the selection nPXDHits > 0 with
B0 → K∗0νν preselections applied.
Figure 76: PXD tables for run-dependent samples, generated with cuts: pt >
0.1 and |dz| < 0.3 and dr < 0.05 and and kaonID > 0.75 or pionID > 0.05.
These corrections are applied to B0 → K∗0ν ¯ν channel.
124
G π0 Reconstruction Efficiency Correction Tables1317
Figure 77 represent the π0 reconstruction efficiency correction for standard list neutral1318
pions with eff50 May2020 photon list.1319
1 2 3
p [GeV]
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
```
cos(
```
```
)
```
0 reconstruction efficiency corrections
0.0
0.2
0.4
0.6
0.8
data MC ratio
Figure 77: π0 reconstruction efficiency correction for standard list neutral pions with
eff50 May2020 photon list.
125
H B → K∗K0S K0S control channels1320
H.1 B0 → K∗0K0S K0S1321
The selection on basic objects is similar to those that is used for B → Kν ¯ν. We select1322
tracks that are reconstructed within the CDC acceptance. All tracks in the event apart1323
from those coming from K0S decays are required to have impact parameters dr < 0.51324
cm and |dz| < 3 cm. We require all tracks to have transverse momentum exceeding1325
0.01 GeV/c and all neutral clusters to have energy exceeding 0.01 GeV. The kaon and1326
pion candidates coming from K∗0 decays must have at least one hit in PXD. To enhance1327
sample in K∗0 candidates, we require kaon candidate coming from K∗0 to have global1328
kaonID more than 0.9. To reconstruct K0S candidates, we combine two charged tracks in1329
a vertex fit. We require an invariant mass of a K0S candidate to be within 0.485 and 0.511330
GeV/c2 window and the cosine of angle between its momentum and decay vertex vertex1331
to exceed 0.98. To reconstruct K∗0 candidates, we combine kaon and pion candidates1332
in a vertex fit and require their invariant mass to be within 0.8 and 1 GeV/c2 range.1333
The B0 candidates are obtained by combining K∗0 and two K0S candidates. To further1334
suppress continuum background, we restrict sample to Mbc > 5.27 GeV/c2, |∆E| < 0.151335
GeV, normalized Fox-Wolfram moment R2 < 0.4, and cosine of angle between thrust axis1336
```
of the signal B and thrust axis of ROE (cosTBTO) < 0.95. Figure 78 shows several1337
```
distributions obtained from the generic simulation.1338
The signal is extracted from a fit of the ∆E distribution. We model the signal and1339
background by using a Gaussian and second-order Chebyshev polynomial function, re-1340
spectively. All shape parameters are left floating. The ∆E distribution overlaid with the1341
fit projection shown at the left plot of Fig. 79. The determined signal yield is 265±49.1342
We do not calculate the branching fraction.1343
We use the sPlot technique to access the signal-only distributions. To determine1344
```
the signal composition, we look at the M (K0S K0S ) distribution, which is calculated as1345
```
```
M (K0S K0S ) =
```
p
M 2B − 2MB EK∗0 + M 2K∗0 , where MB is a nominal B0-meson mass, EK∗0 is1346
a reconstructed energy of the K∗0 candidate, and MK∗0 is a reconstructed invariant mass1347
```
of K∗0 candidate. The background-subtracted M (K0S K0S ) distributions obtained in data1348
```
and generic simulation are shown in the right plot of Fig. 79. In simulation, we observe1349
a distinguished peak around 1.5 GeV/c2 which corresponds to the f ′2 and f2 mesons. In1350
data, no distinguished peaks are observed.1351
```
Finally, we compare the background-subtracted M (K0S K0S ) distribution obtained in1352
```
data with those obtained in the simulation with removed B → K∗0f ′2 and B → K∗0f21353
decays. As shown in Fig. 80, the data-simulation agreement is satisfactory. Hence, we1354
remove the resonant components of B0 → K∗0K0S K0S , as B0 → K∗0f ′2, from the generic1355
simulation.1356
H.2 B+ → K∗+K0S K0S1357
We apply same selection on the basic objects as for the B0 → K∗0K0S K0S sample. In addi-1358
tion, we reconstruct π0 candidates by using standard eff50 selection. To reconstruct K∗+1359
candidates, we combine charged kaon and neutral pion candidates and K0S and charged1360
126
0
50
100
150
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
5.270 5.275 5.280 5.285 5.290
Mbc [GeV/c2]
0.5
1.0
1.5
DataPred.
0
50
100
150
200
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0.15 0.10 0.05 0.00 0.05 0.10 0.15
E [GeV]
0.5
1.0
1.5
DataPred.
0
100
200
300
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0.0 0.2 0.4 0.6 0.8 1.0
cosTBTO
0.5
1.0
1.5
DataPred.
0
25
50
75
100
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0.80 0.85 0.90 0.95 1.00
B_sig_Kstar0_M
0.5
1.0
1.5
DataPred.
```
Figure 78: Distributions of (top left) Mbc, (top right) ∆E, (bottom left) cosTBTO,
```
```
(bottom right) M (K+π−) obtained for B0 → K∗0K0S K0S candidates reconstructed in data
```
and generic simulation corresponding to 400 fb−1 of integrated luminosity. Black points
with errors are data, filled histograms are simulation. The simulation sample is normalized
to data luminosity.
0.15 0.10 0.05 0.00 0.05 0.10 0.150
20
40
60
80
100
120
deltaE
total
background
signal
Data
1.0 1.5 2.0 2.5 3.0 3.5 4.0
MK0SK0S [GeV/c2]
0
20
40
60
Entries
MC
```
Belle II data (sPlot)
```
```
Figure 79: Distribution of (left) ∆E obtained for B0 → K∗0K0S K0S candidates re-
```
```
constructed in data with fit projections overlaid and (right) M (K0S K0S ) obtained for
```
B0 → K∗0K0S K0S candidates in background-subtracted data and generic simulation by
using sPlot technique. The simulation sample is normalized to data luminosity.
127
1.0 1.5 2.0 2.5 3.0 3.5 4.0
MK0SK0S [GeV/c2]
0
10
20
30
40
Entries
```
Belle II data (sPlot)
```
```
Belle II mc (sPlot)
```
```
Figure 80: Distribution of M (K0S K0S ) obtained for B0 → K∗0K0S K0S candidates in
```
background-subtracted data and generic simulation with removed B → K∗0f ′2 and
B → K∗0f2 decays. The simulation sample is normalized to data luminosity. The blue
and orange points with errors correspond to data and simulation, respectively.
pion candidates, separately, in a vertex fit and require their invariant mass to be within1361
the 0.8 and 1 GeV/c2 range. The B+ candidates are obtained by combining K∗+ and1362
two K0S candidates. To suppress the continuum background, we restrict the sample to1363
Mbc > 5.27 GeV/c2 and |∆E| < 0.15 GeV.1364
To further suppress the continuum background, we train a boosted-decision tree. We1365
generate one million B+ → K∗+K0S K0S by using the phase-space model, apply the se-1366
lection mentioned in the previous paragraph and use the obtained sample as signal. As1367
background, we use the generic simulated run-independent sample without excluding the1368
B+ → K∗+K0S K0S candidates. The choice of hyper-parameters for the BDT is optimized1369
using optuna package. The most discriminating features are the angle between two pho-1370
tons coming from the neutral pions, normalized Fox-Wolfram moment R2 and cosTBTO.1371
After training and applying the classifier on the data and generic simulated samples, we1372
select candidates with the BDT output exceeding 0.92. Figure 81 shows several distribu-1373
tions obtained from the generic simulation.1374
The signal is extracted from a fit of the ∆E distribution. We model the signal and1375
background by using a Gaussian and second-order Chebyshev polynomial function, re-1376
spectively. All shape parameters are left floating. The ∆E distribution overlaid with the1377
fit projection shown at the left plot of Fig. 82. The determined signal yield is 55±33. We1378
do not observe a significant signal.1379
```
However, we use the sPlot technique to produce signal-only M (K0S K0S ) distribution in1380
```
```
data and generic simulation (Fig. 82). In simulation, we see a peak from the B+ → K∗+f ′21381
```
and B+ → K∗+f2 decays. The events corresponding to this decay are removed from the1382
generic simulation.1383
128
0
20
40
60
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
5.270 5.275 5.280 5.285 5.290
Mbc [GeV/c2]
0.5
1.0
1.5
DataPred.
0
20
40
60
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0.15 0.10 0.05 0.00 0.05 0.10 0.15
E [GeV]
0.5
1.0
1.5
DataPred.
0
50
100
150
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0 1 2 3 4
```
E(K*0) [GeV]
```
0.5
1.0
1.5
DataPred.
0
10
20
30
40
50
Entries
ccbarssbar
ddbaruubar
mixedcharged
Model stat. unc.Data
0.80 0.85 0.90 0.95 1.00
B_sig_Kstar_M
0.5
1.0
1.5
DataPred.
```
Figure 81: Distributions of (top left) Mbc, (top right) ∆E, (bottom left) energy of
```
```
K∗+ candidate, (bottom right) M (Kπ) obtained for B+ → K∗+K0S K0S candidates recon-
```
structed in data and generic simulation corresponding to 400 fb−1 of integrated luminosity.
Black points with errors are data, filled histograms are simulation. The simulation sample
is normalized to data luminosity.
0.15 0.10 0.05 0.00 0.05 0.10 0.150
10
20
30
40
deltaE
total
background
signal
Data
1.0 1.5 2.0 2.5 3.0 3.5 4.0
MK0SK0S [GeV/c2]
10
0
10
20
30
40
Entries
MC
```
Belle II data (sPlot)
```
```
Figure 82: Distribution of (left) ∆E obtained for B+ → K∗+K0S K0S candidates re-
```
```
constructed in data with fit projections overlaid and (right) M (K0S K0S ) obtained for
```
B+ → K∗+K0S K0S candidates in background-subtracted data and generic simulation by
using the sPlot technique. The simulation sample is normalized to data luminosity.
129
I Leading branching fractions of B-decays1384
A dedicated study is conducted to investigate the contribution of leading B meson back-1385
ground decays in the signal region of all four channels. We assign weights as corrections1386
to the central values of the branching fractions to correct their values during generation1387
to those in the pdg. Finally, we assign a dedicated systematic due to the uncertainty on1388
```
the branching fraction of these decays. We consider following 56 (62) charged (mixed) B1389
```
meson decays and their uncertainty, shown in Fig. 83. The highest branching fractions1390
belong to semileptonic B-decays involving D, followed by hadronic B decays involving1391
D, leptonic B decays, with the smallest branching fractions belonging to the charmless1392
hadronic decays. The fractional uncertainty is higher backgrounds that are not semilep-1393
tonic B-decays involving D.1394
0.00 0.01 0.02 0.03 0.04 0.05 0.06Decay BR Fraction with Uncertainty
```
B± D0 ± ± ±B± D*(2010)± 0 ± ±B
```
```
± D*(2007)0 ± ± ± 0B± K*(892)±K0SB± K*(892)±K0
```
B± K0K0 ±B± K0K±B
```
± K0K±B± (1020)K±B± ppK±
```
```
B± K± (1020)B± (1020)K±B
```
```
± K0L ±B± K0 ±B± K±K*(892)±K±
```
```
B± K*0(1430)0 ±B± K*(892)±B
```
```
± ±B± D*(2007)0K±K0B± D*(2007)0K±K*(892)0
```
B± D0K±B± D0K±K0B
```
± D*(2007)0K±B± K*(892)±D0B± D*(2007)0K*(892)±
```
```
B± D*(2007)0K*(892)±B± J/ (1S)K±B
```
```
± c(1S)K±B± c(1S)K*(892)±B± J/ (1S)K*(892)±
```
```
B± D0 (782) ±B± D0 ±B
```
```
± D0 ±B± D*(2007)0 ±B± D*(2007)0 ±
```
```
B± D*(2007)0D±sB± D* +s D0B
```
```
± D0 ±B± D0D±sB± (770)±D0
```
```
B± (770)±D0B± D*(2007)0 (770)±B
```
```
± a1(1260)±D0B± D* +s D*(2007)0B± D*(2007)0a1(1260)±
```
```
B± D*(2007)0 ±B± D0e± eB
```
± D0 ±B± D0 ±B± D0e± e
```
B± D0e± eB± D*(2007)0 ±B
```
```
± D*(2007)0e± eB± D*(2007)0e± eB± D*(2007)0 ±
```
```
B± D*(2007)0e± e
```
Decay Mode
nan%nan%nan%
136.00%136.00%96.00%
12.97%12.97%15.65%
9.14%7.03%7.03%
2.62%1.98%20.71%
13.72%5.55%22.09%
100.00%11.43%4.04%
9.20%7.11%8.37%
16.77%16.77%5.27%
6.43%42.35%7.56%
22.49%2.15%2.15%
2.91%2.91%13.72%
20.46%32.55%6.46%
11.01%11.01%17.83%
57.30%13.87%29.17%
10.80%3.10%3.10%
3.10%3.10%3.10%
1.90%1.90%1.90%
1.90%1.90%
Leading B-backgrounds: charged
0.00 0.01 0.02 0.03 0.04 0.05 0.06Decay BR Fraction with Uncertainty
```
B0 D*(2010)± ± ± ± 0B0 D± ± ± ±B0 D*(2010)± ± 0
```
```
B0 K*(892)0K0SB0 K*(892)0K0B0 K
```
0SK0SB0 K0K0B0 K±K±K0
B0 K0 0B0 K0S 0B0 D±s K±
```
B0 K*(892)0B0 D0K0SB
```
```
0 D0K0B0 D*(2010)±K±K0B0 ±e± e
```
B0 D±K±K0B0 D±K±K0B0 D±K±
```
B0 D±K±B0 D*(2010)±K±B0 (770)± ±
```
```
B0 D*(2010)±K*(892)±B0 K*(892)±D±B0 K*(892)±D±
```
```
B0 D±K±K*(892)0B0 D±K0 ±B0 c(1S)K*(892)0
```
```
B0 J/ (1S)K0B0 J/ (1S)K0LB0 J/ (1S)K
```
```
0SB0 c(1S)K0B0 c(1S)K0S
```
```
B0 c(1S)K0LB0 J/ (1S)K*(892)0B0 D± ±
```
```
B0 D± ±B0 D± ±B0 D*(2010)± ±
```
```
B0 D*(2010)±D*(2010)±K*(892)0B0 (770)±D*(2010)±B0 D*(2010)±D*(2010)±K0
```
```
B0 D* +s D±B0 (770)±D±B0 (770)±D±
```
```
B0 D±D±sB0 D*(2010)±D±sB0 D± ±
```
```
B0 a1(1260)±D±B0 D*(2010)±a1(1260)±B0 D*(2010)± ±
```
```
B0 D* +s D*(2010)±B0 D±e± eB0 D±e± e
```
B0 D± ±B0 D± ±B0 D±e± e
```
B0 D*(2010)± ±B0 D*(2010)± ±B0 D*(2010)±e± e
```
```
B0 D*(2010)±e± eB0 D*(2010)±e± e
```
Decay Mode
nan%nan%nan%
137.50%137.50%13.27%
13.27%36.17%3.81%
3.81%17.15%5.93%
7.99%7.99%100.00%
3.33%15.85%100.00%
3.97%3.97%3.67%
7.18%18.63%16.08%
16.08%7.81%18.00%
16.99%5.44%5.44%
5.44%11.73%11.73%
11.73%6.20%3.11%
3.11%3.11%2.72%
100.00%13.43%10.14%
21.51%16.42%16.42%
7.04%9.82%21.44%
35.66%21.36%6.34%
8.00%3.33%3.33%
3.33%3.33%3.33%
1.85%1.85%1.85%
1.85%1.85%
Leading B-backgrounds: mixed
```
Figure 83: Branching fractions of the leading charged B meson decays (left) and mixed
```
```
B meson decays (right) along with their absolute (bar) and fractional uncertainties (per-
```
```
centage).
```
I.1 Corrections to the central values of branching fractions1395
In this section, we list the correction weights for all the leading B decay backgrounds.1396
The correction is defined in Eq. 6. We classify the leading B decays into 4 categories:1397
B to semileptonic decay in Tab. 41, 2-body decay in Tab. 42, B to D hadronic decay in1398
Tab. 43, B to charmless decay in Tab. 44.1399
wBFcorr ± σw =
BPDG
BRel6
±
σBPDG
BRel6
```
. (6)1400
```
130
Here, BPDG and σBPDG denote the latest B meson decay branching fraction and its cor-1401
responding uncertainty from PDG Live. BRel6 refers to the branching fraction defined in1402
```
the BELLE2 DECAY.dec file from Release-6 (EvtGen and Pythia).1403
```
For the modes highlighted in red, we use the modified non-resonant branching fraction1404
```
(Bmod) to calculate the weight. This modified branching fraction refers to the inclusive1405
```
```
branching fraction (PDG live) with contributions from intermediate resonant decays sub-1406
```
```
tracted. For example, in the case of the decay B0 → D−K+ ¯K∗(892)0, the contribution1407
```
```
from the resonant decay B0 → D−a+1 (→ K+ ¯K∗(892)0) must be excluded.1408
```
The modes highlighted in green are related to Pythia and we keep relative 100% for1409
their weights uncertainties.1410
The modes highlighted in blue are related to studies of hadronic FEI decay modes.1411
Since the branching fractions in the decay file were updated in release-8, but we are using1412
the outdated release-6 and the PDG live values have large uncertainties. In this case, the1413
values of Bmod used to calculate the correction weights for these modes are taken from1414
the modified branching fractions in release-8 which have been validated by FEI validation1415
study. [BELLE2-NOTE-PH-2022-002][BELLE2-NOTE-PH-2022-046]1416
For B → J/ψK decays, we assign an additional 5% uncertainty to the correction1417
weights to account for the potential contribution from the J/ψ → n¯n background, which1418
closely mimics the behavior of the signal channel.1419
Table 41: Summary of B meson semileptonic and leptonic decays with branching fractions
```
from EvtGen (BELLE2 DECAY.dec, Release-6) and PDG Live.
```
Decay Mode BEvtGen BPDG/Bmod wBFcorr σwwBFcorr
B → Dℓν
```
B0 → D∗−ℓ+νℓ 0.0511 (4.87 ± 0.09) × 10−2 0.953 ± 0.0176 0.0185
```
```
B+ → ¯D∗0µ+νµ 0.0549 (5.26 ± 0.10) × 10−2 0.958 ± 0.0182 0.0190
```
```
B+ → ¯D0ℓ+νℓ 0.0231 (2.26 ± 0.07) × 10−2 0.978 ± 0.0303 0.0310
```
```
B0 → D−ℓ+νℓ 0.0214 (2.10 ± 0.07) × 10−2 0.981 ± 0.0327 0.0333
```
b → uℓν
```
B0 → ρ−ℓ+νℓ 0.000294 (2.94 ± 0.21) × 10−4 1.000 ± 0.0718 0.0720
```
```
B0 → π−ℓ+νℓ 0.000145 (1.50 ± 0.05) × 10−4 1.034 ± 0.0333 0.0333
```
With τ leptons
```
B+ → τ +ντ 0.000109 (1.09 ± 0.24) × 10−4 1.003 ± 0.2209 0.2210
```
```
B+ → ¯D0τ +ντ 0.006907 (7.7 ± 2.5) × 10−3 1.115 ± 0.3255 0.3255
```
```
B0 → D∗−τ +ντ 0.013184 (1.48 ± 0.09) × 10−2 1.125 ± 0.0634 0.0634
```
```
B0 → D−τ +ντ 0.006399 (9.8 ± 2.1) × 10−3 1.539 ± 0.2144 0.2144
```
131
Table 42: Two-body decay modes: comparison between EvtGen branching ratios and
PDG values, including ratio and relative error.
Decay Mode BEvtGen BPDG/Bmod wBFcorr σwwBFcorr
DK
```
B+ → ¯D0K+ 0.00036255 (3.64 ± 0.15)×10−4 1.0036 ± 0.0406 0.0404
```
```
B+ → ¯D0K∗+ 0.00053194 (5.3 ± 0.4)×10−4 1.0000 ± 0.0837 0.0837
```
```
B+ → ¯D∗(2007)0K+ 0.00039744 (4.19+0.31−0.28)×10−4 1.0554 ± 0.0750 0.0711
```
```
B+ → ¯D∗(2007)0K∗+ 0.00081240 (8.1 ± 1.4)×10−4 1.0000 ± 0.1677 0.1677
```
```
B0 → D−K+ 0.00018595 (2.05 ± 0.08)×10−4 1.1032 ± 0.0438 0.0397
```
```
B0 → D−K∗+ 0.00044578 (4.5 ± 0.7)×10−4 1.0000 ± 0.1608 0.1608
```
```
B0 → D∗(2010)−K+ 0.00021213 (2.16 ± 0.08)×10−4 1.0200 ± 0.0374 0.0367
```
```
B0 → D∗(2010)−K∗+ 0.00032971 (3.3 ± 0.6)×10−4 1.0000 ± 0.1863 0.1863
```
```
B0 → ¯D0K0 0.00005231 (5.5 ± 0.4)×10−5 1.0514 ± 0.0840 0.0799
```
```
B0 → D−s K+ 0.00002748 (2.7 ± 0.5)×10−5 0.9973 ± 0.1711 0.1715
```
c¯cK
```
B+ → J/ψ(1S)K+ 0.00100556 (1.020 ± 0.019)×10−3 1.0142 ± 0.0543 0.0535
```
```
B0 → J/ψ(1S)K0 0.00043650 (8.91 ± 0.21)×10−4 1.0202 ± 0.0566 0.0555
```
```
B+ → J/ψ(1S)K∗+ 0.001429920 (1.43 ± 0.08)×10−3 1.0000 ± 0.0756 0.0756
```
```
B0 → J/ψ(1S)K∗0 0.001270001 (1.27 ± 0.05)×10−3 0.9962 ± 0.0616 0.0618
```
```
B+ → ηcK+ 0.00106262 (1.10 ± 0.07)×10−3 1.0397 ± 0.0668 0.0643
```
```
B0 → ηcK0L 0.00079513 (9.0 ± 1.1)×10−4 1.1347 ± 0.1332 0.1173
```
```
B0 → ηcK0 0.00079513 (9.0 ± 1.1)×10−4 1.1347 ± 0.1332 0.1173
```
DDs
```
B+ → ¯D0D+s 0.00900977 (9.3 ± 0.6)×10−3 1.0322 ± 0.0663 0.0646
```
```
B+ → ¯D0D∗+s 0.00760000 (7.6 ± 1.6)×10−3 1.0023 ± 0.2051 0.2046
```
```
B+ → ¯D∗(2007)0D+s 0.00821845 (7.0 ± 1.0)×10−3 0.8566 ± 0.1175 0.1372
```
```
B+ → ¯D∗(2007)0D∗+s 0.01710000 (1.71 ± 0.24)×10−2 0.9978 ± 0.1383 0.1387
```
```
B0 → D−D+s 0.00723697 (8.1 ± 0.6)×10−3 1.1243 ± 0.0791 0.0704
```
```
B0 → D−D∗+s 0.00740000 (7.4 ± 1.6)×10−3 0.9971 ± 0.2145 0.2151
```
```
B0 → D∗(2010)−D+s 0.00804457 (8.2 ± 0.8)×10−3 1.0150 ± 0.0997 0.0982
```
132
Table 43: B to hadronic D decay modes: comparison between EvtGen branching ratios
and PDG values, including ratio and relative error. Color representation: FEI modes
```
(modified according to rel-08), generated by Pythia, non-resonant BF from PDG.
```
Decay Mode BEvtGen/Pythia BPDG/Bmod wBFcorr ± σw σwwBFcorr
B → Dπ
```
B+ → ¯D0π+ 0.00467517 (4.61 ± 0.10)×10−3 0.9868 ± 0.0212 0.0215
```
```
B+ → ¯D∗(2007)0π+ 0.00490086 (5.17 ± 0.15)×10−3 1.0554 ± 0.0307 0.0291
```
```
B0 → D−π+ 0.00252113 (2.51 ± 0.08)×10−3 0.9940 ± 0.0309 0.0311
```
```
B0 → D∗(2010)−π+ 0.00274268 (2.66 ± 0.07)×10−3 0.9695 ± 0.0264 0.0272
```
B → Dππ0
```
B+ → ¯D0ρ+ 0.0134483 (9.7 ± 1.1)×10−3 0.7229 ± 0.0795 0.1101
```
```
B+ → ¯D∗(2007)0ρ+ 0.00981176 (9.8 ± 1.7)×10−3 1.0000 ± 0.1783 0.1783
```
```
B0 → D−ρ+ 0.00757464 (7.6 ± 1.2)×10−3 1.0001 ± 0.1642 0.1642
```
```
B0 → D∗(2010)−ρ+ 0.00679879 (6.8 ± 0.9)×10−3 1.0000 ± 0.1343 0.1343
```
```
B0 → D∗(2010)−π+π0 0.00835892 0 0 ± 0 -
```
B → Dπππ
```
B+ → ¯D∗(2007)0 a1(1260)+ 0.0188000 (1.9 ± 0.5)×10−2 1.0000 ± 0.2792 0.2792
```
```
B0 → D∗(2010)− a1(1260)+ 0.0129942 (1.30 ± 0.27)×10−2 1.0000 ± 0.2104 0.2104
```
```
B+ → ¯D0 a1(1260)+ 0.00000131 (1.0 ± 0.57)×10−2 2.2222 ± 1.273 0.5426
```
```
B0 → D− a1(1260)+ 0.0060000 (1.07 ± 0.38)×10−2 1.7857 ± 0.637 0.3566
```
B+ → ¯D0 π+π+π− 0.0051000 0 0 ± 0 -
```
B+ → ¯D0 ω π+ 0.0041000 (4.1 ± 0.9)×10−3 1.0000 ± 0.2249 0.2249
```
```
B → Dππ(π)π0
```
```
B+ → D∗(2010)−π+π+π0 0.01515771 0 0 ± 0 -
```
```
B+ → D∗(2007)0π−π+π+π0 0.01800000 0 0 ± 0 -
```
B → DKK
```
B+ → ¯D0K+ ¯K0 0.0005500 (3.73 ± 0.34)×10−4 0.6789 ± 0.0624 0.0920
```
```
B+ → ¯D∗(2007)0K+ ¯K0 0.0007100 (2.9 ± 0.6)×10−4 0.2070 ± 0.2070 1.0000
```
```
B0 → D−K+ ¯K0 0.0009300 (1.64 ± 0.26)×10−4 0.0882 ± 0.0882 1.0000
```
```
B0 → D∗(2010)−K+ ¯K0 0.0008510 (1.8 ± 0.4)×10−4 0.1069 ± 0.1069 1.0000
```
```
B+ → ¯D∗(2007)0K+ ¯K∗(892)0 0.0015000 (0.28± 0.03)×10−3 0.1830 ± 0.0209 0.1143
```
```
B0 → D−K+ ¯K∗(892)0 0.0008800 (4.74 ± 0.37) × 10−4 0.5386 ± 0.0420 0.0781
```
B → DDK
```
B0 → D∗−D∗+K0 0.0081092 (7.30 ± 0.74)×10−3 0.9002 ± 0.0913 0.1014
```
133
Table 44: B to charmless decay modes: comparison between EvtGen branching ratios
and PDG values, including ratio and relative error. Color representation: non-resonant
BF from PDG.
Decay Mode BEvtGen/Pythia BPDG/Bmod wBFcorr ± σw σwwBFcorr
B → KX
```
B+ → K+ϕ 8.83×10−6 (8.8+0.7−0.6)×10−6 0.9998 ± 0.0703 0.0703
```
```
B+ → ϕK+γ 2.71×10−6 (2.7 ± 0.4)×10−6 0.9983 ± 0.1563 0.1565
```
```
B+ → K∗0 (1430)0π+ 3.91×10−5 (3.9+0.6−0.5)×10−5 0.99997 ± 0.1372 0.1372
```
B → KK
```
B+ → K+ ¯K0 1.31×10−6 (1.32 ± 0.17)×10−6 1.0041 ± 0.1303 0.1297
```
```
B0 → K0 ¯K0 1.69×10−6 (1.21 ± 0.16)×10−6 0.7160 ± 0.0950 0.1327
```
B → KKK
```
B0 → K0K+K− 3.3×10−5 (0.48 ± 0.17)×10−6 0.1456 ± 0.0529 0.3631
```
```
B+ → K∗+K+K− 2.6×10−5 (2.60 ± 0.54)×10−6 1.000 ± 0.2071 0.2071
```
others
```
B+ → p¯pK+ 5.92×10−6 (5.9 ± 0.5)×10−6 1.0004 ± 0.0914 0.0914
```
```
B+ → K0π+ 2.37×10−5 (2.39 ± 0.06)×10−5 1.0088 ± 0.0264 0.0262
```
134
I.2 Coverage1420
The abundance of these 118 decays in the signal region has been studied across all four1421
```
channels: B+ → K+ν ¯ν, B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν decays. The1422
```
coverage of these 118 decays, together with D∗∗, discussed in Appendix J and fake K∗,1423
prevented in Appendix M, is as follows: 80.6% for B+ → K+ν ¯ν, 90.9% for B0 → K0S ν ¯ν,1424
89.8% for B0 → K∗0ν ¯ν, and 88.2% for B+ → K∗+ν ¯ν5. More detailed fractional abun-1425
dances of the top 15 leading branching fractions contributing to the charged B back-1426
grounds are summarized in Fig. 87. The main contributors are semileptonic B decays.1427
Figure 88 shows the top 15 mixed B background modes and their corresponding fractional1428
abundances. It should be noted that for each channel not all the backgrounds are present,1429
as seen in Figure 84, which shows counts of B0 → K∗0ν ¯ν.
B0 D
±K±
B0 K
```
*(892)±D
```
±
```
B0 c(1S)K
```
0L
B0 D
```
±K±K0B0 D±e± eB0 D±K±K0B0 c(1S)K0B0 c(1S)K0S
```
B0 D
```
*(2010)±
```
```
K*(892)
```
±
B0 D
± ±B0 D0K0SB0 D0K0B0 D±K±
B0 D
±e± e
B0 D
```
*(2010)±
```
D±s
B0 D
±D±s
B0 D
```
*(2010)±
```
±
B0 J/
```
(1S)K
```
```
*(892)0B0 ±e± e
```
```
B0 (770)
```
±D±
```
B0 (770)
```
```
±D*(2010)
```
±
B0 D
```
±K±K*(892)
```
0
B0 D
± ±
B0 D
```
*(2010)±
```
±
```
B0 a1(1260)
```
±D±
```
B0 (770)
```
±D±
B0 D
± ±B0 D± ±
B0 K
```
*(892)±D
```
±
B0 D
```
*(2010)±
```
K±
B0 D
± ±
B0 D
±e± eB0 D± ±
B0 D
- +s D±
B0 D
- +s D*(2010)
±
B0 K
±K±K0
B0 D
```
*(2010)±
```
± 0
B0 D
```
*(2010)±
```
±
B0 D
```
*(2010)±
```
```
D*(2010)
```
±K0
B0 D
```
*(2010)±
```
```
a1(1260)
```
±
B0 D
```
*(2010)±
```
e± e
```
B0 (770)
```
± ±
B0 D
```
*(2010)±
```
e± e
B0 J/
```
(1S)K
```
0L
B0 J/
```
(1S)K
```
0
B0 J/
```
(1S)K
```
0S
B0 D
±s K±
B0 D
```
*(2010)±
```
K±K0
B0 D
```
*(2010)±
```
e± e
B0 D
```
*(2010)±
```
±
B0 D
```
*(2010)±
```
```
D*(2010)
```
```
±K*(892)
```
0
B0 K
```
*(892)0
```
```
B0 c(1S)K
```
```
*(892)0B0 K0K0B0 K0SK0S
```
B0 K
```
*(892)0K
```
0S
B0 K
```
*(892)0K
```
0
B0 K
0 0
B0 K
0S 0
B0 D
±K0 ±
B0 D
```
*(2010)±
```
± ± ±
0
B0 D
± ± ± ±
B± D
0 ± ± ±
```
B± (1020)K
```
±
B± D
0K±K0
B± D
```
*(2007)0
```
±
B± D
0e± eB± D0 ±
```
B± (1020)K
```
±
B± D
```
*(2007)0K
```
```
*(892)±
```
B± D
```
*(2007)0a
```
```
1(1260)
```
±
B± D
```
*(2007)0D
```
±s
B± D
0e± e
B± K
```
*0(1430)0
```
±
B± J/
```
(1S)K
```
±
B± J/
```
(1S)K
```
```
*(892)±
```
B± D
```
0 (782)
```
±
B± a1
```
(1260)±
```
D0
B± ppK
±
B± D
```
*(2007)0
```
±
B± K
0K±
B± D
```
*(2007)0
```
±
B± D
```
*(2007)0K
```
```
±K*(892)
```
0
B± D
```
*(2010)±
```
0 ± ±
B± K
```
*(892)±D
```
0
B± D
0K±
B± D
0 ±
```
B± (770)
```
±D0B± D0D±s
B± D
```
*(2007)0e
```
± e
B± D
- +s D*(2007)
0
B± D
```
*(2007)0e
```
± e
B± c
```
(1S)K±
```
B± c
```
(1S)K*(892)
```
±
B± K
```
*(892)±
```
B± D
```
*(2007)0K
```
```
*(892)±B± K0L ±B± D0 ±
```
B± D
```
*(2007)0K
```
±
B± K
```
± (1020)
```
```
B± (770)
```
±D0
B± K
0K±
B± D
- +s D0
B± D
```
*(2007)0
```
±
B± D
```
*(2007)0K
```
±K0
B± D
0 ±
B± D
0e± e
B± K
```
±K*(892)
```
±K±
B± D
```
*(2007)0
```
±B± ±
B± D
```
*(2007)0
```
± ± ±
0
B± D
```
*(2007)0
```
```
(770)±
```
B± D
```
*(2007)0e
```
± e
B± D
0 ±B± K0 ±
B± K
0K0 ±
B± K
```
*(892)±K
```
0
B± K
```
*(892)±K
```
0S
Identifier
0
2000
4000
6000
8000
Number of Events19 156272 7195776 277 40 61
3036
0 135157597693109519575019589420316228
7769
106072959
6088
11 66 7
4032
6973511863 01320514777
5220
28
2767
190 0 55 13 52803
3056
283 12 310 0 0 0 10 0 0 102 0 0 0 1 318
3879
6459772 10991620
5189
4 1501321606751 306 31177112 0 175 76 367 441090
5605
1078799158138 3 170 0
2681
88 27180695
8483
81
8023
2403
14 52 112 0582
2751
65 2 0 0 0
Counts of Events with Weight Corrections by IdentifierBzero2KstarZero v53
Figure 84: Individual counts of different leading B-decays in B0 → K∗0ν ¯ν. Some of the
decays are not at all present, i.e. have zero counts.
1430
The events tagged by the leading branching fraction, D∗∗ and fake K∗ categories can1431
```
be compared to the remaining untagged events in terms of η(BDT2) and q2rec distribution.1432
```
These are shown in Fig. 85 and Fig. 86. Overall, the distributions look similar. There1433
```
is an increase observed for untagged events for B0 → K∗0ν ¯ν channel for the η(BDT2)1434
```
```
distribution; we are considering increasing coverage of the leading branching fractions to1435
```
improve this.1436
5For the B0 → K0S ν ¯ν and B0 → K∗0ν ¯ν channels, for the more important mixed background, it is
not possible to separate tag and signal side due to B0B0 mixing. Therefore, for the leading B branching
fractions, we consider both signal and tag side when estimating the coverage. For the charged mode,
and for the D∗∗ decays, we always consider signal side only. Including tag side increases coverage for the
neutral modes by 9% for B0 → K0S ν ¯ν and 7% for B0 → K∗0ν ¯ν.
135
0.92 0.94 0.96 0.98 1.00BDT2_Bplus2Kplus_v42_signal_inefficiency0
500
1000
1500
2000
2500
3000 tagged un tagged
0.92 0.94 0.96 0.98 1.00
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0 5 10 15B_sig_H_reconstructed_q20
200
400
600
800
1000
1200
1400 tagged un tagged
0 5 10 15
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0.92 0.94 0.96 0.98 1.00BDT2_Bzero2Kshort_v54_signal_inefficiency0
100
200
300
400
500tagged un tagged
0.92 0.94 0.96 0.98 1.00
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0 5 10 15B_sig_H_reconstructed_q20
50
100
150
200
250
tagged un tagged
0 5 10 15
0.6
0.8
1.0
1.2
1.4
utagged/tagged
```
Figure 85: Top: distributions of η(BDT2) and q2rec for events tagged as leading branching
```
fraction or D∗∗ compared to the untagged events for B+ → K+ν ¯ν and B0 → K0S ν ¯ν
channels. The distributions are normalized to a common area. Bottom: ratios of untagged
over tagged distributions.
0.97 0.98 0.99 1.00BDT2_Bplus2KstarPlus_v56_signal_inefficiency0
500
1000
1500
2000
2500
tagged un tagged
0.97 0.98 0.99 1.00
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0 5 10 15B_sig_H_reconstructed_q20
200
400
600
800
1000
1200
tagged un tagged
0 5 10 15
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0.95 0.96 0.97 0.98 0.99 1.00BDT2_Bzero2KstarZero_v53_signal_inefficiency0
250
500
750
1000
1250
1500
1750
2000 tagged un tagged
0.95 0.96 0.97 0.98 0.99 1.00
0.6
0.8
1.0
1.2
1.4
utagged/tagged
0 5 10 15B_sig_H_reconstructed_q20
200
400
600
800
1000
tagged un tagged
0 5 10 15
0.6
0.8
1.0
1.2
1.4
utagged/tagged
```
Figure 86: Top: distributions of η(BDT2) and q2rec for events tagged as leading branching
```
fraction, D∗∗ or fake K∗ compared to the untagged events for B+ → K∗+ν ¯ν and B0 →
K∗0ν ¯ν channels. The distributions are normalized to a common area. Bottom: ratios of
untagged over tagged distributions.
136
```
(a) B+ → K+νν
```
Decay Mode Percentage
B± → D0µ±νµ 8.1%
```
B± → D∗(2007)0µ±νµ 5.8%
```
B± → D0e±νe 5.8%
```
B± → D∗(2007)0e±νe 4.2%
```
B± → D0e±νeγ 2.7%
B± → D0K± 2.2%
```
B± → D∗(2007)0e±νeγ 2.0%
```
```
B± → D∗(2007)0K± 1.9%
```
B± → D0π± 1.5%
```
B± → D∗(2007)0π± 1.2%
```
```
B± → ηc(1S)K± 1.0%
```
```
B± → ρ(770)±D0 1.0%
```
B± → D0τ ±ντ 1.0%
B± → D0K±K0 0.9%
```
B± → D∗(2007)0τ ±ντ 0.9%
```
```
(b) B0 → K0S νν
```
Decay Mode Percentage
B± → D0µ±νµ 6.1%
B± → D0e±νe 3.7%
```
B± → D∗(2007)0µ±νµ 3.6%
```
```
B± → D∗(2007)0e±νe 2.4%
```
B± → D0e±νeγ 1.7%
```
B± → D∗(2007)0e±νeγ 1.1%
```
```
B± → K∗(892)±D0 0.7%
```
B± → D0µ±νµγ 0.6%
B± → D0D±s 0.6%
B± → D0e±νeγγ 0.5%
```
B± → ρ(770)±D0 0.5%
```
B± → D0τ ±ντ 0.4%
```
B± → D∗(2007)0K∗(892)± 0.4%
```
```
B± → D∗(2007)0τ ±ντ 0.4%
```
```
B± → D∗(2007)0µ±νµγ 0.4%
```
```
(c) B0 → K∗0νν
```
Decay Mode Percentage
B± → D0µ±νµ 6.5%
```
B± → D∗(2007)0µ±νµ 5.6%
```
B± → D0e±νe 4.1%
```
B± → D∗(2007)0e±νe 3.6%
```
```
B± → D∗(2007)0τ ±ντ 1.9%
```
B± → D0e±νeγ 1.9%
```
B± → D∗(2007)0e±νeγ 1.8%
```
B± → D0τ ±ντ 1.7%
B± → D0µ±νµγ 0.7%
B± → D0D±s 0.7%
```
B± → D∗(2007)0µ±νµγ 0.6%
```
B± → D0e±νeγγ 0.5%
```
B± → D∗+s D∗(2007)0 0.5%
```
```
B± → D∗(2007)0e±νeγγ 0.5%
```
```
B± → ρ(770)±D0 0.4%
```
```
(d) B+ → K∗+νν
```
Decay Mode Percentage
B± → D0µ±νµ 5.3%
```
B± → D∗(2007)0µ±νµ 5.2%
```
B± → D0e±νe 3.7%
```
B± → D∗(2007)0e±νe 3.6%
```
```
B± → D∗(2007)0τ ±ντ 2.6%
```
B± → D0τ ±ντ 2.0%
```
B± → D∗(2007)0e±νeγ 1.7%
```
B± → D0e±νeγ 1.6%
```
B± → D∗(2007)0K∗(892)± 0.9%
```
```
B± → K∗(892)±D0 0.9%
```
```
B± → D∗(2007)0µ±νµγ 0.7%
```
B± → D0D±s 0.6%
B± → D0µ±νµγ 0.6%
```
B± → D∗+s D∗(2007)0 0.6%
```
```
B± → ρ(770)±D0 0.5%
```
```
Figure 87: Top 15 charged B meson background decays with their respective fraction (per-
```
```
centage) with respect to both charged and mixed B meson backgrounds in simulation. All
```
the tagged charged B meson background decays represent 50% of B meson backgrounds
in B+ → K+ν ¯ν, 25% in B0 → K0S ν ¯ν, 34% in B0 → K∗0ν ¯ν, and 35% in B+ → K∗+ν ¯ν
decays.
137
```
(a) B+ → K+νν
```
Decay Mode Percentage
B0 → D±K± 3.0%
```
B0 → D∗(2010)±µ±νµ 2.7%
```
B0 → D±µ±νµ 2.0%
```
B0 → D∗(2010)±e±νe 1.9%
```
B0 → D±π± 1.5%
B0 → D±e±νe 1.4%
```
B0 → D∗(2010)±K± 1.1%
```
```
B0 → ρ(770)±D± 0.9%
```
```
B0 → D∗(2010)±e±νeγ 0.9%
```
B0 → D±e±νeγ 0.7%
B0 → D±D±s 0.7%
```
B0 → D∗(2010)±π± 0.7%
```
```
B0 → K∗(892)±D± 0.6%
```
B0 → D±π±γ 0.5%
```
B0 → D∗(2010)±τ ±ντ 0.4%
```
```
(b) B0 → K0S νν
```
Decay Mode Percentage
B0 → D±µ±νµ 12.7%
B0 → D±e±νe 8.2%
```
B0 → D∗(2010)±µ±νµ 4.7%
```
B0 → D±e±νeγ 4.2%
```
B0 → D∗(2010)±e±νe 3.2%
```
B0 → D±τ ±ντ 1.9%
B0 → D±µ±νµγ 1.7%
```
B0 → D∗(2010)±e±νeγ 1.5%
```
```
B0 → K∗(892)±D± 1.4%
```
B0 → D±e±νeγγ 1.2%
B0 → D±D±s 1.1%
```
B0 → ηc(1S)K0 0.9%
```
```
B0 → ρ(770)±D± 0.8%
```
```
B0 → D∗(2010)±µ±νµγ 0.7%
```
B0 → D0K0 0.7%
```
(c) B0 → K∗0νν
```
Decay Mode Percentage
```
B0 → D∗(2010)±µ±νµ 4.6%
```
B0 → D±µ±νµ 4.0%
```
B0 → D∗(2010)±e±νe 3.1%
```
B0 → D±e±νe 2.7%
B0 → D±τ ±ντ 1.7%
```
B0 → D∗(2010)±τ ±ντ 1.6%
```
```
B0 → D∗(2010)±e±νeγ 1.6%
```
B0 → D±e±νeγ 1.3%
B0 → D±D±s 0.7%
```
B0 → D∗(2010)±µ±νµγ 0.7%
```
B0 → D±µ±νµγ 0.6%
```
B0 → a1(1260)±D± 0.6%
```
```
B0 → J/ψ(1S)K∗(892)0 0.6%
```
```
B0 → D∗(2010)±e±νeγγ 0.4%
```
B0 → D∗+s D± 0.4%
```
(d) B+ → K∗+νν
```
Decay Mode Percentage
```
B0 → D∗(2010)±µ±νµ 3.9%
```
B0 → D±µ±νµ 3.5%
B0 → D±τ ±ντ 2.5%
```
B0 → D∗(2010)±e±νe 2.5%
```
B0 → D±e±νe 2.3%
```
B0 → D∗(2010)±τ ±ντ 1.9%
```
```
B0 → K∗(892)±D± 1.7%
```
```
B0 → D∗(2010)±e±νeγ 1.3%
```
B0 → D±e±νeγ 1.2%
B0 → D±D±s 0.9%
```
B0 → D∗(2010)±µ±νµγ 0.6%
```
B0 → D±µ±νµγ 0.5%
B0 → D∗+s D± 0.5%
```
B0 → a1(1260)±D± 0.5%
```
```
B0 → D∗(2010)±K∗(892)± 0.5%
```
Figure 88: Top 15 mixed B meson background decays with their respective fraction
```
(percentage) with respect to both charged and mixed B meson backgrounds in simulation.
```
All the tagged mixed B meson background decays represent 24% of B meson backgrounds
in B+ → K+ν ¯ν, 49% in B0 → K0S ν ¯ν, 28% in B0 → K∗0ν ¯ν and 28% in B+ → K∗+ν ¯ν
decays.
138
I.3 Treatment of the systematical uncertainty1437
In the past, specifically in analysis of B+ → K+ν ¯ν [3], to assess the uncertainty associated1438
with the branching fractions of a specific set of 97 B meson decays, we simultaneously1439
varied the uncertainties for all these decays and performed an eigenvalue decomposition,1440
retaining the leading 10 eigenvectors as correlated shape nuisance parameters. In the1441
combined analysis presented here, the strategy was modified: instead of using a reduced1442
basis, we introduced one correlated shape nuisance parameter per branching fraction mode.1443
These were defined by up and down variations corresponding to the uncertainties on the1444
respective branching fractions. This approach allows for more straightforward sharing of1445
this source of uncertainty across different signal channels, albeit at the expense of a higher1446
number of nuisance parameters. Additionally, it offers the advantage of faster reevaluation1447
in case the branching fractions are updated with improved measurements.1448
Using the B+ → K+ν ¯ν ITA from [3], it was verified that the inclusion of these1449
additional nuisance parameters has a negligible impact on the uncertainty of the fitted1450
µ when compared to the eigenvalue decomposition approach. Furthermore, the pulls of1451
the individual nuisance parameters did not exhibit significant deviations. We therefore1452
have 97 nuisance parameters in our likelihood that cover the uncertainty due to leading1453
B branching fractions.1454
139
J B → D∗∗X backgrounds studies1455
A dedicated study is performed to investigate the B±,0 backgrounds with D∗∗ produc-1456
tion, also referred as B → D∗∗X background. We use the notation D∗∗ to indicate one1457
```
of the following resonances6: D∗0 (2300)±, D∗0 (2300)0, D1(2420)±, D1(2420)0, D′1(2430)±,1458
```
```
D′1(2430)0, D∗2 (2460)±, D∗2 (2460)0, D∗s0(2317)±, Ds1(2460)±, D′s1(2536)±, D∗s2(2573)±.1459
```
These decays enter in the signal region when a K from a D decay of the charmed1460
cascade is reconstructed and the rest of the event is not reconstructed. This K may1461
```
come from signal side or from the rest-of-the-event (ROE) side, with about the same1462
```
```
probability. The shape of the q2 and η(BDT2) distributions of these backgrounds is1463
```
different from signals. Thus, they are distinguishable in the template fit. The fraction of1464
signal candidates in signal region produced by a B → D∗∗X decay is about 3% for B+1465
```
and 5% for B0 (this is strictly true for K+, for the other channels the yields are similar).1466
```
The B → D∗∗X backgrounds are composed of a large number of individual decays1467
```
(about 80 different modes, largely shared between the four signal channels). However the1468
```
```
q2 and η(BDT2) distributions for all these decays are very similar. Specific categories are1469
```
studied, grouping the decays according to the specific D∗∗, according to the candidate1470
```
coming from signal or ROE side, according on X composition (hadronic or semileptonic),1471
```
according to the number of daughters of the D∗∗. However, all the categories show similar1472
```
q2 and η(BDT2)) distributions (both 1D and 2D). On Fig. 89 some example grouping are1473
```
shown for B+ → K+ν ¯ν background. Therefore, the fit has no handle to constrain them1474
separately according to these categories.1475
We group the B → D∗∗X decays according to the knowledge of the decays, forming1476
four groups of decays. We assign a nuisance parameter to each of these groups to control1477
the branching fractions of all the B → D∗∗X decays of the specific group. The groups1478
are the following:1479
• B → D∗∗ℓν, ℓ = e, µ, τ . The branching fractions of most of these modes are known1480
and corrections are available also for central values.1481
• B → D∗∗h, h = π+, ρ+. Some measurements by Belle are available. Some new1482
measurements of these modes will likely to come in the future by Belle II.1483
```
• B → D∗∗D(∗)+s . The branching fractions of most of these modes is known via some1484
```
relative branching fractions measurement by LHCb Collaboration.1485
```
• B → D+sj D(∗). Some measurements by Belle are available.1486
```
With this grouping, if some of the branching fractions will be updated in the future1487
with new measurements, it will be easy to reinterpret the result, changing a single nuisance1488
parameter. The update will likely update multiple branching fractions in a single group.1489
The branching fractions of the MC are corrected according to the most recent mea-1490
```
surement of these decays available for the main decays (B → D∗∗eν, B → D∗∗µν,1491
```
```
B → D∗02 D+s , B → D∗+s0 D(∗)0,±). This is done with a weight on event-by-event basis.1492
```
An uncertainty is assigned to each branching fraction of the known decays, according to1493
```
6the D∗∗(2S) are not included because are missing in the decay file and Pythia is not producing them
```
in the signal regions.
140
the most updated measured uncertainty. For the unknown decays, generated by Pythia1494
a uncertainty equal to 100% of the branching fraction is assigned.1495
A correlated shape nuisance parameter is assigned for each of the categories for a total1496
of four nuisances. The nuisances are built assuming a full correlation of the branching1497
fractions within one group. This is a conservative choice made to avoid implementing1498
an unnecessarily complicated correlation matrix within the groups. Each of the nuisance1499
parameters is shared between the four signal channel, to correlate the branching fractions.1500
The impact of these nuisance parameters is shown in Fig. 38 for the Asimov fit and1501
Fig.[to be added after the fit is performed] for the fit on data. The largest contribution is1502
given by the B → D∗∗ℓν group at 0.15% level. All the other nuisance parameters induce1503
a relative uncertainty on the signal branching fractions below 10−3 level.1504
5 0 5 10 15 20 25
q2 [GeV2]
0.00
0.02
0.04
0.06
0.08
0.10
0.12
```
1NdNd (q
```
```
2) [1/GeV
```
2]
Belle II simulation preliminary
ROE HadronicROE Semileptonic
Signal HadronicSignal Semileptonic
5 0 5 10 15 20 25
q2 [GeV2]
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
```
1NdNd (q
```
```
2) [1/GeV
```
2]
Belle II simulation preliminary
Strange, >2 daughtersStrange, 2 daughters
Narrow, >2 daughtersNarrow, 2 daughters
Broad, >2 daughtersBroad, 2 daughters
```
0.90 0.92 0.94 0.96 0.98 1.00 1.02(BDT2)0
```
5
10
15
20
25
30
35
1N
```
dNd (BDT2)
```
Belle II simulation preliminary
ROE HadronicROE Semileptonic
Signal HadronicSignal Semileptonic
```
0.90 0.92 0.94 0.96 0.98 1.00 1.02(BDT2)0
```
5
10
15
20
25
30
35
40
1N
```
dNd (BDT2)
```
Belle II simulation preliminary
Strange >2 daughtersStrange 2 daughters
Narrow >2 daughtersNarrow 2 daughters
Broad >2 daughtersBroad 2 daughters
```
Figure 89: Normalized distribution of q2 (top) and η(BDT2) (bottom) for B → D∗∗X
```
backgrounds in B+ → K+ν ¯ν signal region. On the left, the backgrounds are grouped
```
according to the X composition (semileptonic or hadronic) and the D∗∗ mother B-side. On
```
```
the right the backgrounds are grouped according the D∗∗ (where D∗0 (2300) and D′1(2430)
```
```
are “broad”, D1(2420)±, D∗2 (2460) are “narrow”, and Dsj are “strange”) and according
```
to the number of D∗∗ daughters.
141
K Treatment of B → Xhs ν ¯ν background1505
B → Xhs ν ¯ν decays where Xhs corresponds to all final states containing strangeness exclud-1506
ing K and K∗ provide important contributions to the background. A Standard Model1507
expectation of the branching fraction for them can be estimated using Ref. [2], which pro-1508
```
vides the total branching fraction for B → Xsν ¯ν decays, (2.9±0.3)×10−5, and subtracting1509
```
```
the contributions from B → Kν ¯ν and B → K∗ν ¯ν to be (1.6 ± 0.3) × 10−5.1510
```
The B → Xhs ν ¯ν decays are expected to follow a complex structure dominated by1511
several K∗ resonances which interfere with each other. For the current analysis, the1512
most important are low multiplicity decays. A glimpse on the possible structures can be1513
obtained by examining the LHCb measurement of B+ → K+π−π+µ+µ−, Ref. [37]. At low1514
```
Xhs invariant masses, the decay is dominated by K1(1270) and K1(1400) resonances, while1515
```
contributions at high masses are relatively small. The LHCb analysis demonstrates that1516
the invariant mass distribution of Xhs is similar to the one observed in B+ → K+π−π+J/ψ1517
decays for which Belle performed an amplitude analysis in Ref. [38].1518
```
In the release 6 Belle II simulation, the processes are modeled using Pythia (Xsu and1519
```
```
Xsd samples). It is assumed that Xhs invariant starts at around 1.1 GeV in a threshold-1520
```
like manner. Resonances are not simulated. We use Belle II simulation as a cross check,1521
```
while for the baseline prediction we use an equal mixture of B → K1(1270)ν ¯ν and B →1522
```
```
K1(1400)ν ¯ν decays generated according to phase space. The total branching fraction is1523
```
```
taken to be (1.6 ± 0.5) × 10−5 for both B+ and B0 decays. K1(1270) and K1(1400) decays1524
```
have different branching fractions for K∗π compared Kρ yielding different impacts on1525
B → Kν ¯ν and B → K∗ν ¯ν backgrounds. To take this into account, we vary relative1526
contributions of the K1 mesons between 0.25/0.75 and 0.75/0.25.1527
Channel B+ → K+ν ¯ν B+ → K∗+ν ¯ν B0 → K0S ν ¯ν B0 → K∗0ν ¯ν
```
K+1 (1270) 0.090 ± 0.003 0.526 ± 0.007 0.047 ± 0.002 0.858 ± 0.010
```
```
K01 (1270) 0.059 ± 0.003 0.671 ± 0.008 0.054 ± 0.002 0.944 ± 0.010
```
```
K+1 (1400) 0.126 ± 0.004 0.718 ± 0.008 0.067 ± 0.003 1.640 ± 0.013
```
```
K01 (1400) 0.083 ± 0.003 0.865 ± 0.009 0.076 ± 0.003 1.122 ± 0.011
```
Xsu 0.270 ± 0.001 0.311 ± 0.001 0.167 ± 0.001 0.421 ± 0.002
Xsd 0.323 ± 0.002 0.424 ± 0.002 0.178 ± 0.001 0.545 ± 0.002
```
Table 45: Efficiency (in %) for reconstructing B → K1ν ¯ν and B → Xsu,dν ¯ν events in the
```
signal region of the analysis. Note that the signal efficiency for the signal region is 8% for
K+ and K0S channels, 5% for K∗0 and 3% for K∗+
Table 45 shows efficiency to reconstruct the B → Xhs ν ¯ν events in the signal region of1528
each analysis. As expected, the impact is larger for K∗ channels since for them only one1529
extra particle should be misreconstructed. Since the Xs model generates also two-body1530
```
decays, it yields a higher impact for K+ and K0S modes compared to the K1 models;1531
```
however, the efficiency is still small compared to the signal efficiency of 8%. For the K∗1532
```
decays, the K1(1400) model gives the highest efficiency: it is expected since K∗π is the1533
```
```
leading branching fraction for K1(1400) decays. Given the smallness of the Xhs contribu-1534
```
tion for the K+ and K0S channels, the variations of the K1 decay fractional contribution1535
and of the overall branching fraction provide sufficient variation of the model.1536
142
L Treatment of B → Kn¯n background1537
Decays with low multiplicity involving neutrons and kaons in the final state are of par-1538
```
ticular concern for the analysis; B → Kn¯n decays fall into this category. The B → Kn¯n1539
```
background constitutes 0.2%, 0.3% and 0.3% of the total background in the signal region1540
of the channel B0 → K0S ν ¯ν, B0 → K∗0ν ¯ν and B+ → K∗+ν ¯ν, respectively. They have1541
not been measured in the past, however, those can be predicted using isospin symmetry1542
relation with B → Kp¯p decays and lifetime difference of B+ and B0. We summarize the1543
branching fractions in Table 46.1544
B → Kp¯p decay BF B → Kn¯n decay BF
B+ → K+p¯p [39] 5 × 10−6 B0 → K0n¯n 4.65 × 10−6
B+ → K∗+p¯p [40] 3.6 × 10−6 B0 → K∗0n¯n 3.35 × 10−6
B0 → K0p¯p [41] 3 × 10−6 B+ → K+n¯n 3.24 × 10−6
B0 → K∗0p¯p [40] 1.24 × 10−6 B+ → K∗+n¯n 1.34 × 10−6
Table 46: Measured BF of B → Kp¯p decays and assumed BF of B → Kn¯n decays using
isospin symmetry relations and lifetime difference of B+ and B0.
These decays are simulated in the standard Belle II MC using a 3-body phase space1545
model. However, as noted in Refs. [39, 40, 41], an enhancement near the p¯p threshold has1546
been observed. To account for this effect, the data from these references were fitted using1547
a threshold plus exponential function, as illustrated in Fig. 90. Subsequently, dedicated1548
samples of 10,000 events for the B → Kn¯n decays were generated and reweighted from1549
```
pure phase space to match the fit result; see Fig. 91. The B → Kn¯n decays from the1550
```
generic simulation are removed and the reweighted events from the dedicated signal MC1551
are inserted according to the branching fractions given in Table 46. In this way, we correct1552
both the modeling and the branching fraction for these decays.1553
Other baryonic decays such as B → KΛ¯Λ also contribute to the background. A1554
detailed study of these modes was performed for the published B+ → K+ν ¯ν analysis, see1555
```
[19], appendix T. These modes have a similar to B → K(∗)n¯n decays K-meson momentum1556
```
spectrum, and are more suppressed due to extra particles and in several cases smaller1557
branching fraction. Since we do not expect an increase of the contribution for the K∗1558
compared to the K+ modes, we follow the same prescription as for the K+ analysis to1559
estimate their impact: we assign 100% systematic uncertainty to the branching fracton1560
```
of B → K(∗)n¯n decays, which takes into account the imperfections in the threshold1561
```
enhancement modeling, the assumption of the isospin symmetry to relate B → Kn¯n to1562
```
B → Kp¯p decays, the modeling of (anti) neutrons in the calorimeter, and contribution1563
```
from other baryonic modes.1564
143
1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
```
M(pp) [GeV/c2]
```
0
50
100
150
200
Yields
B + K + pp
```
Threshold fit: A(x xth)ne xA=33877.1, xth=1.93
```
```
n=0.34, =2.212/dof=2.35
```
```
Threshold = 1.93 GeV/c2Data
```
1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
```
M(pp) [GeV/c2]
```
0
50
100
150
200
Yields
```
B0 K0ppThreshold fit: A(x xth)ne xA=48381.3, xth=1.98n=0.16, =2.50
```
2/dof=1.02Threshold = 1.98 GeV/c2
Data
1.75 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00
```
M(pp) [GeV/c2]
```
0
5
10
15
20
25
30
Yields
B + K* + pp
```
Threshold fit: A(x xth)ne xA=2523437.0, xth=1.93
```
```
n=0.56, =5.112/dof=1.65
```
```
Threshold = 1.93 GeV/c2Data
```
1.75 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00
```
M(pp) [GeV/c2]
```
5
0
5
10
15
20
25
30
Yields
B0 K*0pp
```
Threshold fit: A(x xth)ne xA=130071.3, xth=1.876
```
```
n=0.54, =3.732/dof=0.23
```
```
Threshold = 1.876 GeV/c2Data
```
```
Figure 90: Result of a threshold plus exponential function fit of M (p¯p) obtained in B →
```
Kp¯p data from Refs. [39, 40, 41]
5 10 15 20
Q2_gen
0
20
40
60
80
100
120
Events
B0 K0nn
```
phspM(pp) enhanced
```
5 10 15 20
Q2_gen
0
50
100
150
200
250
300
Events
B0 K*0nn
```
phspM(pp) enhanced
```
5 10 15 20
Q2_gen
0
50
100
150
200
250
300
350
Events
B+ K* + nnphsp
```
M(pp) enhanced
```
Figure 91: Generator level q2 distributions of simulated B → Kn¯n decays. The blue his-
tograms correspond to phase space MC and the red histograms correspond to reweighted
MC. The reweighting has been done using the fit function described in Fig. 90.
144
M Fake K∗ background investigations1565
Besides the K∗0 and K∗+ mass sideband samples are used to validate the fake K∗ back-1566
```
ground, we checked directly the fake K∗ background composition in M (K∗) signal region.1567
```
M.1 Fake K∗0 background investigation1568
```
We directly examined the composition of fake K∗0 candidates within the M (K∗0) signal1569
```
region. Fake candidates are identified based on the mcPDG value associated to the K∗0.1570
A significant contribution originates from semileptonic B decays involving D0 or D+1571
mesons. In addition, there is a substantial combinatorial background component, includ-1572
```
ing fake contributions from both B mesons and Υ(4S) decays. Figure 92 illustrates the1573
```
composition of the fake K∗0 background in both the ηBDT2 signal region and its close1574
sideband. The MC events in the ηBDT2 close sideband region show a composition similar1575
to that of the signal region. This similarity allows us to validate the data–MC agreement1576
using the sideband events.1577
To validate the D+ fake contribution, we reconstruct D+ candidates using the signal1578
K+ and π+π−. The pions can come either from the signal side or from the ROE. In the1579
K+π+π− mass spectrum, we observe a D+ peak as shown in Fig. 93. We then extract1580
```
the D+ yields from both data and MC by fitting the M (K+π+π−) distribution as shown1581
```
in Fig. 94. The yield ratio between data and MC is found to be 0.9 ± 0.06, indicating1582
that the MC overestimates this component by about 10%. We also examine the data–MC1583
```
yield ratio in the M (K∗0) sideband region and the ηBDT2 signal region by performing a1584
```
```
fit (an example is shown in Fig. 94), obtaining a ratio of 0.81 ± 0.07. To be conservative,1585
```
we assign 20% uncertainty for D+ fakes.1586
Figure 92: Fake K∗0 background compositions in ηBDT2 signal region and close sideband
region.
```
To validate the Υ(4S) fake contribution, we reconstruct D0 candidates using the signal1587
```
```
K+ and π− from the rest of the event (ROE). The data–MC comparison of the M (K+π−)1588
```
145
Figure 93: Data and MC comparisons for D+ fake background in ηBDT2 close sideband
```
region in M (K∗0) signal region (left) and in M (K∗0) sideband region (right).
```
```
Figure 94: Example: Data and MC fits to M (K+π+π−) in the M (K∗0) sideband region.
```
```
**Fits to the other distributions also show good agreement; therefore, we do not include
```
them here for brevity.**
```
distribution is shown in Fig. 95. A clear D0 peak is observed, originating from Υ(4S) and1589
```
```
q ¯q (Z0) fake backgrounds. The q ¯q component is normalized using a scale factor derived1590
```
from off-resonance data. After applying this normalization, the data–MC yield ratio for1591
```
the D0 peak is found to be 1.05 ± 0.06, which quantifies data-MC discrepancy of Υ(4S)1592
```
```
fakes. We assign 10% uncertainty for Υ(4S) fakes.1593
```
To validate the D0 fake contribution, we reconstruct D0 candidates using the signal1594
```
K+ and either the π−π0 from the rest of the event (ROE) or the ROE π0 with signal π−.1595
```
```
The data–MC comparison of the M (K+π−π0) distribution is shown in Fig. 96 (upper),1596
```
where a clear D0 peak from D0 fake is observed. The data–MC yield ratio for the D01597
peak is determined to be 1.11 ± 0.18, consistent with unity, although the relatively large1598
uncertainty and potential impact of additional π0 reconstruction effects limit its precision.1599
Additionally, we validate the D0 fake contribution using reconstructed D0 candidates1600
formed from the signal K+ and π−π+π− tracks from the ROE or signal π−. The corre-1601
```
sponding M (K+π−π+π−) distribution is shown in Fig. 96 (lower left). In the M (K∗0)1602
```
signal region, both D0 fake backgrounds and real K0 events contribute to the peak at1603
D0 mass, complicating the interpretation. To isolate the D0 fake component, we examine1604
```
the same M (K+π−π+π−) distribution in the M (K∗0) sideband region, shown in Fig. 961605
```
146
```
Figure 95: Data and MC comparisons for Υ(4S) fake background in ηBDT2 close sideband
```
region.
```
(right), where real K0 contributions are suppressed. The data–MC yield ratio in this re-1606
```
gion is found to be 0.71 ± 0.06. To account for discrepancies and maintain a conservative1607
estimate, we assign a 30% systematic uncertainty to the D0 fake background contribution.1608
M.2 Fake K∗+ background investigation1609
Similar investigation is performed for fake K∗+ in B+ → K∗+ν ¯ν signal channel. A signifi-1610
cant contribution originates from semileptonic B decays involving D0 mesons. In addition,1611
there is a substantial combinatorial background component, including fake contributions1612
```
from both B mesons and Υ(4S) decays. Fake candidates are identified based on the1613
```
mcPDG value of the associated K+. We directly examined the composition of fake K∗+1614
```
candidates within the M (K∗+) signal region in both the ηBDT2 signal region and its close1615
```
sideband. The MC events in the ηBDT2 close sideband region show a composition similar1616
to that of the signal region, as shown in Fig. 97. This similarity allows us to validate the1617
data–MC agreement using the sideband events.1618
To validate the D0 fake contribution, we reconstruct D0 candidates using the signal1619
```
K+ and a π− track from ROE. The data–MC comparison of the M (K+π−) distribution is1620
```
```
shown in Fig. 98 (upper), where a clear D0 peak from fake D0 contributions is observed.1621
```
The data–MC yield ratio for the D0 peak is found to be 0.85 ± 0.17, which is consistent1622
with unity within uncertainties. Based on this study and the corresponding analysis in1623
the K0 channel, we assign a conservative 30% uncertainty to the D0 fake background1624
and a 20% uncertainty to the D+ fake background. The D+ fake contribution in the K+1625
```
channel is negligible (less than 1%).1626
```
```
To validate the Υ(4S) fake contribution, we reconstruct D0 candidates using the signal1627
```
```
K meson (K+ or K0S ) and a π− track from ROE. The data–MC comparisons of the1628
```
```
M (K+π−) and M (K0S π−) distributions are shown in Fig. 99. Clear D0 peaks are observed,1629
```
```
originating from Υ(4S) fake backgrounds. The q ¯q component is normalized using a scale1630
```
factor derived from off-resonance data. The data–MC yield ratios for the D0 peak are1631
147
```
Figure 96: Comparison between data and MC for M (K+π−π0) (top left), M (K+π−π+π−)
```
```
in the M (K0) signal region (top right) and sideband region (bottom), showing the D0
```
fake background within the ηBDT2 close sideband region.
Figure 97: Fake K∗+ background compositions in ηBDT2 signal region and close sideband
region.
found to be 0.87 ± 0.05 for the K+ → K+π0 channel and 0.86 ± 0.11 for the K+ → K0S π+1632
```
channel. These values quantify the level of data–MC discrepancy in the Υ(4S) fake1633
```
148
Figure 98: Data and MC comparisons for D+ fake background in ηBDT2 close sideband
region.
```
background. Consequently, we assign a conservative 10% uncertainty to the Υ(4S) fake1634
```
background.1635
```
Figure 99: Data and MC comparisons for Υ(4S) fake background in ηBDT2 close sideband
```
region.
149
N Validation of total weight in sidebands1636
We validate the total event weight, defined as the product of all individual weights, by1637
performing template fits to the reconstructed q2rec distributions in the ηBDT2 and K∗ mass1638
sideband samples.1639
For the modeling of the fit components, all event weights used in the nominal analysis1640
are applied consistently to the sideband samples. These include weights associated with1641
D → K0L decays, leading-B and D∗∗ contributions, additional normalization weights for1642
events untagged by the leading-B or D∗∗ corrections, as well as weights related to BDTc,1643
PID corrections etc.1644
In the fits, the q ¯q components are assigned a 50% normalization uncertainty and are1645
allowed to float, following the nominal signal-extraction procedure described in Sec. 14.1646
The B ¯B components are fixed, as their normalizations are already corrected by the applied1647
weights. We should note that, the nominal signal-extraction has more freedom in the fit1648
model, such as 50% uncertainties assigned to untagged events, 10–30% uncertainties on1649
fake K∗ contributions, and additional systematic uncertainties related to PID and other1650
sources. Fixing the B ¯B components in this study therefore provides a stringent test for1651
the overall weighting and fitting procedure.1652
The χ2/ndf values obtained from fits to the ηBDT2 sideband are 26/21, 16/22, 50/21,1653
```
and 50/21 for the K+, K0S , K∗0, and K∗+ channels, respectively (first four panels in1654
```
```
Fig. 100). For the K∗ mass sideband fits, the corresponding χ2/ndf values are 31/21 and1655
```
```
15/21 for the K∗0 and K∗+ channels, respectively (Fig. 101). All fits exhibit acceptable1656
```
quality, although the ηBDT2 sideband fits in the K∗0 and K∗+ channels yield somewhat1657
larger χ2 values.1658
To provide additional freedom for the B ¯B component, a 50% normalization uncer-1659
tainty is assigned to the untagged event category. With this modification, shown in the1660
last two panels of Fig. 100, the fit quality improves, yielding χ2/ndf = 40/21 and 25/211661
for the K∗0 and K∗+ channels, respectively.1662
150
0
2000
4000
6000
8000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B + →K + ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
0
500
1000
1500
2000
2500
```
Candidates/(1 GeV
```
2/c
```
4)
```
B 0→K 0S ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15 20
q2rec
0.9
1.0
1.1
data/MC
0
2000
4000
6000
8000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B 0→K ∗0ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
0
2000
4000
6000
8000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B + →K ∗ + ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
0
2000
4000
6000
8000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B 0→K ∗0ν¯ν
untagged
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
0
2000
4000
6000
8000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B + →K ∗ + ν¯ν
untagged
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
Figure 100: Fits to q2rec are performed using ηBDT2 sideband samples for the four channels.
In the last two ηBDT2 sideband fits, the untagged event yields are allowed to vary with a
50% uncertainty.
151
0
500
1000
1500
2000
2500
3000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B 0→K ∗0ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
0
200
400
600
800
1000
```
Candidates/(1 GeV
```
2/c
```
4)
```
B + →K ∗ + ν¯ν
mixed
charged
taupair
ssbar
ccbar
ddbar
uubar
Sim. stat. unc.
Data
0 5 10 15
q2rec
0.9
1.0
1.1
data/MC
Figure 101: Fits to q2rec are performed using K∗0 mass sideband samples.
152
O D veto studies for B+ → K+ν ¯ν decays1663
In the original analysis [3], the D veto variables are designed to cover all possible D as well1664
as K∗ decays. Only a loose selection on the invariant mass of the particles forming the1665
meson candidate is applied. The candidates are then ranked and a single candidate with1666
the best probability of a common vertex fit pvtx is considered. While being reasonably1667
efficient to remove generic D decays, this approach misses low-multiplicity D decays that1668
may have worse pvtx compared to the best candidate.1669
Decay Fraction PDG Fraction SR
```
D0 → K−π+ (3.947 ± 0.030)% 21.00%
```
```
D0 → K−π+π0 (14.4 ± 0.6)% 32.82%
```
```
D0 → K−e+νe (3.548 ± 0.026)% 16.60%
```
```
D0 → K−µ+νµ (3.41 ± 0.04)% 14.17%
```
Table 47: Fraction of D0 → K−X decays as in PDG and for events in which K−
```
corresponds to the signal region (SR) of the B+ → K+ν ¯ν analysis from Ref. [3]
```
The background where the signal K+ candidate originates from a D-meson decay1670
accounts for 47% of the B-background in the signal region, thus it has substantial impact1671
on the measurement. In a new study, the truth-level composition of the D0-meson decays1672
is studied as shown in Table 47. The background composition in the signal region of the1673
analysis is skewed towards low-multiplicity decays. Thus, variables targeting D0 → K−π+1674
in a narrow mass range around the nominal D0 mass can be used to further suppress1675
background.1676
O.1 Normalization factors1677
```
The goal is to extract the normalization factor (NF) for the η(BDT2) signal region1678
```
```
[0.92, 1.00] to better constrain the D0 background (and potentially other D backgrounds)1679
```
in the final fit for both on-resonance and off-resonance samples. Specifically, we recon-1680
struct the D0 → K−π+ decay for events that survive the B+ → K+ν ¯ν analysis from1681
Ref. [3]. The NF is defined as the ratio of data to MC D yields, which can be directly1682
```
obtained by fitting the M (Kπ) distributions in the η(BDT2) signal region [0.92, 1.00].1683
```
```
Due to the limited statistics in the η(BDT2) signal region [0.92, 1.00], we predict the1684
```
```
NF for this region by measuring the NFs in the η(BDT2) sideband regions [0.75, 0.80],1685
```
[0.80, 0.85], and [0.85, 0.92]. The final NF will be determined using a weighted average1686
of the directly fitted NF in the signal region and the predicted NF derived from the1687
sideband regions.1688
```
• Signal and background modeling;1689
```
```
– Signal: Figure 102 shows the invariant mass fits for the signal (isSignal==1)1690
```
D0 → K−π+ decay. The signal is modeled by JohnsonSU function. We get1691
```
the parameters for the signal model for the on-(off-)resonance sample from in1692
```
153
```
the η(BDT2) sideband ([0.75, 0.80], [0.80, 0.85], [0.85, 0.92]) and signal region1693
```
```
[0.92, 1.00] of the B+ → K+ν ¯ν analysis from Ref. [3];1694
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
1000
2000
3000
4000
5000
6000
7000 TotalJohnsonSUData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
500
1000
1500
2000
2500
3000 TotalJohnsonSU
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
200
400
600
800
1000
1200
1400 TotalJohnsonSU
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
50
100
150
200TotalJohnsonSUData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
100
200
300
400
500
600TotalJohnsonSUData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
50
100
150
200
250
300TotalJohnsonSU
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
20
40
60
80
100
120
140 TotalJohnsonSU
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
5
10
15
20TotalJohnsonSUData
```
Figure 102: Invariant mass fit of K− π+ signal for (1 ab−1 q ¯q, 3 ab−1 B ¯B) of the on-
```
```
resonance MC (upper) 4×42 fb−1 of the off-resonance MC (lower) in the η(BDT2) sideband
```
```
regions: [0.75, 0.80], [0.80, 0.85], [0.85, 0.92] and signal region [0.92, 1.00] (from left to
```
```
right) of the B+ → K+ν ¯ν analysis from Ref. [3].
```
– Background: Figure 103 shows the modeling of background from D0 → K−π+1695
decays reconstructed with isSignal != 1, using a second-order polynomial1696
with free parameters. A first-order polynomial does not adequately describe1697
```
the background shape, due to a bias in the M (Kπ) distribution introduced1698
```
```
by the η(BDT2) selection. While the second-order polynomial still provides1699
```
a suboptimal description, it is sufficient for the fit. In the global fits to MD,1700
the second-order polynomial shape is fixed to the current model, while the1701
background yield is allowed to float. The resulting signal and background1702
yields are consistent with the input values from simulation.1703
```
• The shape parameters described above are fixed in the corresponding η(BDT2)1704
```
regions. To achieve better agreement between data and MC, we introduce two1705
fudge factors for the signal resolution and the peak position. Specifically, in the1706
```
global fits to the M (Kπ) distributions, the D peak resolution and position of the1707
```
JohnsonSU function are parameterized as γ × r and µ + s, respectively. Here, γ and1708
µ are the parameters obtained from signal-only MC fits, while r and s are fudge1709
factors that are allowed to float freely in the fit. Figure 104 and Figure 105 show1710
```
the M (Kπ) global fits to data and MC for on-resonance and off-resonance samples.1711
```
The fit results and the NFs can be found in Table 48.1712
• Systematic uncertainty1713
– The data-MC difference of fudge factors will be considered as the system-1714
```
atic uncertainty for signal PDF modeling. They are 3%(11%), 3.9%(21.6%),1715
```
```
6.3%(32.4%) for the η(BDT2) sideband regions [0.75, 0.80], [0.80, 0.85], [0.85,1716
```
```
0.92] for on-resonance (off-resonance) sample, respectively. The uncertainty1717
```
154
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M1600
1800
2000
2200
2400TotalBackgroundData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M700
800
900
1000
1100
1200Total
BackgroundData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M
400
450
500
550
600 TotalBackground
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M70
80
90
100
110
120
130
140 TotalBackground
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M180
200
220
240
260
280
300
320 TotalBackground
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M70
8090
100110
120130
140 TotalBackgroundData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M20
30
40
50
60TotalBackgroundData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
2
4
6
8
10
12
14
16Total
BackgroundData
```
Figure 103: Invariant mass fit of K− π+ background for (1 ab−1 q ¯q, 3 ab−1 B ¯B) of the
```
```
on-resonance MC (upper) 4 × 42 fb−1 of the off-resonance MC (lower) in the η(BDT2)
```
```
sideband regions: [0.75, 0.80], [0.80, 0.85], [0.85, 0.92] and signal region [0.92, 1.00] (from
```
```
left to right) of the B+ → K+ν ¯ν analysis from Ref. [3].
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
2000
4000
6000
8000Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
500
1000
1500
2000
2500
3000
3500Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
250
500
750
1000
1250
1500
1750 Totalbackground
signalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
50
100
150
200
250
300
350Total
backgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
500
1000
1500
2000
2500
3000 Totalbackground
signalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
200
400
600
800
1000
1200Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
100
200
300
400
500
600 Totalbackground
signalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
20
40
60
80
100
120 Totalbackground
signalData
```
Figure 104: Invariant mass fit of K− π+ for (1 ab−1 q ¯q, 3 ab−1 B ¯B) of the on-resonance
```
```
MC (upper) and 365 fb−1 of on-resonance data (lower) in the η(BDT2) sideband regions:
```
```
[0.75, 0.80], [0.80, 0.85], [0.85, 0.92] and signal region [0.92, 1.00] (from left to right) of
```
the B+ → K+ν ¯ν analysis from Ref. [3].
comes from the signal resolution, while the uncertainty for peak position is1718
found out to be negligible.1719
– The systematic uncertainty associated with the fixed second-order polynomial1720
background is evaluated by refitting the data using a free second-order polyno-1721
mial background. The difference in the D signal yield obtained from these fits1722
```
is taken as the systematic uncertainty for the background. They are 1.4%(0%),1723
```
```
1.2%(0%), 2.2%(0%) for the η(BDT2) sideband regions [0.75, 0.80], [0.80, 0.85],1724
```
```
[0.85, 0.92] for on-resonance (off-resonance) sample, respectively.1725
```
```
• The normalization factor (NF) in the signal region is extrapolated from the NFs in1726
```
155
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
200
400
600
800Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
50
100
150
200
250
300
350Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
25
50
75
100
125
150
175 Totalbackground
signalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
5
10
15
20
25
30Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
50
100
150
200Totalbackgroundsignal
Data
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
1020
3040
5060
7080 TotalbackgroundsignalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
10
20
30
40TotalbackgroundsignalData
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90M0
2
4
6
8
10
12 Totalbackground
signalData
```
Figure 105: Invariant mass fit of K− π+ for 4 × 42 fb−1 of the off-resonance MC (upper)
```
```
42 fb−1 of the off-resonance data (lower) in the η(BDT2) sideband regions: [0.75, 0.80],
```
```
[0.80, 0.85], [0.85, 0.92] and signal region [0.92, 1.00] (from left to right) of the B+ → K+ν ¯ν
```
analysis from Ref. [3].
0.75 0.80 0.85 0.90 0.95 1.00BDT20.90
0.95
1.00
1.05
1.10
1.15
1.20
1.25
R
Linear Fit and Prediction: R vs. BDT2
Fitted Line: y = -0.21x + 1.24Predicted: 1.04 ± 0.13
```
Measured: 1.09 ± 0.16Measured Data
```
0.75 0.80 0.85 0.90 0.95 1.00BDT2
0.2
0.4
0.6
0.8
1.0
1.2
R
Linear Fit and Prediction: R vs. BDT2
Fitted Line: y = -2.19x + 2.77Predicted: 0.67 ± 0.47
```
Measured: 0.49 ± 0.29Measured Data
```
```
Figure 106: NFs in the η(BDT2) sideband regions and the predicted NF in the η(BDT2)
```
```
signal region for on-resonance (left) and off-resonance (right) samples.
```
the sideband regions by fitting with a linear function, as illustrated in Figure 106.1727
```
The predicted on-resonance (off-resonance) NF is 1.04 ± 0.13 (0.67 ± 0.47). After1728
```
performing a weighted average with the measured NF in the signal region, 1.09±0.161729
```
(0.49 ± 0.29), the final values are determined to be 1.06 ± 0.10 (0.54 ± 0.25).1730
```
O.1.1 Constrain on each component1731
```
The D0 background in the η(BDT2) signal region comprises three components, as shown1732
```
in Figure 107. To ensure a more accurate and stable fit, constraints are applied to each1733
component in the on-resonance sample. The corresponding D0 yields are determined from1734
simulation, as illustrated in Figure 107.1735
156
```
η(BDT2) region on-res data on-res MC off-res data off-res MC
```
[0.75, 0.80] ND 12911 ± 234 11993 ± 123 833 ± 61 775 ± 29
```
NF 1.07 ± 0.04 (0.02) 1.07 ± 0.14 (0.07)
```
[0.80, 0.85] ND 5640 ± 159 5207 ± 82 336 ± 50 342 ± 19
```
NF 1.08 ± 0.05 (0.03) 0.98 ± 0.24 (0.11)
```
[0.85, 0.92] ND 2602 ± 114 2516 ± 61 131 ± 27 161 ± 13
```
NF 1.03 ± 0.09 (0.05) 0.82 ± 0.30 (0.13)
```
[0.92, 1.00] ND 430 ± 48 398 ± 29 11 ± 6 23 ± 5
NF 1.09 ± 0.16 0.49 ± 0.29
Table 48: the D0 normalization factors for on-resonance and off-resonance samples in
```
η(BDT2) sideband and signal regions. MC yields are normalized to the data luminosities.
```
Figure 107: Proportion of D0 background sources.
O.2 Inclusion in the likelihood1736
The constraints obtained using reconstructed D-meson decays are included directly into1737
PYHF likelihood. At the moment, PYHF is designed for binned fits to data counts and1738
uses Poisson statistics. This is not applicable for the data to simulation D0 yield ratios1739
R. To make the Poisson contribution negligible, the model is built using an arbitrarily1740
large number Nref for the data counts, which is compared to the prediction Nref /R. The1741
uncertainty on R, σR, is treated as statistical uncertainty on the prediction. The predic-1742
tions are scaled using the background normalization factors µ. For off-resonance data,1743
157
Parameter Value
Nref 100000
Roffr 0.55
σoffrR 0.25
RY4S 1.06
σY4SR 0.10
fc¯c 0.47
fB+B− 0.44
fB0B0 0.09
```
Table 49: Values of parameters used in Eq. (7) and Eq. (8)
```
the only contributing factor is µc¯c, and the corresponding χ2 function is71744
```
χ2offres(µc¯c) =
```

Nref − NrefRoffr µc¯c
2

σoffrR
Roffr
Nref
Roffr
```
2 . (7)1745
```
```
For Υ (4S) data, contributions from c¯c, BB and B+B− are weighted with corresponding1746
```
fractions f and the χ2 function is1747
```
χ2Y4S(µc¯c, µB+B− , µB0B0 ) =
```

```
Nref − NrefRY4S (fc¯cµc¯c + fB+B− µB+B− + fB0B0 µB0B0 )
```
2

σY4SR
RY4S
Nref
RY4S
```
2 . (8)1748
```
The values of parameters used are given in Table 49.1749
```
O.3 BDT2 bias correction in M (Kπ)1750
```
```
As M (Kπ) (with BCS based on D vertex) is one of the most important BDT2 training1751
```
```
features, the selections applied to BDT2 would bias the M (Kπ) distribution (without BCS1752
```
```
based on D vertex), that is, what we are using in this section. Since the resolution of D1753
```
in MC used for training BDT2 is better than in the actual data as shown in Figure 1081754
```
(left), applying the BDT2 selection introduces a bias in the data peak for the second1755
```
```
bump due to the poorer resolution Figure 108 (right).1756
```
To correct this bias, we adjust the data resolution by narrowing the broader data1757
peak to match the sharper MC peak. This is achieved by fitting the distributions shown1758
```
in Figure 109 (left) and computing the cumulative distributions for both data and MC.1759
```
```
Using the mapping derived from Figure 109 (right), we apply a correction to each data1760
```
```
point. The resulting shifted distribution (Figure 110) replaces the original MKπ spectrum.1761
```
Finally, we apply the BDT2 weights to obtain ηBDT2 for the D-veto analysis.1762
7The statistical uncertainty on the prediction is implemented in PYHF as an additional nuisance
```
parameter. This treatment is equivalent to including the uncertainty in the denominator of Eq. (7), as
```
can be demonstrated by minimizing the likelihood with respect to the nuisance parameter.
158
```
Figure 108: The invariant mass of K+π with only BDT1 selection (left); The invariant
```
```
mass of K+π with η(BDT2) selection (sideband [0.75,0.92])
```
```
Figure 109: Fits to invariant mass of K+π with only BDT1 selection (left); cumulative
```
distributions in data and MC.
Figure 110: Invariant mass of K+π in data before and after correction
159
Trigger Description
```
fff N(2D tracks) is 2 or more and no injection veto
```
```
ffo N(2D tracks) is 2 or 3 or more and CDC opening angle > 90
```
◦
and no Bhabha and injection vetoes
```
ffb N(2D tracks) is 2 or 3 or more and CDC track 1-5 back-to-backand no Bhabha and injection vetoes
```
```
ffy N(2D tracks) is 3 or more and N(Neuro 3D tracks) is 1 or 2 or moreand no injection veto
```
```
fyb N(2D tracks) is 2 or 3 or more and N(Neuro 3D tracks) is 1 or 2 or more andCDC track 1-5 back-to-back and no Bhabha and injection vetoes
```
```
fyo N(2D tracks) is 2 or 3 or more and N(Neuro 3D tracks) is 1 or 2 or more andCDC opening angle > 90◦ and no Bhabha and injection vetoes
```
hie ECL total energy > 1 GeV and no Bhabha and injection vetoes
```
c4 N(clusters)>3 and no Bhabha and injection vetoes
```
Table 50: List of triggers used for the trigger efficiency study for the B0 → K0S ν ¯ν channel.
P Trigger study for the B0 → K0S ν ¯ν channel1763
We study the trigger efficiency for the B0 → K0S ν ¯ν candidates reconstructed in data in1764
```
the partially blinded region, η(BDT2) > 0.68 and 0.9 < BDT1 < 0.99. The considered1765
```
triggers and their description are summarized in Table 50.1766
We define efficiency as a ratio, where the number of events that pass the trigger of1767
```
interest selection, as well as the normalization trigger selection, is considered a numerator;1768
```
the number of events that pass only the normalization trigger selection is considered1769
```
a denominator: ε(trigger of interest) = N (events passed trigger of interest and normalization trigger)N (events passed normalization trigger) .1770
```
The ffy and c4 are used as normalization triggers for the ECL and CDC trigger studies,1771
respectively. Figure 111, left plane, shows the trigger efficiency as a function of experiment1772
number. It is visible that the definition of fff, ffo, and ffb was changed after the experiment1773
16.1774
Further, we calculate a trigger efficiency by combining CDC and ECL trigger effi-1775
```
ciencies, i.e. εcombined = εffy|fyo|fff|ffo + (1 − εffy|fyo|fff|ffo)εc4|hie. We check how the combined1776
```
```
efficiency looks as a function of tracks in the rest of event (Figure 111, right plane). The1777
```
efficiency reaches 100% for all events apart from the events with only two tracks in the1778
rest of event, where the efficiency drops to 98%.1779
160
```
Figure 111: Trigger efficiency as a function of (left) experiment number and (right)
```
number of tracks in the rest of event obtained for the B0 → K0S ν ¯ν candidates reconstructed
in data.
161
Q Deep Neural Network Architectures1780
```
To supplement or replace the Boosted Decision Tree (BDT) classifiers for background sup-1781
```
```
pression, Deep Neural Network (DNN) models were explored. Two primary architectures1782
```
```
were investigated: a Multi-Layer Perceptron (MLP) based on NeuralNetwork (Figure 113)1783
```
```
and a Transformer-based model, TransformerClassifier (Figure 114). For the channels1784
```
```
where DNNs were applied (currently B0 → K∗0ν ¯ν, B0 → K0S ν ¯ν and B+ → K∗+ν ¯ν as1785
```
```
DNN2), an improvement in significance of approximately 20% was observed compared to1786
```
the BDT approach.1787
Q.1 Performance Comparison with BDT1788
```
The performance of the final DNN classifiers (DNN2) was compared against the BDT1789
```
classifiers used in previous iterations or as benchmarks. Figure 112 illustrates the signal1790
```
significance (S/
```
√
```
S + B, assuming nominal branching fractions and background levels) as1791
```
a function of signal efficiency for both the DNN and BDT approaches in the B0 → K0S ν ¯ν,1792
B0 → K∗0ν ¯ν, and B+ → K∗+ν ¯ν channels. This comparison confirms the enhanced1793
discriminating power of the DNNs, particularly in specific efficiency regions relevant for1794
the analysis.1795
```
Q.2 Multi-Layer Perceptron (MLP) Architecture1796
```
A standard feed-forward neural network architecture, implemented in the NeuralNetwork1797
class, was utilized. This network consists of sequential layers designed to learn complex1798
patterns from the input features, as depicted in Figure 113.1799
• Structure: The network comprises an input layer taking the selected features,1800
followed by several hidden layers, and a final output layer producing a single value.1801
• Layers: Each hidden layer typically consists of:1802
```
– A fully connected linear layer (nn.Linear) transforming the features from the1803
```
previous layer.1804
```
– An activation function, specifically Leaky Rectified Linear Unit (nn.LeakyReLU)1805
```
with α = 0.05, introducing non-linearity.1806
```
– A batch normalization layer (nn.BatchNorm1d) to stabilize learning and im-1807
```
prove generalization.1808
```
– A dropout layer (nn.Dropout) to prevent overfitting by randomly setting a1809
```
```
fraction of neuron outputs to zero during training (typically with a rate of1810
```
```
0.4-0.5).1811
```
• Configuration: A common configuration uses hidden layers with sizes [1024, 512, 512, 256],1812
though this can vary. The final layer is a single linear unit outputting a logit score.1813
This MLP architecture serves as a robust baseline for tabular data classification.1814
162
0.00 0.05 0.10 0.15 0.20 0.25 0.30
Efficiency
0.0
0.2
0.4
0.6
Significance
B 0→K 0S ν¯ν
BDT2_Bzero2Kshort_v54
DNN2_Bzero2Kshort_v54
```
(a) B0 → K0S ν ¯ν channel (b) B0 → K∗0ν ¯ν channel
```
0.00 0.02 0.04 0.06 0.08 0.10
Absolute Signal Efficiency
0.0
0.2
0.4
0.6
0.8
```
Significance (s / sqrt(s+b))
```
B + →K ∗ + ν¯ν
BDT2_Bplus2KstarPlus_v55
DNN2_Bplus2KstarPlus_v55_D
```
(c) B+ → K∗+ν ¯ν channel
```
```
Figure 112: Comparison of signal significance (S/
```
√
```
S + B) versus signal efficiency for the
```
```
DNN2 classifier and the BDT classifier for the (a) B0 → K0S ν ¯ν, (b) B0 → K∗0ν ¯ν, and (c)
```
B+ → K∗+ν ¯ν decay channels. Update required for B+ → K∗+ν ¯ν.
163
Input Features
```
(input dim)
```
```
Linear(·, 1024)
```
```
LeakyReLU(α=0.05)
```
```
BatchNorm1d(1024)
```
```
Dropout(0.5)
```
```
Linear(1024, 512)
```
```
LeakyReLU(α=0.05)
```
```
BatchNorm1d(512)
```
```
Dropout(0.5)
```
```
Linear(512, 384)
```
```
LeakyReLU(α=0.05)
```
```
BatchNorm1d(384)
```
```
Dropout(0.5)
```
```
Linear(384, 256)
```
```
LeakyReLU(α=0.05)
```
```
BatchNorm1d(256)
```
```
Dropout(0.5)
```
```
Linear(256, 128)
```
```
LeakyReLU(α=0.05)
```
```
BatchNorm1d(128)
```
```
Dropout(0.5)
```
```
Linear(128, 1)
```
```
(Logit
```
```
Output)
```
```
Figure 113: Architecture of the Multi-Layer Perceptron (NeuralNetwork) model with a
```
snake-like layout for compact representation.
Q.3 Transformer Architecture1815
Inspired by successes in sequence modeling and increasingly in other domains, a Transformer-1816
```
based architecture (TransformerClassifier) was adapted for classification, shown schemat-1817
```
ically in Figure 114.1818
• Structure: This model utilizes a Transformer Encoder stack.1819
• Components:1820
```
– An input embedding layer (nn.Linear) projects the input features into a1821
```
```
higher-dimensional space (dmodel).1822
```
```
– A learned positional encoding (nn.Parameter) is added to the embedding,1823
```
```
providing the model with positional information (fixed for this 1D tabular1824
```
```
data adaptation).1825
```
– The core consists of multiple nn.TransformerEncoderLayer instances stacked1826
in an nn.TransformerEncoder. Each layer contains:1827
```
∗ A multi-head self-attention mechanism (nhead) allowing the model to1828
```
weigh the importance of different features.1829
```
∗ Feed-forward networks (dim feedforward).1830
```
```
∗ Layer normalization (norm first=True) and dropout (dropout rate).1831
```
```
∗ GELU or ReLU activation (activation).1832
```
164
– The output sequence from the Transformer Encoder is averaged over the se-1833
```
quence dimension (which is 1 for this input type).1834
```
```
– A final linear layer (nn.Linear) maps the averaged representation to a single1835
```
logit output.1836
• Configuration: Typical hyperparameters include an embedding dimension dmodel =1837
64, nhead = 4 attention heads, num layers = 2 encoder layers, a dropout rate = 0.4,1838
and feed-forward dimension dim feedforward = 512.1839
```
• Initialization: Weights are initialized using Kaiming Normal initialization (kaiming normal )1840
```
suitable for ReLU-like activations.1841
This architecture explores the capability of attention mechanisms to capture feature in-1842
teractions for classification.1843
Q.4 Training Configuration1844
The models were trained using the following configuration:1845
```
• Loss Function: Binary Cross-Entropy with Logits (nn.BCEWithLogitsLoss), suit-1846
```
able for binary classification tasks.1847
```
• Optimizer: AdamW (optim.AdamW), an adaptive learning rate optimization algo-1848
```
```
rithm with weight decay. Typical parameters include a learning rate (lr) of 2-3 ×1849
```
```
10−3 (scaled by batch size multiplier batch mul if used), weight decay (weight decay)1850
```
```
of 5 × 10−4, betas of (0.9, 0.999), and epsilon of 10−8.1851
```
• Learning Rate Scheduler: Two primary schedulers were employed:1852
```
– ReduceLROnPlateau (ReduceLROnPlateau): Reduces the learning rate when1853
```
```
the validation AUC stops improving (e.g., patience = 5-8, factor = 0.6-0.75).1854
```
```
– CosineAnnealingLR (CosineAnnealingLR): Anneals the learning rate following1855
```
```
a cosine curve over a defined period (Tmax = 50 epochs) down to a minimum1856
```
```
(ηmin = 10−6).1857
```
```
The scheduler monitors the validation AUC (val auc) to adjust the learning rate.1858
```
```
• Mixed Precision: Training utilized automatic mixed precision (torch.amp.autocast1859
```
```
and GradScaler) to accelerate computation and reduce memory usage on compati-1860
```
```
ble GPUs (like NVIDIA Ampere) by performing operations in lower precision (e.g.,1861
```
```
float16) where possible.1862
```
```
• Gradient Clipping: Gradient norms were clipped (torch.nn.utils.clip grad norm )1863
```
```
to a maximum value (e.g., 1.0) to prevent exploding gradients and stabilize training.1864
```
165
Input Features
```
(input dim)
```
Linear Embedding
```
(dmodel)
```
- Positional Encoding
Transformer
Encoder
```
(Multi-Head
```
Attention,
Add & Norm,
Feed Forward,
```
Add & Norm)
```
× num layers
Average Pooling
```
(Sequence Di-
```
```
mension)
```
Linear Output
Logit Output
Pos. Enc.
Figure 114: Architecture of the TransformerClassifier model.
166
Q.5 Optimized Data Loading1865
Training deep learning models on large datasets often encounters bottlenecks related to1866
```
transferring data between the CPU (where data loading typically occurs) and the GPU1867
```
```
(where computations happen). To mitigate this, a custom data loading strategy was1868
```
implemented using GPUVRAMDataLoader.1869
```
• Mechanism: The entire training and validation datasets (features X and targets y)1870
```
```
are pre-loaded directly into the GPU’s Video RAM (VRAM) using tensor.cuda().1871
```
```
• Sampling: A custom sampler (GPUVRAMSampler) operates directly on the GPU,1872
```
generating batches of indices pointing to the data already resident in VRAM.1873
• Benefit: This approach bypasses the standard CPU-based data loading pipeline1874
and eliminates the CPU-to-GPU data transfer overhead during training epochs.1875
• Performance: This optimization resulted in a significant reduction in epoch train-1876
ing time, observed to be up to 35 times faster compared to standard CPU-based1877
data loading methods, drastically accelerating the training process.1878
This data handling optimization was crucial for efficiently training the DNN models on1879
the available hardware.1880
167
R Exploration of Lorentz Equivariant Neural Net1881
Event-shape and secondary kinematic features are high-level observables that aim to cap-1882
ture the event topology and kinematics. They are constructed in a predefined way from1883
low-level particle features, such that their distributions and physical meanings are readily1884
understandable. Therefore, they can serve as direct inputs to relatively simple networks1885
such as BDTs for event classification. However, the high-level characteristic of such vari-1886
ables suggests that information may be lost when computing them from low-level particle1887
features. Recent studies in jet classification on LHC benchmark datasets show superior1888
performance of neural nets trained on low-level particle features. For a comprehensive1889
overview of neural nets in high energy physics see [42].1890
Lorentz Equivariant Neural Net1891
In search for the best possible classification performance, besides training boosted decision1892
trees on high level features, we trained neural networks on low level particle features. Our1893
input data corresponds to an unordered set of particles with their four vectors and other1894
scalar properties, such as particle identification probabilities. The number of particles1895
```
per event varies with the number of particles in the ROE. Graph neural nets (GNNs) are1896
```
designed to operate on such a so-called point cloud.1897
Of particular interest are GNNs that respect the physical symmetries of the input1898
data. The classification result should not depend on any particular spatial rotation or1899
Lorentz boost of an event. By encoding these Lorentz group symmetries in a symmetry-1900
preserving neural net, they do not need to be learned from the input data. [43] presents1901
```
a Lorentz equivariant neural net (LEGNN), which outperforms state-of-the-art models in1902
```
jet classification benchmarks. LEGNN achieves Lorentz equivariance by aggregating the1903
input four vectors through Lorentz-equivariant layers into output four vectors. Applying1904
a Lorentz transformation onto the input four vectors of such a layer would transform the1905
embedded output four vectors accordingly. The stacked Lorentz-equivariant layers build a1906
neural network, whose output is mapped onto Lorentz-invariant scalars and decoded into1907
a classification probability. In this way, the network can learn through a deep embedding1908
of four vectors, while respecting the Lorentz group symmetries and produce a Lorentz-1909
invariant classification result.1910
Structure1911
The Lorentz-equivariant embedding of four vectors is based on the universal approxima-1912
tion theorem for Lorentz-equivariant functions:1913
A continuous function ϕ : RN ×4 → R4 is Lorentz-equivariant if and only if1914
1915
```
ϕ(x1, . . . , xN ) =
```
NX
```
i=1
```
```
gi (⟨xi, x1⟩, . . . , ⟨xi, xN ⟩) xi, (9)1916
```
1917
for continuous Lorentz-invariant scalar functions gi and N the number of particles per event.1918
168
Theorem 9 allows to first compute Lorentz-invariant Minkowski products ⟨xi, xj ⟩ of1919
four vectors, which can then enter scalar functions gi to compute attention weights for1920
```
each four vector xi. The functions gi can be modelled by multi-layer perceptrons (MLP).1921
```
This weighting coined Minkowski dot product attention allows to construct a Lorentz1922
group equivariant mapping of four vectors in LEGNN, while relying on basic MLPs and1923
without costly computations of high-order tensors.1924
Figure 115: Structure of the Lorentz equivariant graph neural net presented in [43].
The structure of LEGNN is shown in Figure 115 and consists of multiple consecutive1925
```
so-called Lorentz group equivariant blocks (LGEB) and a decoder. For each Lorentz group1926
```
equivariant block, Minkowski products are computed from all pairs of input four vectors1927
xi. These products and the Lorentz-invariant scalars hi enter an MPL ϕe, which encodes1928
the edge message between particles i and j1929
```
mlij = ϕe
```

```
hi, hj , ψ(||xi − xj ||2), ψ(⟨xi, xj ⟩)
```

,1930
```
where ||...|| denotes the Lorentz-invariant norm and ψ(. . . ) = sgn(. . . ) log(| . . . | + 1) reg-1931
```
ularizes large numbers.1932
Following Theorem 9, all four vectors can be aggregated in a manifestly Lorentz-1933
equivariant way by applying scalar functions onto mij . Formula 10 defines the Minkowski1934
dot product attention, which embeds four vectors from layer l to l+1 Lorentz-equivariantly1935
xl+1i = xli + c
NX
```
j=1
```
```
ϕx(mlij ) · xlj , (10)1936
```
where ϕx is a MLP modeling scalar functions and c a hyperparameter.1937
Similarly, the scalars hi get embedded from layer l to l + 1 by1938
hl+1i = hli + ϕh
"
hli,
NX
```
j=1
```
```
ϕm(mlij )mlij
```
#
,1939
```
with ϕh, ϕm MLPs. ϕm(mlij ) ∈ (0, 1) corresponds to the edge significance from particle j1940
```
to i. Notice that the embedding hl+1i includes information learned from the four vectors xi1941
169
through the message passing mlij . Therefore, it suffices to only decode the scalars hi after1942
the last LGEB L. Average pooling over all particles guarantees permutation invariance1943
in1944
```
hav =
```
1
N
NX
```
i=1
```
hLi .1945
We map hav, BDT2 onto a classification probability using a softmax function following a1946
MLP, which includes dropout to prevent overfitting. Notice that this includes hav learned1947
from low-level particle features, as well as the BDT2 classification value learned from1948
high-level event features.1949
Training1950
We aim to separate signal against background events in a binary classification. We utilize1951
an Adam optimizer and a binary cross entropy loss function with a class weight. The1952
learning rate scheduler follows a cosine annealing scheme with one warm-up epoch. We1953
use 6 consecutive LGEB, followed by a 2 layer decoder with dropout. All hidden layers1954
in all MLPs are of size 72.1955
Due to the structure of basf2 output files, we write out properties of different particles1956
to different trees. Offline, we match B meson candidates with the four-vectors of the1957
particles in the corresponding event. This includes four vectors of final state particles, as1958
well as for intermediate π0, K0S and K∗+. For the scalar particle features, we use 8 types1959
of particle identification probabilities for π, K, γ, e, µ, p, n, 2H+, as well as a flag which1960
takes different values for ROE particles, signal K∗+, π0 and K0S candidates and their final1961
state daughter particles. Training is performed in batches of 1000 events each. Within1962
each batch, the proportions of signal events and events from the different background1963
productions are kept constant.1964
Results1965
Figure 116 compares the classification performance of LEGNN training and BDT2. The1966
left-most figure shows that each network dominates in different regions of the receiver1967
operating curve. LEGNN outperforms BDT2 in the high efficiency region, while BDT21968
outperforms LEGNN in the high background suppression region. This translates into1969
a broader significance curve for LEGNN as a function of signal efficiency with lower1970
maximum. The integrated AUC value is higher for LEGNN1971
```
AUCtestBDT2 = 0.97541972
```
```
AUCtestLEGNN = 0.9793.1973
```
When aiming for maximum significance in a rare decay mode, stronger background sup-1974
pression shows to be more beneficial than higher signal retention.1975
Contrary to jet classification at LHC, low-level particle features and Lorentz equiv-1976
ariance seem to barely bring any extra information over high-level event features. The1977
170
Figure 116: Receiver operating significance curves for BDT2 and Lorentz Equivariant
Graph Neural Net.
constant collision energy at the SuperKEKB lepton collider and the low particle multi-1978
plicities at Belle II seem to allow the engineered high-level event features to capture all1979
information relevant for classification.1980
171