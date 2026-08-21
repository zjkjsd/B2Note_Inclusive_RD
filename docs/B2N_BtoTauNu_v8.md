Belle
BELLE2-NOTE-PH-2025-062
DRAFT Version 7.0
July 10, 2026
Measurement of the branching fraction of B+ → τ +ντ decays
with the semileptonic tagging method at Belle II
Tristan Fillinger,∗ Yinghui Guan,† and Akimasa Ishikawa‡
```
High Energy Accelerator Research Organization (KEK), Tsukuba 305-0801, Japan
```
```
(The Belle II Collaboration)
```
Abstract
In this note we present the measurement of the branching fraction of the decay B+ →
τ +ντ using the semileptonic tagging method at Belle II. This measurement uses a data
sample of 387 million BB meson pairs recorded by the Belle II detector at the SuperKEKB
electron-positron collider between 2019 and 2022.
∗ tristan.fillinger@kek.jp
† yinghui.guan@kek.jp
‡ akimasa.ishikawa@kek.jp
1
CONTENTS
Changelog 5
Analysis software and datasets 11
1. Introduction 13
2. Data samples 16
3. Event selection 17
3.1. Skim 17
3.2. Reconstruction 19
3.3. Pre-selection 21
4. Selection optimization 33
4.1. Background suppression 33
4.2. Signal optimization 44
4.3. Fitting variables before/after optimization 50
5. Corrections 54
5.1. FEI corrections 54
5.2. Extra energy corrections 60
5.3. pCMS corrections 69
6. Data/MC comparison and validation 73
6.1. Embedded sample efficiencies 73
6.2. BDT output checks 76
6.3. Fitting variables after full selection 79
6.3.1. SB control sample 79
6.3.2. Off-resonance data 80
6.3.3. Embedded sample 83
6.3.4. B+ → D∗0ℓ+νℓ control sample 84
6.3.5. Double tagged control sample 88
6.3.6. Blind on-resonance data 89
7. BR extraction 92
7.1. Fitting procedure 92
7.2. Fit validation 96
7.2.1. Toy study 97
7.2.2. Bootstrap study and linearity check 98
2
8. Systematics 100
8.1. ROE corrections 100
8.2. FEI corrections 100
8.3. pCMS corrections 101
8.4. Tracking efficiency 101
8.5. Charged particle identification 101
8.5.1. Corrections and implementation in the fit 101
8.5.2. light-release issue correction 103
8.6. Neutral particle identification 103
8.7. Branching fractions of background decays 103
8.7.1. Main background composition 103
8.7.2. Rare BB background 107
```
8.8. D(∗)ℓνℓ form factors 115
```
8.9. MC statistics 118
8.10. f+− and f00 118
```
8.11. Number of produced Υ (4S) 118
```
8.12. Summary of and impact of the systematics in the fit 118
8.12.1. Method to evaluate the impact 121
8.12.2. Impact of the systematics on the signal strength 121
9. Unblinding procedure 123
9.1. Unblinding steps 123
9.2. Results of the unblinding steps 123
9.2.1. Step 1: µ channel 123
9.2.2. Step 2: e channel 128
9.2.3. Step 3: hadronic channels and blinded POI comparison 132
9.2.4. Step 4: consistency checks on sub-samples 137
10. Results 140
10.1. Fit distributions 140
10.2. Fit results 144
10.3. Branching fraction 145
Appendix 147
A. Event selection, additional material 147
A.a. Additional pre-selection plots 147
A.b. Cumulative pre-selection tables for each channel 148
B. ROE mask optimization 152
B.a. FOM optimization 152
B.b. ROE correction uncertainty 153
3
C. Background suppression, additional plots 154
C.a. Correlations 154
C.b. Variable importance 156
C.c. Data/MC agreement 157
D. Corrections, additional plots 175
D.a. ROE corrections validation with the extra track SB control
sample 175
D.b. BDT sidebands, additional checks 183
D.c. BB ROE correction transferability checks 184
D.d. τpCMS checks 194
E. Post-selection, additional material 196
E.a. Extra track study 196
E.b. Self-crossfeed study 197
F. Fitting, additional plots 201
F.a. MC templates 201
F.b. Correlation matrix 210
F.c. Pulls of individual NPs 211
F.d. Impact of individual NPs 212
G. Unblinding, additional material 216
G.a. Agreement with other measurements 216
G.b. Pulls of individual NPs 217
G.c. Post-fit plots 218
G.d. Post-fit plots: SR cut 222
G.e. Post-fit plots: pvis cut 225
References 231
4
CHANGELOG1
Version 7.02
Unblinding procedure done, BR measured.3
```
• Unblinding and Final result sections updated (see Sections 9 and 10).4
```
• Added additional post-fit checks in Appendix G.5
• Updated the number of NPs used in the fit with the new gathering of eigen-6
vectors in Section 8.7
• Added D0tag corrections for µ mode in Section 5.1.8
• Updated Asimov fit results in Section 7.1.9
Version 6.010
```
• Found a bug in ℓℓXX normalization (assumed 1444 fb−1 instead of 360 fb−1),11
```
updated tables and fit. No major changes in the results.12
• Modified and added more details on the unblinding procedure in Section 9.13
• Add EROEextra checks in low and high BDT sidebands in Appendix D.b.14
Version 5.015
Further RC comments addressed.16
• Updated embedded sample efficiencies using new embedded MC samples.17
```
Added a 11% systematic uncertainty to the signal efficiency (see Section 6.1).18
```
• Use official rare MC samples, updated Section 8.7.2 and fitting results. Num-19
bers are slightly lower than before, but same conclusion applies.20
• Added more details for SCF in Appendix E.b.21
• After checking control samples, added pCMS correction + systematic to signal22
sample, updated fit.23
5
• Re-ran the ROE mask optimization, taking into account data/MC discrepancy24
```
and the uncertainty of the ROE corrections. No improvement was found (see25
```
```
Appendix B).26
```
Version 4.027
Further RC comments addressed.28
• ROE correction transferability checks. For signal weights, now using the con-29
```
trol samples (B+ → D∗0ℓ+νℓ and double tagged) instead of the extra track30
```
sample. For BB background, now using BDT sideband instead of the extra31
```
track sample. Updated all related sections and plots (see Sections 5.2, 6.3.432
```
```
and 6.3.5 and appendix D.c).33
```
• Increase SCF shape syst to a conservative 10% value, update the fit results.34
• Added impact of each NPs in Appendix F.d.35
Ongoing changes for next version:36
```
• Use official rare MC samples (we found out only exp7 was skimmed. The37
```
```
experts are looking to fix the issue in the workflow and reprocess the files).38
```
Version 3.039
Latest RC comments addressed.40
• Added Appendix E with extra track and SCF studies.41
```
• Updated Xuℓν and other BR in the systematic uncertainties (see Section 8.7.1).42
```
• Added SCF shape systematic.43
• Update fit results in Section 7.2.44
• Update B+ → D∗0ℓ+νℓ control channel checks using the new BDT and correc-45
```
tions (see Section 6.3.4).46
```
```
• Update double tagged sample (SL FEI + hadronic FEI) using the new BDT47
```
```
and corrections (see Section 6.3.5).48
```
6
• Update tables in Appendix A.b with the correct FEI reconstruction efficiency.49
• Fixed typos / made more clarifications on multiple sections based on additional50
RC reviewers comments.51
Version pre3.0-252
Feb B2GM plenary version.53
• Update fit results and new systematics.54
Version pre3.0-155
Post WGR, addressing RC reviewers comments.56
```
• Double tagged sample (SL FEI + hadronic FEI) checks for hadronic channels57
```
```
(see Section 6.3.5).58
```
• Added Section 4.3 to see the signal distribution shape on the fit variables.59
• Removed 2 least important features from leptonic BDT, updated everything60
```
accordingly (see Section 4.1).61
```
```
• The extra track sample is now used for ROE corrections (see Section 5.2).62
```
• The FEI calibration factors are now applied to only correctly reconstructed63
```
Btag (see Section 5.1).64
```
• Update Figure 64 with more points.65
• Made NPs distribution Figure 75 readable.66
• Added pull plot of all NPs on Asimov datasets in Appendix F.c.67
• Fixed typos / made more clarifications on multiple sections based on RC re-68
viewers comments.69
Version 2.070
Post FSR, addressing WG reviewers and additional comments.71
72
Major changes since last version:73
7
• Removed Btag decay mode from BDT variables in Section 4.1. Updated ev-74
erything post-BDT accordingly.75
• Corrections are now done after the BDT. The BDT sidebands is now used for76
```
ROE and τpCMS (see Sections 5.1 and 5.2). The FEI calibration factors are77
```
```
now used correctly, and continuum is corrected using off-resonance data (see78
```
```
Section 5.1). Updated all related sections and plots.79
```
```
• Fit is now using sysvar for all the correction calculations (see Section 8).80
```
Updated all plots and tables with the new fit settings and results.81
Minor changes since last version:82
• Added additional plots for τ +τ − background pre-selection cuts in Appendix A.a.83
• Increased NP kept in the fit for BF systematics in Section 8.7.1.84
• Rare background calculation was updated in Section 8.7.2. Also removed the85
added rare background from generic MC.86
• Updated Figure 2 with the latest |Vub| exclusive value updated.87
• Checked: removing ρ channel doesn’t increases significance.88
• Fixed typos and added more explanations when relevant.89
Version 1.490
Note version for the FSR. Continue replying to WG conveners comments.91
• Added B+ → D∗0ℓ+νℓ FF systematic uncertainty in Section 8.8.92
• Updated wrongly scaled Table 7 and in Appendix A.b.93
• Updated PID systematic uncertainty taking into account the light-release issue94
in Section 8.5.2.95
• Updated fit results with data/MC scaling from blind on-resonance data in96
Section 6.3.6.97
Version 1.398
Replying to WG conveners comments.99
8
• Clarified Btag BCS selection in Section 3.1.100
• Clarified ROE mask notation in Section 3.2.101
• Updated yrange of plots in Section 6.3.3.102
• Added Figure 65 showing the πID efficiency correction.103
• Changed uncertainties in Tables 20 and 21.104
• Better explanations of K0LK0Lℓν BF in Section 8.7.2.105
• Updated in Tables 22 and 23 the expected yields.106
• Added Figure 72 showing the fit variables distribution for rare BB decays.107
Version 1.2108
Stable version, send to the WG for comments.109
• Removed D1st daughterdr variable from BDT, updated everything accordingly.110
• Fit:111
```
– All NPs now split into norm+shape (normsys+histosys).112
```
– Added rare BB decays section and added a new template in the fit.113
– Signal and SCF templates now taken from signal-only sample.114
– EROEextra corrections applied to signal, τpCMS corrections removed from signal.115
– Complete list of systematic uncertainties.116
Version 1.1117
Addressing Ishikawa-san’s comments from the last version.118
119
Major changes since last version:120
• Added D ∗ ℓν control sample study.121
• Removed irrelevant sigProb cuts, updated the syst corrections accordingly.122
• Added blind on-resonance data checks.123
9
• Updated fit checks.124
Minor changes since last version:125
• Updated B and fB values.126
• Updated luminosity numbers and introduction section.127
• Harmonized the notation of τpCMS .128
• BDT variables explained.129
• Fixed typos, added more text when relevant.130
Version 1.0131
• Initial version with all sections filled.132
10
ANALYSIS SOFTWARE AND DATASETS133
The ntuples, produced with the basf2 [1] release light-2506-deimos, are kept134
on KEKCC at the following path:135
/gpfs/group/belle/users/tfilling/b2tv/grid/merged/
The gitlab repository of the analysis is located at the following path:136
```
https://gitlab.desy.de/tristan.fillinger/b2taunu/
```
The document server repository of the analysis is located at the following path:137
```
https://docs.belle2.org/pub data/analyses/SLME-016/
```
Code dependencies:138
• plothist>=1.2.6 [2]139
• awkward==2.6.6140
• b2luigi==1.2.2141
• boost-histogram==1.4.0142
• cabinetry @ git+https://github.com/MoAly98/cabinetry@5d441aacb35705c143
5028ed198d17813fb160ca252144
• matplotlib==3.8.4145
• numpy==1.26.0146
• optuna==3.6.1147
• pandas==2.0.3148
• paramiko==3.2.0149
• particle==0.25.3150
• psutil==5.9.0151
• pyarrow==11.0.0152
• pyhf[minuit]==0.7.2153
11
• PyYAML==6.0154
• scikit-learn==1.5.2155
• scikit-optimize==0.10.2156
• scipy==1.12.0157
• scp==0.14.5158
• seaborn==0.13.2159
• tabulate==0.8.9160
• uncertainties==3.1.6161
• uproot==5.3.10162
• xgboost==2.0.0163
• zfit==0.24.3164
• prek==0.1.6165
• awkward-pandas==2023.8.0166
• jax==0.4.13167
• jaxlib==0.4.13168
• numexpr==2.8.4169
• iminuit==2.24.0170
• shap==0.48.0171
• tensorflow==2.18172
12
1. INTRODUCTION173
```
In this paper, we present the Branching Fraction (BF) measurement of B+ → τ +ντ174
```
```
decays, a rare process in the Standard Model (SM) with a theoretical branching175
```
```
fraction of B(B+ → τ +ντ ) = (0.80 ± 0.06) × 10−4 [3]. This measurement uses a data176
```
sample of 387 million BB meson pairs recorded by the Belle II detector at the177
SuperKEKB electron-positron collider between 2019 and 2022. It corresponds to a178
```
luminosity of (365.4 ± 1.7) fb−1 of on-resonance data, corresponding to a number of179
```
```
produced Υ (4S) estimated to be nΥ (4S) = (387±6)×106, and 42 fb−1 of off-resonance180
```
```
data, where the energy is around 60 MeV below the Υ (4S) resonance peak.181
```
Two scenarios can arise with the B+ → τ +ντ decay: a measurement of the SM182
```
with better precision or the discovery of New Physics (NP).183
```
FIG. 1. Feynman diagram of the B+ → τ +ντ decay.
The branching fraction of B+ → τ +ντ can be expressed as:184
B
 
B+ → τ +ντ

=
G2F mB m2τ
8π

1 −
m2τ
m2B
2
```
f 2B |Vub|2 τB , (1)
```
with the values of the input parameters used in the calculation of the branching185
fraction of B+ → τ +ντ decays are shown in Table 1.186
The BF is sensitive to the CKM matrix element |Vub|, which is usually measured187
with B → πlν decays [6]. The inclusive and exclusive central values of |Vub| have a188
slight disagreement. Measuring the BF of B+ → τ +ντ decays with better precision189
can help to clarify this discrepancy and get a better uncertainty on |Vub|.190
In addition, the B+ → τ +ντ decay is a good probe to search NP effects. The191
W boson in Figure 1 can be replaced by a charged Higgs boson in the Two-Higgs-192
```
Doublet Model (2HDM) [7] or various super-symmetric extensions of the SMs. The193
```
NP effects can be parameterized by the ratios [8]:194
Rps ∝
```
B (B+ → τ +ντ )
```
```
B (B → πlν)
```
```
= (0.539 ± 0.043) · |1 + rNP|2 , (2)
```
and195
13
Value Relative
Uncertainty
GF 11.7 TeV−2 5 · 10−7
τB 1.64 ps 2 · 10−3
mB 5.28 GeV 1 · 10−5
mτ 1.78 GeV 5 · 10−5
mµ 105 MeV 2 · 10−8
fB 190.0 MeV 1 · 10−2
|Vub|inc 4.13 · 10−3 6 · 10−2
|Vub|exc 3.70 · 10−3 4 · 10−2
|Vub|avg 3.82 · 10−3 5 · 10−2
TABLE 1. Parameters used in the calculation of the branching fraction of B+ → τ +ντ
decays [4, 5].
```
Rpl =
```
```
B (B+ → τ +ντ )
```
```
B (B+ → µ+ντ )
```
```
= 222 · |1 + rNP|2 , (3)
```
where rNP is a combination of Wilson coefficients sensitive to the NP contribution.196
With the full Belle II dataset, we can expect to search for a NP contribution to197
```
B+ → τ +ντ decays with a sensitivity of rNP > O(0.1) at 95% confidence level.198
```
199
Past measurements of the BF of B+ → τ +ντ decays have been performed by the200
Belle and BaBar collaborations using two approaches: with a semileptonic tag [9, 10]201
and with a hadronic tag [11, 12]. The semileptonic tag method has the advantage of a202
larger branching fraction, but it is more challenging due to the presence of neutrinos203
in the final state. In 2025, Belle II also measured the BF with a fully reconstructed204
tag [13]. All the different measurements are shown Figure 2. The current PDG205
average is compatible within 1σ with the SM prediction [4]. There are currently no206
5 σ observations of the B+ → τ +ντ decay, only evidence at the level of ≈ 3σ.207
14
FIG. 2. Summary of the measurements of the branching fraction of B+ → τ +ντ decays [13].
15
2. DATA SAMPLES208
This analysis uses:209
```
• Monte Carlo (MC) samples:210
```
```
– Signal: 50M B+ → τ +ντ signal only: a Υ (4S) decaying to B+ →211
```
τ +ντ and an additional B± that decays generically. This corresponds212
```
to ≈ 400 ab−1 of signal MC (MC15rd).213
```
```
– Generic: 1444 fb−1 BB background (MC15rd)214
```
```
– non-BB: 1444 fb−1 continuum (qq) and τ +τ −, and 361 fb−1 of ℓℓXX215
```
```
backgrounds (MC15rd)216
```
Control samples:217
```
∗ Off-resonance: 170 fb−1 off-resonance (qq and τ +τ −) (MC15rd)218
```
```
∗ Sidebands (SB) Signal: 50M B+ → τ +ντ signal only with at least219
```
one track in the rest of event220
∗ SB Generic: 1444 fb−1 BB background with at least one track in221
the rest of event222
```
∗ SB Continuum: 1444 fb−1 continuum (qq) and τ +τ −, and 361 fb−1223
```
of ℓℓXX backgrounds with at least one track in the rest of event224
```
(MC15rd)225
```
• Data samples:226
```
– On-resonance: 385 fb−1 on-resonance data (LS1 dataset)227
```
```
– Off-resonance: 42 fb−1 off-resonance data (LS1 dataset)228
```
Control samples:229
∗ SB On-resonance: 385 fb−1 on-resonance data with at least one230
```
track in the rest of event (LS1 dataset)231
```
∗ SB Off-resonance: 42 fb−1 off-resonance data with at least one232
```
track in the rest of event (LS1 dataset)233
```
∗ Embedded signal: ≈ 200 candidates of embedded B+ → τ +ντ234
```
events (see Section 6.1)235
```
16
3. EVENT SELECTION236
This section describes the reconstruction and the pre-selection of the B+ → τ +ντ237
```
candidates. The reconstruction is done using the Full-Event Interpretation (FEI)238
```
Skim, and the pre-selection is done using a set of loose cuts on the reconstructed239
candidates.240
3.1. Skim241
```
This analysis uses the semileptonic (SL) Full-Event Interpretation (FEI) Skim [14].242
```
One of the B± in the decay is reconstructed as one of the following modes shown in243
Tables 2 and 3.244
Mode ID Decay mode
0 B+SL → D0e+νe
1 B+SL → D0µ+νµ
2 B+SL → D0∗e+νe
3 B+SL → D0∗µ+νµ
4 B+SL → D−π+e+νe
5 B+SL → D−π+µ+νµ
6 B+SL → D−∗π+e+νe
7 B+SL → D−∗π+µ+νµ
```
TABLE 2. SL FEI Skim modes and their corresponding Mode ID. The D(∗) is reconstructed
```
in hadronic modes only.
The D is only reconstructed with hadronic modes, so only one neutrino is present245
in this B± decay. This correctly SL tagged B± is called Btag. The rest of the event246
can be analyzed to reconstruct our signal event B+ → τ +ντ , called Bsig. In the FEI247
Skim, the events are already filtered imposing very loose selection requirements on248
the quality of tracks and clusters and their multiplicities. Additionally, this set of249
cut is applied to the Btag:250
• −4 < cos θ∗B,Dl < 3,251
```
• log10(signal probability) > −2.4,252
```
```
• pCMSl > 1.0 GeV (in center-of-mass (CMS) frame).253
```
17
Mode ID D0 decay D+ decay D∗0 decay D∗+ decay
0 K−π+ K−π+π+ D0π0 D0π+
1 K−π+π0 K−π+π+π0 D0γ D+π0
2 K−π+π0π0 K−K+π+ D+γ
3 K−π+π+π− K−K+π+π0
4 K−π+π+π−π0 π+π0
5 π−π+ π+π+π−
6 π−π+π+π− π+π+π−π0
7 π−π+π0 K0S π+
8 π−π+π0π0 K0S π+π0
9 K0S π0 K0S π+π+π−
10 K0S π+π− K+K0S K0S
11 K0S π+π−π0
12 K−K+
13 K−K+π0
14 K−K+K0S
TABLE 3. Charm meson decay modes and their corresponding Mode ID. The D0 and D+
are reconstructed in hadronic modes only, while the D∗0 and D∗+ are reconstructed from
their charm-meson daughters.
If multiple Btag are found in the event, the one with the highest signal probability254
is selected as the Btag, and the rest are discarded. No multiple candidate remain255
after this selection.256
```
In addition, the Rest of Event (ROE) of the Btag is reconstructed using the remain-257
```
ing tracks and clusters that doesn’t belong to it. Continuum suppression variables258
are calculated in the CMS using a standard set of cuts on the tracks and clusters in259
```
the ROE recommended by the FEI Task Force (see ref):260
```
• Track cut: dr < 0.5 cm, |dz | < 2 cm, pt > 0.2 GeV/c and in the CDC261
acceptance.262
```
• ECL cut: (Ecluster > 0.08 GeV in the forward region or Ecluster > 0.03 GeV263
```
```
in the barrel region or Ecluster > 0.06 in the backward region), clusterNHits264
```
> 1.5, |clusterTiming| < 200 ns and in ECL acceptance.265
Finally, a cut on cos θthrust, Bsig, ROE < 0.9 is applied.266
18
3.2. Reconstruction267
The Bsig is reconstructed with the remaining tracks and clusters in the event.268
Only the one-prong decays of the τ are reconstructed. This accounts for around 72%269
```
of the τ decays (see Table 4).270
```
τ decay Branching fraction
µνν 17%
eνν 18%
πν 11%
```
(ρ → ππ0)ν 26%
```
Total BF 72%
TABLE 4. Branching fractions of the τ decays.
The τ decay modes are reconstructed as follows:271
• µ channel: the tracks that satisfy the leptonid Moriond2023 Official rel6 v0b272
standard muon requirements for FixedThresh09 selection with global likelihood273
are selected. Then a standard set of cut is applied on the muon candidates:274
they must be in the CDC acceptance and have dr < 0.5 cm, |dz | < 2 cm,275
pt > 0.1 GeV/c and E < 5.5 GeV.276
• e channel: The tracks that satisfy the leptonid Moriond2023 Official rel6 v0b277
standard electron requirements for FixedThresh09 selection with global BDT278
are selected. On data, we apply the tracking momentumScaleFactor global279
scaling factor to each track candidate. We then apply the Belle-like bremsstrahlung280
correction to the electrons. Finally, the candidates must pass the same stan-281
dard set of cut as the muons.282
• π channel: the pion candidates must also follow the same set of cuts as for the283
electrons or muons, and we also require that they have a pionID noSVD > 0.6. If284
we run on data, we apply the tracking momentumScaleFactor global scaling285
factor to each track candidate.286
• ρ channel: a ρ candidate is reconstructed by combining a pion candidate with287
a π0 candidate. For the pion candidate, the same list created for the pion chan-288
nel is used. The π0 candidate is reconstructed using the pi0:eff40 May2020289
requirements. If running on data, the energies of the photons are corrected290
19
using the291
PhotonEnergyBiasCorrection MC15rd June2023 table. The photons are292
combined to form a π0 candidate if they have 0.120 < M < 0.145 GeV/c2.293
The τ candidate is then formed by combining the pion and the π0 candidates294
if they are around the ρ mass 0.625 < M < 0.925 GeV/c2.295
The Bsig is reconstructed with a single τ using the four channels described above.296
Additionally, a ROE of the Bsig is reconstructed using the remaining tracks and297
clusters that doesn’t belong to it. Continuum suppression variables are calculated in298
```
the CMS using a common set of cuts on the tracks and clusters in the ROE (ref):299
```
• Track cut: pCMS ≤ 3.2 GeV/c.300
• ECL cut: E ≥ 0.05 GeV/c and ECMS ≤ 3.2 GeV/c.301
Once the Bsig and the Btag are reconstructed, they are combined together to form302
```
a Υ (4S). If multiple candidates are found for the Bsig, the following criteria are used303
```
to select the best candidate:304
• µ channel: the candidate with the highest muonID noSVD is selected.305
• e channel: the candidate with the highest pidChargedBDTScore e is selected.306
• π channel: the candidate with the highest pionID noSVD is selected.307
• ρ channel: the candidate which has a mass closest to the nominal ρ mass is308
selected309
```
In some events, two Υ (4S) candidates remain. For 99.3% of the case, it’s between310
```
π and ρ channels. For 0.5% of the case, it’s between µ and π channels, and for 0.1%311
of the case between e and ρ channel. We select at random one of the two candidates.312
This happens in around 5% for the signal events.313
```
Only one Υ (4S) candidate remains after this selection. We then reconstruct the314
```
```
ROE of the Υ (4S) by all the remaining tracks and clusters that doesn’t belong to315
```
B+ → τ +ντ or the Btag. To remove most of the background without losing signal316
efficiency, we clean the ROE using the following criteria:317
• No extra tracks coming from the IP:318
```
– nTracks in ROE with (dr < 0.5 cm, |dz | < 2 cm, in CDC acceptance319
```
```
) = 0.320
```
• No neutrals in the ROE:321
20
```
– Number of K0S in ROE = 0; with standard K0S :merged list.322
```
```
– Number of Λ0 in ROE = 0; with standard Λ0:merged list.323
```
```
– Number of π0 in ROE = 0; with pi0:eff20 May2020 list.324
```
The first cut removes more than 99% of the expected background if no cut on the325
tracks of the ROE is applied. The second set of cuts further reduces the background326
by 82% on the remaining candidates after the first cut, while only losing 7% on the327
signal efficiency.328
In addition, we also have a control sample, referred as Extra track SB, where the329
no extra track cut is inverted to select events with at least one extra track in the330
```
ROE (nTracks in ROE > 0). No significant signal is expected in this sample, and it331
```
is used to get some of the corrections in Section 5.332
```
The event shape variables for the Υ (4S) are calculated in the CMS using the333
```
photons that are in the ECL acceptance, have E > 0.05 GeV, minC2TDist > 20 cm,334
|cluster timing/error| < 2.0 and |cluster timing| < 200 ns, and the pions that335
are in the CDC acceptance, have dr < 0.5 cm, |dz | < 2.0 cm, pt > 0.1 GeV/c and336
E < 5.5.337
```
The energy of the ROE EROEextra (often seen as EROEextra c2 bbS 32 in the plots) used338
```
as one of our final fitting variable is using photons that follows:339
• Energy cut: Ecluster > 0.100 GeV in the forward region or Ecluster > 0.055 GeV340
in the barrel region or Ecluster > 0.080 in the backward region341
• Additional cut: minC2TDist > 30 cm and beamBackgroundSuppression >342
0.15.343
The photons in data are corrected using the344
PhotonEnergyBiasCorrection MC15rd June2023 table. The signal is peaking at 0345
while the different backgrounds follow a Gaussian around ≈ 2 − 3 GeV, except for346
```
the τ +τ − and ℓℓXX backgrounds which also peak at 0 (see Section 3.3 on how347
```
```
it has been removed). The values of the additional cut have been optimized, see348
```
```
Appendix B. In the rest of the note, the signal region (SR) is defined as EROEextra < 0.2349
```
GeV, corresponding to the first two bins of the EROEextra distribution.350
The reconstruction efficiency on the signal is calculated using the B+ → τ +ντ351
signal only sample of 50M events. We find an efficiency of 0.6000 ± 0.0011%. For352
the background, we use the BB generic sample of 1444 fb−1.353
3.3. Pre-selection354
A small set of loose cuts is applied on the B candidates to further reduce back-355
ground without losing signal efficiency. Some pre-selection cuts are motivated by the356
21
```
old B+ → τ +ντ Belle analysis [9]. The selected variables are (see Figure 3 to see the357
```
```
distributions):358
```
```
• Btag decays: the decay mode of the Btag (see Table 2). All the D−(∗)π+ℓ+νℓ359
```
modes are removed as these modes have low statistics and the calibration360
```
factors are not reliable (see Figure 3(a)).361
```
```
• τpCMS : the CMS momentum of the τ (e.g. of the µ, e, π or ππ0) in the Bsig362
```
```
to reduce miss-reconstructed Bsig candidates (see Figure 3(b)). A loose cut363
```
inspired from the Belle analysis [9] is applied.364
• p∗D,tag: the CMS momentum of the D in the Btag to further reduce miss-365
```
reconstructed Btag candidates (see Figure 3(c)). A loose cut inspired from366
```
the Belle analysis [9] is applied.367
• cos θ∗B,Dl : the cosine of the angle in CMS between the Dl system and the Btag.368
If only a mass-less particle like a neutrino is missing in the reconstruction, it369
```
is expected to have a value between -1 and 1 (see Figure 3(d)). A loose cut370
```
inspired from the Belle analysis [9] is applied.371
```
• R2 based on ROE of Υ (4S): the second Fox-Wolfram moment, using the ROE372
```
```
of the Υ (4S) (event shape), to reduce the background from τ +τ − and ℓℓXX373
```
```
events, which is peaking in the signal region (see Figures 3(e) and 4(a)). The374
```
value of the cut has been optimized to remove as much τ +τ − background as375
possible while keeping a high signal efficiency.376
• Btag R2: the second Fox-Wolfram moment of the Btag, using the ROE of the377
```
Btag, (continuum suppression, see here the difference with above), to further378
```
```
reduce the background from τ +τ − and ℓℓXX events (see Figures 3(f) and 4(b)).379
```
The value of the cut has been optimized to remove as much τ +τ − background380
as possible while keeping a high signal efficiency.381
• cos θthurst,Btag,z : the cosine of the angle between the thrust axis of the Btag and382
the z axis to remove a peaking structure seen in data and not modeled in the383
```
MC (see Figures 3(g) and 5) 1. The value of the cut has been optimized to384
```
remove the peaking structure while keeping a high signal efficiency.385
1 In all the data/MC comparison plots, the MC normalization is first scaled using the luminosity
ratio with data. Then, to compare the shape of the distributions, the ratio of the number of
entries between MC and data is computed, and the MC is rescale accordingly. If used, the ratio
used is displayed in the y-label of the bottom panel.
22
Furthermore, τ channel specific pre-selection cuts are applied to the B candidates.386
For the hadronic channels, a tighter cut on pBsig = τpCMS is applied. This cut387
```
greatly reduces the background (see Figures 6(a) and 6(b)), which will help the388
```
BDT to focus on the remaining background candidates without using momentum389
```
information as features (see Section 4).390
```
23
0 2 4 6 8
Btag decays
0.0
0.5
1.0
1.5
Candidates
×105 Belle II preliminary simulationXX
ττcc
ssdd
uuB0B0
B+B−49M Signal
```
(a)
```
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0
1
2
3
4
Candidates
×104 Belle II preliminary simulation
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(b)
```
0.0 0.5 1.0 1.5 2.0 2.5 3.0
Dtag pCMS
0
2000
4000
6000
8000
Candidates
Belle II preliminary simulation
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(c)
```
3 2 1 0 1
cos θ ∗Btag, Dl
0
1000
2000
3000
4000
5000
6000
Candidates
Belle II preliminary simulation
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(d)
```
0.2 0.4 0.6 0.8 1.0
```
R2 (Fox-Wolfram event based)
```
0
2000
4000
6000
8000
Candidates
Belle II preliminary simulation
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(e)
```
0.0 0.2 0.4 0.6 0.8 1.0
Btag R2
0
2000
4000
6000
8000
Candidates
Belle II preliminary simulation
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(f)
```
0.2 0.4 0.6 0.8
Btag cosTBz
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary simulation
```
(g)
```
FIG. 3. Distributions of the pre-selection variables before the cut is applied. They gray
area represents the discarded region. Each variable is shown after the previous pre-selection
cuts have been applied.
24
0.2 0.4 0.6 0.8 1.0
```
R2 (Fox-Wolfram event based)
```
0
1
2
3
Event density
Belle II preliminary simulation
B+B−B0B0
qqττ
XX49M Signal
```
(a)
```
0.0 0.2 0.4 0.6 0.8 1.0
Btag R2
0
1
2
3
4
Event density
Belle II preliminary simulation
B+B−B0B0
qqττ
XX49M Signal
```
(b)
```
FIG. 4. Showing the τ +τ − background in the R2 and Bsig R2 variables. The pre-selection
cut on both variables removes the peaking structure.
25
0
50
100
150
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.29 × MC
```
(a)
```
0
25
50
75
100
125
150
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.36 × MC
```
(b)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.73 × MC
```
(c)
```
0
50
100
150
200
Candidates
Belle II preliminary L dt = 365 fb-1channel
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.32 × MC
```
(d)
```
```
FIG. 5. Distributions of the pre-selection cuts for the cos θthurst,Btag,z variable for the µ (a),
```
```
e (b), π (c) and ρ (d) events in a signal enriched region. We can see a peaking structure
```
in data that is not modeled in the MC. The structure is removed by the pre-selection cut.
26
1 2 3 4
Bsig p
0
500
1000
1500
2000
2500
3000
Candidates
Belle II preliminary simulationchannel
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(a)
```
1 2 3 4
Bsig p
0
500
1000
1500
2000
Candidates
Belle II preliminary simulationchannel
XXττ
ccss
dduu
B0B0B+B−
49M Signal
```
(b)
```
```
FIG. 6. Distributions of the pre-selection cuts for the pBsig variable for only the π (a) and
```
```
ρ (b) events. The Gray area represents the discarded region.
```
27
For the e channel, a peaking structure in the signal region from τ +τ − backgrounds391
remains after applying all the cuts above. This background is coming from ISR/FSR392
photons converting into e+e− pairs, which are then wrongly reconstructed as particles393
from the Btag or the electron from the Bsig. To remove it, we apply a set of cuts394
using tag-side final state particle information:395
• Ktag electronID: an electron from the ISR/FSR photon conversion can be396
wrongly reconstructed as a kaon by the FEI. By cutting on the electronID, we397
can remove 49.7 ± 2.3% of the τ +τ − background while keeping 96.18 ± 0.21% of398
```
the signal events (see Figure 7(a)). If multiple kaons are present, we take the399
```
kaon with the highest electronID. If the Btag does not have a kaon, the event400
is not impacted by the cut.401
```
• Converted γ InvM(ℓtag − esig): the invariant mass of the ℓtag-esig system as402
```
defined in this presentation assuming it’s a converted photon. If the system is403
from ISR/FSR photon conversion, the invariant mass is expected to be 0. This404
cut removes an additional 44.0 ± 3.2% of the τ +τ − background while keeping405
```
98.64 ± 0.13% of the signal events (see Figure 8(a)). If the charge of the two406
```
particles is not opposite, the event is not impacted by the cut.407
```
• Converted γ InvM(Dtag, daughters − esig): for each daughter of the Dtag, the408
```
invariant mass of the Dtag, daughter-esig system, assuming it’s a converted photon,409
is calculated. Then, the minimum of these invariant masses is taken as the value410
for the B candidate. If the system is from ISR/FSR photon conversion, the411
invariant mass is expected to be 0. This cut removes an additional 72 ± 4%412
```
of the τ +τ − background while keeping 96.40 ± 0.21% of the signal events (see413
```
```
Figure 8(b)). If the charge of the two particles is not opposite, the event is not414
```
impacted by the cut.415
These three cuts are applied only on the e channel and remove 92.1 ± 1.2% of the416
τ +τ − background. With the addition of the pre-selection cuts, 99.20 ± 0.01% of the417
τ +τ − background is removed.418
28
0.0 0.2 0.4 0.6 0.8 1.0
KtagelectronID
0
10
20
30
40
Event density
Belle II preliminary simulation
B+B−B0B0
qqττ
XX49M Signal
```
(a)
```
FIG. 7. Distributions of the Ktag electronID variable for only the e events after applying
the pBsig cut. τ +τ − and ℓℓXX events are peaking at 1, while the signal is peaking at 0.
0.0 0.5 1.0 1.5 2.0
```
conv. γ InvM(`tag - esig)
```
0
100
200
300
400
Candidates
Belle II preliminary simulatione channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.1
```
(a)
```
0.0 0.2 0.4 0.6 0.8 1.0
```
conv. γ InvM(Dtag, daughters - esig)
```
0
200
400
600
Candidates
Belle II preliminary simulatione channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.1
```
(b)
```
```
FIG. 8. Distributions of the converted γ InvM(ℓtag − esig) (a) and converted γ
```
```
InvM(Dtag, daughters − esig) (b) variables for only the e events after applying the
```
Ktag electronID cut. τ +τ − and ℓℓXX events are peaking at 0, while the signal is flat.
The pre-selection cuts values are shown in Table 5, the signal efficiency and back-419
ground retention are shown in Table 6. The cumulative version of this table, with the420
number of signal and background candidate, is shown in Table 7. The cumulative421
tables for each individual channel are shown in Appendix A.b.422
29
Channel Cut value
All Btag decay mode ID < 4
All p∗τ,sig > 0.4 GeV/c
All p∗Dtag < 2.5 GeV/c
All −3 < cos θ∗B,Dl < 1.5
```
All R2(Event based) < 0.45
```
All Btag R2 < 0.45
All cos θthurst,Btag,z < 0.85
For π channel: pBsig > 1. GeV/c
For ρ channel: pBsig > 1. GeV/c
For e channel: Ktag electronID < 0.2
```
For e channel: conv. γ InvM(ℓtag − esig) > 0.02 GeV/c2
```
```
For e channel: conv. γ InvM(Dtag, daughters − esig) > 0.02 GeV/c2
```
TABLE 5. Pre-selection cuts values.
30
Cut Sgn. eff. [%] Bkg. ret. [%] FOM
```
Reconstruction (w/ FEI) 0.6138 ± 0.0011 - -
```
Btag decay mode ID 94.61 ± 0.04 87.092 ± 0.027 0.85
p∗τ,sig 94.65 ± 0.04 85.547 ± 0.030 0.87
p∗Dtag 99.870 ± 0.007 81.09 ± 0.04 0.96
cos θ∗B,Dl 97.237 ± 0.031 69.95 ± 0.05 1.12
```
R2(Event based) 84.02 ± 0.07 68.93 ± 0.06 1.13
```
Btag R2 99.358 ± 0.017 98.202 ± 0.020 1.14
cos θthurst,Btag,z 92.10 ± 0.06 83.22 ± 0.06 1.15
For π channel: pBsig ∗92.31 ± 0.13 ∗40.72 ± 0.15 ∗0.69
For ρ channel: pBsig ∗90.07 ± 0.19 ∗52.53 ± 0.17 ∗0.34
For e channel: Ktag electronID ∗96.04 ± 0.08 ∗95.03 ± 0.07 ∗0.73
```
For e channel: conv. γ InvM(ℓtag − esig) ∗98.66 ± 0.05 ∗98.70 ± 0.04 ∗0.73
```
```
For e channel: conv. γ InvM(Dtag, daughters − esig) ∗96.71 ± 0.07 ∗96.78 ± 0.06 ∗0.71
```
Total pre-selection 0.3879 ± 0.0009 16.648 ± 0.030 1.30
TABLE 6. Pre-selection cuts efficiency, calculated on the 50M signal only sample, and
```
background retention, obtained on the 1444 fb−1 MC sample. The Figure Of Merit (FOM)
```
is calculated as the ratio of the signal efficiency and the square root of the background
retention. The values with a star only apply to the specific τ channel.
31
Cut #Sgn. Sgn. eff. cumul [%] #Bkg Bkg. ret. cumul [%]
```
Reconstruction (w/ FEI) 263 0.6138 ± 0.0011 389385 -
```
Btag decay mode ID 249 0.581 ± 0.009 339121 87.09 ± 0.05
p∗τ,sig 235 0.550 ± 0.012 290106 74.50 ± 0.07
p∗Dtag 235 0.549 ± 0.012 235248 60.42 ± 0.08
cos θ∗B,Dl 228 0.534 ± 0.013 164545 42.26 ± 0.08
```
R2(Event based) 192 0.448 ± 0.017 113415 29.13 ± 0.07
```
Btag R2 191 0.446 ± 0.017 111377 28.60 ± 0.07
cos θthurst,Btag,z 176 0.410 ± 0.018 92686 23.80 ± 0.07
π channel: pBsig 173 0.403 ± 0.018 77179 19.82 ± 0.06
ρ channel: pBsig 171 0.399 ± 0.018 66857 17.17 ± 0.06
e channel: Ktag electronID 168 0.394 ± 0.018 65762 16.89 ± 0.06
```
e channel: conv. γ InvM(ℓtag − esig) 168 0.392 ± 0.018 65490 16.82 ± 0.06
```
```
e channel: conv. γ InvM(Dtag, daughters − esig) 166 0.388 ± 0.018 64824 16.65 ± 0.06
```
TABLE 7. Cumulative signal efficiency and background retention after each pre-selection
cut. The number of truth-matched signal candidates and the number of background can-
didates is obtained on the 1444 fb−1 MC sample and has been scaled expected LS1 data
luminosity.
32
4. SELECTION OPTIMIZATION423
To optimize the signal-to-background ratio, the following steps are taken:424
```
• Background suppression: Training of a BDT to suppress the background (Sec-425
```
```
tion 4.1).426
```
• Signal optimization: Optimize the cut value on the BDT outputs to maximize427
```
the signal-to-background ratio (see Section 4.2).428
```
4.1. Background suppression429
For the µ, e and hadronic channels of the Bsig, a BDT is trained on variables that430
have the most discriminating power between signal and background. All background431
```
process are considered as background, including BB (B+B−, B0B0), continuum (cc,432
```
```
ss, dd, uu) and τ +τ −. For the training and testing, we use 66% and 34% of the signal433
```
only sample and background from the generic MC sample respectively. The resulting434
signal efficiency is cross-checked later using the signal contained in the generic MC435
sample.436
The BDT is trained using XGBoost package [15] on GPUs, and the hyperparam-437
eters are optimized using the optuna package [16]. Since the signal sample is higher438
than the background sample, a scaling factor is applied to the background sample to439
balance the signal and background samples. The scaling factor is calculated as the440
ratio of the number of background candidates to the number of signal candidates.441
Reducing the false positive rate, not having significant overtraining and not having442
correlations between the output of the BDT and the two fitting variables are the443
main goals of the optimization. Each training uses two objectives to optimize the444
hyperparameters. The first one is defined as:445
```
objective1 = precisiontest ×
```

precisiontest
precisiontrain
2
×

loglosstrain
loglosstest
2
```
(4)
```
where precisiontest and precisiontrain are the precision of the test and train samples446
respectively, and loglosstest and loglosstrain are the logloss of the test and train samples447
respectively. The precision is defined as:448
```
precision =
```
TP
TP + FP
```
(5)
```
where TP and FP are the true positive and false positive rates respectively. A449
cut on the BDT output at 0.5 is applied to calculate the precision. The goal of450
33
this objective is to maximize the precision of the test sample while minimizing the451
overtraining. The second objective is defined as:452
```
objective2 =
```
q
```
r excess2A + r excess2B (6)
```
where r excessA and r excessB are defined as:453
r excessA = max
 
```
0, r(XGBoost output, EROEextra) − 0.1
```

```
(7)
```
```
r excessB = max(0, |r(XGBoost output, τpCMS )| − 0.1) (8)
```
```
(9)
```
where r is the Pearson correlation coefficient between the output of the BDT454
```
and the two fitting variables, defined in Equation (31). The goal of this objective455
```
is to minimize the correlations between the output of the BDT and the two fitting456
variables. The correlation is considered as acceptable if its absolute value is below457
0.1. The best set of objectives is the one that maximizes objective1 while minimizing458
objective2. The optimal set is taken following the Pareto front. The trial with the459
lowest objective2 is prioritized, then the one with the highest objective1 is selected.460
We use 15 and 18 variables for the leptonic and hadronic channels respectively.461
Here is a brief description of them:462
• aplanarity: event shape variable describing the flatness of the event, defined as463
the 3/2 of the third sphericity eigenvalue.464
• cosTBz: cosine of the angle between the thrust axis of the B and the z axis465
• cosTBTO: cosine of the angle between the thrust axis of the B and the thrust466
axis of the rest of the event.467
• deltaE: difference between the energy of the Btag and half of the center-of-mass468
energy.469
```
• τsig decays: decay mode of the Bsig (in this case, π or ρ channel).470
```
• miss E: missing energy in the event, calculated as the difference between the471
center-of-mass energy and the sum of the energies of all reconstructed particles472
in the event.473
• CleoConeCS i: CLEO Cones [17] calculated using the final state particles as-474
sociated to the Btag.475
34
• KSFWVariables hso01: modified Fox-Wolfram moment [18, 19].476
• cos θ∗Btag ,Dl : the cosine of the angle in CMS between the Dl system and the477
Btag.478
• thrustBm: magnitude of the B thrust axis.479
• ∆z: distance along the z axis between the decay vertices of the Btag and Bsig.480
• R2: ratio of the second to zeroth Fox-Wolfram moment calculated using all481
particles in the event.482
• harmonicMomentThrust i: harmonic moments of the i-th order calculated us-483
ing the thrust axis of the event.484
• miss theta: polar angle of the missing momentum in the event.485
• nROETracksGood: number of remaining tracks in the rest of the event that486
pass the mask dr < 2 cm, | |dz | | < 4 cm, θ in CDC acceptance and nCDC hits >487
20.488
• nRemainingTracks: number of all the remaining tracks in the event minus the489
tracks used in the Btag and Bsig candidates.490
• thrustAxisCosTheta: cosine of the polar angle of the thrust axis.491
The list of variables used in the training is shown in Table 8. Table 9 shows the492
hyperparameters used in the optimization. The Data/MC agreement of each variable493
is shown Appendix C.494
35
Feature µ e hadronic
Btag cosTBz ✓ ✓
Bsig cosTBTO ✓ ✓
Btag cosTBTO ✓
Btag deltaE ✓
τsig decays ✓
miss E ✓
harmonicMomentThrust3 ✓
Btag CleoConeCS 1 ✓ ✓ ✓
Btag CleoConeCS 2 ✓ ✓ ✓
Btag CleoConeCS 3 ✓ ✓ ✓
Btag KSFWVariables hso01 ✓ ✓ ✓
cos θ∗Btag ,Dl ✓ ✓ ✓
Btag thrustBm ✓ ✓ ✓
∆z ✓ ✓ ✓
```
R2 (Fox-Wolfram event based) ✓ ✓ ✓
```
harmonicMomentThrust1 ✓ ✓ ✓
miss theta ✓ ✓ ✓
nROETracksGood ✓ ✓ ✓
nRemainingTracks ✓ ✓ ✓
thrustAxisCosTheta ✓ ✓ ✓
TABLE 8. Variables used in the training of the BDT for each BDTs.
36
Hyperparameter Type Range Sampling
n estimators Integer [500, 2000] Uniform
max depth Integer [1, 10] Uniform
min child weight Integer [1, 10] Uniform
learning rate Float [0.01, 0.3] Logarithmic
subsample Float [0.1, 1.0] Step size 0.1
colsample bytree Float [0.1, 1.0] Step size 0.1
gamma Float [0.01, 0.5] Logarithmic
lambda Float [1e-3, 1] Logarithmic
alpha Float [1e-3, 1] Logarithmic
TABLE 9. Hyperparameters optimized by Optuna for XGBoost.
37
The hyperparameters are optimized over 1000 trials. After the training, good495
performance with no significant overtraining is observed. The BDT outputs and496
the comparison between training and testing samples are shown in Figure 9. The497
variable importance is shown in Figures 10 and 11.498
As for the performance, the ROC curve is shown in Figure 12 and the logloss is499
shown in Figure 13.500
38
0
1
2
3
4
5
Candidates density
Belle II preliminary simulation
Sig train
Bkg train
Sig test
Bkg test
0
2
Test
Sig
Train
Sig
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (µ channel)
```
0
2
Test
Bkg
Train
Bkg
```
(a)
```
0
1
2
3
4
5
Candidates density
Belle II preliminary simulation
Sig train
Bkg train
Sig test
Bkg test
0
2
Test
Sig
Train
Sig
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (e channel)
```
0
2
Test
Bkg
Train
Bkg
```
(b)
```
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Candidates density
Belle II preliminary simulation
Sig trainBkg train
Sig testBkg test
0
2
Test
Sig
Train
Sig
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (hadronic channels)
```
0
2
Test
Bkg
Train
Bkg
```
(c)
```
FIG. 9. BDT outputs for each channels. The Signal and Background are the signal only
and background from the generic MC sample respectively. The pull distribution between
the training and testing samples is shown in the bottom panel. No overtraining is observed.
39
```
0.0 0.1 0.2 0.3 0.4 0.5mean(|SHAP value|)
```
nRemainingTracks
cos θ ∗Btag, Dl
nROETracksGood
Btag CleoConeCS_3
Btag CleoConeCS_2
Bsig cosTBTO
```
R2 (Event based)
```
Btag KSFWVariables_hso01
thrustAxisCosTheta
miss_theta
Btag CleoConeCS_1
z
Btag thrustBm
Btag cosTBz
harmonicMomentThrust1
nRemainingTracks
cos θ ∗Btag, Dl
nROETracksGood
Btag CleoConeCS_3
Btag CleoConeCS_2
Bsig cosTBTO
```
R2 (Event based)
```
Btag KSFWVariables_hso01
thrustAxisCosTheta
miss_theta
Btag CleoConeCS_1
z
Btag thrustBm
Btag cosTBz
harmonicMomentThrust1
+0.46
+0.19
+0.11
+0.1
+0.09
+0.09
+0.09
+0.08
+0.06
+0.05
+0.04
+0.01
+0
+0
+0
For mu channel, on testing sample
```
(a)
```
```
0.0 0.1 0.2 0.3 0.4mean(|SHAP value|)
```
nRemainingTracks
cos θ ∗Btag, Dl
Btag KSFWVariables_hso01
nROETracksGood
```
R2 (Event based)
```
Btag CleoConeCS_2
Btag CleoConeCS_3
miss_theta
Bsig cosTBTO
thrustAxisCosTheta
Btag CleoConeCS_1
Btag thrustBm
harmonicMomentThrust1
Btag cosTBz
z
nRemainingTracks
cos θ ∗Btag, Dl
Btag KSFWVariables_hso01
nROETracksGood
```
R2 (Event based)
```
Btag CleoConeCS_2
Btag CleoConeCS_3
miss_theta
Bsig cosTBTO
thrustAxisCosTheta
Btag CleoConeCS_1
Btag thrustBm
harmonicMomentThrust1
Btag cosTBz
z
+0.44
+0.17
+0.16
+0.11
+0.11
+0.1
+0.09
+0.08
+0.06
+0.05
+0.05
+0.01
+0.01
+0
+0
For e channel, on testing sample
```
(b)
```
```
FIG. 10. The shapley value is used to evaluate the importance of each variable (see here).
```
The higher the absolute value of the shapley value, the more important the variable is to
separate signal from background.
40
```
0.0 0.1 0.2 0.3 0.4 0.5mean(|SHAP value|)
```
nRemainingTracks
cos θ ∗Btag, Dl
miss_E
Btag cosTBTO
thrustAxisCosTheta
z
τsig decays
miss_theta
Btag deltaE
Btag CleoConeCS_2
nROETracksGood
Btag CleoConeCS_3
harmonicMomentThrust1
Btag CleoConeCS_1
Btag KSFWVariables_hso01
```
R2 (Event based)
```
Btag thrustBm
harmonicMomentThrust3
nRemainingTracks
cos θ ∗Btag, Dl
miss_E
Btag cosTBTO
thrustAxisCosTheta
z
τsig decays
miss_theta
Btag deltaE
Btag CleoConeCS_2
nROETracksGood
Btag CleoConeCS_3
harmonicMomentThrust1
Btag CleoConeCS_1
Btag KSFWVariables_hso01
```
R2 (Event based)
```
Btag thrustBm
harmonicMomentThrust3
+0.51
+0.41
+0.4
+0.34
+0.28
+0.21
+0.18
+0.17
+0.16
+0.15
+0.15
+0.14
+0.12
+0.09
+0.09
+0.03
+0.02
+0.01
For hadronic channel, on testing sample
```
FIG. 11. The shapley value is used to evaluate the importance of each variable (see here).
```
The higher the absolute value of the shapley value, the more important the variable is to
separate signal from background.
41
0.0 0.2 0.4 0.6 0.8 1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
XGBoost ROC curve for mu channel
AUC Train = 0.76
AUC Test = 0.75
```
(a)
```
0.0 0.2 0.4 0.6 0.8 1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
XGBoost ROC curve for e channel
AUC Train = 0.76
AUC Test = 0.76
```
(b)
```
0.0 0.2 0.4 0.6 0.8 1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
XGBoost ROC curve for hadronic channel
AUC Train = 0.85
AUC Test = 0.85
```
(c)
```
FIG. 12. ROC curve for each channels. No overtraining is observed.
42
```
(a) (b)
```
```
(c)
```
FIG. 13. Logloss for each channels. No overtraining is observed.
43
4.2. Signal optimization501
A cut on the output of each BDT is applied to reduce the remaining background502
while keeping a high signal efficiency. Only the candidates in the SR are considered503
for the optimization process, to keep the shape information of EROEextra. The following504
steps are taken to optimize the cut value for each channels:505
1. The signal efficiency as a function of the BDT output is calculated for the506
signal only sample. The plots are shown in Figure 14.507
2. The FOM is calculated as a function of the BDT output. The FOM is defined508
```
as:509
```
```
FOM =
```
S∗√
S∗ + B
```
(10)
```
where B is the number of background candidates, and S∗ corresponds to the510
number of signal event from the signal only sample normalized to the signal511
```
expected for the luminosity of the background sample (1444 fb−1). The plots512
```
are shown in Figure 15.513
3. The BDT output is flattened to have a uniform distribution of the signal effi-514
ciency using the cumulative distribution function of the signal efficiency shown515
in Figure 14. This way, the area around the maximum of the FOM in Figure 15516
is enhanced, and a cut on the flattened BDT output will directly correspond517
to a cut on the signal efficiency. The plots are shown in Figure 16.518
4. The FOM is calculated as a function of the signal efficiency. The maximum of519
the FOM is found, and the corresponding signal efficiency is used as the cut520
value. The plots are shown in Figure 17.521
44
```
(a) (b)
```
```
(c)
```
FIG. 14. Signal efficiency as a function of the BDT output for each channels.
45
```
(a) (b)
```
```
(c)
```
FIG. 15. FOM as a function of the BDT output for each channels. Luminosity is four
```
times the LS1 dataset (1444 fb−1).
```
46
0.0 0.2 0.4 0.6 0.8 1.0
```
1 - Flattened XGBoost output (µ channel)
```
100
Event density
Belle II preliminary simulation
Signal
Background
```
(a)
```
0.0 0.2 0.4 0.6 0.8 1.0
```
1 - Flattened XGBoost output (e channel)
```
100
Event density
Belle II preliminary simulation
Signal
Background
```
(b)
```
0.0 0.2 0.4 0.6 0.8 1.0
```
1 - Flattened XGBoost output (hadronic channels)
```
10 1
100
Event density
Belle II preliminary simulation
Signal
Background
```
(c)
```
FIG. 16. Flattened BDT output for each channels.
47
```
(a) (b)
```
```
(c)
```
FIG. 17. FOM as a function of the signal efficiency for each channels.
48
```
The signal efficiency (corresponding to the cut value on the flattened BDT output)522
```
and background retention for each channels is shown in Table 10. The background523
composition for each channels is shown in Table 11, and in the fit region in Table 12.524
The total background retention of this step is equal to 30.99 ± 0.09%. The total525
signal efficiency on the signal only sample and the signal found in the generic MC526
sample is equal to 72.01±0.10% and 71.0±1.7% respectively. With the pre-selection,527
the total background retention, signal efficiency on the signal only sample and the528
signal found in the generic MC sample is equal to 5.159 ± 0.018%, 0.2793 ± 0.0008%529
and 0.290 ± 0.009% respectively.530
τ channel Sgn Eff [%] Bkg Ret [%]
µ 76.87 ± 0.31 40.43 ± 0.33
e 76.52 ± 0.35 39.33 ± 0.35
hadronic 62.3 ± 0.4 13.70 ± 0.23
```
TABLE 10. Relative signal efficiency (corresponding to the cut value on the flattened BDT
```
```
output) and background retention for each channels after applying the BDT cuts.
```
µ e π ρ Total
Signal 43 46 20 5 115
B 0B 0 514 490 80 46 1132
B +B − 1828 1699 302 141 3973
uu 48 17 41 12 120
d d 13 3 11 4 31
ss 16 2 10 2 32
cc 203 128 92 25 451
τ τ 13 4 11 1 29
ℓℓXX 12 12 2 0 27
Total 2690 2401 569 236 5910
FOM 0.83 0.94 0.84 0.33 1.50
TABLE 11. Expected number of candidates with LS1 dataset for each channels in the fit
region after the optimization.
49
µ e π ρ Total
Signal 30 35 11 4 82
B 0B 0 69 67 9 3 149
B +B − 135 134 40 12 322
uu 11 7 11 4 35
d d 5 2 1 0 9
ss 3 0 2 0 7
cc 37 29 20 5 93
τ τ 9 2 6 1 20
ℓℓXX 12 6 2 0 20
Total 311 282 102 29 737
FOM 1.70 2.08 1.09 0.74 3.02
TABLE 12. Expected number of candidates with LS1 dataset for each channels in the
signal region after the optimization.
4.3. Fitting variables before/after optimization531
```
The distributions of the fitting variables (EROEextra and τpCMS ) before and after the532
```
optimization for each channels are shown in Figures 18 to 20.533
50
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
500
1000
1500
2000
2500
Candidates / 0.15 GeV/
c
Belle II preliminary simulationchannel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×1.0
```
(a)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
500
1000
1500
Candidates / 0.15 GeV/
c
Belle II preliminary simulationchannel
XXττ
qqB0B0
B+B−49M Signal ×1.0
```
(b)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
250
500
750
1000
1250
1500
Candidates / 0.10 GeV
Belle II preliminary simulationchannel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2
```
(c)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
100
200
300
400
500
600
Candidates / 0.10 GeV
Belle II preliminary simulationchannel
XXττ
qqB0B0
B+B−49M Signal ×0.1
```
(d)
```
FIG. 18. Distributions of the fitting variables for the µ channel before and after the
optimization.
51
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
500
1000
1500
2000
Candidates / 0.15 GeV/
c
Belle II preliminary simulatione channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×1.0
```
(a)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
250
500
750
1000
1250
1500
Candidates / 0.15 GeV/
c
Belle II preliminary simulatione channel
XXττ
qqB0B0
B+B−49M Signal ×1.0
```
(b)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
200
400
600
800
1000
1200
Candidates / 0.10 GeV
Belle II preliminary simulatione channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2
```
(c)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
100
200
300
400
Candidates / 0.10 GeV
Belle II preliminary simulatione channel
XXττ
qqB0B0
B+B−49M Signal ×0.1
```
(d)
```
FIG. 19. Distributions of the fitting variables for the e channel before and after the opti-
mization.
52
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
500
1000
1500
2000
2500
3000
Candidates / 0.15 GeV/
c
Belle II preliminary simulation+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×1.0
```
(a)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
200
400
600
800
1000
1200
Candidates / 0.15 GeV/
c
Belle II preliminary simulation+ channels
XXττ
qqB0B0
B+B−49M Signal ×1.0
```
(b)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
200
400
600
800
1000
1200
Candidates / 0.10 GeV
Belle II preliminary simulation+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2
```
(c)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
50
100
150
Candidates / 0.10 GeV
Belle II preliminary simulation+ channels
XXττ
qqB0B0
B+B−49M Signal ×0.04
```
(d)
```
FIG. 20. Distributions of the fitting variables for the hadronic channel before and after the
optimization.
53
5. CORRECTIONS534
We describe in this section a set of corrections applied to important variables used535
```
in the analysis to improve the data/MC agreement. Some corrections (like the PIDs,536
```
```
BF, form factors...) are described in details in Section 8.537
```
5.1. FEI corrections538
A discrepancy between the efficiency of the different FEI decay modes is seen539
between Data and MC after the pre-selection, as seen in Figure 21.540
Calibrations factors corresponding to the FEI signal probability cut used in the re-541
```
construction are available for the B+B− and B0B0 samples (see SLFEI rd cal factors Bp 004).542
```
After applying the calibration factors corresponding to the FEI signal probability cut543
used in the reconstruction to the correctly reconstructed Btag, the data/MC agree-544
ment is improved as shown in Figure 22, but some discrepancy remains, specially for545
the hadronic τ decays which have a larger fraction of qq background.546
To correct the continuum sample, we therefore derive additional correction factors547
based on the FEI decay mode distributions using off-resonance data and MC. The548
small energy shift between off-resonance data and MC is taken into account. The549
correction factors are derived as the ratio of the data and MC distributions of the550
FEI decay modes. The off-resonance data distribution before correction can be seen551
in Figure 23, and the final data/MC agreement after applying all corrections is shown552
in Figure 24.553
In addition, an efficiency discrepancy of the D0tag channels is seen after the selection554
```
on the EROEextra > 0.3 GeV sideband region for the µ channel (see Figure 25). We decided555
```
to correct the first four D0tag channels efficiencies. An additional systematic has been556
included in the fit to account for this effect.557
54
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.19 × MC
```
(a)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.18 × MC
```
(b)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.17 × MC
```
(c)
```
FIG. 21. Comparison between data and MC of the FEI decay mode for the different τ
decays before any FEI corrections.
55
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.12 × MC
```
(a)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.18 × MC
```
(b)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.12 × MC
```
(c)
```
FIG. 22. Comparison between data and MC of the FEI decay mode for the different τ
decays after applying the FEI calibration correction.
56
0
50
100
150
Candidates
Belle II preliminary L dt = 42 fb 1channel
ττcc
ssdd
uuMC stat. unc.
Off-res
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Off
res
Off
resMC
Data/MC = 1.20
```
(a)
```
0
20
40
60
Candidates
Belle II preliminary L dt = 42 fb 1e channel
ττcc
ssdd
uuMC stat. unc.
Off-res
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Off
res
Off
resMC
Data/MC = 1.16
```
(b)
```
0
200
400
600
Candidates
Belle II preliminary L dt = 42 fb 1+ channels
ττcc
ssdd
uuMC stat. unc.
Off-res
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Off
res
Off
resMC
Data/MC = 1.05
```
(c)
```
FIG. 23. Comparison between off-resonance data and MC of the FEI decay mode for the
different τ decays before any FEI corrections.
57
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.18 × MC
```
(a)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.17 × MC
```
(b)
```
0.0
0.2
0.4
0.6
0.8
1.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 2 4 6 8
Btag decays
0.5
1.0
1.5
Data1.16 × MC
```
(c)
```
FIG. 24. Comparison between data and MC of the FEI decay mode for the different τ
decays after applying all FEI corrections.
58
0
200
400
600
800
Candidates / 1.00
Belle II preliminary L dt = 365 fb 1channel
0.0 2.5 5.0 7.5 10.0 12.5 15.0
D0_dmID
0.5
1.0
1.5
DataMC
```
(a)
```
0
200
400
600
800
Candidates / 1.00
Belle II preliminary L dt = 365 fb 1e channel
0.0 2.5 5.0 7.5 10.0 12.5 15.0
D0_dmID
0.5
1.0
1.5
DataMC
```
(b)
```
0
50
100
150
200
250
Candidates / 1.00
Belle II preliminary L dt = 365 fb 1+ channels
0.0 2.5 5.0 7.5 10.0 12.5 15.0
D0_dmID
0.5
1.0
1.5
DataMC
```
(c)
```
FIG. 25. Comparison between data and MC of the D0tag decay mode for the different
τ decays after the selection and in the EROEextra > 0.3 GeV sideband selection. Each bin
corresponds to a mode ID in Table 3.
59
5.2. Extra energy corrections558
A shift can be seen between data and MC on the energy of the rest of event for559
```
each τ channel after the pre-selection (see Figure 26).560
```
0
250
500
750
1000
1250
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra c2_bbS_32
0.5
1.0
1.5
Data1.18 × MC
```
(a)
```
0
200
400
600
800
1000
1200
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra c2_bbS_32
0.5
1.0
1.5
Data1.24 × MC
```
(b)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra c2_bbS_32
0.5
1.0
1.5
Data1.27 × MC
```
(c)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra c2_bbS_32
0.5
1.0
1.5
Data1.18 × MC
```
(d)
```
FIG. 26. Comparison between data and MC of EROEextra for each τ decay.
In order to correct this discrepancy, three steps are performed:561
1. Apply the photon efficiency data/MC ratio correction from neutral group study562
[ref], which gives a weight for each ROE photons given its energy, ϕ and θ.563
Then, for each photon, a random number in [0, 1] is uniformly generated and564
compared to the weight. If the random number is smaller than the weight, the565
60
photon is kept, otherwise it is removed from the ROE. The distribution of the566
number of photon in the ROE N ROEγ and the EROEextra =
P
Eγ are updated. The567
weight table used is PhotonEfficiencyDataMCRatio Run1MC15rd April2024 rev 1.568
2. The shape further corrected using off and on-resonance data sidebands:569
```
(a) Continuum correction: using off-resonance MC and data, each bin of570
```
N ROEγ is corrected by the ratio data/MC ration. The shape of the EROEextra571
distribution is directly impacted by this correction.572
```
(b) Signal correction: using the data/MC ratio of the N ROEγ distributions for573
```
```
the control channels (B+ → D∗0ℓ+νℓ for leptonic channels and double574
```
```
tagged for hadronic channels), we derive correction factors for each bin of575
```
N ROEγ . The shape of the EROEextra distribution is directly impacted by this576
correction. More information about the control channels can be found in577
Sections 6.3.4 and 6.3.5.578
```
(c) BB background correction: using the BDT sidebands, removing candi-579
```
dates above 0.51 and 0.62 BDT score for leptonic and hadronic channel580
respectively. We subtract from data the continuum corrected MC. The581
resulting distribution corresponds to the BB contribution of data. By582
comparing BB distribution of MC and data, each bin of N ROEγ is then583
corrected by the data/MC ratio. Since the hadronic channels have low584
statistics and a single control channel, they are also merged together to585
have better statistics for the correction. More information on the compo-586
sition of the BDT sidebands can be found in Appendix D.c.587
The distributions before and after step 1 are shown in Figure 27. The photon588
```
multiplicity N ROEγ and the EROEextra before and after step 2 (a) are shown in Figures 28589
```
and 29. The final distributions with all corrections applied on the BDT sideband and590
```
on the full region (blind) are shown in Figures 32 and 33. No data/MC discrepancy591
```
is observed in the EROEextra distribution after all the corrections.592
The corrections is also checked using the extra track SB control sample, where we593
don’t expect signal. Thus, the signal region is not blinded for this control sample.594
The distributions can be seen in Appendix D.595
61
0
250
500
750
1000
1250
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.16 × MC
```
(a)
```
0
200
400
600
800
1000
1200
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.22 × MC
```
(b)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.22 × MC
```
(c)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.14 × MC
```
(d)
```
FIG. 27. Comparison between data and MC of EROEextra for each τ decay after step 1 of the
correction.
62
0.00
0.05
0.10
0.15
0.20
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1e channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(d)
```
FIG. 28. Comparison between off-resonance data and MC of N ROEγ for each τ decay.
63
0.0
0.2
0.4
0.6
0.8
1.0
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.00
0.25
0.50
0.75
1.00
1.25
Event density
Belle II preliminary L dt = 42 fb 1e channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.00
0.25
0.50
0.75
1.00
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(d)
```
FIG. 29. Comparison between off-resonance data and MC of EROEextra for each τ decay after
reweighting each bin of the N ROEγ distribution to its data/MC ratio.
64
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 365 fb 1channel
BB MCBB MC corr
BB Data
0 5 10 15 20
NROE
0.5
1.0
1.5
Data/MC
```
(a)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 365 fb 1e channel
BB MCBB MC corr
BB Data
0 5 10 15 20
NROE
0.5
1.0
1.5
Data/MC
```
(b)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 365 fb 1+ channels
BB MCBB MC corr
BB Data
0 5 10 15 20
NROE
0.5
1.0
1.5
Data/MC
```
(c)
```
FIG. 30. Comparison between on-resonance BB data and MC of N ROEγ for each τ decay
for the BDT sideband.
65
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 365 fb 1channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
EROEextra
0.5
1.0
1.5
Data/MC
```
(a)
```
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 365 fb 1e channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
EROEextra
0.5
1.0
1.5
Data/MC
```
(b)
```
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 365 fb 1+ channels
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
EROEextra
0.5
1.0
1.5
Data/MC
```
(c)
```
FIG. 31. Comparison between on-resonance BB data and MC of EROEextra for each τ decay
of the BDT sideband after reweighting each bin of the N ROEγ distribution to its data/MC
ratio.
66
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.20 × MC
```
(a)
```
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.21 × MC
```
(b)
```
0
100
200
300
400
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.24 × MC
```
(c)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.15 × MC
```
(d)
```
FIG. 32. Comparison between data and MC of EROEextra for each τ decay on the sideband of
the BDT output after step 2 of the correction.
67
0
250
500
750
1000
1250
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.20 × MC
```
(a)
```
0
200
400
600
800
1000
1200
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.21 × MC
```
(b)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.26 × MC
```
(c)
```
0
100
200
300
400
500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
```
Data (blind)
```
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.17 × MC
```
(d)
```
FIG. 33. Comparison between data and MC of EROEextra for each τ decay after step 2 of the
correction.
68
5.3. pCMS corrections596
The momentum of the τ distribution does not agree between data and MC after597
the pre-selection, as shown in Figure 34. Since this is one of the fit variable, the598
distribution has to be corrected. We observe a good agreement between off-resonance599
```
data and MC after the pre-selection (see Figure 35), thus the pCMS correction is only600
```
calculated using the BB background. We use the BDT sideband to correct the MC.601
We remove the non-BB samples from MC, and the same amount is removed from602
the data distribution. Then, for each τ channel, each bin of pCMS is corrected to603
match the data distribution. Figure 36 shows the data/MC agreement before and604
after applying the corrections on the BB MC. Figure 37 shows the final data/MC605
agreement after all corrections are applied. No significant discrepancy remains after606
the correction.607
0
500
1000
1500
2000
2500
3000
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.12 × MC
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.18 × MC
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.17 × MC
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.09 × MC
FIG. 34. Comparison between data and MC of the momentum of the τ in the CMS frame
for each τ decay after the pre-selection without correction applied.
69
0
20
40
60
80
Candidates
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.19 × MC
0
5
10
15
20
25
30
Candidates
Belle II preliminary L dt = 42 fb 1e channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.10 × MC
0
25
50
75
100
125
Candidates
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.12 × MC
0
20
40
60
80
100
Candidates
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.05 × MC
FIG. 35. Comparison between off-resonance data and MC of the momentum of the τ in
the CMS frame for each τ decay on the sideband of the BDT output.
70
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb-1channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data/MC
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb-1e channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data/MC
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb-1channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data/MC
0.0
0.2
0.4
0.6
0.8
1.0
Event density
Belle II preliminary L dt = 365 fb-1channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data/MC
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb-1
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data/MC
FIG. 36. Comparison between data and MC of the momentum of the τ in the CMS frame
```
for each τ decay on the sideband of the BDT output, before (blue) and after (red) applying
```
the pCMS correction.
71
0
500
1000
1500
2000
2500
3000
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.18 × MC
0
500
1000
1500
2000
2500
3000
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.17 × MC
0
500
1000
1500
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0 3.5
pvis [GeV/c]
0.5
1.0
1.5
Data1.20 × MC
0
500
1000
1500
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0 3.5
pvis [GeV/c]
0.5
1.0
1.5
Data1.13 × MC
FIG. 37. Comparison between data and MC of the momentum of the τ in the CMS frame
for each τ decay with the τpCMS correction applied.
72
6. DATA/MC COMPARISON AND VALIDATION608
This section shows some data/MC comparison plots and validation checks.609
6.1. Embedded sample efficiencies610
The embedded sample is used to validate the analysis procedure and check the611
different efficiencies and data/MC agreements. Each event of the embedded sample612
is created by taking an on-resonance data event where the tag-side B meson is fully613
reconstructed and replacing the signal-side B meson by a simulated B+ → τ +ντ614
decay. The ROE is kept from data. This way, the embedded sample has the same615
background conditions as data, but with a known signal decay. The same method616
used in the B → Kνν ITA analysis is used. Here are the different steps to achieve617
```
this:618
```
• Create B+ → τ +ντ signal MC udst skim using very loose cuts.619
```
• Create fully hadronic udst skims of the on-resonance data using B+ → (K∗ →620
```
```
Kπ)(J/ψ → µµ) and B+ → K+(J/ψ → µµ or ee) decays. All the final states621
```
particles of the B+ are required to be reconstructed and identified.622
• Use the embedding tool to remove the KJψ system from the udst data skims.623
• Use the embedding tool to remove the tag-side B meson and the ROE from624
the udst signal MC skims.625
• Merge the two udst skims together to create the embedded udst skims. The626
sample is now composed of a tag-side B meson and ROE from data, and a627
simulated signal-side B+ → τ +ντ decay.628
• Run the reconstruction script on the embedded udst skims to create the final629
embedded mdst sample.630
The same procedure is run on MC samples to create an embedded MC sample,631
which is used to check the data/MC agreement of the embedding procedure.632
After the reconstruction, 257 signal candidates remain in the embedded sample.633
The same pre-selection is applied. The resulting data/MC efficiency ratios for the634
different pre-selection cuts are shown in Table 13. All efficiencies are compatible635
between data and MC within the statistical uncertainty.636
The same BDT cuts as on for the main analysis are applied on the embedded637
sample. The resulting data/MC efficiency ratios for the different BDT selection cuts638
73
Selection step Data/MC ratio
Reconstruction 0.96 ± 0.06
p∗l,tag > 0.3 GeV/c 1.000 ± 0.004
p∗τ,sig > 0.4 GeV/c 1.015 ± 0.017
p∗Dtag < 2.5 GeV/c 1.004 ± 0.004
−3 < cos θ∗B,Dl < 1.5 1.007 ± 0.017
```
R2(Event based) < 0.45 1.026 ± 0.028
```
Btag R2 < 0.45 0.994 ± 0.007
cos θthurst,Btag,z < 0.85 0.967 ± 0.026
Btag decay mode ID < 4 1.006 ± 0.016
π: pBsig > 1. GeV/c 1.04 ± 0.08
ρ: pBsig > 1. GeV/c 1.10 ± 0.08
```
e: Ktag electronID < 0.2 0.98 ± 0.04
```
```
e: conv. γ InvM(ℓtag − esig) > 0.02 GeV/c2 0.990 ± 0.023
```
```
e: conv. γ InvM(Dtag, daughters − esig) > 0.02 GeV/c2 0.981 ± 0.033
```
Total
Pre-selection 1.03 ± 0.06
Reco + pre-selection 0.99 ± 0.08
TABLE 13. Data/MC efficiency ratios for the embedded sample during reconstruction and
pre-selection.
for each τ decays are shown in Table 14. The data/MC efficiency ratio in bins of639
τpCMS are also shown Figure 38. The data/MC efficiency ratios are compatible with640
1 within the statistical uncertainty.641
We decide to correct the measured BF value by 10% and assign a 10% systematic642
uncertainty to the signal efficiency to cover the observed data/MC discrepancy in643
the embedded sample.644
74
Channel Data/MC ratio
µ 1.02 ± 0.08
e 1.19 ± 0.09
hadronic 1.12 ± 0.13
Total
Selection 1.11 ± 0.06
Reco + pre-sel + selection 1.10 ± 0.11
TABLE 14. Data/MC BDT efficiency ratios for the embedded samples.
0.5 1.0 1.5 2.0
```
pvis (binning of fit region)
```
0
1
2
3
Embedded data/MC ratio
BDT efficiency ratio for channel
0.5 1.0 1.5 2.0
```
pvis (binning of fit region)
```
0
1
2
3
4
5
Embedded data/MC ratio
BDT efficiency ratio for e channel
1.0 1.5 2.0 2.5
```
pvis (binning of fit region)
```
0
1
2
3
Embedded data/MC ratio
BDT efficiency ratio for hadronic channel
FIG. 38. Data/MC BDT efficiency ratio in bins of τpCMS for the embedded samples.
75
6.2. BDT output checks645
To check if the output of the BDT is agreeing between data and MC, we compare646
the BDT output distributions after the pre-selection for each τ channels on the off-647
```
resonance, on the on-resonance data by cutting away the BDT signal region (BDT648
```
```
sideband), and on the embedded data sample. The results are shown in Figures 39649
```
to 41. A good agreement between data and MC is observed.650
0
10
20
30
40
50
Candidates / 0.05
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (µ channel)
```
0.5
1.0
1.5
Data1.19 × MC
0
5
10
15
20
Candidates / 0.05
Belle II preliminary L dt = 42 fb 1e channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (e channel)
```
0.5
1.0
1.5
Data1.09 × MC
0
50
100
150
200
250
Candidates / 0.05
Belle II preliminary L dt = 42 fb 1+ channels
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (hadronic channels)
```
0.5
1.0
1.5
Data1.08 × MC
```
FIG. 39. Distribution of the BDT output after the pre-selection for the µ (left), e (right)
```
```
and hadronic (bottom) channels on the off-resonance data.
```
76
0
200
400
600
800
1000
Candidates / 0.03
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.1 0.2 0.3 0.4 0.5
```
XGBoost output (µ channel) (blind)
```
0.5
1.0
1.5
Data1.18 × MC
0
200
400
600
800
1000
Candidates / 0.03
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.1 0.2 0.3 0.4 0.5
```
XGBoost output (e channel) (blind)
```
0.5
1.0
1.5
Data1.18 × MC
0
500
1000
1500
Candidates / 0.03
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.1 0.2 0.3 0.4 0.5
```
XGBoost output (hadronic channels) (blind)
```
0.5
1.0
1.5
Data1.15 × MC
```
FIG. 40. Distribution of the BDT output after the pre-selection for the µ (left), e (right)
```
```
and hadronic (bottom) channels on the on-resonance data by cutting away the BDT signal
```
region.
77
0
2
4
6
Event density
Belle II preliminary simulationchannel
Embedded BSig TM B
MC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (µ channel)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.710
2
4
6
Event density
Belle II preliminary simulatione channel
Embedded BSig TM B
MC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (e channel)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.67
0
1
2
3
4
Event density
Belle II preliminary simulationhadronic channels
Embedded BSig TM B
MC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (hadronic channels)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.88
FIG. 41. Distributions of the fitting variables in the embedded sample after the full selection
```
for the µ channel. The Kolmogorov-Smirnov (KS) test p-value is used to quantify the
```
agreement between data and MC.
78
6.3. Fitting variables after full selection651
The distributions of EROEextra and τpCMS after the full selection for each τ channels652
are checked using the different data sample available.653
6.3.1. SB control sample654
To check if the selection cuts are well modeled by MC, we use the SB control655
sample defined in Section 2 to compare the fitting variables. No signal is expected in656
the signal region. The EROEextra and τpCMS distributions after the full selection for each657
τ channels are shown in Figures 42 to 44. No significant data/MC discrepancies are658
observed.659
0
5
10
15
20
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.10 × MC
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Candidates
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.11 × MC
FIG. 42. Distributions of the fitting variables in the SB control sample after the full
selection for the µ channel
.
79
0
5
10
15
20
25
30
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.34 × MC
0
5
10
15
20
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.34 × MC
FIG. 43. Distributions of the fitting variables in the SB control sample after the full
selection for the e channel
.
0
10
20
30
40
Candidates
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.5
1.0
1.5
Data1.27 × MC
0
5
10
15
20
25
30
Candidates
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.27 × MC
FIG. 44. Distributions of the fitting variables in the SB control sample after the full
selection for the hadronic channels
.
6.3.2. Off-resonance data660
The off-resonance data is used to validate the non-BB background modeling. The661
EROEextra and τpCMS distributions after the full selection for each τ channels are shown662
in Figures 45 to 47. No significant data/MC discrepancies are observed.663
80
0
5
10
15
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
2
Data
1.20 ± 0.14 × MC
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Candidates / 0.10 GeV
Belle II preliminary L dt = 42 fb 1channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
2
Data
1.21 ± 0.14 × MC
FIG. 45. Distributions of the fitting variables in the off-resonance data after the full
selection for the µ channel
.
0
2
4
6
8
10
12
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 42 fb 1e channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
2
Data
1.12 ± 0.18 × MC
0
2
4
6
8
10
Candidates / 0.10 GeV
Belle II preliminary L dt = 42 fb 1e channel
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
2
Data
1.12 ± 0.18 × MC
FIG. 46. Distributions of the fitting variables in the off-resonance data after the full
selection for the e channel
.
81
0
2
4
6
8
10
12
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 42 fb 1+ channels
XXττ
ccss
dduu
MC stat. unc.Off-res
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0
2
Data
0.99 ± 0.14 × MC
0
2
4
6
8
10
Candidates / 0.10 GeV
Belle II preliminary L dt = 42 fb 1+ channels
XXττ
ccss
dduu
MC stat. unc.Off-res
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0
2
Data
0.97 ± 0.14 × MC
FIG. 47. Distributions of the fitting variables in the off-resonance data after the full
selection for the hadronic channels
.
82
6.3.3. Embedded sample664
The embedded sample defined in Section 6.1 is used to check the modeling of the665
fitting variables for signal candidates. The EROEextra and τpCMS distributions after the666
full selection for each τ channels are shown in Figures 48 to 50. Despite the low667
statistics, no significant data/MC discrepancies are observed.668
0.0
0.5
1.0
1.5
Event density
Belle II preliminary simulationchannel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.0
2.5
Embedded
Sig
KS p-value: 0.580
2
4
6
Event density
Belle II preliminary simulationchannel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.14
FIG. 48. Distributions of the fitting variables in the embedded sample after the full selection
```
for the µ channel. The Kolmogorov-Smirnov (KS) test p-value is used to quantify the
```
agreement between data and MC.
83
0.0
0.5
1.0
1.5
Event density
Belle II preliminary simulatione channel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.0
2.5
Embedded
Sig
KS p-value: 0.680
1
2
3
4
5
Event density
Belle II preliminary simulatione channel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.74
FIG. 49. Distributions of the fitting variables in the embedded sample after the full selection
```
for the e channel. The Kolmogorov-Smirnov (KS) test p-value is used to quantify the
```
agreement between data and MC.
0.0
0.5
1.0
1.5
Event density
Belle II preliminary simulation+ channel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0.0
2.5
Embedded
Sig
KS p-value: 0.260
1
2
3
4
5
Event density
Belle II preliminary simulation+ channel
Embedded BSig TM B
MC stat. unc.
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
2.5
Embedded
Sig
KS p-value: 0.74
FIG. 50. Distributions of the fitting variables in the embedded sample after the full selection
```
for the hadronic channels. The Kolmogorov-Smirnov (KS) test p-value is used to quantify
```
the agreement between data and MC.
6.3.4. B+ → D∗0ℓ+νℓ control sample669
```
We select a control sample of B+ → D∗0ℓ+νℓ,(ℓ = e, µ) decay to check data/MC670
```
consistency and validate the analysis procedure. The control sample is similar with671
the signal B+ → τ +ντ , with a charged lepton and neutrino in the final state and the672
84
extra energy is also expected peaking at zero. To select the control sample, we re-673
construct a semi-leptonic Btag candidate per event with semi-leptonic FEI algorithm674
and a signal Bsig decaying to D∗0ℓ+ν. The D∗0 is reconstructed from D∗0 → D0γ and675
D∗0 → D0π0. The D0 is reconstructed from D0 → K−π+, D0 → K−π+π+π− and676
D0 → K0S π+π−. The selection criterion are same with B+ → τ +ντ when applicable.677
Other selection criterion are summarized in Table 15.678
Variable requirement
K± dr < 0.5 cm and |dz | < 2 cm and kaonID noSVD > 0.6
K0S K0S standard list from ksSelector
```
M (D0) (1.855, 1.875) GeV/c2
```
```
M (D∗0) - M (D0) (0.120, 0.155) GeV/c2
```
γ in D∗0 → D0γ Eγ > 0.1 GeV, fakePhotonSuppression > 0.15
```
cosθ∗B,Dl (−1, 1)
```
```
MissingMass square (−1, 1)
```
Background Suppression Apply the same BDT of B+ → τ +ντ and same cut
```
BCS Best D0 mass; best D∗0 mass; then the highest PID of the lepton
```
ROE No extra tracks coming from the IP. No extra K0S , Λ0, π0
```
TABLE 15. Selection criterion for control sample B+ → D∗0ℓ+νℓ,(l = e, µ).
```
The extra energy distribution of the control sample is expected to be same with679
signal mode B+ → τ +ντ . We compare the extra energy distributions of correctly680
reconstructed B+ → D∗0ℓ+νℓ and B+ → τ +ντ , shown in Figure 51. The distributions681
are consistent.682
After final event selection, the continuum backgrounds in B+ → D∗0ℓ+νℓ are683
```
negligible (expect 0 events in B+ → D∗0e+ν and 1.1 events in B+ → D∗0mu+ν).684
```
We applied the same FEI correction and pCMS correction factors for B+ → D∗0ℓ+νℓ685
as that of B+ → τ +ντ . We also applied the extra energy correction following the686
same procedure of B+ → τ +ντ . The extra energy correction factors are obtained687
by comparing the distributions of number of photons in the ROE in data and MC.688
```
After all corrections, the fit variables (i.e. momentum of the lepton in CMS frame689
```
```
and extra energy) of the control sample are shown in Figure 52. The data/MC ratio690
```
for each bin of N ROEγ distribution is shown in Table 16. These weights are applied to691
the signal MC sample of the leptonic decays to correct its N ROEγ distribution. The692
background breakdown is shown and also overlayed with data points. The shapes693
between data and MC are consistent. The ratio of data and MC events is 0.912 ±694
0.046 for electron mode and 0.954 ± 0.044 for muon mode, respectively.695
85
FIG. 51. Extra energy distribution of B+ → D∗0ℓ+νℓ compared to that of B+ → τ +ντ ,
only MC truth-matched signal events are shown.
bin µ channel e channel
0 1.07 ± 0.10 0.99 ± 0.10
1 1.11 ± 0.09 1.05 ± 0.09
2 0.97 ± 0.10 0.95 ± 0.10
3 0.71 ± 0.12 1.09 ± 0.16
4 1.09 ± 0.27 0.89 ± 0.22
5 0.46 ± 0.24 0.65 ± 0.35
6 0.29 ± 0.30 1.27 ± 1.02
7 0 ± 0 0 ± 0
TABLE 16. Data/MC ratio in each bin of N ROEγ distribution of the control sample B+ →
D∗0ℓ+νℓ.
86
0
50
100
150
200
Candidates / 0.1 GeV
Belle II preliminary L dt = 365 fb 1D
∗0µν
D ∗0`ν
D0
D01
Other B ¯B bkg
q¯q
MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0.5
1.0
1.5
DataMC
0
20
40
60
80
Candidates / 0.16 GeV/
c Belle II preliminary L dt = 365 fb
1D ∗0µν
0.5 1.0 1.5 2.0
p* [GeV/c]
0.5
1.0
1.5
DataMC
0
50
100
150
200
Candidates / 0.1 GeV
Belle II preliminary L dt = 365 fb 1D ∗0eνD ∗0`ν
D0
D01
Other B ¯B bkg
q¯q
MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0.5
1.0
1.5
DataMC
0
20
40
60
80
Candidates / 0.16 GeV/
c Belle II preliminary L dt = 365 fb
1D ∗0eν
0.5 1.0 1.5 2.0
p* [GeV/c]
0.5
1.0
1.5
DataMC
FIG. 52. Lepton pCMS and extra energy distributions of the control sample B+ →
D∗0ℓ+νℓ, the MC histograms are scaled to number of events in data.
87
6.3.5. Double tagged control sample696
To check the hadronic channels, we use a double tagged control sample where the697
signal side is reconstructed using hadronic FEI. The tag side is still reconstructed698
using the SL FEI. The selection criterion are same with B+ → τ +ντ when applicable.699
Other selection criterion are summarized in Table 17.700
Variable requirement
```
sigProb (or extraInfo(dmID)) > 0.001 (or = 25)
```
Mbc > 5.27 GeV/c2
```
∆E (−0.15, 0.1) GeV
```
R2 < 0.6
Keep the best Btag candidate highest sigProb
Background Suppression Apply the same BDT of B+ → τ +ντ and same cut
ROE No extra tracks coming from the IP
ROE No extra K0S , Λ0, π0
TABLE 17. Selection criterion for double tagged control sample.
After the final event selection, the continuum backgrounds in double tagged con-701
trol sample are negligible. The same method as for the B+ → D∗0ℓ+νℓ control sample702
is used to correct the FEI efficiency and extra energy. The EROEextra distribution before703
and after the extra energy correction is shown in Figure 53. The data/MC ratio for704
each bin of N ROEγ distribution is shown in Table 18. These weights are applied to705
the signal MC sample of the hadronic decays to correct its N ROEγ distribution.706
88
0
2000
4000
6000
8000
Candidates / 0.1 GeV
Belle II preliminary L dt = 365 fb 1Double tagB ¯B
q¯q
MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0.5
1.0
1.5
DataMC
0
2000
4000
6000
8000
Candidates / 0.1 GeV
Belle II preliminary L dt = 365 fb 1Double tagB ¯B
q¯q
MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0.5
1.0
1.5
DataMC
```
FIG. 53. Extra energy distribution of double tagged control sample before (left) and after
```
```
(right) the ROE correction.
```
bin Data/MC ratio
0 1.10 ± 0.02
1 1.06 ± 0.02
2 0.99 ± 0.02
3 0.89 ± 0.02
4 0.86 ± 0.03
5 0.84 ± 0.04
6 0.80 ± 0.06
7 0.96 ± 0.12
8 0.55 ± 0.16
9 0 ± 0
TABLE 18. Data/MC ratio in each bin of EROEextra distribution of the double tagged control
sample.
6.3.6. Blind on-resonance data707
We also check the fitting variables on the blind on-resonance data. An enlarged708
SR cut is applied to fully remove the signal events. The EROEextra and τpCMS distributions709
after the full selection for each τ channels in the fit region are shown in Figures 54710
to 56. No significant data/MC discrepancies are observed. We observe a slight711
89
data/MC scaling difference. The µ, e and hadronic channels will be scaled by a712
factor 1.19, 1.21 and 1.38 respectively in the final fit.713
0
100
200
300
400
500
600
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.19 × MC
0
200
400
600
800
1000
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.19 × MC
FIG. 54. Distributions of the fitting variables in the blind on-resonance data after the full
selection for the µ channel
.
0
100
200
300
400
500
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.21 × MC
0
200
400
600
800
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.21 × MC
FIG. 55. Distributions of the fitting variables in the blind on-resonance data after the full
selection for the e channel
.
90
0
25
50
75
100
125
150
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.38 × MC
0
50
100
150
200
250
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
```
MC stat. unc.Data (blind)
```
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.38 × MC
FIG. 56. Distributions of the fitting variables in the blind on-resonance data after the full
selection for the hadronic channels
.
91
7. BR EXTRACTION714
This section describes the fitting procedure and the validation of the fit results.715
The fitting procedure is based on the pyhf package, which is a pure Python imple-716
mentation of the HistFactory model [20], with the help of the cabinetry package [21].717
7.1. Fitting procedure718
The fit is performed using the pyhf package, which allows for the construction of719
a statistical model based on the HistFactory framework. The fit is performed using720
the cabinetry package, which provides a convenient interface for constructing and721
fitting models. The model used in the fit is a binned likelihood function that includes722
the signal and background contributions, along with their associated statistical and723
systematic uncertainties. Then, cabinetry can directly compute the significance of724
the signal. To learn more about the pyhf package, see here.725
```
To fit the signal, EROEextra and pCMS (= τpCMS = pvis) are used. The fit is performed726
```
simultaneously in 3 orthogonal regions: one is for the µ channel, one is for the e727
channel, and one is for the two hadronic channel combined due to the low statistics.728
For the µ, e and hadronic channels, we create a 2D histogram of the EROEextra and τpCMS729
variables. By default, pyhf doesn’t support 2D histograms, so a flattening of the 2D730
histogram is performed. The EROEextra is binned into 10 bins in the range [0, 1.0] GeV,731
while τpCMS has a custom range for the leptonic and hadronic modes in order to avoid732
empty bins in the edges. For µ and e, τpCMS has 10 bins in the range [0.4, 2.2] GeV/c,733
for the hadronic modes, they have 10 bins in the range [0.85, 2.7] GeV/c. EROEextra and734
τpCMS variables are then flattened into a 1D histogram with a total of 100 bins, which735
is used as the input to the fit. The new variable is called global index.736
The fit is composed of 6 components:737
• Signal: the signal template is taken from truth-matched signal events from the738
signal-only sample.739
```
• Self-crossfeed (SCF): the SCF corresponds to miss-reconstructed signal events.740
```
The template is taken from non truth-matched signal events from the signal-741
only sample. The SCF is also present and removed from the charged back-742
```
ground using the information from GenMCTagTool (see here). More study on743
```
the SCF component is described in Appendix E.b.744
• non-BB background: the non-BB background is composed of qq, τ +τ − and745
ℓℓXX background. The template is taken from the MC15rd.746
92
• BB background: the BB background is composed of B0B0 and B+B− back-747
ground, where the SCF has been removed. The template is taken from the748
MC15rd.749
• Rare BB background: the rare BB background described in Section 8.7.2. The750
template is taken from privately generated samples.751
• Data: all the tests and fits are performed on Asimov dataset, which is taken752
from the MC samples. The final fit on data will be performed after unblinding.753
The signal and the SCF have the same normfactor parameter, which is used to754
scale without constrains the contribution in the fit. The signal normalization factor is755
called µ, and represents the signal fraction in the fit. The expected value of µ is 1, and756
we let it float in the range [−0.5, 7.0]. For BB, non-BB and rare BB backgrounds, a757
normsys parameter is used to scale the contribution, which varying the template by758
```
a factor [0.5, 2], [0.83, 1.21] (according to off-resonance/MC agreement) and [0.80,759
```
```
1.25] (according to the uncertainty on the rare BB branching fractions) respectively.760
```
The plots of EROEextra, τpCMS and the flattened 2D histogram of the 3 regions before761
the fit can be seen in Figures 57 to 62.762
Each contribution template plots are shown in Appendix F.763
764
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
100
200
300
400
500
Events / 0.10 GeV
Pre-fitchannel Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
0.5 1.0 1.5 2.0
pvis [GeV/c]
0
100
200
300
400
500
Events / 0.18 GeV/
c
Pre-fitchannel Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
FIG. 57. The EROEextra and pCMS distribution for the µ channel before the fit.
93
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
20
40
60
80
Events
Pre-fitchannel Belle II preliminary simulation
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
FIG. 58. The EROEextra and pCMS flattened distribution for the µ channel before the fit.
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
100
200
300
400
Events / 0.10 GeV
Pre-fite channel Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
0.5 1.0 1.5 2.0
pvis [GeV/c]
0
100
200
300
400
Events / 0.18 GeV/
c
Pre-fite channel Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
FIG. 59. The EROEextra and pCMS distribution for the e channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
20
40
60
Events
Pre-fite channel Belle II preliminary simulation
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
FIG. 60. The EROEextra and pCMS flattened distribution for the e channel before the fit.
94
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
25
50
75
100
125
Events / 0.10 GeV
Pre-fitHadronic chan. Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
1.0 1.5 2.0 2.5
pvis [GeV/c]
0
50
100
150
Events / 0.18 GeV/
c
Pre-fitHadronic chan. Belle II preliminary simulation
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
FIG. 61. The EROEextra and pCMS distribution for the hadronic channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
5
10
15
20
25
Events
Pre-fitHadronic chan. Belle II preliminary simulation
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
FIG. 62. The EROEextra and pCMS flattened distribution for the hadronic channel before the
fit.
95
The result of the fit, µ, is then directly used to compute the branching fraction765
of B+ → τ +ντ decay using:766
```
B(B+ → τ +ντ ) = B(B+ → τ +ντ )PDG × µ (11)
```
```
with B(B+ → τ +ντ )PDG = (1.09 ± 0.24) × 10−4 [4].767
```
We can also directly get the |Vub|, using the values from Table 19 and the fitted768
value of µ:769
|Vub| =
vu
```
ut 8πµB(B+ → τ +ντ )PDG
```
G2F mB+ m2τ

1 − m2τm2
B+
2
f 2B τB+
```
(12)
```
Parameter Value Source
```
GF (1.1663785 ± 0.0000006) × 10−5 GeV−2 [4]
```
mB+ 5.27941 ± 0.00007 GeV [4]
mτ 1.77693 ± 0.00009 GeV [4]
fB 0.190 ± 0.0013 GeV [5]
```
τB+ (2.489 ± 0.006) × 1012 GeV−1 [4]
```
TABLE 19. Inputs used to compute |Vub| from the fitted signal strength µ.
The fit is returning an up and down uncertainty on µ from the minos method and a770
symmetric uncertainty from minuit. The uncertainty is then split into statistical and771
systematic uncertainties. The statistical uncertainty is obtained in Section 7.2.1 using772
a toy study, while the systematic uncertainty is obtained in Section 8 by quadratically773
adding all the systematic uncertainties. The total uncertainty of the fit can be774
retrieved by quadratically adding the statistical and systematic uncertainties.775
The expected significance of the signal is also computed directly by cabinetry776
```
by fitting the Asimov dataset with the background-only hypothesis (µ = 0) and777
```
comparing it to the nominal fit.778
With all the systematics included by fitting on the Asimov dataset, the expected779
uncertainty on µ is found to be:780
```
µ = 1.000+0.424−0.404 ⇒ Significance = 2.6 σ (13)
```
7.2. Fit validation781
Multiple checks are performed to validate the fitting procedure, which are de-782
scribed in the next sections. For each checks, all the systematics described in Sec-783
96
tion 8 are included in the fit as nuisance parameters.784
7.2.1. Toy study785
A toy study is performed to check the validity of the fit under Poisson fluctuations.786
This allows us to get the statistical uncertainty on µ from the fit. The procedure is787
as follows:788
• Get the Asimov dataset from MC.789
• Fit the Asimov dataset to extract the best fit parameters.790
• Generate 1500 toy datasets from the Asimov dataset by fluctuating each bin of791
each region according to a Poisson distribution. For the pulls studies, the aux-792
iliary measurements for the nuisance parameters are also fluctuated according793
to a Gaussian distribution.794
```
• Fit each toy dataset with the expected MC, all the parameters (normalization795
```
```
factors and nuisance parameters) are free in the fit.796
```
• Extract the values of µ.797
We compute the pull for µ defined as:798
```
pull =
```
µfit − µtrue
σµfit
```
(14)
```
where µfit is the fitted value of µ, µtrue is the true value of µ used to generate the799
fake data sample, and σµfit is the total uncertainty on the fitted value of µ.800
Results of the toy study can be seen in Figure 63. The statistical uncertainty on801
µ is obtained from the width of the distribution of the fitted values of µ, which is802
expected to be:803
```
σstat = 0.32 ± 0.01 (15)
```
The pull distribution of µ is found to be centered around 0 with a width of804
compatible with 1 within 2 σ.805
97
0.5 0.0 0.5 1.0 1.5 2.0 2.5
mu values
0
50
100
150
Events
Toys values mu
```
G = 1.001 ± 0.010G = 0.315 ± 0.007 Fit
```
Data
4 2 0 2 4
mu pull
0
50
100
150
Events
Toys pull mu
```
G = 0.008 ± 0.030G = 0.956 ± 0.021 Fit
```
Data
```
FIG. 63. Distribution of the fitted values of µ from the toy study with a Gaussian fit (left)
```
```
and distribution of the pulls of µ with a Gaussian fit (right).
```
7.2.2. Bootstrap study and linearity check806
To further check the validity of the fit, we perform a study using the bootstrap807
method. The procedure is as follows:808
• For each sample used in the fit, generate a fake data sample by sampling with809
replacement from the original sample. The number of sampled candidates in810
the fake data sample is a Poisson fluctuation of the sum of the weights of the811
original sample multiplied by the Data/MC scale factor. The sampling uses812
the event weights as probabilities.813
```
• Fit the fake data sample with the expected MC, with all the parameters (nor-814
```
```
malization factors and nuisance parameters) free in the fit.815
```
• Extract the values of µ.816
This procedure is repeated 250 times for different signal scaling factors, varying817
from 0.0 to 3.5, corresponding to a significance of the signal varying from 0 to around818
5 σ.819
The mean of the values of µ as a function of the signal factor can be seen in820
Figure 64. A linear fit is performed to check the linearity of the fit. A good agreement821
is observed.822
98
0 1 2 3
Signal fraction
0
1
2
3
ax + b fit
```
a = 0.996 ± 0.006
```
```
b = 0.006 ± 0.012
```
mu
FIG. 64. Mean of the fitted values of µ as a function of the signal factor, with a linear fit.
99
8. SYSTEMATICS823
An additional set of corrections is applied to the MC samples, all leading to824
systematic uncertainties in the final measurement, added as nuisance parameters825
```
(NPs) in the fit. These corrections are described in the following sections.826
```
8.1. ROE corrections827
To implement the systematic uncertainties in the fit, we use the eigenvector828
method developed in the sysvar package. The covariance matrix is built by draw-829
ing 500 random variations of the correction weights according to their uncertainties.830
The covariance matrix is then diagonalized to obtain the eigenvectors and eigen-831
values. Each eigenvector represents a direction in the parameter space along which832
the weights can be varied to account for the systematic uncertainties. After some833
tests to see the impact of the number of eigenvectors, we decided to keep either as834
many eigendirections as fully correlated NPs as needed to reconstruct the original835
covariance matrix with differences smaller than 10−4, or a maximum between 1 and 9836
eigendirections per correction table according to their impact on the POI, whichever837
is smaller. In addition, all the remaining eigendirections are quadratically merged838
into an additional NP. This results in a total of 26 NPs for the ROE corrections839
systematics. These variations are then implemented in the fit as normsys+histosys840
NPs, where the normalization variation accounts for the overall change in yield due841
to the PID correction variation, and the histogram variation accounts for the shape842
change in the templates. The two components are kept fully correlated.843
We can provide detailed information for each individual systematic uncertainty844
using sysvar visualization API per request during the review. sysvar visualization845
API automatically plots the correction weight variations, the covariance matrix of846
the corrections, either explicitly defined or build from the different set of uncertain-847
ties, the varied templates across all reconstruction channels and the full correlation848
matrix across all bins, templates, reconstruction channels. We avoid providing this849
information for all systematics by default in this document since this would result850
to an extremely large number of plots. The setup used to generate the eigenvectors851
is available on gitlab.852
8.2. FEI corrections853
Using the same method as described in Section 8.1, the FEI corrections described854
in Section 5.1 are implemented in the fit as normsys+histosys NPs in the model.855
100
Each channel has 4 NPs associated with the continuum corrections, the BB calibra-856
tion corrections and the D0tag corrections for the µ channel. This results in a total of857
40 NPs for the FEI corrections systematics.858
8.3. pCMS corrections859
Using the same method as described in Section 8.1, the pCMS corrections described860
in Section 5.3 are implemented in the fit as normsys+histosys NPs in the model.861
Each channel can have up to 30 NPs associated with the pCMS correction, affecting862
only the BB candidates. This results in a total of 51 NPs for the pCMS corrections863
systematics.864
8.4. Tracking efficiency865
The tracking efficiency uncertainty is applied as a percentage per track. The866
current correction is 0.27%/track. Since we only have one charged track from the867
signal τ decay, the total uncertainty is 0.27% for all τ channels. This uncertainty is868
applied as a single histosys NP affecting all templates in all channels, varying the869
event weights up and down by 0.27%.870
8.5. Charged particle identification871
8.5.1. Corrections and implementation in the fit872
We correct for charged-particle identification efficiencies using the syscorr frame-873
work and apply the weights using the sysvar package. The PID correction tables874
used are:875
• µ efficiency correction for the FixedThresh09 PID selection for the muon chan-876
nel.877
• e efficiency correction for the FixedThresh09 PID selection for the electron878
channel.879
• π efficiency correction for the pionID noSVD > 0.6 selection for the hadronic880
channels.881
• K → µ fake rate correction for the FixedThresh09 PID selection for the muon882
channel.883
101
• K → e fake rate correction for the FixedThresh09 PID selection for the elec-884
tron channel.885
• K → π fake rate correction for the pionID noSVD > 0.6 selection for the886
hadronic channels.887
• π → µ fake rate correction for the FixedThresh09 PID selection for the muon888
channel.889
• π → e fake rate correction for the FixedThresh09 PID selection for the electron890
channel.891
The correction tables provide weights binned in track charge, momentum and892
```
polar angle. In each bin the weight is defined as the ratio of the efficiency (or fake893
```
```
rate) in data to the efficiency (or fake rate) in MC, measured on dedicated calibration894
```
samples. For each bin, the statistical and systematic uncertainties are provided.895
All the corrections are already provided in sysvar from the performance group,896
except the pion ID corrections, which are manually computed using syscorr. Fig-897
ure 65 shows the pion ID efficiency correction table used for the hadronic channels.898
0.297 0.489 0.698 1.047 1.344 1.675 2.007 2.321 2.618-2 0 -2 0 -2 0 -2 0 -2 0 -2 0 -2 0 -2 0 2theta and charge bins
0.30.6
0.91.2
1.51.8
2.12.4
2.73.0
3.33.5
4.04.5
p bins
0.89 0.88 0.86 0.86 0.94 0.93 0.94 0.94 0.94 0.94 0.95 0.95 0.94 0.96 0.77 0.880.96 0.97 0.95 0.97 1.00 0.97 0.99 0.99 0.97 0.96 0.94 0.95 1.04 1.07 1.03 1.00
0.98 0.99 0.99 1.00 0.99 0.97 0.96 0.96 0.94 0.94 0.94 0.94 0.95 1.00 0.69 0.801.04 1.03 0.98 0.97 0.96 0.95 0.96 0.95 0.94 0.94 0.95 0.95 0.98 1.01 0.43 0.60
1.03 1.02 0.96 0.96 0.95 0.95 0.95 0.94 0.95 0.94 0.96 0.95 0.94 0.98 0.53 0.221.05 1.02 0.95 0.95 0.93 0.93 0.95 0.94 0.95 0.94 0.97 0.96 0.89 0.89 0.40
1.01 1.01 0.95 0.94 0.93 0.93 0.94 0.96 0.94 0.94 0.95 0.96 0.82 0.81 0.39 0.131.03 1.02 0.94 0.95 0.91 0.91 0.95 0.95 0.94 0.94 0.96 0.95 0.76 0.77 0.37 0.32
1.04 1.03 0.95 0.95 0.92 0.93 0.96 0.96 0.95 0.96 0.95 0.96 0.75 0.76 0.36 0.281.04 1.02 0.97 0.97 0.92 0.93 0.96 0.98 0.95 0.97 0.97 0.95 0.79 0.75 0.35 0.30
1.05 1.02 1.00 0.99 0.95 0.93 0.97 0.98 0.99 0.97 1.01 1.00 0.72 0.71 0.07 0.001.04 1.04 0.99 1.02 0.94 0.95 0.98 1.00 1.00 0.97 0.96 0.95 0.77 0.39 0.00 0.00
1.10 1.03 1.06 1.09 0.93 0.93 1.00 0.99 0.90 1.01 0.93 -0.00
```
pi ratio table for cut "excludeSubdetectorFromPID(pi,SVD) > 0.6"
```
0.0
0.2
0.4
0.6
0.8
1.0
FIG. 65. Pion ID efficiency correction table used for the hadronic channels, computed
using syscorr. The weights are binned in pion momentum, θ and charge.
We use sysvar to implement this systematic. We decided to keep either as many899
eigendirections as fully correlated NPs as needed to reconstruct the original covari-900
ance matrix with differences smaller than 10−4, or a maximum of 2 to 3 eigendirec-901
tions per correction table according to the impact on the POI, whichever is smaller.902
This results in a total of 27 NPs for the charged PID corrections systematics. These903
variations are then implemented in the fit as normsys+histosys NPs, where the904
normalization variation accounts for the overall change in yield due to the PID cor-905
rection variation, and the histogram variation accounts for the shape change in the906
templates.907
102
8.5.2. light-release issue correction908
It was reported during the https://indico.belle2.org/event/16060/timetable/ that909
some charged PID corrections provided with old light-release versions were incor-910
rectly computed with new light-release versions due to changes in how the input911
parameters definitions. This issue affects the muon and electron PID corrections912
used in this analysis. To correct for this issue, the performance group recommended913
to compare the old and new light-release efficiencies and, if not too large, derive914
a systematic uncertainty from the difference. For the background candidates, we915
found that the difference in efficiency is less than 1% across the different samples.916
For the signal sample, we found a difference of 1.6%. To be conservative, we sum917
this difference linearly with the systematic uncertainty we get from the eigenvector918
method described previously.919
8.6. Neutral particle identification920
For the ρ channel, we apply a correction for the π0 identification efficiency for the921
eff40 selection using syscorr and sysvar. The correction table provides weights922
binned in π0 momentum and cos θ. In each bin the weight is defined as the ratio923
of the efficiency in data to the efficiency in MC, measured on dedicated calibration924
samples. For each bin, the statistical and systematic uncertainties are provided.925
Using the same eigenvector method as described in Section 8.5, we implement the926
systematic uncertainties in the fit. This results in a total of 3 NPs for the neutral927
PID corrections systematics.928
8.7. Branching fractions of background decays929
8.7.1. Main background composition930
The BB background template is our main background contribution in the fit. The931
composition of this background in the signal region can be seen in Figures 66 and 67.932
```
The dominant contributions come from semileptonic B decays, mainly D(∗)ℓν, Dℓν,933
```
π0ℓν. We can also find some rare background modes generated by PYTHIA, which is934
mostly Xuℓν decaying to charged or neutral pions. The composition of these rare935
background modes from PYTHIA are not well modeled in the generic MC generation,936
thus they are studied in detail in Section 8.7.2.937
103
```
(D*0 , D0 ) (30.14%)
```
```
(D*0 , D*0 ) (17.74%)
```
```
Other (<0.50%) (13.34%)
```
```
(D0 , D0 ) (8.29%)
```
```
(D*0 , 0 ) (4.61%)(PYTHIA (3 FS part. ), D*0 ) (3.46%)
```
BplusMode background modes
```
(D0 , D*00 ) (0.50%)
```
```
(D0 , D*02 ) (0.58%)
```
```
(D*0 , D*0 ) (0.58%)
```
```
(D*0 , D0 ) (0.65%)
```
```
(D0 , D0 ) (0.65%)
```
```
(D*0 , 0 ) (0.72%)
```
```
(D*0 , D0) (0.79%)
```
```
(D0 , D0 ) (0.79%)
```
```
(D0 , D0) (0.79%)
```
```
(D0 , K0 ) (0.79%)
```
```
(D*0 , D0 ) (0.87%)
```
```
(D*0 , D*02 ) (0.94%)
```
```
(D*0 , K0 ) (1.01%)
```
```
(D*0 , D0 ) (1.01%)
```
```
(D*0 , D*00 ) (1.08%)
```
```
(D0 , ) (1.23%)
```
```
(D*0 , D0 ) (1.51%)
```
```
(PYTHIA (3 FS part. ), D0 ) (1.66%)
```
```
(D0 , 0 ) (1.80%)
```
```
(D*0 , D*0 ) (1.87%)
```
```
(D*0 , ) (2.60%)
```
FIG. 66. Composition of the B+B− background in the signal region after the full selection.
104
```
(D* + , D+ ) (35.44%)
```
```
(D* + , D* + ) (19.16%)
```
```
(D+ , D+ ) (12.67%)
```
```
Other (<0.50%) (10.86%)
```
B0Mode background modes
```
(PYTHIA (4 FS part. ), D* + ) (0.75%)
```
```
(D+ , D+ ) (0.75%)
```
```
(D+ , + ) (0.75%)
```
```
(D+ , D+ ) (0.90%)
```
```
(D* + , D* +2 ) (1.06%)
```
```
(D* + , D+1 ) (1.06%)
```
```
(D* + , D+ ) (1.21%)
```
```
(D+ , D+1 ) (1.36%)
```
```
(D* + , + ) (1.51%)
```
```
(D+ , D* +0 ) (1.66%)(PYTHIA (3 FS part. ), D+ ) (1.81%)
```
```
(D* + , D* + ) (1.96%)
```
```
(D* + , D+ ) (1.96%)
```
```
(D* + , D+ ) (2.26%)
```
```
(PYTHIA (3 FS part. ), D* + ) (2.87%)
```
FIG. 67. Composition of the B0B0 background in the signal region after the full selection.
105
The uncertainties on the branching fractions of the various background modes938
can impact the shape and normalization of the BB template. To account for these939
uncertainties, each event has a new weight corresponding to the ratio of the branching940
fraction in the PDG [4] to the branching fraction in the MC generation. For the941
shape variations, sysvar is used to compute the upper and lower variations of the942
BB template by varying the branching fractions up and down by their uncertainties943
in the PDG. These variations are then implemented in the fit as normsys+histosys944
NPs. The branching fractions that are corrected and their uncertainties are listed in945
Tables 20 and 21. For all the decay modes, the HFLAV averages are taken if available.946
For some decay modes, the uncertainties are quite large due to the imprecise values947
in generic MC generation. In these cases, we use an arbitrary 100% uncertainty,948
indicated by a †. This uncertainty does not impact significantly the final result due949
to the small contribution of these modes in the signal region.950
After some tests to see the impact of the number of eigenvectors, we decided to951
keep either as many eigendirections as fully correlated NPs as needed to reconstruct952
the original covariance matrix with differences smaller than 10−4, or a maximum of953
6 eigendirections, whichever is smaller. We correct both Bsig and Btag branching954
fractions where applicable, on the BB, SCF and signal templates. This results in a955
total of 28 NPs for the branching fraction systematics.956
Decay mode PDG value ± unc. Dec File value
D∗0ℓν 0.0560 ± 0.0010 0.0549
D0ℓν 0.0226 ± 0.0007 0.0231
π0ℓν 0.000078 ± 0.0000027 0.000078
Xuℓν 0.00150 ± 0.00024 a 0.001724
D0π+ 0.00461 ± 0.00010 0.00467517
D∗0τ ν 0.0188 ± 0.0020 0.0141642
D∗00 ℓν 0.0013 ± 0.0019 0.00389
D∗02 ℓν 0.0032 ± 0.0003 0.00373
D0τ ν 0.0077 ± 0.0025 0.0069069
K0π+ 0.0000239 ± 0.0000006 0.00002368
D0ρ+ 0.0097 ± 0.0011 0.00939
a Partial to full BR + removed resonant contributions
TABLE 20. List of B+B− branching fractions of background modes corrected in the fit
and their uncertainties taken from the PDG [4] and D∗ℓν analysis [22].
106
Decay mode PDG value ± unc. Dec File value
D∗+ℓν 0.0487 ± 0.0009 0.0511
D+ℓν 0.0210 ± 0.0007 0.0214
D+τ ν 0.0098 ± 0.0021 0.0063986
Xuℓν 0.00132 ± 0.00022 a 0.001701
D+π− 0.00251 ± 0.00008 0.00252113
D∗+0 ℓν 0.0012 ± 0.0020 0.00362
D∗+τ ν 0.0148 ± 0.0009 0.0131838
π+ℓν 0.000150 ± 0.000005 0.00015
D+1 ℓν 0.00637 ± 0.00067b 0.00704
D∗+2 ℓν 0.0032 ± 0.0003 0.00347
a Partial to full BR + removed resonant contributions
b Combination of multiple BF from the PDG: Γ16 + Γ17 + Γ18
TABLE 21. List of B0B0 branching fractions of background modes corrected in the fit and
their uncertainties taken from the PDG [4] and D∗ℓν analysis [22].
8.7.2. Rare BB background957
The composition of the rare background modes generated by PYTHIA in the signal958
region is shown in Figures 68 to 71.959
107
```
X0u (60.47%)
```
```
K0LK0L (5.81%)
```
```
K * (4.65%)
```
```
K (4.65%)Xsu (4.65%)
```
B+ background modes
```
DK (1.16%)
```
```
Kn0p (1.16%)
```
```
J/ K0 (1.16%)
```
```
n0n0 (1.16%)
```
```
K0n0n0 (1.16%)
```
```
K * n0n0 (1.16%)
```
```
D0 (1.16%)
```
```
Kn0n0 (1.16%)
```
```
c 0 (1.16%)
```
```
D*0K * K0 (1.16%)
```
```
D0n0p (1.16%)
```
```
K (1.16%)0 0
```
```
(1.16%)
```
```
K * (2.33%)
```
```
Xsu (2.33%)
```
FIG. 68. Composition of the B+B− background from PYTHIA in the signal region after the
full selection.
108
```
Xu (60.47%)
```
```
Dn0p (4.65%)
```
B0 background modes
```
DK0K0 (2.33%)
```
```
DXu (2.33%)
```
```
D* (2.33%)
```
```
n0 (2.33%)
```
```
DK0K0 (2.33%)
```
```
DD* n0 (2.33%)
```
```
D*K * K0 0 (2.33%)
```
```
D0n0n0 (2.33%)
```
```
DDKK0 (2.33%)
```
```
D*0 0n0 (2.33%)
```
```
D n0 (2.33%)
```
```
DD*0 n0n0 (2.33%)
```
```
D0 0n0 (2.33%)
```
```
J/ 0n0 (2.33%)
```
```
Dn0n0 (2.33%)
```
FIG. 69. Composition of the B0B0 background from PYTHIA in the signal region after the
full selection.
109
```
(42.31%)
```
```
0 0 (32.69%)
```
```
KK (5.77%)
```
```
(5.77%)
```
```
0 (3.85%)
```
Xu from B+ background modes
```
n0n0 (1.92%)0
```
```
(1.92%)0 0
```
```
(1.92%)
```
```
(1.92%)0 0 0
```
```
(1.92%)
```
FIG. 70. Composition of the Xuℓν background from PYTHIA in the signal region after the
full selection for B+B−.
110
```
0 (62.96%)
```
```
KK0 (7.41%)
```
```
(7.41%)K*K0 (3.70%)
```
```
0 (3.70%)
```
```
0 0 (3.70%)
```
```
(3.70%)
```
```
KK * 0 0 (3.70%)
```
```
0 (3.70%)
```
Xu from B0 background modes
FIG. 71. Composition of the Xuℓν background from PYTHIA in the signal region after the
full selection for B0B0.
111
In generic MC generation, the Xu resonances part are simulated with EvtGen,960
while the non-resonant part and the contribution of broad higher resonances are961
covered by Pythia. To have a better understanding and simulation of the non-962
resonant part, we generated additional large MC samples of these modes to study963
the efficiency of the selection, and see if some remains in the signal region after the964
full selection. The modes with p¯p, n¯n, K+K− and K0LK0L in the final state, the965
form factors used in PYTHIA show non-uniform distribution [23, 24]. We generate966
10M events for each of these modes to have a good estimate of their contribution967
in the signal region. We also save the invariant mass of the hadronic system to968
do the reweighting due to the threshold enhancement. For the other modes, we969
generate 2M events each. Table 22 summarizes the different modes that could be a970
peaking background in the signal region, along with the number of events generated,971
reconstructed, and remaining after the full selection. The total efficiency of each972
mode is also provided.973
Table 23 shows the expected number of events in the signal region for each mode974
for LS1 dataset, taking into account the branching fractions from different sources975
and the non-uniform distribution of the hadronic system invariant mass where ap-976
plicable. For n¯nℓν, we use the same BF as for p¯pℓν from the PDG [4]. No mea-977
surement is available for the K0LK0Lℓν, so we estimate it from the measured BF of978
```
B+ → K+K−ℓν [24]. For the estimation of the branching fraction B(KLKLℓν)979
```
```
relative to the measured B(K+K−ℓν), we consider the following isospin relations:980
```
• For a pure 0++ resonance, the branching fractions satisfy981
```
B(K+K−) : B(KS KS ) : B(KLKL) = 2 : 1 : 1,
```
```
leading to B(KLKLℓν) = 12 B(K+K−ℓν).982
```
• For a pure 1−− resonance,983
```
B(K+K−) : B(KS KL) = 1 : 1,
```
implying no KLKL contribution.984
• In the absence of a resonance, a non-resonant K ¯K system yields approximately985
1
```
4 B(K
```
```
+K−ℓν).986
```
```
A conservative assumption of (1/4 ± 1/4) B(K+K−ℓν) is therefore adopted for987
```
```
B(KLKLℓν).988
```
For most of the modes, the efficiency after the full selection is quite small, of the989
order of 10−3 or less. The modes with the highest efficiency are the ones with n¯n and990
K0LK0L in the final state, reaching up to 1%. These two rare background modes are991
112
```
Decay mode # gen. # after reco. # after full sel. (# in SR) Tot. eff. (in SR) (%)
```
```
B+ → (a, b, f, h)a eνe 1992205 4247 709.0 (38.4) 0.0356 (0.0019)
```
```
B+ → (a, b, f, h)a µνµ 1888220 4217 644.4 (17.0) 0.0341 (0.0009)
```
```
B0 → (a, b)b eνe 1879042 2860 181.4 (7.1) 0.0097 (0.0004)
```
```
B0 → (a, b)b µνµ 1992213 2954 151.5 (11.2) 0.0076 (0.0006)
```
```
B+ → p¯peνe 9960825 3239 313.4 (51.9) 0.0031 (0.0005)
```
```
B+ → p¯pµνµ 9684430 3192 333.9 (63.5) 0.0034 (0.0007)
```
```
B+ → n¯neνe 9960867 154031 61406 (11229) 0.6164 (0.1127)
```
```
B+ → n¯nµνµ 9960876 149943 59442 (9955) 0.5968 (0.0999)
```
```
B+ → K+K−eνe 9175586 9061 2192.0 (181.9) 0.0239 (0.0020)
```
```
B+ → K+K−µνµ 9960818 9430 1994.8 (184.5) 0.0200 (0.0019)
```
```
B+ → K0LK0Leνe 9960858 163261 83884 (14113) 0.8421 (0.1417)
```
```
B+ → K0LK0Lµνµ 9960857 159840 83830 (12850) 0.8416 (0.1290)
```
```
a With a = a00, a10, a20; b = b10; f = f0, f1, f2; h = h1.
```
```
b With a = a00, a10, a20; b = b10.
```
TABLE 22. List of potentially peaking background modes from Xuℓν decays and the
number of events generated in dedicated signal only samples to study their contribution in
the signal region.
also expected to peak in the signal region. We decided to include these two modes in992
the fit as separate rare templates, each with a single normsys NP to account for the993
uncertainty on their branching fractions. The EROEextra and pCMS distributions of these994
two modes after the full selection can be seen in Figure 72. In addition, the shape995
of the two modes can vary independently thanks to two additional histosys NPs in996
the fit, one for each mode. The uncertainty on the shape is set to 10%, estimated997
```
from the B → Kνν analysis (see Appendix V and R). Finally, if these modes are998
```
found in generic MC samples, we remove them to avoid double counting.999
For the other modes, their expected contribution in the signal region is negligible1000
```
(less than 1 event each), so we do not include them in the fit.1001
```
113
Decay mode BF Expected # in SR
```
B+ → (a, b, f, h)eνe 0.0001a 0.7
```
```
B+ → (a, b, f, h)µνµ 0.0001a 0.4
```
```
B0 → (a, b)eνe 0.0002a 0.3
```
```
B0 → (a, b)µνµ 0.0002a 0.4
```
B+ → p¯peνe 0.0000058 [4] 0.01
B+ → p¯pµνµ 0.00000532 [4] 0.01
B+ → n¯neνe 0.0000058b 2.6
B+ → n¯nµνµ 0.00000532b 2.1
B+ → K+K−eνe 0.0000305 [24] 0.24
B+ → K+K−µνµ 0.0000305 [24] 0.22
B+ → K0LK0Leνe 0.000007625c 4.3
B+ → K0LK0Lµνµ 0.000007625c 3.9
```
a Belle decay.dec (inflated)
```
b Same as p¯pℓν
```
c BB+→K+K−ℓν × (1/4 ± 1/4)
```
TABLE 23. Expected number of events in the signal region for each potentially peaking
background mode from Xuℓν decays for LS1 dataset, taking into account the branching
fractions and the non-uniform distribution of the hadronic system invariant mass where
applicable.
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra
0.0
0.5
1.0
1.5
2.0
2.5
Events
Belle II preliminary simulationBelle II preliminary simulation
B + nn e + eB + nn +
B + K0LK0L e + eB + K0
LK0L +
0.5 1.0 1.5 2.0 2.5 3.0p
vis
0
1
2
3
Events
Belle II preliminary simulationBelle II preliminary simulation
B + nn e + eB + nn +
B + K0LK0L e + eB + K0
LK0L +
```
FIG. 72. EROEextra (left) and pCMS (right) distributions of the two rare background modes
```
kept in the fit. The number of events is normalized to LS1 dataset.
114
```
8.8. D(∗)ℓνℓ form factors1002
```
```
Since D(∗)ℓνℓ decays are the dominant background contribution, we include in1003
```
```
the fit a systematic linked to the form factors (FF) used to generate these decays.1004
```
FF model and its parametrization can alter the kinematic distributions of the decay1005
```
products, which can impact the shape of the fit templates. In Belle II, D(∗)ℓνℓ1006
```
decays assumes the BGL FF parametrization [25, 26]. We use the Helicity Amplitude1007
```
Module for Matrix Elements Reweighting (HAMMER) [27] software to reweight the1008
```
the dataset from an assumed FF parametrization to a target one. To find more1009
detailed information on HAMMER, please refer to [28, 29]. We chose the BLPRXP1010
FF parametrization [30] as target model to reweight both D∗ℓνℓ and Dℓνℓ decays.1011
Figures 73 and 74 show the set of parameters that have been used for the production1012
of the MC samples in Belle II and the target model respectively.1013
The output of HAMMER can directly be used to create the up and down vari-1014
```
ations of the D(∗)ℓνℓ templates in the fit using sysvar. BLPRXP is composed of1015
```
9 parameters, resulting in 9 NPs for each B meson decay, giving 18 NPs in total.1016
The variations are then implemented in the fit as normsys+histosys NPs on BB1017
samples, where the normalization variation accounts for the overall change in yield1018
due to the FF variation, and the histogram variation accounts for the shape change1019
in the templates.1020
115
ag_0 ag_1 af_0 af_1 aF1_1 aF1_2value 0.001 -0.0024 0.0005 0.0007 0.0003 -0.0037
unc 0.0 0.0 0.0 0.0 0.0 0.0
ag_0 ag_1 af_0 af_1 aF1_1 aF1_2
FF model parameters
0.003
0.002
0.001
0.000
0.001
Value
a+_1 a+_2 a+_3 a+_4 a0_1 a0_2 a0_3 a0_4value 0.0127 -0.095 0.393 -0.577 0.0114 -0.058 0.231 -0.789
unc 0.0001 0.003 0.157 2.244 0.0001 0.003 0.139 2.143
a+_1 a+_2 a+_3 a+_4 a0_1 a0_2 a0_3 a0_4FF model parameters
3
2
1
0
1
Value
a+_1 a+_2 a+_3 a+_4 a0_1 a0_2 a0_3 a0_4FF model parameters
a+_1
a+_2
a+_3
a+_4
a0_1
a0_2
a0_3
a0_4
FF model parameters
1 0.13 -0.028 -0.042 0 0.12 0.091 -0.11
0.13 1 -0.57 0.35 0 0.72 -0.17 0.029
-0.028 -0.57 1 -0.93 0 -0.41 0.65 -0.59
-0.042 0.35 -0.93 1 0 0.25 -0.69 0.75
0 0 0 0 1 0 0 0
0.12 0.72 -0.41 0.25 0 1 -0.44 0.24
0.091 -0.17 0.65 -0.69 0 -0.44 1 -0.93
-0.11 0.029 -0.59 0.75 0 0.24 -0.93 1
Correlation matrix BGLB2 B D ` ν
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
```
FIG. 73. Parameters used in the BGL parametrization for D(∗)ℓνℓ (top) and Dℓνℓ (bottom)
```
decays in the Belle II MC.
116
```
RhoStSq cSt mb DelMbc(mc) la2 eta1 rho1 chi21 phi1pvalue 1.1 2.39 4.71 1.3 0.12 0.34 -0.36 -0.12 0.25
```
unc 0.04 0.18 0.05 0.0 0.02 0.04 0.24 0.02 0.21
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
0
1
2
3
4
5
Value
RhoStSqcSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
RhoStSqcSt
mb
DelMbcla2
eta1
rho1
chi21
phi1p
FF model parameters
1 0.36 -0.72 0.11 0.034 0.42 -0.075 -0.47 -0.63
0.36 1 -0.46 0.048 -0.056 0.38 -0.076 -0.65 -0.11
-0.72 -0.46 1 0.028 0.008 -0.43 -0.007 0.37 0.36
0.11 0.048 0.028 1 0.009 0.11 0.48 -0.089 0.011
0.034 -0.056 0.008 0.009 1 -0.26 -0.094-0.034-0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075-0.076-0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089-0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D∗ ` ν
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
```
RhoStSq cSt mb DelMbc(mc) la2 eta1 rho1 chi21 phi1pvalue 1.1 2.39 4.71 1.3 0.12 0.34 -0.36 -0.12 0.25
```
unc 0.04 0.18 0.05 0.0 0.02 0.04 0.24 0.02 0.21
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
0
1
2
3
4
5
Value
RhoStSqcSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
RhoStSqcSt
mb
DelMbcla2
eta1
rho1
chi21
phi1p
FF model parameters
1 0.36 -0.72 0.11 0.034 0.42 -0.075 -0.47 -0.63
0.36 1 -0.46 0.048 -0.056 0.38 -0.076 -0.65 -0.11
-0.72 -0.46 1 0.028 0.008 -0.43 -0.007 0.37 0.36
0.11 0.048 0.028 1 0.009 0.11 0.48 -0.089 0.011
0.034 -0.056 0.008 0.009 1 -0.26 -0.094-0.034-0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075-0.076-0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089-0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D ` ν
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
```
FIG. 74. Target parameters used in the BLPRXP parametrization for D(∗)ℓνℓ (top) and
```
```
Dℓνℓ (bottom) decays for the reweighting with HAMMER.
```
117
8.9. MC statistics1021
The number of events in MC samples being finite, the associated statistical needs1022
to be taken into account. To do so, we use the staterror modifier in pyhf, which1023
is calculated as:1024
σbin =
sX
i
```
w2i (16)
```
where wi is the weight of each event in the bin. This creates one NP per bin of1025
each template to account for the statistical fluctuations. This results in 300 NPs for1026
the MC statistics systematics.1027
8.10. f+− and f001028
```
We vary the fraction of Υ (4S) → B+B−/Υ (4S) → B0B0 according to the value1029
```
obtained by HFLAV [31]: f+−/00 = 51.1 ± 1.1%.1030
```
8.11. Number of produced Υ (4S)1031
```
```
The total number of produced Υ (4S) between 2019 and 2021 is estimated to be1032
```
```
nΥ (4S) = (387.1 ± 5.6) × 106.1033
```
8.12. Summary of and impact of the systematics in the fit1034
A summary of the systematic uncertainties considered in this analysis is given in1035
Table 24 along with the number of associated NPs for each source. The summary1036
of the NPs distribution per sample and channel can be seen in Figure 75, and the1037
correlation matrix of all the NPs is provided in Appendix F.b.1038
118
Source Number of NPs
MC statistics 300
ROE corrections 26
pCMS corrections 51
Branching fractions of background decays 28
FEI corrections 40
Tracking efficiency 1
Neutral particle identification 3
Charged particle identification 27
```
D(∗)ℓνℓ form factors 18
```
BB normalization 1
non-BB normalization 1
Rare BB normalization 1
Rare background shape 2
SCF shape 1
Signal efficiency -
Fit bias -
Fraction of B+B− pairs -
```
Number of produced Υ (4S) -
```
TABLE 24. Summary of systematic uncertainties considered in the analysis and number
```
of associated nuisance parameters (NPs).
```
119
BBbarSCF
nonBBrareBB
signal
Fit region
BBbarSCF
nonBBrareBB
signal
e Fit region
B0_BF_sig_[0-6]B0_BF_tag_[0-6]Bp_BF_sig_[0-6]Bp_BF_tag_[0-6]
D0tag_mu_channel_[0-3]FEIcal_B0_mu_channel_[0-3]FEIcal_Bp_mu_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_mu_channel_BBbar_[0-9]
d0_FF_DlvDslv_tag_[0-8]d1_FF_DlvDslv_sig_[0-8]
d1_d0_pCMS_BB_mu_channel_[0-12]muID_K_fake_mu_channel_[0-3]
muID_eff_mu_channel
muID_pi_fake_mu_channel_[0-3]
tracking
ROE_nROEg_c2_bbS_32_kcorr_sig_mu_channel_SCF
SCF_shape
ROE_nROEg_c2_bbS_32_kcorr_c0_mu_channel_nonBB_[0-8]
d0_dmID_c0_mu_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_mu_channel_rareBB_[0-2]
rareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_mu_channel_signal_[0-4]
FEIcal_B0_e_channel_[0-3]FEIcal_Bp_e_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_e_channel_BBbar_[0-9]
d1_d0_pCMS_BB_e_channel_[0-12]
eID_K_fake_e_channel_[0-3]eID_eff_e_channel_[0-2]eID_pi_fake_e_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_sig_e_channel_SCF
ROE_nROEg_c2_bbS_32_kcorr_c0_e_channel_nonBB_[0-8]
d0_dmID_c0_e_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_e_channel_rareBB_[0-2]ROE_nROEg_c2_bbS_32_kcorr_sig_e_channel_signal_[0-4]
FEIcal_B0_hadronic_channel_[0-3]FEIcal_Bp_hadronic_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_hadronic_channel_BBbar_[0-9]
d1_d0_pCMS_BB_hadronic_channel_[0-24]
neutral_pi_hadronic_channel_[0-2]piID_eff_hadronic_channel_[0-2]piID_fake_hadronic_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_sig_hadronic_channel_SCF
ROE_nROEg_c2_bbS_32_kcorr_c0_hadronic_channel_nonBB_[0-8]
d0_dmID_c0_hadronic_channel_[0-3]
ROE_nROEg_c2_bbS_32_kcorr_BB_hadronic_channel_rareBB_[0-2]ROE_nROEg_c2_bbS_32_kcorr_sig_hadronic_channel_signal_[0-4]
mu
BBbar_normsysnonBB_normsysrareBB_normsys
staterror_ -Fit-regionstaterror_e-Fit-region
staterror_hadronic-Fit-region
BBbarSCF
nonBBrareBB
signal
hadronic Fit region
normfactor
shapefactor
shapesys
lumi
staterror
normsys + histosys
histosys
normsys
none
```
FIG. 75. Distribution of the number of nuisance parameters (NPs) per sample and channel.
```
120
8.12.1. Method to evaluate the impact1039
To estimate the impact of each source of systematic uncertainty on the signal1040
strength µ, we use the same method as described in the B0 → K∗0τ +τ − analysis [32],1041
which follows the methodology described in Ref. [33]:1042
• Every NP’s auxiliary measurement is shifted up and down by one standard1043
deviation, not fixed, and allowed to vary within the same constraint.1044
```
• A fit (with all NPs free) is performed for each variation, and the resulting signal1045
```
strength µ is saved.1046
• The difference between the nominal signal strength and the one obtained for1047
each variation is taken as the impact of that NP on µ.1048
• For each source of systematic uncertainty, the individual impacts of all associ-1049
ated NPs are summed in quadrature to obtain the total impact of that source1050
on µ.1051
```
This method has been validated (see here) and its cabinetry implementation is1052
```
used.1053
8.12.2. Impact of the systematics on the signal strength1054
The pull and the impact of each systematic can be found in Appendices F.c1055
and F.d. The impact of the different sources of systematic uncertainties on the1056
signal strength µ is summarized in Table 25. As expected, the dominant sources1057
of systematic uncertainties are the MC statistics, followed by the ROE corrections.1058
These two systematics are limited by statistics are are reducible in the future. The1059
total systematic uncertainty is obtained by summing in quadrature the individual1060
contributions. The final result for the signal strength including statistical and sys-1061
tematic uncertainties is:1062
```
µ = 1.0 ± 0.32 ± 0.29 (17)
```
which result in a expected branching fraction of:1063
```
B(B+ → τ +ντ ) = (1.09 ± 0.35(stat) ± 0.32(syst)) × 10−4 (18)
```
and an expected value of |Vub| of:1064
```
|Vub| = (4.14 ± 0.66(stat) ± 0.60(syst)) × 10−3 (19)
```
121
```
Source Systematics (= impact on µ) (%)
```
MC statistics 16.9
ROE corrections 17.6
pCMS corrections 5.8
Branching fractions of background decays 4.1
FEI corrections 6.3
Tracking efficiency 0.3
Neutral particle identification 0.5
Charged particle identification 3.8
```
D(∗)ℓνℓ form factors < 0.1
```
BB normalization 0.2
non-BB normalization 5.8
Rare BB normalization 0.8
Rare BB shape 0.1
SCF shape 1.4
Signal efficiency 10.0
Fit bias 1.6
```
Number of produced Υ (4S) 1.5
```
Fraction of BB pairs 2.1
Total 29.1 ± 1.0
TABLE 25. Impact of the different sources of systematic uncertainties on the signal
strength µ, with the total systematic uncertainty obtained by summing in quadrature
the individual contributions. The uncertainty on the total is obtained by summing the
positive and negative impacts separately.
122
9. UNBLINDING PROCEDURE1065
This section presents the unblinding procedure and the results for each step.1066
9.1. Unblinding steps1067
```
The unblinding procedure consists of the following steps (inspired by the B+ →1068
```
```
τ +ντ with hadronic tagging analysis [13]):1069
```
1. We check the µ channel, in which we expect the highest uncertainty. The1070
```
fitted POI is kept blinded (e.g. by adding a hidden offset). We first check the1071
```
pulls and pre-fit distributions. If everything looks good, we check the post-fit1072
distributions and compare the uncertainty to the expected one with Asimov1073
dataset.1074
2. We check the e channel. The fitted POI is kept blinded. The same procedure1075
as for the µ channel is applied.1076
3. We check the hadronic channels. The fitted POI is kept blinded. The same pro-1077
cedure as for the µ channel is applied. In addition, we compare the consistency1078
between the 3 blinded POIs.1079
4. We split the data into 3 independent sub-samples and perform the simultaneous1080
fit on the 3 channels on each sample. We check the consistency of the POI in1081
the different sub-samples. The fitted POIs are kept blinded.1082
5. We perform the final fit, unblind the central value of the fit and report the1083
final result.1084
9.2. Results of the unblinding steps1085
9.2.1. Step 1: µ channel1086
The µ channel is the one with the highest uncertainty. The pre-fit distributions1087
are shown in Figure 76. Good agreement is observed, but a slight increase in the1088
second bin of EROEextra is observed.1089
The pulls of each NPs are shown in Figure 77. The x-axis shows the pulls of the1090
NPs, where ˆθ is the post-fit value of the NPs, θ0 is the pre-fit central value, and1091
∆θ is the pre-fit uncertainty. The pulls of the NPs are all within 1σ. The non-BB1092
background normalization is pulled down by a factor 0.83, which is still compatible1093
123
with the expected distributions. Additionally, the trend is seen on the other channel.1094
The small uncertainty on the BB background normalization is due to the fact that1095
the normsys modifier is Gaussian constraining the normalization, and we have a1096
```
large range for this parameter (see Section 7.1).1097
```
The post-fit distributions are shown in Figure 78. The p-values of the fit is1098
```
p = 0.318, which is compatible with the expected distribution. Good agreement is1099
```
observed. The fitted POI is kept blind, and we find an uncertainty of:1100
```
σµ = 1.01+0.07−0.03 (20)
```
```
σµAsimov = 0.88+0.04−0.01 (21)
```
where the central value comes from MINUIT, while the upper and lower uncer-1101
tainties come from the MINOS algorithm. The uncertainty is slightly higher than the1102
expected one, but still compatible within 2σ.1103
124
0
100
200
300
400
500
Events / 0.18 GeV/
c
Pre-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
0.5 1.0 1.5 2.0
pvis [GeV/c]
0
2
DataMC
0
100
200
300
400
500
Events / 0.10 GeV
Pre-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
2
DataMC
0
20
40
60
80
100
Events
Pre-fit
channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
2
DataMC
FIG. 76. Pre-fit distributions for the µ channel. The top left plot shows the pCMS distri-
bution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
125
```
3 2 1 0 1 2 3(0)/
```
B0_BF_sig_var1B0_BF_sig_var2B0_BF_sig_var3
B0_BF_sig_var4B0_BF_sig_var5B0_BF_sig_var6
B0_BF_sig_var7B0_BF_tag_var1B0_BF_tag_var2
B0_BF_tag_var3B0_BF_tag_var4B0_BF_tag_var5
B0_BF_tag_var6B0_BF_tag_var7Bp_BF_sig_var1
Bp_BF_sig_var2Bp_BF_sig_var3Bp_BF_sig_var4
Bp_BF_sig_var5Bp_BF_sig_var6Bp_BF_sig_var7
Bp_BF_tag_var1Bp_BF_tag_var2Bp_BF_tag_var3
Bp_BF_tag_var4Bp_BF_tag_var5Bp_BF_tag_var6
Bp_BF_tag_var7D0tag_var1_mu_channelD0tag_var2_mu_channel
D0tag_var3_mu_channelD0tag_var4_mu_channelFEIcal_B0_var1_mu_channel
FEIcal_B0_var2_mu_channelFEIcal_B0_var3_mu_channelFEIcal_B0_var4_mu_channel
FEIcal_Bp_var1_mu_channelFEIcal_Bp_var2_mu_channelFEIcal_Bp_var3_mu_channel
```
FEIcal_Bp_var4_mu_channel3 2 1 0 1 2 3(
```
```
0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var10_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var4_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var6_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var7_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var9_mu_channel_BBbard0_FF_DlvDslv_tag_var1d0_FF_DlvDslv_tag_var2
d0_FF_DlvDslv_tag_var3d0_FF_DlvDslv_tag_var4d0_FF_DlvDslv_tag_var5
d0_FF_DlvDslv_tag_var6d0_FF_DlvDslv_tag_var7d0_FF_DlvDslv_tag_var8
d0_FF_DlvDslv_tag_var9d1_FF_DlvDslv_sig_var1d1_FF_DlvDslv_sig_var2
d1_FF_DlvDslv_sig_var3d1_FF_DlvDslv_sig_var4d1_FF_DlvDslv_sig_var5
d1_FF_DlvDslv_sig_var6d1_FF_DlvDslv_sig_var7d1_FF_DlvDslv_sig_var8
d1_FF_DlvDslv_sig_var9d1_d0_pCMS_BB_var10_mu_channeld1_d0_pCMS_BB_var11_mu_channel
d1_d0_pCMS_BB_var12_mu_channeld1_d0_pCMS_BB_var13_mu_channeld1_d0_pCMS_BB_var1_mu_channel
d1_d0_pCMS_BB_var2_mu_channeld1_d0_pCMS_BB_var3_mu_channeld1_d0_pCMS_BB_var4_mu_channel
d1_d0_pCMS_BB_var5_mu_channeld1_d0_pCMS_BB_var6_mu_channeld1_d0_pCMS_BB_var7_mu_channel
d1_d0_pCMS_BB_var8_mu_channel
```
3 2 1 0 1 2 3(0)/
```
d1_d0_pCMS_BB_var9_mu_channelmuID_K_fake_var1_mu_channelmuID_K_fake_var2_mu_channel
muID_K_fake_var3_mu_channelmuID_K_fake_var4_mu_channelmuID_eff_var1_mu_channel
muID_pi_fake_var1_mu_channelmuID_pi_fake_var2_mu_channelmuID_pi_fake_var3_mu_channel
muID_pi_fake_var4_mu_channeltrackingROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_SCF
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_SCFSCF_shapeROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_mu_channel_nonBBd0_dmID_c0_var1_mu_channel
d0_dmID_c0_var2_mu_channeld0_dmID_c0_var3_mu_channeld0_dmID_c0_var4_mu_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_rareBB
rareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBBROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var4_mu_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var5_mu_channel_signalBBbar_normsysnonBB_normsys
rareBB_normsys
FIG. 77. Pulls of all the NPs included in the fit for the µ channel.
126
0
100
200
300
400
500
Events / 0.18 GeV/
c
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
100
200
300
400
500
Events / 0.10 GeV
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
80
100
Events
Post-fit
channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 78. Post-fit distributions for the µ channel. The top left plot shows the pCMS dis-
tribution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
127
9.2.2. Step 2: e channel1104
The pre-fit distributions for the e channel are shown in Figure 79. Good agreement1105
is observed. The pulls of each NPs are shown in Figure 80. The pulls of the NPs1106
are all within 1σ. The post-fit distributions are shown in Figure 81. The p-values1107
of the fit is p = 0.460, which is compatible with the expected distribution. Good1108
agreement is observed. The fitted POI is kept blind, and we find an uncertainty of:1109
```
σµ = 0.85+0.05−0.02 (22)
```
```
σµAsimov = 0.84+0.05−0.01 (23)
```
128
0
100
200
300
400
Events / 0.18 GeV/
c
Pre-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
0.5 1.0 1.5 2.0
pvis [GeV/c]
0
2
DataMC
0
100
200
300
400
Events / 0.10 GeV
Pre-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
2
DataMC
0
20
40
60
80
Events
Pre-fit
e channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
2
DataMC
FIG. 79. Pre-fit distributions for the e channel. The top left plot shows the pCMS distri-
bution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
129
```
3 2 1 0 1 2 3(0)/
```
B0_BF_sig_var1B0_BF_sig_var2B0_BF_sig_var3
B0_BF_sig_var4B0_BF_sig_var5B0_BF_sig_var6
B0_BF_sig_var7B0_BF_tag_var1B0_BF_tag_var2
B0_BF_tag_var3B0_BF_tag_var4B0_BF_tag_var5
B0_BF_tag_var6B0_BF_tag_var7Bp_BF_sig_var1
Bp_BF_sig_var2Bp_BF_sig_var3Bp_BF_sig_var4
Bp_BF_sig_var5Bp_BF_sig_var6Bp_BF_sig_var7
Bp_BF_tag_var1Bp_BF_tag_var2Bp_BF_tag_var3
Bp_BF_tag_var4Bp_BF_tag_var5Bp_BF_tag_var6
Bp_BF_tag_var7FEIcal_B0_var1_e_channelFEIcal_B0_var2_e_channel
FEIcal_B0_var3_e_channelFEIcal_B0_var4_e_channelFEIcal_Bp_var1_e_channel
FEIcal_Bp_var2_e_channelFEIcal_Bp_var3_e_channelFEIcal_Bp_var4_e_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var10_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_BBbar
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_BBbar3 2 1 0 1 2 3(
```
```
0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var6_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var7_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var8_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_e_channel_BBbar
d0_FF_DlvDslv_tag_var1d0_FF_DlvDslv_tag_var2
d0_FF_DlvDslv_tag_var3d0_FF_DlvDslv_tag_var4
d0_FF_DlvDslv_tag_var5d0_FF_DlvDslv_tag_var6
d0_FF_DlvDslv_tag_var7d0_FF_DlvDslv_tag_var8
d0_FF_DlvDslv_tag_var9d1_FF_DlvDslv_sig_var1
d1_FF_DlvDslv_sig_var2d1_FF_DlvDslv_sig_var3
d1_FF_DlvDslv_sig_var4d1_FF_DlvDslv_sig_var5
d1_FF_DlvDslv_sig_var6d1_FF_DlvDslv_sig_var7
d1_FF_DlvDslv_sig_var8d1_FF_DlvDslv_sig_var9
d1_d0_pCMS_BB_var10_e_channeld1_d0_pCMS_BB_var11_e_channel
d1_d0_pCMS_BB_var12_e_channeld1_d0_pCMS_BB_var13_e_channel
d1_d0_pCMS_BB_var1_e_channeld1_d0_pCMS_BB_var2_e_channel
d1_d0_pCMS_BB_var3_e_channeld1_d0_pCMS_BB_var4_e_channel
d1_d0_pCMS_BB_var5_e_channeld1_d0_pCMS_BB_var6_e_channel
d1_d0_pCMS_BB_var7_e_channeld1_d0_pCMS_BB_var8_e_channel
d1_d0_pCMS_BB_var9_e_channeleID_K_fake_var1_e_channel
eID_K_fake_var2_e_channeleID_K_fake_var3_e_channel
```
3 2 1 0 1 2 3(0)/
```
eID_K_fake_var4_e_channeleID_eff_var1_e_channel
eID_eff_var2_e_channeleID_eff_var3_e_channel
eID_pi_fake_var1_e_channeleID_pi_fake_var2_e_channel
eID_pi_fake_var3_e_channeleID_pi_fake_var4_e_channel
trackingROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_SCF
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_SCFSCF_shape
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var3_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var7_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var8_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var9_e_channel_nonBBd0_dmID_c0_var1_e_channel
d0_dmID_c0_var2_e_channeld0_dmID_c0_var3_e_channel
d0_dmID_c0_var4_e_channelROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_rareBB
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_rareBB
rareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var3_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var4_e_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var5_e_channel_signalBBbar_normsysnonBB_normsys
rareBB_normsys
FIG. 80. Pulls of all the NPs included in the fit for the e channel.
130
0
100
200
300
400
Events / 0.18 GeV/
c
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
100
200
300
400
Events / 0.10 GeV
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
80
Events
Post-fit
e channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 81. Post-fit distributions for the e channel. The top left plot shows the pCMS dis-
tribution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
131
9.2.3. Step 3: hadronic channels and blinded POI comparison1110
The pre-fit distributions for the hadronic channels are shown in Figure 82. Good1111
agreement is observed.1112
The pulls of each NPs are shown in Figure 83. The pulls of the NPs are all1113
within 1σ. The post-fit distributions are shown in Figure 84. The first pCMS NP’s1114
uncertainty is small1115
The p-values of the fit is p = 0.473, which is compatible with the expected distri-1116
bution. Good agreement is observed. The fitted POI is kept blind, and we find an1117
uncertainty of:1118
```
σµ = 0.61+0.04−0.02 (24)
```
```
σµAsimov = 0.55+0.03−0.02 (25)
```
132
0
50
100
150
Events / 0.18 GeV/
c
Pre-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
1.0 1.5 2.0 2.5
pvis [GeV/c]
0
2
DataMC
0
50
100
150
Events / 0.10 GeV
Pre-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBMC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
0
2
DataMC
0
10
20
30
Events
Pre-fit
Hadronic chan. Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
MC stat. unc.
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
2
DataMC
FIG. 82. Pre-fit distributions for the hadronic channels. The top left plot shows the pCMS
distribution, the top right plot shows the EROEextra distribution, and the bottom plot shows
the flattened 2D distribution of both variables.
133
```
3 2 1 0 1 2 3(0)/
```
B0_BF_sig_var1B0_BF_sig_var2B0_BF_sig_var3
B0_BF_sig_var4B0_BF_sig_var5B0_BF_sig_var6
B0_BF_sig_var7B0_BF_tag_var1B0_BF_tag_var2
B0_BF_tag_var3B0_BF_tag_var4B0_BF_tag_var5
B0_BF_tag_var6B0_BF_tag_var7Bp_BF_sig_var1
Bp_BF_sig_var2Bp_BF_sig_var3Bp_BF_sig_var4
Bp_BF_sig_var5Bp_BF_sig_var6Bp_BF_sig_var7
Bp_BF_tag_var1Bp_BF_tag_var2Bp_BF_tag_var3
Bp_BF_tag_var4Bp_BF_tag_var5Bp_BF_tag_var6
Bp_BF_tag_var7FEIcal_B0_var1_hadronic_channelFEIcal_B0_var2_hadronic_channel
FEIcal_B0_var3_hadronic_channelFEIcal_B0_var4_hadronic_channelFEIcal_Bp_var1_hadronic_channel
FEIcal_Bp_var2_hadronic_channelFEIcal_Bp_var3_hadronic_channelFEIcal_Bp_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var10_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var4_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_hadronic_channel_BBbar
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var6_hadronic_channel_BBbar3 2 1 0 1 2 3(
```
```
0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_hadronic_channel_BBbar
d0_FF_DlvDslv_tag_var1d0_FF_DlvDslv_tag_var2d0_FF_DlvDslv_tag_var3
d0_FF_DlvDslv_tag_var4d0_FF_DlvDslv_tag_var5d0_FF_DlvDslv_tag_var6
d0_FF_DlvDslv_tag_var7d0_FF_DlvDslv_tag_var8d0_FF_DlvDslv_tag_var9
d1_FF_DlvDslv_sig_var1d1_FF_DlvDslv_sig_var2d1_FF_DlvDslv_sig_var3
d1_FF_DlvDslv_sig_var4d1_FF_DlvDslv_sig_var5d1_FF_DlvDslv_sig_var6
d1_FF_DlvDslv_sig_var7d1_FF_DlvDslv_sig_var8d1_FF_DlvDslv_sig_var9
d1_d0_pCMS_BB_var10_hadronic_channeld1_d0_pCMS_BB_var11_hadronic_channeld1_d0_pCMS_BB_var12_hadronic_channel
d1_d0_pCMS_BB_var13_hadronic_channeld1_d0_pCMS_BB_var14_hadronic_channeld1_d0_pCMS_BB_var15_hadronic_channel
d1_d0_pCMS_BB_var16_hadronic_channeld1_d0_pCMS_BB_var17_hadronic_channeld1_d0_pCMS_BB_var18_hadronic_channel
d1_d0_pCMS_BB_var19_hadronic_channeld1_d0_pCMS_BB_var1_hadronic_channeld1_d0_pCMS_BB_var20_hadronic_channel
d1_d0_pCMS_BB_var21_hadronic_channeld1_d0_pCMS_BB_var22_hadronic_channeld1_d0_pCMS_BB_var23_hadronic_channel
d1_d0_pCMS_BB_var24_hadronic_channeld1_d0_pCMS_BB_var25_hadronic_channeld1_d0_pCMS_BB_var2_hadronic_channel
d1_d0_pCMS_BB_var3_hadronic_channeld1_d0_pCMS_BB_var4_hadronic_channeld1_d0_pCMS_BB_var5_hadronic_channel
d1_d0_pCMS_BB_var6_hadronic_channel
```
3 2 1 0 1 2 3(0)/
```
d1_d0_pCMS_BB_var7_hadronic_channeld1_d0_pCMS_BB_var8_hadronic_channeld1_d0_pCMS_BB_var9_hadronic_channel
neutral_pi_var1_hadronic_channelneutral_pi_var2_hadronic_channelneutral_pi_var3_hadronic_channel
piID_eff_var1_hadronic_channelpiID_eff_var2_hadronic_channelpiID_eff_var3_hadronic_channel
piID_fake_var1_hadronic_channelpiID_fake_var2_hadronic_channelpiID_fake_var3_hadronic_channel
piID_fake_var4_hadronic_channeltrackingROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_SCF
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_SCFSCF_shapeROE_nROEg_c2_bbS_32_kcorr_c0_var1_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_hadronic_channel_nonBBd0_dmID_c0_var1_hadronic_channel
d0_dmID_c0_var2_hadronic_channeld0_dmID_c0_var3_hadronic_channeld0_dmID_c0_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_rareBB
rareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBBROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var4_hadronic_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var5_hadronic_channel_signalBBbar_normsysnonBB_normsys
rareBB_normsys
FIG. 83. Pulls of all the NPs included in the fit for the hadronic channels.
134
0
50
100
150
Events / 0.18 GeV/
c
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
1.0 1.5 2.0 2.5
pvis [GeV/c]
5
0
5
Data
MCData
0
50
100
150
Events / 0.10 GeV
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
10
20
30
Events
Post-fit
Hadronic chan. Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 84. Post-fit distributions for the hadronic channels. The top left plot shows the pCMS
distribution, the top right plot shows the EROEextra distribution, and the bottom plot shows
the flattened 2D distribution of both variables.
135
The compatibility between the 3 blinded POIs is shown in Figure 85 and Figure 86.1119
No discrepancy is observed between the 3 channels.1120
1.7 1.8 1.9 2.0 2.1
```
B(B + → τ+ντ) + common offset ×10 3
```
Hadronic channel
```
(1.78 ± 0.07) × 10 3
```
e channel
```
(1.78 ± 0.09) × 10 3
```
mu channel
```
(1.99 ± 0.11) × 10 3
```
```
µmean = (1.85 ± 0.05) × 10 3
```
FIG. 85. Comparison of the 3 blinded POIs for the 3 channels.
136
mu channele channel
Hadronic channel
Mean
mu channel
e channel
Hadronic channel
Mean
1.46 1.63 1.14
1.46 0.00 0.66
1.63 0.00 0.82
1.14 0.66 0.82
Pairwise significance between POI subsets
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Tension [ ]
FIG. 86. Significance between the 3 blinded POIs for the 3 channels, assuming independent
measurements.
9.2.4. Step 4: consistency checks on sub-samples1121
We split the data into 3 independent sub-samples and perform the simultaneous fit1122
on the 3 channels on each sample. The results are shown in Figure 87 and Figure 88.1123
No discrepancy is observed between the 3 sub-samples.1124
We also compare the 3 sub-samples with the 3 channels fits, and no discrepancy1125
is observed. The results are shown in Figure 89 and Figure 90.1126
137
1.70 1.75 1.80 1.85 1.90 1.95
```
B(B + → τ+ντ) + common offset ×10 3
```
Split 3
```
(1.82 ± 0.07) × 10 3
```
Split 2
```
(1.77 ± 0.07) × 10 3
```
Split 1
```
(1.87 ± 0.07) × 10 3
```
```
µmean = (1.82 ± 0.04) × 10 3
```
FIG. 87. Comparison of the 3 blinded POIs for the 3 sub-samples.
Split 1Split 2Split 3Mean
Split 1
Split 2
Split 3
Mean
0.97 0.50 0.60
0.97 0.48 0.59
0.50 0.48 0.01
0.60 0.59 0.01
Pairwise significance between POI subsets
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Tension [ ]
FIG. 88. Significance between the 3 blinded POIs for the 3 sub-samples, assuming inde-
pendent measurements.
138
1.7 1.8 1.9 2.0 2.1
```
B(B + → τ+ντ) + common offset ×10 3
```
```
Split 3(1.82 ± 0.07) × 10 3
```
```
Split 2(1.77 ± 0.07) × 10 3
```
```
Split 1(1.87 ± 0.07) × 10 3
```
```
Hadronic channel(1.78 ± 0.07) × 10 3
```
```
e channel(1.78 ± 0.09) × 10 3
```
```
mu channel(1.99 ± 0.11) × 10 3
```
```
µmean = (1.84 ± 0.03) × 10 3
```
FIG. 89. Comparison of the 6 blinded POIs for the 3 sub-samples and 3 channels.
mu channele channel
Hadronic channel
Split 1Split 2Split 3Mean
mu channel
e channel
Hadronic channel
Split 1
Split 2
Split 3
Mean
1.46 1.63 0.88 1.61 1.26 1.32
1.46 0.00 0.81 0.02 0.39 0.59
1.63 0.00 0.97 0.03 0.46 0.78
0.88 0.81 0.97 0.97 0.50 0.47
1.61 0.02 0.03 0.97 0.48 0.77
1.26 0.39 0.46 0.50 0.48 0.17
1.32 0.59 0.78 0.47 0.77 0.17
Pairwise significance between POI subsets
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Tension [ ]
FIG. 90. Significance between the 6 blinded POIs for the 3 sub-samples and 3 channels,
assuming independent measurements.
139
10. RESULTS1127
Once each unblinding steps have been successful, the simultaneous fit of the 31128
channels on the full LS1 dataset is performed. All the additional checks and studies1129
concerning the full unblinding are shown in Appendix G.1130
10.1. Fit distributions1131
The fit distributions for the µ, e and hadronic channels are shown in Figures 911132
to 93. Good agreement between the data and the fit model is observed in all channels.1133
140
0
100
200
300
400
500
Events / 0.18 GeV/
c
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
100
200
300
400
500
Events / 0.10 GeV
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
80
100
Events
Post-fit
channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 91. Post-fit distributions for the µ channel. The top left plot shows the pCMS dis-
tribution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
141
0
100
200
300
400
Events / 0.18 GeV/
c
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
100
200
300
400
Events / 0.10 GeV
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
80
Events
Post-fit
e channel Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 92. Post-fit distributions for the e channel. The top left plot shows the pCMS dis-
tribution, the top right plot shows the EROEextra distribution, and the bottom plot shows the
flattened 2D distribution of both variables.
142
0
50
100
150
Events / 0.18 GeV/
c
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
1.0 1.5 2.0 2.5
pvis [GeV/c]
5
0
5
Data
MCData
0
50
100
150
Events / 0.10 GeV
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
10
20
30
Events
Post-fit
Hadronic chan. Belle II preliminary L dt = 365 fb 1
Signal
SCF
Rare BB
Non -BB
BB
Data
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
5
0
5
Data

MC
Data
FIG. 93. Post-fit distributions for the hadronic channels. The top left plot shows the pCMS
distribution, the top right plot shows the EROEextra distribution, and the bottom plot shows
the flattened 2D distribution of both variables.
143
10.2. Fit results1134
We obtain the following signal strength:1135
```
µ = 2.19+0.490−0.462 (26)
```
Where the uncertainty is statistical + systematics. The p-value of the fit is p =1136
0.388.1137
The systematic table have been reproduced using the same method described in1138
Section 8.12.1.The table is shown Table 26. We then get the statistical uncertainty1139
from toy study using the same method described in Section 7.2.1. The result is:1140
```
µ = 2.19 ± 0.35(stat) ± 0.35(syst) (27)
```
144
```
Source Systematics (= impact on µ) (%)
```
MC statistics 21.6
ROE corrections 18.6
pCMS corrections 7.9
Branching fractions of background decays 4.4
FEI corrections 12.6
Tracking efficiency 0.7
Neutral particle identification 0.8
Charged particle identification 4.8
```
D(∗)ℓνℓ form factors 0.2
```
BB normalization 0.6
non-BB normalization 7.3
Rare BB normalization 1.5
Rare BB shape 0.5
SCF shape 3.1
Signal efficiency 10.0
Fit bias 1.6
```
Number of produced Υ (4S) 1.5
```
Fraction of BB pairs 2.1
Total 35.4 ± 1.1
TABLE 26. Impact of the different sources of systematic uncertainties on the signal
strength µ, with the total systematic uncertainty obtained by summing in quadrature
the individual contributions. The uncertainty on the total is obtained by summing the
positive and negative impacts separately.
10.3. Branching fraction1141
Taking into account the corrections from Section 6.1, the resulting branching1142
fraction is equal to:1143
```
B(B+ → τ +ντ ) = (2.17 ± 0.35(stat) ± 0.35(syst)) × 10−4 (28)
```
corresponding to a significance of 4.38σ.1144
```
We can also get the CKM matrix element |Vub|, according to Equation (12):1145
```
145
```
|Vub| = (5.83 ± 0.47(stat) ± 0.47(syst)) × 10−3 (29)
```
The compatibility of this result with the previous measurements is shown in Fig-1146
ure 94.1147
0 1 2 3 4 5
```
Branching Ratio of B + → τ+ντ (×10−4)
```
```
Belle II (365 fb−1, Semileptonic)
```
2.17 ± 0.35 ± 0.35 To be published
```
Belle II (365 fb−1, Hadronic)
```
```
1.24 ± 0.41 ± 0.19 PRD 112(2025)072002
```
```
Belle (711 fb−1, Semileptonic)
```
```
1.25 ± 0.28 ± 0.27 PRD 92(2015)5,051102
```
```
Belle (711 fb−1, Hadronic)
```
```
0.72 +0.270.25 ± 0.11 PRL 110(2013)13,131801
```
```
BaBar (426 fb−1, Hadronic)
```
```
1.83 +0.530.49 ± 0.24 PRD 88(2013)3,031102
```
```
BaBar (417.6 fb−1, Semileptonic)
```
```
1.7 ± 0.8 ± 0.2 PRD 81(2010)051101
```
PDG average
1.09 ± 0.24
SM
0.869+0.0310.03
FIG. 94. Comparison of the measured branching fraction with previous measurements.
146
APPENDIX1148
A. Event selection, additional material1149
This section shows additional material related to the event selection.1150
A.a. Additional pre-selection plots1151
Here are shown the data/MC agreement of the three variables used in the pre-1152
selection on the electron channel to remove the τ +τ − background described in Sec-1153
tion 3.3. Good agreement is observed between data and MC.1154
0.0
0.5
1.0
1.5
Candidates
×104 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
KtagelectronID
0.5
1.0
1.5
Data1.13 × MC
0
200
400
600
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
```
conv. γ InvM(`tag esig)
```
0.5
1.0
1.5
Data1.09 × MC
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0
```
conv. γ InvM(Dtag, daughters esig)
```
0.5
1.0
1.5
Data1.12 × MC
FIG. 95. Comparison between data and MC of the pre-selection variables used to remove
the τ +τ − background on the electron channel, described in Section 3.3.
147
A.b. Cumulative pre-selection tables for each channel1155
Here are shown the cumulative pre-selection tables for each channel.1156
1157
```
Cut (µ channel) #Sgn. Sgn. eff. cumul [%] #Bkg Bkg. ret. cumul [%]
```
```
Reconstruction (w/ FEI) 91 1.227 ± 0.004 63912 -
```
Btag decay mode ID 86 1.161 ± 0.029 52117 81.54 ± 0.15
p∗τ,sig 81 1.10 ± 0.04 47670 74.59 ± 0.17
p∗Dtag 81 1.10 ± 0.04 42419 66.37 ± 0.19
cos θ∗B,Dl 79 1.07 ± 0.04 32775 51.28 ± 0.20
```
R2(Event based) 67 0.90 ± 0.06 25893 40.51 ± 0.19
```
Btag R2 66 0.89 ± 0.06 25676 40.17 ± 0.19
cos θthurst,Btag,z 61 0.82 ± 0.06 22759 35.61 ± 0.19
π channel: pBsig 61 0.82 ± 0.06 22759 35.61 ± 0.19
ρ channel: pBsig 61 0.82 ± 0.06 22759 35.61 ± 0.19
e channel: Ktag electronID 61 0.82 ± 0.06 22759 35.61 ± 0.19
```
e channel: conv. γ InvM(ℓtag − esig) 61 0.82 ± 0.06 22759 35.61 ± 0.19
```
```
e channel: conv. γ InvM(Dtag, daughters − esig) 61 0.82 ± 0.06 22759 35.61 ± 0.19
```
TABLE 27. Cumulative signal efficiency and background retention after each pre-selection
cut for the µ channel. The number of truth-matched signal candidates and the number
of background candidates is obtained on the 1444 fb−1 MC sample and has been scaled
expected LS1 data luminosity.
148
```
Cut (e channel) #Sgn. Sgn. eff. cumul [%] #Bkg Bkg. ret. cumul [%]
```
```
Reconstruction (w/ FEI) 87 1.139 ± 0.004 55218 -
```
Btag decay mode ID 82 1.077 ± 0.028 44114 79.89 ± 0.17
p∗τ,sig 74 0.97 ± 0.04 40941 74.14 ± 0.19
p∗Dtag 74 0.97 ± 0.04 37938 68.71 ± 0.20
cos θ∗B,Dl 72 0.94 ± 0.05 30026 54.38 ± 0.21
```
R2(Event based) 60 0.79 ± 0.06 24529 44.42 ± 0.21
```
Btag R2 60 0.78 ± 0.06 24386 44.16 ± 0.21
cos θthurst,Btag,z 55 0.72 ± 0.06 22025 39.89 ± 0.21
π channel: pBsig 55 0.72 ± 0.06 22025 39.89 ± 0.21
ρ channel: pBsig 55 0.72 ± 0.06 22025 39.89 ± 0.21
e channel: Ktag electronID 53 0.69 ± 0.06 20930 37.90 ± 0.21
```
e channel: conv. γ InvM(ℓtag − esig) 52 0.69 ± 0.06 20659 37.41 ± 0.21
```
```
e channel: conv. γ InvM(Dtag, daughters − esig) 50 0.66 ± 0.06 19993 36.21 ± 0.20
```
TABLE 28. Cumulative signal efficiency and background retention after each pre-selection
cut for the e channel. The number of truth-matched signal candidates and the number
of background candidates is obtained on the 1444 fb−1 MC sample and has been scaled
expected LS1 data luminosity.
149
```
Cut (π channel) #Sgn. Sgn. eff. cumul [%] #Bkg Bkg. ret. cumul [%]
```
```
Reconstruction (w/ FEI) 53 1.158 ± 0.005 166520 -
```
Btag decay mode ID 50 1.10 ± 0.04 150759 90.53 ± 0.07
p∗τ,sig 50 1.09 ± 0.04 120771 72.53 ± 0.11
p∗Dtag 50 1.09 ± 0.04 91858 55.16 ± 0.12
cos θ∗B,Dl 49 1.06 ± 0.04 59624 35.81 ± 0.12
```
R2(Event based) 42 0.91 ± 0.06 35043 21.04 ± 0.10
```
Btag R2 42 0.91 ± 0.07 33918 20.37 ± 0.10
cos θthurst,Btag,z 38 0.83 ± 0.07 26159 15.71 ± 0.09
π channel: pBsig 35 0.77 ± 0.07 10652 6.40 ± 0.06
ρ channel: pBsig 35 0.77 ± 0.07 10652 6.40 ± 0.06
e channel: Ktag electronID 35 0.77 ± 0.07 10652 6.40 ± 0.06
```
e channel: conv. γ InvM(ℓtag − esig) 35 0.77 ± 0.07 10652 6.40 ± 0.06
```
```
e channel: conv. γ InvM(Dtag, daughters − esig) 35 0.77 ± 0.07 10652 6.40 ± 0.06
```
TABLE 29. Cumulative signal efficiency and background retention after each pre-selection
cut for the π channel. The number of truth-matched signal candidates and the number
of background candidates is obtained on the 1444 fb−1 MC sample and has been scaled
expected LS1 data luminosity.
150
```
Cut (ρ channel) #Sgn. Sgn. eff. cumul [%] #Bkg Bkg. ret. cumul [%]
```
```
Reconstruction (w/ FEI) 30 0.2825 ± 0.0015 103732 -
```
Btag decay mode ID 29 0.268 ± 0.011 92130 88.82 ± 0.10
p∗τ,sig 28 0.264 ± 0.013 80723 77.82 ± 0.13
p∗Dtag 28 0.264 ± 0.013 63032 60.76 ± 0.15
cos θ∗B,Dl 28 0.257 ± 0.015 42118 40.60 ± 0.15
```
R2(Event based) 22 0.206 ± 0.023 27949 26.94 ± 0.14
```
Btag R2 22 0.204 ± 0.023 27395 26.41 ± 0.14
cos θthurst,Btag,z 20 0.187 ± 0.024 21741 20.96 ± 0.13
π channel: pBsig 20 0.187 ± 0.024 21741 20.96 ± 0.13
ρ channel: pBsig 18 0.168 ± 0.025 11419 11.01 ± 0.10
e channel: Ktag electronID 18 0.168 ± 0.025 11419 11.01 ± 0.10
```
e channel: conv. γ InvM(ℓtag − esig) 18 0.168 ± 0.025 11419 11.01 ± 0.10
```
```
e channel: conv. γ InvM(Dtag, daughters − esig) 18 0.168 ± 0.025 11419 11.01 ± 0.10
```
TABLE 30. Cumulative signal efficiency and background retention after each pre-selection
cut for the ρ channel. The number of truth-matched signal candidates and the number
of background candidates is obtained on the 1444 fb−1 MC sample and has been scaled
expected LS1 data luminosity.
151
B. ROE mask optimization1158
B.a. FOM optimization1159
To choose which ROE masks to use for the analysis, an optimization study has1160
been performed. All the possible combinations of the cuts present in Table 31 have1161
been tested on 1 ab−1 of generic B+B− MC, where our signal is present. For each1162
combination, the full selection is applied and the expected signal significance is com-1163
puted using the formula:1164
```
Significance =
```
S√
S + B
```
(30)
```
where S is the number of signal events and B the number of B+B− background1165
events, both in the EROEextra < 1 GeV region.1166
In the end, the top 6 combinations with the highest expected significance have1167
been selected. The difference in significance between these top 6 combinations is1168
very small:1169
1. Energy cut and minC2TDist > 30 cm and beamBackgroundSuppression >1170
0.151171
2. Energy cut and minC2TDist > 30 cm and beamBackgroundSuppression >1172
0.15 and |clusterTiming| < 200 ns1173
3. Energy cut and minC2TDist > 30 cm and beamBackgroundSuppression > 0.31174
4. Energy cut and minC2TDist > 30 cm and beamBackgroundSuppression > 0.11175
5. Energy cut and minC2TDist > 30 cm and beamBackgroundSuppression >1176
0.15 and fakePhotonSuppression > 0.021177
6. Energy cut and minC2TDist > 30 cm and |clusterTiming| < 200 ns1178
with energy cut defined as: Ecluster > 0.100 GeV in the forward region or Ecluster >1179
0.055 GeV in the barrel region or Ecluster > 0.080 in the backward region.1180
After checking the distributions of the different ROE variables for these top 6 com-1181
binations, the first one has been chosen as the nominal ROE mask for the analysis,1182
as it shown the best data/MC agreement.1183
152
TABLE 31. ROE mask cuts values in the optimization study. All possible combinations
have been tested.
Variable operator Cut values
clusterE9E21 > 0.8, 0.9, 0.96
minC2TDist [ cm] > 20, 30, 40, 50, 60, 70, 80, 90, 100
beamBackgroundSuppression > 0.02, 0.05, 0.1, 0.15, 0.3, 0.5
fakePhotonSuppression > 0.02, 0.05, 0.1, 0.15, 0.3, 0.5
|clusterTiming| [ ns] < 200
|clusterTimingClusterErrorTiming| < 2
B.b. ROE correction uncertainty1184
The ROE correction systematic is proportional to the uncertainty of the first1185
```
bins of the photon multiplicity corrections (see Section 5.2). The mask optimization1186
```
study has been re-run taking into account the FOM from the last section, along with1187
the uncertainty of the 2 first bins of N ROEγ on the off-resonance data and on the1188
BDT sidebands for BB background. No improvement was found compared to the1189
nominal ROE mask, which was found to be part of the top combinations in this new1190
optimization study as well.1191
153
C. Background suppression, additional plots1192
C.a. Correlations1193
This section shows the correlations between the variables used for B+ → τ +ντ1194
background suppression. The method used to compute the correlations is the Pearson1195
correlation coefficient. The correlation coefficient r is defined as:1196
```
r(x, y) =
```
Pn
```
i=1(xi − ¯x)(yi − ¯y)pP
```
n
```
i=1(xi − ¯x)2
```
pPn
```
i=1(yi − ¯y)2
```
```
(31)
```
where xi and yi are the values of the two variables, ¯x and ¯y are the means of the1197
two variables, and n is the number of data points. The correlation coefficient can1198
take values between -1 and 1, where -1 indicates a perfect negative correlation, 01199
indicates no correlation, and 1 indicates a perfect positive correlation.1200
For each channel, the correlation matrix is shown for signal and background. In1201
```
addition, the two variables used in the fit (but not in the training) and the XGBoost1202
```
output are shown below and after the black line.1203
Btag cosTBzcos θ
∗Btag, Dl
```
Bsig cosTBTOnRemainingTracksnROETracksGoodthrustAxisCosThetaBtag thrustBmR2 (Event based)miss_thetaBtag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3
```
harmonicMomentThrust1
z
Btag KSFWVariables_hso01
τsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (
```
```
µ channel)
```
Btag cosTBzcos θ ∗Btag, Dl
Bsig cosTBTOnRemainingTracks
nROETracksGoodthrustAxisCosTheta
```
Btag thrustBmR2 (Event based)
```
miss_thetaBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1z
Btag KSFWVariables_hso01τsig pCMS
```
EROEextra c2_bbS_32 (with removal)XGBoost output (µ channel)
```
1.00 -0.01 -0.10 0.00 -0.00 0.39 0.03 -0.01 -0.02 0.06 0.03 -0.01 0.00 -0.00 -0.00 -0.01 0.04 -0.05-0.01 1.00 -0.01 -0.04 -0.03 -0.02 0.05 0.04 0.05 0.04 0.02 0.04 -0.01 0.01 0.02 -0.00 -0.22 -0.08
-0.10 -0.01 1.00 -0.00 -0.01 -0.09 -0.17 0.39 -0.01 -0.12 -0.07 0.05 0.00 -0.00 -0.00 -0.02 0.00 -0.120.00 -0.04 -0.00 1.00 0.22 -0.00 0.01 -0.00 -0.01 0.01 0.01 -0.00 -0.00 0.00 -0.00 0.01 0.04 -0.79
-0.00 -0.03 -0.01 0.22 1.00 -0.00 0.01 -0.00 -0.01 0.02 0.01 0.00 0.00 0.00 -0.01 0.01 0.02 -0.340.39 -0.02 -0.09 -0.00 -0.00 1.00 -0.01 -0.02 -0.02 0.01 0.01 -0.01 0.01 0.00 0.01 0.03 0.02 -0.08
0.03 0.05 -0.17 0.01 0.01 -0.01 1.00 0.52 0.02 0.44 0.35 0.06 -0.00 0.00 -0.01 0.06 0.01 0.01-0.01 0.04 0.39 -0.00 -0.00 -0.02 0.52 1.00 -0.02 0.29 0.21 0.04 -0.01 0.00 -0.00 -0.10 -0.01 -0.00
-0.02 0.05 -0.01 -0.01 -0.01 -0.02 0.02 -0.02 1.00 0.04 0.01 -0.01 0.21 0.00 -0.05 0.08 -0.01 -0.110.06 0.04 -0.12 0.01 0.02 0.01 0.44 0.29 0.04 1.00 -0.26 -0.22 -0.00 0.00 -0.01 0.05 0.04 0.05
0.03 0.02 -0.07 0.01 0.01 0.01 0.35 0.21 0.01 -0.26 1.00 -0.34 0.00 0.00 -0.00 0.02 0.01 -0.05-0.01 0.04 0.05 -0.00 0.00 -0.01 0.06 0.04 -0.01 -0.22 -0.34 1.00 -0.01 -0.00 -0.00 -0.01 0.00 -0.11
0.00 -0.01 0.00 -0.00 0.00 0.01 -0.00 -0.01 0.21 -0.00 0.00 -0.01 1.00 -0.00 0.01 -0.00 0.01 -0.02-0.00 0.01 -0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 -0.00 -0.00 1.00 -0.00 -0.00 -0.00 -0.00
-0.00 0.02 -0.00 -0.00 -0.01 0.01 -0.01 -0.00 -0.05 -0.01 -0.00 -0.00 0.01 -0.00 1.00 0.01 -0.00 0.02-0.01 -0.00 -0.02 0.01 0.01 0.03 0.06 -0.10 0.08 0.05 0.02 -0.01 -0.00 -0.00 0.01 1.00 -0.01 -0.11
0.04 -0.22 0.00 0.04 0.02 0.02 0.01 -0.01 -0.01 0.04 0.01 0.00 0.01 -0.00 -0.00 -0.01 1.00 -0.05-0.05 -0.08 -0.12 -0.79 -0.34 -0.08 0.01 -0.00 -0.11 0.05 -0.05 -0.11 -0.02 -0.00 0.02 -0.11 -0.05 1.00
```
Correlation matrix for mu decay (Sig. TM)
```
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
(a)
```
Btag cosTBzcos θ
∗Btag, Dl
```
Bsig cosTBTOnRemainingTracksnROETracksGoodthrustAxisCosThetaBtag thrustBmR2 (Event based)miss_thetaBtag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3
```
harmonicMomentThrust1
z
Btag KSFWVariables_hso01
τsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (
```
```
µ channel)
```
Btag cosTBzcos θ ∗Btag, Dl
Bsig cosTBTOnRemainingTracks
nROETracksGoodthrustAxisCosTheta
```
Btag thrustBmR2 (Event based)
```
miss_thetaBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1z
Btag KSFWVariables_hso01τsig pCMS
```
EROEextra c2_bbS_32 (with removal)XGBoost output (µ channel)
```
1.00 -0.01 -0.07 0.02 -0.00 0.38 0.03 0.04 -0.02 0.04 0.04 -0.01 0.02 -0.01 0.01 -0.07 0.02 -0.05-0.01 1.00 -0.01 -0.03 -0.01 -0.02 0.03 0.03 0.07 -0.00 0.05 0.06 0.00 0.00 0.01 -0.01 -0.05 -0.24
-0.07 -0.01 1.00 -0.00 0.02 -0.06 -0.15 0.39 0.00 -0.10 -0.05 0.07 0.00 0.00 -0.02 0.03 0.09 -0.140.02 -0.03 -0.00 1.00 0.41 0.01 -0.01 0.01 -0.03 -0.01 0.00 -0.00 -0.02 -0.00 0.00 -0.09 -0.13 -0.71
-0.00 -0.01 0.02 0.41 1.00 -0.00 -0.00 0.02 -0.01 0.00 0.01 0.01 -0.00 -0.01 0.01 -0.04 -0.07 -0.520.38 -0.02 -0.06 0.01 -0.00 1.00 -0.01 -0.00 -0.02 -0.00 0.01 -0.01 0.05 0.01 0.00 -0.02 0.03 -0.07
0.03 0.03 -0.15 -0.01 -0.00 -0.01 1.00 0.44 0.02 0.42 0.36 0.04 -0.00 -0.00 -0.02 0.03 0.00 0.040.04 0.03 0.39 0.01 0.02 -0.00 0.44 1.00 -0.01 0.24 0.21 0.06 0.00 -0.00 -0.01 -0.07 -0.00 -0.05
-0.02 0.07 0.00 -0.03 -0.01 -0.02 0.02 -0.01 1.00 0.05 0.01 -0.00 0.23 0.00 -0.04 0.07 -0.01 -0.060.04 -0.00 -0.10 -0.01 0.00 -0.00 0.42 0.24 0.05 1.00 -0.24 -0.21 -0.01 -0.01 -0.01 0.04 0.01 0.06
0.04 0.05 -0.05 0.00 0.01 0.01 0.36 0.21 0.01 -0.24 1.00 -0.33 -0.00 0.00 -0.02 -0.00 0.02 -0.04-0.01 0.06 0.07 -0.00 0.01 -0.01 0.04 0.06 -0.00 -0.21 -0.33 1.00 0.01 -0.00 -0.00 -0.03 0.06 -0.07
0.02 0.00 0.00 -0.02 -0.00 0.05 -0.00 0.00 0.23 -0.01 -0.00 0.01 1.00 0.00 0.03 -0.02 0.01 -0.01-0.01 0.00 0.00 -0.00 -0.01 0.01 -0.00 -0.00 0.00 -0.01 0.00 -0.00 0.00 1.00 0.00 0.00 0.00 0.00
0.01 0.01 -0.02 0.00 0.01 0.00 -0.02 -0.01 -0.04 -0.01 -0.02 -0.00 0.03 0.00 1.00 -0.03 0.02 0.02-0.07 -0.01 0.03 -0.09 -0.04 -0.02 0.03 -0.07 0.07 0.04 -0.00 -0.03 -0.02 0.00 -0.03 1.00 -0.13 0.04
0.02 -0.05 0.09 -0.13 -0.07 0.03 0.00 -0.00 -0.01 0.01 0.02 0.06 0.01 0.00 0.02 -0.13 1.00 0.09-0.05 -0.24 -0.14 -0.71 -0.52 -0.07 0.04 -0.05 -0.06 0.06 -0.04 -0.07 -0.01 0.00 0.02 0.04 0.09 1.00
```
Correlation matrix for mu decay (background)
```
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
(b)
```
```
FIG. 96. Correlation matrix for signal (a) and background (b) for the µ channel. The
```
variables used in the fit and the XGBoost output are shown below and after the black line.
154
Btag cosTBzcos θ
∗Btag, Dl
```
Bsig cosTBTOnRemainingTracksnROETracksGoodthrustAxisCosThetaBtag thrustBmR2 (Event based)miss_thetaBtag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3
```
harmonicMomentThrust1
z
Btag KSFWVariables_hso01
τsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (
```
```
e channel)
```
Btag cosTBzcos θ ∗Btag, Dl
Bsig cosTBTOnRemainingTracks
nROETracksGoodthrustAxisCosTheta
```
Btag thrustBmR2 (Event based)
```
miss_thetaBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1z
Btag KSFWVariables_hso01τsig pCMS
```
EROEextra c2_bbS_32 (with removal)XGBoost output (e channel)
```
1.00 -0.01 -0.08 0.01 0.00 0.39 0.03 0.01 -0.01 0.05 0.03 -0.01 0.01 -0.00 0.00 -0.01 0.03 -0.05-0.01 1.00 -0.00 -0.02 -0.03 -0.01 0.06 0.05 0.06 0.05 0.01 0.05 -0.01 0.01 0.02 0.00 -0.20 -0.09
-0.08 -0.00 1.00 0.01 0.00 -0.08 -0.17 0.35 -0.01 -0.12 -0.07 0.05 -0.01 -0.01 0.00 -0.02 0.02 -0.120.01 -0.02 0.01 1.00 0.22 0.00 0.01 0.00 -0.01 0.01 0.01 -0.00 0.00 -0.01 0.00 -0.00 0.03 -0.75
0.00 -0.03 0.00 0.22 1.00 0.01 0.00 0.00 -0.01 0.01 0.01 0.00 -0.00 0.01 -0.00 -0.01 0.01 -0.340.39 -0.01 -0.08 0.00 0.01 1.00 -0.01 -0.01 -0.00 0.01 -0.00 -0.00 0.03 0.01 0.00 0.02 0.01 -0.08
0.03 0.06 -0.17 0.01 0.00 -0.01 1.00 0.54 0.02 0.43 0.35 0.06 0.00 0.00 -0.00 0.05 0.02 0.020.01 0.05 0.35 0.00 0.00 -0.01 0.54 1.00 -0.02 0.31 0.23 0.03 -0.00 0.01 -0.00 -0.11 -0.01 0.03
-0.01 0.06 -0.01 -0.01 -0.01 -0.00 0.02 -0.02 1.00 0.04 0.01 -0.01 0.22 -0.00 -0.04 0.09 -0.00 -0.170.05 0.05 -0.12 0.01 0.01 0.01 0.43 0.31 0.04 1.00 -0.26 -0.21 -0.01 0.00 -0.01 0.04 0.04 0.04
0.03 0.01 -0.07 0.01 0.01 -0.00 0.35 0.23 0.01 -0.26 1.00 -0.35 0.00 0.01 -0.00 0.01 0.01 -0.05-0.01 0.05 0.05 -0.00 0.00 -0.00 0.06 0.03 -0.01 -0.21 -0.35 1.00 -0.00 -0.00 0.01 -0.01 0.01 -0.08
0.01 -0.01 -0.01 0.00 -0.00 0.03 0.00 -0.00 0.22 -0.01 0.00 -0.00 1.00 -0.00 0.01 -0.00 0.01 -0.04-0.00 0.01 -0.01 -0.01 0.01 0.01 0.00 0.01 -0.00 0.00 0.01 -0.00 -0.00 1.00 0.00 -0.01 -0.01 -0.00
0.00 0.02 0.00 0.00 -0.00 0.00 -0.00 -0.00 -0.04 -0.01 -0.00 0.01 0.01 0.00 1.00 0.02 -0.00 0.04-0.01 0.00 -0.02 -0.00 -0.01 0.02 0.05 -0.11 0.09 0.04 0.01 -0.01 -0.00 -0.01 0.02 1.00 -0.04 -0.20
0.03 -0.20 0.02 0.03 0.01 0.01 0.02 -0.01 -0.00 0.04 0.01 0.01 0.01 -0.01 -0.00 -0.04 1.00 -0.04-0.05 -0.09 -0.12 -0.75 -0.34 -0.08 0.02 0.03 -0.17 0.04 -0.05 -0.08 -0.04 -0.00 0.04 -0.20 -0.04 1.00
```
Correlation matrix for e decay (Sig. TM)
```
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
(a)
```
Btag cosTBzcos θ
∗Btag, Dl
```
Bsig cosTBTOnRemainingTracksnROETracksGoodthrustAxisCosThetaBtag thrustBmR2 (Event based)miss_thetaBtag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3
```
harmonicMomentThrust1
z
Btag KSFWVariables_hso01
τsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (
```
```
e channel)
```
Btag cosTBzcos θ ∗Btag, Dl
Bsig cosTBTOnRemainingTracks
nROETracksGoodthrustAxisCosTheta
```
Btag thrustBmR2 (Event based)
```
miss_thetaBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1z
Btag KSFWVariables_hso01τsig pCMS
```
EROEextra c2_bbS_32 (with removal)XGBoost output (e channel)
```
1.00 -0.01 -0.05 0.00 -0.01 0.37 0.02 0.04 -0.02 0.03 0.04 -0.01 0.02 -0.01 0.00 -0.03 0.02 -0.02-0.01 1.00 -0.00 -0.02 -0.01 -0.01 0.02 0.03 0.06 -0.01 0.05 0.06 -0.00 0.00 0.01 -0.01 -0.05 -0.23
-0.05 -0.00 1.00 0.00 0.01 -0.06 -0.16 0.38 -0.01 -0.10 -0.06 0.07 -0.00 -0.00 -0.03 0.01 0.10 -0.140.00 -0.02 0.00 1.00 0.40 0.00 -0.00 0.01 -0.03 -0.01 -0.00 0.00 -0.01 0.00 0.01 -0.06 -0.16 -0.70
-0.01 -0.01 0.01 0.40 1.00 -0.01 0.00 0.01 -0.01 0.00 0.01 0.01 0.00 0.01 -0.00 -0.03 -0.09 -0.530.37 -0.01 -0.06 0.00 -0.01 1.00 -0.02 -0.01 -0.01 0.00 -0.00 -0.01 0.09 -0.00 0.01 0.01 0.02 -0.04
0.02 0.02 -0.16 -0.00 0.00 -0.02 1.00 0.44 0.02 0.42 0.36 0.03 0.00 -0.01 -0.03 0.03 -0.00 0.040.04 0.03 0.38 0.01 0.01 -0.01 0.44 1.00 -0.01 0.24 0.21 0.05 -0.00 -0.00 -0.02 -0.07 -0.02 -0.04
-0.02 0.06 -0.01 -0.03 -0.01 -0.01 0.02 -0.01 1.00 0.05 0.01 -0.00 0.23 0.00 -0.06 0.08 -0.02 -0.090.03 -0.01 -0.10 -0.01 0.00 0.00 0.42 0.24 0.05 1.00 -0.25 -0.22 0.00 0.00 -0.01 0.03 0.02 0.05
0.04 0.05 -0.06 -0.00 0.01 -0.00 0.36 0.21 0.01 -0.25 1.00 -0.34 -0.00 -0.00 -0.02 0.01 0.02 -0.05-0.01 0.06 0.07 0.00 0.01 -0.01 0.03 0.05 -0.00 -0.22 -0.34 1.00 0.00 -0.00 0.00 -0.01 0.05 -0.07
0.02 -0.00 -0.00 -0.01 0.00 0.09 0.00 -0.00 0.23 0.00 -0.00 0.00 1.00 0.00 0.02 -0.01 0.00 -0.03-0.01 0.00 -0.00 0.00 0.01 -0.00 -0.01 -0.00 0.00 0.00 -0.00 -0.00 0.00 1.00 0.00 0.00 -0.00 -0.01
0.00 0.01 -0.03 0.01 -0.00 0.01 -0.03 -0.02 -0.06 -0.01 -0.02 0.00 0.02 0.00 1.00 -0.04 0.01 0.05-0.03 -0.01 0.01 -0.06 -0.03 0.01 0.03 -0.07 0.08 0.03 0.01 -0.01 -0.01 0.00 -0.04 1.00 -0.13 -0.04
0.02 -0.05 0.10 -0.16 -0.09 0.02 -0.00 -0.02 -0.02 0.02 0.02 0.05 0.00 -0.00 0.01 -0.13 1.00 0.11-0.02 -0.23 -0.14 -0.70 -0.53 -0.04 0.04 -0.04 -0.09 0.05 -0.05 -0.07 -0.03 -0.01 0.05 -0.04 0.11 1.00
```
Correlation matrix for e decay (background)
```
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
(b)
```
```
FIG. 97. Correlation matrix for signal (a) and background (b) for the e channel. The
```
variables used in the fit and the XGBoost are shown below and after the black line.
Btag cosTBTOcos
θ ∗Btag, Dl
nROETracksGoodnRemainingTracksBtag
thrustBm
```
R2 (Fox-Wolfram event based)
```
miss_theta
thrustAxisCosTheta
miss_E
Btag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3harmonicMomentThrust1harmonicMomentThrust3
z
Btag KSFWVariables_hso01
Btag deltaEτsig decaysτsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (hadronic channels)
```
Btag cosTBTOcos θ ∗Btag, Dl
nROETracksGoodnRemainingTracks
```
Btag thrustBmR2 (Fox-Wolfram event based)
```
miss_thetathrustAxisCosTheta
miss_EBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1harmonicMomentThrust3
zBtag KSFWVariables_hso01
Btag deltaEτsig decays
```
τsig pCMSEROEextra c2_bbS_32 (with removal)
```
```
XGBoost output (hadronic channels)
```
1.00 -0.03 0.01 0.01 -0.12 0.47 -0.01 -0.11 0.00 -0.07 -0.04 0.09 -0.01 0.01 -0.01 -0.02 -0.07 0.04 -0.04 0.03 -0.27-0.03 1.00 -0.02 -0.03 0.06 0.02 0.03 -0.01 -0.05 0.06 0.02 0.04 0.00 -0.00 0.01 0.02 0.38 0.01 -0.00 -0.21 0.02
0.01 -0.02 1.00 0.23 0.00 0.00 0.00 -0.00 0.00 0.01 0.01 0.01 0.00 -0.00 0.00 0.00 0.00 -0.00 0.00 0.01 -0.250.01 -0.03 0.23 1.00 0.00 0.01 -0.01 -0.01 0.01 0.01 0.00 0.00 -0.00 0.00 0.01 -0.00 -0.01 -0.01 -0.00 0.04 -0.48
-0.12 0.06 0.00 0.00 1.00 0.36 0.05 0.01 -0.03 0.46 0.35 0.03 -0.01 -0.02 0.00 -0.00 0.53 -0.05 0.02 0.02 0.050.47 0.02 0.00 0.01 0.36 1.00 -0.01 -0.01 -0.02 0.21 0.15 0.05 -0.00 0.01 0.00 -0.02 0.24 0.04 0.01 -0.01 -0.10
-0.01 0.03 0.00 -0.01 0.05 -0.01 1.00 0.06 -0.02 0.07 0.01 -0.01 0.22 0.10 0.00 -0.03 0.10 0.10 0.04 0.02 -0.20-0.11 -0.01 -0.00 -0.01 0.01 -0.01 0.06 1.00 0.02 0.02 0.01 -0.01 0.14 0.02 0.01 0.00 0.01 0.01 -0.01 0.02 -0.17
0.00 -0.05 0.00 0.01 -0.03 -0.02 -0.02 0.02 1.00 -0.01 -0.04 0.01 -0.00 -0.01 0.01 0.03 -0.07 -0.00 -0.04 0.10 -0.37-0.07 0.06 0.01 0.01 0.46 0.21 0.07 0.02 -0.01 1.00 -0.24 -0.22 -0.01 -0.02 0.01 0.00 0.58 -0.03 0.02 0.05 0.10
-0.04 0.02 0.01 0.00 0.35 0.15 0.01 0.01 -0.04 -0.24 1.00 -0.34 -0.00 -0.01 0.00 -0.00 0.23 -0.01 0.00 0.01 -0.030.09 0.04 0.01 0.00 0.03 0.05 -0.01 -0.01 0.01 -0.22 -0.34 1.00 -0.00 0.00 -0.01 0.00 -0.09 0.03 0.00 0.01 -0.15
-0.01 0.00 0.00 -0.00 -0.01 -0.00 0.22 0.14 -0.00 -0.01 -0.00 -0.00 1.00 0.41 -0.00 0.00 -0.01 -0.01 0.01 -0.00 -0.080.01 -0.00 -0.00 0.00 -0.02 0.01 0.10 0.02 -0.01 -0.02 -0.01 0.00 0.41 1.00 -0.00 -0.02 -0.02 -0.01 0.02 -0.00 -0.01
-0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.00 -0.01 -0.00 -0.00 1.00 0.00 0.01 0.01 -0.01 0.00 -0.01-0.02 0.02 0.00 -0.00 -0.00 -0.02 -0.03 0.00 0.03 0.00 -0.00 0.00 0.00 -0.02 0.00 1.00 0.01 0.00 -0.01 -0.00 -0.07
-0.07 0.38 0.00 -0.01 0.53 0.24 0.10 0.01 -0.07 0.58 0.23 -0.09 -0.01 -0.02 0.01 0.01 1.00 -0.03 0.01 -0.03 0.110.04 0.01 -0.00 -0.01 -0.05 0.04 0.10 0.01 -0.00 -0.03 -0.01 0.03 -0.01 -0.01 0.01 0.00 -0.03 1.00 -0.05 -0.02 -0.32
-0.04 -0.00 0.00 -0.00 0.02 0.01 0.04 -0.01 -0.04 0.02 0.00 0.00 0.01 0.02 -0.01 -0.01 0.01 -0.05 1.00 0.00 0.100.03 -0.21 0.01 0.04 0.02 -0.01 0.02 0.02 0.10 0.05 0.01 0.01 -0.00 -0.00 0.00 -0.00 -0.03 -0.02 0.00 1.00 -0.10
-0.27 0.02 -0.25 -0.48 0.05 -0.10 -0.20 -0.17 -0.37 0.10 -0.03 -0.15 -0.08 -0.01 -0.01 -0.07 0.11 -0.32 0.10 -0.10 1.00
```
Correlation matrix for hadronic decay (Sig. TM)
```
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
(a)
```
Btag cosTBTOcos
θ ∗Btag, Dl
nROETracksGoodnRemainingTracksBtag
thrustBm
```
R2 (Fox-Wolfram event based)
```
miss_theta
thrustAxisCosTheta
miss_E
Btag CleoConeCS_1Btag CleoConeCS_2Btag CleoConeCS_3harmonicMomentThrust1harmonicMomentThrust3
z
Btag KSFWVariables_hso01
Btag deltaEτsig decaysτsig pCMS
```
EROEextra c2_bbS_32 (with
```
```
removal)
```
```
XGBoost output (hadronic channels)
```
Btag cosTBTOcos θ ∗Btag, Dl
nROETracksGoodnRemainingTracks
```
Btag thrustBmR2 (Fox-Wolfram event based)
```
miss_thetathrustAxisCosTheta
miss_EBtag CleoConeCS_1
Btag CleoConeCS_2Btag CleoConeCS_3
harmonicMomentThrust1harmonicMomentThrust3
zBtag KSFWVariables_hso01
Btag deltaEτsig decays
```
τsig pCMSEROEextra c2_bbS_32 (with removal)
```
```
XGBoost output (hadronic channels)
```
1.00 0.01 0.01 -0.01 0.02 0.40 -0.03 -0.08 -0.00 0.01 0.11 0.20 -0.01 0.00 -0.01 0.03 0.02 0.03 -0.01 0.05 -0.290.01 1.00 -0.01 -0.03 0.04 0.04 0.03 -0.01 0.02 0.00 0.06 0.06 -0.00 -0.00 -0.00 -0.01 0.42 -0.01 -0.01 -0.03 -0.18
0.01 -0.01 1.00 0.41 -0.00 0.00 -0.00 -0.01 0.01 0.01 0.01 0.02 -0.01 -0.01 0.00 0.01 -0.00 0.01 -0.04 -0.06 -0.34-0.01 -0.03 0.41 1.00 -0.00 -0.00 -0.01 0.03 0.00 -0.00 0.01 -0.01 -0.01 -0.01 0.00 0.02 -0.02 0.01 -0.12 -0.13 -0.47
0.02 0.04 -0.00 -0.00 1.00 0.43 0.01 -0.01 0.02 0.39 0.38 0.06 -0.02 -0.04 -0.01 -0.02 0.45 -0.01 -0.05 -0.00 -0.020.40 0.04 0.00 -0.00 0.43 1.00 -0.02 0.01 0.00 0.22 0.24 0.10 -0.00 0.02 -0.00 0.04 0.27 -0.02 0.06 -0.01 -0.13
-0.03 0.03 -0.00 -0.01 0.01 -0.02 1.00 0.06 0.19 0.04 0.01 -0.02 0.28 0.13 0.01 -0.04 0.06 0.12 -0.06 -0.07 -0.21-0.08 -0.01 -0.01 0.03 -0.01 0.01 0.06 1.00 -0.00 0.00 0.00 -0.02 0.29 0.06 0.01 -0.00 -0.02 -0.00 -0.06 -0.00 -0.14
-0.00 0.02 0.01 0.00 0.02 0.00 0.19 -0.00 1.00 0.04 0.02 0.01 0.02 0.00 0.00 0.01 0.07 0.10 0.01 0.08 -0.350.01 0.00 0.01 -0.00 0.39 0.22 0.04 0.00 0.04 1.00 -0.19 -0.19 -0.01 -0.02 -0.00 -0.01 0.46 0.01 -0.02 0.01 0.05
0.11 0.06 0.01 0.01 0.38 0.24 0.01 0.00 0.02 -0.19 1.00 -0.29 -0.01 -0.02 -0.01 -0.00 0.29 0.02 -0.04 0.04 -0.110.20 0.06 0.02 -0.01 0.06 0.10 -0.02 -0.02 0.01 -0.19 -0.29 1.00 -0.01 0.00 -0.00 -0.00 -0.03 0.02 0.01 0.10 -0.14
-0.01 -0.00 -0.01 -0.01 -0.02 -0.00 0.28 0.29 0.02 -0.01 -0.01 -0.01 1.00 0.47 0.01 -0.01 -0.03 -0.01 -0.03 -0.01 -0.080.00 -0.00 -0.01 -0.01 -0.04 0.02 0.13 0.06 0.00 -0.02 -0.02 0.00 0.47 1.00 0.00 -0.05 -0.04 -0.01 0.02 -0.00 -0.01
-0.01 -0.00 0.00 0.00 -0.01 -0.00 0.01 0.01 0.00 -0.00 -0.01 -0.00 0.01 0.00 1.00 -0.01 -0.00 -0.00 -0.00 0.00 -0.000.03 -0.01 0.01 0.02 -0.02 0.04 -0.04 -0.00 0.01 -0.01 -0.00 -0.00 -0.01 -0.05 -0.01 1.00 -0.03 -0.00 0.02 -0.02 -0.05
0.02 0.42 -0.00 -0.02 0.45 0.27 0.06 -0.02 0.07 0.46 0.29 -0.03 -0.03 -0.04 -0.00 -0.03 1.00 0.00 -0.02 -0.03 -0.030.03 -0.01 0.01 0.01 -0.01 -0.02 0.12 -0.00 0.10 0.01 0.02 0.02 -0.01 -0.01 -0.00 -0.00 0.00 1.00 -0.05 0.02 -0.21
-0.01 -0.01 -0.04 -0.12 -0.05 0.06 -0.06 -0.06 0.01 -0.02 -0.04 0.01 -0.03 0.02 -0.00 0.02 -0.02 -0.05 1.00 -0.02 0.170.05 -0.03 -0.06 -0.13 -0.00 -0.01 -0.07 -0.00 0.08 0.01 0.04 0.10 -0.01 -0.00 0.00 -0.02 -0.03 0.02 -0.02 1.00 0.02
-0.29 -0.18 -0.34 -0.47 -0.02 -0.13 -0.21 -0.14 -0.35 0.05 -0.11 -0.14 -0.08 -0.01 -0.00 -0.05 -0.03 -0.21 0.17 0.02 1.00
```
Correlation matrix for hadronic decay (background)
```
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
(b)
```
```
FIG. 98. Correlation matrix for signal (a) and background (b) for the hadronic channels.
```
The variables used in the fit and the XGBoost are shown below and after the black line.
155
C.b. Variable importance1204
Below is a more detailed plot of the variable importance for each channel using1205
shapley beeswarm representation.1206
```
2.0 1.5 1.0 0.5 0.0SHAP value (impact on model output)
```
harmonicMomentThrust1
Btag cosTBz
Btag thrustBm
z
Btag CleoConeCS_1
miss_theta
thrustAxisCosTheta
Btag KSFWVariables_hso01
```
R2 (Event based)
```
Bsig cosTBTO
Btag CleoConeCS_2
Btag CleoConeCS_3
nROETracksGood
cos θ ∗Btag, Dl
nRemainingTracks
For mu channel, on testing sample
Low
High
Feature value
```
(a)
```
```
1.5 1.0 0.5 0.0SHAP value (impact on model output)
```
z
Btag cosTBz
harmonicMomentThrust1
Btag thrustBm
Btag CleoConeCS_1
thrustAxisCosTheta
Bsig cosTBTO
miss_theta
Btag CleoConeCS_3
Btag CleoConeCS_2
```
R2 (Event based)
```
nROETracksGood
Btag KSFWVariables_hso01
cos θ ∗Btag, Dl
nRemainingTracks
For e channel, on testing sample
Low
High
Feature value
```
(b)
```
```
2.5 2.0 1.5 1.0 0.5 0.0 0.5 1.0SHAP value (impact on model output)
```
harmonicMomentThrust3Btag thrustBm
```
R2 (Fox-Wolfram event based)
```
Btag KSFWVariables_hso01Btag CleoConeCS_1
harmonicMomentThrust1Btag CleoConeCS_3
nROETracksGoodBtag CleoConeCS_2
Btag deltaEmiss_theta
τsig decaysz
thrustAxisCosThetaBtag cosTBTO
miss_E
cos θ ∗Btag, DlnRemainingTracks
For hadronic channel, on testing sample
Low
High
Feature value
```
(c)
```
```
FIG. 99. The shapley value is used to evaluate the importance of each variable (see here).
```
The higher the absolute value of the shapley value, the more important the variable is to
```
separate signal from background. The color represents the value of the variable (orange
```
```
for high value, black for low value).
```
156
C.c. Data/MC agreement1207
This section shows the Data/MC agreement after pre-selection for each variables1208
used for B+ → τ +ντ background suppression.1209
1210
µ and e channels:1211
0
200
400
600
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
200
400
600
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Btag cosTBz
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 100. Data/MC agreement of Btag cosTBz for mu and e channels.
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
3 2 1 0 1
cos θ ∗Btag, Dl
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
3 2 1 0 1
cos θ ∗Btag, Dl
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 101. Data/MC agreement of cos θ∗Btag ,Dl for mu and e channels.
157
0
100
200
300
400
500
600
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Bsig cosTBTO
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
100
200
300
400
500
600
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8
Bsig cosTBTO
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 102. Data/MC agreement of Bsig cosTBTO for mu and e channels.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8 10 12
nRemainingTracks
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Candidates
×104 Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8 10 12
nRemainingTracks
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 103. Data/MC agreement of nRemainingTracks for mu and e channels.
158
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8
nROETracksGood
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8
nROETracksGood
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 104. Data/MC agreement of nROETracksGood for mu and e channels.
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 0.0 0.5 1.0
thrustAxisCosTheta
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 0.0 0.5 1.0
thrustAxisCosTheta
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 105. Data/MC agreement of thrustAxisCosTheta for mu and e channels.
159
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.6 0.7 0.8 0.9
Btag thrustBm
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.6 0.7 0.8 0.9
Btag thrustBm
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 106. Data/MC agreement of Btag thrustBm for mu and e channels.
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8 1.0
```
R2 (Fox-Wolfram event based)
```
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8 1.0
```
R2 (Fox-Wolfram event based)
```
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
```
FIG. 107. Data/MC agreement of R2 (Fox-Wolfram event based) for mu and e channels.
```
160
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0
miss_theta
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0
miss_theta
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 108. Data/MC agreement of miss theta for mu and e channels.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_1
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Candidates
×104 Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_1
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 109. Data/MC agreement of Btag CleoConeCS 1 for mu and e channels.
161
0
2000
4000
6000
8000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_2
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
2000
4000
6000
8000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_2
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 110. Data/MC agreement of Btag CleoConeCS 2 for mu and e channels.
0
2000
4000
6000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_3
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
1000
2000
3000
4000
5000
6000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_3
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 111. Data/MC agreement of Btag CleoConeCS 3 for mu and e channels.
162
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.0 0.1 0.2 0.3 0.4
aplanarity
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.0 0.1 0.2 0.3 0.4
aplanarity
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 112. Data/MC agreement of aplanarity for mu and e channels.
0
500
1000
1500
2000
2500
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75
harmonicMomentThrust1
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75
harmonicMomentThrust1
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 113. Data/MC agreement of harmonicMomentThrust1 for mu and e channels.
163
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.4 0.2 0.0 0.2 0.4
harmonicMomentThrust3
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.4 0.2 0.0 0.2 0.4
harmonicMomentThrust3
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 114. Data/MC agreement of harmonicMomentThrust3 for mu and e channels.
0
1000
2000
3000
4000
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.15 0.10 0.05 0.00 0.05 0.10 0.15
z
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
1000
2000
3000
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.15 0.10 0.05 0.00 0.05 0.10 0.15
z
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 115. Data/MC agreement of ∆z for mu and e channels.
164
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.1 0.0 0.1 0.2
Btag KSFWVariables_hso01
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
0
250
500
750
1000
1250
Candidates
Belle II preliminary L dt = 365 fb-1e channel
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.1 0.0 0.1 0.2
Btag KSFWVariables_hso01
0.5
1.0
1.5
Data1.12 × MC
```
(b)
```
FIG. 116. Data/MC agreement of Btag KSFWVariables hso01 for mu and e channels.
165
hadronic channels:1212
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.0 0.2 0.4 0.6 0.8
Btag cosTBTO
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 117. Data/MC agreement of Btag cosTBTO for hadronic channels.
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
3 2 1 0 1
cos θ ∗Btag, Dl
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 118. Data/MC agreement of cos θ∗Btag ,Dl for hadronic channels.
166
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8
nROETracksGood
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 119. Data/MC agreement of nROETracksGood for hadronic channels.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Candidates
×104 Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 2 4 6 8 10 12
nRemainingTracks
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 120. Data/MC agreement of nRemainingTracks for hadronic channels.
167
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.6 0.7 0.8 0.9
Btag thrustBm
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 121. Data/MC agreement of Btag thrustBm for hadronic channels.
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.4 0.6 0.8 1.0
```
R2 (Fox-Wolfram event based)
```
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
```
FIG. 122. Data/MC agreement of R2 (Fox-Wolfram event based) for hadronic channels.
```
168
0
200
400
600
800
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 1.0 1.5 2.0 2.5 3.0
miss_theta
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 123. Data/MC agreement of miss theta for hadronic channels.
0
200
400
600
800
1000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.5 0.0 0.5 1.0
thrustAxisCosTheta
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 124. Data/MC agreement of thrustAxisCosTheta for hadronic channels.
169
0
500
1000
1500
2000
2500
3000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 5 10 15 20 25 30
miss_E
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 125. Data/MC agreement of miss E for hadronic channels.
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Candidates
×104 Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_1
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 126. Data/MC agreement of Btag CleoConeCS 1 for hadronic channels.
170
0
2000
4000
6000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_2
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 127. Data/MC agreement of Btag CleoConeCS 2 for hadronic channels.
0
1000
2000
3000
4000
5000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0 1 2 3 4 5
Btag CleoConeCS_3
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 128. Data/MC agreement of Btag CleoConeCS 3 for hadronic channels.
171
0
500
1000
1500
2000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.75 0.50 0.25 0.00 0.25 0.50 0.75
harmonicMomentThrust1
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 129. Data/MC agreement of harmonicMomentThrust1 for hadronic channels.
0
500
1000
1500
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.4 0.2 0.0 0.2 0.4
harmonicMomentThrust3
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 130. Data/MC agreement of harmonicMomentThrust3 for hadronic channels.
172
0
1000
2000
3000
4000
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.15 0.10 0.05 0.00 0.05 0.10 0.15
z
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 131. Data/MC agreement of ∆z for hadronic channels.
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
0.2 0.1 0.0 0.1 0.2
Btag KSFWVariables_hso01
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 132. Data/MC agreement of Btag KSFWVariables hso01 for hadronic channels.
173
0
250
500
750
1000
1250
1500
Candidates
Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
2.0 1.5 1.0 0.5 0.0 0.5
Btag deltaE
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 133. Data/MC agreement of Btag deltaE for hadronic channels.
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Candidates
×104 Belle II preliminary L dt = 365 fb-1+ channels
XXττ
ccss
dduu
B0B0B+B−
49M Signal ×0.2MC stat. unc.
Data
3 4 5 6 7
τsig decays
0.5
1.0
1.5
Data1.06 × MC
```
(a)
```
FIG. 134. Data/MC agreement of τsig decays for hadronic channels.
174
D. Corrections, additional plots1213
D.a. ROE corrections validation with the extra track SB control sample1214
The ROE corrections method is also validated using the extra track SB control1215
```
sample (see Section 2) where we don’t expect signal. The distributions before and1216
```
after step 1 are shown in Figures 135 and 136. The photon multiplicity N ROEγ and1217
```
the EROEextra before and after step 2 (a) are shown in Figures 137 and 138, and before1218
```
```
and after the step 2 (b) are shown in Figures 139 and 140. The final distributions1219
```
with all corrections applied are shown in Figure 141 for after the pre-selection. No1220
data/MC discrepancy is observed in the EROEextra distribution after all corrections.1221
175
0
1
2
3
4
5
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 1 2 3 4 5
EROEextra c2_bbS_32
0.5
1.0
1.5
Data0.94 × MC
```
(a)
```
0
1
2
3
4
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.00 × MC
```
(b)
```
0
1
2
3
4
Candidates
×104 Belle II preliminary L dt = 365 fb-1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 1 2 3 4 5
EROEextra c2_bbS_32
0.5
1.0
1.5
Data0.98 × MC
```
(c)
```
0
1
2
3
Candidates
×104 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data1.05 × MC
```
(d)
```
```
FIG. 135. Comparison between data and MC of EROEextra for µ and e decays before (left) and
```
```
after (right) first step of the correction.
```
176
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 1 2 3 4 5
EROEextra c2_bbS_32
0.5
1.0
1.5
Data0.91 × MC
```
(a)
```
0.0
0.5
1.0
1.5
2.0
2.5
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data0.97 × MC
```
(b)
```
0
1
2
3
Candidates
×104 Belle II preliminary L dt = 365 fb-1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0 1 2 3 4 5
EROEextra c2_bbS_32
0.5
1.0
1.5
Data0.90 × MC
```
(c)
```
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Candidates
×104 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0 2.5
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data0.97 × MC
```
(d)
```
```
FIG. 136. Comparison between data and MC of EROEextra for π and ρ decays before (left) and
```
```
after (right) first step of the correction.
```
177
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1e channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(d)
```
FIG. 137. Comparison between off-resonance data and MC of N ROEγ for each τ decay.
178
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 42 fb 1e channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 42 fb 1channel
Off-res MCOff-res MC corr
Off-res data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(d)
```
FIG. 138. Comparison between off-resonance data and MC of EROEextra for each τ decay after
reweighting each bin of the N ROEγ distribution to its data/MC ratio.
179
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 365 fb 1channel
BB MCBB MC corr
BB Data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.00
0.05
0.10
0.15
0.20
Event density
Belle II preliminary L dt = 365 fb 1e channel
BB MCBB MC corr
BB Data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.00
0.05
0.10
0.15
Event density
Belle II preliminary L dt = 365 fb 1+ channels
BB MCBB MC corr
BB Data
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
FIG. 139. Comparison between on-resonance BB data and MC of N ROEγ for each τ decay.
180
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb 1channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(a)
```
0.0
0.2
0.4
0.6
0.8
Event density
Belle II preliminary L dt = 365 fb 1e channel
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(b)
```
0.0
0.2
0.4
0.6
Event density
Belle II preliminary L dt = 365 fb 1+ channels
BB MCBB MC corr
BB Data
0.0 0.5 1.0 1.5 2.0
```
EROEextra c2_bbS_32 (with removal)
```
0.5
1.0
1.5
Data/MC
```
(c)
```
FIG. 140. Comparison between on-resonance BB data and MC of EROEextra for each τ decay
after reweighting each bin of the N ROEγ distribution to its data/MC ratio.
181
0
1
2
3
4
Candidates / 0.10 GeV
×10
4 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.01 × MC
```
(a)
```
0
1
2
3
Candidates / 0.10 GeV
×10
4 Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.05 × MC
```
(b)
```
0.0
0.5
1.0
1.5
2.0
2.5
Candidates / 0.10 GeV
×10
4 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data0.98 × MC
```
(c)
```
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Candidates / 0.10 GeV
×10
4 Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data0.97 × MC
```
(d)
```
FIG. 141. Comparison between data and MC of EROEextra for each τ decay with all corrections
after pre-selection.
182
D.b. BDT sidebands, additional checks1222
To further check the ROE corrections, we split the BDT sidebands into 2 sub-1223
```
samples, one more background like (BDT score < BDT cut /2) and one more signal1224
```
```
like (BDT score between BDT cut /2 and BDT cut). The EROEextra distributions for1225
```
each τ decay in the two sub-samples are shown in Figures 142 and 143. No data/MC1226
discrepancy is observed in the EROEextra distribution in both sub-samples after applying1227
all corrections.1228
0
100
200
300
400
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.21 × MC
0
100
200
300
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.22 × MC
0
50
100
150
200
250
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.24 × MC
0
100
200
300
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.14 × MC
FIG. 142. EROEextra distribution for each τ decay in the low BDT sideband.
183
0
100
200
300
400
500
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.20 × MC
0
100
200
300
400
500
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1e channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.20 × MC
0
50
100
150
200
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.24 × MC
0
25
50
75
100
125
150
Candidates / 0.10 GeV
Belle II preliminary L dt = 365 fb 1channel
SignalXX
ττcc
ssdd
uuB0B0
B+B−MC stat. unc.
Data
0.0 0.5 1.0 1.5 2.0
EROEextra [GeV]
0.5
1.0
1.5
Data1.17 × MC
FIG. 143. EROEextra distribution for each τ decay in the high BDT sideband.
D.c. BB ROE correction transferability checks1229
The ROE corrections for the BB background can be derived from the BDT side-1230
band or the extra track SB control sample. Fitting toys made of MC templates using1231
the method to get the BB ROE corrections using templates from the second method1232
shows an non-negligible bias on the POI. To decide which region is more suitable1233
for deriving the BB ROE corrections, we compare the BB composition as well as1234
the EROEextra and N ROEγ distributions. The BB composition results can be found in1235
Tables 32 and 33 for all channels and in Tables 34 to 39 for each τ decay separately.1236
The EROEextra and N ROEγ distributions are shown in Figure 144. The BDT sideband is1237
found to be more similar to the signal region than the extra track SB control sample,1238
184
which have less modes containing a π0 while having more modes containing D∗∗.1239
Therefore, the BDT sideband is used for deriving the BB ROE corrections in the1240
nominal fit.1241
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗+ℓ−νℓ, D+ℓ−νℓ) 35.51 30.49 17.11
```
```
(D∗+ℓ−νℓ, D∗+ℓ−νℓ) 19.01 21.54 17.81
```
```
(D+ℓ−νℓ, D+ℓ−νℓ) 11.74 6.70 1.83
```
```
(Pythia (3 fs parts.), D∗+ℓ−νℓ) 2.61 2.55 2.80
```
```
(D∗+ℓ−νℓ, D∗+τ −ντ ) 2.24 2.18 1.32
```
```
(Pythia (3 fs parts.), D+ℓ−νℓ) 2.05 2.07 1.12
```
```
(D∗+ℓ−νℓ, D+τ −ντ ) 2.05 1.78 0.91
```
```
(D+ℓ−νℓ, D∗+0 ℓ−νℓ) 1.77 0.76 1.00
```
```
(D∗+ℓ−νℓ, D+π−) 1.40 0.80 0.75
```
```
(Pythia (4 fs parts.), D∗+ℓ−νℓ) 1.30 0.98 2.29
```
```
(D+ℓ−νℓ, D+1 ℓ−νℓ) 1.30 1.64 1.45
```
```
(D∗+ℓ−νℓ, D+1 ℓ−νℓ) 1.12 1.27 2.66
```
```
(D∗+τ −ντ , D+ℓ−νℓ) 1.12 1.27 < 0.01
```
```
(D∗+ℓ−νℓ, π+ℓ−νℓ) 0.93 1.16 < 0.01
```
```
(D∗+ℓ−νℓ, D∗+2 ℓ−νℓ) 0.93 0.55 1.86
```
```
(D+ℓ−νℓ, D+τ −ντ ) 0.84 1.13 < 0.01
```
```
(D+ℓ−νℓ, ρ+ℓ−νℓ) 0.75 < 0.01 < 0.01
```
```
(D+ℓ−νℓ, π+ℓ−νℓ) 0.75 < 0.01 < 0.01
```
```
(D+ℓ−νℓ, D+π−) 0.56 < 0.01 < 0.01
```
```
Remaining (below 0.5%) 11.18 10.44 15.89
```
TABLE 32. The B0B0 composition in the signal region after full selection for all modes,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
185
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗0ℓ−νℓ, D0ℓ−νℓ) 29.99 29.71 22.02
```
```
(D∗0ℓ−νℓ, D∗0ℓ−νℓ) 21.43 25.34 17.17
```
```
(D0ℓ−νℓ, D0ℓ−νℓ) 8.18 8.00 6.09
```
```
(D∗0ℓ−νℓ, π0ℓ−νℓ) 3.69 0.74 < 0.01
```
```
(Pythia (3 fs parts.), D∗0ℓ−νℓ) 2.85 2.52 2.51
```
```
(D∗0ℓ−νℓ, τ −ντ ) 2.27 0.66 < 0.01
```
```
(D∗0ℓ−νℓ, D∗0τ −ντ ) 2.22 1.89 1.22
```
```
(Pythia (3 fs parts.), D0ℓ−νℓ) 1.38 1.59 1.46
```
```
(D0ℓ−νℓ, π0ℓ−νℓ) 1.34 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D0π−) 1.26 1.04 1.22
```
```
(D∗0ℓ−νℓ, D∗00 ℓ−νℓ) 1.17 1.42 1.46
```
```
(D0ℓ−νℓ, τ −ντ ) 1.09 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D0τ −ντ ) 0.96 1.27 0.92
```
```
(D∗0ℓ−νℓ, ρ−D0) 0.92 1.15 1.34
```
```
(D∗0τ −ντ , D0ℓ−νℓ) 0.84 1.36 0.76
```
```
(D∗0ℓ−νℓ, K0π−) 0.84 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D∗02 ℓ−νℓ) 0.80 0.74 1.18
```
```
(Pythia (4 fs parts.), D∗0ℓ−νℓ) 0.80 0.83 1.64
```
```
(D0ℓ−νℓ, D0τ −ντ ) 0.71 0.81 0.51
```
```
(D∗0ℓ−νℓ, D∗0π−) 0.63 0.64 0.77
```
```
(D0ℓ−νℓ, ρ−D0) 0.63 0.59 0.79
```
```
(D0ℓ−νℓ, D∗00 ℓ−νℓ) 0.59 0.61 0.81
```
```
(D0ℓ−νℓ, D0π−) 0.55 < 0.01 0.64
```
```
(D∗0ℓ−νℓ, ρ0ℓ−νℓ) 0.55 0.59 < 0.01
```
```
(D0ℓ−νℓ, K0π−) 0.55 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D10ℓ−νℓ) 0.50 1.00 1.67
```
```
(D∗0π−, D0ℓ−νℓ) 0.50 < 0.01 < 0.01
```
```
(Pythia (4 fs parts.), D0ℓ−νℓ) 0.50 < 0.01 0.99
```
```
Remaining (below 0.5%) 10.78 7.93 13.26
```
TABLE 33. The B+B− composition in the signal region after full selection for all modes,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
186
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗+ℓ−νℓ, D+ℓ−νℓ) 34.88 34.79 21.70
```
```
(D∗+ℓ−νℓ, D∗+ℓ−νℓ) 20.74 24.48 22.97
```
```
(D+ℓ−νℓ, D+ℓ−νℓ) 14.73 7.17 2.23
```
```
(D∗+ℓ−νℓ, D∗+τ −ντ ) 2.71 1.84 1.43
```
```
(Pythia (3 fs parts.), D∗+ℓ−νℓ) 2.71 2.01 2.31
```
```
(Pythia (3 fs parts.), D+ℓ−νℓ) 2.13 2.19 0.90
```
```
(D∗+τ −ντ , D+ℓ−νℓ) 1.55 1.66 0.51
```
```
(D+ℓ−νℓ, D∗+0 ℓ−νℓ) 1.55 0.52 1.20
```
```
(D∗+ℓ−νℓ, D+τ −ντ ) 1.36 1.75 0.98
```
```
(D+ℓ−νℓ, ρ+ℓ−νℓ) 1.36 < 0.01 < 0.01
```
```
(D∗+ℓ−νℓ, D+1 ℓ−νℓ) 1.36 0.70 3.38
```
```
(D∗+ℓ−νℓ, D∗+2 ℓ−νℓ) 1.16 0.70 2.25
```
```
(D+ℓ−νℓ, D+τ −ντ ) 1.16 1.31 < 0.01
```
```
(D+ℓ−νℓ, D+1 ℓ−νℓ) 0.97 1.84 1.77
```
```
(Pythia (4 fs parts.), D∗+ℓ−νℓ) 0.97 0.70 1.42
```
```
(D+ℓ−νℓ, π+ℓ−νℓ) 0.97 < 0.01 < 0.01
```
```
(D∗+ℓ−νℓ, D∗+0 ℓ−νℓ) 0.78 1.31 2.62
```
```
(Pythia (4 fs parts.), D+ℓ−νℓ) 0.58 0.70 0.78
```
```
Remaining (below 0.5%) 7.56 4.28 6.89
```
TABLE 34. The B0B0 composition in the signal region after full selection for the µ mode,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
187
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗0ℓ−νℓ, D0ℓ−νℓ) 33.90 33.70 28.90
```
```
(D∗0ℓ−νℓ, D∗0ℓ−νℓ) 23.36 29.94 22.64
```
```
(D0ℓ−νℓ, D0ℓ−νℓ) 9.44 9.23 7.91
```
```
(D∗0ℓ−νℓ, π0ℓ−νℓ) 4.37 1.05 < 0.01
```
```
(Pythia (3 fs parts.), D∗0ℓ−νℓ) 2.49 2.14 2.15
```
```
(D∗0ℓ−νℓ, D∗0τ −ντ ) 2.39 1.67 1.31
```
```
(D0ℓ−νℓ, π0ℓ−νℓ) 1.69 0.57 < 0.01
```
```
(D∗0ℓ−νℓ, D∗00 ℓ−νℓ) 1.29 1.48 1.75
```
```
(Pythia (3 fs parts.), D0ℓ−νℓ) 1.19 1.38 1.24
```
```
(D∗0ℓ−νℓ, D∗02 ℓ−νℓ) 1.19 0.67 1.42
```
```
(D∗0ℓ−νℓ, D0τ −ντ ) 1.09 0.76 0.97
```
```
(D∗0τ −ντ , D0ℓ−νℓ) 1.09 1.19 0.83
```
```
(D∗0ℓ−νℓ, τ −ντ ) 0.89 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D10ℓ−νℓ) 0.80 0.90 2.16
```
```
(D∗0ℓ−νℓ, ρ0ℓ−νℓ) 0.70 0.62 < 0.01
```
```
(D0ℓ−νℓ, D0τ −ντ ) 0.70 0.62 0.54
```
```
(D∗0ℓ−νℓ, D0π−) 0.70 < 0.01 < 0.01
```
```
(D0ℓ−νℓ, D∗00 ℓ−νℓ) 0.70 < 0.01 0.96
```
```
(D0ℓ−νℓ, τ −ντ ) 0.60 - < 0.01
```
```
Remaining (below 0.5%) 9.54 6.66 7.45
```
TABLE 35. The B+B− composition in the signal region after full selection for the µ mode,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
188
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗+ℓ−νℓ, D+ℓ−νℓ) 42.40 35.73 23.71
```
```
(D∗+ℓ−νℓ, D∗+ℓ−νℓ) 20.28 25.57 24.87
```
```
(D+ℓ−νℓ, D+ℓ−νℓ) 10.60 8.52 2.27
```
```
(Pythia (3 fs parts.), D+ℓ−νℓ) 2.30 1.34 0.85
```
```
(D+ℓ−νℓ, D∗+0 ℓ−νℓ) 2.30 1.15 1.20
```
```
(Pythia (3 fs parts.), D∗+ℓ−νℓ) 1.84 1.82 2.11
```
```
(D∗+ℓ−νℓ, D+τ −ντ ) 1.61 1.44 0.94
```
```
(D∗+ℓ−νℓ, D∗+τ −ντ ) 1.61 1.63 1.42
```
```
(D+ℓ−νℓ, D+1 ℓ−νℓ) 1.61 1.53 1.90
```
```
(D∗+ℓ−νℓ, D+1 ℓ−νℓ) 1.15 2.01 3.56
```
```
(Pythia (4 fs parts.), D∗+ℓ−νℓ) 0.92 1.05 1.30
```
```
(D∗+ℓ−νℓ, D∗+2 ℓ−νℓ) 0.92 0.67 2.46
```
```
(D∗+τ −ντ , D+ℓ−νℓ) 0.69 < 0.01 0.53
```
```
(D+ℓ−νℓ, D+τ −ντ ) 0.69 < 0.01 < 0.01
```
```
(D∗+ℓ−νℓ, J/ψK0L) 0.69 < 0.01 < 0.01
```
```
(D∗+ℓ−νℓ, π+ℓ−νℓ) 0.69 1.25 0.63
```
```
Remaining (below 0.5%) 8.76 4.98 6.63
```
TABLE 36. The B0B0 composition in the signal region after full selection for the e mode,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
189
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗0ℓ−νℓ, D0ℓ−νℓ) 35.31 35.41 31.24
```
```
(D∗0ℓ−νℓ, D∗0ℓ−νℓ) 27.06 29.69 24.85
```
```
(D0ℓ−νℓ, D0ℓ−νℓ) 8.25 8.70 8.56
```
```
(D∗0ℓ−νℓ, π0ℓ−νℓ) 4.73 0.70 < 0.01
```
```
(Pythia (3 fs parts.), D∗0ℓ−νℓ) 2.31 1.89 1.88
```
```
(D∗0ℓ−νℓ, D∗0τ −ντ ) 1.65 1.09 1.31
```
```
(D0ℓ−νℓ, π0ℓ−νℓ) 1.54 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D∗00 ℓ−νℓ) 1.32 1.59 1.83
```
```
(D∗0ℓ−νℓ, τ −ντ ) 1.32 < 0.01 < 0.01
```
```
(Pythia (3 fs parts.), D0ℓ−νℓ) 1.21 1.19 1.11
```
```
(D∗0ℓ−νℓ, ηℓ−νℓ) 0.88 < 0.01 < 0.01
```
```
(Pythia (4 fs parts.), D∗0ℓ−νℓ) 0.77 0.80 0.88
```
```
(D∗0τ −ντ , D0ℓ−νℓ) 0.77 1.19 0.81
```
```
(D0ℓ−νℓ, D∗00 ℓ−νℓ) 0.66 0.80 1.00
```
```
(D∗0ℓ−νℓ, D0τ −ντ ) 0.66 1.14 0.97
```
```
(D0ℓ−νℓ, τ −ντ ) 0.55 < 0.01 < 0.01
```
```
Remaining (below 0.5%) 10.12 8.95 12.68
```
TABLE 37. The B+B− composition in the signal region after full selection for the e mode,
in the BDT sideband and in the extra track SB control sample. The mode combinations
are ordered by their percentage in the signal region.
190
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗+ℓ−νℓ, D+ℓ−νℓ) 13.82 11.96 6.74
```
```
(D∗+ℓ−νℓ, D+π−) 12.20 3.57 1.79
```
```
(D∗+ℓ−νℓ, D∗+ℓ−νℓ) 7.32 8.04 6.47
```
```
(D∗+ℓ−νℓ, D+τ −ντ ) 6.50 2.50 < 0.01
```
```
(Pythia (3 fs parts.), D∗+ℓ−νℓ) 4.88 5.00 3.91
```
```
(Pythia (4 fs parts.), D∗+ℓ−νℓ) 4.07 1.43 4.04
```
```
(D∗+ℓ−νℓ, π+ℓ−νℓ) 4.07 < 0.01 < 0.01
```
```
(D+ℓ−νℓ, D+π−) 4.07 < 0.01 < 0.01
```
```
(D+ℓ−νℓ, D+ℓ−νℓ) 3.25 2.32 1.05
```
```
(D+ℓ−νℓ, ρ−D+) 3.25 1.96 < 0.01
```
```
(D∗+ℓ−νℓ, D∗+τ −ντ ) 2.44 3.93 1.13
```
```
(D∗+ℓ−νℓ, D∗+π−) 2.44 1.07 < 0.01
```
```
(D∗+ℓ−νℓ, ρ−D+) 2.44 4.46 2.41
```
```
(D∗+D−s , D∗+ℓ−νℓ) 1.63 - < 0.01
```
```
(D∗+ℓ−νℓ, ρ+ℓ−νℓ) 1.63 < 0.01 < 0.01
```
```
(Pythia (4 fs parts.), D+ℓ−νℓ) 1.63 1.43 1.89
```
```
(D+ℓ−νℓ, D+1 ℓ−νℓ) 1.63 1.43 < 0.01
```
```
(Pythia (3 fs parts.), π+ℓ−νℓ) 1.63 - < 0.01
```
```
Remaining (below 1.0%) 20.33 11.61 6.59
```
TABLE 38. The B0B0 composition in the signal region after full selection for the hadronic
modes, in the BDT sideband and in the extra track SB control sample. The mode combi-
nations are ordered by their percentage in the signal region.
191
```
Mode combination After Sel. (%) BDT Sideband (%) Extra Track SB CC (%)
```
```
(D∗0ℓ−νℓ, D0ℓ−νℓ) 11.30 12.79 6.42
```
```
(D∗0ℓ−νℓ, τ −ντ ) 7.04 2.47 < 0.01
```
```
(D∗0ℓ−νℓ, D∗0ℓ−νℓ) 6.40 9.63 4.46
```
```
(D0ℓ−νℓ, D0ℓ−νℓ) 5.33 4.60 1.93
```
```
(Pythia (3 fs parts.), D∗0ℓ−νℓ) 4.69 4.26 3.45
```
```
(D∗0ℓ−νℓ, K0π−) 4.26 < 0.01 < 0.01
```
```
(D∗0ℓ−νℓ, D0π−) 4.26 3.67 2.92
```
```
(D0ℓ−νℓ, τ −ντ ) 3.20 1.36 < 0.01
```
```
(D∗0ℓ−νℓ, ρ−D0) 2.99 3.75 3.45
```
```
(D∗0ℓ−νℓ, D∗0τ −ντ ) 2.99 3.67 1.03
```
```
(D0ℓ−νℓ, D0π−) 2.35 < 0.01 1.47
```
```
(D0ℓ−νℓ, K0π−) 2.35 < 0.01 < 0.01
```
```
(D0ℓ−νℓ, ρ−D0) 2.35 1.62 1.95
```
```
(D∗0π−, D0ℓ−νℓ) 2.13 1.28 1.02
```
```
(Pythia (3 fs parts.), D0ℓ−νℓ) 2.13 2.64 2.00
```
```
(D∗0ℓ−νℓ, D∗0π−) 1.92 1.71 1.80
```
```
(Pythia (4 fs parts.), D∗0ℓ−νℓ) 1.71 1.36 3.10
```
```
(D∗0ℓ−νℓ, D0τ −ντ ) 1.28 2.39 < 0.01
```
```
(D0ℓ−νℓ, D0τ −ντ ) 1.28 1.02 < 0.01
```
```
(D∗0ℓ−νℓ, ρ0ℓ−νℓ) 1.07 < 0.01 < 0.01
```
```
(Pythia (4 fs parts.), D0ℓ−νℓ) 1.07 < 0.01 1.87
```
```
(D∗0ℓ−νℓ, D∗0ρ−) 1.07 1.96 1.30
```
```
(Pythia (5 fs parts.), D∗0ℓ−νℓ) 1.07 < 0.01 1.32
```
```
Remaining (below 1.0%) 24.09 15.17 16.75
```
TABLE 39. The B+B− composition in the signal region after full selection for the hadronic
modes, in the BDT sideband and in the extra track SB control sample. The mode combi-
nations are ordered by their percentage in the signal region.
192
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Event density
Belle II preliminary simulationchannel, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.00
0.05
0.10
0.15
0.20
Event density
Belle II preliminary simulationchannel, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Event density
Belle II preliminary simulatione channel, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.00
0.05
0.10
0.15
0.20
Event density
Belle II preliminary simulatione channel, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Event density
Belle II preliminary simulationHad. channels, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
0 5 10 15 20
```
NROE c2_bbS_32 (with removal)
```
0.00
0.05
0.10
0.15
0.20
0.25
Event density
Belle II preliminary simulationHad. channels, BB bkg
After selBDT sideband
Extra track CCMC stat. unc.
FIG. 144. The EROEextra and N ROEγ distributions of the BB background in the fitting region
for the nominal sample after the selection, the BDT sideband and the extra track SB
control sample.
193
D.d. τpCMS checks1242
Figure 145 show the τpCMS distribution in the fourth to ninth bins = 0.1 GeV of1243
EROEextra for the hadronic channels, where we don’t expect signal. A good agreement is1244
observed between data/MC.1245
194
0
5
10
15
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.37 × MC
0
5
10
15
20
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.37 × MC
0
5
10
15
20
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.86 × MC
0
5
10
15
20
25
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.44 × MC
0
5
10
15
20
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.42 × MC
0
5
10
15
20
25
30
Candidates / 0.15 GeV/
c
Belle II preliminary L dt = 365 fb 1+ channels
SignalXX
ττqq
B0B0B+B−
MC stat. unc.Data
0.5 1.0 1.5 2.0 2.5 3.0
pvis [GeV/c]
0.5
1.0
1.5
Data1.34 × MC
```
FIG. 145. The τpCMS distribution in the fourth (top left), fifth (top right), sixth (middle
```
```
left), seventh (middle right), eighth (bottom left) and ninth (bottom right) EROEextra bins for
```
the hadronic channels.
195
E. Post-selection, additional material1246
This section shows additional material related to the events after the full selection.1247
E.a. Extra track study1248
Table 40 recaps the different ROE mask used to get the different extra track1249
variables. After the full selection, a few additional tracks are still observed. The1250
composition of these tracks is studied using MC truth information, and the results1251
are shown in Figure 146. Most of the remaining extra tracks are fake tracks or1252
secondary particles.1253
Variable ROE mask Description
nROETracksLoose dr < 2 and |dz | < 4 and θ in CDC
acceptance
Set to 0 at the reconstruction level.
nROETracksGood dr < 0.5 and |dz | < 2 and θ in CDC ac-
ceptance and nCDCHits > 20
Equal to 0 after the BDT selection.
nRemainingTracks No cuts Can be equal to 0 or 1 after the BDT
selection.
TABLE 40. ROE mask used to get the different extra track variables.
196
```
2212 (p)
```
25.3%
```
211 ( ±)
```
38.6%
```
13 ( ±) 20.5%
```
```
11 (e±)
```
8.4%
```
321 (K±)
```
7.2%
```
mcPDG (|PDG|) occurrences in duplicated rows
```
```
512.0 (fake/bkg tracks or clusters)39.0%
```
```
132.0 (miss ID + secondary/wrong hypo)
```
24.3%
```
4.0 (secondary/wrong hypo) 14.0%
```
```
0.0 (correct)
```
14.0%
```
128.0 (miss ID)
```
8.8%
mcErrors occurrences in duplicated rows
FIG. 146. Composition of the extra tracks observed after the full selection in MC.
E.b. Self-crossfeed study1254
```
The self-crossfeed (SCF) component is defined as the signal events where at least1255
```
one of the reconstructed particles is not matched to the corresponding generated1256
particle. The composition of the SCF events is studied using MC truth information,1257
and the proportions are shown in Table 41. The overlap between the channels using1258
truth-matching and generator information is shown in Tables 42 and 43 respectively.1259
The distributions of the fit variables for the SCF events are shown in Figure 147.1260
Most of the SCF events are due to:1261
• missID: the reconstructed particle is misidentified. The systematic uncertainty1262
related to the particle identification is already included in the fit.1263
• π − ρ overlap: the reconstructed particle is a π or ρ from a τ decay, but the1264
generated particle is a ρ or π. In the case of B → ρ+ρ− decays [34], the post-fit1265
test shows around 10% SCF component due to π0 miss-reconstruction.1266
• The majority of the ”other” category is due to τ → π2π0ντ or τ → 3πντ1267
decays, which are well measured.1268
We assign a 10% systematic uncertainty on the shape to the SCF component in1269
the fit as a histosys, shown in Figure 148.1270
197
τ decay mode Proportion of SCF events
µ channel 13.83 ± 0.14%
e channel 20.79 ± 0.17%
hadronic channels 44.52 ± 0.19%
TABLE 41. Proportions of SCF events for the different τ decay modes.
Decay mode µ e π ρ other
µ 90.1 0.1 9.0 0.0 0.8
e 0.0 99.7 0.2 0.0 0.1
π 1.7 0.1 97.8 0.0 0.4
ρ 0.5 0.0 25.7 73.3 0.4
```
TABLE 42. Overlap between the channels using truth-matching (mcPDG) information (in
```
```
%).
```
Decay mode µ e π ρ other
µ 88.2 0.8 3.8 5.0 2.1
e 0.9 97.4 0.3 0.8 0.5
π 1.9 0.3 57.7 33.7 6.4
ρ 0.7 0.2 15.3 66.3 17.5
TABLE 43. Overlap between the channels using generator-level information with
```
GenMCTagTool (in %).
```
198
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
0.5
1.0
1.5
2.0
Candidates
×104 Belle II preliminary simulationchannel
TM signalSCF signal
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0
2000
4000
6000
Candidates
Belle II preliminary simulationchannel
TM signalSCF signal
MC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
0.5
1.0
1.5
Candidates
×104 Belle II preliminary simulatione channel
TM signalSCF signal
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0
1000
2000
3000
4000
5000
6000
Candidates
Belle II preliminary simulatione channel
TM signalSCF signal
MC stat. unc.
0.0 0.2 0.4 0.6 0.8 1.0
```
EROEextra c2_bbS_32 (with removal)
```
0.0
0.5
1.0
1.5
Candidates
×104 Belle II preliminary simulationhadronic channels
TM signalSCF signal
MC stat. unc.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
τsig pCMS
0
1000
2000
3000
4000
5000
Candidates
Belle II preliminary simulationhadronic channels
TM signalSCF signal
MC stat. unc.
FIG. 147. EROEextra and τpCMS distributions for the different τ decay modes.
199
0.00
0.05
0.10
0.15
0.20
Entries
```
Fit region (affected samples only)
```
NominalSCF_shape Up
SCF_shape Down
0 20 40 60 80 100
EROEextra × pvis
0.010.00
0.01
Diff
0.0
0.1
0.2
0.3
0.4
Entries
```
e Fit region (affected samples only)
```
NominalSCF_shape Up
SCF_shape Down
0 20 40 60 80 100
EROEextra × pvis
0.0250.000
0.025
Diff
0.0
0.2
0.4
0.6
Entries
```
hadronic Fit region (affected samples only)
```
NominalSCF_shape Up
SCF_shape Down
0 20 40 60 80 100
EROEextra × pvis
0.05
0.00
0.05
Diff
FIG. 148. Shape variation of the SCF component used as a histosys in the fit.
200
F. Fitting, additional plots1271
This section shows additional plots related to the fit procedure.1272
F.a. MC templates1273
Here are shown unstacked templates for the three channels.1274
1275
µ channel:1276
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
1
2
3
Events
Pre-fit
Fit region Belle II preliminary simulation
Signal
FIG. 149. The EROEextra and τpCMS flattened distribution for the signal sample in the µ channel
before the fit.
201
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.00
0.05
0.10
0.15
Events
Pre-fit
Fit region Belle II preliminary simulation
SCF
FIG. 150. The EROEextra and τpCMS flattened distribution for the SCF sample in the µ channel
before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
20
40
60
80
Events
Pre-fit
Fit region Belle II preliminary simulation
BB
FIG. 151. The EROEextra and τpCMS flattened distribution for the BB background in the µ
channel before the fit.
202
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
5
10
15
20
25
Events
Pre-fit
Fit region Belle II preliminary simulation
Non -BB
FIG. 152. The EROEextra and τpCMS flattened distribution for the non-BB background in the
µ channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.1
0.2
0.3
Events
Pre-fit
Fit region Belle II preliminary simulation
Rare BB
FIG. 153. The EROEextra and τpCMS flattened distribution for the rare BB background in the
µ channel before the fit.
203
e channel:1277
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.5
1.0
1.5
2.0
2.5
Events
Pre-fit
e Fit region Belle II preliminary simulation
Signal
FIG. 154. The EROEextra and τpCMS flattened distribution for the signal sample in the e channel
before the fit.
204
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.1
0.2
0.3
0.4
Events
Pre-fit
e Fit region Belle II preliminary simulation
SCF
FIG. 155. The EROEextra and τpCMS flattened distribution for the SCF sample in the e channel
before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
20
40
60
Events
Pre-fit
e Fit region Belle II preliminary simulation
BB
FIG. 156. The EROEextra and τpCMS flattened distribution for the BB background in the e
channel before the fit.
205
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
2.5
5.0
7.5
10.0
12.5
Events
Pre-fit
e Fit region Belle II preliminary simulation
Non -BB
FIG. 157. The EROEextra and τpCMS flattened distribution for the non-BB background in the
e channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.1
0.2
0.3
0.4
Events
Pre-fit
e Fit region Belle II preliminary simulation
Rare BB
FIG. 158. The EROEextra and τpCMS flattened distribution for the rare BB background in the
e channel before the fit.
206
Hadronic channel:1278
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.5
1.0
1.5
2.0
2.5
Events
Pre-fit
hadronic Fit region Belle II preliminary simulation
Signal
FIG. 159. The EROEextra and τpCMS flattened distribution for the signal sample in the hadronic
channel before the fit.
207
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.0
0.2
0.4
0.6
Events
Pre-fit
hadronic Fit region Belle II preliminary simulation
SCF
FIG. 160. The EROEextra and τpCMS flattened distribution for the SCF sample in the hadronic
channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
5
10
15
20
Events
Pre-fit
hadronic Fit region Belle II preliminary simulation
BB
FIG. 161. The EROEextra and τpCMS flattened distribution for the BB background in the
hadronic channel before the fit.
208
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0
2
4
6
8
10
Events
Pre-fit
hadronic Fit region Belle II preliminary simulation
Non -BB
FIG. 162. The EROEextra and τpCMS flattened distribution for the non-BB background in the
hadronic channel before the fit.
0 20 40 60 80 100
EROEextra × pvis [GeV × GeV/c]
0.000
0.002
0.004
0.006
0.008
0.010
Events
Pre-fit
hadronic Fit region Belle II preliminary simulation
Rare BB
FIG. 163. The EROEextra and τpCMS flattened distribution for the rare BB background in the
hadronic channel before the fit.
209
F.b. Correlation matrix1279
Here is shown the correlation matrix of all the NPs included in the fit.1280
1281
B0_BF_sig_var1B0_BF_sig_var2B0_BF_tag_var1B0_BF_tag_var2
FEIcal_B0_var1_mu_channelFEIcal_Bp_var1_mu_channelmuID_K_fake_var1_mu_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBB
FEIcal_B0_var1_e_channelFEIcal_Bp_var1_e_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBB
FEIcal_B0_var1_hadronic_channelFEIcal_Bp_var1_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbar
d1_d0_pCMS_BB_var1_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBB
mu
BBbar_normsysnonBB_normsys
staterror_ -Fit-region[0]staterror_ -Fit-region[1]staterror_ -Fit-region[2]staterror_ -Fit-region[5]staterror_ -Fit-region[11]staterror_e-Fit-region[2]
staterror_hadronic-Fit-region[4]staterror_hadronic-Fit-region[49]staterror_hadronic-Fit-region[99]
B0_BF_sig_var1
B0_BF_sig_var2
B0_BF_tag_var1
B0_BF_tag_var2
FEIcal_B0_var1_mu_channel
FEIcal_Bp_var1_mu_channel
muID_K_fake_var1_mu_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBB
FEIcal_B0_var1_e_channel
FEIcal_Bp_var1_e_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBB
FEIcal_B0_var1_hadronic_channel
FEIcal_Bp_var1_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbar
d1_d0_pCMS_BB_var1_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBB
mu
BBbar_normsys
nonBB_normsys
staterror_ -Fit-region[0]
staterror_ -Fit-region[1]
staterror_ -Fit-region[2]
staterror_ -Fit-region[5]
staterror_ -Fit-region[11]
staterror_e-Fit-region[2]
staterror_hadronic-Fit-region[4]
staterror_hadronic-Fit-region[49]
staterror_hadronic-Fit-region[99]
1.00 0.26 -0.04 0.03 -0.24 -0.33 -0.03 0.02 -0.06 0.18 0.25 -0.03 0.06 0.08 0.01 -0.03 -0.02 -0.38 0.09 -0.02 0.01 -0.02 0.02 -0.01 -0.02
0.26 1.00 0.03 0.02 -0.07 -0.10 -0.01 -0.01 -0.05 0.07 0.09 -0.03 0.01 0.02 0.02 -0.02 0.04 -0.09 0.11 -0.03 -0.02 -0.01 0.04 0.01 -0.01 -0.01
-0.04 0.03 1.00 0.36 -0.01 -0.01 0.01 -0.02 0.01 0.02 0.03 -0.02 -0.05 0.01 0.62 -0.06 0.02 -0.01 0.02 -0.01 0.02 0.02 0.03
0.03 0.02 0.36 1.00 -0.01 -0.01 0.01 0.01 -0.01 -0.03 0.22 0.01 0.01 0.01 -0.02 -0.01
-0.24 -0.07 -0.01 -0.01 1.00 -0.24 0.01 0.01 0.05 0.08 0.12 0.07 0.11 -0.02 0.01 -0.04 -0.16 0.01 -0.01 -0.01 -0.01
-0.33 -0.10 -0.01 -0.01 -0.24 1.00 0.01 0.02 0.07 0.12 0.17 0.01 0.11 0.15 -0.02 0.01 -0.05 -0.22 0.01 0.01 -0.01 -0.01
-0.03 -0.01 0.01 0.01 0.01 1.00 0.02 -0.02 -0.01 -0.01 -0.01 -0.01 0.01 -0.01 0.04 0.01 0.01 -0.01 0.25
0.02 -0.01 -0.02 0.01 0.01 0.02 0.02 1.00 0.12 0.02 0.03 -0.09 -0.03 -0.05 0.08 0.02 -0.06 0.16 -0.07 0.28 0.46 0.27 0.21 0.23 -0.01 -0.02 -0.04 0.01
-0.06 -0.05 0.01 0.01 0.05 0.07 -0.02 0.12 1.00 -0.01 -0.02 -0.04 -0.03 -0.05 0.01 0.02 -0.03 -0.03 0.01 0.26 -0.04 -0.02 -0.02 -0.03 0.01 -0.02 -0.03
0.18 0.07 0.08 0.12 0.02 -0.01 1.00 -0.29 -0.02 0.10 0.14 -0.01 -0.01 -0.04 -0.31 0.06 -0.01 -0.01 -0.01 -0.01 -0.01
0.25 0.09 0.12 0.17 -0.01 0.03 -0.02 -0.29 1.00 -0.03 0.14 0.20 -0.02 -0.02 -0.01 -0.06 -0.44 0.08 -0.01 -0.01 -0.01 0.01 -0.01 -0.01
-0.03 -0.03 0.01 -0.01 -0.09 -0.04 -0.02 -0.03 1.00 0.02 0.03 -0.07 -0.02 0.04 -0.18 0.04 -0.13 0.01 0.01 0.01 0.01 0.01 -0.46 0.02
0.06 0.01 0.02 0.07 0.11 -0.01 -0.03 -0.03 0.10 0.14 0.02 1.00 -0.26 0.02 -0.08 -0.17 -0.06 0.01 0.01 0.01
0.08 0.02 0.03 0.11 0.15 -0.01 -0.05 -0.05 0.14 0.20 0.03 -0.26 1.00 0.03 0.01 0.01 -0.11 -0.24 -0.08 0.01 0.01 0.01 0.01
0.01 0.02 -0.02 -0.01 -0.02 -0.02 0.01 0.08 0.01 -0.01 -0.02 -0.07 0.02 0.03 1.00 -0.09 0.14 0.29 0.02 0.01 -0.01 -0.01 -0.01 0.03 -0.02 -0.02
-0.03 -0.05 0.02 0.02 -0.01 -0.02 -0.02 0.01 -0.09 1.00 -0.05 0.02 -0.02 0.06 -0.01 -0.01 -0.02 0.21 0.21
-0.02 -0.02 0.01 0.01 0.01 -0.01 -0.06 -0.03 -0.01 0.04 0.01 0.14 -0.05 1.00 -0.10 0.02 -0.11 0.01 0.01 0.01 0.01 0.01 -0.23 -0.01 -0.01
0.04 -0.03 -0.04 -0.05 0.04 0.16 -0.03 -0.04 -0.06 -0.18 -0.08 -0.11 0.29 0.02 -0.10 1.00 0.04 -0.25 0.06 0.02 -0.04 -0.02 -0.03 0.01 -0.01 0.01 0.01
-0.38 -0.09 0.62 0.22 -0.16 -0.22 0.01 -0.07 0.01 -0.31 -0.44 0.04 -0.17 -0.24 -0.02 0.02 0.04 1.00 -0.18 0.02 0.01 0.03 -0.01 0.02 0.03 0.01
0.09 0.11 -0.06 0.01 0.28 0.26 0.06 0.08 -0.13 -0.06 -0.08 0.02 0.06 -0.11 -0.25 -0.18 1.00 -0.10 -0.07 -0.02 -0.02 -0.01 -0.08 -0.10 0.01 0.01
-0.03 0.02 0.01 0.01 0.46 -0.04 -0.01 -0.01 0.01 0.01 -0.01 0.01 0.06 0.02 -0.10 1.00 0.18 0.13 0.15 0.01 0.01
-0.02 -0.02 0.01 0.01 0.01 -0.01 0.27 -0.02 -0.01 -0.01 0.01 0.01 0.02 0.01 -0.07 0.18 1.00 0.08 0.09 0.01 0.01
0.01 -0.01 -0.01 0.01 -0.01 -0.01 0.21 -0.02 0.01 0.01 0.01 -0.01 0.01 -0.04 -0.02 0.13 0.08 1.00 0.08
-0.02 0.04 0.02 -0.02 -0.01 0.23 -0.03 -0.01 -0.01 0.01 -0.01 0.01 -0.02 0.03 -0.02 0.15 0.09 0.08 1.00
0.02 0.01 -0.01 -0.01 -0.01 0.25 -0.01 0.01 0.01 0.01 0.01 0.01 -0.01 -0.03 -0.01 -0.01 0.01 1.00
-0.01 -0.01 0.02 -0.02 -0.02 -0.01 -0.01 -0.46 0.01 -0.01 0.01 0.01 0.02 -0.08 0.01 1.00 0.01
-0.02 -0.01 0.02 -0.04 -0.03 -0.01 -0.01 0.02 0.01 0.01 0.03 -0.02 -0.23 -0.01 0.03 -0.10 0.01 0.01 0.01 1.00
0.03 -0.02 0.21 -0.01 0.01 0.01 0.01 1.00 0.04
-0.01 0.01 -0.02 0.21 -0.01 0.01 0.01 0.04 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 164. Correlation matrix of all the NPs included in the fit, with a minimal threshold
of 0.1.
210
F.c. Pulls of individual NPs1282
Here are shown the pulls of all the NPs included in the fit on Asimov dataset.1283
1284
```
3 2 1 0 1 2 3(0)/
```
B0_BF_sig_var1B0_BF_sig_var2B0_BF_sig_var3
B0_BF_sig_var4B0_BF_sig_var5B0_BF_sig_var6
B0_BF_sig_var7B0_BF_tag_var1B0_BF_tag_var2
B0_BF_tag_var3B0_BF_tag_var4B0_BF_tag_var5
B0_BF_tag_var6B0_BF_tag_var7Bp_BF_sig_var1
Bp_BF_sig_var2Bp_BF_sig_var3Bp_BF_sig_var4
Bp_BF_sig_var5Bp_BF_sig_var6Bp_BF_sig_var7
Bp_BF_tag_var1Bp_BF_tag_var2Bp_BF_tag_var3
Bp_BF_tag_var4Bp_BF_tag_var5Bp_BF_tag_var6
Bp_BF_tag_var7D0tag_var1_mu_channelD0tag_var2_mu_channel
D0tag_var3_mu_channelD0tag_var4_mu_channelFEIcal_B0_var1_mu_channel
FEIcal_B0_var2_mu_channelFEIcal_B0_var3_mu_channelFEIcal_B0_var4_mu_channel
FEIcal_Bp_var1_mu_channelFEIcal_Bp_var2_mu_channelFEIcal_Bp_var3_mu_channel
FEIcal_Bp_var4_mu_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_BBbar
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_mu_channel_BBbar
d0_FF_DlvDslv_tag_var1d0_FF_DlvDslv_tag_var2d0_FF_DlvDslv_tag_var3
d0_FF_DlvDslv_tag_var4d0_FF_DlvDslv_tag_var5d0_FF_DlvDslv_tag_var6
d0_FF_DlvDslv_tag_var7d0_FF_DlvDslv_tag_var8d0_FF_DlvDslv_tag_var9
d1_FF_DlvDslv_sig_var1d1_FF_DlvDslv_sig_var2d1_FF_DlvDslv_sig_var3
d1_FF_DlvDslv_sig_var4d1_FF_DlvDslv_sig_var5d1_FF_DlvDslv_sig_var6
d1_FF_DlvDslv_sig_var7d1_FF_DlvDslv_sig_var8d1_FF_DlvDslv_sig_var9
d1_d0_pCMS_BB_var10_mu_channeld1_d0_pCMS_BB_var11_mu_channeld1_d0_pCMS_BB_var12_mu_channel
d1_d0_pCMS_BB_var13_mu_channeld1_d0_pCMS_BB_var1_mu_channeld1_d0_pCMS_BB_var2_mu_channel
d1_d0_pCMS_BB_var3_mu_channeld1_d0_pCMS_BB_var4_mu_channeld1_d0_pCMS_BB_var5_mu_channel
d1_d0_pCMS_BB_var6_mu_channeld1_d0_pCMS_BB_var7_mu_channeld1_d0_pCMS_BB_var8_mu_channel
d1_d0_pCMS_BB_var9_mu_channelmuID_K_fake_var1_mu_channelmuID_K_fake_var2_mu_channel
muID_K_fake_var3_mu_channelmuID_K_fake_var4_mu_channelmuID_eff_var1_mu_channel
muID_pi_fake_var1_mu_channelmuID_pi_fake_var2_mu_channel
```
3 2 1 0 1 2 3(0)/
```
muID_pi_fake_var3_mu_channelmuID_pi_fake_var4_mu_channeltracking
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_SCFSCF_shape
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var2_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var4_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var5_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var7_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var8_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_mu_channel_nonBB
d0_dmID_c0_var1_mu_channeld0_dmID_c0_var2_mu_channeld0_dmID_c0_var3_mu_channel
d0_dmID_c0_var4_mu_channelROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_rareBB
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_rareBBrareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_mu_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var4_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_mu_channel_signalFEIcal_B0_var1_e_channel
FEIcal_B0_var2_e_channelFEIcal_B0_var3_e_channelFEIcal_B0_var4_e_channel
FEIcal_Bp_var1_e_channelFEIcal_Bp_var2_e_channelFEIcal_Bp_var3_e_channel
FEIcal_Bp_var4_e_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var4_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var5_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_e_channel_BBbar
FIG. 165. Pulls of all the NPs included in the fit on Asimov dataset.
211
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_e_channel_BBbar
d1_d0_pCMS_BB_var10_e_channeld1_d0_pCMS_BB_var11_e_channeld1_d0_pCMS_BB_var12_e_channel
d1_d0_pCMS_BB_var13_e_channeld1_d0_pCMS_BB_var1_e_channeld1_d0_pCMS_BB_var2_e_channel
d1_d0_pCMS_BB_var3_e_channeld1_d0_pCMS_BB_var4_e_channeld1_d0_pCMS_BB_var5_e_channel
d1_d0_pCMS_BB_var6_e_channeld1_d0_pCMS_BB_var7_e_channeld1_d0_pCMS_BB_var8_e_channel
d1_d0_pCMS_BB_var9_e_channeleID_K_fake_var1_e_channeleID_K_fake_var2_e_channel
eID_K_fake_var3_e_channeleID_K_fake_var4_e_channeleID_eff_var1_e_channel
eID_eff_var2_e_channeleID_eff_var3_e_channeleID_pi_fake_var1_e_channel
eID_pi_fake_var2_e_channeleID_pi_fake_var3_e_channeleID_pi_fake_var4_e_channel
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_SCFROE_nROEg_c2_bbS_32_kcorr_c0_var1_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_e_channel_nonBBd0_dmID_c0_var1_e_channel
d0_dmID_c0_var2_e_channeld0_dmID_c0_var3_e_channeld0_dmID_c0_var4_e_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_rareBB
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var3_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var4_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_e_channel_signal
FEIcal_B0_var1_hadronic_channelFEIcal_B0_var2_hadronic_channelFEIcal_B0_var3_hadronic_channel
FEIcal_B0_var4_hadronic_channelFEIcal_Bp_var1_hadronic_channelFEIcal_Bp_var2_hadronic_channel
FEIcal_Bp_var3_hadronic_channelFEIcal_Bp_var4_hadronic_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_hadronic_channel_BBbar
d1_d0_pCMS_BB_var10_hadronic_channeld1_d0_pCMS_BB_var11_hadronic_channeld1_d0_pCMS_BB_var12_hadronic_channel
d1_d0_pCMS_BB_var13_hadronic_channeld1_d0_pCMS_BB_var14_hadronic_channeld1_d0_pCMS_BB_var15_hadronic_channel
d1_d0_pCMS_BB_var16_hadronic_channeld1_d0_pCMS_BB_var17_hadronic_channeld1_d0_pCMS_BB_var18_hadronic_channel
d1_d0_pCMS_BB_var19_hadronic_channeld1_d0_pCMS_BB_var1_hadronic_channeld1_d0_pCMS_BB_var20_hadronic_channel
d1_d0_pCMS_BB_var21_hadronic_channeld1_d0_pCMS_BB_var22_hadronic_channeld1_d0_pCMS_BB_var23_hadronic_channel
d1_d0_pCMS_BB_var24_hadronic_channeld1_d0_pCMS_BB_var25_hadronic_channeld1_d0_pCMS_BB_var2_hadronic_channel
d1_d0_pCMS_BB_var3_hadronic_channeld1_d0_pCMS_BB_var4_hadronic_channel
```
3 2 1 0 1 2 3(0)/
```
d1_d0_pCMS_BB_var5_hadronic_channeld1_d0_pCMS_BB_var6_hadronic_channeld1_d0_pCMS_BB_var7_hadronic_channel
d1_d0_pCMS_BB_var8_hadronic_channeld1_d0_pCMS_BB_var9_hadronic_channelneutral_pi_var1_hadronic_channel
neutral_pi_var2_hadronic_channelneutral_pi_var3_hadronic_channelpiID_eff_var1_hadronic_channel
piID_eff_var2_hadronic_channelpiID_eff_var3_hadronic_channelpiID_fake_var1_hadronic_channel
piID_fake_var2_hadronic_channelpiID_fake_var3_hadronic_channelpiID_fake_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_SCFROE_nROEg_c2_bbS_32_kcorr_c0_var1_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_hadronic_channel_nonBBd0_dmID_c0_var1_hadronic_channel
d0_dmID_c0_var2_hadronic_channeld0_dmID_c0_var3_hadronic_channeld0_dmID_c0_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_hadronic_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var4_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_hadronic_channel_signalBBbar_normsys
nonBB_normsysrareBB_normsys
```
FIG. 166. Pulls of all the NPs included in the fit on Asimov dataset (cont.).
```
F.d. Impact of individual NPs1285
Here are shown the impact of the most impactful NPs included in the fit on1286
Asimov dataset.1287
1288
212
0.10 0.05 0.00 0.05 0.10
```
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0(
```
```
0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_BBbar
nonBB_normsysROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_e_channel_BBbar
staterror_hadronic-Fit-region[6]ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBB
staterror_e-Fit-region[1]d1_d0_pCMS_BB_var2_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBB
staterror_hadronic-Fit-region[5]FEIcal_Bp_var1_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_c0_var6_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_BB_var9_hadronic_channel_BBbar
staterror_ -Fit-region[3]
staterror_hadronic-Fit-region[16]staterror_hadronic-Fit-region[15]
staterror_e-Fit-region[11]staterror_hadronic-Fit-region[8]
ROE_nROEg_c2_bbS_32_kcorr_c0_var4_e_channel_nonBBFEIcal_B0_var1_hadronic_channel
staterror_hadronic-Fit-region[17]staterror_e-Fit-region[0]
staterror_hadronic-Fit-region[14]staterror_hadronic-Fit-region[7]
staterror_e-Fit-region[4]staterror_hadronic-Fit-region[25]
staterror_ -Fit-region[4]d1_d0_pCMS_BB_var9_hadronic_channel
staterror_ -Fit-region[13]
staterror_e-Fit-region[12]staterror_hadronic-Fit-region[26]
staterror_hadronic-Fit-region[0]staterror_hadronic-Fit-region[18]
staterror_ -Fit-region[0]FEIcal_Bp_var1_e_channel
staterror_ -Fit-region[14]staterror_ -Fit-region[10]
FEIcal_Bp_var1_mu_channel
staterror_hadronic-Fit-region[28]staterror_e-Fit-region[10]
staterror_hadronic-Fit-region[36]staterror_hadronic-Fit-region[27]
staterror_ -Fit-region[15]ROE_nROEg_c2_bbS_32_kcorr_c0_var7_e_channel_nonBB
staterror_e-Fit-region[6]
post-fit impact: a = a0 + a post-fit impact: a = a0 a pulls
FIG. 167. Impact of all the NPs included in the fit on Asimov dataset.
213
0.10 0.05 0.00 0.05 0.10
```
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0(
```
```
0)/
```
Bp_BF_sig_var3
d1_d0_pCMS_BB_var7_hadronic_channelmuID_K_fake_var1_mu_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_mu_channel_BBbarFEIcal_B0_var1_e_channel
staterror_ -Fit-region[8]Bp_BF_sig_var1
staterror_ -Fit-region[12]staterror_ -Fit-region[2]
Bp_BF_sig_var7
staterror_ -Fit-region[16]FEIcal_B0_var1_mu_channel
Bp_BF_sig_var2
staterror_ -Fit-region[6]
staterror_e-Fit-region[13]SCF_shape
staterror_ -Fit-region[7]
staterror_e-Fit-region[15]B0_BF_sig_var2
staterror_e-Fit-region[14]ROE_nROEg_c2_bbS_32_kcorr_BB_var8_e_channel_BBbar
d1_d0_pCMS_BB_var4_hadronic_channeld1_d0_pCMS_BB_var7_mu_channel
d1_d0_pCMS_BB_var6_e_channelROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBB
staterror_hadronic-Fit-region[1]staterror_ -Fit-region[11]
ROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_signal
staterror_hadronic-Fit-region[19]staterror_e-Fit-region[5]
staterror_hadronic-Fit-region[3]staterror_ -Fit-region[19]
Bp_BF_sig_var5B0_BF_tag_var2
staterror_ -Fit-region[9]
staterror_e-Fit-region[8]staterror_e-Fit-region[9]
ROE_nROEg_c2_bbS_32_kcorr_BB_var10_mu_channel_BBbar
staterror_hadronic-Fit-region[35]staterror_hadronic-Fit-region[88]
staterror_e-Fit-region[29]muID_pi_fake_var1_mu_channel
staterror_ -Fit-region[17]ROE_nROEg_c2_bbS_32_kcorr_c0_var9_hadronic_channel_nonBB
rareBB_normsys
staterror_ -Fit-region[50]ROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_signal
post-fit impact: a = a0 + a post-fit impact: a = a0 a pulls
```
FIG. 168. Impact of all the NPs included in the fit on Asimov dataset (cont.).
```
214
0.10 0.05 0.00 0.05 0.10
```
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0(
```
```
0)/
```
muID_eff_var1_mu_channelROE_nROEg_c2_bbS_32_kcorr_c0_var8_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_BB_var10_hadronic_channel_BBbarB0_BF_sig_var6
staterror_ -Fit-region[60]B0_BF_sig_var4
staterror_e-Fit-region[3]ROE_nROEg_c2_bbS_32_kcorr_BB_var10_e_channel_BBbar
staterror_hadronic-Fit-region[68]staterror_ -Fit-region[18]
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_mu_channel_nonBBd1_d0_pCMS_BB_var5_hadronic_channel
staterror_hadronic-Fit-region[92]FEIcal_Bp_var3_mu_channel
staterror_hadronic-Fit-region[95]staterror_hadronic-Fit-region[87]
ROE_nROEg_c2_bbS_32_kcorr_c0_var6_hadronic_channel_nonBBstaterror_hadronic-Fit-region[97]
ROE_nROEg_c2_bbS_32_kcorr_BB_var6_hadronic_channel_BBbarstaterror_hadronic-Fit-region[96]
staterror_e-Fit-region[16]staterror_hadronic-Fit-region[98]
staterror_e-Fit-region[22]staterror_hadronic-Fit-region[78]
staterror_ -Fit-region[40]staterror_ -Fit-region[51]
staterror_hadronic-Fit-region[9]staterror_ -Fit-region[22]
B0_BF_sig_var7staterror_ -Fit-region[61]
staterror_ -Fit-region[80]FEIcal_Bp_var2_e_channel
staterror_hadronic-Fit-region[61]staterror_ -Fit-region[30]
staterror_ -Fit-region[5]staterror_ -Fit-region[90]
staterror_hadronic-Fit-region[77]staterror_hadronic-Fit-region[90]
ROE_nROEg_c2_bbS_32_kcorr_c0_var7_hadronic_channel_nonBBd0_dmID_c0_var1_hadronic_channel
staterror_hadronic-Fit-region[72]FEIcal_Bp_var3_e_channel
staterror_hadronic-Fit-region[34]staterror_ -Fit-region[70]
eID_eff_var1_e_channel
staterror_hadronic-Fit-region[13]staterror_hadronic-Fit-region[70]
post-fit impact: a = a0 + a post-fit impact: a = a0 a pulls
```
FIG. 169. Impact of all the NPs included in the fit on Asimov dataset (cont.).
```
215
G. Unblinding, additional material1289
Additional plots/checks on the unblinded LS1 dataset.1290
G.a. Agreement with other measurements1291
Figure 170 shows the significance between the past measurements, as well as with1292
the null-hypothesis and the PDG average [4], assuming independent measurements.1293
Belle II
SL
Belle IIHAD
BelleSLBelleHADBaBarHADBaBarSL
PDG Average
Null-hyp
Belle II
SL
Belle II
HAD
Belle
SL
Belle
HAD
BaBar
HAD
BaBar
SL
PDG Average
Null-hyp
1.39 1.46 2.54 0.45 0.49 1.96 4.38
1.39 0.02 0.98 0.82 0.49 0.29 2.74
1.46 0.02 1.10 0.85 0.49 0.35 3.21
2.54 0.98 1.10 1.76 1.12 1.00 2.55
0.45 0.82 0.85 1.76 0.13 1.21 3.25
0.49 0.49 0.49 1.12 0.13 0.71 2.06
1.96 0.29 0.35 1.00 1.21 0.71 4.54
4.38 2.74 3.21 2.55 3.25 2.06 4.54
Pairwise significance between measurements
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Tension [ ]
FIG. 170. Comparison of the measured branching fraction with previous measurements.
216
G.b. Pulls of individual NPs1294
Here are shown the pulls of all the NPs included in the fit on LS1 dataset.1295
1296
```
3 2 1 0 1 2 3(0)/
```
B0_BF_sig_var1B0_BF_sig_var2B0_BF_sig_var3
B0_BF_sig_var4B0_BF_sig_var5B0_BF_sig_var6
B0_BF_sig_var7B0_BF_tag_var1B0_BF_tag_var2
B0_BF_tag_var3B0_BF_tag_var4B0_BF_tag_var5
B0_BF_tag_var6B0_BF_tag_var7Bp_BF_sig_var1
Bp_BF_sig_var2Bp_BF_sig_var3Bp_BF_sig_var4
Bp_BF_sig_var5Bp_BF_sig_var6Bp_BF_sig_var7
Bp_BF_tag_var1Bp_BF_tag_var2Bp_BF_tag_var3
Bp_BF_tag_var4Bp_BF_tag_var5Bp_BF_tag_var6
Bp_BF_tag_var7D0tag_var1_mu_channelD0tag_var2_mu_channel
D0tag_var3_mu_channelD0tag_var4_mu_channelFEIcal_B0_var1_mu_channel
FEIcal_B0_var2_mu_channelFEIcal_B0_var3_mu_channelFEIcal_B0_var4_mu_channel
FEIcal_Bp_var1_mu_channelFEIcal_Bp_var2_mu_channelFEIcal_Bp_var3_mu_channel
FEIcal_Bp_var4_mu_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_BBbar
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_mu_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_mu_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_mu_channel_BBbar
d0_FF_DlvDslv_tag_var1d0_FF_DlvDslv_tag_var2d0_FF_DlvDslv_tag_var3
d0_FF_DlvDslv_tag_var4d0_FF_DlvDslv_tag_var5d0_FF_DlvDslv_tag_var6
d0_FF_DlvDslv_tag_var7d0_FF_DlvDslv_tag_var8d0_FF_DlvDslv_tag_var9
d1_FF_DlvDslv_sig_var1d1_FF_DlvDslv_sig_var2d1_FF_DlvDslv_sig_var3
d1_FF_DlvDslv_sig_var4d1_FF_DlvDslv_sig_var5d1_FF_DlvDslv_sig_var6
d1_FF_DlvDslv_sig_var7d1_FF_DlvDslv_sig_var8d1_FF_DlvDslv_sig_var9
d1_d0_pCMS_BB_var10_mu_channeld1_d0_pCMS_BB_var11_mu_channeld1_d0_pCMS_BB_var12_mu_channel
d1_d0_pCMS_BB_var13_mu_channeld1_d0_pCMS_BB_var1_mu_channeld1_d0_pCMS_BB_var2_mu_channel
d1_d0_pCMS_BB_var3_mu_channeld1_d0_pCMS_BB_var4_mu_channeld1_d0_pCMS_BB_var5_mu_channel
d1_d0_pCMS_BB_var6_mu_channeld1_d0_pCMS_BB_var7_mu_channeld1_d0_pCMS_BB_var8_mu_channel
d1_d0_pCMS_BB_var9_mu_channelmuID_K_fake_var1_mu_channelmuID_K_fake_var2_mu_channel
muID_K_fake_var3_mu_channelmuID_K_fake_var4_mu_channelmuID_eff_var1_mu_channel
muID_pi_fake_var1_mu_channelmuID_pi_fake_var2_mu_channel
```
3 2 1 0 1 2 3(0)/
```
muID_pi_fake_var3_mu_channelmuID_pi_fake_var4_mu_channeltracking
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_SCFSCF_shape
ROE_nROEg_c2_bbS_32_kcorr_c0_var1_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var2_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var4_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var5_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_mu_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var7_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var8_mu_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_mu_channel_nonBB
d0_dmID_c0_var1_mu_channeld0_dmID_c0_var2_mu_channeld0_dmID_c0_var3_mu_channel
d0_dmID_c0_var4_mu_channelROE_nROEg_c2_bbS_32_kcorr_BB_var1_mu_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_mu_channel_rareBB
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_mu_channel_rareBBrareBB_shape_KLKLlnu_rareBBrareBB_shape_nnlnu_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_mu_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var4_mu_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_mu_channel_signalFEIcal_B0_var1_e_channel
FEIcal_B0_var2_e_channelFEIcal_B0_var3_e_channelFEIcal_B0_var4_e_channel
FEIcal_Bp_var1_e_channelFEIcal_Bp_var2_e_channelFEIcal_Bp_var3_e_channel
FEIcal_Bp_var4_e_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var4_e_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var5_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_e_channel_BBbar
FIG. 171. Pulls of all the NPs included in the fit on LS1 dataset.
217
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_e_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_e_channel_BBbar
d1_d0_pCMS_BB_var10_e_channeld1_d0_pCMS_BB_var11_e_channeld1_d0_pCMS_BB_var12_e_channel
d1_d0_pCMS_BB_var13_e_channeld1_d0_pCMS_BB_var1_e_channeld1_d0_pCMS_BB_var2_e_channel
d1_d0_pCMS_BB_var3_e_channeld1_d0_pCMS_BB_var4_e_channeld1_d0_pCMS_BB_var5_e_channel
d1_d0_pCMS_BB_var6_e_channeld1_d0_pCMS_BB_var7_e_channeld1_d0_pCMS_BB_var8_e_channel
d1_d0_pCMS_BB_var9_e_channeleID_K_fake_var1_e_channeleID_K_fake_var2_e_channel
eID_K_fake_var3_e_channeleID_K_fake_var4_e_channeleID_eff_var1_e_channel
eID_eff_var2_e_channeleID_eff_var3_e_channeleID_pi_fake_var1_e_channel
eID_pi_fake_var2_e_channeleID_pi_fake_var3_e_channeleID_pi_fake_var4_e_channel
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_SCFROE_nROEg_c2_bbS_32_kcorr_c0_var1_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_e_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_e_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_e_channel_nonBBd0_dmID_c0_var1_e_channel
d0_dmID_c0_var2_e_channeld0_dmID_c0_var3_e_channeld0_dmID_c0_var4_e_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_e_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_e_channel_rareBB
```
3 2 1 0 1 2 3(0)/
```
ROE_nROEg_c2_bbS_32_kcorr_BB_var3_e_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_sig_var1_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_e_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var3_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var4_e_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_e_channel_signal
FEIcal_B0_var1_hadronic_channelFEIcal_B0_var2_hadronic_channelFEIcal_B0_var3_hadronic_channel
FEIcal_B0_var4_hadronic_channelFEIcal_Bp_var1_hadronic_channelFEIcal_Bp_var2_hadronic_channel
FEIcal_Bp_var3_hadronic_channelFEIcal_Bp_var4_hadronic_channelROE_nROEg_c2_bbS_32_kcorr_BB_var10_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var4_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var5_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var6_hadronic_channel_BBbar
ROE_nROEg_c2_bbS_32_kcorr_BB_var7_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var8_hadronic_channel_BBbarROE_nROEg_c2_bbS_32_kcorr_BB_var9_hadronic_channel_BBbar
d1_d0_pCMS_BB_var10_hadronic_channeld1_d0_pCMS_BB_var11_hadronic_channeld1_d0_pCMS_BB_var12_hadronic_channel
d1_d0_pCMS_BB_var13_hadronic_channeld1_d0_pCMS_BB_var14_hadronic_channeld1_d0_pCMS_BB_var15_hadronic_channel
d1_d0_pCMS_BB_var16_hadronic_channeld1_d0_pCMS_BB_var17_hadronic_channeld1_d0_pCMS_BB_var18_hadronic_channel
d1_d0_pCMS_BB_var19_hadronic_channeld1_d0_pCMS_BB_var1_hadronic_channeld1_d0_pCMS_BB_var20_hadronic_channel
d1_d0_pCMS_BB_var21_hadronic_channeld1_d0_pCMS_BB_var22_hadronic_channeld1_d0_pCMS_BB_var23_hadronic_channel
d1_d0_pCMS_BB_var24_hadronic_channeld1_d0_pCMS_BB_var25_hadronic_channeld1_d0_pCMS_BB_var2_hadronic_channel
d1_d0_pCMS_BB_var3_hadronic_channeld1_d0_pCMS_BB_var4_hadronic_channel
```
3 2 1 0 1 2 3(0)/
```
d1_d0_pCMS_BB_var5_hadronic_channeld1_d0_pCMS_BB_var6_hadronic_channeld1_d0_pCMS_BB_var7_hadronic_channel
d1_d0_pCMS_BB_var8_hadronic_channeld1_d0_pCMS_BB_var9_hadronic_channelneutral_pi_var1_hadronic_channel
neutral_pi_var2_hadronic_channelneutral_pi_var3_hadronic_channelpiID_eff_var1_hadronic_channel
piID_eff_var2_hadronic_channelpiID_eff_var3_hadronic_channelpiID_fake_var1_hadronic_channel
piID_fake_var2_hadronic_channelpiID_fake_var3_hadronic_channelpiID_fake_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_SCFROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_SCFROE_nROEg_c2_bbS_32_kcorr_c0_var1_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var2_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var3_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var4_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var5_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var6_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var7_hadronic_channel_nonBB
ROE_nROEg_c2_bbS_32_kcorr_c0_var8_hadronic_channel_nonBBROE_nROEg_c2_bbS_32_kcorr_c0_var9_hadronic_channel_nonBBd0_dmID_c0_var1_hadronic_channel
d0_dmID_c0_var2_hadronic_channeld0_dmID_c0_var3_hadronic_channeld0_dmID_c0_var4_hadronic_channel
ROE_nROEg_c2_bbS_32_kcorr_BB_var1_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var2_hadronic_channel_rareBBROE_nROEg_c2_bbS_32_kcorr_BB_var3_hadronic_channel_rareBB
ROE_nROEg_c2_bbS_32_kcorr_sig_var1_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var2_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var3_hadronic_channel_signal
ROE_nROEg_c2_bbS_32_kcorr_sig_var4_hadronic_channel_signalROE_nROEg_c2_bbS_32_kcorr_sig_var5_hadronic_channel_signalBBbar_normsys
nonBB_normsysrareBB_normsys
```
FIG. 172. Pulls of all the NPs included in the fit on LS1 dataset (cont.).
```
G.c. Post-fit plots1297
Here are show additional post-fit data/MC comparison plots.1298
218
0
100
200
300
Events / 0.21
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
100
200
300
Events / 0.21
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
25
50
75
100
125
Events / 0.21
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
FIG. 173. Post-fit distributions for the 3 channels
219
0
250
500
750
1000
Events / 0.05
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (µ channel)
```
5
0
5
Data
MCData
0
200
400
600
800
Events / 0.05
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (e channel)
```
5
0
5
Data
MCData
0
100
200
300
Events / 0.05
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
```
XGBoost output (hadronic channels)
```
5
0
5
Data
MCData
FIG. 174. Post-fit distributions for the 3 channels
220
0
200
400
600
800
Events / 1.00
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
200
400
600
Events / 1.00
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
100
200
300
Events / 1.00
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
FIG. 175. Post-fit distributions for the 3 channels
221
G.d. Post-fit plots: SR cut1299
Here are shown post-fit data/MC comparison plots with a cut on the signal region1300
EROEextra < 0.3 GeV, corresponding to the first 3 bins of EROEextra.1301
0
20
40
60
80
100
Events / 0.18 GeV/
c
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
20
40
60
80
Events / 0.18 GeV/
c
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.5 1.0 1.5 2.0
pvis [GeV/c]
5
0
5
Data
MCData
0
10
20
30
40
50
Events / 0.18 GeV/
c
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
1.0 1.5 2.0 2.5
pvis [GeV/c]
5
0
5
Data
MCData
FIG. 176. Post-fit distributions for the 3 channels in the SR.
222
0
20
40
60
80
Events / 0.21
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
20
40
60
Events / 0.21
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
10
20
30
Events / 0.21
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
FIG. 177. Post-fit distributions for the 3 channels in the SR.
223
0
100
200
300
Events / 1.00
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
50
100
150
200
Events / 1.00
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
25
50
75
100
125
Events / 1.00
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
FIG. 178. Post-fit distributions for the 3 channels in the SR.
224
G.e. Post-fit plots: pvis cut1302
Post-fit data/MC comparison plots with a cut on the momentum of the τ daughter1303
pvis < 1.3 GeV/c and pvis < 1.8 GeV/c for leptonic and hadronic modes respectively,1304
shown in Figures 179 to 181. The inverted cut plots are shown in Figures 182 to 1841305
0
50
100
150
200
Events / 0.10 GeV
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
50
100
150
200
Events / 0.10 GeV
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
80
100
Events / 0.10 GeV
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
FIG. 179. Post-fit distributions for the 3 channels for low momentum τ daughters
.
225
0
50
100
150
Events / 0.21
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
50
100
150
Events / 0.21
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
20
40
60
80
Events / 0.21
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
FIG. 180. Post-fit distributions for the 3 channels for low momentum τ daughters
.
226
0
100
200
300
Events / 1.00
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
100
200
300
Events / 1.00
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
50
100
150
Events / 1.00
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
FIG. 181. Post-fit distributions for the 3 channels for low momentum τ daughters
.
227
0
100
200
300
Events / 0.10 GeV
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
50
100
150
200
250
Events / 0.10 GeV
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
0
20
40
60
Events / 0.10 GeV
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0.0 0.2 0.4 0.6 0.8 1.0
EROEextra [GeV]
5
0
5
Data
MCData
FIG. 182. Post-fit distributions for the 3 channels for high momentum τ daughters
.
228
0
50
100
150
200
Events / 0.21
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
50
100
150
Events / 0.21
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
0
20
40
60
Events / 0.21
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
3 2 1 0 1
cos θ ∗Btag, Dl
5
0
5
Data
MCData
FIG. 183. Post-fit distributions for the 3 channels for high momentum τ daughters
.
229
0
100
200
300
400
Events / 1.00
Post-fitchannel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
100
200
300
400
Events / 1.00
Post-fite channel Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
0
25
50
75
100
Events / 1.00
Post-fitHadronic chan. Belle II preliminary L dt = 365 fb 1
SignalSCF
Rare BBNon -BB
BBData
0 5 10 15 20
NROE
5
0
5
Data
MCData
FIG. 184. Post-fit distributions for the 3 channels for high momentum τ daughters
.
230
[1] T. Kuhr et al., Belle II collaboration, The Belle II Core Software, Comput. Softw.1306
```
Big. Sci. 3 (2018) , arXiv:1809.04299 [physics.comp-ph].1307
```
[2] C. Praz and T. Fillinger, plothist - A Python package for plotting histograms,1308
Zenodo, BSD-3-Clause . https://plothist.readthedocs.io/en/latest/.1309
[3] A. Crivellin, S. Iguro, and T. Kitahara, Discriminating Tauphilic Leptoquark1310
Explanations of the B Anomalies via K → πν ¯ν and B → Kν ¯ν, arXiv:2505.055521311
[hep-ph].1312
[4] S. Navas et al., Particle Data Group, Review of particle physics, Phys. Rev. D 1101313
```
(2024) no. 3, 030001.1314
```
```
[5] Y. Aoki et al., Flavour Lattice Averaging Group (FLAG), FLAG Review 2024 ,1315
```
```
arXiv:2411.04268 [hep-lat].1316
```
[6] A. Sibidanov et al., Belle, Study of Exclusive B → Xuℓν Decays and Extraction of1317
∥Vub∥ using Full Reconstruction Tagging at the Belle Experiment, Phys. Rev. D 881318
```
(2013) no. 3, 032005, arXiv:1306.2781 [hep-ex].1319
```
[7] G. Branco et al., Theory and phenomenology of two-Higgs-doublet models, Physics1320
```
Reports 516 (2012) no. 1-2, 1–102.1321
```
[8] M. Tanaka and R. Watanabe, New physics contributions in B → πτ ¯ν and1322
```
B+ → τ +ντ , Progress of Theoretical and Experimental Physics 2017 (2017) no. 1, .1323
```
[9] B. Kronenbitter et al., Belle, Measurement of the branching fraction of B+ → τ +ντ1324
```
decays with the semileptonic tagging method , Phys. Rev. D 92 (2015) no. 5, 051102,1325
```
```
arXiv:1503.05613 [hep-ex].1326
```
[10] B. Aubert et al., BaBar, A Search for B+ → ℓ+νℓ Recoiling Against B− → D0ℓ− ¯νX,1327
```
Phys. Rev. D 81 (2010) 051101, arXiv:0912.2453 [hep-ex].1328
```
[11] I. Adachi et al., Belle, Evidence for B− → τ − ¯ντ with a Hadronic Tagging Method1329
```
Using the Full Data Sample of Belle, Phys. Rev. Lett. 110 (2013) no. 13, 131801,1330
```
```
arXiv:1208.4678 [hep-ex].1331
```
[12] J. P. Lees et al., BaBar, Evidence of B+ → τ +ν decays with hadronic B tags, Phys.1332
```
Rev. D 88 (2013) no. 3, 031102, arXiv:1207.0698 [hep-ex].1333
```
[13] I. Adachi et al., Belle II, Measurement of B+ → τ +ντ branching fraction with a1334
hadronic tagging method at Belle II , arXiv:2502.04885 [hep-ex].1335
[14] T. Keck et al., The Full Event Interpretation: An Exclusive Tagging Algorithm for1336
```
the Belle II Experiment, Comput. Softw. Big Sci. 3 (2019) no. 1, 6,1337
```
```
arXiv:1807.08680 [hep-ex].1338
```
[15] T. Chen and C. Guestrin, XGBoost: A Scalable Tree Boosting System, in1339
Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge1340
Discovery and Data Mining, KDD ’16. ACM, 2016.1341
231
```
http://dx.doi.org/10.1145/2939672.2939785.1342
```
[16] T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama, Optuna: A Next-generation1343
Hyperparameter Optimization Framework , arXiv:1907.10902 [cs.LG].1344
```
https://arxiv.org/abs/1907.10902.1345
```
[17] D. M. Asner et al., Search for exclusive charmless hadronic B decays, Phys. Rev.1346
```
D53 (1996) 1039.1347
```
[18] G. C. Fox and S. Wolfram, Observables for the Analysis of Event Shapes in e+e−1348
```
Annihilation and Other Processes, Phys. Rev. Lett. 41 (1978) 1581–1585.1349
```
```
https://link.aps.org/doi/10.1103/PhysRevLett.41.1581.1350
```
[19] S. H. Lee et al., Belle Collaboration, Evidence for B0 → π0π0, Phys. Rev. Lett. 911351
```
(2003) 261801. https://link.aps.org/doi/10.1103/PhysRevLett.91.261801.1352
```
[20] M. Feickert, L. Heinrich, and G. Stark, pyhf: a pure-Python statistical fitting library1353
```
with tensors and automatic differentiation, PoS ICHEP2022 (2022) 245,1354
```
```
arXiv:2211.15838 [hep-ex].1355
```
[21] A. Held, cabinetry: v0.6.0 , .1356
```
https://github.com/scikit-hep/cabinetry/releases/tag/v0.6.0.1357
```
[22] M. Mantovano et al., Simultaneous analysis of B → Dℓν and B → D∗ℓν decays,1358
```
BELLE2-NOTE-PH-2024-045 (2025) . https://docs.belle2.org/files/16/BELLE1359
```
2-NOTE-PH-2024-045/3/BELLE2-NOTE-PH-2024-045.pdf.1360
[23] R. Aaij et al., LHCb, Observation of the semileptonic decay B+ → ppµ+νµ, JHEP1361
```
03 (2020) 146, arXiv:1911.08187 [hep-ex].1362
```
[24] L. Matic, Measurement of the decay B+ → K+K−ℓ+νℓ with B2BII , Belle Note 14861363
```
(2018) .1364
```
```
https://belle.kek.jp/secured/belle_note/gn1486/bnote_1486_lubej_v5.pdf.1365
```
[25] R. Glattauer et al., Belle Collaboration, Measurement of the decay B → Dℓνℓ in1366
fully reconstructed events and determination of the Cabibbo-Kobayashi-Maskawa1367
```
matrix element |Vcb|, Phys. Rev. D 93 (2016) 032006.1368
```
```
https://link.aps.org/doi/10.1103/PhysRevD.93.032006.1369
```
[26] D. Ferlewicz, P. Urquijo, and E. Waheed, Revisiting fits to B0 → D∗−ℓ+νℓ to1370
measure |Vcb| with novel methods and preliminary LQCD data at nonzero recoil ,1371
```
Phys. Rev. D 103 (2021) 073005.1372
```
```
https://link.aps.org/doi/10.1103/PhysRevD.103.073005.1373
```
[27] F. U. Bernlochner, S. Duell, Z. Ligeti, M. Papucci, and D. J. Robinson, HAMMER -1374
Helicity Amplitude Module for Matrix Element Reweighting, .1375
```
https://doi.org/10.5281/zenodo.11245573.1376
```
[28] F. U. Bernlochner, S. Duell, Z. Ligeti, M. Papucci, and D. J. Robinson, Das ist der1377
```
HAMMER: consistent new physics interpretations of semileptonic decays, Eur. Phys.1378
```
J. C 80 (2020) no. 10, 883, arXiv:2003.02291 [hep-ph].1379
232
```
[29] I. Tsaklidis et al., Measurement of the R(D∗) ratio and Pτ in hadronic 1-prong τ1380
```
decays with the hadronic Full Event Interpretation at Belle II ,1381
```
BELLE2-NOTE-PH-2025-031 (2025) . https://docs.belle2.org/files/4547/BEL1382
```
LE2-NOTE-PH-2025-031/7/BELLE2-NOTE-PH-2025-031.pdf.1383
[30] F. U. Bernlochner, Z. Ligeti, M. Papucci, M. T. Prim, D. J. Robinson, and C. Xiong,1384
```
Constrained second-order power corrections in HQET: R(D(∗)), |Vcb|, and new1385
```
```
physics, Phys. Rev. D 106 (2022) 096015.1386
```
```
https://link.aps.org/doi/10.1103/PhysRevD.106.096015.1387
```
```
[31] S. Banerjee et al., Heavy Flavor Averaging Group (HFLAV), Averages of b-hadron,1388
```
c-hadron, and τ -lepton properties as of 2023 , arXiv:2411.18639 [hep-ex].1389
[32] I. Adachi et al., Belle-II, Search for B0→K*0τ +τ - Decays at the Belle II Experiment,1390
```
Phys. Rev. Lett. 135 (2025) no. 15, 151801, arXiv:2504.10042 [hep-ex].1391
```
[33] A. Pinto, Z. Wu, F. Balli, N. Berger, M. Boonekamp, ´E. Chapon, T. Kawamoto, and1392
B. Malaescu, Uncertainty components in profile likelihood fits, Eur. Phys. J. C 841393
```
(2024) no. 6, 593, arXiv:2307.04007 [physics.data-an].1394
```
[34] R. Okubo et al., Measurement of Time-Dependent CP Asymmetry in B → ρρ and1395
Extraction of the CKM angle ϕ2 using 2019-2022 data,1396
```
BELLE2-NOTE-PH-2024-011 (2024) . https://docs.belle2.org/files/4495/BEL1397
```
LE2-NOTE-PH-2025-023/1/BELLE2-NOTE-PH-2025-023.pdf.1398
233