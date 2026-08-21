Belle1
BELLE2-NOTE-PH-2023-0132
Version 5.33
November 26, 20254
5
Measurements of inclusive B → Xuℓν decays and |Vub| with6
hadronic tagging7
Tommy Martinov,∗ Martin Angelsmark, Florian Bernlochner, Lu Cao, Merle8
Graf-Schreiber, Marcel Hohmann, Munira Khan, Kerstin Tackmann, and Phillip Urquijo9
```
(The Belle II Collaboration)10
```
Abstract11
This analysis note presents the analysis details of the inclusive charmless semileptonic B → Xuℓν12
decays. The study makes use of hadronic tagging and is performed on the LS1 data set. The13
B → Xuℓν partial branching fraction and |Vub| in various phase-space regions are measured.14
∗ tommy.martinov@desy.de
1
1. Change Log15
v2.0:16
• Rephrased parts of the text for the sake of clarity17
• Now using the full available MC15 ri data set18
– Updated continuum suppression MVA classifier19
– Updated B → Xcℓν MVA classifier20
– Updated fit21
– Updated plots22
• A linearity check of the fit was added23
• A bug with the γS systematic calculation was fixed24
• The description of the correction factor extraction has not been updated as a new25
strategy is currently being tested26
• Added Table XVI: it lists the various fiducial regions used for the fit together with27
their corresponding acceptances28
• Added Tables XVIII to XXII: the set of fits intended to be used for signal extraction29
together with their corresponding Asimov results is given30
• A plan for the extraction of |Vub| was added31
v3.0:32
• Added information about train and test samples for MVAs33
• Removed the kaon multiplicities from Tab. IX34
• Added description of the exact procedure used to correct the B → Xcℓν shape in35
Section 7 3 336
• A precise description of the new signal extraction setup is given in Section 837
• Updated all plots and branching fractions obtained from the fit in Section 838
• Added extracted values of |Vub| in Section 8 939
• Added distributions of Xcℓν suppression MVA input features in Appendix C40
• Added information about pyhf as a fitting tool and how we use it in this analysis to41
extract the signal in Appendix E42
• Added plots from all fits in Appendix F43
• Added information about the impact of KL on the analysis in Appendix G44
v4.0:45
2
```
• The recommended value of f ±/00 is now used; value obtained from Belle measure-46
```
ment [1] rather than PDG value47
• The B → ηℓν was updated based on the latest PDG average48
• The exclusive B → Xcℓν branching fractions were updated based on the latest HFLAV49
```
public averages (2021)50
```
• A section describing the systematic uncertainties related to the continuum calibration51
was added52
• A table summarising all fit parameters was added to Appendix E53
• The nCDCHits > 0 requirement for leptons was removed and hadron ID correction54
factors were computed with a nCDCHits > 20 requirement55
• A description of the high-momentum π± selection was added in Section 3 2 356
• Descriptions of the Xu hadronisation modelling and fit-related uncertainties were57
added in Section 658
• Added in Appendix H plots to illustrate the efficiency and fake rate of kaon and pion59
ID for the likelihood-based and the neural-network-based scores60
• Fits 2 and 6 were dropped as their output was estimated to not be as meaningful as for61
other fits. The numbering of other fits is kept the same to allow for easy comparison62
with previous versions of the analysis note.63
v4.1:64
• Added a fit systematics breakdown in Table XXIV65
• Added data-MC comparison of pBℓ , MX and q2 using off-resonance samples in Figure 1166
• Added data-MC comparison of pBℓ , MX and q2 in the wrong-sign-lepton region in67
Figure 3268
• Updated plots and description in Appendix G69
• Documented in Section 8 10 and Appendix I the following test proposed during working70
group review: repeat the fit procedure with data using only the control region CR0,low71
split in two in order to evaluate the B → Xcℓν correction procedure72
v4.2:73
• Corrected Sections 3 2 1 and 3 2 5 as the events with multiple signal and ROE lepton74
candidates are now rejected75
• Added low-lepton-momentum region plots in Appendix J76
• A small bug was fixed when computing the input signal BR for the fit77
• Documented the split lepton flavour e/µ in Section 8 11 2 and Appendix K78
3
• Performed two additional split sample fits as discussed in Section 8 11 379
```
• Added Section 9 dedicated to the unblinded results; for now, a proposed unblinding80
```
plan is detailed in that Section81
• Updated continuum reweighting plots in Section 4 and added plots of all variables82
used for training in Appendix L83
• Added plots of the track and cluster multiplicities in Appendix M in order to study84
the topology differences between between B → Xuℓν and B → Xcℓν events85
• Added in Appendix N a study of a sample with an FEI cut set at PFEI > 0.001 instead86
of 0.01 as in our nominal sample87
• Added in Section 7 adetails about the data and MC efficiencies for various cuts88
v4.389
• A small bug in the template definition was fixed and the stability of fits was recon-90
```
sidered: fit 7 and fit 1 with lepton flavour split are dropped from the list of results;91
```
in fit 3 and 5, the ”other backgrounds” template normalisation is fixed because of the92
relatively low yields in the considered regions93
• Added a test of the fit setup using CRK,low and CRK,high in Section 8 10 294
• Added a summary of the discussion with Peter Skands regarding the parameter in95
Appendix O96
• Added plots of the efficiency as a function of pBℓ , MX and q2 in Appendix P97
v4.498
```
• Use the 2D variable pBℓ :q2 for the nominal fit; replaced figures and rephrased text99
```
wherever relevant100
• Use the CRK,high region to produce pseudo-data for the signal region101
• Rephrased the MC and data efficiency discussion in Section 7102
• Show full MC efficiency in Appendix P using generator level samples103
v4.5104
```
• Updated B(B → Xcℓν) based on HFLAV 2023 and updated all relevant fit results105
```
• Added section 8 10 3 to document the CR0,low-CRK,high fit106
v4.6107
• Documented the fit projection in Appendix E 4108
• Documented the Xu fragmentation in Section 6 14109
```
• Updated unblinding plan based on discussion with RC (Section 9)110
```
4
v5.0111
• The first unboxing step was performed. The results of the CR0,low - VR2 fits are112
documented in Section 9 2 and Appendix Q.113
v5.1114
• The second unboxing step was performed. The results and the added corrections and115
uncertainties are documented in Section 9 3 and Appendix S.116
v5.2117
• The final unboxing step was performed. The results are documented in Section 9 4.118
v5.3119
• During CWR2, a question was raised about the shift in the fraction of kaon events120
in inclusive B → Xuℓν events caused by the hybrid procedure. The results of the121
conducted tests are documented in Appendix O.122
CONTENTS123
1. Change Log 2124
1. Introduction 9125
2. Modelling 10126
1. Data 10127
2. Monte Carlo simulation 10128
1. B → Xuℓν 10129
2. Hybrid model 11130
3. BLNP model issues 12131
4. B → Xcℓν 13132
5. Continuum 15133
6. Other 16134
3. Charm Decay Modelling 16135
3. Event selection and Reconstruction 19136
1. Tag Side 19137
1. Continuum Suppression Masks 19138
2. Signal Side 20139
1. Rest Of Event 20140
2. Slow π 21141
3. High-momentum π± 21142
4. Kaons 22143
5. Signal Lepton 22144
6. J/ψ and Photon Conversion Vetoes 23145
3. Other selections 24146
5
4. Continuum Modelling 25147
1. Input Variables 25148
1. Classifier Training 26149
2. Variable Importance 28150
3. Uncertainty 29151
4. Results 29152
5. Multivariate selection 32153
1. Classifiers and training 32154
1. Continuum suppression 32155
2. B → Xcℓν background 34156
2. MVA-induced model dependence 41157
6. Corrections and Systematics 43158
1. Slow π efficiency 43159
2. Tracking efficiency 44160
3. Form factors 44161
1. B → Xuℓν form factors 45162
2. B → Xcℓν form factors 46163
4. Charged particle identification 47164
5. FEI tagging 48165
6. Branching fractions 48166
7. Hybrid parameter variations 49167
8. Inclusive model differences 49168
9. K0S efficiency 50169
10. s¯s fragmentation 50170
11. MC statistics 50171
12. f ±/0 50172
13. Continuum calibration 50173
14. Xu hadronisation modelling 50174
15. Uncertainties related to the fitting procedures 51175
7. Data-MC agreement 52176
1. Kinematic distributions 53177
2. Sample compositions 53178
3. Data-MC disagreement 53179
1. Origin of the data-MC disagreement 55180
2. Normalisation mismodelling 59181
3. Shape mismodelling 64182
8. Signal extraction 66183
1. pyhf 66184
2. Fit templates, free-floating parameters and phase-space regions 66185
3. Fit parameters 68186
1. Implementation of systematic uncertainties within the fit 69187
4. Symmetrising 71188
5. List of fits 71189
6. ∆B(B → Xuℓν) measurement 73190
6
1. Asimov test 73191
2. Systematics breakdown 77192
7. Fitter validation 79193
1. Toy fit 79194
2. Linearity check 79195
8. B → Xcℓν factors 82196
9. |Vub| measurement 83197
10. Fits with control regions 86198
1. Fit with CR0,low split 86199
2. Fit with CRK,low and CRK,high 86200
3. Fit with CR0,low and CRK,high 87201
11. Split sample fits 88202
1. Fit with split B charge: ∆B(B0 → Xuℓν), ∆B(B± → Xuℓν) 88203
2. Fit with split lepton flavour: ∆B(B → Xueν), ∆B(B → Xuµν) 88204
3. Additional split sample fits: split missing momentum θ angle and split lepton205
charge 90206
9. Box opening 97207
1. Proposed unblinding strategy 97208
2. Step 1: CR0,low - VR2 fit 97209
3. Step 2: signal region plots and first checks 102210
4. Final unboxing step: perform the three nominal fits 107211
A. BLNP modelling 116212
B. Continuum suppression MVA input features 119213
C. Xcℓν suppression MVA input features 128214
D. Data - MC comparison in SB1 in different channels 131215
E. pyhf 135216
1. Notation 135217
2. Statistical model 136218
3. Modifiers 136219
4. Postfit projections 137220
F. Plots from fits to all variables in all regions 140221
1. q2 fit 140222
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV 140223
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,224
Experimental cut: pBℓ > 1.0 GeV 144225
3. Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0 GeV 148226
2. pBℓ fit 152227
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV 152228
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,229
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 156230
3. MX fit 159231
7
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV 159232
4. MX :q2 fit 162233
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV 162234
5. pBℓ :q2 fit 166235
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV 166236
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, Experimental cut:237
pBℓ > 1.0 GeV, MX < 1.7 GeV 170238
G. KL 174239
H. Hadron ID 177240
I. Fits with control regions 178241
1. Fit 3 178242
2. Fit 5 182243
J. Low-lepton-momentum region 186244
K. Fit with split lepton flavour 187245
1. Electron 187246
2. Muon 190247
L. Continuum reweighting variables 192248
1. Before applying corrections 192249
2. After applying corrections 202250
M. Track and cluster multiplicities 212251
N. Low FEI cut studies 214252
O. Strange quark fragmentation 218253
1. γs 218254
2. Fraction of kaons before/after hybridisation 218255
P. Variable dependent efficiency 220256
Q. VR2 fits 223257
1. Fit 3 223258
2. Fit 5 227259
R. Signal region distributions 231260
1. Splits in lepton flavour 231261
2. Fit 3 region: EBℓ > 1.0 GeV, MX < 1.7 GeV 233262
3. Fit 5 region: EBℓ > 1.0 GeV, MX < 1.7 GeV 234263
S. Additional fit corrections 235264
1. Fit 3 235265
2. Fit 5 237266
References 239267
8
1. INTRODUCTION268
The discrepancy between inclusive and exclusive measurements of the CKM matrix element269
|Vub| has posed a longstanding puzzle. The major difficulty involved with the inclusive |Vub|270
measurement is the determination of the non-perturbative distribution function describing271
the internal Fermi motion of the b-quark. On the experimental aspect, the measurement of272
B → Xuℓν is challenged by the high background of the CKM-favoured B → Xcℓν decays.273
Belle II has unique advantage for the inclusive semileptonic decays with a clean experimental274
environment. As 3-body decays, semi-leptonic events can be characterised by the following275
```
three variables: the lepton momentum, pℓ (equivalent to the lepton energy Eℓ1, in the case276
```
```
of massless leptons), the mass of the hadronic system, MX and the invariant mass of the277
```
leptonic system ℓ − ν, q2.278
279
This work aims to measure the partial branching fraction of charmless semileptonic B →280
Xuℓν decays, where ℓ = e, µ and the inclusive Xu includes the non-resonant contribution and281
the exclusive resonances, e.g. π, η, η′, ρ, ω. Subsequently, the inclusive |Vub| can be extracted282
based on the underlying theoretical decay rates. The branching fraction and |Vub| will be283
measured in different phase-space regions defined by cuts to the three kinematic variables284
pBℓ , MX and q2. This measurement will also provide separate results for testing the lepton285
```
flavour universality in (e, µ) and iso-spin asymmetry of (B+, B0). Further measurements286
```
including the differential spectra of key kinematic variables, a ratio of inclusive |Vub| and287
|Vcb|, etc. are also planned.288
FIG. 1: Standard Model charmless semileptonic decay.
The analysis presented within this note is co-developed with the Weak Annihilation in289
charmless semi-leptonic decays measurement presented in BELLE2-NOTE-PH-2023-060 [2].290
There is significant overlap in the data and Monte Carlo samples, the analysis selections,291
Monte Carlo corrections, and analysis methods between both analyses.292
The basf2 release light-2311-nebelung is used.293
1 These will be denoted pBℓ , EBℓ when taken in the B-meson rest frame.
9
2. MODELLING294
1. Data295
```
The analysis will be performed on the Long Shutdown 1 (LS1) data sample, corresponding296
```
to 364.558±0.021stat ±2.297syst fb−1 collected on-resonance and a further 42.561±0.007stat ±297
0.269syst fb−1 collected off-resonance.298
2. Monte Carlo simulation299
```
The signal and background are simulated using generic MC15 (MC15ri b) which corresponds300
```
to 1 ab−1 of q ¯q events and 2.8 ab−1 of b¯b events. Specific modes must also be added. All the301
branching fractions quoted below are up-to-date with the PDG2022 [3].302
1. B → Xuℓν303
The exclusive and inclusive B → Xuℓν modes are taken from signal MC. For some of the304
```
decay modes, the branching fraction needs to be updated to a more up-to-date value (see Sec-305
```
```
tion 6 6). The considered modes with their associated branching fraction are listed in Tab. I.306
```
307
Various theoretical models exist to describe the inclusive B → Xuℓν mode. In the generic308
```
MC, the De Fazio - Neubert (DFN) model [4] is used with outdated parameters. Following309
```
Tab. IV in Ref. [5], the values of the non-perturbative parameters ¯Λ and λ1 are updated.310
Their values can then be converted to values of the b-quark mass and non-perturbative311
parameter a in the Kagan-Neubert renormalisation scheme. They are updated in the signal312
```
MC to: mKNb = (4.66 ± 0.04) GeV and aKN = 1.3 ± 0.5. The uncertainties related to these313
```
parameters are taken into account in this analysis. The DFN model is used as the nominal314
model for our samples. We were initially advised to use the Bosch - Lange - Neubert - Paz315
```
(BLNP) model [6] but various issues were spotted. These are discussed in Section 2 2 3.316
```
However, as the modelling of inclusive B → Xuℓν decays is known to be imperfect, the317
```
difference between the DFN and BLNP models is taken as an additional uncertainty (c.f.318
```
```
Section 6 for more details).319
```
320
Resonant decays are described by form factors. We give here a quick overview of the321
models used for each exclusive mode but more details about the models and associated322
uncertainties are given in and Section 6 3.323
```
π: Generated following the expansion of Bourrely, Caprini, and Lellouch (BCL) [7] to324
```
8 terms using outdated parameters. Updated to the BCL expansion truncated at 5325
terms of Tab. 57 of Ref.[8] via reweighting in q2.326
ρ/ω: Generated following the BCL expansion with outdated parameters. Updated to pa-327
rameter values of Tab. 4 of Ref.[9] via reweighting in q2.328
```
η(′): Generated via ISGW2. Updated to the light-cone-sum-rules based model of Ref.[10]329
```
via reweighting in hadronic recoil, w = m
2B +m2X −q2
2mB mX .330
10
The γS parameter in PYTHIA8 controls the suppression of s quark production relative to u331
or d production. This eventually impacts the number of K produced. Since the number of332
```
K± and K0 is used in the MVA classifier (see Section 5), this parameter can impact the333
```
post-classifier signal efficiency. Samples with varied γS values were produced: one sample334
```
with the PYTHIA8 default value, γS = 0.217; one with a more accurate value taken from the335
```
average of two measurements [11, 12], γS = 0.300 ± 0.09 and one with the +1σ variation336
taken from the same average, γS = 0.390. γS = 0.300 is the nominal value.337
338
For fragmentation and and subsequent hadronisation of the Xu system in non-resonant339
modes, PYTHIA8 is used. No Belle II dedicated tune of PYTHIA8 has been performed so340
far. The known poor modelling of fragmentation is taken into account as an additional341
```
uncertainty (see Section 6)342
```
TABLE I: Assumed branching fractions, number of generated events and decfile for the
B → Xuℓν channels. For the inclusive channel, the first entry gives the nominal sample
and the following give details on samples used to study systematic uncertainties.
Decay mode B [×10−4] Model Dec File Code N Events [×106]
B− → π0ℓν 0.780 ± 0.027 BCL 1290710003 0.188 × 50
B− → ρ0ℓν 1.58 ± 0.11 BCL 1290710003 0.380 × 50
B− → ηℓν 0.350 ± 0.040 DM 1290710003 0.091 × 50
B− → η′ℓν 0.240 ± 0.070 DM 1290710003 0.055 × 50
B− → ωℓν 1.19 ± 0.09 BCL 1290710003 0.286 × 50
```
B− → X0uℓν 19.2 ± 2.4 DFN (γs = 0.300) 1290710022 30
```
```
B− → X0uℓν 19.2 ± 2.4 DFN (γs = 0.217) 1290710012 10
```
```
B− → X0uℓν 19.2 ± 2.4 DFN (γs = 0.390) 1290710032 10
```
```
B− → X0uℓν 19.2 ± 2.4 BLNP (γs = 0.300) 1290710021 20
```
B0 → π+ℓν 1.50 ± 0.06 BCL 1190710003 0.330 × 50
B0 → ρ+ℓν 2.94 ± 0.21 BCL 1190710003 0.670 × 50
```
B0 → X+u ℓν 17.6 ± 2.2 DFN (γs = 0.300) 1190710022 30
```
```
B0 → X+u ℓν 17.6 ± 2.2 DFN (γs = 0.217) 1190710012 10
```
```
B0 → X+u ℓν 17.6 ± 2.2 DFN (γs = 0.390) 1190710032 10
```
```
B0 → X+u ℓν 17.6 ± 2.2 BLNP (γs = 0.300) 1190710022 20
```
2. Hybrid model343
Models describing inclusive B → Xuℓν decays cannot make predictions about resonant344
decays. In the latter case quark-hadron duality breaks down and therefore form factor345
models must be used. The models used in our samples are given in Tab. I. See also Section346
6 3 for a discussion about form factors. For our simulation to cover all decays, inclusive347
and exclusive contributions are combined with the hybrid approach [13]: the exclusive and348
```
inclusive contributions are summed in three-dimensional bins of Eℓ, MX and q2; in each349
```
bin, the inclusive part is scaled down such that the total contribution matches the initial350
```
inclusive contribution; this way, the total branching fraction matches the inclusive branching351
```
11
fraction and the exclusive contribution is included. Therefore, the inclusive part is scaled352
by the weights:353
```
wijk =
```
∆Bincijk − ∆Bexcijk
∆Bincijk
```
(1)
```
where ∆Binc, ∆Bexc are the partial branching fraction of the exclusive and inclusive com-
ponents respectively and the indices i, j, k define a three-dimensional bin. These three-
dimensional bins are defined by the combinations of the following one-dimensional bins:
```
q2 : [0, 2.5, 5, 7.5, 10, 12.5, 15, 20, 25] GeV2,
```
EBℓ : [0, 0.5, 1, 1.25, 1.5, 1.75, 2, 2.25, 3] GeV, and
```
MX : [0, 1.4, 1.6, 1.8, 2, 2.5, 3, 3.5] GeV.
```
The hybrid reweighting is illustrated in Fig. 2.354
0 5 10 15 20 25 30
q2 [GeV2]
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Arbitrary Normalisation
×105
ResonantInclusive - DFN
BLNPDFN
Hybrid Model
0.0 0.5 1.0 1.5 2.0 2.5 3.0
pB [GeV]
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Arbitrary Normalisation
×105
ResonantInclusive - DFN
BLNPDFN
Hybrid Model
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5m
X [GeV]
0.00
1.00
2.00
3.00
4.00
5.00
Arbitrary Normalisation
×105
ResonantInclusive - DFN
BLNPDFN
Hybrid Model
FIG. 2: Projections of the hybrid MC in MX , EBℓ and q2 in the B+ → Xuℓν channel. The
grey vertical dotted lines show the boundaries of the bins used for hybrid weights
calculations from Equ. 1. A finer binning is used to illustrate the hybrid procedure.
3. BLNP model issues355
First, many of the calculated hybrid weights were noticed to be negative, corresponding356
to bins where the number of exclusive events exceeds the number of inclusive ones. These357
weights are usually set to 0 which has the consequence of over-estimating the inclusive rate.358
However, if the number of negative weights is limited they will have little to no effect. In359
12
0.0 0.5 1.0 1.5 2.0 2.5
EB [GeV]
0
5
10
15
20
25
q2
[GeV
2]
```
BLNP: 8,000,000 events; no cuts; B±/B0
```
0
100
200
300
400
500
600
700
800
FIG. 3: Two-dimensional histogram of q2 versus EBℓ for 8 million events generated with
the most up-to-date input values for the BLNP model in EvtGen.
this case their number was relatively large and they could’ve spoiled the hybrid modelling360
of B → Xuℓν. Moreover, as illustrated in Fig. 3 an unexpected spike of events was observed361
in 2D plots of EBℓ , q2 and MX which doesn’t appear in 1D plots. More details about this362
feature are discussed in Appendix A.363
4. B → Xcℓν364
Specific B → Xcℓν decays are also replaced in the generic MC by dedicated signal MC. In365
```
particular, modes such as B → D0(→ Dππ)ℓν must be added to the samples in order to366
```
fill the gap between the total B → Xcℓν branching fraction measured from the sum of all367
```
exclusive modes and the one measured from the inclusive mode (so far no inclusive predic-368
```
```
tions exist for B → Xcℓν decays as they do for charmless decays). The nominal B → Xcℓν369
```
and gap modes are listed in Tab. II with associated branching fractions for B+ and B0.370
371
We give here a quick overview of the B → Xcℓν form factor models:372
• B → Dℓν: in the generic MC these decays are modelled using the BGL form factor373
```
parametrisation [14]. B → Dℓν events are modelled using the N = 3 expansion (8374
```
```
parameters). The B → Dℓν decays are described using the leptonic system invariant375
```
```
mass q2 (or alternatively the w recoil parameter)2 and the angle between the direction376
```
2 w = m2B +m2X −q22m
B mX
13
of the lepton momentum in the W rest frame and the direction of the W momentum377
in the B rest frame, θℓ. We update the modelling to the BLPRXP model [15] using378
the HAMMER package [16].379
```
• B → D∗ℓν: in the generic MC, modelled using the (1, 1, 2) expansion of the BGL380
```
```
parametrisation (6 parameters). As D∗ mesons decay typically to Dπ/γ, to describe381
```
them one needs to consider in addition of q2 and θℓ the following variables: the angle382
between the direction of the D meson momentum in the D∗ rest frame and the direction383
of the D∗ momentum in the B rest frame, θV and the angle between the planes defined384
by the leptonic system and the D∗ system, χ. Also updated to the BLPRXP model.385
```
• B → D∗∗ℓν: modelled using the BLR form factor model (previously called LLSW).386
```
There are 3 parameters for D0 and D′1 and 4 parameters for D1 and D2. The values387
of these parameters were updated following Ref. [17]. An issue was spotted with the388
modelling of the two broad D∗∗ channels, D0 and D′1. Because of their very large389
width, in some events the generated D∗∗ mass is much larger than the nominal one.390
It was observed that these events lead to an unphysical enhancement of the w ≈ 1391
```
region. Therefore, events with a mass more than 3 (resp. 2.5) times higher than the392
```
```
nominal D0 (resp. D′1) mass are rejected. After this cut is applied, all the remaining393
```
events are up-scaled accordingly. The scale factor is calculated separately for each D∗∗394
decay channel including the gap modes with EvtGen truth samples.395
```
• B− → D(∗)+s K−ℓν: taken from the generic MC, where they are modelled with PHSP,396
```
for lack of a better model. We expect these decays to have a negligible impact, as397
their branching fraction is low, ∼ 3 × 10−4 [18]398
• B → D∗∗Gapℓν: There remains a significant gap between the sum of branching fractions399
of all measured channels and the measured branching fractions of B → Xcℓν. The400
```
missing branching fraction is filled with final states of the type B → D(∗)ππℓν and401
```
```
B → D(∗)ηℓν. Within the generic MC these channels are simulated via PHSP. As402
```
these are four and five body decays this gives an extremely soft lepton momentum403
spectrum. We replace the events from the generic MC with events simulated through404
```
intermediate resonances, using the two broad D∗∗ resonances (D∗0 and D′1) as the405
```
intermediate resonances. It is important to note that D∗0 and D′1 are only known406
to decay to Dπ and D∗π respectively. Some of the decays used for the gap modes407
could be physically allowed [19] but they have never been observed. Throughout408
```
this analysis, the gap modes are treated as regular B → D∗∗ℓν decays (which is409
```
```
mostly relevant for the form factor reweighting c.f Section 6 3 2). The generic MC410
```
```
additionally contains some B → D(∗)πℓν events. These are removed as their measured411
```
branching fractions are saturated by production via the D∗∗ resonances. In Ref. [20]412
an unphysical enhancement at w = 1 was observed in the broad D∗∗ decays, caused by413
events generated several widths away from the nominal mass. We adopt the procedure414
```
of Ref. [20] and add a generator level selection, requiring events to be, at most 3 (2.5)415
```
```
widths above the nominal D0 (D′1) mass. The weight of the remaining events is416
```
increased to compensate for the removed events. The unphysical feature, and the post417
selection spectrum for an example channel can be seen in Fig. 4.418
14
Decay mode [×10−2] Model Dec File Code N Events [×106]
B− → Dℓν 2.27 ± 0.06 BLPRXP Generic -
B− → D∗ℓν 5.27 ± 0.12 BLPRXP Generic -
B− → D1ℓν 0.64 ± 0.10 BLR Generic -
B− → D∗0ℓν 0.13 ± 0.19 BLR Generic -
B− → D′1ℓν 0.28 ± 0.04 BLR Generic -
B− → D∗2ℓν 0.32 ± 0.03 BLR Generic -
B− → DsKℓν 0.030 ± 0.013 PHSP Generic -
B− → D∗s Kℓν 0.029 ± 0.019 PHSP Generic -
```
B− → D∗0(→ Dη)ℓν 0.90 ± 0.90 BLR 1296708001 10
```
```
B− → D′1(→ D∗η)ℓν 0.90 ± 0.90 BLR 1296708000 10
```
```
B− → D′1(→ Dππ)ℓν 0.5 × (0.07 ± 0.09) BLR 1296700001 10
```
```
B− → D∗0(→ Dππ)ℓν 0.5 × (0.07 ± 0.09) BLR 1296700003 10
```
```
B− → D′1(→ D∗ππ)ℓν 0.5 × (0.22 ± 0.10) BLR 1296700002 10
```
```
B− → D∗0(→ D∗ππ)ℓν 0.5 × (0.22 ± 0.10) BLR 1296700004 10
```
B0 → Dℓν 2.11 ± 0.06 BLPRXP Generic -
B0 → D∗ℓν 4.90 ± 0.11 BLPRXP Generic -
B0 → D1ℓν 0.59 ± 0.10 BLR Generic -
B0 → D∗0ℓν 0.12 ± 0.18 BLR Generic -
B0 → D′1ℓν 0.26 ± 0.04 BLR Generic -
B0 → D∗2ℓν 0.30 ± 0.03 BLR Generic -
```
B− → D∗0(→ Dη)ℓν 0.86 ± 0.86 BLR 1196708001 10
```
```
B0 → D′1(→ D∗η)ℓν 0.86 ± 0.86 BLR 1196708000 10
```
```
B0 → D′1(→ Dππ)ℓν 0.5 × (0.07 ± 0.08) BLR 1196700001 10
```
```
B0 → D∗0(→ Dππ)ℓν 0.5 × (0.07 ± 0.08) BLR 1196700003 10
```
```
B0 → D′1(→ D∗ππ)ℓν 0.5 × (0.20 ± 0.10) BLR 1196700002 10
```
```
B0 → D∗0(→ D∗ππ)ℓν 0.5 × (0.20 ± 0.10) BLR 1196700004 10
```
TABLE II: Assumed branching fractions, models, number of generated events and decay
```
files for the channels. The gap channels to D(∗)ππ are taken to be fully correlated across
```
both intermediate D∗∗ resonances.
5. Continuum419
We use the generic continuum samples: 1 ab−1 of generic on-resonance events and 50 fb−1420
of off-resonance. e+e− → q ¯q processes are simulated using KKMC [21]. As the modelling of421
continuum is known to be poor, we perform a data-driven reweighting using the off-resonance422
sample. This is described in section 4.423
15
2.0 2.5 3.0 3.5 4.0 4.5 5.0MX [GeV]0.0
0.5
1.0
1.5
2.0
2.5
```
B± D*00 ( D )
```
Central value3 width cut
1.0 1.1 1.2 1.3 1.4 1.5w0
1
2
3
4
```
B± D*00 ( D )
```
Before cutAfter cut
2.0 2.5 3.0 3.5 4.0 4.5 5.0MX [GeV]0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
```
B± D′01 ( D )
```
Central value2.5 width cut
1.0 1.1 1.2 1.3 1.4w0
1
2
3
4
5
```
B± D′01 ( D )
```
Before cutAfter cut
FIG. 4: Two examples of the broad D∗∗ mass cuts. On the left-hand side the generator
level mass distributions are shown together with the corresponding mass nominal values as
well as the maximum allowed mass. On the right-hand side, the generator level w
distributions are shown before and after the cut and rescaling are applied. The unphysical
spike at w ≈ 1 is removed thanks to the mass cut.
6. Other424
For completeness we list here the remaining event categories, which originate primarily from425
the generic MC. These are:426
a. Secondaries Events in which we have selected a lepton which is not a primary child of427
the B-meson. This includes leptons originating from semileptonic decays of D mesons, and428
leptons originating from leptonic decays of taus. In the case of the tau channels, the leptons429
are expected to be low momentum and thus lie outside the region of interest. Semileptonic430
decays of the D are further discussed in section 2 3.431
b. Fakes Events in which we have misidentified a hadron as the signal lepton. These432
events are taken from the generic MC.433
3. Charm Decay Modelling434
Inclusive studies at Belle and Belle II have reported poor data to MC agreement in quantities435
```
related to the hadronic system (mX , m2miss, q2, . . . ) [20, 22–25]. We therefore reweight the436
```
decay of the charm mesons to the most up to date values, and more importantly, attempt to437
capture the uncertainty of these branching fractions. The full list of decays and the assumed438
branching fractions are attached to this note on the document server.439
440
As we cannot re-generate all events, we reweight the signal side charm decays within441
the existing MC, expanding on the procedure of Ref. [26]. This is achieved by finding the442
16
matching MC particle to the selected lepton candidate, searching up the decay tree until443
```
finding a B meson, then recursively searching down the decay tree for up to four D(∗) mesons444
```
and storing their decays. In this way we additionally aim to minimise any impact on the445
tag side as the corrections to the FEI efficiency were calculated without this update of the446
charm decay modelling.447
448
```
The branching fractions are updated to the latest PDG2023 versions (for some decays449
```
we must refer back to 2008 PDG as subsequent versions no longer list all sub-modes of450
```
D0 → Kπππ ). There are several caveats to the reweighting procedure that should be451
```
```
noted:452
```
• We can only include channels that were listed in the decay file with a non-zero branch-453
```
ing fraction. This means there are channels (although usually they are very rare454
```
```
channels) in the PDG which are not reproduced in the decay file.455
```
• When a decay has been measured through a decay channel of an intermediate resonance456
```
(ex. D0 → K−a+1 (a+1 → ρ0π+)), then the branching fraction is corrected assuming457
```
```
the branching fraction of the intermediate resonance used in the decay file ((a+1 →458
```
```
ρ0π+) = 0.30875). No uncertainty is associated to this branching fraction.459
```
• If a channel has been measured through multiple intermediate resonances, we try to460
infer which was previously used in the decay file and use the same.461
• If only a limit is available, the branching fraction is set to the limit with 100% uncer-462
tainty.463
• Uncertainties are taken to be fully uncorrelated. This can lead to significantly in-464
flated uncertainties when a poorly known resonance contribution is subtracted from465
an inclusive rate.466
• The reweighting procedure only considers the branching fraction. It is not feasible467
to reweight the decay models, as either no better model exists, or a large amount of468
additional information would need to be stored per event. A significant portion of469
events is modelled via PHSP and thus likely to still be poorly modelled even with470
corrected branching fractions.471
• The D0 → K−a+1 , as measured through a1 → ρ0π+, rate has increased several per-472
centage points from 7.8% to 14%. Combined with all other measured channels at their473
respective central values, and zeroing out the unmeasured D0 → KS/Lπ+π−π0π0π0,474
the total D0 branching fraction is ∼ 102%. As the branching fractions of the a1 are475
not well known, we decrease the D0 → K−a+1 branching fraction to 11.94 ± 2.3%, such476
that the total D0 branching fraction correctly sums to unity. The difference to the477
nominal branching fraction is added as an additional uncertainty on this channel.478
• For the D+ we face the opposite problem, with the measured branching fractions cov-479
ering approximately 98% of the total decay rate. We therefore increase the branching480
```
fraction of the unmeasured channels (D+ → η5π) by a factor of ∼ 2.5 over what is481
```
currently in the decay file. The branching fractions of these channels are given a 100%482
uncertainty. This gives these channels branching fractions a factor of ∼ 2 larger than483
the equivalent η4π or η3π channels, which appears somewhat unphysical. For lack of484
17
other channels with which to fill the gap we nevertheless adopt these large branching485
fractions.486
Table III presents a summary of the final state particles produced in comparison with the487
inclusive measurements available in the PDG [18], and the official decay table. The table488
is created by recursively expanding all unstable intermediate states, as outlined above no489
uncertainty is associated to the branching fractions of the intermediate resonances. Neutral490
pions are considered stable, if they are allowed to decay, the electron rate increases by491
approximately 1 percentage point.492
493
Curiously, the updated decay file has largely shifted the inclusive particle production rates494
further from the measured values than the decay file used for MC15 production. The inclu-495
sive neutral kaon production rate in the D0 channel is especially concerning, at a ∼ 2.3σ496
deviation between the PDG value and the updated decay file. As the updated values are497
the most up-to-date branching fractions available, we nevertheless adopt them.498
D0 [%] D+ [%]
Final State PDG Dec File Updated Dec File PDG Dec File Updated Dec File
K0S X - 20.44 18.48 ± 1.46 - 30.39 32.01 ± 0.78
K0LX - 20.12 18.50 ± 1.46 - 30.32 31.95 ± 0.78
```
(K0S or K0L)X 47.00 ± 4.00 40.07 36.46 ± 2.45 61.00 ± 5.00 59.70 63.32 ± 1.27
```
K+X 3.40 ± 0.40 3.36 3.24 ± 0.27 5.90 ± 0.80 5.60 4.40 ± 0.15
K−X 54.70 ± 2.80 55.85 59.84 ± 4.33 25.70 ± 1.40 27.66 27.57 ± 1.20
```
(K+ or K−)X - 56.47 60.45 ± 4.33 - 31.41 30.23 ± 1.20
```
µ+X 6.80 ± 0.60 6.27 6.96 ± 1.34 17.60 ± 3.20 16.26 15.27 ± 0.25
e+X 6.49 ± 0.11 6.54 7.20 ± 1.32 16.07 ± 0.30 16.17 16.11 ± 0.82
TABLE III: Comparison of the inclusive particle production, as listed in the PDG, the
MC15 generic dec file, and the updated branching fractions used within this study.
18
3. EVENT SELECTION AND RECONSTRUCTION499
We use the hadronic FEI to reconstruct a tag B meson, which is paired with a lepton500
candidate from the remaining tracks. All remaining tracks and clusters are inclusively501
```
summed to form the rest of event (ROE). The ROE is used to represent the hadronic502
```
system, X.503
1. Tag Side504
```
The tag candidate is reconstructed by the FEI in one of 32 (36) charged (neutral) hadronic505
```
B channels. As we use the official FEI calibration channels, we adopt the common tag side506
selection as defined within the FEI calibration studies. The selections are:507
• A beam energy difference, ∆E = E∗B − E∗beam, of −0.15 < ∆E < 0.10 GeV.508
• A beam constrained mass, mbc =
p
E∗beam − p∗2B , of mbc > 5.24 GeV. This loose509
selection provides a useful sideband to the calibration studies. After the selection of510
the best candidate on the tag side, we tighten this to mbc > 5.27 GeV.511
• An FEI signal probability, PFEI > 0.01.512
• A selection on the continuum suppression variable cos θcMTB TO , the cosine of the angle513
between the thrust of the tag B meson and the rest of event, of cos θTB TO < 0.9, to514
reduce the continuum contamination at a cost of approximately 10% of the signal. The515
details of the rest of event selections used to calculate cos θcMTB TO are given in section516
3 1 1.517
After these selections, we perform a tag-side best candidate selection, selecting the recon-518
structed B meson with the highest PFEI. We then tighten the mbc requirement to 5.27 GeV.519
For off-resonance events we apply the selection to a scaled beam-constrained mass to account520
for the energy difference between on-resonance and off-resonance events,521
mcorr.bc =
s
10.582
4
−

10.58
10.52
2
```
p∗2Btag , (2)
```
where p∗Btag is the centre-of-mass frame four momentum of the tag B candidate.522
1. Continuum Suppression Masks523
To calculate cos θcMTB TO , we must define which particles in the rest of event are considered524
‘good’, and enter the event-shape calculations. We adopt the official selection used in cal-525
ibrating the FEI. These selections are only used for the definition of cos θTB TO within this526
selection and are marked by the superscript cM. The selections are:527
• Tracks:528
– originate close to the interaction point with dr < 2 cm and |dz| < 4 cm.529
19
– Have a minimum transverse momentum of pt > 0.2 GeV.530
– Have momentum within the CDC acceptance passing thetaInCDCAcceptance.531
• Clusters:532
– Have a minimum energy of 80, 30, or 60 MeV respectively in the forward, barrel,533
and backwards regions of the ECL.534
– Clusters from the edge of the ECL are rejected, requiring 0.2967 < θcl <535
2.6180 rad.536
– Clusters must be recorded within 200 ns either side of t0, consistent with origi-537
nating from photons created in the event.538
For the remainder of this note, all event shape variables are calculated using the nominal539
rest of event selection defined in Sec. 3 2 1.540
2. Signal Side541
Our signal consists of a lepton, an invisible neutrino and finally the ROE which is used as542
the inclusive hadronic system X. Even though we cannot detect the neutrino, we can use543
the known initial state energy to calculate the missing energy carried by the neutrino.544
1. Rest Of Event545
The ROE is used to get kinematic information about the hadronic system without explic-546
```
itly reconstructing it. Various sets of selections (called masks) can be used for the ROE547
```
reconstruction. We use a mask without any cuts as well as a mask based on the selections548
described in Ref. [22] for reference. The nominal selections were optimised they are listed549
below. The optimisation is discussed and illustrated in Appendix A in Ref. [2].550
• Tracks:551
– Originate close to the interaction point with dr < 1 cm and |dz| < 3 cm.552
– Have momentum within the CDC acceptance, passing thetaInCDCAcceptance553
```
(17◦ < θ < 150◦), and must have been seen in the CDC: nCDCHits ≥ 2.554
```
– Polar angle: 0.31 < θ < 2.61.555
– Pass the MVA based duplicate curl track rejection: isCurl==0.556
• Clusters:557
– Have a minimum energy of 70, 60, or 70 MeV in the forward, barrel, and backward558
regions of the ECL respectively.559
– Clusters must be recorded within 70 ns of t0, consistent with photons created in560
```
the event: abs(clusterTiming) < 70.561
```
– Fake photons are suppressed using an MVA based classifier: fakePhotonSuppression >562
0.5.563
20
```
Events with lepton candidates in the ROE (based on the criteria defined below for leptons)564
```
are rejected as they are indicative of B → Xcℓν events and they have a worse resolution565
than events without ROE leptons.566
2. Slow π567
The slow charged and neutral π are treated carefully as they are used to reject B → D∗ℓν568
```
events in the MVA classifier (cf. Section 5). D∗ mesons mostly decay to a D and a π:569
```
```
approximately two-thirds of the D∗± decay to D0π± and the remaining third to D±π0;570
```
D∗0 likewise decay to D0π0 at a rate of about two-thirds, with the remainder being D0γ571
```
(D∗0 → D±π∓ is not possible as the sum of the D± and π± masses exceeds the D∗0 mass).572
```
The D∗ and D masses are very close and therefore the π produced has a very low momentum.573
These π are called slow π and their properties can be used to reject B → D∗ℓν events. The574
corrections and uncertainties associated to slow π are explained in Section 6 1. Slow π have a575
momentum between 50 and 200 MeV. The efficiency of these π is calibrated in independent576
```
studies (Ref. [27] and [28] for π± and π0 respectively). For the quoted calibration factors577
```
to be used in our data sets, the exact corresponding selections need to be applied to π.578
```
Slow charged π are identified as tracks with momentum in the [50; 200] MeV range. The579
```
selections for π0 are summarised in Tab. IV. They are reconstructed from a pair of photons3.580
Selections on MC Additional selections on data
eff40 list
γ |clusterTiming| < 200 ns apply correctEnergyBias
fakePhotonSuppression > 0.1
π0 |dM| < 0.015 GeV
mass constrained kFit
TABLE IV: Selections applied on π0. The selections of the eff40 list can be found in
Ref. [29]
3. High-momentum π±581
An uncertainty must be associated to the hadronisation of the Xu system by PYTHIA8. For582
```
that purpose, the π± multiplicity is used (see Section 6 14 for a precise description of the583
```
```
procedure applied to extract the uncertainty). We only consider π± candidates covered584
```
by the π± identification and K± to π± fake rate correction tables. The correction factors585
are given in bins of lab-frame momentum p and polar angle θ. The momentum is taken586
between 0.3 < p < 4.5 GeV and the polar angle is taken between 0.3 < θ < 2.6 rad. To587
specifically identify π±, a pionID > 0.6 cut is applied. Both for π± and K±, the neural588
network identification scores were considered but it was noticed that the fraction of fake589
```
hadrons is in general higher than for the likelihood-based scores (see Appendix H).590
```
3 The branching fraction π0 → γγ is known to be about 99%.
21
4. Kaons591
D mesons decay very often to a final state containing a kaon. As D mesons are always part592
of the decay chain of D∗∗ and D∗ mesons, the presence of kaons in an event can be used593
to tag this event as a B decay to a charm meson. In particular, charged and neutral kaon594
```
multiplicities are used in our B → Xcℓν MVA classifier (c.f. Section 5).595
```
596
Charged kaons K± are simply reconstructed as charged tracks with a kaon identifica-597
tion probability kaonID required to be greater than 0.6. Similarly to high-momentum π±,598
only K± covered by the correction tables are considered.599
600
The K0S are reconstructed from two oppositely charged tracks on which a pion mass hypoth-601
esis is applied. As the K0S is long lived we do not require the tracks to pass the selection de-602
scribed in Section 3 2 1. The K0S candidate is required to have an invariant mass between 0.47603
and 0.53 GeV, and have a momentum vector consistent with the vector between the interac-604
tion point and its vertex, requiring cosAngleBetweenMomentumAndVertexVector > 0.998.605
5. Signal Lepton606
The signal lepton can either be an electron or a muon. Tracks are required to have a high607
likelihood of being an electron or a muon. To identify electrons, the track is required to have608
an identification BDT score pidChargedBDTScore > 0.9 [30]. To identify muons, the track609
is required to have a likelihood identification score muonID noSVD > 0.9. Other track quality610
```
cuts are applied to the signal leptons: thetaInCDCAcceptance (17◦ < θ < 150◦), nCDCHits611
```
> 0, dr < 1, and |dz| < 2. Furthermore, tracks with a lab frame momentum lower than 0.3612
GeV are rejected. These selections are summarised in Tab. V. The signal electron also need613
to be corrected for Bremsstrahlung with the correctBremsBelle module and an additional614
cut of protonID < 0.99 is applied on electrons in order to reject protons.615
Lepton e± µ±
Identification pidChargedBDTScore > 0.9 muonID noSVD > 0.9
|∆r| < 1 cm
|∆z| < 3 cm
```
Selections thetaInCDCAcceptance (17◦ < θ < 150◦)
```
nCDCHits > 0 a
plab > 0.3 GeV
a According to the following page: https://confluence.desy.de/pages/viewpage.action?pageId=349455022,
nCDCHits > 20 is not used for lepton ID. However, it is recommended to use it for hadrons.
TABLE V: Summary of selections applied on tracks to identify signal leptons.
After having been pre-selected, the signal lepton candidates are combined with the selected616
best Btag. If there are multiple lepton candidates, the event is rejected as this is indicative617
of secondary semileptonic decays, identifying the event as B → Xcℓν. The signal lepton618
multiplicity is illustrated in Figure 5. Events with lepton candidates in the ROE are also619
rejected for the same reason. We additionally define a side-band selection, consisting of620
22
```
events in which the lepton candidate is vetoed by the J/ψ or photon conversion vetoes (see621
```
```
below) to study these contributions.622
```
1 2 3 4 5 6Signal lepton candidate multiplicity0
50000
100000
150000
200000
250000
300000
1 2 3 4 5 6Signal lepton candidate multiplicity
10 1
100
101
102
103
104
105
FIG. 5: Signal lepton candidate multiplicity before rejecting events with multiple leptons
```
in linear scale (left) and log scale (right).
```
6. J/ψ and Photon Conversion Vetoes623
In addition to the channels outlined in section 2 2 true leptons may arise from the decay of624
the J/ψ or, in the case of electrons, from photon conversion in the detector materials. In625
both cases, the two-body nature of the decay allows for efficient vetoing of these contribu-626
tions.627
628
We combine the lepton candidate with all oppositely charged tracks in the rest-of-event, and629
```
select the pair with an invariant mass closest to the mass of the J/ψ or 0 GeV (for photon630
```
```
conversion) where the oppositely charged track is assigned the same mass hypothesis as the631
```
signal lepton. For the J/ψ veto we require the oppositely charged track to pass the selection632
outlined in Section 3 2 1, for the photon conversion veto such a selection is not required as we633
expect a significant fraction of conversions to happen at the beam pipe, and applying strict634
dr and |dz| requirements may miss such conversion events. Tracks used with an electron635
hypothesis undergo the same bremsstrahlung recovery procedure as the signal lepton. No636
particle identification selections are made on the second track to remain inclusive. We veto637
any candidate with:638
• me+e− < 0.050 GeV, where the threshold has been selected to capture 95.45% of the639
true photon conversion tracks.640
• 3.043 < me+e− < 3.129 GeV, where the thresholds have been selected to capture641
95.45% of true J/ψ candidates above the nominal J/ψ mass and 68.27% below the642
nominal J/ψ mass. The coverage in the lower mass direction has been reduced due to643
the long and broad tail caused by bremsstrahlung.644
• 3.072 < mµ+µ− < 3.122 GeV, where the upper threshold has been selected to capture645
95.45% of true J/ψ candidates above the nominal J/ψ mass. The mass peak has a646
23
small broad ‘base’ towards the negative direction. To capture only the peak, and not647
this broad base, we symmetrise the upper threshold about the nominal J/ψ mass.648
The distribution of the selected candidates in the dilepton invariant masses is shown in649
Fig. 6.650
2.9 3.0 3.1 3.2 3.3 3.4
m [GeV]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
×102
true J/
```
fake J/ ( from B)
```
```
fake J/ ( not from B)
```
Veto Range
PDG Mass
2.9 3.0 3.1 3.2 3.3 3.4
mee [GeV]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4×10
2
true J/ ee
```
fake J/ ee (e from B)
```
```
fake J/ ee (e not from B)
```
Veto Range
PDG Mass
0.000 0.025 0.050 0.075 0.100 0.125 0.150 0.175 0.200
mee [GeV]
10 1
100
101
102
103true ee
```
fake ee (e not from B)
```
```
fake ee (e from B)
```
Veto Range
```
FIG. 6: J/ψ vetoes (left: muon, right: electron) and photon conversion veto (bottom).
```
3. Other selections651
Cuts on the main variables of interest, pBℓ , MX and q2, are very effective to reject background.652
These cuts are of high importance for theory predictions. A minimal pBℓ cut will always be653
added as it cuts away very large portions of continuum background as well as background654
coming from secondary and fake leptons. The low pBℓ region of phase-space is sparsely655
populated with signal events. This selection is set to pBℓ > 1 GeV for now but lower cuts656
will be explored. Additional cuts on MX and q2 will be also be considered. They will be657
```
mentioned whenever relevant (see Section 8).658
```
24
4. CONTINUUM MODELLING659
Despite ongoing efforts to improve the simulation of the continuum processes, recent studies660
still show significant disagreement between continuum MC and data. Therefore, we per-661
form a data-driven reweighting in two steps, correcting the normalisation and shape of the662
continuum sample.663
664
To improve the normalisation, we compare the number of off-resonance data events in665
```
the training sample (defined below) to the expected number of off-resonance events from the666
```
MC using the training sample defined below. This is done independently for the charged667
and neutral Btag channels, since the rate at which false B mesons are reconstructed by the668
FEI may differ between both channels. We find correction factors of 0.874 and 0.938 for the669
charged and mixed channels.670
671
To improve the shape of the continuum sample, we follow the approach proposed in Ref. [31],672
and used in the recent Belle B → µν search [32]. This approach is detailed in Ref. [33].673
Our primary goal is to improve the modelling of the event-shape variables, as these are674
subsequently used to train a continuum suppression classifier. We therefore train a classifier675
on these variables, and a few selected other variables, to distinguish off-resonance data676
from off-resonance MC. This classifier can then be applied to on-resonance MC, assigning a677
weight of678
```
wCW =
```
PCW
1 − PCW
```
, (3)
```
where PCW is the classifier response, which is larger as the event is more data-like. The679
```
ratio PCW/(1 − PCW) can be interpreted as an estimate of the likelihood ratio LData/LMC,680
```
where LData, LMC are the likelihoods of the continuum event to be from data and simulation681
respectively.682
1. Input Variables683
As input variables, we include the standard event-shape variables.The full set of variables684
```
is:685
```
• Thrust based variables:686
– The magnitude of the thrust of the tag B, |TB |, and rest of event particles |TO|.687
– the cosine of the angle between the two thrust axes, cos θTB TO .688
– the cosine of the angle between the thrust of the tag B and the z-axis, cos θTB z .689
• CLEO Cones [34]:690
– The fraction of total momentum flow in nested cones of 10◦ about the thrust691
```
axes: C1, . . . , C9.692
```
```
• (Kakuno-Super-)Fox-Wolfram (KSFW) moments [35, 36]:693
```
– The normalised ratio of the second to zeroeth Fox-Wolfram moment R2.694
25
– The KSFW moments: Hso00, Hso01, Hso02, Hso03, Hso04, Hso10, Hso12, Hso14, Hso20, Hso22, Hso24,695
Hoo0 , Hoo1 , Hoo2 , Hoo3 , Hoo4 .696
– The missing mass squared, m2miss,CS and transverse energy, Et,CS.697
1. Classifier Training698
We reconstruct 59687 data and 89142 MC events in the off-resonance sample. These are699
split into three categories:700
```
• training (40%), used directly to train the sample and derive the normalisation correc-701
```
tion.702
```
• validation (10%), to prevent the growth of unnecessarily complex models by termi-703
```
nating training when performance on this sample, independent of the training sample,704
plateaus for 20 training iterations.705
```
• testing (50%), used to check classifier performance. As this sample is not used in706
```
training the classifier, it remains statistically independent and can be used later to707
further constrain the continuum.708
```
As this is a simple classification task, we use a boosted decision tree (BDT) as the classi-709
```
fier, via the xgboost package. Hyperparameters optimisation is performed via a Bayesian710
optimisation process as implemented in Ref. [37, 38] running for 500 trials, optimising for711
the best loss on the validation sample. We take a quasi-deep learning approach to this712
optimisation, floating almost all hyperparameters in the process. The complete set of hy-713
perparameters along with a brief description, their allowed ranges, and optimised values are714
given in Tab. VI.715
716
```
We adopt an exponentially decaying learning rate (l) to allow the model to quickly learn to717
```
separate the samples while allowing later estimators to fine-tune the separation. To prevent718
a vanishing learning rate, we enforce a minimum lmin. The learning rate for tree n is thus719
given by720
```
l(n) = max(l0(1 − r)n, lmin), (4)
```
where l0, lmin and the decay rate r are hyper-parameters that are optimised.721
```
Figure 7 provides the loss curve (binary cross-entropy) on the training and validation sam-722
```
ples and the evolution of the loss for each trial of the hyperparameter optimisation. The723
optimisation is able to rapidly find the region of minimum loss, with the majority of itera-724
tions fine-tuning within this region.725
726
```
For the interpretation of the ratio PCW/(1 − PCW) as a ratio of likelihoods to be valid,727
```
the classifier must be well calibrated, with its score728
26
Parameter Value Range Description
```
Max Depth (d) 5 [1, 11] Maximum depth of each decision tree. Note the maxi-
```
mum number of trees permitted to the model is depen-
dent on the depth of each tree. If lossguide is adopted
as the grow policy we instead limit the tree to 2d nodes.
Initial
Learning Rate
```
(l0)
```
0.124 [0.01, 1.0] Initial learning rate of model. See text for more
details.
Minimum
Learning Rate
```
(lmin)
```
0.034 [0.001, 0.1] Minimum learning rate of model. See text for more
details.
Learning Rate
```
Decay (r)
```
0.0026 [10−6, 0.05] Decay of the learning rate. See text for more details.
```
Alpha (α) 0.078 [10−5, 104] Minimum reduction in loss required to further split a
```
node of the tree. Can help to prevent over-fitting.
```
Lambda (λ) 53 [0.05, 1000] L1 regularisation term on the weights. Can help to
```
prevent over-fitting.
```
Gamma (γ) 0.007 [0.001, 2] L2 regularisation term on the weights. Can help to
```
prevent over-fitting.
Subsample 0.895 [0.5, 1.0] Fraction of training events sampled used to train each
tree. Can help to prevent over-fitting.
Column
Subsample
0.559 [0.5, 1.0] Fraction of variables sampled used in training each
tree. Can help to prevent over-fitting by forcing the
model to rely on a broader range of variables.
Minimum Child
Weight
5 - Minimum number of training events required in each
node after splitting a sample. Can prevent over-fitting
by preventing extremely targeted selections.
Grow Policy depthwise [depthwise,
lossguide]
Whether new nodes are added to a tree in order of
closest to the root node or in order of maximum re-
duction in loss. If lossguide is selected rather than
limiting the maximum depth of the tree we limit the
maximum number of nodes of each tree.
Tree Method gpu hist - The method used by XGBoost to train the trees.
The hist methods pre-bin continuous features into his-
tograms and base their node splitting on the bin in-
dices of the histograms. This strategy is also employed
by FastBDT [39].
nBins 512 - Number of bins used to bin continuous features.
TABLE VI: Hyperparameters of the XGBoost model. For parameters tuned by Bayesian
optimisation, the range investigated by the optimiser is provided in the “Range” column.
All parameters not listed are left at their default value as per version 1.7.6 of XGBoost.
27
0 20 40 60 80
N Trees
0.60
0.62
0.64
0.66
0.68
0.70
Loss
Belle II Simulation dt = 42.56 0.007 1
TrainingValidation
0 1 2 3 4 5
Trial ×102
10 2
10 1
Offset Validation Loss
Belle II Simulation dt = 42.56 0.007 1
FIG. 7: Left: Validation and training loss for the selected classifier. The early stopping
terminates the model growth after 182 trees. Right: Final validation loss of the individual
trials of the hyper-parameter optimisation. The selected classifier is shown as a pink cross.
To better show the variations near the minimum loss, all validation losses have been offset
such that the minimum is at 0.01.
2. Variable Importance729
We estimate the importance of each variable to the classifier via their Shapley values [40],730
which provide the average marginal contribution of a feature to the output, as implemented731
in the SHAP package of Refs. [41, 42]. In this context, a higher importance indicates a larger732
disagreement between the data and MC in these variables. The importances, as measured733
on the validation sample, are presented in Fig. 8.734
0.0 2.5 5.0 7.5
cos Bz
| B|
| O|
cos B O
R2
1
2
3
Belle II Simulationdt = 42.56 0.007 1
0.0 2.5 5.0 7.5
4
5
6
7
8
9
m2miss, CS
Et, CS
0.0 2.5 5.0 7.5
so00
so01
so02
so03
so04
so10
so12
so14
0.0 2.5 5.0 7.5
so20
so22
so24
oo0
oo1
oo2
oo3
oo4
0.0 0.2 0.4 0.6 0.8 1.0
mean |Shap Value| [10 2]
0.0
0.2
0.4
0.6
0.8
1.0
FIG. 8: Variable importance for the data-driven continuum reweighting.
28
3. Uncertainty735
Two sources of systematic uncertainty are assigned to the reweighting procedure. Firstly,736
the full size of the normalisation shift is taken as an uncertainty. Secondly, we propagate the737
statistical uncertainty of the training sample by repeating the training 200 times, varying738
the weight of each event by drawing from a Poisson distribution of mean 1.739
4. Results740
Figure 9 shows the output of the nominal classifier. Figure 10 gives an example of the741
pre-reweighting and post-reweighting distributions in R2. Figure 11 shows a data-MC com-742
parison of the three main kinematic variables in the off-resonance sample. For a comparison743
of all the input variables before and after the reweighting see Appendix L.744
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
CW
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.02)
```
×102
ddss
uucc
MC Uncert.Data
FIG. 9: Distribution of the nominal classifier response for the classifier trained to
distinguish data from Monte Carlo. All MC uncertainties except the continuum
reweighting ones are shown here.
29
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
R2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.016)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
R2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.016)
```
×102
ddss
uucc
MC Uncert.Data
FIG. 10: Distribution of R2 before and after the data-driven reweighting. All MC
uncertainties except the continuum reweighting ones are shown on the left. On the right
these are also included.
0 2 4 6 8 10 12 14q2 [GeV2]0.75
1.00
1.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb 1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.5 GeV
```
```
2)
```
×103dd
ssuu
ccMC Uncert.
Data
pB > 1 GeV
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7pB [GeV]0.75
1.00
1.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.05 GeV)
```
×103dd
ssuu
ccMC Uncert.
Data
pB > 1 GeV
0.00 0.75 1.50 2.25 3.00 3.75 4.50MX [GeV]0.75
1.00
1.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.5 GeV)
```
×103dd
ssuu
ccMC Uncert.
Data
pB > 1 GeV
FIG. 11: Distribution of q2, pBℓ and MX after the data-driven reweighting. All MC
uncertainties including the continuum reweighting ones are shown here.
30
0.0 0.5 1.0 1.5 2.0 2.5Continuum shape calibration weights0
200
400
600
800
1000
1200
1400
1600
Off-resonance MC
FIG. 12: Distribution of continuum calibration weights in the nominal preselected sample.
31
5. MULTIVARIATE SELECTION745
```
After an initial preselection, two Multivariate (MVA) classifiers are applied to the data in746
```
order to further distinguish between signal and background events. Signal corresponds to747
B → Xuℓν events. The first classifier trains against continuum events and the second one748
```
against B → Xcℓν events. In both cases, a neural network (NN) from the tensorflow749
```
package is trained. The hyperparameters are optimised using the optuna package. For750
both classifiers, 5% of the MC Xuℓν signal and 20% of the respective MC background were751
randomly selected to form a training sample. The rest forms the test sample. Both the752
training sample and test sample are rescaled to match the initial total weight of the MC753
sample.754
1. Classifiers and training755
1. Continuum suppression756
The variables used to reject continuum are listed in Section 4 1. The corresponding distri-757
butions are shown in Appendix B. Based on the observed data-MC agreement the following758
14 variables are chosen:759
• C2760
• cos θTB TO761
• cos θTB z762
• Hoo1763
• Hoo3764
• Hoo4765
• Hso01766
• Hso02767
• Hso03768
• Hso04769
• Hso12770
• Hso14771
• Hso20772
• N CStr773
32
Parameter Value Range Description
N Layers 2 [2, 4] Number of layers in the feed forward network.
```
Layer Size [256, 128] {8, 16, 32,
```
```
64, 128, 256}
```
Number of neurons in each layer of the network. The
number is independently selected for each layer and is
restricted to a power of two.
Activation
Function
Swish - We use the swish [43] activation function of the form
```
f (x) = x1+exp(−x) . Tests with ReLU showed similar
```
performance, indicating the network is largely agnostic
to the specific activation function.
Optimiser AdamW - We adopt the AdamW [44] optimiser which computes
adaptive learning rates for each parameter and has
demonstrated rapid convergence in few epochs. Tests
using the SGD optimiser converged on similar models.
Learning Rate 9.3 · 10−3 [10−5, 10−2] Learning rate of the model. Governs the rate at of
gradient descent.
Weight Decay 9.6 · 10−4 [10−8, 10−3] Strength of the weight decay regularisation. Helps to
avoid over-fitting by penalising overly complex models.
Dropout Rate 0.25 We add a dropout layer after each dense layer. This
parameter governs the rate at which the dropout lay-
ers randomly drop a fraction of input connections.
The remaining connections are re-scaled to compen-
sate. Dropout is used to reduce overtraining of the
classifier so its value is fixed.
Label
Smoothing
8.8 · 10−5 [10−5, 0.05] Slightly smooths the labels by changing them from
binary, 1 or 0 for signal and background, to 1 − s and
s. This helps to prevent over-fitting, and prevents
issues with many events being assigned to exactly 1 or
0 due to floating point precision.
```
Batch Size 4096 {1024,
```
```
2048, 4096}
```
Size of a minibatch for each epoch of training. The
batches are large to allow for accurate calculation of
the DisCo loss term for each batch.
TABLE VII: Hyperparameters of the continuum suppression neural network. All
hyperparameters not mentioned are left at their default values as of tensorflow v2.17.0.
The optimal cut on this classifier is chosen according to the maximal significance defined as:774
S/
√
S + B, where S is the number of B → Xuℓν events and B the number of continuum775
events that pass the selection. The values of the hyperparameters for the optimal classifier776
are shown in Tab. VII.777
778
The performance of the continuum suppression classifier is illustrated in Figures 13, 14 and779
15. We evaluate overtraining from the corresponding Receiver Operating Characteristic780
```
(ROC) curve as shown in Fig. 16.781
```
33
0.0 0.2 0.4 0.6 0.8 1.0CS0
2
4
6
8
10
12
14 BackgroundSignal
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
CS
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.01)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
FIG. 13: The continuum suppression score. On the left the score is shown as signal vs
background. After optimisation, the cut score is equal to 0.80. The plot on the right shows
the good data-MC agreement of the score.
0.0 0.2 0.4 0.6 0.8 1.0Continuum suppression score0
100
200
300
400
500
600
700
800
Off-resonance
MCData
FIG. 14: The continuum suppression score of the MC and data off-resonance samples.
2. B → Xcℓν background782
The variables used in the second MVA classifier trained against B → Xcℓν events are listed783
in Tab. VIII. This classifier is trained and applied after adding the continuum suppression784
selection discussed above. In addition, a kaon veto is applied as K are characteristic of785
charm meson decays. The cut on K multiplicities is discussed in Section 7.786
787
The MVA cut minimising the value of the partial B → Xuℓν branching fraction total un-788
certainty in an Asimov fit is chosen as the optimal MVA cut. The extraction of the partial789
branching fraction and its associated uncertainty is discussed in later Sections. The optimal790
MVA cut is obtained from a nominal fit. We illustrate this classifier’s performance using a791
cut obtained from a fit to q2 in a region of phase-space where pBℓ > 1.0 GeV. The optimal792
34
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
```
FIG. 15: Distribution of q2 before (left) and after (right) applying the optimal continuum
```
suppression selection.
0.0 0.2 0.4 0.6 0.8 1.0
True positive rate
0.0
0.2
0.4
0.6
0.8
1.0
False positive rate
CS ROC
Test
Train
FIG. 16: Receiver Operating Characteristic curve for the continuum suppression MVA
classifier.
35
0 5 10 15
cos B O
cos Bz
2
so01
so02
0 5 10 15
so03
so04
so12
so14
so20
0 5 10 15
oo1
oo3
oo4
NCStr
0.0 0.2 0.4 0.6 0.8 1.0
mean |Shap Value| [10 2]
0.0
0.2
0.4
0.6
0.8
1.0
```
FIG. 17: Input feature importances (quantified using the shap values) for the continuum
```
suppression MVA classifier.
Notation Definition
M 2miss Missing mass squared of the semi-leptonic event
```
M 2miss(π±slow) Invariant mass squared of the system recoiling against
```
the reconstructed slow π± coming from a D∗
```
M 2miss(π0slow) Invariant mass squared of the system recoiling against
```
the reconstructed slow π0 coming from a D∗
```
log10(χ2vtx/ndgf ) χ2 of the ROE vertex fit
```
```
cos θc(π±) Cosine of the angle between the D∗ reconstructed from the slow π±
```
and the lepton flight directions in the CMS frame
```
cos θc(π0) Cosine of the angle between the D∗ reconstructed from the slow π0
```
and the lepton flight directions in the CMS frame
```
cos θBY (π±) Cosine of the angle in CMS frame between the B reconstructed
```
from the slow π± and a nominal B particle
```
cos θBY (π0) Cosine of the angle in CMS frame between the B reconstructed
```
from the slow π0 and a nominal B particle
Qtot Total charge of event
TABLE VIII: B → Xcℓν MVA input features
cut is equal to 0.87. The classifier’s performance is shown in Fig. 18 and its score in Fig.793
20. Its ROC curve is shown in Fig. 21 and its loss curve is shown in Fig. 22. We also display794
the importance of each input feature in Fig. 19. The importance is calculated with the shap795
package using the Kernel method. The values of the optimised classifier hyper-parameters796
are shown in Tab. IX.797
798
799
36
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.25 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.1 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.027 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
FIG. 18: pBℓ , q2 and MX distributions after applying both the continuum suppression
```
selection (score > 0.80), the B → Xcℓν suppression selection (score > 0.87) and the K
```
veto.
0.0 2.5 5.0 7.5 10.0 12.5
M2miss
Qtot
```
log10 ( 2vtx/ndgf)
```
0.0 2.5 5.0 7.5 10.0 12.5
```
M2miss( ±slow)
```
```
M2miss( 0slow)
```
```
cos c( ±)
```
0.0 2.5 5.0 7.5 10.0 12.5
```
cos c( 0)
```
```
cos BY( ±)
```
```
cos BY( 0)
```
0.0 0.2 0.4 0.6 0.8 1.0
mean |Shap Value| [10 2]
0.0
0.2
0.4
0.6
0.8
1.0
```
FIG. 19: Input feature importances (quantified using the shap values) for the B → Xcℓν
```
MVA classifier.
37
0.0 0.2 0.4 0.6 0.8 1.0= 0
Xc
0
1
2
3
4
5
6
7
8BackgroundSignal
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000= 0
Xc
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.01)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Asimov Data
pB > 1 GeV,
FIG. 20: The B → Xcℓν suppression score. On the left, the yields of each distribution are
normalised to be visible on the same scale. On the right, the composition of the score is
broken down. The optimal cut is found to 0.87.
0.0 0.2 0.4 0.6 0.8 1.0
True positive rate
0.0
0.2
0.4
0.6
0.8
1.0
False positive rate
= 0X
c ROC
Test
Train
FIG. 21: ROC curve of the optimised B → Xcℓν suppression MVA classifier.
38
0 20 40 60 80 100 120
Epoch
0.42
0.43
0.44
0.45
0.46
0.47
0.48
0.49
0.50
Loss
FIG. 22: Training loss epoch by epoch of the B → Xcℓν suppression MVA classifier. The
training of the neural network is stopped after 128 epochs.
```
The output score of the B → Xcℓν classifier (Fig. 20) exhibits a non-smooth behaviour800
```
which could point to overtraining. This behaviour was investigated and it was concluded801
that the spikes that appear in the score distribution correspond to particularities of the802
input features. To isolate the effects of the input features, the classifier was retrained using803
the nominal hyper-parameter values given in Tab. IX with a subset of the input features.804
The following observations were made:805
• Classifier trained using only the 6 slow pion variables from Tab. VIII: for all events for806
which a slow pion hasn’t been found and reconstructed these variables are not defined.807
For these events, a common value is given to the slow pion variables for all events. The808
value is chosen to be far away from the distribution of the given variable for events809
where it’s defined. The output score for these events is therefore always equal to 0.5810
as the classifier cannot use them. This results in a large spike at 0.5 in the output811
score distribution.812
• Classifier trained using the slow pion variables and M 2miss: a large spike towards large813
```
scores (0.8 - 0.9) is observed. When isolating this spike in the distribution it was814
```
observed that it corresponds to a tight cut of M 2miss around 0. M 2miss being the most815
important variable in the classifier, it is expected that a tight cut around the nominal816
39
Parameter Value Range Description
N Layers 4 [2, 4] Number of layers in the feed forward network.
Layer Size [64, 32,
128, 128]
```
{8, 16, 32,
```
```
64, 128, 256}
```
Number of neurons in each layer of the network. The
number is independently selected for each layer and is
restricted to a power of two.
Activation
Function
Swish - We use the swish [43] activation function of the form
```
f (x) = x1+exp(−x) . Tests with ReLU showed similar
```
performance, indicating the network is largely agnostic
to the specific activation function.
Optimiser AdamW - We adopt the AdamW [44] optimiser which computes
adaptive learning rates for each parameter and has
demonstrated rapid convergence in few epochs. Tests
using the SGD optimiser converged on similar models.
Learning Rate 3.30 · 10−3 [10−5, 10−2] Learning rate of the model. Governs the rate at of
gradient descent.
Weight Decay 1.15 · 10−5 [10−8, 10−3] Strength of the weight decay regularisation. Helps to
avoid over-fitting by penalising overly complex models.
Dropout Rate 0.40 - We add a dropout layer after each dense layer. This
parameter governs the rate at which the dropout lay-
ers randomly drop a fraction of input connections.
The remaining connections are re-scaled to compen-
sate. Dropout is used to reduce overtraining of the
classifier so its value is fixed.
Label
```
Smoothing (s)
```
7.05 · 10−3 [10−5, 0.05] Slightly smooths the labels by changing them from
binary, 1 or 0 for signal and background, to 1 − s and
s. This helps to prevent over-fitting, and prevents
issues with many events being assigned to exactly 1 or
0 due to floating point precision.
```
Batch Size 4096 {1024,
```
```
2048, 4096}
```
Size of a minibatch for each epoch of training. The
batches are large to allow for accurate calculation of
the DisCo loss term for each batch.
L1/L2
Regularisers
0.01, 0.01 - L1 and L2 regularisations are penalty terms to the loss
function. They reduce the complexity of the model
which helps avoiding overtraining.
TABLE IX: Hyperparameters of the B → Xcℓν suppression neural network. All
hyperparameters not mentioned are left at their default values as of tensorflow v2.11.0.
The classifier is trained over 128 epochs.
neutrino mass indeed isolates signal events. This is illustrated in Figure 24.817
• Classifier trained using the slow pion variables and the total event charge: a large818
spike of events appears in the distribution. When isolated it was observed that it819
corresponds to values of Qtot equal to 0.820
The combination of all the above mentioned effects results in the non smooth distribution821
40
observed in Fig. 20.822
2. MVA-induced model dependence823
As the MVA classifiers we use are trained on simulated data, the output score used to select824
events depends on the modelling of the MC. To avoid introducing model dependence various825
```
strategies have been developed for MVA classifiers (adversarial networks [45], DisCo [46]...).826
```
```
The continuum is corrected using off-resonance data (see Section 4) and relies on well-827
```
modelled variables. The model dependence induced by the continuum suppression classifier828
is therefore expected to have a very limited impact. However, as the B → Xcℓν classifier829
relies on the modelling of both B → Xcℓν and B → Xuℓν events, it is preferable to avoid830
any model dependence. To evaluate this effect, we monitor the correlation between the831
classifier output score and each of the three kinematic variables pBℓ , MX and q2. This is832
shown in Fig. 23 where no strong correlations are observed between the three variables and833
the classifier score. As the proportion of signal to background is not uniform in the three834
kinematical variables, it is expected that more events with a higher or lower score will be835
present in particular regions of phase-space. The DisCo algorithm was implemented and836
tested in order to limit the correlation between the score and the kinematical variables.837
However, its implementation leads to unexpected behaviour of the classifier and its effect838
appeared to be limited in our case so it was decided to not use it. The superscript λ = 0839
appearing in the score label indicates that the DisCo algorithm was not used during the840
neural network training.841
41
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5MX [GeV]4
3
2
1
0
1
2
3
4
5
```
log(
```
= 0Xc1
```
= 0Xc)
```
0
100
200
300
400
0 5 10 15 20 25 30q2 [GeV2]4
3
2
1
0
1
2
3
4
5
```
log(
```
= 0Xc1
```
= 0Xc)
```
0
100
200
300
400
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]4
3
2
1
0
1
2
3
4
5
```
log(
```
= 0Xc1
```
= 0Xc)
```
0
50
100
150
200
250
FIG. 23: Two-dimensional distributions of the B → Xcℓν MVA score versus the three
kinematical variables pBℓ , MX and q2.
4 2 0 2 4 6 8 10M2
miss [GeV2]
0.0
0.2
0.4
0.6
0.8
1.0
= 0Xc
0
100
200
300
400
500
600
700
4 2 0 2 4 6 8 10M2
miss [GeV2]
0.0
0.2
0.4
0.6
0.8
1.0
= 0Xc
0
50
100
150
200
250
FIG. 24: Two-dimensional distributions of the B → Xcℓν MVA score versus M 2miss for all
```
events (left) and for signal events (right).
```
42
6. CORRECTIONS AND SYSTEMATICS842
1. Slow π efficiency843
We carefully treat slow π coming from B → D∗ℓν events are their properties are used in844
the MVA selection. They can be rejected by the ROE mask but they need to be taken into845
account in the slow π efficiency reweighting. Charged and neutral π are treated separately.846
The selections applied on slow π are given in Section 3.847
848
All π± reconstructed in the ROE and π± reconstructed from a D∗ decay and not caught849
by the ROE mask are assigned a correction factor. Each π± corresponds to a track so850
the correction factor assigned to these pions corresponds to a track correction. The track851
correction defined in Section 6 2 is only applied on tracks with a momentum higher than852
200 MeV. As π0 don’t leave tracks, only the ones used in a D∗ reconstruction and caught853
by the ROE mask are corrected.854
855
The efficiencies are given in three bins of momentum between 50 and 200 MeV. The856
correction factors are summarised in Tab. X and are taken from Ref. [27] and [28] for π±857
and π0 respectively. The efficiency in the 200 - 400 MeV bin is assumed to be 1 and is858
therefore used as a normalisation for the three low momentum bins. For each π of a given859
type in an event and a given bin the corresponding efficiency scale factor is applied to the860
event.861
862
```
High momentum π0 (p > 200 MeV) are also reconstructed using a different channel than863
```
the slow π0. Because of the higher statistics in this momentum region, the extracted cor-864
rection factors are deemed more reliable. Therefore, the correction factor obtained for865
200 MeV < p < 400 MeV is used as an additional normalisation factor for slow π0. This866
number is equal to 0.818 and is directly multiplied to the correction factors.867
π±
```
Bins (GeV) [0.05, 0.12] [0.12, 0.16] [0.16, 0.2]
```
Correction factors 0.996 ± 0.020 ± 0.013 ± 0.003 0.990 ± 0.015 ± 0.013 ± 0.003 0.987 ± 0.017 ± 0.013 ± 0.003
π0
```
Bins (GeV) [0.05, 0.10] [0.10, 0.15] [0.15, 0.2]
```
Correction factors 1.027 ± 0.103 ± 0.054 0.963 ± 0.063 ± 0.024 1.033 ± 0.031 ± 0.033
TABLE X: Slow π efficiency correction factors. An additional factor of 0.818 is applied on
the π0 factors. The uncertainties are respectively the uncorrelated statistical, correlated
```
statistical and systematic uncertainties for π± and (uncorrelated) statistical and
```
systematic for π0. Refer to the main text for details.
Three types of uncertainties are quoted: the uncorrelated and correlated statistical errors868
```
(because of the normalisation to the [200; 400] MeV bin) and the systematical error. The869
```
total covariance matrix is calculated as follows:870
43
```
C =
```


σ2tot, 1 σcorr, 1σcorr, 2 + σsyst, 1σsyst, 2 σcorr, 1σcorr, 3 + σsyst, 1σsyst, 3
σcorr, 2σcorr, 1 + σsyst, 2σsyst, 1 σ2tot, 2 σcorr, 2σcorr, 3 + σsyst, 2σsyst, 3
σcorr, 3σcorr, 1 + σsyst, 3σsyst, 1 σcorr, 3σcorr, 2 + σsyst, 3σsyst, 2 σ2tot, 3

 ,
```
(5)
```
where the diagonal elements are:871
```
σ2tot, i = σ2uncorr, i + σ2corr, i + σ2syst, i. (6)
```
```
If no correlated error is used (as is the case for π0), it can simply be set to 0. The covariance872
```
matrix is then decomposed as:873
```
C = V diag(⃗λ)V −1, (7)
```
```
where V is the matrix of eigenvectors (⃗e i) of C and diag(⃗ λ) the diagonal matrix of eigenvalues874
```
```
(λi). The ±1σ eigendirection variations are computed from the central vector⃗x central as:875
```
⃗x ±i =⃗x central ±
p
```
λi⃗e i, (8)
```
where⃗x ±i are the varied vectors.876
2. Tracking efficiency877
The tracking efficiency uncertainty is applied as a percentage per track. The current cor-878
rection is 0.24%/track. It’s applied on tracks with momentum higher than 200 MeV.879
3. Form factors880
```
Semileptonic resonant B decays are described by form factors (FF). For each decay, different881
```
FF models exist. One specific model for each decay is implemented in the basf2 EvtGen882
framework. The form factor parametrisation used in the decay files must be updated for883
some of the b → u and b → c semi-leptonic decays. We update to a more recent model and/or884
more up-to-date parameter values. In addition, an uncertainty is associated to each form885
factor parameter. Because these parameters are correlated with each other, the systematic886
```
uncertainty associated to each decay is determined as follows (similar method as for the slow887
```
```
π, see Section 6 1):888
```
• Combine the individual errors and the total correlation matrix to obtain a covariance889
matrix890
• Compute the eigenvalues and eigenvectors of this matrix891
• Vary each parameter by ±1σ in the eigendirection892
For n form factor parameters, this gives a set of n up/down variations. For each variation,893
new hybrid weights are calculated and the difference with the nominal distribution is taken894
as a systematic uncertainty.895
44
1. B → Xuℓν form factors896
For the B → Xuℓν decays, the eFFORT [47] package was used for the form factor reweighting.897
898
The form factor models were already discussed in Section 2 2. We give here a short overview899
of the model update for each type of resonant decay.900
• B → πℓν: the BCL model is used but a more up-to-date set of parameter values is901
given in Tab. 57 of Ref. [8]. The truncation of the BCL expansion is different and902
therefore 5 parameters are used instead of 8.903
• B → ρ/ωℓν: the BCL expansion is used but the values are updated to the ones found904
in Ref. [9]. The model has 11 parameters. The B → ωℓν normalised differential decay905
rate as a function of q2 is illustrated in Fig. 25 together with the impact of form factor906
parameter variations.907
• B → η/η′ℓν: in the decay files the ISGW2 model is used. It’s considered to be out-908
of-date and therefore the model is updated to the more recent Light Cone Sum Rules909
```
(LCSR) QCD model from Ref. [10]. This change is illustrated in Fig. 26 where the910
```
normalised differential decay rate as a function of the recoil parameter w is plotted.911
ISGW2 does not have any parameter, whereas the new model has two parameters.912
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
q2 [GeV2]
0.00
0.01
0.02
0.03
0.04
0.05
0.06
1/

d
/dq
2
B
Central
Total variation
```
FIG. 25: The central B → ωℓν normalised differential decay rate is illustrated here (black
```
```
line). The red band corresponds to the total impact of the 11 up/down B → ω form factor
```
parameter variations.
45
1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
w
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
1/

d
/dw
B
ISGW2
LCSR
FIG. 26: The central normalised B → ηℓν differential decay rate as a function of w. The
```
decay rate is shown for both the ISGW2 (red) and the more up-to-date LCSR (black)
```
B → η form factor models.
2. B → Xcℓν form factors913
For B → Xcℓν form factors, the HAMMER framework [16] was used.914
• B → Dℓν: the BGL [14] parametrisation is used to model these decays in the decay915
```
file (N = 3 expansion, 8 parameters). However, the theoretical calculation on which916
```
the basf2 implementation is based was criticised by theorists in Ref. [48]. Therefore,917
a new HAMMER class correcting these errors was used. These mistakes have a negligible918
impact on the form factor calculation and they do not invalidate the parameter values919
used for the decay file. Nevertheless, they are fixed for completion4. The B → D920
form factor modelling was updated to the BLPRXP model [15]. This model has the921
advantage to fit both D and D∗ data which makes it more accurate.922
• B → D∗ℓν: in basf2, these decays are modelled using the BGL model with the923
```
(1, 1, 2) expansion. They are are updated to the BLPRXP model. The difference924
```
between the two models as well as the variations associated to the BLPRXP model925
are illustrated in Fig. 27.926
• B → D∗∗ℓν: the name D∗∗ is not a single state but covers all four states D∗0 , D1, D∗1927
and D∗2 . For B → D∗∗ℓν decays, only the BLR model exists. The two broad states928
4 These changes are discussed for example in https://gitlab.desy.de/belle2/software/basf2/-
/merge requests/1631 where a new EvtGen class was created.
46
D∗0 and D∗1 are not described by the same parameters as the narrower D1 and D∗2929
```
(3 parameters for the former, 4 for the latter). The values of these parameters are930
```
updated to the ones found in Tab. 5 in [17].931
1.0 1.1 1.2 1.3 1.4 1.5w0.0
0.5
1.0
1.5
2.0
2.5
Arbitrary units
B D *
Central BGLCentral BLPRXP
Variation BLPRXP
1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00cos L0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Arbitrary units
B D *
Central BGLCentral BLPRXP
Variation BLPRXP
1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00cos V0.0
0.1
0.2
0.3
0.4
0.5
0.6
Arbitrary units
B D *
Central BGLCentral BLPRXP
Variation BLPRXP
0 1 2 3 4 5 60.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
Arbitrary units
B D *
Central BGLCentral BLPRXP
Variation BLPRXP
FIG. 27: The four main variables w, cos θL, cos θV and χ used to describe B → D∗ℓν
decays are shown here for the two form factor models described in the text. For the model
```
that we use in our samples (BLPRXP), the total variation due to the 9 parameters
```
uncertainties is also shown.
4. Charged particle identification932
We correct for charged-particle identification efficiencies using the PIDVar package. This933
includes the following:934
• ℓ± → ℓ± efficiency corrections. Taken from the official v0b tables.935
• π± → ℓ± fake rate corrections. Taken from the official v0b tables.936
• K± → ℓ± fake rate corrections. Taken from the official v0b tables.937
• p± → ℓ± fake rate corrections. Estimated with the systematics framework. Includes938
the protonID veto requirement.939
• K± → K± efficiency corrections. Estimated with the systematics framework.940
• π± → K± fake rate corrections. Estimated with the systematics framework.941
47
The correction tables provide weights binned in track charge, lab frame momentum, and942
polar angle. In each bin a correction weight is applied, ηk = ϵData/ϵMC, where k gives943
the bin index, and ϵData, ϵMC are the measured identification efficiencies in data and MC944
control samples. For each bin the statistical and systematic uncertainties of this ratio are945
also available. Using PIDVar we draw 200 variations of the⃗η values using multivariate946
gaussians, about the nominal values, where the statistical uncertainties are taken to be fully947
```
uncorrelated, and the systematic (within a correction table) to be fully correlated.948
```
949
In a small number of cases, mostly K → ℓ fake rates, the tracks fall outside the cover-950
age of the correction tables. When this occurs, the correction factor is assumed to be 1951
with an uncertainty that combines the average of the total uncertainties in all measured952
bins, and the average difference of the measured correction factors from unity in quadrature.953
954
When used to correct veto efficiencies, as when searching the rest of event for charged955
kaon or lepton candidates, rather than a binary veto of events in MC, we apply correction956
```
weights (wk) as957
```
```
wk = 1 − ηk, (9)
```
such that if the identification in data is less efficient than in MC, the MC events are kept958
with a small weight. If identification in data is more efficient than in MC the MC events959
are assigned a negative weight. This occurs rarely, such that when performing the binned960
fit, all bins have positive yield expectation values.961
5. FEI tagging962
```
For Belle II, a novel algorithm, the Full Event Interpretation [49] (FEI), was developed to963
```
reconstruct exclusive tag-candidates. The algorithm relies on machine learning to identify964
plausible B-meson decay-chains and uses hadronic and semi-leptonic tag-side decays to do965
so. In order to apply the tag-side reconstruction algorithm in a physics measurement it is966
important to quantify and correct for potential mismatches in the tag-side efficiency between967
data and simulation. The calibration factors are taken from Ref. [50]. They are computed968
```
from a combination of the signal-side B → Xℓν and B → D(∗)π channel calibrations. The969
```
correction factors are split by B meson charge. One calibration factor per tag-side channel970
```
is given (the least common channels were in fact grouped and one factor is given for all of971
```
```
them). There are respectively 11 and 12 factors for the neutral B and charged B modes.972
```
Furthermore, different factors were extracted for the two most common FEI probability973
PFEI cuts, 0.01 and 0.001. As mentioned in Section 3 1, we use PFEI > 0.01.974
975
The variations are calculated using the same method as for the slow π and form factor976
```
variations (see Sections 6 1 and 6 3 respectively). The covariance matrix is diagonalised and977
```
the eigenvariations are calculated. As the FEI calibration factors and covariance matrices978
are separated for charged and neutral B mesons, the variations are also separated.979
6. Branching fractions980
The branching fractions for B and D decays have to be updated. For B decays they are981
simply changed to more up-to-date values. The associated uncertainty needs to be taken982
48
into account. For each variation, new hybrid weights are computed and the difference with983
the nominal distribution is taken as an uncertainty. There is therefore one up/down varia-984
tion per branching fraction.985
986
D decays are discussed in details in Section 2 3. For these decays, the branching frac-987
tion is varied according to its associated uncertainty and the difference with the nominal988
distribution is taken as an systematic uncertainty.989
7. Hybrid parameter variations990
The DFN model is chosen as our nominal model for the description of B → Xuℓν events. It991
```
requires two input parameters for their modelling with EvtGen, mb and a (cf. Section 2 2 1).992
```
These parameters are correlated and their uncertainties yield two different sets of up/down993
variations. The hybrid weights are recalculated for each one of these eigenvariations and the994
difference with the nominal distribution is taken as a systematic uncertainty. The parameters995
and their values are given in Tab. XI. Their values in two dimensions are shown in Fig. 28.996
mb a
Central 4.658 1.328
Variation 1 4.698 1.021
Variation 2 4.618 1.659
Variation 3 4.649 1.042
Variation 4 4.667 1.734
TABLE XI: DFN parameters central values and up/down correlated variations
4.62 4.63 4.64 4.65 4.66 4.67 4.68 4.69 4.70m
b [GeV]
1.0
1.1
1.2
1.3
1.4
1.5
1.6
1.7
a [GeV]
FIG. 28: Illustration of the four variations of the DFN parameters on a 2D plane.
8. Inclusive model differences997
Discrepancies are observed between different inclusive models. Therefore, an additional998
uncertainty is associated to the difference between the BLNP and DFN models. The hybrid999
49
weights are recalculated for the nominal DFN model and the difference with the nominal1000
BLNP distribution is taken as a systematic uncertainty.1001
9. K0S efficiency1002
Following the recommendations of the performance group, we assign a weight of 0.55% per1003
cm of flight distance from the interaction point to K0S candidates. The full correction is1004
taken as a systematic uncertainty.1005
10. s¯s fragmentation1006
In Section 2 2, the variation of the PYTHIA parameter controlling the production of s quarks1007
was discussed. The difference between the nominal distribution and those obtained with the1008
varied γS parameter is taken as a systematic uncertainty.1009
11. MC statistics1010
The number of events in Monte Carlo samples being finite, the associated statistical uncer-1011
tainty needs to be taken into account. It is simply calculated as:1012
sX
i
```
w2i , (10)
```
wi being all the weights applied to each event.1013
12. f ±/01014
```
We vary the fraction of Υ (4S) → B+B− / Υ (4S) → B0B0 according to the value obtained1015
```
in [51]: f+−/00 = 51.1 ± 1.1%.1016
13. Continuum calibration1017
The full size of the normalisation corrections discussed in Sec. 4, are assigned as systematic1018
uncertainties. The corrections for the charged and neutral tagged samples are taken to be1019
uncorrelated. Uncertainties on the BDT based shape correction arising from the limited1020
statistics of the off-resonance data and simulated samples are propagated by training 2001021
additional classifiers on bootstrapped samples of the off-resonance data and MC.1022
14. Xu hadronisation modelling1023
The hadronisation modelling of the non-resonant Xuℓν component is performed by PYTHIA8.1024
However, its parameters have yet to be tuned in Belle II and therefore a method must be de-1025
vised to estimate the uncertainty related to the hadronisation modelling. It was attempted1026
50
to extract this uncertainty by changing the values of a limited number of parameters which1027
could impact the Xu modelling in a similar way to the γS uncertainty described above.1028
Modifying the values of this small subset of PYTHIA8 parameters had a very limited effect1029
on tested distributions and therefore it was concluded that a specific large-scale study should1030
be performed. The tuning of PYTHIA8 parameters is currently ongoing in Belle II.1031
1032
The alternative method relies on the π± multiplicity in the ROE and can only be performed1033
with signal region data. π± are selected with a hadron ID cut of 0.6. The nominal fit results1034
are projected onto the π± multiplicity using the method described in Appendix E 4. The1035
non-resonant Xuℓν component is scaled in bins of the generator-level π± multiplicity such1036
that the post-fit π± multiplicity in MC matches exactly the data distribution. The resulting1037
weights are applied on the nominal sample and the nominal fit is repeated. The difference1038
between the two B → Xuℓν branching fraction central values is taken as an additional1039
uncertainty. This procedure will be completed after unblinding of the signal region. We1040
use the EBℓ :q2 CRK,low-CRK,high fit described in Section 8 10 2 to check the pre and postfit1041
agreement of the π± multiplicity in the CRK,high region. If resonant B → Xcℓν decays are1042
properly modelled, then the assumption that the postfit disagreement is due only to the1043
non-resonant B → Xuℓν component holds. The π± multiplicity is shown in Figure 29. The1044
projection method is described in Appendix E 4.1045
0
500
1000
1500
2000
2500
3000
events
SignalRegion
pre-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5bin0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
2500
3000
events
SignalRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5bin0.68
0.84
1.0
1.16
1.32
data / model
FIG. 29: Pre and postfit π± multiplicities in CRK,high1046
1047
15. Uncertainties related to the fitting procedures1048
The signal extraction procedure is detailed in Section 8. Additional uncertainties are as-1049
signed to the measured BR based on the corrections described in Section 9 3.1050
51
7. DATA-MC AGREEMENT1051
In this Section we compare data and MC distributions in different control regions. The pre-1052
selections presented in Section 3 are applied on all samples. We define 5 different control1053
regions where the data can be unblinded safely as the signal is overwhelmed by different1054
sources of background. The signal region is defined by selecting events without K and with1055
an MVA score greater than 0.87. By applying or not and inverting the K and MVA score1056
selections, one can define various control regions. A cut on pBℓ > 1.0 GeV is always applied1057
on all events. As described in Section 8, other selections on kinematical variables are also1058
applied to probe regions with higher signal purity. All the plots and results discussed in this1059
Section are for the nominal case where only the pBℓ cut is applied. The control regions are1060
defined as follows:1061
```
• Control region 1 (CR1): no other selections than the pre-selections defined in Section 31062
```
```
are applied (Fig. 30)1063
```
```
• B → Xℓν control region (CRXℓν ): the continuum suppression classifier is applied1064
```
```
(Fig. 31); in this region, semi-leptonic decays to any hadronic system are enhanced1065
```
```
(X = Xu, Xc)1066
```
```
• Wrong sign lepton region (CRWSLR): charged B events where the tag-side B and the1067
```
```
lepton have the same charge (neutral B-mesons are not considered because of mixing);1068
```
```
the continuum suppression classifier is applied (Fig. 32)1069
```
```
• Kaon, low score region (CRK,low): events are required to have at least one K and a1070
```
```
B → Xcℓν MVA classifier score lower than 0.60; the continuum suppression classifier1071
```
```
is applied (Fig. 33)1072
```
```
• Kaon, high score region (CRK,high): events are required to have at least one K and a1073
```
```
B → Xcℓν MVA classifier score higher than 0.87; the continuum suppression classifier1074
```
```
is applied (Fig. 34)1075
```
```
• No kaon, low score region (CR0,low): events are required to have no K and a B → Xcℓν1076
```
```
MVA classifier score lower than 0.60; the continuum suppression classifier is applied1077
```
```
(Fig. 35)1078
```
In this analysis it is not straightforward to find a control mode to validate the efficiency of1079
the main selections defining the signal region. In fact, the most similar decays to our signal1080
B → Xuℓν decays are the B → Xcℓν decays. We can therefore use a B → Xcℓν-enhanced1081
region to estimate the selection efficiencies of B → Xuℓν decays. It is important to note that1082
this estimate remains fairly qualitative. Charm and charmless semileptonic B decays exhibit1083
important differences in particular in their modelling and kinematics. B → Xuℓν events1084
tend to have softer hadronic systems and harder leptonic systems. Their modelling partly1085
relies on specific models of the non-resonant contribution. We quote below the efficiencies1086
and their associated total uncertainty for three important cuts: the continuum suppression1087
selection on CR1 events, the K veto on CRXℓν events and the Xcℓν suppression MVA cut1088
on CRXℓν events with at least one K. The SR efficiency will be checked in data as part of1089
```
our unblinding procedure (see Section 9). The total signal efficiency in MC as a function of1090
```
the three main kinematical variables in shown in Appendix P.1091
52
• Continuum suppression1092
```
– Data: (48.9 ± 0.1)%1093
```
```
– MC: (47.6 ± 1.0)%1094
```
– Compatible within 1.3σ1095
• K veto1096
– Data: 30.3%1097
– MC: 29.7%1098
– The exact uncertainty which factors in correlations is challenging to derive for1099
technical reasons but the total MC uncertainty is expected to be about 0.5 − 1%1100
and therefore the efficiencies would be compatible within about 1σ1101
• B → Xcℓν suppression MVA1102
```
– Data: (2.95 ± 0.05)%1103
```
```
– MC: (3.23 ± 0.12)%1104
```
– Compatible within 2.2σ1105
The conclusion of this test is fairly qualitative but given the large difference in modelling1106
between Xuℓν and Xcℓν events, this is the best check that can be done. The disagreement1107
between MC and data in this test is corrected using Xcℓν events as detailed later in this1108
Section. Furthermore, the pre-fit uncertainty on Xuℓν events is expected to be larger than1109
that of Xcℓν events because of the important modelling uncertainties that are added for the1110
signal mode. It is therefore expected that any discrepancy in the signal efficiency between1111
MC and data is well covered by the total uncertainty.1112
1. Kinematic distributions1113
In Figures 30 to 35 plots of pBℓ , MX and q2 are shown in the control regions defined above.1114
```
In addition, we show the same distributions in the signal region without data (see Fig. 36).1115
```
In the plots, ’MC Uncert.’ indicates that all sources of uncertainties are considered in1116
the uncertainty bands whereas ’MC Stat. Uncert.’ indicates that only the MC statistical1117
uncertainty is considered.1118
2. Sample compositions1119
For each sample, in Tables XII and XIII, the composition in terms of signal and background1120
components and the B → Xcℓν composition are given respectively.1121
3. Data-MC disagreement1122
A large disagreement is observed in all three variables in the control regions discussed above.1123
The exact origin of this disagreement is not yet known but we give in the next Section an1124
outline of our current understanding of the data-MC disagreement as well as a potential1125
solution to it.1126
53
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
FIG. 30: Data-MC comparison of pBℓ , MX and q2 in control region 1. The uncertainty
band includes only the MC statistical error.
CRK,low CRK,high CR0,low Signal
B → Xuℓν 0.46 ± 0.01% 2.55 ± 0.04% 1.49 ± 0.01% 29.5 ± 0.2%
B → Xcℓν 93.2 ± 0.2% 92.2 ± 0.8% 90.9 ± 0.1% 61.5 ± 0.4%
Secondary leptons 3.19 ± 0.02% 1.60 ± 0.06% 3.30 ± 0.01% 1.70 ± 0.05%
Fake leptons 2.27 ± 0.01% 2.65 ± 0.08% 2.74 ± 0.01% 3.98 ± 0.08%
Continuum 0.88 ± 0.02% 0.99 ± 0.10% 1.56 ± 0.02% 3.30 ± 0.14%
TABLE XII: Composition of various background regions and the signal region. The
statistical error is shown.
54
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
FIG. 31: Data-MC comparison of pBℓ , MX and q2 in the B → Xℓν control region.
CRK,low CRK,high CR0,low Signal
B → Dℓν 17.33 ± 0.05% 40.4 ± 0.4% 19.1 ± 0.04% 37.3 ± 0.4%
B → D∗ℓν 61.21 ± 0.12% 47.3 ± 0.5% 58.7 ± 0.09% 49.2 ± 0.5%
B → D∗∗ℓν 9.66 ± 0.03% 6.15 ± 0.13% 10.0 ± 0.03% 6.85 ± 0.14%
B → D∗∗Gapℓν 11.8 ± 0.10% 6.10 ± 0.40% 12.2 ± 0.07% 6.62 ± 0.35%
TABLE XIII: Composition of the Xcℓν component in various background regions and the
signal region. The statistical error is shown.
1. Origin of the data-MC disagreement1127
Similar data-MC differences were already observed in past inclusive measurements in Belle1128
II, in particular in Ref. [52]. We divide our MC templates in three categories and discuss1129
```
them below: lepton backgrounds (fake and secondary leptons), continuum and B → Xℓν.1130
```
55
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 404.7/30
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.05 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
pB > 1 GeV, Wrong sign lepton region
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 488.7/96
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.05 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
pB > 1 GeV, Wrong sign lepton region
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 425.9/73
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.25 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
pB > 1 GeV, Wrong sign lepton region
FIG. 32: Data-MC comparison of pBℓ , MX and q2 in the wrong sign lepton control region.
1131
The fake and secondary lepton components correspond to a very small portion of the events1132
in the Xℓν control region and are thus not expected to be the main cause of disagreement.1133
However, the lepton background contributions are increased in the wrong sign lepton region1134
region compared to the Xℓν control region. Similar trends as in the Xℓν control region can1135
be seen so the fake and secondary leptons could also contribute to the data-MC disagreement.1136
1137
The continuum is in general known to be poorly modelled. However, as described in1138
Section 4, the continuum is rescaled using off-resonance data. After these corrections, in1139
the off-resonance region, the data-MC agreement is much improved. However, the on- and1140
off-resonance samples present small differences. In particular, as illustrated in Fig. 38,1141
shape differences can be observed in the variables used for the continuum calibration. As1142
the scaling factors are extracted using off-resonance MC and data and then applied to on-1143
resonance samples, some disagreement between MC and data is expected in continuum in1144
the on-resonance region. Nevertheless, the disagreement coming from continuum modelling1145
56
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.05 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.05 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.25 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
FIG. 33: Data-MC comparison of pBℓ , MX and q2 in the CRK,low.
can hardly explain entirely the large data-MC differences observed in the Xℓν control region.1146
1147
1148
Therefore, the data-MC disagreement is expected to be largely explained by the B → Xℓν1149
modelling. From Fig. 31, it can be seen that the B → Xuℓν component contribution1150
is too small in this region but that most events are B → Xcℓν events. As described in1151
Section 2 2, the inclusive B → Xcℓν component is modelled as a sum of exclusive charm1152
meson decays and gap modes. As the latter are not physical but are added to fill the gap1153
between sum of exclusive and total inclusive, they are not expected to perfectly model the1154
non-resonant part of B → Xcℓν. Large uncertainties are associated to this contribution to1155
compensate for its imperfect modelling. Another potential cause for the poor B → Xcℓν1156
modelling are D meson decays. In particular, hadronic decays to four or more particles1157
are modelled using phase-space modelling instead of decay-specific models. As D∗ and D∗∗1158
mesons always eventually decay to a D meson, these decays appear in effectively every1159
B → Xcℓν event and they could spoil the modelling of this component. Another type of1160
57
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.027 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.1 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.25 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
FIG. 34: Data-MC comparison of pBℓ , MX and q2 in the CRK,high.
D decays that are known to be badly modelled are decays to K0L. In Ref. [53], an overall1161
correction factor of 30% for these decays was derived from data. To test how much this1162
component could impact our modelling we use the CR1 and we split it in the following1163
three templates: continuum, B decays with D → K0LX decays and B decays without1164
D → K0LX decays, X representing any generic system. We correct the template with K0L1165
```
by 30% and we observe no improvement in the data-MC comparison (cf. Fig. 39). These1166
```
decays do not represent a large portion of all events and therefore a simple normalisation of1167
this component could hardly cover the gap between data and MC that is currently observed.1168
1169
To conclude this discussion, it is likely that the difference between data and MC can be1170
explained by the cumulative effect of a few mismodelled components rather than a unique1171
template. Nevertheless, it appears that the B → Xcℓν poor modelling is the largest cause1172
of the disagreement. In the next Section, we describe a method to correct this component.1173
58
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.05 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.25 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
FIG. 35: Data-MC comparison of pBℓ , MX and q2 in the CR0,low.
2. Normalisation mismodelling1174
From the various plots shown in this Section, it is clear that the shape of the B → Xcℓν1175
component is not well modelled. However, the total normalisation difference between MC1176
and data is also widely different between different control regions. This can be explained by1177
the Xcℓν MVA score and K multiplicity distributions in Figures 40 and 41. Depending on1178
the selection on these variables the normalisation is expected to shift. The normalisations1179
in the different control regions defined above are summarised in Table XIV.1180
1181
The control regions built based on the K and MVA score cut are illustrated in Figure 42.1182
We therefore need to correct for both effects. When using the pyhf package, fits where both1183
the normalisation and the shape of a component are free-floated at the same time yield1184
very unpredictable and unstable results. We therefore choose to split the normalisation and1185
shape corrections in two parts. The later is corrected in a simultaneous fit of the signal1186
region and a control region as detailed later.1187
59
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.027 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.1 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.25 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Asimov Data
pB > 1 GeV
FIG. 36: pBℓ , MX and q2 in the signal region.
Region Data/MC ratio
B → Xℓν 0.986 ± 0.002
CRK,low 1.039 ± 0.004
CRK,high 0.946 ± 0.018
CR0,low 1.113 ± 0.003
TABLE XIV: B → Xcℓν data-MC ratio for the different control regions described in this
Section for a kinematical selection pBℓ > 1.0 GeV. The uncertainty is statistical.
1188
To derive a normalisation correction for the signal region we use what is commonly re-1189
ferred to as the ABCD method. We split the phase-space into four separate regions based1190
on the K multiplicity and the B → Xcℓν MVA score which are two weakly correlated1191
variables. The signal and control regions were defined above and Figure 42 illustrates them1192
60
5.2450 5.2525 5.2600 5.2675 5.2750 5.2825 5.2900m
bc [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.00051 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Asimov Data
pB > 1 GeV, SR
4 2 0 2 4 6 8 10 12
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.5 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Asimov Data
pB > 1 GeV, SR
FIG. 37: Mbc and M 2miss in the signal region.
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8R
2
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Without continuum calibration weights
Off Res.On Res.
0.0 0.2 0.4 0.6 0.8 1.0cos
TBTO
0
2
4
6
8
Without continuum calibration weights
On Res.Off Res.
FIG. 38: Comparison of MC continuum on- and off-resonance samples using R2 and
cos θT BT O. As shape differences can be seen, it is expected that despite the continuum
correction being applied to on-resonance samples, the data and MC distributions in this
region will exhibit some disagreement.
in a 2D phase-space. Since the trend in the MVA score as seen in Figure 40 appears to be1193
very similar when the K veto is applied or not, we assume that the signal region data/MC1194
ratio can be well approximated by using the three control regions CRK,low, CRK,high and1195
CR0,low. In the following when talking about data/MC ratio we only refer to the ratio for1196
B → Xcℓν events. When computing these ratios, all other components are removed from1197
```
MC and the MC-estimated yields are also subtracted from data: (data - non-Xc) / Xc. The1198
```
data/MC ratio RSR in the SR is then equal to:1199
```
RSR =
```
R0,low · RK,high
RK,low
```
, (11)
```
This assumption can be tested by using the two validation regions defined by an MVA1200
score between 0.60 and 0.87. Using RV R2 = R3 · RV R1/R1, when only a kinematical cut1201
pBℓ > 1.0 GeV is applied, we find a value of RV R2 = 1.07 ± 0.01 where the error is the1202
61
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.03 GeV)
```
×104Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.12 GeV)
```
×104Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.5 GeV
```
```
2)
```
×104Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
FIG. 39: The three main kinematic variables in CR1 after rescaling by 30% the B decay
events containing a D → K0LX decay.
statistical uncertainty. The value obtained directly from using MC and data in this region1203
```
is RV R2 = 1.03 ± 0.01 (stat.). The gap between the two values is used as an additional1204
```
uncertainty on the SR data/MC. An additional uncertainty is associated to the fact that the1205
non-Xcℓν components also have a non-prefect modelling. The ratio RSR is computed again1206
by varying the non-Xcℓν yields by 50%. The difference with respect to the nominal value of1207
RSR is used as an additional uncertainty. Finally, we find: RSR = 1.01 ± 0.02 ± 0.06 ± 0.05 =1208
1.01 ± 0.08 where the first uncertainty is statistical, the second comes from the validation1209
region estimate and the third one from the non-Xcℓν yield variation. As justified in the1210
next Section, in the fit we use CR0,low. Its normalisation correction is directly taken from1211
data and MC. An uncertainty is also derived by varying the non-Xcℓν component yields1212
```
giving: R0,low = 1.11 ± 0.01(stat.) ± 0.05(additional uncert.) = 1.11 ± 0.05. When extracting1213
```
the signal branching fraction, we also probe regions where the cuts MX < 1.7 GeV and/or1214
q2 > 8 GeV2 are applied. We repeat the procedure described above for these regions and1215
the SR and CR0,low Xc data/MC ratios are summarise in Table XV.1216
62
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000= 0
Xc
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.01)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000= 0
Xc
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.01)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
FIG. 40: The B → Xcℓν suppression score after applying continuum suppression is shown
```
when requiring the presence of at least one K (left) and after applying the K veto (right).
```
The score is cut at 0.60 for the later plot to avoid unblinding the signal region.
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0N
K
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
Events
×105Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0N
K0S
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
Events
×105Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Data
pB > 1 GeV,
```
FIG. 41: The charged (left) and neutral (right) K multiplicities after applying continuum
```
suppression are shown.
Kinematic selection CR0,low SR
pBℓ > 1.0 GeV 1.11 ± 0.05 1.01 ± 0.08
pBℓ > 1.0 GeV, MX < 1.7 GeV 1.18 ± 0.04 1.07 ± 0.13
pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 1.24 ± 0.03 1.09 ± 0.25
TABLE XV: CR and SR Xcℓν normalisation factors for different kinematic selections.
63
FIG. 42: Illustration of the CR and SR definitions based on the K multiplicity and the Xc
MVA score. The SR is highlighted in green. The CR used in the fit setup is highlighted in
```
red (see Section 7 3 3 for details on the choice of this region). The regions VR1 and VR2
```
are used as validation regions for the ABCD method used to estimate the SR Xcℓν
```
component normalisation (see Section 7 3 2 for details about this method).
```
3. Shape mismodelling1217
Even though the Xcℓν normalisation doesn’t translate from one region to the other, the1218
shape of the data/MC ratio appears to be similar in all regions as illustrated in Figure 43.1219
We would like to use a control region orthogonal to the signal region in order to correct the12201221
B → Xcℓν component. A few different contributions could explain the mismodelling of this1222
component both on the level of detector modelling and the level of event generation. We1223
therefore correct this component as a whole.1224
1225
The shape correction factors are extracted together with the B → Xuℓν branching fraction1226
in a simultaneous fit of the signal and control regions. Binned free-floating normalisation1227
factors are assigned to the B → Xcℓν component in order to let the fit correct it. The1228
SR B → Xcℓν component is normalised to the value of RSR that we found above and1229
the B → Xcℓν MC yields in the CR are directly normalised to data. With this strategy,1230
all correlations between nuisance parameters are properly handled and the uncertainty on1231
the extracted branching fraction incorporates the B → Xcℓν shape correction. A nuisance1232
parameter is added for the Xc normalisation in each of the two regions based on the central1233
values and errors found. More details about the fitting setup are given in the next Section.1234
1235
CR0,low is orthogonal to the signal region and is mostly composed of B → Xcℓν events.1236
The yields of these events are large enough in this region to obtain statistically significant1237
Xcℓν shape factors. Using CRK,high was also considered but the compositions and shapes1238
of this region are much more similar to the signal region than for CR0,low and therefore1239
the correction factor extraction would rely heavily on the signal region which we want to1240
64
1.0 1.2 1.4 1.6 1.8 2.0 2.2pB [GeV]0.7
0.8
0.9
1.0
1.1
1.2
1.3
Xc Data/MC ratioCRK, low
CRK, highCR0, low
0 2 4 6 8 10 12 14 16q2 [GeV2]
0.8
0.9
1.0
1.1
1.2
1.3
1.4
Xc Data/MC ratioCRK, low
CRK, highCR0, low
0.0 0.5 1.0 1.5 2.0 2.5 3.0MX [GeV]
0.6
0.8
1.0
1.2
1.4
1.6
Xc Data/MC ratioCRK, low
CRK, highCR0, low
0 2 4 6 8 10 12pB : q2 [GeV:GeV2]0.8
0.9
1.0
1.1
1.2
1.3
Xc Data/MC ratioCRK, low
CRK, highCR0, low
FIG. 43: The normalised data/MC ratio is shown here for the three control regions
CRK,low, CR0,low and CRK,high defined above. The shape of the disagreement appears to be
similar within uncertainties for all regions.
avoid. Nevertheless, as the Xcℓν component is corrected as a whole, an uncertainty on the1241
```
Xcℓν composition difference between the K and signal regions (c.f. Tables XIII) needs to1242
```
be considered. This is also discussed in the next Section.1243
65
8. SIGNAL EXTRACTION1244
To extract signal yields, the pyhf and cabinetry packages are used to extract the B → Xuℓν1245
branching fraction from data distributions. We perform a binned template fit using MC1246
distributions. As discussed in the previous Section, we simultaneously fit the signal region1247
and the kaon region in order to constrain the B → Xcℓν shape using data and automatically1248
correct for mismodelling of this component in the signal region. The MC yield is split into1249
four templates including the signal template. The templates are discussed in Section 8 2.1250
```
The signal strength µ is extracted as a Parameter of Interest (POI) and nuisance parame-1251
```
```
ters (NP) based on the aforementioned systematic uncertainties are added to the fit. This1252
```
section details the fitting procedure.1253
1254
Different variables can be used to extract the signal. As we are considering a semi-leptonic1255
decay, the three variables MX , q2 and pBℓ are used. Two-dimensional fits are also considered.1256
In addition to the preselection and MVA cuts described previously, different phase-space1257
selections applied on generator level and different experimental selections on pBℓ , MX and1258
q2 are also applied. These selections directly impact the theoretical prediction for the triple1259
differential decay rate dΓ/dMX dq2dpBℓ as they reduce the phase-space region from which1260
the B → Xuℓν signal is extracted. This is also discussed in Section 8 2.1261
1. pyhf1262
The pyhf package is widely used in HEP as a fitting tool. It is based on the HistFactory1263
package. An outline of its functioning is given here. A general Poisson probability model1264
can be written as follows:1265
```
P(nb|µ) = L(µ) ∝
```
Y
b∈bins
```
Pois(nb|µνsigb + νbkgb ) (12)
```
```
where L(µ) is the likelihood function, b is the bin index, µ is the signal strength, nb is the1266
```
data histogram and νb are the signal and background MC histograms.1267
1268
In order to include multiple samples as well as various normalisations and variations,1269
the likelihood template needs to be generalised. Most importantly, multiplicative and addi-1270
tive modifiers are added to the definition of the event rates νb. Each modifier corresponds1271
to a nuisance parameter. For each modifier a constraint term is added to limit the rate1272
modification. The modifiers can influence both the total normalisation and the shape of1273
the considered distribution. The exact statistical model and the event rates as defined in1274
pyhf are given in Appendix E. The parameters assigned to each template are summarised1275
in Section 8 3.1276
2. Fit templates, free-floating parameters and phase-space regions1277
Historically, various cuts on pBℓ , MX and q2 have been applied in B → Xuℓν measurements1278
as they reduce background contributions. For instance, we always apply a requirement that1279
the lepton momentum is greater than 1.0 GeV as the low lepton momentum region is mainly1280
populated with continuum and lepton backgrounds. Moreover, a selection on the hadronic1281
66
mass at MX < 1.7 GeV cuts away most B → Xcℓν processes as the lightest charm meson,1282
the D meson, has a mass around 1.86 GeV and is very narrow. The inclusive B → Xuℓν1283
models take these selections into account and predictions for the decay rate are calculated in1284
specific phase-space regions. In order to test these predictions we apply various phase-space1285
cuts on the generator level on signal events in the distributions we fit. Signal events are1286
```
therefore split in two templates: events in the phase-space region (signal-in component) and1287
```
```
events outside of the phase space region (signal-out component). The former template is1288
```
our nominal signal template and the signal strength is extracted from it. The background is1289
split into a B → Xcℓν template and a template including all other background contributions1290
```
(consisting of continuum as well as fake and secondary leptons). Additionally, we apply1291
```
different cuts on the experimental level in order to reject more or less background. In certain1292
cases, very few signal events pass the experimental cuts but not the phase-space cuts. This1293
is the case for instance when the pBℓ cut at 1.0 GeV is applied on both levels because of1294
the good resolution of this variable. In these cases the signal contribution outside of the1295
phase-space is neglected and a single template is defined for the signal. In other cases the1296
signal-out component is small but cannot be neglected. In these fits, the same free-floating1297
normalisation is assigned to the signal-in and signal-out templates. More details about the1298
fit parameters are given in the following sections.1299
1300
We consider the following phase-space cuts:1301
• pBℓ > 1.0 GeV: always applied as the equivalent experimental cut is already applied1302
on our samples1303
• MX < 1.7 GeV: the equivalent experimental cut is known to reduce B → Xcℓν1304
background so this phase-space cut is also probed1305
```
• q2 > 8 GeV2: the equivalent experimental cut rejects B → Xcℓν background; this cut1306
```
could also reduce the sensitivity to specific theoretical components1307
The acceptance of each phase-space region is calculated from MC as the ratio of number1308
of generated events before and after applying the phase-space cuts. The acceptance for1309
different phase-space regions is given in Tab. XVI.1310
Phase space cuts Acceptance ε∆B
EBℓ > 1.0 GeV 86.7%
EBℓ > 1.0 GeV 56.5%
MX < 1.7 GeV
EBℓ > 1.0 GeV
MX < 1.7 GeV 31.5%
q2 > 8 GeV2
TABLE XVI: Phase-space acceptance for different selections.1311
1312
1313
In the following Sections, the phase-space region that is probed and the experimental1314
cuts that are applied are clearly mentioned.1315
67
3. Fit parameters1316
In our fit, the following pyhf modifiers are implemented:1317
```
• Normalisation uncertainty (normsys): modifier to take into account overall normali-1318
```
sation uncertainties on the considered distribution. This modifier enters the fit as the1319
up and down variations of the overall normalisation factor associated to the param-1320
```
eter (the central value of the normalisation factor being equal to 1). As the other-1321
```
backgrounds template is small in the fitted distributions, a normsys modifier is also1322
```
attached to it in order to constrain it and limit fit instabilities (Gaussian constraint1323
```
```
with a width of 50% around the nominal yields). As explained Section 7 3 3, the1324
```
Xcℓν normalisation is corrected in the SR and CR and the associated uncertainty is1325
implemented in the fit as a Gaussian constrained normalisation uncertainty.1326
```
• Correlated shape (histosys): modifier to take into account shape variations on the1327
```
considered distribution. This modifier enters the fit as the binned sample up and down1328
rate variations associated to the parameter.1329
```
• MC statistical uncertainty (staterror): specific modifier for the MC statistical un-1330
```
certainty. The uncertainty per bin is estimated using a set of bin-wise constrained1331
scale factors.1332
```
• Unconstrained normalisation (normfactor): this modifier is used for the strength of1333
```
```
the signal templates (signal-in and signal-out when it is not neglected). It scales the1334
```
sample rate by a free-floating parameter. The signal template strength is the POI and1335
eventually allows the computation of the B → Xuℓν branching fraction. The signal1336
strength is only assigned to the B → Xuℓν component in the signal region which keeps1337
```
the (small) signal component fixed in the control region.1338
```
```
• Data-driven shape (shapefactor): free bin-wise normalisation factors. This modifier1339
```
is used to fit the normalisation and shape of the B → Xcℓν template as each bin is1340
normalised separately. It is assigned to both regions in the fit.1341
In our fit, every nuisance parameter except for the MC statistical uncertainty is split into a1342
```
normsys and a histosys contribution. An uncertainty is associated to B(B → Xuℓν) and1343
```
this is incorporated in the fit. However, this is also the number we want to extract from1344
the fit. Therefore, the associated nuisance parameter is allowed to modify the shape of the1345
considered distribution but not its overall normalisation.1346
1347
As explained in the next Section, for certain systematic uncertainty sources with a large1348
number of associated nuisance parameters, this number is reduced such that 99% of the1349
associated variance is covered. The number of bins is also different for different fits and1350
```
therefore the number of nuisance parameters can slightly vary from one fit to another (dif-1351
```
```
ferent fitted variable and different phase-space region).1352
```
1353
As mentioned above, in some of the fits, the signal-out template is completely neglected as1354
its yields are extremely small relatively to the the signal-in template. In other fits, the yields1355
are small but not negligible and their shape is similar to the background template shapes1356
and in particular the B → Xcℓν shape. This is illustrated in Fig. 44 for a phase-space1357
68
region defined by the cuts pBℓ > 1.0 GeV and MX < 1.7 GeV. Therefore, the normalisa-1358
tion of this template can correlate very strongly to the other three normalisations and its1359
resulting uncertainty and bias can be very large. In these cases the two Xuℓν templates are1360
kept separate but the same free-floating normalisation µXu is assigned to both templates.1361
Finally, in other fits, the signal-out component is large enough to be treated as a completely1362
separate template and is therefore assigned its own independent free-floating normalisation.1363
The parameters assigned to each of the four templates are summarised in Table XVII.1364
```
Besides, in fits with a very tight phase-space region (when applying a tight MX or q2 cut1365
```
```
for example), the yields of ”other backgrounds” events become very small compared to the1366
```
semi-leptonic event yields. Floating this component therefore renders the fit unstable and1367
```
we fix its normalisation (all NPs related to this component are still allowed to float its1368
```
```
normalisation and shape).1369
```
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75pB [GeV]0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6 Xu Signal-inXu Signal-out
Xc BackgroundOther backgrounds
0 1 2 3 4 5MX [GeV]0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8 Xu Signal-inXu Signal-out
Xc BackgroundOther backgrounds
0 5 10 15 20 25q2 [GeV2]0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16 Xu Signal-in
Xu Signal-outX
c BackgroundOther backgrounds
FIG. 44: pBℓ , MX and q2 split into the four templates defined for the fit. The signal
component is split in signal-in and signal-out templates using the cuts pBℓ > 1.0 GeV and
MX < 1.7 GeV applied on generator level. Each histogram is normalised to compare the
shapes.1370
1371
13721373
There are in total N + 2 free-floating parameters where N is the number of bins in the con-1374
sidered fit. If the signal-out component is ignored there are N + 1 free-floating parameters.1375
1. Implementation of systematic uncertainties within the fit1376
a. Two-sided variation1377
1378
69
Signal region Control region
Xuℓν-in 1 free-floating normalisation factor -
Xuℓν-out Neglected, same normalisation factor as Xuℓν-in -
or independent normalisation factor
Xcℓν N free-floating normalisation factors N free-floating normalisation factors
```
(+1 Gaussian constrained normalisation NP) (+1 Gaussian constrained normalisation NP)
```
Other backgrounds Gaussian constrained normalisation NP Gaussian constrained normalisation NP
```
(with width of 50% around nominal yields) (with width of 50% around nominal yields)
```
or fixed when yields are too low or fixed when yields are too low
```
TABLE XVII: Summary of fit parameters used for each of the four templates (for N bins).
```
The majority of systematics we consider are what we label two-sided variations. These cor-1379
respond to systematic uncertainties such as branching fractions of the B → Xℓν channels,1380
form factors or slow π calibration factors in which we have auxiliary measurements from1381
which we can take ±σ variations. These variations are propagated through the reconstruc-1382
tion by reweighting events to generate two sets of varied MC templates. When the fit pulls on1383
the nuisance parameters, the templates are morphed in the direction of the varied templates.1384
When several parameters are correlated, the variations are calculated from the covariance1385
matrix and the corresponding eigenvectors and eigenvalues as explained in Section 6. For1386
each pair of up/down variations, one nuisance parameter is added to the fit.1387
1388
1389
b. One-sided variation1390
1391
Systematics in which we have only a one-sided variation, such as switching the nominal1392
```
inclusive B → Xuℓν model (DFN) to the alternate (BLNP), are challenging to deal with, as1393
```
there is no natural choice for the distribution of the prior for the nuisance parameter. Within1394
this analysis the choice of the inclusive B → Xuℓν model is the most impactful nuisance1395
parameter. As the modelling of B → Xuℓν is in general not well known, we symmetrise such1396
one-sided variations by mirroring about the nominal shape to create two-sided variations.1397
1398
1399
c. Toy variation1400
1401
1402
Several uncertainties, such as those associated to the statistical uncertainty on BDT based1403
continuum shape corrections, or particle identification corrections, are propagated through1404
the analysis as N sets of toy weights. To capture the bin-to-bin correlations of these un-1405
certainties within the pyhf framework, we construct the covariance matrix of the binned1406
MC samples from the N sets of weights. The covariance matrix is constructed in a flat-1407
```
tened global binning that assigns a unique bin index to the combination of channel (only1408
```
one channel is considered for now but splitting the B charge or the lepton flavour is also1409
```
possible), template and fitted variable(s). The covariance matrix is diagonalised and its1410
```
eigenvectors/eigenvalues are calculated as described earlier.1411
1412
To capture the full covariance matrix, the number of variations, and hence nuisance param-1413
70
eters in the fit, would be equivalent to the number of bins in the flattened global binning.1414
Most of these nuisance parameters would be negligible. To avoid adding these, we truncate1415
the number of components, taking the largest n components such that the sum of their1416
eigenvalues exceeds 99% of the sum of all eigenvalues, and thus covers 99% of the variance.1417
1418
We additionally consider a special case of the two-sided variations in which we build a1419
covariance matrix from a large number of two-sided variations and follow the procedure1420
above to reduce the number of nuisance parameters. This is used to reduce the number of1421
nuisance parameters associated with the modelling of the charm decay from 234 to ∼ 101422
and to reduce the number of nuisance parameters associated with the FEI calibration from1423
a total of 23 to one for the the B0 channel and two for the B± channel.1424
4. Symmetrising1425
Most systematics that are considered are symmetric about the nominal template in the1426
upward and downward varied templates. However, to avoid introducing biases in the fit, the1427
variations that are known to be asymmetric are symmetrised. These are mainly form factor1428
variations and inclusive model parameter variations. The asymmetry is tested via:1429
```
A = maxi
```
```
(Hi − H−i ) − (H+i − Hi)
```
Hi
```
, (13)
```
where i runs over the flattened global bin index, Hi is the nominal yield in the bin, and H±i1430
are the yields of the up and down varied templates in the bin. If the asymmetry is found to1431
be small A < 0.005, we average the distance between the nominal and varied templates. If1432
the asymmetry is found to be large, we take the maximum envelope of the varied template1433
in each bin.1434
5. List of fits1435
The list of fits we perform is given below. We present results for all considered variables only1436
for Fit 1 to illustrate them but subsequent fits are repeated only for the variable yielding1437
the most precise and most stable result. Compared to the previous iteration of the analysis,1438
fits 2 and 6 were removed. In these setups, the Xuℓν-out component was assigned the same1439
normalisation parameter as the Xuℓν-in component even though its yields weren’t negligible.1440
This makes the fit output much more dependent on the modelling of the signal template1441
in the considered phase-space region. Fit 4 is kept for illustration purposes but this setup1442
leads to biased results as is shown in Appendix F.1443
1444
1445
• Fit 11446
– Signal phase-space selection: pBℓ > 1.0 GeV1447
– Experimental cut: pBℓ > 1.0 GeV1448
– Signal-out: ≈ 0.1% of all signal events so it is neglected1449
71
– Other backgrounds: floated normalisation within a Gaussian constraint of 50%1450
of the nominal yields1451
– Fitted variables: pBℓ , q2, MX , 2D MX :q2, 2D pBℓ :q21452
• Fit 31453
– Signal phase-space selection: pBℓ > 1.0 GeV, MX < 1.7 GeV1454
– Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV1455
– Signal-out: ≈ 2.5% of all signal events so it is assigned the same free-floating1456
normalisation as the signal-in component1457
– Other backgrounds: fixed normalisation1458
– Fitted variables: 2D pBℓ :q21459
• Fit 41460
– Signal phase-space selection: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV21461
– Experimental cut: pBℓ > 1.0 GeV1462
– Signal-out: ≈ 46% of all signal events so it is assigned an independent free-floating1463
normalisation1464
– Other backgrounds: floated normalisation within a Gaussian constraint of 50%1465
of the nominal yields1466
– Fitted variables: q21467
• Fit 51468
– Signal phase-space selection: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV21469
– Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV21470
– Signal-out: ≈ 4.5% of all signal events so it is assigned the same free-floating1471
normalisation as the signal-in component1472
– Other backgrounds: fixed normalisation1473
– Fitted variables: pBℓ1474
• Fit 71475
– Signal phase-space selection: pBℓ > 2.1 GeV1476
– Experimental cut: pBℓ > 1.0 GeV1477
– Signal-out: ≈ 68% of all signal events so it is assigned an independent free-floating1478
normalisation1479
– Other backgrounds: floated normalisation within a Gaussian constraint of 50%1480
of the nominal yields1481
– Fitted variables: q21482
72
6. ∆B(B → Xuℓν) measurement1483
```
To extract ∆B(B → Xuℓν), we use an MC sample on which all selections discussed in1484
```
Sections 3 and 5 are applied. From the fit presented above, the signal strength µ is extracted.1485
```
Given the input B(B → Xuℓν), one can therefore obtain the measured branching fraction.1486
```
```
The MC B → Xuℓν events were generated with the branching ratio values of B(B± →1487
```
```
Xuℓν) = (1.92 ± 0.24) · 10−3 and B(B0 → Xuℓν) = (1.76 ± 0.22) · 10−3. The input value used1488
```
for the total full phase-space branching fraction is extracted from generator level samples1489
```
as: B(B → Xuℓν) = N genXuℓν /(2NB ¯B ) = (1.82 ± 0.03) · 10−3. Where the uncertainty comes1490
```
```
from the uncertainty on the number of B ¯B pairs NB ¯B = (387.1 ± 5.6) · 106 (the statistical1491
```
```
uncertainty on the number of Xuℓν events generated is negligible). Cuts on the phase-space1492
```
reduce the theoretical acceptance ε∆B as discussed in Section 8 2. The predicted branching1493
fraction in each phase-space region is therefore scaled by the corresponding acceptance.1494
1. Asimov test1495
Before unblinding the data we first perform an Asimov fit5. An Asimov fit consists of using1496
the MC distribution itself as pseudo-data in both regions used in the fit. When performing1497
the fit, one would then expect to recover exactly the initial settings i.e. every single free-1498
floating and nuisance parameter should be equal to its initial value. In the Asimov test, a1499
signal strength of µ = 1.0 is obtained as expected. The statistical uncertainty is obtained1500
from 1,000 toy fits where all nuisance parameters are fixed to their initial value. The re-1501
sulting distribution of signal strengths is fitted to a Gaussian whose width corresponds to1502
the statistical uncertainty. The systematic uncertainty is then derived by subtracting in1503
quadrature the statistical uncertainty from the total uncertainty.1504
1505
We want to perform fits for different variables in different phase-space regions and with1506
different experimental cuts improving the signal to background ratio. A lepton momentum1507
cut at 1.0 GeV is applied by default on all samples. The results from all these fits are1508
shown in Tables XVIII to XXII. The optimal B → Xcℓν MVA cut is chosen as the cut that1509
minimises the value of the total uncertainty in fit 1 with a phase-space and experimental1510
```
cuts of pBℓ > 1.0 GeV (cf. Section 5). The value of the cut was found to be equal to 0.87.1511
```
In addition, for this same fit, we show the pre- and post-fit distributions in Fig. 45. Even15121513
though each systematic source is symmetrised according to the procedure described above,1514
the total uncertainty can still be asymmetric and it is computed as such. Nevertheless, if1515
```
the asymmetry is small, we quote the larger uncertainty as symmetric. Fits using MX (q2)1516
```
```
are not performed with an experimental MX (q2) cut at 1.7 GeV (8 GeV2).1517
```
The binning chosen to fit each variable is shown in Tab. XXIII.15181519
1520
The separate impact of every nuisance parameter can be obtained directly with pyhf.1521
The impact of a nuisance parameter is defined as the difference between the nominal POI1522
post-fit value and its value from a fit where the nuisance parameter is held constant at its1523
central value plus or minus its associated uncertainty. The 30 parameters with the largest1524
impact from the q2 fit in the region pBℓ > 1.0 GeV are displayed in Fig. 46. The ranking1525
5 The name Asimov comes from Isaac Asimov’s short story Franchise where one person is selected to
represent the entire electorate during the United States presidential election.
73
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
1400
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
```
FIG. 45: Pre-fit (top) and post-fit (bottom) pBℓ :q2 distributions for a simultaneous fit of
```
```
the signal region (left) and CR0,low (right) using Asimov data. The Xuℓν-in region is
```
```
defined by a selection pBℓ > 1.0 GeV (fit 1).
```
```
Fitted variable ∆B(B → Xuℓν) × 103
```
pBℓ 1.58+0.18−0.16
q2 1.58 ± 0.13 = 1.58 ± 0.08 ± 0.10
MX 1.58+0.21−0.18
```
MX :q2 1.58 ± 0.13
```
pBℓ :q2 1.58 ± 0.13 = 1.58 ± 0.08 ± 0.10
TABLE XVIII: Partial branching fractions obtained from various Asimov fits for a phase
```
space selection of pBℓ > 1.0 GeV and an experimental selection of pBℓ > 1.0 (Fit 1). The
```
uncertainties given for the branching fraction are respectively the statistical and
systematic errors.
74
```
Fitted variable ∆B(B → Xuℓν) × 103
```
pBℓ :q2 1.03 ± 0.08 = 1.03 ± 0.06 ± 0.06
TABLE XIX: Partial branching fractions obtained from various Asimov fits for a phase
space selection of pBℓ > 1.0 GeV, MX < 1.7 GeV and an experimental selection of pBℓ > 1.0
```
GeV, MX < 1.7 GeV (Fit 3). The uncertainties given for the branching fraction are
```
respectively the statistical and systematic errors.
```
Fitted variable ∆B(B → Xuℓν) × 103
```
q2 0.57 ± 0.05
TABLE XX: Partial branching fractions obtained from various Asimov fits for a phase
space selection of pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 and an experimental
```
selection of pBℓ > 1.0 GeV (Fit 4). The uncertainties given for the branching fraction are
```
respectively the statistical and systematic errors.
```
Fitted variable ∆B(B → Xuℓν) × 103
```
pBℓ 0.57 ± 0.06 = 0.57 ± 0.03 ± 0.05
TABLE XXI: Partial branching fractions obtained from various Asimov fits for a phase
space selection of pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 and an experimental
```
selection of pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 (Fit 5). The uncertainties given
```
for the branching fraction are respectively the statistical and systematic errors.
```
Fitted variable ∆B(B → Xuℓν) × 103
```
q2 0.35 ± 0.05 = 0.35 ± 0.04 ± 0.03
TABLE XXII: Partial branching fractions obtained from various Asimov fits for a phase
```
space selection of pBℓ > 2.1 GeV and an experimental selection of pBℓ > 1.0 GeV (Fit 7).
```
The uncertainties given for the branching fraction are respectively the statistical and
systematic errors.
Variable Binning
```
pBℓ 12 bins: 11 bins of width 0.1 GeV in [1.0, 2.1] GeV and [2.1, 2.7] GeV (fit 1)
```
```
10 bins: [1.0, 1.4, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.7] GeV (fit 5)
```
q2 10 bins: 9 bins of width 2 GeV2 in [0, 18] GeV2 and [18, 26] GeV2
MX 4 bins: [0, 1.5, 1.9, 2.5, 5.0] GeV
[0, 1.5] GeV × [0, 2, 4, 6, 8, 10, 12, 14, 26] GeV2
```
MX :q2 [1.5, 1.9] GeV × [0, 2, 4, 6, 26] GeV2
```
[1.9, 2.5] GeV × [0, 2, 4, 26] GeV2
[2.5, 5.0] GeV × [0, 2, 26] GeV2
pBℓ :q2 12 bins: [1.0, 1.3, 1.6, 1.9, 2.7] GeV × [0, 4, 8, 26] GeV2
TABLE XXIII: Binning of variables used in the fits described in this Section.
75
of the most impactful nuisance parameters for every fit is shown in Appendix F. The un-1526
```
certainty of the DFN parameters has the largest impact on this fit (particularly the first1527
```
```
eigenvariation). For each nuisance parameter, the pull, which is defined below in Section1528
```
8 7, is also shown on Fig. 46.1529
1530
1531
DFN[1]gammaS
mu_signal_XclnuMCStatsignal[11]
FEI_B0FEI_BpleptonID[0]f+-/00
bf_B0topilnubf_Bptorholnu
0.050
0.025
0.000
0.025
0.050
bf_B0torholnuHybridModel
mu_sideband_XclnuMCStatsignal[8]bf_B0toDstetalnu
bf_BptoXulnubf_BptoDstetalnuMCStatsignal[9]bf_B0toXulnuTracking
0.050
0.025
0.000
0.025
0.050
ff_Pion[3]Slow_Pi0[1]leptonID[3]bf_Bptopilnu
bf_B0toDetalnuMCStatsignal[0]bf_BptoomegalnuMCStatsignal[6]bf_BptoDstpipilnu
ff_Rho[9]
0.050
0.025
0.000
0.025
0.050
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 46: Nuisance parameter impact ranking for the 30 most important sources for fit 1.
```
The post-fit (resp. pre-fit) impact is shown as a full (resp. empty) box. The blue (resp.
```
```
purple) band corresponds to the POI impact of the parameter when it is held to its nominal
```
```
value plus (resp. minus) its associated uncertainty. More details are given in the text.
```
Fit 4 and 7 are dropped as a non-negligible bias of the signal-out normalisation is observed1532
as shown in Appendix F. Based on the various checks discussed below and the expected1533
precision, we propose to quote the following four fits in a publication with the nominal fit1534
in bold:1535
• Fit 1 with pBℓ :q21536
• Fit 3 with pBℓ :q21537
• Fit 5 with pBℓ1538
76
Slow_Pi0[0]bf_B0toDstetalnubf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]ff_DststBroad[2]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]mu_Xclnu_shape[10]mu_Xclnu_shape[11]MCStatsideband[2]MCStatsideband[9]
Slow_Pi0[0]
bf_B0toDstetalnu
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
ff_DststBroad[2]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
mu_Xclnu_shape[10]
mu_Xclnu_shape[11]
MCStatsideband[2]
MCStatsideband[9]
1.00 -0.03 -0.02 0.14 -0.12 0.01 -0.01 0.02 0.03 -0.13 0.02 0.13 -0.02 -0.01 -0.15 -0.03 -0.01 -0.20 -0.08 -0.10 -0.21 -0.12 -0.12 -0.15
-0.03 1.00 -0.06 -0.12 0.14 -0.09 0.02 0.02 -0.04 -0.02 0.12 -0.15 0.09 0.14 -0.25 -0.09 0.12 -0.21 -0.03 0.08 0.07 0.13 0.15 0.01
-0.02 -0.06 1.00 -0.12 0.04 -0.06 -0.03 0.02 0.03 0.02 0.03 -0.02 -0.22 -0.05 -0.24 -0.04 0.12 -0.32 -0.05 0.10 -0.10 0.09 0.14 0.11 0.12 0.13
-0.12 -0.12 1.00 0.07 -0.08 0.02 -0.01 0.02 -0.02 -0.08 -0.07 0.06 -0.19 0.13 0.13 -0.34 -0.07 0.16 -0.34 -0.15 0.11 0.07 0.14 0.15
0.14 0.14 0.04 0.07 1.00 0.01 0.01 -0.01 0.01 -0.04 0.19 0.03 0.02 -0.10 0.06 0.13 -0.07 0.09 0.22 0.21 0.25 0.11 0.29 0.24
-0.12 -0.09 -0.06 -0.08 1.00 -0.12 -0.01 0.01 -0.07 -0.12 -0.02 0.10 -0.40 0.01 0.10 -0.45 -0.05 0.21 -0.05 0.11 0.23 0.22 0.23
0.01 -0.03 0.01 -0.12 1.00 0.01 0.01 0.01 -0.02 -0.08 -0.03 -0.02 -0.30 -0.07 0.08 -0.13 -0.08 0.25 0.23 0.12 0.11 0.09 0.07
-0.01 0.02 0.02 0.02 0.01 0.01 1.00 0.03 -0.02 -0.62 -0.06 0.12 0.02 0.03 0.01 -0.02 0.02 -0.02 0.01 0.03 -0.03 -0.01 -0.04 0.01
0.02 0.03 -0.01 -0.01 -0.01 0.01 0.03 1.00 -0.02 -0.08 0.04 -0.05 -0.42 0.04 0.03 -0.11 0.02 0.02 -0.08 -0.03 -0.09 -0.08 -0.05 -0.10 0.01 0.02
0.02 0.02 0.02 0.01 0.01 -0.02 -0.02 1.00 0.21 -0.01 -0.05 0.14 0.02 0.02 0.04 -0.02 -0.01 0.05 -0.02 0.02 -0.01 0.05 0.04 0.01
0.03 -0.04 0.03 -0.02 -0.04 0.01 -0.62 -0.08 0.21 1.00 0.07 -0.34 0.03 0.02 0.04 0.02 0.01 0.06 0.03 0.01 0.04 0.02 0.03 -0.01
-0.13 -0.02 -0.08 0.19 -0.07 -0.02 0.04 -0.01 0.07 1.00 -0.04 0.16 0.05 -0.03 -0.12 -0.01 -0.07 -0.20 -0.06 -0.12 -0.22 -0.09 -0.15 -0.19
0.02 -0.02 -0.22 -0.07 0.03 -0.12 -0.08 -0.06 -0.05 -0.05 -0.04 1.00 -0.21 -0.48 -0.26 -0.16 0.06 0.19 0.05 0.08 0.17 0.09 -0.17 -0.02 0.02
0.13 0.12 -0.05 0.06 0.02 -0.02 -0.03 0.12 -0.42 0.14 -0.34 0.16 -0.21 1.00 0.01 0.01 0.04 -0.16 -0.16 -0.07 -0.18 -0.20 -0.12 -0.04 -0.07 -0.04
-0.02 -0.15 -0.24 -0.19 -0.10 0.10 -0.02 0.02 0.04 0.02 0.03 0.05 -0.48 0.01 1.00 0.53 0.10 0.71 0.39 0.07 0.44 0.19 0.01 0.11 -0.02 -0.03 -0.01
-0.01 0.09 -0.04 0.13 0.06 -0.40 -0.30 0.03 0.03 0.02 -0.03 -0.26 0.01 0.53 1.00 0.37 0.31 0.70 0.47 0.08 0.29 0.25 0.08 0.11 0.13
-0.15 0.14 0.12 0.13 0.13 0.01 -0.07 0.01 -0.11 0.04 0.02 -0.12 -0.16 0.04 0.10 0.37 1.00 -0.02 0.24 0.55 0.05 0.27 0.46 0.25 0.35 0.40 -0.23
-0.03 -0.25 -0.32 -0.34 -0.07 0.10 0.08 -0.02 0.02 -0.02 0.04 -0.01 0.06 -0.16 0.71 0.31 -0.02 1.00 0.51 0.09 0.66 0.42 0.12 0.07 0.02 -0.01
-0.01 -0.09 -0.05 -0.07 0.09 -0.45 -0.13 0.02 -0.01 0.02 -0.07 0.19 -0.16 0.39 0.70 0.24 0.51 1.00 0.49 0.35 0.57 0.38 0.04 0.15 0.15
-0.20 0.12 0.10 0.16 0.22 -0.05 -0.08 0.02 -0.08 0.05 0.01 -0.20 0.05 -0.07 0.07 0.47 0.55 0.09 0.49 1.00 0.18 0.54 0.74 0.31 0.53 0.61 0.01 0.01
-0.08 -0.21 -0.10 -0.34 0.21 0.25 -0.02 -0.03 -0.02 0.06 -0.06 0.08 -0.18 0.44 0.08 0.05 0.66 0.35 0.18 1.00 0.56 0.33 0.24 0.25 0.22
-0.10 -0.03 0.09 -0.15 0.21 -0.05 0.23 0.01 0.02 0.03 -0.12 0.17 -0.20 0.19 0.29 0.27 0.42 0.57 0.54 0.56 1.00 0.68 0.33 0.50 0.50 0.01
-0.21 0.08 0.14 0.11 0.25 0.11 0.12 0.03 -0.09 0.01 -0.22 0.09 -0.12 0.01 0.25 0.46 0.12 0.38 0.74 0.33 0.68 1.00 0.42 0.68 0.76 0.01 0.01
-0.12 0.07 0.11 0.07 0.11 0.23 0.11 -0.03 -0.08 -0.01 0.04 -0.09 -0.17 -0.04 0.11 0.08 0.25 0.07 0.04 0.31 0.24 0.33 0.42 1.00 0.43 0.45 -0.25
-0.12 0.13 0.12 0.14 0.29 0.22 0.09 -0.01 -0.05 0.05 0.02 -0.15 -0.07 -0.02 0.11 0.35 0.02 0.15 0.53 0.25 0.50 0.68 0.43 1.00 0.69 0.01
-0.15 0.15 0.13 0.15 0.24 0.23 0.07 -0.04 -0.10 0.04 0.03 -0.19 -0.02 -0.04 -0.03 0.13 0.40 -0.01 0.15 0.61 0.22 0.50 0.76 0.45 0.69 1.00 0.01 0.01
0.01 -0.23 0.01 0.01 0.01 1.00
0.01 0.01 0.02 0.01 -0.01 0.02 -0.01 0.01 0.01 0.01 -0.25 0.01 0.01 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
```
FIG. 47: Correlation matrix for fit 1 (pBℓ :q2 fit with pBℓ > 1.0 GeV cut for phase-space and
```
```
experimental selection). Only rows/columns where a value of 0.20 or larger is found are
```
shown.
2. Systematics breakdown1539
We break down the systematic uncertainty contributions by producing a set of 1000 toys1540
whose data yields are fixed to the Asimov yields and whose auxiliary data is fixed to the1541
initial value for all systematics except the one we evaluate the contribution of. Each toy is1542
then fitted and the obtained uncertainty is taken as the systematic source contribution to1543
the total uncertainty. The breakdown for all fits is summarised in Table XXIV. The DFN1544
model parameter uncertainty is the largest contribution for all four fits discussed in this1545
Section.1546
77
```
Systematics source Systematics uncertainty (%)
```
Fit 1 Fit 3 Fit 5
DFN parameters 4.7 4.2 5.8
DFN → BLNP 0.14 0.44 1.6
γS 1.6 1.2 1.8
B → πℓν form factors 0.30 0.32 0.33
B → ρℓν form factors 0.27 0.30 0.24
B → ωℓν form factors 0.10 0.11 0.11
```
B → η(′)ℓν form factors 0.01 0.01 0.02
```
B± → Xuℓν branching fractions 0.95 0.70 0.49
B0 → Xuℓν branching fractions 0.56 0.53 0.53
B → D∗∗Broad form factors 0.45 0.23 0.03
B → D∗∗Narrow form factors 0.06 0.02 0.01
B → D/D∗ℓν form factors 0.02 0.04 0.02
B± → Xcℓν branching fractions 0.73 0.56 0.06
B0 → Xcℓν branching fractions 0.66 0.22 0.09
D decay branching fractions 0.15 0.28 0.23
SR Xcℓν normalisation 1.5 2.3 3.8
CR Xcℓν normalisation 1.0 0.76 0.59
Other backgrounds normalisation 0.19 N/A N/A
NB ¯B 1.6 1.6 1.6
FEI 1.3 1.4 1.4
Slow π 0.40 0.25 0.20
ℓ ID 0.70 0.67 0.68
f ±/00 0.64 0.66 0.72
Continuum reweighting 0.12 0.15 0.18
Tracking 0.27 0.25 0.29
K0S efficiency 0.05 0.06 0.04
K± ID 0.01 0.02 0.02
MC Statistics 1.2 1.1 0.85
Additional composition uncertainty 2.0 2.9 0.06
Total systematic 6.4 6.5 7.8
Statistical 5.1 5.0 4.6
Total 8.2 8.2 9.1
TABLE XXIV: Systematic uncertainty breakdown for all fits. The systematic sources are
ranked in descending order of their contribution in fit 1.
78
7. Fitter validation1547
The pull of a parameter entering a fit is defined as:1548
```
(µinit−µ
```
σ+ , if µ ≤ µinit
µ−µinit
σ− , if µ > µinit
```
(14)
```
```
where µinit is the initial (true) value of the parameter, µ its post-fit value and σ+/σ− are1549
```
the amplitudes of associated positive/negative post-fit uncertainties. The pull is expected1550
to be equal to 0 for every parameter in an Asimov fit. This is confirmed in Fig. 48 for all1551
nuisance parameters for the pBℓ fit in the region pBℓ > 1.0 GeV.1552
1. Toy fit1553
We want to test the fit set-up on a large number of randomly generated toy data sets. These1554
toys are generated from Poisson variations of the input MC yields. In addition, for each1555
nuisance parameter the initial value of the auxiliary data is Gaussian-varied. For each of1556
these toys, the fit is performed, the signal strength µ is extracted and its pull from the initial1557
value is calculated as defined in Equ. 14. For a sufficiently large number of toys, the pulls1558
are expected to be distributed as a Gaussian normal distribution. Any deviation from this1559
distribution would indicate problems in the fit, such as a bias on the POI. In Fig. 49, the1560
pull distribution obtained from the pBℓ :q2 fit in the phase-space region pBℓ > 1.0 GeV for1561
5,000 toys is shown together with the normal distribution fit. Toy distributions from every1562
fit are shown in Appendix F.1563
2. Linearity check1564
In order to further asses the stability of the fit, we perform a linearity check. In this test,1565
different sets of toys are produced by varying the initial POI value. Each toy is fitted and1566
for each set of toys the mean value of the signal strength is extracted assuming a Gaussian1567
distribution. This value is expected to be close to the initial value. We test this for 11 initial1568
equidistant values between 0.5 and 1.5. In Fig. 50, we show the output value of the signal1569
strength as a function of its initial value for the pBℓ :q2 fit in the phase-space region pBℓ > 1.01570
GeV. The overall behaviour is linear and therefore this fit is expected to be stable. Linearity1571
```
check plots of every fit are shown in Appendix F. For some fits (in particular the MX fits),1572
```
if the initial value of the signal strength given in the linearity test is small i.e. 0.5 − 0.7, the1573
output value is slightly overestimated. The MX fits in general are expected to lead to large1574
uncertainties and we will therefore not investigate this behaviour further.1575
79
FEI_B0FEI_BpKshortVetoSlow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Tracking
bf_B0toDetalnubf_B0toDlnubf_B0toDonelnu
bf_B0toDoneprimelnu
bf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnu
2
0
2
```
(
```
```
) /
```
bf_BptoDstzerolnubf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]kaonIDVetoleptonID[0]leptonID[1]leptonID[2]leptonID[3]
DFN[1]DFN[2]
HybridModelbf_B0toXulnubf_B0topilnubf_B0torholnu
2
0
2
```
(
```
```
) /
```
bf_BptoXulnubf_Bptoetalnu
bf_Bptoetaprimelnubf_Bptoomegalnu
bf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]ff_Rho[4]
2
0
2
```
(
```
```
) /
```
ff_Rho[5]ff_Rho[6]ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaSCont.Norm.[0]Cont.Norm.[1]
Cont.Reweight[0]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]Cont.Reweight[4]mu_sideband_Xclnumu_other_bkgmu_signal_XclnuMCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsideband[10]MCStatsideband[11]MCStatsignal[0]MCStatsignal[1]
2
0
2
```
(
```
```
) /
```
MCStatsignal[2]MCStatsignal[3]MCStatsignal[4]MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]MCStatsignal[10]MCStatsignal[11]
2
0
2
```
(
```
```
) /
```
FIG. 48: Pulls for all nuisance parameters for fit 1 with Asimov data.
80
4 2 0 2 4
```
( in)/
```
0
50
100
150
200
Trials
```
G = 0.027±0.014
```
```
G = 1.010±0.010
```
FIG. 49: Distribution of the signal strength pulls from 5,000 toys for fit 1. The
distribution is fitted to a normal Gaussian distribution. The fitted values of the mean and
variance of the normal distribution are displayed as well.
0.6 0.8 1.0 1.2 1.4 1.6 1.8
in
0.6
0.8
1.0
1.2
1.4
```
( 0.9982±0.0022) in+(0.0042±0.0020)
```
FIG. 50: Linearity check for fit 1. For each point, 1,000 toys were produced
81
8. B → Xcℓν factors1576
In the Asimov fit discussed above, all B → Xcℓν factors are equal to 1 as expected. However,1577
as the data-MC disagreement is large in the control region as illustrated in Fig. 35, the as-1578
sociated uncertainties are expected to be different from what is obtained from the Asimov fit.1579
1580
In order to get a more realistic expectation of the B → Xcℓν shape factor values and1581
their associated uncertainties, we perform a fit using data in the control region and pseudo-1582
data in the signal region. In order to create realistic pseudo-data yields, we use bin-by-bin1583
data-MC ratio factors obtained from CRK,high. These factors are then multiplied to the MC1584
B → Xcℓν component yields in the signal region. The obtained signal region pseudo-data1585
yields are therefore obtained by summing up the signal region MC yields of the signal and1586
other-backgrounds components together with the Xcℓν MC yields scaled by the data-MC1587
ratio obtained from the control region. The resulting pre-fit data and MC distributions are1588
shown in Fig. 51.1589
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
```
FIG. 51: Pre-fit pBℓ :q2 distributions in the signal (left) and control (right) regions. Data is
```
used in the control region and pseudo-data in the signal region.
The B → Xcℓν shape is corrected in the fit as one single component. However, its com-1590
position is different between the signal and control region as can be seen from Table XIII.1591
Because of these differences, the shape factors extracted in the simultaneous fit don’t nec-1592
essarily translate perfectly from one region to the other as every charm component could1593
induce different sources of data-MC disagreement. We consider an additional uncertainty to1594
cover these differences. The procedure is described in this Section. Effectively, the bin-by-bin1595
composition of the Xcℓν component as well as the shapes of each individual sub-component1596
are different between the signal region and CR0,low which makes it extremely tedious to1597
properly estimate an uncertainty. Nevertheless, we assume that the total uncertainty ob-1598
tained from the fit and the additional composition systematic cover most of uncertainty1599
related to the differences between the signal and control region B → Xcℓν component.1600
1601
In order to estimate the uncertainty related to the compositions, we perform two fits1602
and compare the resulting B → Xuℓν branching fraction. In the first fit, data is used in the1603
82
control region and pseudo-data in the signal region as described above. In the second fit,1604
we use the same MC and data yields in the signal region and the same data yields in the1605
control region as in the first fit. However, in the control region, the Xcℓν sub-components1606
are scaled such that the composition matches the signal region composition. A comparison1607
of the shape of the Xcℓν component with and without this scaling is shown in Figure 52. A1608
comparison of the resulting pre-fit scaled pBℓ :q2 distributions are shown in Fig. 53. In order1609
to illustrate the procedure, we compare below the results from these two fits performed1610
```
with the phase-space and experimental selections defined for Fit 1 (pBℓ > 1.0 GeV for both1611
```
```
selections, c.f. Section 8 5). After unblinding, we plan to repeat this procedure for every1612
```
fit discussed above using data both in the signal and control region. The B → Xcℓν shape1613
factors obtained from the two fits together with their uncertainties are shown in Fig. 54.1614
```
The B(B → Xuℓν) obtained are also compared in Tab. XXV. The difference can then be1615
```
```
added as an additional uncertainty (which assumes no correlation between this uncertainty1616
```
```
and the total uncertainty). The test will be repeated with data in the signal region.1617
```
0 5 10 15 20 25q2 [GeV2]0
5000
10000
15000
20000
25000
30000
35000
B Xc , CR0, low
NominalScaled
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75pB [GeV]0
2500
5000
7500
10000
12500
15000
17500
B Xc , CR0, low
NominalScaled
```
FIG. 52: Comparison of the q2 (left) and pBℓ (right) distributions in CR0,low of Xcℓν events
```
before and after the Xcℓν sub-component composition scaling described in the text.
Variable pBℓ :q2
Unscaled Xcℓν 1.52 ± 0.13
Scaled Xcℓν 1.49 ± 0.13
TABLE XXV: Branching fractions obtained from the pBℓ :q2 fit in the pBℓ > 1.0 GeV region
using pseudo-data. The branching fractions obtained with the scaled and unscaled Xcℓν
component are compared. See text for more details.
9. |Vub| measurement1618
```
Once the partial branching fraction ∆B(B → Xuℓν) has been measured, one can derive the1619
```
amplitude of Vub via:1620
|Vub| =
s
```
∆B(B → Xuℓν)
```
```
τB · ∆Γ(B → Xuℓν)
```
```
, (15)
```
83
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
```
FIG. 53: Pre-fit pBℓ :q2 distributions in the signal (left) and control (right) regions. Data is
```
used in the control region and pseudo-data in the signal region. The B → Xcℓν MC yields
in the control region have been scaled as described in the text.
where τB = 1.579 ± 0.003 ps is the average charged/neutral B meson lifetime [3] and1621
```
∆Γ(B → Xuℓν) is the theoretical partial decay rate without |Vub|.1622
```
1623
```
The decay rates for different models are extracted from previous measurements of ∆B(B →1624
```
```
Xuℓν) and the most recent HFLAV averages of |Vub| (see Tables 94 and 95 in [54])6. Four1625
```
inclusive models are considered: BLNP [6], GGOU [55], DGE [56] and ADFR [57]. The1626
decay rates for the pBℓ > 1.0 GeV region are summarised in Tab. XXVI.1627
Phase-space region BLNP GGOU DGE ADFR
pBℓ > 1.0 GeV 63.0+7.2−5.6 60.8+3.1−2.6 59.3+3.9−3.3 61.4+6.2−5.4
TABLE XXVI: Partial decay rates ∆Γ for different models. Numbers are given in ps−1.
Using the partial branching fraction obtained from the q2 fit in the pBℓ > 1.0 GeV region1628
```
(Tab. XVIII) and Equ. 15, we can therefore extract a value of |Vub| for each model quoted1629
```
above. These are summarised in Tab. XXVII.1630
Phase-space region BLNP GGOU DGE ADFR
pBℓ > 1.0 GeV 4.01 ± 0.10 ± 0.14+0.23−0.18 4.08 ± 0.10 ± 0.14+0.10−0.09 4.13 ± 0.10 ± 0.14+0.14−0.12 4.06 ± 0.10 ± 0.14+0.20−0.18
TABLE XXVII: |Vub| × 103 for different models using the branching fraction extracted
from a q2 fit with the experimental and phase-space selections of Fit 1. The quoted
uncertainties are statistical, systematic and theoretical respectively.
6 The numbers used to extracted the values of |Vub| quoted here were taken from the most recent HFLAV
paper which is yet to be published.
84
0 2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.6
0.7
0.8
0.9
1.0
1.1
1.2
B Xc correction factors
Shape factors
Shape factors, scaled Xc
0 2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.85
0.90
0.95
1.00
1.05
1.10
1.15
B Xc correction factors
Shape factors
Shape factors, scaled Xc
FIG. 54: The B → Xcℓν shape factors obtained from the fits using pseudo-data. The cyan
points correspond to the fit where the B → Xcℓν yields have been scaled as described in
the text. The bottom plot shows the same shape factors normalised to the factors obtained
from the fit where B → Xcℓν is left unscaled.
85
10. Fits with control regions1631
1. Fit with CR0,low split1632
We perform the fit procedure using CR0,low only. This region is split in two based on the1633
Xcℓν MVA score: one with a score lower than 0.45 and one with a score between 0.45 and1634
0.60. We will call these two regions CR’0,low and VR’2 respectively. The former is used as1635
the control region in the fit and the latter as the signal region. We illustrate the test in1636
this Section for fit 1. Plots for fit 3 and 5 are shown in Appendix I Fit 7 uses the same1637
kinematical cuts as fit 1 and only the signal phase-space selection is different. The Xcℓν1638
background correction being unchanged, we do not repeat the test for fit 7.1639
1640
The signal purity in CR0,low is about 1.50% as shown in Table XIII. The normalisation1641
of the Xcℓν component in both regions is extracted exactly as described in Section 7 3 2 and1642
the fit procedure is performed exactly as described in Section 8. Using data and MC, the1643
```
normalisation in CR’0,low is found to be 1.11 ± 0.05 (stat.) and in VR’2, 1.06 ± 0.01 (stat.).1644
```
Using the ABCD method, the normalisation in VR’2 is found to be 1.08 ± 0.04 where the1645
error is the uncertainty covering all sources described in Section 7 3 2.1646
1647
As illustrated in Figure 55, the fit captures well the B → Xcℓν shape in both regions1648
which is confirmed by the obtained p-value of 0.99. We compare the output Xcℓν scale1649
factors with the Xcℓν data/MC ratios for regions CR’0,low and VR’2 in Figure 56.1650
2. Fit with CRK,low and CRK,high1651
We also repeat the fit procedure using the two control regions where the presence of at least1652
one kaon is required. The goal of this test is to confirm that the shape of Xcℓν as corrected1653
in the low MVA region can reliably correct the Xcℓν component in the high MVA score1654
region. We use CRK,low as CR and CRK,high as SR. In this case, the Xcℓν normalisations1655
are taken directly from MC. We respectively find 1.04 ± 0.04 and 0.95 ± 0.05, where the1656
total uncertainty is obtained from the statistical uncertainty and the non-Xcℓν component1657
variation. The pre and post-fit distributions for pBℓ :q2 with the fit 1 setup are illustrated in1658
Figures 57. A p-value of 0.60 is obtained. The NP pulls of this fit are shown in Figure 58.1659
The B → Xcℓν shape factors extracted from the fit are compared with data/MC ratios in1660
the two regions from the fit in Figure 59. The fit is projected onto q2 and EBℓ as shown in1661
Figure 60. The CRK,low-CRK,high fit is projected onto EBℓ :q2 with the Xcℓν template broken1662
down in subcomponents in order to compare the pre and postfit Xcℓν compositions. The1663
comparison is summarised in Table XXVIII.16641665166616671668
CRK,high B → Dℓν B → D∗ℓν B → D∗∗ℓν B → D∗∗Gapℓν
Prefit 40.4% 47.3% 6.2% 6.1%
Postfit 40.2% 49.2% 6.0% 4.6%
TABLE XXVIII: Composition changes slightly except for the gap modes which, as the NP
pulls show, are reduced.1669
1670
86
0
1000
2000
3000
4000
5000
6000
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
1000
2000
3000
4000
5000
6000
events
signal
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
```
FIG. 55: Pre- (left) and post-fit (right) pBℓ :q2 distributions in VR’2 (top) and CR’0,low
```
```
(bottom) for fit 1.
```
3. Fit with CR0,low and CRK,high1671
We also repeat the fit procedure using the two control regions CR0,low as CR and CRK,high1672
as SR. This represents a cross-check of the previous CRK,low-CRK,high test. In this case,1673
the Xcℓν normalisations are taken directly from MC. We respectively find 1.11 ± 0.05 and1674
0.95 ± 0.05, where the total uncertainty is obtained from the statistical uncertainty and the1675
non-Xcℓν component variation. The pre and post-fit distributions for EBℓ :q2 with the fit 11676
setup are illustrated in Figures 61. A p-value of 0.44 is obtained. The NP pulls of this fit1677
are shown in Figure 62.1678
87
0 2 4 6 8 10 12pB : q2 [GeV:GeV2]
0.7
0.8
0.9
1.0
1.1
Data/MC ratio
CR'0, lowVR'2
Fit output
FIG. 56: Comparison between the normalised Xcℓν data/MC ratio for regions CR’0,low and
VR’2 and the fit output Xcℓν shape factors.
11. Split sample fits1679
With the current fit setup, one can split the signal and control region in order to perform1680
a simultaneous fit of specific decay channels. In this Section, we discuss a simultaneous fit1681
of the B+ and B0 channels as well as the B → eℓν and B → µℓν channels. We also discuss1682
additional split fits used as cross-checks of our fit setup.1683
1. Fit with split B charge: ∆B(B0 → Xuℓν), ∆B(B± → Xuℓν)1684
Before performing the signal extraction for the B+ and B0 channels split in two different1685
channels, we must evaluate and, if necessary, correct the crossfeed between the charged1686
and neutral B channels. This is of particular relevance in our fit setup as the crossfeed1687
rate in B → Xcℓν events has an impact on the normalisation and shape corrections of this1688
component. The crossfeed for all events in CR0,low and SR is shown in Figure 63. The1689
crossfeed for Xu events in the SR is shown in Figure 64. The crossfeed for signal events1690
in the SR is relatively low and one could simply correct the extracted BR for B+ and B01691
using the crossfeed rate of each B charge. However, the crossfeed rate for B → Xcℓν events1692
appears to be larger both in the CR and the SR. It also appears to be different between the1693
two regions. As the normalisation and shape corrections are also extracted separately for1694
each channel, one would need to carefully treat the crossfeed between charged and neutral1695
B mesons. Given the complexity of properly correcting the crossfeed we have decided to not1696
perform the measurement for split B charge.1697
2. Fit with split lepton flavour: ∆B(B → Xueν), ∆B(B → Xuµν)1698
The crossfeed between the electron and muon channels is negligible. We could extract the1699
two separate branching fractions using the setup of fit 1. However, after further checking, it1700
was noticed that the normalisation of the signal component in the electron channel is biased.1701
Fixing the ”other background” yields in the electron channel doesn’t fix the bias so the e/µ1702
88
0
100
200
300
400
500
600
700
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
100
200
300
400
500
600
700
events
signal
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
```
FIG. 57: Pre- (left) and post-fit (right) q2 distributions in CRK,high (top) and CRK,low
```
```
(bottom) for fit 1.
```
split is left as cross-check where each channel is fitted separately.1703
e µ
CR0,low 1.13 ± 0.04 1.10 ± 0.07
SR 1.00 ± 0.08 1.03 ± 0.09
TABLE XXIX: Xcℓν normalisation factors for the e/µ split fit.
89
FEI_B0FEI_BpSlow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Tracking
bf_B0toDetalnubf_B0toDlnubf_B0toDonelnubf_B0toDoneprimelnubf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnubf_BptoDstzerolnu
2
0
2
```
(
```
```
) /
```
bf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]
kaonIDleptonID[0]leptonID[1]leptonID[2]leptonID[3]DFN[1]DFN[2]HybridModelbf_B0toXulnubf_B0topilnu
bf_B0torholnubf_BptoXulnu
2
0
2
```
(
```
```
) /
```
bf_Bptoetalnubf_Bptoetaprimelnubf_Bptoomegalnubf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]ff_Rho[4]ff_Rho[5]
2
0
2
```
(
```
```
) /
```
ff_Rho[6]ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaSCont.Norm.[0]Cont.Norm.[1]
Cont.Reweight[0]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]Cont.Reweight[4]mu_sideband_Xclnumu_other_bkgmu_signal_XclnuMCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsideband[10]MCStatsideband[11]MCStatsignal[0]MCStatsignal[1]MCStatsignal[2]
2
0
2
```
(
```
```
) /
```
MCStatsignal[3]MCStatsignal[4]MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]MCStatsignal[10]MCStatsignal[11]
2
0
2
```
(
```
```
) /
```
FIG. 58: Pull plot of the CRK,low-CRK,high fit with EBℓ :q2.
3. Additional split sample fits: split missing momentum θ angle and split lepton charge1704
Fit 1 is repeated with the SR and CR region split in two using the missing momentum polar1705
angle, θmiss. The cut splitting the two samples is set at π/2. We show the θmiss distribution1706
in SR and CR0,low in Figure 65. As this fit is meant as a cross-check rather than a physics1707
result, each of the two channels is fitted separately. The Xcℓν component is normalised in1708
the SR and CR separately following the ABCD method discussed in Section 7 3 2. We repeat1709
```
the same split fits using the lepton charge (positive vs negative). We perform Asimov fits1710
```
with these setups as well as the unblinded fit using regions CR’0,low and VR’2. The results of1711
all fits look satisfying and we propose to perform these fits with an unblinded signal region1712
during the box opening procedure in order to cross-check the stability of our fit setup.1713
90
0 2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.8
0.9
1.0
1.1
1.2
1.3
1.4
Xc Data/MC ratio
CRK, low
CRK, high
Fit factors
FIG. 59: Xcℓν shape factors as extracted from the CRK,low-CRK,high fit with EBℓ :q2
compared to the data/MC ratios in these two regions. As expected, the shape factors
match the CRK,low data/MC ratios.
91
0
5000
10000
15000
20000
25000
30000
35000
events
ControlRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7 8 9bin0.68
0.84
1.0
1.16
1.32
data / model
0
200
400
600
800
1000
1200
events
SignalRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7 8 9bin0.68
0.84
1.0
1.16
1.32
data / model
0
2500
5000
7500
10000
12500
15000
17500
events
ControlRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 2 4 6 8 10 12bin0.68
0.84
1.0
1.16
1.32
data / model
0
100
200
300
400
500
600
events
SignalRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 2 4 6 8 10 12bin0.68
0.84
1.0
1.16
1.32
data / model
FIG. 60: Postfit projections of the EBℓ :q2 CRK,low-CRK,high fit on q2 and EBℓ . SignalRegion
denotes CRK,high and ControlRegion CRK,low.
92
0
100
200
300
400
500
600
700
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
100
200
300
400
500
600
700
events
signal
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
2 4 6 8 10 12
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
```
FIG. 61: Pre- (left) and post-fit (right) EBℓ :q2 distributions in CRK,high (top) and CR0,low
```
```
(bottom) for fit 1.
```
93
FEI_B0FEI_BpSlow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Tracking
bf_B0toDetalnubf_B0toDlnubf_B0toDonelnubf_B0toDoneprimelnubf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnubf_BptoDstzerolnu
2
0
2
```
(
```
```
) /
```
bf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]leptonID[0]leptonID[1]leptonID[2]leptonID[3]
DFN[1]DFN[2]HybridModelbf_B0toXulnubf_B0topilnu
bf_B0torholnubf_BptoXulnubf_Bptoetalnu
2
0
2
```
(
```
```
) /
```
bf_Bptoetaprimelnubf_Bptoomegalnu
bf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]ff_Rho[4]ff_Rho[5]ff_Rho[6]
2
0
2
```
(
```
```
) /
```
ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaSCont.Norm.[0]Cont.Norm.[1]
Cont.Reweight[0]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]mu_sideband_Xclnumu_other_bkgmu_signal_XclnuMCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsideband[10]MCStatsideband[11]MCStatsignal[0]MCStatsignal[1]MCStatsignal[2]MCStatsignal[3]MCStatsignal[4]
2
0
2
```
(
```
```
) /
```
MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]MCStatsignal[10]MCStatsignal[11]
2
0
2
```
(
```
```
) /
```
FIG. 62: Pull plot of the CR0,low-CRK,high fit with pBℓ :q2.
94
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
1000
2000
3000
4000
5000
6000
7000
```
crossfeed = 12.7%
```
B0
B + B +B0 B0
B + B0B0 B +
Continuum
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
2000
4000
6000
8000
10000
12000
```
crossfeed = 10.7%
```
B±
B + B +B0 B0
B + B0B0 B +
Continuum
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
20
40
60
80
100
120
140
160
```
crossfeed = 9.4%
```
B0
B + B +B0 B0
B + B0B0 B +
Continuum
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
100
200
300
400
```
crossfeed = 4.4%
```
B±
B + B +B0 B0
B + B0B0 B +
Continuum
```
FIG. 63: pBℓ in CR0,low (top) and SR (bottom) for the neutral (left) and charged (right)
```
channels.
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
10
20
30
40
50
60
```
crossfeed = 4.1%
```
B0
B + B +B0 B0
B + B0B0 B +
Continuum
0.0 0.5 1.0 1.5 2.0 2.5pB [GeV]0
20
40
60
80
100
```
crossfeed = 3.3%
```
B±
B + B +B0 B0
B + B0B0 B +
Continuum
```
FIG. 64: pBℓ for B → Xuℓν events in the SR for the neutral (left) and charged (right)
```
channels.
95
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8
miss [rad]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.052 rad)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Asimov Data
pB > 1 GeV, Signal region
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8
miss [rad]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.063 rad)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV,
```
FIG. 65: θmiss distribution in SR (left) and CR0,low (right)
```
96
9. BOX OPENING1714
1. Proposed unblinding strategy1715
• Perform all fits using CR0,low and VR2 instead of SR in order to validate the background1716
correction and signal extraction procedures with the validation region closest to the1717
signal region1718
• Unbox the signal region, check the data-MC agreement on the following variables1719
```
(combined and split e, µ modes): EBℓ , q2, MX , M 2miss and Mbc; check the total efficiency1720
```
```
of the SR in data as discussed in Section 7; check the normalisation of the signal-1721
```
```
dominated region (EBℓ > 2.1 GeV) to make sure that the signal normalisation is1722
```
```
consistent between MC and data within uncertainties; check the ratio of yields in the1723
```
nominal sample and the low FEI cut sample in MC and data in the signal region1724
```
• Perform nominal fit (fit 1), keep branching fractions and |Vub| blinded, compare pre-fit1725
```
and post-fit spectra and check output p-value, nuisance parameter pulls as well as1726
```
total uncertainty; perform fit 1 separately in each split channel (θmiss, lepton charge1727
```
```
and flavour) and check the difference between each BR by adding an unknown factor1728
```
```
to both results to keep them blinded; use post-fit charged π multiplicity to derive an1729
```
additional uncertainty on the Xu system hadronisation1730
• Fully unblind BR and |Vub| obtained from the nominal fit. Perform fits 3 and 5 and1731
all associated cross-checks.1732
2. Step 1: CR0,low - VR2 fit1733
For all three fits, the CR0,low Xcℓν normalisation is extracted by directly comparing MC and1734
data and the VR2 normalisation is extracted via the ABCD method described in Section 7 3 2.1735
The normalisation factors obtained for the three regions considered in our fits are summarised1736
in Table XXX.1737
Kinematic selection CR0,low VR2
pBℓ > 1.0 GeV 1.11 ± 0.05 1.07 ± 0.07
pBℓ > 1.0 GeV, MX < 1.7 GeV 1.18 ± 0.04 1.15 ± 0.05
pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2 1.24 ± 0.03 1.22 ± 0.07
TABLE XXX: CR0,low and VR2 Xcℓν normalisation factors for different kinematic
selections.1738
1739
The pre and postfit distributions of fit 1 are shown in Figure 66. The pulls are shown in1740
Figure 67. The normalised prefit Xcℓν data/MC ratios in CR0,low and VR2 are compared1741
to the fit Xcℓν shape factors in Figure 68. The pre and postfit projections on q2, EBℓ and1742
MX in the VR2 region which is used as signal region in this setup are shown in Figure 69.1743
For the three fits, we respectively obtain a p-value of 0.31, 0.35 and 0.53. The plots for fits1744
3 and 5 are shown in Appendix Q.1745
97
0
1000
2000
3000
4000
5000
events
VR2
pre-fit
Other bkg.
Xc
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
1000
2000
3000
4000
5000
events
VR2
post-fit
Other bkg.
Xc
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
10000
20000
30000
40000
events
CR0, low
pre-fit
Other bkg.
Xc
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
10000
20000
30000
40000
events
CR0, low
post-fit
Other bkg.
Xc
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
FIG. 66: Pre and postfit EBℓ :q2 distributions of the CR0,low - VR2 fit 1.
98
FEI_B0FEI_BpKshortVeto
Slow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Trackingbf_B0toDetalnubf_B0toDlnubf_B0toDonelnu
bf_B0toDoneprimelnu
bf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnu
2
0
2
```
(
```
```
) /
```
bf_BptoDstzerolnubf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]kaonIDVeto[0]kaonIDVeto[1]leptonID[0]leptonID[1]leptonID[2]leptonID[3]
DFN[1]DFN[2]
HybridModelbf_B0toXulnubf_B0topilnu
2
0
2
```
(
```
```
) /
```
bf_B0torholnubf_BptoXulnubf_Bptoetalnu
bf_Bptoetaprimelnubf_Bptoomegalnu
bf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]
2
0
2
```
(
```
```
) /
```
ff_Rho[4]ff_Rho[5]ff_Rho[6]ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaS
Cont.Norm.[0]Cont.Norm.[1]Cont.Reweight[0]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]Cont.Reweight[4]Cont.Reweight[5]
mu_sideband_Xclnu
mu_other_bkgmu_signal_Xclnu
MCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsideband[10]MCStatsideband[11]
2
0
2
```
(
```
```
) /
```
MCStatsignal[0]MCStatsignal[1]MCStatsignal[2]MCStatsignal[3]MCStatsignal[4]MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]MCStatsignal[10]MCStatsignal[11]
2
0
2
```
(
```
```
) /
```
FIG. 67: CR0,low - VR2 fit 1 nuisance parameter pulls
99
0 2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.5
0.6
0.7
0.8
0.9
1.0
1.1
1.2
Xc Data/MC ratio
CR0, low
VR2
Fit factors
```
FIG. 68: Comparison of the normalised prefit (fit 1) Xcℓν data/MC ratios in CR0,low and
```
VR2 with statistical uncertainties and Xcℓν shape factors with full fit uncertainties.
100
0
2000
4000
6000
8000
events
VR2pre-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
events
VR2post-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.68
0.84
1.0
1.16
1.32
data / model
0
1000
2000
3000
4000
5000
events
VR2pre-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.68
0.84
1.0
1.16
1.32
data / model
0
1000
2000
3000
4000
5000
events
VR2post-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
VR2pre-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
0.0 0.5 1.0 1.5 2.0 2.5 3.0MX [GeV]0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
VR2post-fitother_bkgXulnu_in
Xclnu[9]Xclnu[8]
Xclnu[7]Xclnu[6]
Xclnu[5]Xclnu[4]
Xclnu[3]Xclnu[2]
Xclnu[1]Xclnu[11]
Xclnu[10]Xclnu[0]
UncertaintyData
0.0 0.5 1.0 1.5 2.0 2.5 3.0MX [GeV]0.68
0.84
1.0
1.16
1.32
data / model
FIG. 69: Projections of the EBℓ :q2 fit 1 on EBℓ , q2 and MX .
101
3. Step 2: signal region plots and first checks1746
We show in Figure 70 distributions of EBℓ , q2, MX , 2D EBℓ :q2, M 2miss and Mbc in the signal1747
region. We add the signal region distributions split in lepton flavour and the distributions1748
in the regions considered for fit 3 and 5 in Appendix R.1749
1750
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 12.1/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.1 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
0 3 6 9 12 15 18 21 24q2 [GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 12.4/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (1 GeV
```
```
2)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0EB : q2 [GeV:GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 12.6/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (1 GeV:GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2MX [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 18.9/11
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
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
Events / (0.3 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0M2
miss [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 11.0/8
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.5 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
5.2700 5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900mbc [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 87.4/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.001 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Uncert.
Data
EB > 1 GeV, SR
FIG. 70: Signal region distributions.1751
1752
As shown in Table XV, the SR normalisation is expected to be close to 1 which is clearly not1753
the case. A setup mimicking the nominal fit setup is created using the CRK,low – CRK,high1754
setup and injecting the SR MC Xuℓν yields in MC and data in CRK,high. This setup allows1755
102
to control the normalisation of the signal injected in data while keeping the MC normali-1756
sation fixed and to control the normalisation of the Xcℓν template while keeping the data1757
normalisation fixed. After careful investigation, two sources of bias in the fit were identified:1758
```
first, the small differences in data/MC ratio shape between CRK,low (CR0,low) and CRK,high1759
```
```
(SR) which lead to an imperfect correction of the Xcℓν template in SR thus forcing the1760
```
fit to pull on the signal normalisation to adjust the mismatch and second, the difference1761
between the ABCD-extracted Xcℓν normalisation and the observed SR normalisation. A1762
correction for the first bias is extracted by varying the normalisation of the signal injected in1763
data in CRK,high choosing values in [0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15]. The output nor-1764
malisations of these different tests are compared to the input normalisations. The resulting1765
distribution shown in Figure 71 is linear and the fitted curve is used to correct the normal-1766
isation. The B → Xuℓν branching fraction obtained from the fit will therefore be corrected1767
```
by f (x) = (x − 0.052)/0.920.1768
```
1769
0.85 0.90 0.95 1.00 1.05 1.10 1.15 1.20 1.25
Injected signal normalisation
0.85
0.90
0.95
1.00
1.05
1.10
Measured normalisation
```
( 0.920±0.008) in+(0.052±0.008)
```
FIG. 71: Distribution of output vs input normalisations of the signal injected CRK,low –
CRK,high fit setup described in the text.1770
1771
Since the correction factor is extracted from a specific setup, we need to derive an uncer-1772
tainty related to the correction. For that, we repeat the signal-injected fit using 1,000 toys1773
which are created by Gaussian-varying the data yields in CRK,high within their statistical1774
uncertainties. This allows to test different configurations of the fit setup used to extract1775
the bias correction instead of relying on a single setup. This test is repeated for different1776
```
Xuℓν input normalisations in the same set of normalisations as above ([0.85, ..., 1.15]) and1777
```
for each test we plot the resulting distribution of 1,000 output normalisations as illustrated1778
in Figure 72. The spread of the Gaussian distribution is between 0.022 and 0.023 for each1779
input normalisation which corresponds to 2.0% to 2.5% relatively to the central value of1780
the distribution. We use this spread to quantify the uncertainty related to the correction1781
procedure and we therefore assign a flat 2.5% uncertainty.1782
103
1783
0.875 0.900 0.925 0.950 0.975 1.000 1.025 1.050 1.075
```
( in)/
```
0
10
20
30
40
50
Trials
```
G = 0.9699±0.0007
```
```
G = 0.0225±0.0005
```
FIG. 72: Distribution of output normalisations with 1,000 toys created by varying the data
yields in CRK,high within their statistical uncertainties. The normalisation of the signal
injected in data is chosen to be 1.1784
1785
The correction for the bias coming from overestimating the Xcℓν normalisation is estimated1786
by keeping the input signal normalisation fixed 1 in MC and data and scaling the Xcℓν1787
template in CRK,high in the signal-injected setup by different overestimation factors and1788
comparing them to the output signal normalisation. Again, the response is linear as shown1789
in Figure 73. It is however impossible to estimate the actual normalisation of the Xcℓν1790
component in the true SR where the signal yields correspond to about a third of all events.1791
The data/MC ratio in the signal region is ∼ 0.88 and we therefore derive a correction factor1792
using the linear response assuming an overestimation factor of 1.15. The resulting flat1793
```
correction factor is therefore 1/(−0.167 × 1.15 + 1.166) ∼ 1.026. The full difference between1794
```
the corrected value and the non-corrected value is added as an uncertainty. We check that1795
this uncertainty is large enough to cover the true signal normalisation even if the true Xcℓν1796
overestimation factor is very different from 1.15 as illustrated in Figure 74.1797
179817991800
Finally, since we use the CRK,low and CRK,high regions to perform all these tests, we derive an1801
additional uncertainty to cover the small difference in Xcℓν composition between these two1802
control regions and CR0,low and SR. To do that, we repeat the signal-injected fit setup with1803
Xuℓν and Xcℓν normalisations fixed to 1 by rescaling the Xcℓν template subcomponents1804
```
in CRK,low (resp. CRK,high) such that its composition matches the composition in CR0,low1805
```
```
(resp. SR). The difference with the nominal setup normalisation is taken as an uncertainty1806
```
resulting in an additional 1.4% error. Such a procedure was used to derive an uncertainty1807
on the difference in SR and CR0,low Xcℓν compositions as described in Section 8 8. The1808
latter uncertainty is removed to avoid double-counting errors related to the composition of1809
Xcℓν.1810
104
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
0.940
0.945
0.950
0.955
0.960
0.965
0.970
```
Measured signal normalisation(-0.154±0.013) in+(1.125±0.014)
```
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
0.965
0.970
0.975
0.980
0.985
0.990
0.995
1.000
```
Measured signal normalisation(-0.167±0.014) in+(1.167±0.016)
```
FIG. 73: Distribution of output signal normalisations vs Xcℓν overestimation factor in the
signal injected CRK,low – CRK,high fit setup described in the text. In the right-hand plot,
the first source of bias described above has been corrected for. The normalisation of the
injected signal is equal to 1.
1.00 1.05 1.10 1.15 1.20 1.25 1.30B Xc overestimation factor
0.96
0.98
1.00
1.02
1.04
Output corrected signal normalisation
FIG. 74: Output signal normalisation corrected by the two corrections described in the
text vs different Xcℓν overestimation factors. The uncertainty is the one added for the
second source of bias.
1811
The procedure described above is summarised as follows:1812
• remove the composition uncertainty described in Section 8 81813
• correct for the bias coming from the data/MC ratio mismatch between CR and SR1814
```
using f (x) = (x − 0.052)/0.9201815
```
• add a 2.6% uncertainty on the corrected normalisation based on the tests performed1816
by varying the datasets used to extract the correction factor1817
• add a 1.4% uncertainty based on the small composition difference between CRK,high/SR1818
and CRK,low/CR0,low1819
• correct for the bias coming from the overestimation of the Xcℓν normalisation in the1820
SR using a flat correction factor of 1.026 and add the difference as an uncertainty1821
105
We give in the following an example with a measured normalisation of 0.952 and a total1822
```
uncertainty of 8.0% (see Table XXIV):1823
```
```
• Initial ∆B(B → Xuℓν) = (1.504 ± 0.120) × 10−31824
```
```
• Apply first correction and add related uncertainty: ∆B(B → Xuℓν) = (1.546±0.136)×1825
```
10−31826
```
• Add composition uncertainty: ∆B(B → Xuℓν) = (1.546 ± 0.138) × 10−31827
```
```
• Correct for second bias and add uncertainty: ∆B(B → Xuℓν) = (1.588 ± 0.148) × 10−31828
```
This results in a total relative uncertainty of 9.3% to which only the Xu hadronisation mod-1829
```
elling uncertainty needs to be added (see Section 6 14). For reference, the Xuℓν branching1830
```
fraction measured by Belle had an uncertainty of 11.0%. We repeated the same procedure1831
for fits 3 and 5 i.e. with additional cuts of MX < 1.7 GeV and MX < 1.7 GeV, q2 > 8 GeV21832
respectively. All related plots are shown in Appendix S. The procedure for fit 3 outlines as1833
```
follows:1834
```
• remove the composition uncertainty described in Section 8 81835
• correct for the bias coming from the data/MC ratio mismatch between CR and SR1836
```
using f (x) = (x − 0.025)/0.9881837
```
• add a 2.3% uncertainty on the corrected normalisation based on the tests performed1838
by varying the datasets used to extract the correction factor1839
• add a 5.7% uncertainty based on the composition difference between CRK,high/SR and1840
CRK,low/CR0,low1841
• correct for the bias coming from the overestimation of the Xcℓν normalisation in the1842
SR using a flat correction factor of 1.004 and add the difference as an uncertainty1843
In general, the corrections and uncertainties added are smaller than for fit 1 owing to a1844
larger signal purity and good signal modelling. However, the Xcℓν composition difference1845
between CRK,high and SR is quite large as summarised in Table XXXI. Because of that,1846
the composition uncertainty becomes the leading uncertainty bringing the total relative1847
uncertainty from 7.7% to about 10% to be compared with an 8.7% uncertainty quoted by1848
Belle for the same phase-space region. For fit 5, the correction procedure outlines as follows:1849
CRK,low CRK,high CR0,low Signal
B → Dℓν 22.05% 64.3% 21.5% 47.7%
B → D∗ℓν 65.32% 33.6% 61.9% 47.3%
B → D∗∗ℓν 6.43% 1.5% 8.0% 2.7%
B → D∗∗Gapℓν 6.30% 0.6% 8.6% 2.3%
TABLE XXXI: Composition of the Xcℓν component in various background regions and the
signal region with an additional cut of MX < 1.7 GeV.1850
1851
• remove the composition uncertainty described in Section 8 81852
106
• correct for the bias coming from the data/MC ratio mismatch between CR and SR1853
```
using f (x) = (x − 0.050)/0.9571854
```
• add a 1.8% uncertainty on the corrected normalisation based on the tests performed1855
by varying the datasets used to extract the correction factor1856
• add a 0.2% uncertainty based on the composition difference between CRK,high/SR and1857
CRK,low/CR0,low1858
• correct for the bias coming from the overestimation of the Xcℓν normalisation in the1859
SR using a flat correction factor of 1.013 and add the difference as an uncertainty1860
In this case, the Xcℓν component also has a small impact. Besides, its composition doesn’t1861
impact the EBℓ variable used for the fit. These additional uncertainties bring the total1862
relative uncertainty from 9.1% to 9.9% to be compared with an uncertainty of 18% quoted1863
by the Belle measurement in this phase-space region.1864
1865
As part of the second unblinding step, we also need to compare the total efficiency of1866
the SR selection in MC and data. As discussed above, the efficiency in MC doesn’t match1867
the data efficiency but the resulting bias is corrected. The data and MC distributions in1868
the signal-dominated region is very similar which indicates a relatively good modelling of1869
B → Xuℓν processes. We finally check the ratio of yields in the nominal sample and the1870
low FEI cut sample in MC and data in the signal region. The ratio is 0.648 ± 0.026 in MC1871
and 0.649 ± 0.011 in data indicating a very good agreement.1872
4. Final unboxing step: perform the three nominal fits1873
We perform the 3 fits. The pre and post-fit distributions are shown in Figures 75 and 761874
respectively. For fits 1, 3 and 5 we respectively find p-values of 0.79, 0.20 ans 0.84 confirming1875
the good agreement.187618771878
1879
The pulls of all nuisance parameters are shown in Figures 77 to 79. In each fit, all pulls are1880
within one standard deviation indicating that they are stable and yield reliable results. As1881
expected, the B → Xcℓν normalisation parameter in the signal region pulls significantly to1882
adjust the overestimated normalisation of this component.1883188418851886
1887
The event yields as extracted from fits 1, 3 and 5 are given in Table XXXII. In the1888
two regions considered for fits 1 and 3, the signal yields are similar to those reported in the1889
latest Belle measurement [58] while the background yields are approximately 30–45% lower,1890
despite using a data set that is about half the size of the 711 fb−1 data set collected by the1891
Belle detector.18921893
1894
Before applying all post-fit corrections and adding all post-fit uncertainties, the signal1895
normalisations are1896
```
• fit 1: 0.926 ± 0.076 (8.2% relative uncertainty)1897
```
```
• fit 3: 0.928 ± 0.081 (8.7%)1898
```
107
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
Events
×104Other backgrounds
XcXu
UncertaintyData
```
EB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
CR0, lowEB > 1 GeV
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
Events
×104Other backgrounds
B XcB Xu out
B Xu inUncertainty
```
DataEB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
CR0, lowEB > 1 GeV
MX < 1.7 GeV
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
Events
×104Other backgrounds
B XcB Xu out
B Xu inUncertainty
Data
CR0, lowEB > 1 GeV
MX < 1.7 GeVq2 > 8 GeV2
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Events
×103Other backgrounds
XcXu
UncertaintyData
```
EB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
SREB > 1 GeV
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Events
×103Other backgrounds
B XcB Xu out
B Xu inUncertainty
```
DataEB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
SREB > 1 GeV
MX < 1.7 GeV
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.75
1.001.25
Data/MC0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
2.00
4.00
6.00
8.00
Events
×102Other backgrounds
B XcB Xu out
B Xu inUncertainty
Data
SREB > 1 GeV
MX < 1.7 GeVq2 > 8 GeV2
```
FIG. 75: The EBℓ :q2 and EBℓ distributions in data and simulated data in CR0,low (top) and
```
```
the signal region (bottom) considered for fit 1 (left), 3 (middle) and 5 (right). The EBℓ :q2
```
```
distribution is shown in bins of EBℓ (in GeV) and q2 as indicated in the figures. The
```
```
B → Xcℓν normalisation correction factors have been applied (see Table XV).
```
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]1.00
0.00
1.00
Pull
2/d. o. f = 0.0/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
Events
×104Other backgrounds
XcXu
UncertaintyData
```
EB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
CR0, lowEB > 1 GeV
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]2.00
0.002.00Pull 2/d. o. f = 0.0/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
Events
×104Other backgrounds
B XcB Xu out
B Xu inUncertainty
```
DataEB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
CR0, lowEB > 1 GeV
MX < 1.7 GeV
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]1.00
0.00
1.00
Pull
2/d. o. f = 0.0/8
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
Events
×104Other backgrounds
B XcB Xu out
B Xu inUncertainty
Data
CR0, lowEB > 1 GeV
MX < 1.7 GeVq2 > 8 GeV2
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]1.00
0.00
1.00
Pull
2/d. o. f = 2.8/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Events
×103Other backgrounds
XcXu
UncertaintyData
```
EB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
SREB > 1 GeV
0 4 8 26 4 8 26 4 8 26 4 8 26q2 [GeV2]2.00
0.002.00Pull 2/d. o. f = 10.3/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
Events
×103Other backgrounds
B XcB Xu out
B Xu inUncertainty
```
DataEB [1.0, 1.3) EB [1.3, 1.6) EB [1.6, 1.9) EB [1.9, 2.7]
```
SREB > 1 GeV
MX < 1.7 GeV
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]1.00
0.00
1.00
Pull
2/d. o. f = 2.3/8
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Preliminary dt = 365 fb 1
0.00
2.00
4.00
6.00
8.00
Events
×102Other backgrounds
B XcB Xu out
B Xu inUncertainty
Data
SREB > 1 GeV
MX < 1.7 GeVq2 > 8 GeV2
```
FIG. 76: Post-fit signal region distributions for fit 1 (left), 2 (middle) and 3 (right). The
```
```
EBℓ :q2 variable is flattened in bins of EBℓ (in GeV) and q2.
```
```
• fit 5: 0.965 ± 0.088 (9.1%)1899
```
108
FEI B
0
FEI B
+
K0s VetoSlow
0[0]
Slow
0[1]
Slow
0[2]
Slow
±[0]
Slow
±[1]
Slow
±[2]Tracking
```
(B
```
D+
```
)
```
```
(B
```
D +
```
)
```
```
(B
```
D+0
```
)
```
```
(B
```
D′01
```
)
```
```
(B
```
D+
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +2
```
)
```
```
(B
```
D* +0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D00
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D*0s K
```
)
```
```
(B
```
D*0K
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*02
```
)
```
2
0
2
```
(
```
```
) /
```
Belle II Preliminary
```
(B
```
D*00
```
)
```
```
(D
```
```
X)f+ /00
```
B D
```
(*) FF[0]
```
B D
```
(*) FF[1]
```
B D
```
(*) FF[2]
```
B D
```
(*) FF[3]
```
B D
```
(*) FF[4]
```
B D
```
(*) FF[5]
```
B D
```
(*) FF[6]
```
B D
```
(*) FF[7]
```
B D
```
(*) FF[8]
```
B D
- *Broad
FF[0]
B D
- *Broad
FF[1]
B D
- *Broad
FF[2]
B D
- *Narrow
FF[0]
B D
- *Narrow
FF[1]
B D
- *Narrow
FF[2]
B D
- *Narrow
FF[3]K ID[0]K ID[1]ID[0]ID[1]ID[2]ID[3]DFN 1DFN 2
DFN
```
BLNP(B X
```
```
+u )
```
```
(B
```
- )
2
0
2
```
(
```
```
) /
```
```
(B
```
- )
```
(B
```
X0u
```
)
```
```
(B
```
```
0 )
```
```
(B
```
```
′0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
B
```
(′) FF[0]
```
B
```
(′) FF[1]
```
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
B
FF[0]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
2
0
2
```
(
```
```
) /
```
B
FF[4]
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
ss fragmentationCont. Norm.[0]Cont. Norm.[1]Cont. Calibration[0]Cont. Calibration[1]Cont. Calibration[2]Cont. Calibration[3]Cont. Calibration[4]
Xc CRotherXc SR
MC Stat. CR[0]MC Stat. CR[1]MC Stat. CR[2]MC Stat. CR[3]MC Stat. CR[4]MC Stat. CR[5]MC Stat. CR[6]MC Stat. CR[7]MC Stat. CR[8]MC Stat. CR[9]MC Stat. CR[10]MC Stat. CR[11]MC Stat. SR[0]
2
0
2
```
(
```
```
) /
```
MC Stat. SR[1]MC Stat. SR[2]MC Stat. SR[3]MC Stat. SR[4]MC Stat. SR[5]MC Stat. SR[6]MC Stat. SR[7]MC Stat. SR[8]MC Stat. SR[9]MC Stat. SR[10]MC Stat. SR[11]
2
0
2
```
(
```
```
) /
```
FIG. 77: Nuisance parameter pulls for fit 1. The acronyms FF, ID, Cont. and Norm. are
used for form factors, identification, continuum and normalisation respectively. Sets of
parameters related to the same source of uncertainty are indexed by the numbers in
brackets.
After applying all post-fit corrections and adding all post-fit uncertainties, the signal nor-1900
malisations are1901
```
• fit 1: 0.975 ± 0.094 (9.6%)1902
```
```
• fit 3: 0.918 ± 0.109 (11.9%)1903
```
```
• fit 5: 0.969 ± 0.104 (10.7%)1904
```
109
FEI B
0
FEI B
+
K0s VetoSlow
0[0]
Slow
0[1]
Slow
0[2]
Slow
±[0]
Slow
±[1]
Slow
±[2]Tracking
```
(B
```
D+
```
)
```
```
(B
```
D +
```
)
```
```
(B
```
D+0
```
)
```
```
(B
```
D′01
```
)
```
```
(B
```
D+
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +2
```
)
```
```
(B
```
D* +0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D00
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D*0s K
```
)
```
```
(B
```
D*0K
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*02
```
)
```
2
0
2
```
(
```
```
) /
```
Belle II Preliminary
```
(B
```
D*00
```
)
```
```
(D
```
```
X)f+ /00
```
B D
```
(*) FF[0]
```
B D
```
(*) FF[1]
```
B D
```
(*) FF[2]
```
B D
```
(*) FF[3]
```
B D
```
(*) FF[4]
```
B D
```
(*) FF[5]
```
B D
```
(*) FF[6]
```
B D
```
(*) FF[7]
```
B D
```
(*) FF[8]
```
B D
- *Broad
FF[0]
B D
- *Broad
FF[1]
B D
- *Broad
FF[2]
B D
- *Narrow
FF[0]
B D
- *Narrow
FF[1]
B D
- *Narrow
FF[2]
B D
- *Narrow
FF[3]K IDID[0]ID[1]ID[2]ID[3]DFN 1DFN 2
DFN
```
BLNP(B X
```
```
+u )
```
```
(B
```
- )
```
(B
```
- )
2
0
2
```
(
```
```
) /
```
```
(B
```
X0u
```
)
```
```
(B
```
```
0 )
```
```
(B
```
```
′0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
B
```
(′) FF[0]
```
B
```
(′) FF[1]
```
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
B
FF[0]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
2
0
2
```
(
```
```
) /
```
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
ss fragmentationCont. Norm.[0]Cont. Norm.[1]Cont. Calibration[0]Cont. Calibration[1]Cont. Calibration[2]Cont. Calibration[3]Cont. Calibration[4]
Xc CRXc SR
MC Stat. CR[0]MC Stat. CR[1]MC Stat. CR[2]MC Stat. CR[3]MC Stat. CR[4]MC Stat. CR[5]MC Stat. CR[6]MC Stat. CR[7]MC Stat. CR[8]MC Stat. CR[9]MC Stat. CR[10]MC Stat. CR[11]MC Stat. SR[0]MC Stat. SR[1]MC Stat. SR[2]
2
0
2
```
(
```
```
) /
```
MC Stat. SR[3]MC Stat. SR[4]MC Stat. SR[5]MC Stat. SR[6]MC Stat. SR[7]MC Stat. SR[8]MC Stat. SR[9]MC Stat. SR[10]MC Stat. SR[11]
2
0
2
```
(
```
```
) /
```
FIG. 78: Nuisance parameter pulls for fit 3. The acronyms FF, ID, Cont. and Norm. are
used for form factors, identification, continuum and normalisation respectively. Sets of
parameters related to the same source of uncertainty are indexed by the numbers in
brackets.
resulting in the partial branching fractions1905
```
• fit 1: ∆B(B → Xuℓν) = (1.540 ± 0.149) × 10−31906
```
```
• fit 3: ∆B(B → Xuℓν) = (0.945 ± 0.112) × 10−31907
```
```
• fit 5: ∆B(B → Xuℓν) = (0.554 ± 0.060) × 10−31908
```
which, when extrapolated to the full phase-space are1909
110
FEI B
0
FEI B
+
K0s VetoSlow
0[0]
Slow
0[1]
Slow
0[2]
Slow
±[0]
Slow
±[1]
Slow
±[2]Tracking
```
(B
```
D+
```
)
```
```
(B
```
D +
```
)
```
```
(B
```
D+0
```
)
```
```
(B
```
D′01
```
)
```
```
(B
```
D+
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +
```
)
```
```
(B
```
D* +2
```
)
```
```
(B
```
D* +0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D00
```
)
```
```
(B
```
D0
```
)
```
```
(B
```
D*0s K
```
)
```
```
(B
```
D*0K
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*0
```
)
```
```
(B
```
D*02
```
)
```
2
0
2
```
(
```
```
) /
```
Belle II Preliminary
```
(B
```
D*00
```
)
```
```
(D
```
```
X)f+ /00
```
B D
```
(*) FF[0]
```
B D
```
(*) FF[1]
```
B D
```
(*) FF[2]
```
B D
```
(*) FF[3]
```
B D
```
(*) FF[4]
```
B D
```
(*) FF[5]
```
B D
```
(*) FF[6]
```
B D
```
(*) FF[7]
```
B D
```
(*) FF[8]
```
B D
- *Broad
FF[0]
B D
- *Broad
FF[1]
B D
- *Broad
FF[2]
B D
- *Narrow
FF[0]
B D
- *Narrow
FF[1]
B D
- *Narrow
FF[2]
B D
- *Narrow
FF[3]K ID[0]K ID[1]ID[0]ID[1]ID[2]DFN 1DFN 2
DFN
```
BLNP(B X
```
```
+u )
```
```
(B
```
- )
```
(B
```
- )
2
0
2
```
(
```
```
) /
```
```
(B
```
X0u
```
)
```
```
(B
```
```
0 )
```
```
(B
```
```
′0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
```
(B
```
```
0 )
```
B
```
(′) FF[0]
```
B
```
(′) FF[1]
```
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
B
FF[0]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
B
FF[0]
B
FF[10]
B
FF[1]
B
FF[2]
B
FF[3]
B
FF[4]
2
0
2
```
(
```
```
) /
```
B
FF[5]
B
FF[6]
B
FF[7]
B
FF[8]
B
FF[9]
ss fragmentationCont. Norm.[0]Cont. Norm.[1]Cont. Calibration[0]Cont. Calibration[1]Cont. Calibration[2]Cont. Calibration[3]Cont. Calibration[4]Cont. Calibration[5]Cont. Calibration[6]Cont. Calibration[7]
Xc CRXc SR
MC Stat. CR[0]MC Stat. CR[1]MC Stat. CR[2]MC Stat. CR[3]MC Stat. CR[4]MC Stat. CR[5]MC Stat. CR[6]MC Stat. CR[7]MC Stat. SR[0]MC Stat. SR[1]MC Stat. SR[2]MC Stat. SR[3]
2
0
2
```
(
```
```
) /
```
MC Stat. SR[4]MC Stat. SR[5]MC Stat. SR[6]MC Stat. SR[7]
2
0
2
```
(
```
```
) /
```
FIG. 79: Nuisance parameter pulls for fit 5. The acronyms FF, ID, Cont. and Norm. are
used for form factors, identification, continuum and normalisation respectively. Sets of
parameters related to the same source of uncertainty are indexed by the numbers in
brackets.
```
• fit 1: B(B → Xuℓν) = (1.777 ± 0.172) × 10−31910
```
```
• fit 3: B(B → Xuℓν) = (1.672 ± 0.198) × 10−31911
```
```
• fit 5: B(B → Xuℓν) = (1.764 ± 0.190) × 10−31912
```
The statistical correlation of the three results was estimated with a bootstrapping method1913
and, assuming a systematic uncertainty of 100%, we find that the result from fit 1 agrees1914
with the results of fit 3 and 5 within 1.0σ and 0.1σ respectively. There is however no good1915
111
TABLE XXXII: Signal, background and data yields in the signal region as extracted from
each fit. The error given for B → Xuℓν and background yields is the total uncertainty as
obtained from each fit.
Fit B → Xuℓν-in B → Xuℓν-out Backgrounds Data
Fit 1 1615 ± 122 – 3781 ± 216 5383
Fit 3 1243 ± 109 33 ± 5 962 ± 100 2236
Fit 5 881 ± 71 42 ± 4 434 ± 65 1355
method to properly evaluate the systematic correlation as any method ignores correlations1916
between fit parameters which are sizeable in our case. These can be compared to the world1917
```
average as given in the PDG [3]: (1.92 ± 0.21) × 10−3 (10.9%). The 3 measured branching1918
```
fractions agree within 0.5σ, 0.9σ and 0.6σ respectively with the world average. When split1919
in statistical and systematic uncertainty, the three measured branching fractions read1920
```
• fit 1: ∆B(B → Xuℓν) = (1.540 ± 0.083 ± 0.122) × 10−31921
```
```
• fit 3: ∆B(B → Xuℓν) = (0.945 ± 0.053 ± 0.099) × 10−31922
```
```
• fit 5: ∆B(B → Xuℓν) = (0.554 ± 0.025 ± 0.054) × 10−31923
```
The systematics uncertainty breakdown is shown in Table XXXIII.19241925
1926
```
The value of |Vub| can be determined from a measured partial branching fraction ∆B(B →1927
```
```
Xuℓν) and partial decay rate ∆Γ(B → Xuℓν) using1928
```
|Vub| =
s
```
∆B(B → Xuℓν)
```
```
τB ∆Γ(B → Xuℓν)
```
```
, (16)
```
where τB = 1.578 ± 0.003 ps is the B meson lifetime [51]. Following Ref. [51], three different1929
theoretical frameworks are used to extract values of |Vub|:1930
• The BLNP model relies on complex theoretical technology to optimise the description1931
of inclusive B → Xuℓν decays in the shape-function region where the hadronic system1932
energy is large while its mass is small. The model then smoothly interpolates between1933
that region and the region where the HQE is valid. The BLNP framework provides1934
decay rate predictions at next-to-leading order in αs and second order in 1/mb for1935
arbitrary phase-space regions. The BLNP calculation relies on the shape function1936
renormalisation scheme and uses as input mSFb = 4.60 ± 0.02 GeV and µ2 SFπ = 0.18+0.05−0.061937
GeV2.1938
```
• The Dressed Gluon Exponentiation (DGE) computation [56] relies on a resummation of1939
```
the perturbation theory. It utilises the momentum scale hierarchy in the semileptonic1940
decays without introducing a momentum cut-off. The DGE calculation is performed1941
in the MS renormalisation scheme and uses mMSb = 4.21 ± 0.04 GeV.1942
• The model developed by Gambino, Giordano, Ossola and Uraltsev [59] doesn’t focus1943
on a particular region of phase space but instead separates between perturbative and1944
112
```
Relative uncertainty (%)
```
Uncertainty source Fit 1 Fit 3 Fit 5
DFN parameters 4.4 4.5 5.7
DFN → BLNP 0.2 0.8 1.3
γS 1.7 2.1 2.1
B → πℓν form factors 0.3 0.3 0.3
B → ρℓν form factors 0.3 0.3 0.2
B → ωℓν form factors 0.1 0.1 0.1
```
B → η(′)ℓν form factors < 0.1 < 0.1 < 0.1
```
B± → Xuℓν branching fractions 0.9 0.6 0.5
B0 → Xuℓν branching fractions 0.6 0.5 0.5
B → D∗∗Broad form factors 0.5 0.1 0.2
B → D∗∗Narrow form factors 0.1 < 0.1 < 0.1
B → D/D∗ℓν form factors < 0.1 < 0.1 < 0.1
B± → Xcℓν branching fractions 0.7 0.5 0.2
B0 → Xcℓν branching fractions 0.6 0.2 0.1
D decay branching fractions 0.1 0.3 0.1
SR Xcℓν normalisation 1.6 3.5 3.4
CR Xcℓν normalisation 1.0 1.1 0.4
Other backgrounds normalisation 0.3 N/A N/A
Xu fragmentation 0.3 4.4 3.9
```
NΥ (4S) 1.6 1.6 1.6
```
FEI 1.3 1.3 1.4
πs 0.4 0.2 0.3
ℓ identification 0.7 0.7 0.6
f ±/00 0.6 0.7 0.6
Continuum calibration 0.2 0.2 0.2
Tracking 0.3 0.3 0.3
efficiency 0.1 0.1 < 0.1
K± ID < 0.1 < 0.1 < 0.1
Simulated data statistics 1.1 1.1 0.8
Fit bias 2.6 2.3 1.8
Composition uncertainty 1.3 5.7 0.2
B → Xcℓν overestimation correction 2.6 0.4 1.3
Total systematic 7.8 10.5 9.7
Statistical 5.4 5.6 4.5
Total 9.5 11.9 10.7
TABLE XXXIII: Systematic uncertainty breakdown for all fits. The systematic sources are
ranked in descending order of their contribution in fit 1.
```
power-suppressed effects yielding predictions O(α2s β0) and O(1/m3b ). For each struc-1945
```
113
ture function describing the decay rate, the b-quark motion is parametrised as a single1946
```
function for which different two-parameter functional forms are tested. The GGOU cal-1947
```
culation is carried out in the kinetic renormalisation scheme and uses mkinb = 4.57±0.011948
GeV and µ2 kinπ = 0.45 ± 0.04 GeV2.1949
The values of |Vub| obtained from each model and each signal extraction fit using Equa-1950
tion 16 are summarised in Table XXXIV.1951
```
Relative uncertainty (%)
```
Fit 1 Fit 3 Fit 5
MX < 1.7 GeV q2 > 8 GeV2
Phase-space region EBℓ > 1 GeV MX < 1.7 GeV
EBℓ > 1 GeV EBℓ > 1 GeV
Fit variable EBℓ : q2 EBℓ : q2 EBℓ
Inclusive B → Xuℓν model
BLNP 63.0+6.4−5.0 47.4+5.2−4.3 24.6+3.2−2.4
```
∆Γ (ps−1) DGE 59.4+3.3−2.8 42.9+4.7−3.9 25.0+2.2−1.7
```
GGOU 60.8+2.8−2.0 47.6+3.3−3.0 25.2+2.9−2.0
BLNP 3.94 ± 0.11 ± 0.16+0.20−0.16 3.56 ± 0.10 ± 0.19+0.20−0.16 3.78 ± 0.09 ± 0.18+0.25−0.18
|Vub| × 103 DGE 4.05 ± 0.11 ± 0.16+0.11−0.09 3.74 ± 0.10 ± 0.20+0.21−0.17 3.75 ± 0.08 ± 0.18+0.16−0.13
GGOU 4.01 ± 0.11 ± 0.16+0.09−0.07 3.55 ± 0.10 ± 0.19+0.12−0.11 3.74 ± 0.08 ± 0.18+0.21−0.15
TABLE XXXIV: Values of the B → Xuℓν decay rate and |Vub| obtained from three
different theoretical predictions in three separate phase-space regions.1952
1953
1954
The values of |Vub| extracted from the broadest phase-space region are compared to the1955
latest inclusive and exclusive HFLAV averages [51] in Figure 80.19561957
114
2.0 2.5 3.0 3.5 4.0 4.5
|Vub| × 103
BLNP
This
measurement
```
{
```
DGE
GGOU
HFLAV inclusive
HFLAV exclusive
HFLAV B
```
FIG. 80: Comparison between the three values of |Vub| obtained from fit 1 (blue), the
```
```
inclusive (purple), exclusive (cyan) and B → πℓν (pink) averages quoted in the latest
```
HFLAV report [51]. The outer error bars represent the total uncertainty and for the three
measured values and the B → πℓν average, the inner error bars represent the theoretical
uncertainty.
115
A. BLNP MODELLING1958
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
q2 [GeV2]
0
5
10
15
20
25
M
X
[GeV]
```
BLNP: 8,000,000 events; no cuts; B±/B0
```
0
200
400
600
800
1000
1200
1400
FIG. 81: Two-dimensional histogram of MX versus q2 for 8 million events generated with
the most up-to-date input values for the BLNP model in EvtGen.
A possible explanation for the unexpected spike observed in the generation of events with1959
the BLNP model is given here.1960
1961
```
In the BLNP model [6], a Soft Colinear Effective Theory (SCET) expansion is performed1962
```
on the triple differential decay rate dΓ/dq2dpBℓ dMX in the so-called shape function region.1963
We define the variables1964
```
P+ = EX − |⃗p X |, P− = EX + |⃗p X |, (17)
```
where EX and |⃗p X | are respectively the energy and 3-momentum magnitude of the hadronic1965
system. In the shape function region, P− is much larger than P+ and therefore an expansion1966
```
in powers of P+/(P− − P+) is performed. However, outside of this specific region, P− and P+1967
```
can be of the same order which when combined with other factors can yield contributions of1968
```
O(1) which are not suppressed by powers of P+/(P− − P+). Therefore, in regions of phase-1969
```
space where P− ∼ P+, an enhancement of events is observed. This seems to be confirmed1970
when one isolates this particular region. In Fig. 83, the same plot as in Fig. 3 is presented1971
```
with an additional selection of 1√2 (P− − P+) < 0.4 GeV. Only the problematic events survive1972
```
this selection.1973
116
0.0 0.5 1.0 1.5 2.0 2.5
EB [GeV]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
M
X
[GeV]
```
BLNP: 8,000,000 events; no cuts; B±/B0
```
0
200
400
600
800
1000
1200
1400
1600
FIG. 82: Two-dimensional histogram of MX versus EBℓ for 8 million events generated with
the most up-to-date input values for the BLNP model in EvtGen.
117
0.0 0.5 1.0 1.5 2.0 2.5
EB [GeV]
0
5
10
15
20
25
q2
[GeV
2]
```
BLNP: 8,000,000 events; 1
```
2
```
(P P + ) < 0.4 GeV; B±/B0
```
0
25
50
75
100
125
150
175
FIG. 83: Two-dimensional histogram of q2 versus EBℓ for 8 million events generated with
the most up-to-date input values for the BLNP model in EvtGen. An additional cut of
1√
```
2 (P− − P+) < 0.4 GeV is added.
```
118
B. CONTINUUM SUPPRESSION MVA INPUT FEATURES1974
The continuum suppression variables after reconstruction and preselection are shown here.1975
0 1 2 3 4 5 6 7 8
1
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
3
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
4
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
119
0 1 2 3 4 5 6 7 8
5
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
6
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
7
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 1 2 3 4 5 6 7 8
8
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.16)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
120
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos B O
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.01)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos Bz
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.01)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
4.50 5.25 6.00 6.75 7.50 8.25 9.00
Et, CS [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.11 GeV)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
4 2 0 2 4 6 8
m2miss, CS [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.3 GeV
```
```
2)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
121
0.050 0.075 0.100 0.125 0.150 0.175 0.200 0.225oo
0
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.004)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
2.25 1.50 0.75 0.00 0.75 1.50 2.25 3.00oo
1 ×10 2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.0012)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
1.25 0.00 1.25 2.50 3.75 5.00 6.25 7.50oo
2 ×10 2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.002)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
2.25 1.50 0.75 0.00 0.75 1.50 2.25oo
3 ×10 2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.001)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
122
1 0 1 2 3 4 5oo
4 ×10 2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.0015)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0so
00
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.036)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.500 0.375 0.250 0.125 0.000 0.125 0.250 0.375 0.500so
01
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.021)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.45 0.30 0.15 0.00 0.15 0.30 0.45 0.60so
02
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.023)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
123
0.300 0.225 0.150 0.075 0.000 0.075 0.150 0.225 0.300so
03
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.013)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.3 0.2 0.1 0.0 0.1 0.2 0.3so
04
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.014)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.2 0.4 0.6 0.8 1.0 1.2 1.4so
10
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.028)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.150 0.075 0.000 0.075 0.150 0.225 0.300so
12
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.012)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
124
0.15 0.10 0.05 0.00 0.05 0.10 0.15 0.20so
14
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.0073)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000so
20
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.022)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.3 0.2 0.1 0.0 0.1 0.2 0.3 0.4so
22
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.015)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.225 0.150 0.075 0.000 0.075 0.150 0.225so
24
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.011)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
125
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
R2
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.0071)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| B|
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.005)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| O|
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (0.005)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
126
0 3 6 9 12 15 18 21 24
NCS
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
2.00
4.00
6.00
8.00
Events
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
0 3 6 9 12 15 18 21 24
NCStr
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Events
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
127
C. Xcℓν SUPPRESSION MVA INPUT FEATURES1976
The Xcℓν suppression MVA input features after reconstruction, preselection, continuum1977
suppression and K veto are shown here.1978
10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0
```
cos BY( ±)
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.2)
```
×103
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0
```
cos BY( 0)
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.2)
```
×103
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
```
cos c( ±)
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.04)
```
×103
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
```
cos c( 0)
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.04)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
128
35 30 25 20 15 10 5 0 5
```
M2miss( ±slow) [GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.98 GeV
```
```
2)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
35 30 25 20 15 10 5 0 5
```
M2miss( 0slow) [GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.98 GeV
```
```
2)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
5.00 3.75 2.50 1.25 0.00 1.25 2.50 3.75 5.00
Qtot
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.91)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
```
log10 ( 2vtx/ndgf)
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.2)
```
×105
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
129
4 2 0 2 4 6 8 10 12
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.5 GeV
```
```
2)
```
×104
ContinuumFake
SecondaryD* *Gap
D* *D*
DXu
Xu ×10MC Stat. Uncert.
Data
pB > 1 GeV,
130
D. DATA - MC COMPARISON IN SB1 IN DIFFERENT CHANNELS1979
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B0 channel
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.05 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B0 channel
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B0 channel
FIG. 84: Data-MC comparison of pBℓ , MX and q2 in side-band 1 in the B0 channel.
131
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B± channel
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B± channel
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B± channel
FIG. 85: Data-MC comparison of pBℓ , MX and q2 in side-band 1 in the B± channel.
132
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, e± channel
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, e± channel
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, e± channel
FIG. 86: Data-MC comparison of pBℓ , MX and q2 in side-band 1 in the e± channel.
133
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, ± channel
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, ± channel
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, ± channel
FIG. 87: Data-MC comparison of pBℓ , MX and q2 in side-band 1 in the µ± channel.
134
E. PYHF1980
1. Notation1981
• b: bins1982
• c: channels1983
```
– Signal region (SR)1984
```
```
– Control region (CR)1985
```
• s: samples1986
– Xuℓν-in1987
– Xuℓν-out1988
– Xcℓν1989
– Other backgrounds1990
```
• ν: event rate (ν0: nominal rate)1991
```
• µ: scale factor1992
• γ: bin-wise scale factors1993
• α: interpolation parameter1994
• κ: multiplicative modifiers1995
• ∆: additive modifiers1996
• η: unconstrained parameters1997
• χ: constrained parameters1998
• n: event counts1999
• a: auxiliary measurements2000
• Free-floating scale factors2001
– Xuℓν-in: 1 free-floating scale factor, not present in control region channel but2002
only in signal region channel2003
– Xuℓν-out: 1 free-floating scale factor, not present in control region channel but2004
only in signal region channel2005
– Xcℓν: 1 free-floating scale factor and 1 free-floating scale factor per bin, present2006
in both channels2007
– Other backgrounds: 1 free-floating scale factor, present in both channels2008
135
2. Statistical model2009
A general statistical model can be written as follows:2010
```
f (n, a|η, χ) =
```
Y
c
Y
b
```
Pois(ncb|νcb(η, χ))
```
Y
χ∈χ
```
cχ(aχ|χ), (18)
```
where the first term corresponds to the simultaneous measurement of multiple channels and2011
the second to constraint terms for auxiliary measurements. The event rates are defined as:2012
νcb =
X
s∈samples
```
νscb(η, χ) =
```
X
s∈samples
 Y
κ∈κ
```
κscb(η, χ)
```

·

```
ν0scb(η, χ) +
```
X
∆∈∆
```
∆scb(η, χ)
```

```
, (19)
```
where κscb and ∆scb are multiplicative and additive modifiers respectively. They therefore2013
correspond to normalisation and shape uncertainties respectively. Each systematic source2014
in the fit is split in normalisation and shape variation. As explained in the main text, for2015
the sample s = Xcℓν, we incorporate binned free-floating normalisations. The event rates2016
for this sample can therefore be written as:2017
νXccb =

γXcb ·
Y
κ∈κ
κXccb

·

ν0,Xccb +
X
∆∈∆
∆Xccb

```
, (20)
```
The total Xcℓνevent rate can be written:2018
νXc =
X
b,c
νXccb
⇒ νXc =
X
b
γXcb
X
c
 Y
κ
κXccb

·

ν0,Xccb +
X
∆
∆Xccb
```
 (21)
```
For the Xuℓν-in template, the event rate can be written similarly with a single unbinned2019
free-floating normalisation. The signal template is fixed in the control region and its yields2020
are negligible in this region compared to the background yields. Therefore, the signal event2021
rate can be written as:2022
νXu = µXu
X
b
 Y
κ
κXuSR,b

·

ν0,XuSR,b +
X
∆
∆XuSR,b

```
(22)
```
The Xuℓν-out event rate can be written in the exact same way with its own associated2023
free-floating normalisation and constrained modifiers. In some of the fits, this template is2024
completely neglected. In other fits, the yields are small but not negligible which leads to2025
large biases and uncertainties in the fit. In these cases the same free-floating normalisation2026
µXu is assigned to both templates. Finally, the other-background template is assigned a2027
```
Gaussian-constrained multiplicative modifier (normsys).2028
```
3. Modifiers2029
For correlated shape and normalisation uncertainties, pyhf makes use of interpolating func-2030
```
tions, fp and gp (for additive and multiplicative modifiers respectively), constructed from2031
```
136
a small number of evaluations of the expected rate. We summarise in the following table2032
each type of modification and its associated constraint term that we implement in our pyhf2033
setup.2034
Description Modification Constraint term
```
Correlated shape (histosys) ∆scb(α) = fp(α) Gaussian with width given by the auxiliary data
```
```
Normalisation uncertainty (normsys) κscb(α) = gp(α) Gaussian with width given by the auxiliary data
```
```
MC statistical uncertainty (staterror) κscb = γb
```
Q
b Gaussians
```
Normalisation (normfactor) κscb = µ Free-floating
```
```
Data-driven shape (shapefactor) κscb = γb Free-floating
```
TABLE XXXV: Modifiers and constraints implemented in the pyhf fit setup described in
Section 8
Parameter Modifier Constraint Regions Type of variation Number of Parameters
```
Slow π efficiency ∆ + κ Gauss Signal + CR0,low Two-sided 3 (π±) + 3 (π0)
```
Tracking efficiency ∆ + κ Gauss Signal + CR0,low Two-sided 1
B → πℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 5
B → ρ/ωℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 11
```
B → η(′)ℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 2
```
```
B → D(∗)ℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 9
```
Broad B → D∗∗ℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 3
Narrow B → D∗∗ℓν form factors ∆ + κ Gauss Signal + CR0,low Two-sided 4
```
Lepton ID ∆ + κ Gauss Signal + CR0,low Toy 200 toys (truncated to O(10))
```
```
Kaon ID ∆ + κ Gauss Signal + CR0,low Toy 200 toys (truncated to O(10))
```
```
FEI ∆ + κ Gauss Signal + CR0,low Two-sided 11 (B0) + 12 (B+) (truncated to O(5))
```
```
B branching fractions ∆ + κ Gauss Signal + CR0,low Two-sided 10 (B0) + 12 (B+)
```
```
D branching fractions ∆ + κ Gauss Signal + CR0,low Two-sided 234 (truncated to O(15))
```
DFN parameter variations ∆ + κ Gauss Signal + CR0,low Two-sided 2
Inclusive model ∆ + κ Gauss Signal + CR0,low One-sided 1
KS0 efficiency ∆ + κ Gauss Signal + CR0,low One-sided 1
s¯s fragmentation ∆ + κ Gauss Signal + CR0,low Two-sided 1
MC Stats κ Qb Gauss Signal + CR0,low Two-sided 1 for each region
f ±/0 ∆ + κ Gauss Signal + CR0,low Two-sided 1
Cont. normalisation calibration ∆ + κ Gauss Signal + CR0,low Two-sided 1
```
Cont. shape calibration ∆ + κ Gauss Signal + CR0,low Toy 200 (truncated to O(15))
```
Signal-in normalisation µXu Unconstrained Signal region Two-sided 1
B → Xcℓν shape γXcb Unconstrained Signal + CR0,low Two-sided 1 per bin
B → Xcℓν normalisation κ Gauss Signal + CR0,low separately Two-sided 1
Other backgrounds normalisation κ Gauss Signal + CR0,low Two-sided 1
TABLE XXXVI: pyhf parameters
4. Postfit projections2035
In order to cross-check the results of the fit, we project them on variables not used for the2036
fit. To do so, we use the cabinetry function cabinetry.model utils.match fit results2037
```
which takes as input a pyhf model (not fitted) produced for the variable on which to apply2038
```
the fit and the fit results obtained for the chosen fit variable. The matching of the nuisance2039
parameters is done by matching NP with the same name. However, the transfer of some of2040
the nuisance parameters is not trivial so they are modified as:2041
137
• up/down variations: these NP depend on a single interpolation parameter so they can2042
trivially be matched and they are therefore not modified2043
• toy variations: see Section 8 3 1 for details on how these NP are implemented in the2044
fit. In the transfer fit, the variations in the eigendirections that are generated in the2045
original fit are taken and added as ±σ weights to the dataset, then treated as up/down2046
variations for transfer fits2047
• normalisation factors: represented by a single free-floating number so their transfer is2048
trivial2049
• shape factors: they are given as a single free-floating number to the fit which internally2050
splits them as one normalisation per bin. To translate them properly, we split the2051
B → Xcℓν sample into subsamples, one per bin. Each is given a norm factor with the2052
same name as the nuisance parameter associated with that bin in the original fit. The2053
fit then matches each shape factor from the original fit to a normalisation factor in2054
the new pyhf model2055
One important caveat is that the MC statistical uncertainty cannot be transferred since2056
the binning and the number of events per bin cannot be matched between two different2057
variables. We show in Figure 88 an example of such a transfer. We use as nominal fit, the2058
CRK,low/CRK,high fit 1 with EBℓ :q2 which we transfer to MX . The B → Xcℓν template is2059
split in 12 separate templates, one for each of the 12 EBℓ :q2 bins in the original fit.20602061
138
0
10000
20000
30000
40000
50000
60000
events
ControlRegion
pre-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7bin0.68
0.84
1.0
1.16
1.32
data / model
0
200
400
600
800
1000
1200
1400
1600
events
SignalRegion
pre-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7bin0.68
0.84
1.0
1.16
1.32
data / model
0
10000
20000
30000
40000
50000
60000
events
ControlRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7bin0.68
0.84
1.0
1.16
1.32
data / model
0
200
400
600
800
1000
1200
1400
1600
events
SignalRegion
post-fit
otherBackground
Xulnu
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 1 2 3 4 5 6 7bin0.68
0.84
1.0
1.16
1.32
data / model
FIG. 88: Projection of the CRK,low
```
/CRK,high (CR/SR) EBℓ :q2 fit projected on MX .
```
139
F. PLOTS FROM FITS TO ALL VARIABLES IN ALL REGIONS2062
In this Section, we add plots from all fits described in Section 8. The pre- and post-fit2063
distributions are shown together with the ranking of the 30 nuisance parameters with largest2064
```
impact, the toy pull distribution, the linearity test and the correlation matrix (only entries2065
```
```
with a value larger than or equal to 0.20 are shown).2066
```
1. q2 fit2067
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV2068
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
1400
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
FIG. 89: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV
140
DFN[1]gammaS
mu_signal_XclnuHybridModel
FEI_B0
bf_BptoXulnubf_B0toXulnu
FEI_BpleptonID[0]
MCStatsignal[9]
0.050
0.025
0.000
0.025
0.050
f+-/00
bf_B0topilnuMCStatsignal[6]bf_B0toDstetalnubf_BptoDstetalnuMCStatsignal[7]MCStatsignal[5]bf_B0toDetalnuff_Pion[3]mu_other_bkg
0.050
0.025
0.000
0.025
0.050
bf_Bptorholnubf_B0torholnu
mu_sideband_XclnuMCStatsignal[8]MCStatsignal[0]
bf_BptopilnuTrackingSlow_Pi0[1]ff_Pion[4]ff_Pion[2]
0.050
0.025
0.000
0.025
0.050
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 90: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV
141
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.008±0.014G = 1.009±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.006±0.014G = 1.013±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.004±0.014G = 0.993±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 0.9968±0.0025) in+(0.0064±0.0023)
```
FIG. 91: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom left: Xcℓν factor
```
```
pulls (bin 9); bottom right: linearity test
```
142
Slow_Pi0[0]bf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]
Slow_Pi0[0]
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
MCStatsideband[7]
MCStatsideband[8]
MCStatsideband[9]
1.00 -0.04 -0.05 0.16 -0.05 -0.01 0.02 0.01 0.04 -0.13 0.01 0.12 -0.04 -0.03 -0.13 -0.21 -0.22 -0.20 -0.17 -0.12 -0.08
-0.04 1.00 -0.17 0.01 -0.05 0.01 0.01 -0.06 -0.19 -0.02 -0.23 -0.22 -0.08 0.08 0.12 0.14 0.12 0.09 0.07 0.05
-0.05 -0.17 1.00 0.07 -0.01 0.02 0.03 0.05 -0.02 -0.05 -0.06 0.06 -0.21 -0.23 -0.09 0.06 0.12 0.12 0.11 0.09 0.04 0.03
0.16 0.01 0.07 1.00 0.11 0.01 0.02 -0.03 0.13 0.14 -0.01 -0.08 -0.07 0.01 0.18 0.28 0.25 0.13 0.02 -0.05 -0.06
-0.05 -0.05 -0.01 0.11 1.00 0.01 -0.03 0.01 -0.07 -0.04 0.33 -0.18 -0.43 -0.24 0.08 0.18 0.20 0.18 0.12 0.06
-0.01 0.02 0.01 0.01 1.00 0.07 -0.03 -0.56 -0.01 0.04 -0.01 -0.01 0.02 0.03 0.02 -0.05 -0.12 -0.25
0.02 0.01 0.03 0.02 0.07 1.00 0.18 -0.15 0.02 -0.05 -0.29 -0.02 -0.02 0.01 -0.04 -0.13 -0.17 -0.19 -0.03 -0.02
0.01 0.05 -0.03 -0.03 0.18 1.00 0.24 0.01 -0.11 0.03 0.01 0.01 0.02 -0.03 -0.01 -0.05 0.01
0.04 0.01 -0.02 -0.03 0.01 -0.56 -0.15 0.24 1.00 0.08 -0.02 -0.34 0.06 0.05 0.03 0.01 0.01 0.04 0.06 0.10 0.01 0.01 0.02
-0.13 -0.06 -0.05 0.13 -0.07 0.02 0.01 0.08 1.00 0.02 0.15 0.01 0.02 -0.04 -0.16 -0.23 -0.24 -0.24 -0.20 -0.13 -0.04
0.01 -0.19 -0.06 0.14 -0.04 -0.01 -0.05 -0.11 -0.02 0.02 1.00 -0.20 -0.42 -0.21 -0.09 0.04 0.10 0.09 0.05 0.01 -0.05 -0.11
0.12 -0.02 0.06 -0.01 0.04 -0.29 0.03 -0.34 0.15 -0.20 1.00 -0.06 -0.13 -0.14 -0.14 -0.11 -0.07 -0.03 0.01 0.04 0.03 -0.01
-0.04 -0.23 -0.21 -0.08 0.33 -0.01 -0.02 0.06 0.01 -0.42 -0.06 1.00 0.72 0.39 0.17 0.08 0.06 0.06 0.06 0.07 0.07
-0.22 -0.23 -0.07 -0.18 -0.01 -0.02 0.05 0.02 -0.21 -0.13 0.72 1.00 0.78 0.48 0.17 0.06 0.02 -0.01 0.01 0.02
-0.03 -0.08 -0.09 0.01 -0.43 0.01 0.01 0.03 -0.04 -0.09 -0.14 0.39 0.78 1.00 0.74 0.40 0.26 0.17 0.10 0.05 0.03
-0.13 0.08 0.06 0.18 -0.24 0.02 0.01 0.01 -0.16 0.04 -0.14 0.17 0.48 0.74 1.00 0.75 0.64 0.51 0.36 0.21 0.09
-0.21 0.12 0.12 0.28 0.08 0.03 0.02 -0.23 0.10 -0.11 0.08 0.17 0.40 0.75 1.00 0.82 0.70 0.52 0.31 0.14 0.01
-0.22 0.14 0.12 0.25 0.18 0.02 -0.04 -0.24 0.09 -0.07 0.06 0.06 0.26 0.64 0.82 1.00 0.71 0.55 0.34 0.15 0.01
-0.20 0.12 0.11 0.13 0.20 -0.13 -0.03 0.01 -0.24 0.05 -0.03 0.06 0.02 0.17 0.51 0.70 0.71 1.00 0.54 0.35 0.17 0.01
-0.17 0.09 0.09 0.02 0.18 -0.05 -0.17 -0.01 0.04 -0.20 0.01 0.01 0.06 -0.01 0.10 0.36 0.52 0.55 0.54 1.00 0.32 0.16 -0.23
-0.12 0.07 0.04 -0.05 0.12 -0.12 -0.19 -0.05 0.06 -0.13 -0.05 0.04 0.07 0.01 0.05 0.21 0.31 0.34 0.35 0.32 1.00 0.15 -0.27
-0.08 0.05 0.03 -0.06 0.06 -0.25 -0.03 0.10 -0.04 -0.11 0.03 0.07 0.02 0.03 0.09 0.14 0.15 0.17 0.16 0.15 1.00 -0.26
0.01 -0.01 0.01 0.01 0.01 -0.23 1.00
0.01 -0.27 1.00
-0.02 0.01 0.02 -0.26 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 92: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV
143
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2, Experimental cut: pBℓ > 1.02069
GeV2070
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
50000
60000
events
sidebandpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
1400
events
signalpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
50000
60000
events
sidebandpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
FIG. 93: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV
144
DFN[1]gammaS
mu_signal_XclnuHybridModel
FEI_B0FEI_Bpf+-/00leptonID[0]
MCStatsignal[9]bf_B0topilnu
0.050
0.025
0.000
0.025
0.050
MCStatsignal[7]mu_sideband_XclnuMCStatsignal[6]bf_BptoXulnu
ff_Pion[3]bf_B0toXulnumu_other_bkgbf_Bptorholnu
MCStatsignal[8]bf_BptoDstetalnu
0.050
0.025
0.000
0.025
0.050
MCStatsignal[5]MCStatsignal[0]bf_B0toDstetalnubf_B0torholnubf_B0toDetalnubf_Bptopilnu
Trackingff_Pion[4]ff_Pion[2]ff_Rho[7]
0.050
0.025
0.000
0.025
0.050
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 94: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV
145
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.003±0.014G = 0.989±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.067±0.014G = 0.996±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.020±0.015G = 1.035±0.010
```
FIG. 95: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
```
Experimental cut: pBℓ > 1.0 GeV. Top left: signal-in pulls; top right: signal-out pulls;
```
```
bottom left: Xcℓν factor pulls (bin 1); bottom right: Xcℓν factor pulls (bin 9)
```
146
Slow_Pi0[0]bf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_signal_Xulnu_outmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]
Slow_Pi0[0]
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_signal_Xulnu_out
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
MCStatsideband[7]
MCStatsideband[8]
MCStatsideband[9]
1.00 -0.02 -0.03 -0.12 -0.11 0.01 0.01 0.04 0.04 -0.13 -0.04 0.06 -0.03 0.03 -0.14 -0.25 -0.26 -0.23 -0.19 -0.13 -0.08
-0.02 1.00 -0.14 0.01 -0.08 0.01 0.05 0.02 0.02 -0.01 -0.01 -0.17 -0.26 -0.23 -0.07 0.09 0.12 0.15 0.12 0.10 0.07 0.05
-0.03 -0.14 1.00 -0.05 -0.07 0.02 0.04 0.05 -0.01 0.02 -0.02 -0.11 0.03 -0.21 -0.21 -0.05 0.08 0.11 0.10 0.09 0.07 0.03 0.03
-0.12 0.01 -0.05 1.00 -0.16 0.01 0.01 0.02 0.02 -0.18 -0.06 -0.01 0.03 -0.15 -0.26 -0.23 -0.11 -0.01 0.05 0.05
-0.11 -0.08 -0.07 -0.16 1.00 -0.03 -0.05 0.03 -0.11 -0.04 -0.03 0.39 -0.16 -0.45 -0.25 0.09 0.18 0.21 0.18 0.12 0.06
0.01 0.02 0.01 1.00 0.07 -0.04 -0.56 -0.19 -0.01 -0.02 0.03 -0.02 -0.02 0.01 0.02 0.01 -0.05 -0.12 -0.24
0.01 0.05 0.04 0.01 -0.03 0.07 1.00 0.20 -0.14 -0.07 0.01 -0.07 -0.19 -0.03 -0.02 0.03 0.02 -0.04 -0.13 -0.16 -0.19 -0.03 -0.02
0.01 0.02 0.05 0.02 -0.05 -0.04 0.20 1.00 0.27 0.14 -0.13 -0.02 -0.02 0.02 0.01 0.01 0.01 -0.04 0.02 -0.09 -0.02 0.01
0.04 0.02 -0.01 0.02 -0.56 -0.14 0.27 1.00 0.44 0.09 -0.03 -0.30 0.05 0.05 0.02 0.01 0.01 0.05 0.05 0.09 0.01 0.01 0.02
0.04 -0.01 0.02 0.03 -0.19 -0.07 0.14 0.44 1.00 0.08 -0.07 -0.74 -0.03 -0.08 -0.09 -0.08 -0.02 -0.01 -0.01 0.02 0.02 0.03 0.01
-0.13 -0.01 -0.02 -0.18 -0.11 -0.01 0.01 0.09 0.08 1.00 -0.07 0.08 0.01 0.03 -0.02 -0.14 -0.21 -0.23 -0.23 -0.20 -0.13 -0.04
-0.04 -0.17 -0.11 -0.06 -0.04 -0.02 -0.07 -0.13 -0.03 -0.07 -0.07 1.00 -0.12 -0.40 -0.18 -0.05 0.08 0.12 0.11 0.08 0.03 -0.02 -0.10
0.06 0.03 -0.03 0.03 -0.19 -0.02 -0.30 -0.74 0.08 -0.12 1.00 -0.02 -0.02 -0.04 -0.07 -0.06 -0.02 0.02 0.02
-0.03 -0.26 -0.21 -0.01 0.39 -0.02 -0.03 -0.02 0.05 -0.03 0.01 -0.40 1.00 0.69 0.33 0.13 0.07 0.05 0.06 0.05 0.06 0.07
0.03 -0.23 -0.21 0.03 -0.16 -0.02 -0.02 0.05 -0.08 0.03 -0.18 -0.02 0.69 1.00 0.76 0.47 0.16 0.06 0.01 -0.01 0.02
-0.07 -0.05 -0.45 0.03 0.02 0.02 -0.09 -0.02 -0.05 -0.02 0.33 0.76 1.00 0.74 0.39 0.25 0.16 0.09 0.05 0.03
-0.14 0.09 0.08 -0.15 -0.25 0.01 0.02 0.01 0.01 -0.08 -0.14 0.08 -0.04 0.13 0.47 0.74 1.00 0.74 0.63 0.50 0.35 0.20 0.10
-0.25 0.12 0.11 -0.26 0.09 0.02 0.01 -0.02 -0.21 0.12 -0.07 0.07 0.16 0.39 0.74 1.00 0.82 0.70 0.52 0.31 0.14 0.01
-0.26 0.15 0.10 -0.23 0.18 0.01 -0.04 0.01 -0.01 -0.23 0.11 -0.06 0.05 0.06 0.25 0.63 0.82 1.00 0.71 0.55 0.34 0.16 0.01
-0.23 0.12 0.09 -0.11 0.21 -0.13 -0.04 0.01 -0.01 -0.23 0.08 -0.02 0.06 0.01 0.16 0.50 0.70 0.71 1.00 0.54 0.36 0.17 0.01
-0.19 0.10 0.07 -0.01 0.18 -0.05 -0.16 0.02 0.05 0.02 -0.20 0.03 0.05 -0.01 0.09 0.35 0.52 0.55 0.54 1.00 0.32 0.16 -0.23
-0.13 0.07 0.03 0.05 0.12 -0.12 -0.19 -0.09 0.05 0.02 -0.13 -0.02 0.02 0.06 0.05 0.20 0.31 0.34 0.36 0.32 1.00 0.15 -0.27
-0.08 0.05 0.03 0.05 0.06 -0.24 -0.03 -0.02 0.09 0.03 -0.04 -0.10 0.02 0.07 0.02 0.03 0.10 0.14 0.16 0.17 0.16 0.15 1.00 -0.26
0.01 0.01 0.01 0.01 -0.23 1.00
0.01 -0.27 1.00
-0.02 0.01 0.02 0.01 -0.26 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 96: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV
147
3. Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0 GeV2071
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sidebandpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
1400
events
signalpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sidebandpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
0 5 10 15 20 25q2 [GeV2]0.5
0.75
1.0
1.25
data / model
FIG. 97: Variable: q2, Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0 GeV
148
DFN[1]
HybridModelmu_signal_Xclnubf_BptoXulnugammaSbf_B0toXulnuMCStatsignal[9]
FEI_B0DFN[2]ff_Pion[3]
0.05
0.00
0.05
bf_B0topilnuMCStatsignal[5]MCStatsignal[8]Slow_Pi0[0]ff_Pion[4]
mu_sideband_Xclnu
bf_Bptopilnu
FEI_Bpff_Pion[2]leptonID[0]
0.05
0.00
0.05
bf_BptorholnuMCStatsideband[9]bf_B0torholnuff_Rho[7]Slow_Pip[0]ff_Rho[6]Slow_Pi0[1]ff_Pion[1]bf_Bptoomegalnuff_Rho[9]
0.05
0.00
0.05
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 98: Variable: q2, Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0 GeV
149
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.002±0.014G = 1.022±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.019±0.015G = 1.046±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.022±0.015G = 1.041±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = -0.016±0.014G = 1.009±0.010
```
FIG. 99: Variable: q2, Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal-in pulls; top right: signal-out pulls; bottom left: Xcℓν factor pulls
```
```
(bin 1); bottom right: Xcℓν factor pulls (bin 9)
```
150
Slow_Pi0[0]bf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_signal_Xulnu_outmu_other_bkgmu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]
Slow_Pi0[0]
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_signal_Xulnu_out
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
MCStatsideband[7]
MCStatsideband[8]
MCStatsideband[9]
1.00 -0.01 -0.02 -0.10 0.03 0.01 0.02 -0.02 0.06 -0.05 0.07 -0.02 -0.02 -0.06 -0.14 -0.20 -0.20 -0.17 -0.13 -0.09 -0.06
-0.01 1.00 -0.12 -0.04 -0.03 0.02 0.02 0.01 -0.20 -0.24 -0.24 -0.10 0.08 0.14 0.17 0.14 0.11 0.08 0.06
-0.02 -0.12 1.00 -0.04 -0.02 0.03 0.03 0.05 -0.10 0.06 -0.22 -0.24 -0.09 0.05 0.11 0.11 0.11 0.09 0.04 0.04
-0.10 -0.04 -0.04 1.00 -0.10 0.01 -0.01 0.01 0.01 -0.04 0.03 0.03 -0.05 -0.21 -0.30 -0.26 -0.14 -0.03 0.03 0.04
-0.03 -0.02 -0.10 1.00 0.03 0.03 -0.01 0.01 0.01 -0.10 0.03 0.33 -0.20 -0.45 -0.25 0.07 0.17 0.20 0.18 0.13 0.07
0.03 0.02 0.03 0.01 0.03 1.00 -0.45 -0.06 -0.04 -0.05 -0.01 -0.03 -0.03 -0.01 0.01 0.01 0.01 -0.03 -0.09 -0.23
0.01 0.02 0.03 -0.01 0.03 1.00 0.03 0.27 -0.45 -0.05 0.05 -0.01 -0.02 0.01 0.02 0.02 -0.02 -0.11 -0.16 -0.19 -0.04 -0.01
0.02 0.05 -0.01 0.03 1.00 -0.03 0.38 -0.15 -0.13 -0.02 -0.02 -0.02 -0.03 0.05 -0.07 -0.01 0.01
-0.02 0.01 0.01 0.01 -0.45 0.27 -0.03 1.00 -0.52 0.02 0.31 0.03 0.03 0.04 0.05 0.04 0.03 0.01 -0.01 -0.01 0.02 0.01 0.03
0.06 0.01 0.01 -0.06 -0.45 0.38 -0.52 1.00 -0.06 -0.65 0.03 -0.03 -0.05 -0.04 -0.03 0.01 0.07 0.06 0.08 -0.01
-0.05 -0.20 -0.10 -0.04 -0.10 -0.04 -0.05 -0.15 0.02 -0.06 1.00 -0.15 -0.41 -0.15 -0.02 0.07 0.09 0.07 0.04 -0.01 -0.04 -0.11
0.07 0.06 0.03 -0.05 0.05 -0.13 0.31 -0.65 -0.15 1.00 -0.05 -0.12 -0.11 -0.10 -0.06 -0.04 -0.02 -0.01 0.01 0.01
-0.02 -0.24 -0.22 0.03 0.33 -0.01 -0.01 0.03 0.03 -0.41 -0.05 1.00 0.70 0.37 0.17 0.07 0.05 0.05 0.05 0.06 0.06
-0.02 -0.24 -0.24 0.03 -0.20 -0.03 -0.02 -0.02 0.03 -0.15 -0.12 0.70 1.00 0.78 0.49 0.17 0.06 0.01 -0.02 -0.01 0.01
-0.06 -0.10 -0.09 -0.05 -0.45 -0.03 0.01 -0.02 0.04 -0.03 -0.02 -0.11 0.37 0.78 1.00 0.74 0.41 0.26 0.16 0.07 0.04 0.02
-0.14 0.08 0.05 -0.21 -0.25 -0.01 0.02 -0.02 0.05 -0.05 0.07 -0.10 0.17 0.49 0.74 1.00 0.75 0.63 0.49 0.33 0.19 0.08
-0.20 0.14 0.11 -0.30 0.07 0.01 0.02 0.04 -0.04 0.09 -0.06 0.07 0.17 0.41 0.75 1.00 0.82 0.68 0.50 0.29 0.13 0.01
-0.20 0.17 0.11 -0.26 0.17 0.01 -0.02 0.03 -0.03 0.07 -0.04 0.05 0.06 0.26 0.63 0.82 1.00 0.70 0.54 0.33 0.15 0.01
-0.17 0.14 0.11 -0.14 0.20 0.01 -0.11 -0.03 0.01 0.01 0.04 -0.02 0.05 0.01 0.16 0.49 0.68 0.70 1.00 0.53 0.35 0.16 0.01
-0.13 0.11 0.09 -0.03 0.18 -0.03 -0.16 0.05 -0.01 0.07 -0.01 -0.01 0.05 -0.02 0.07 0.33 0.50 0.54 0.53 1.00 0.31 0.16 -0.24
-0.09 0.08 0.04 0.03 0.13 -0.09 -0.19 -0.07 -0.01 0.06 -0.04 0.01 0.06 -0.01 0.04 0.19 0.29 0.33 0.35 0.31 1.00 0.15 -0.27
-0.06 0.06 0.04 0.04 0.07 -0.23 -0.04 -0.01 0.02 0.08 -0.11 0.06 0.01 0.02 0.08 0.13 0.15 0.16 0.16 0.15 1.00 -0.26
0.01 0.01 0.01 -0.24 1.00
0.01 -0.27 1.00
-0.01 0.01 0.03 -0.01 0.01 -0.26 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 100: Variable: q2, Phase-space region: pBℓ > 2.1 GeV, Experimental cut: pBℓ > 1.0
GeV
151
2. pBℓ fit2072
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV2073
0
200
400
600
800
1000
1200
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
FIG. 101: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
152
DFN[1]
mu_other_bkgff_DststBroad[0]mu_signal_Xclnu
mu_sideband_Xclnu
gammaS
bf_B0toDetalnu
f+-/00
MCStatsignal[11]
FEI_B0
0.05
0.00
0.05
bf_B0toDstetalnu
FEI_Bp
HybridModelbf_BptoDstetalnuSlow_Pi0[0]bf_BptoDetalnuMCStatsignal[1]MCStatsignal[10]MCStatsignal[9]leptonID[0]
0.05
0.00
0.05
MCStatsignal[0]bf_B0torholnu
DFN[2]
bf_Bptorholnubf_B0topilnuleptonID[3]Cont.Norm.[0]bf_BptoDstpipilnu
MCStatsideband[11]
Tracking
0.05
0.00
0.05
2
0
2
```
(
```
```
) /
```
= + = = + = pulls
2
0
2
```
(
```
```
) /
```
2
0
2
```
(
```
```
) /
```
FIG. 102: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
153
```
4 2 0 2 4( in)/0
```
50
100
150
200
Trials
```
G = 0.034±0.014G = 1.002±0.010
```
```
4 2 0 2 4( in)/0
```
50
100
150
200
250
Trials
```
G = -0.024±0.015G = 1.047±0.010
```
```
4 2 0 2 4( in)/0
```
50
100
150
200
Trials
```
G = 0.025±0.014G = 1.003±0.010
```
FIG. 103: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom: Xcℓν factor pulls
```
```
(bin 11)
```
154
Slow_Pi0[0]Slow_Pi0[1]bf_B0toDetalnubf_B0toDstetalnubf_BptoDetalnubf_BptoDstetalnubf_charm_decaysf+-/00ff_DststBroad[0]ff_DststBroad[2]DFN[1]HybridModel
mu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]mu_Xclnu_shape[10]mu_Xclnu_shape[11]
Slow_Pi0[0]
Slow_Pi0[1]
bf_B0toDetalnu
bf_B0toDstetalnu
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
f+-/00
ff_DststBroad[0]
ff_DststBroad[2]
DFN[1]
HybridModel
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
mu_Xclnu_shape[10]
mu_Xclnu_shape[11]
1.00 -0.24 0.35 0.13 0.12 -0.04 -0.22 0.12 -0.63 0.15 0.09 -0.16 -0.31 0.25 0.02 0.34 0.31 0.27 0.18 0.10 -0.07 -0.17 -0.26 -0.30 -0.30 -0.38
-0.24 1.00 -0.16 -0.05 -0.16 0.18 0.15 -0.11 0.39 -0.11 0.08 -0.13 -0.11 -0.12 0.05 -0.21 -0.03 -0.01 0.01 0.06 0.11 0.20 0.26 0.31 0.33 0.34 0.38
0.35 -0.16 1.00 0.08 0.21 -0.21 -0.33 0.10 -0.59 0.12 -0.01 0.06 -0.03 -0.09 0.08 0.05 0.23 0.21 0.18 0.12 0.07 -0.05 -0.14 -0.22 -0.25 -0.25 -0.29
0.13 -0.05 0.08 1.00 0.05 -0.06 0.07 0.01 -0.21 0.04 0.03 -0.02 -0.11 -0.12 0.13 -0.05 0.20 0.19 0.18 0.14 0.13 0.10 0.06 0.04 0.04 0.04 0.02
0.12 -0.16 0.21 0.05 1.00 -0.16 -0.35 0.15 -0.46 0.11 -0.11 0.19 0.38 0.36 -0.48 0.35 -0.36 -0.35 -0.33 -0.35 -0.36 -0.40 -0.42 -0.43 -0.43 -0.42 -0.36
-0.04 0.18 -0.21 -0.06 -0.16 1.00 0.36 -0.07 0.19 -0.06 0.12 -0.13 -0.17 -0.23 0.07 -0.20 0.05 0.09 0.09 0.14 0.17 0.21 0.25 0.30 0.34 0.35 0.36
-0.22 0.15 -0.33 0.07 -0.35 0.36 1.00 -0.24 0.53 -0.12 0.18 -0.33 -0.45 -0.47 0.51 -0.62 0.44 0.50 0.54 0.62 0.68 0.77 0.81 0.82 0.83 0.83 0.78
0.12 -0.11 0.10 0.01 0.15 -0.07 -0.24 1.00 -0.23 0.05 -0.05 0.09 0.08 0.18 -0.18 0.17 -0.15 -0.17 -0.19 -0.22 -0.24 -0.28 -0.30 -0.30 -0.31 -0.30 -0.29
-0.63 0.39 -0.59 -0.21 -0.46 0.19 0.53 -0.23 1.00 -0.25 0.12 -0.27 -0.12 -0.18 -0.06 -0.29 -0.19 -0.14 -0.10 0.02 0.14 0.36 0.50 0.63 0.67 0.68 0.74
0.15 -0.11 0.12 0.04 0.11 -0.06 -0.12 0.05 -0.25 1.00 -0.02 0.05 0.04 0.03 -0.03 0.06 0.01 0.01 0.02 0.01 -0.05 -0.07 -0.11 -0.13 -0.14 -0.15
0.08 -0.01 0.03 -0.11 0.12 0.18 -0.05 0.12 -0.02 1.00 -0.03 -0.66 -0.28 0.19 -0.15 0.18 0.20 0.21 0.23 0.25 0.27 0.27 0.27 0.26 0.26 0.19
0.09 -0.13 0.06 -0.02 0.19 -0.13 -0.33 0.09 -0.27 0.05 -0.03 1.00 0.22 0.36 -0.25 0.18 -0.22 -0.25 -0.28 -0.32 -0.35 -0.40 -0.42 -0.43 -0.44 -0.44 -0.42
-0.16 -0.11 -0.03 -0.11 0.38 -0.17 -0.45 0.08 -0.12 0.04 -0.66 0.22 1.00 0.69 -0.67 0.51 -0.63 -0.66 -0.67 -0.69 -0.69 -0.67 -0.63 -0.58 -0.56 -0.55 -0.44
-0.31 -0.12 -0.09 -0.12 0.36 -0.23 -0.47 0.18 -0.18 0.03 -0.28 0.36 0.69 1.00 -0.75 0.82 -0.74 -0.78 -0.80 -0.83 -0.85 -0.84 -0.81 -0.76 -0.73 -0.73 -0.63
0.25 0.05 0.08 0.13 -0.48 0.07 0.51 -0.18 -0.06 -0.03 0.19 -0.25 -0.67 -0.75 1.00 -0.77 0.93 0.96 0.96 0.94 0.91 0.82 0.73 0.63 0.57 0.55 0.40
0.02 -0.21 0.05 -0.05 0.35 -0.20 -0.62 0.17 -0.29 0.06 -0.15 0.18 0.51 0.82 -0.77 1.00 -0.71 -0.77 -0.80 -0.85 -0.87 -0.89 -0.87 -0.83 -0.80 -0.79 -0.70
0.34 -0.03 0.23 0.20 -0.36 0.05 0.44 -0.15 -0.19 0.01 0.18 -0.22 -0.63 -0.74 0.93 -0.71 1.00 0.96 0.96 0.93 0.89 0.77 0.67 0.55 0.50 0.48 0.33
0.31 -0.01 0.21 0.19 -0.35 0.09 0.50 -0.17 -0.14 0.01 0.20 -0.25 -0.66 -0.78 0.96 -0.77 0.96 1.00 0.98 0.97 0.93 0.83 0.73 0.62 0.57 0.55 0.40
0.27 0.01 0.18 0.18 -0.33 0.09 0.54 -0.19 -0.10 0.02 0.21 -0.28 -0.67 -0.80 0.96 -0.80 0.96 0.98 1.00 0.98 0.96 0.87 0.77 0.67 0.61 0.59 0.45
0.18 0.06 0.12 0.14 -0.35 0.14 0.62 -0.22 0.02 0.01 0.23 -0.32 -0.69 -0.83 0.94 -0.85 0.93 0.97 0.98 1.00 0.98 0.93 0.85 0.76 0.72 0.70 0.56
0.10 0.11 0.07 0.13 -0.36 0.17 0.68 -0.24 0.14 0.25 -0.35 -0.69 -0.85 0.91 -0.87 0.89 0.93 0.96 0.98 1.00 0.96 0.91 0.84 0.80 0.78 0.66
-0.07 0.20 -0.05 0.10 -0.40 0.21 0.77 -0.28 0.36 -0.05 0.27 -0.40 -0.67 -0.84 0.82 -0.89 0.77 0.83 0.87 0.93 0.96 1.00 0.98 0.94 0.92 0.90 0.81
-0.17 0.26 -0.14 0.06 -0.42 0.25 0.81 -0.30 0.50 -0.07 0.27 -0.42 -0.63 -0.81 0.73 -0.87 0.67 0.73 0.77 0.85 0.91 0.98 1.00 0.98 0.97 0.96 0.89
-0.26 0.31 -0.22 0.04 -0.43 0.30 0.82 -0.30 0.63 -0.11 0.27 -0.43 -0.58 -0.76 0.63 -0.83 0.55 0.62 0.67 0.76 0.84 0.94 0.98 1.00 0.99 0.99 0.94
-0.30 0.33 -0.25 0.04 -0.43 0.34 0.83 -0.31 0.67 -0.13 0.26 -0.44 -0.56 -0.73 0.57 -0.80 0.50 0.57 0.61 0.72 0.80 0.92 0.97 0.99 1.00 0.99 0.96
-0.30 0.34 -0.25 0.04 -0.42 0.35 0.83 -0.30 0.68 -0.14 0.26 -0.44 -0.55 -0.73 0.55 -0.79 0.48 0.55 0.59 0.70 0.78 0.90 0.96 0.99 0.99 1.00 0.96
-0.38 0.38 -0.29 0.02 -0.36 0.36 0.78 -0.29 0.74 -0.15 0.19 -0.42 -0.44 -0.63 0.40 -0.70 0.33 0.40 0.45 0.56 0.66 0.81 0.89 0.94 0.96 0.96 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 104: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
155
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2, Experimental cut: pBℓ > 1.02074
GeV, MX < 1.7 GeV, q2 > 8 GeV22075
0
100
200
300
400
500
600
700
800
events
signalpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
2500
5000
7500
10000
12500
15000
17500
20000
events
sidebandpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
100
200
300
400
500
600
700
800
events
signalpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
0
2500
5000
7500
10000
12500
15000
17500
20000
events
sidebandpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6pB [GeV]0.5
0.75
1.0
1.25
data / model
FIG. 105: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2
156
DFN[1]
mu_signal_Xclnu
gammaSHybridModelFEI_B0FEI_Bp
MCStatsignal[7]
f+-/00leptonID[0]
mu_sideband_Xclnu
0.05
0.00
0.05
DFN[2]
bf_B0topilnubf_B0torholnubf_BptorholnuMCStatsignal[6]Trackingff_Pion[3]bf_Bptopilnubf_charm_decaysMCStatsignal[5]
0.05
0.00
0.05
leptonID[1]Cont.Norm.[0]Slow_Pip[0]ff_Pion[4]leptonID[2]
bf_BptoomegalnuCont.Norm.[1]MCStatsideband[7]MCStatsignal[2]
ff_Rho[9]
0.05
0.00
0.05
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 106: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2
157
```
4 2 0 2 4( in)/0
```
50
100
150
200
Trials
```
G = -0.004±0.014G = 1.003±0.010
```
```
4 2 0 2 4( in)/0
```
50
100
150
200
Trials
```
G = -0.018±0.014G = 0.997±0.010
```
```
4 2 0 2 4( in)/0
```
50
100
150
200
Trials
```
G = 0.009±0.014G = 1.011±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 0.9925±0.0025) in+(0.0070±0.0022)
```
FIG. 107: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
```
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2. Top left: signal pulls; top
```
```
right: Xcℓν factor pulls (bin 1); bottom left: Xcℓν factor pulls (bin 9); bottom right:
```
linearity check
Slow_Pi0[0]Slow_Pi0[1]bf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_sideband_Xclnumu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]
Slow_Pi0[0]
Slow_Pi0[1]
bf_charm_decays
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
1.00 -0.01 -0.01 0.06 -0.02 -0.02 -0.04 0.07 -0.34 -0.35 -0.37 -0.39 -0.40 -0.39 -0.37 -0.36
-0.01 1.00 -0.02 0.01 -0.02 0.01 -0.02 0.15 0.14 0.15 0.16 0.18 0.19 0.19 0.22
-0.02 1.00 0.02 0.02 -0.05 -0.04 -0.03 -0.04 0.51 0.54 0.57 0.61 0.66 0.67 0.66 0.56
0.02 1.00 0.02 0.05 -0.02 -0.02 -0.02 -0.57 -0.54 -0.45 -0.33 -0.11 0.01 0.06 0.04
-0.01 0.01 0.02 0.02 1.00 0.11 -0.02 -0.67 -0.02 0.15 0.01 0.01 0.01 0.02 0.02 0.02 -0.12
0.06 -0.02 -0.05 0.05 0.11 1.00 0.16 0.20 0.06 -0.62 -0.13 -0.12 -0.12 -0.12 -0.12 -0.12 -0.11 -0.08
-0.02 -0.02 -0.02 0.16 1.00 0.25 -0.02 0.10 0.03 0.04 0.03 0.02 0.03 0.01 0.03 0.06
-0.02 0.01 -0.04 -0.67 0.20 0.25 1.00 0.06 -0.54 0.10
-0.04 -0.03 -0.02 -0.02 0.06 -0.02 0.06 1.00 0.08 -0.35 -0.36 -0.38 -0.41 -0.44 -0.44 -0.44 -0.39
0.07 -0.02 -0.04 -0.02 0.15 -0.62 0.10 -0.54 0.08 1.00 -0.05 -0.07 -0.08 -0.08 -0.09 -0.09 -0.08 -0.10
-0.34 0.15 0.51 -0.57 -0.13 0.03 -0.35 -0.05 1.00 0.97 0.95 0.92 0.83 0.76 0.71 0.66
-0.35 0.14 0.54 -0.54 0.01 -0.12 0.04 -0.36 -0.07 0.97 1.00 0.98 0.95 0.87 0.80 0.75 0.69
-0.37 0.15 0.57 -0.45 0.01 -0.12 0.03 -0.38 -0.08 0.95 0.98 1.00 0.97 0.91 0.84 0.80 0.73
-0.39 0.16 0.61 -0.33 0.01 -0.12 0.02 -0.41 -0.08 0.92 0.95 0.97 1.00 0.94 0.90 0.85 0.78
-0.40 0.18 0.66 -0.11 0.02 -0.12 0.03 -0.44 -0.09 0.83 0.87 0.91 0.94 1.00 0.96 0.93 0.85
-0.39 0.19 0.67 0.01 0.02 -0.12 0.01 -0.44 -0.09 0.76 0.80 0.84 0.90 0.96 1.00 0.94 0.86
-0.37 0.19 0.66 0.06 0.02 -0.11 0.03 -0.44 -0.08 0.71 0.75 0.80 0.85 0.93 0.94 1.00 0.85
-0.36 0.22 0.56 0.04 -0.12 -0.08 0.06 0.10 -0.39 -0.10 0.66 0.69 0.73 0.78 0.85 0.86 0.85 1.00
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 108: Variable: pBℓ , Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV, q2 > 8 GeV2
158
3. MX fit2076
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV2077
0
500
1000
1500
2000
2500
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 1 2 3 4 5MX [GeV]0.5
0.75
1.0
1.25
data / model
0
25000
50000
75000
100000
125000
150000
175000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 1 2 3 4 5MX [GeV]0.5
0.75
1.0
1.25
data / model
0
500
1000
1500
2000
2500
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 1 2 3 4 5MX [GeV]0.5
0.75
1.0
1.25
data / model
0
25000
50000
75000
100000
125000
150000
175000
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
0 1 2 3 4 5MX [GeV]0.5
0.75
1.0
1.25
data / model
FIG. 109: Variable: MX , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
159
DFN[1]
HybridModelgammaS
DFN[2]FEI_B0
mu_signal_Xclnumu_other_bkgMCStatsignal[0]bf_BptoXulnu
FEI_Bp
0.10
0.05
0.00
0.05
0.10
ff_DststBroad[0]bf_B0toDstetalnuMCStatsignal[1]
f+-/00
bf_B0topilnubf_Bptorholnubf_B0toXulnuleptonID[0]MCStatsignal[3]bf_BptoDstetalnu
0.10
0.05
0.00
0.05
0.10
bf_B0torholnuSlow_Pi0[0]Cont.Norm.[0]
mu_sideband_Xclnu
Cont.Norm.[1]
Tracking
MCStatsignal[2]bf_Bptopilnubf_B0toDetalnubf_BptoDlnu
0.10
0.05
0.00
0.05
0.10
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 110: Variable: MX , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
160
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.030±0.015G = 1.026±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.053±0.014G = 0.988±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.004±0.014G = 1.012±0.010
```
FIG. 111: Variable: MX , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom: Xcℓν factor pulls
```
```
(bin 3)
```
bf_BptoDetalnubf_BptoDstetalnubf_charm_decays[0]bf_charm_decays[1]
f+-/00
ff_DststBroad[0]
DFN[1]HybridModel
mu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays[0]
bf_charm_decays[1]
f+-/00
ff_DststBroad[0]
DFN[1]
HybridModel
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
1.00 -0.13 -0.02 0.10 -0.03 -0.11 0.02 0.01 -0.01 -0.06 -0.07 0.05 -0.09 -0.27 -0.04
-0.13 1.00 0.03 0.13 -0.02 -0.12 0.03 -0.09 0.02 0.05 -0.08 0.16 -0.06 -0.24 -0.17
-0.02 0.03 1.00 -0.10 -0.11 0.04 0.05 0.02 0.01 -0.25 -0.09 -0.08 -0.06 0.14 0.20
0.10 0.13 -0.10 1.00 -0.05 0.06 -0.01 -0.11 0.08 -0.05 -0.01 -0.01 0.70 0.17 -0.03
-0.03 -0.02 -0.11 -0.05 1.00 0.03 0.02 -0.07 -0.04 -0.03 -0.23 -0.06 0.01 0.01
-0.11 -0.12 0.04 0.06 1.00 -0.03 0.03 0.01 -0.13 0.14 -0.13 -0.26 -0.10
0.02 0.03 0.05 -0.01 0.03 1.00 -0.06 -0.64 -0.04 -0.03 0.33 0.04 0.03 0.03
0.01 -0.09 0.02 -0.11 0.02 -0.03 -0.06 1.00 -0.54 0.01 0.04 0.08 0.22 0.15
-0.01 0.02 0.01 0.08 -0.07 0.03 -0.64 -0.54 1.00 0.08 -0.07 -0.34 -0.05 -0.10 -0.02
-0.06 0.05 -0.25 -0.05 -0.04 0.01 -0.04 0.08 1.00 -0.07 0.13 0.07 0.12 0.17
-0.07 -0.08 -0.09 -0.01 -0.03 -0.13 -0.03 0.01 -0.07 -0.07 1.00 -0.11 0.08 -0.04 -0.72
0.05 0.16 -0.08 -0.01 -0.23 0.14 0.33 0.04 -0.34 0.13 -0.11 1.00 -0.24 -0.42 -0.17
-0.09 -0.06 -0.06 0.70 -0.06 -0.13 0.04 0.08 -0.05 0.07 0.08 -0.24 1.00 0.64 0.21
-0.27 -0.24 0.14 0.17 0.01 -0.26 0.03 0.22 -0.10 0.12 -0.04 -0.42 0.64 1.00 0.52
-0.04 -0.17 0.20 -0.03 0.01 -0.10 0.03 0.15 -0.02 0.17 -0.72 -0.17 0.21 0.52 1.00
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 112: Variable: MX , Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
161
4. MX :q2 fit2078
The two-dimensional bins of MX :q2 are flattened resulting in a total of 17 bins simply labelled2079
1 to 17.2080
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV2081
0
250
500
750
1000
1250
1500
1750
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12 14 16D2_bin_mx0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12 14 16D2_bin_mx0.5
0.75
1.0
1.25
data / model
0
250
500
750
1000
1250
1500
1750
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12 14 16D2_bin_mx0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12 14 16D2_bin_mx0.5
0.75
1.0
1.25
data / model
FIG. 113: Variable: MX :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut:
pBℓ > 1.0 GeV
162
DFN[1]
mu_other_bkgmu_signal_Xclnu
gammaS
mu_sideband_Xclnu
FEI_B0FEI_Bp
MCStatsignal[7]
f+-/00leptonID[0]
0.05
0.00
0.05
MCStatsignal[0]MCStatsignal[6]bf_BptoDetalnu
DFN[2]
bf_BptoXulnubf_BptoDstetalnubf_B0topilnubf_B0toXulnubf_Bptorholnubf_B0toDetalnu
0.05
0.00
0.05
MCStatsignal[5]bf_B0toDstetalnubf_B0torholnuMCStatsignal[13]
ff_Pion[3]Slow_Pi0[0]bf_BptopilnuHybridModel
bf_charm_decays[1]MCStatsignal[1]
0.05
0.00
0.05
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 114: Variable: MX :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut:
pBℓ > 1.0 GeV
163
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.010±0.014G = 1.025±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.019±0.014G = 1.004±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
300
350
Trials
```
G = -0.052±0.017G = 1.183±0.012
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 0.9857±0.0021) in+(0.0166±0.0019)
```
FIG. 115: Variable: MX :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut:
```
pBℓ > 1.0 GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom left:
```
```
Xcℓν factor pulls (bin 16); bottom right: linearity test
```
164
Slow_Pi0[0]bf_B0toDetalnubf_B0toDstetalnubf_BptoDetalnubf_BptoDstetalnu
bf_charm_decays[0]bf_charm_decays[1]ff_DststBroad[0]
DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]mu_Xclnu_shape[10]mu_Xclnu_shape[11]mu_Xclnu_shape[12]mu_Xclnu_shape[13]mu_Xclnu_shape[14]mu_Xclnu_shape[15]mu_Xclnu_shape[16]
Slow_Pi0[0]
bf_B0toDetalnu
bf_B0toDstetalnu
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays[0]
bf_charm_decays[1]
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
mu_Xclnu_shape[10]
mu_Xclnu_shape[11]
mu_Xclnu_shape[12]
mu_Xclnu_shape[13]
mu_Xclnu_shape[14]
mu_Xclnu_shape[15]
mu_Xclnu_shape[16]
1.00 0.02 -0.12 0.10 0.01 -0.07 -0.09 -0.11 -0.04 0.06 0.13 -0.16 -0.24 0.21 -0.03 -0.08 -0.17 -0.26 -0.30 -0.30 -0.26 -0.12 -0.04 -0.06 -0.28 0.03 0.08 -0.08 0.19 0.19
0.02 1.00 -0.03 -0.09 -0.03 -0.12 0.01 0.15 0.04 0.16 0.08 0.06 -0.18 -0.33 0.15 -0.10 -0.04 0.10 0.16 0.23 0.30 -0.17 -0.18 -0.10 0.05 0.10 -0.13 -0.02 0.34 0.23
-0.12 -0.03 1.00 0.07 -0.26 -0.09 0.03 -0.01 0.06 -0.04 0.04 -0.03 -0.21 -0.05 0.06 0.06 0.13 0.14 0.18 0.21 0.23 0.27 -0.01 -0.12 -0.02 0.10 -0.21 -0.10 0.02 -0.02
0.10 -0.09 0.07 1.00 -0.39 -0.06 0.08 -0.02 0.02 0.19 -0.02 -0.03 -0.34 -0.20 -0.04 0.22 0.27 0.28 0.33 0.34 0.35 -0.33 -0.22 0.03 0.16 -0.38 -0.13 0.01 0.16 0.18
0.01 -0.03 -0.26 -0.39 1.00 -0.11 -0.03 -0.09 0.04 0.02 0.15 0.10 0.13 -0.23 0.22 0.05 0.01 -0.07 -0.09 -0.12 -0.09 -0.05 -0.18 -0.04 -0.08 -0.08 -0.05 -0.10 0.02 0.18 0.15
-0.07 -0.12 -0.09 -0.06 -0.11 1.00 0.03 -0.37 -0.05 -0.23 -0.20 0.41 0.61 -0.12 0.36 0.40 0.50 0.50 0.40 0.19 -0.14 -0.01 0.35 0.47 0.54 -0.38 0.04 0.25 -0.61 -0.44
-0.09 0.01 0.03 0.08 -0.03 0.03 1.00 -0.04 -0.03 -0.03 -0.03 -0.04 -0.10 0.05 0.03 0.18 0.23 0.24 0.26 0.31 0.39 0.41 -0.40 -0.22 -0.13 -0.18 -0.25 -0.19 -0.16 -0.06 -0.09
-0.11 0.15 -0.01 -0.02 -0.09 -0.37 -0.04 1.00 0.03 -0.05 -0.12 0.01 -0.10 -0.28 0.54 -0.64 -0.72 -0.64 -0.48 -0.34 -0.19 0.10 -0.69 -0.83 -0.60 0.20 -0.64 -0.84 0.24 -0.20
-0.04 0.04 0.06 0.02 0.04 -0.05 -0.03 0.03 1.00 -0.33 -0.10 -0.61 -0.11 -0.02 0.22 0.02 0.04 0.06 0.07 0.09 0.06 -0.03 -0.04 -0.01 0.06 -0.05 -0.07 -0.02 0.01 -0.02
0.06 0.16 -0.04 0.19 0.02 -0.23 -0.03 -0.05 -0.33 1.00 0.17 0.05 -0.03 -0.40 -0.07 0.03 0.05 -0.03 -0.07 -0.07 -0.05 0.03 -0.03 0.02 0.03 -0.03 0.21 0.21 0.17 0.41 0.46
0.08 0.04 -0.02 0.15 -0.03 -0.12 -0.10 0.17 1.00 0.23 -0.07 0.05 0.06 0.09 0.08 0.08 0.06 0.04 0.03 -0.06 0.05 0.08 0.10 -0.07 0.05 0.12 0.06 0.10
0.13 0.06 -0.03 -0.03 0.10 -0.20 -0.04 0.01 -0.61 0.05 0.23 1.00 0.22 -0.36 -0.12 -0.03 -0.09 -0.19 -0.24 -0.24 -0.20 -0.08 0.09 0.02 -0.06 -0.20 0.28 0.19 0.05 0.38 0.37
-0.16 -0.18 -0.21 -0.34 0.13 0.41 -0.10 -0.10 -0.11 -0.03 0.22 1.00 0.02 0.11 -0.11 -0.19 -0.25 -0.34 -0.43 -0.50 0.28 0.29 0.13 -0.05 0.35 0.33 0.15 0.04 0.13
-0.24 -0.33 -0.05 -0.20 -0.23 0.61 0.05 -0.28 -0.02 -0.40 -0.07 -0.36 0.02 1.00 -0.33 0.21 0.23 0.40 0.42 0.36 0.21 -0.06 0.05 0.31 0.38 0.45 -0.43 -0.07 0.14 -0.98 -0.83
0.21 0.15 0.06 -0.04 0.22 -0.12 0.03 0.54 0.22 -0.07 0.05 -0.12 0.11 -0.33 1.00 -0.48 -0.50 -0.47 -0.37 -0.29 -0.20 -0.08 -0.22 -0.62 -0.65 -0.51 -0.09 -0.57 -0.66 0.25 -0.08
-0.03 -0.10 0.06 0.05 0.36 0.18 -0.64 0.03 0.06 -0.03 0.21 -0.48 1.00 0.84 0.75 0.64 0.54 0.43 0.26 0.14 0.67 0.75 0.64 -0.06 0.53 0.71 -0.17 0.15
-0.08 -0.04 0.13 0.22 0.01 0.40 0.23 -0.72 0.02 0.05 0.09 -0.09 -0.11 0.23 -0.50 0.84 1.00 0.91 0.82 0.74 0.62 0.43 -0.08 0.59 0.79 0.77 -0.30 0.43 0.75 -0.21 0.13
-0.17 0.14 0.27 -0.07 0.50 0.24 -0.64 0.04 -0.03 0.08 -0.19 -0.19 0.40 -0.47 0.75 0.91 1.00 0.94 0.87 0.75 0.51 -0.17 0.48 0.75 0.85 -0.49 0.23 0.65 -0.39 -0.10
-0.26 0.10 0.18 0.28 -0.09 0.50 0.26 -0.48 0.06 -0.07 0.08 -0.24 -0.25 0.42 -0.37 0.64 0.82 0.94 1.00 0.94 0.84 0.61 -0.21 0.32 0.61 0.84 -0.57 0.03 0.49 -0.42 -0.21
-0.30 0.16 0.21 0.33 -0.12 0.40 0.31 -0.34 0.07 -0.07 0.06 -0.24 -0.34 0.36 -0.29 0.54 0.74 0.87 0.94 1.00 0.89 0.71 -0.26 0.17 0.47 0.75 -0.59 -0.10 0.36 -0.37 -0.23
-0.30 0.23 0.23 0.34 -0.09 0.19 0.39 -0.19 0.09 -0.05 0.04 -0.20 -0.43 0.21 -0.20 0.43 0.62 0.75 0.84 0.89 1.00 0.80 -0.30 0.01 0.29 0.59 -0.54 -0.20 0.22 -0.23 -0.17
-0.26 0.30 0.27 0.35 -0.05 -0.14 0.41 0.06 0.03 0.03 -0.08 -0.50 -0.06 -0.08 0.26 0.43 0.51 0.61 0.71 0.80 1.00 -0.30 -0.18 0.04 0.32 -0.38 -0.26 0.05 0.04
-0.12 -0.17 -0.01 -0.33 -0.18 -0.01 -0.40 0.10 -0.03 -0.03 -0.06 0.09 0.28 0.05 -0.22 0.14 -0.08 -0.17 -0.21 -0.26 -0.30 -0.30 1.00 0.42 0.16 0.03 0.60 0.40 0.15 0.03 0.09
-0.04 -0.18 -0.12 -0.22 -0.04 0.35 -0.22 -0.69 -0.04 0.02 0.05 0.02 0.29 0.31 -0.62 0.67 0.59 0.48 0.32 0.17 0.01 -0.18 0.42 1.00 0.84 0.59 0.27 0.81 0.83 -0.21 0.19
-0.06 -0.10 -0.02 0.03 -0.08 0.47 -0.13 -0.83 -0.01 0.03 0.08 -0.06 0.13 0.38 -0.65 0.75 0.79 0.75 0.61 0.47 0.29 0.04 0.16 0.84 1.00 0.81 -0.07 0.70 0.92 -0.31 0.13
-0.28 0.05 0.10 0.16 -0.08 0.54 -0.18 -0.60 0.06 -0.03 0.10 -0.20 -0.05 0.45 -0.51 0.64 0.77 0.85 0.84 0.75 0.59 0.32 0.03 0.59 0.81 1.00 -0.35 0.31 0.73 -0.41 -0.10
0.03 0.10 -0.21 -0.38 -0.05 -0.38 -0.25 0.20 -0.05 0.21 -0.07 0.28 0.35 -0.43 -0.09 -0.06 -0.30 -0.49 -0.57 -0.59 -0.54 -0.38 0.60 0.27 -0.07 -0.35 1.00 0.52 0.08 0.53 0.53
0.08 -0.13 -0.10 -0.13 -0.10 0.04 -0.19 -0.64 -0.07 0.21 0.05 0.19 0.33 -0.07 -0.57 0.53 0.43 0.23 0.03 -0.10 -0.20 -0.26 0.40 0.81 0.70 0.31 0.52 1.00 0.80 0.18 0.56
-0.08 -0.02 0.01 0.02 0.25 -0.16 -0.84 -0.02 0.17 0.12 0.05 0.15 0.14 -0.66 0.71 0.75 0.65 0.49 0.36 0.22 0.05 0.15 0.83 0.92 0.73 0.08 0.80 1.00 -0.06 0.38
0.19 0.34 0.02 0.16 0.18 -0.61 -0.06 0.24 0.01 0.41 0.06 0.38 0.04 -0.98 0.25 -0.17 -0.21 -0.39 -0.42 -0.37 -0.23 0.04 0.03 -0.21 -0.31 -0.41 0.53 0.18 -0.06 1.00 0.87
0.19 0.23 -0.02 0.18 0.15 -0.44 -0.09 -0.20 -0.02 0.46 0.10 0.37 0.13 -0.83 -0.08 0.15 0.13 -0.10 -0.21 -0.23 -0.17 0.09 0.19 0.13 -0.10 0.53 0.56 0.38 0.87 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 116: Variable: MX :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut:
pBℓ > 1.0 GeV
165
5. pBℓ :q2 fit2082
The two-dimensional bins of pBℓ :q2 are flattened resulting in a total of 25 bins simply labelled2083
1 to 25.2084
1. Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0 GeV2085
0
200
400
600
800
1000
1200
1400
events
signalpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
1400
events
signalpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
10000
20000
30000
40000
events
sidebandpost-fitother_bkg
XclnuXulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
FIG. 117: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
166
DFN[1]gammaS
mu_signal_XclnuMCStatsignal[11]
FEI_B0FEI_BpleptonID[0]f+-/00
bf_B0topilnubf_Bptorholnu
0.050
0.025
0.000
0.025
0.050
bf_B0torholnuHybridModel
mu_sideband_XclnuMCStatsignal[8]bf_B0toDstetalnu
bf_BptoXulnubf_BptoDstetalnuMCStatsignal[9]bf_B0toXulnuTracking
0.050
0.025
0.000
0.025
0.050
ff_Pion[3]Slow_Pi0[1]leptonID[3]bf_Bptopilnu
bf_B0toDetalnuMCStatsignal[0]bf_BptoomegalnuMCStatsignal[6]bf_BptoDstpipilnu
ff_Rho[9]
0.050
0.025
0.000
0.025
0.050
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 118: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
167
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = 0.027±0.014G = 1.010±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.021±0.014G = 1.010±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.023±0.014G = 0.983±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 0.9982±0.0022) in+(0.0042±0.0020)
```
FIG. 119: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factors pulls (bin 1); bottom left: Xcℓν factor
```
```
pulls (bin 24); bottom right: linearity test
```
168
Slow_Pi0[0]bf_B0toDstetalnubf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]ff_DststBroad[2]DFN[1]HybridModelgammaSmu_signal_Xulnu_inmu_sideband_Xclnumu_other_bkgmu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]mu_Xclnu_shape[10]mu_Xclnu_shape[11]MCStatsideband[2]MCStatsideband[9]
Slow_Pi0[0]
bf_B0toDstetalnu
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
ff_DststBroad[2]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_other_bkg
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
mu_Xclnu_shape[10]
mu_Xclnu_shape[11]
MCStatsideband[2]
MCStatsideband[9]
1.00 -0.03 -0.02 0.14 -0.12 0.01 -0.01 0.02 0.03 -0.13 0.02 0.13 -0.02 -0.01 -0.15 -0.03 -0.01 -0.20 -0.08 -0.10 -0.21 -0.12 -0.12 -0.15
-0.03 1.00 -0.06 -0.12 0.14 -0.09 0.02 0.02 -0.04 -0.02 0.12 -0.15 0.09 0.14 -0.25 -0.09 0.12 -0.21 -0.03 0.08 0.07 0.13 0.15 0.01
-0.02 -0.06 1.00 -0.12 0.04 -0.06 -0.03 0.02 0.03 0.02 0.03 -0.02 -0.22 -0.05 -0.24 -0.04 0.12 -0.32 -0.05 0.10 -0.10 0.09 0.14 0.11 0.12 0.13
-0.12 -0.12 1.00 0.07 -0.08 0.02 -0.01 0.02 -0.02 -0.08 -0.07 0.06 -0.19 0.13 0.13 -0.34 -0.07 0.16 -0.34 -0.15 0.11 0.07 0.14 0.15
0.14 0.14 0.04 0.07 1.00 0.01 0.01 -0.01 0.01 -0.04 0.19 0.03 0.02 -0.10 0.06 0.13 -0.07 0.09 0.22 0.21 0.25 0.11 0.29 0.24
-0.12 -0.09 -0.06 -0.08 1.00 -0.12 -0.01 0.01 -0.07 -0.12 -0.02 0.10 -0.40 0.01 0.10 -0.45 -0.05 0.21 -0.05 0.11 0.23 0.22 0.23
0.01 -0.03 0.01 -0.12 1.00 0.01 0.01 0.01 -0.02 -0.08 -0.03 -0.02 -0.30 -0.07 0.08 -0.13 -0.08 0.25 0.23 0.12 0.11 0.09 0.07
-0.01 0.02 0.02 0.02 0.01 0.01 1.00 0.03 -0.02 -0.62 -0.06 0.12 0.02 0.03 0.01 -0.02 0.02 -0.02 0.01 0.03 -0.03 -0.01 -0.04 0.01
0.02 0.03 -0.01 -0.01 -0.01 0.01 0.03 1.00 -0.02 -0.08 0.04 -0.05 -0.42 0.04 0.03 -0.11 0.02 0.02 -0.08 -0.03 -0.09 -0.08 -0.05 -0.10 0.01 0.02
0.02 0.02 0.02 0.01 0.01 -0.02 -0.02 1.00 0.21 -0.01 -0.05 0.14 0.02 0.02 0.04 -0.02 -0.01 0.05 -0.02 0.02 -0.01 0.05 0.04 0.01
0.03 -0.04 0.03 -0.02 -0.04 0.01 -0.62 -0.08 0.21 1.00 0.07 -0.34 0.03 0.02 0.04 0.02 0.01 0.06 0.03 0.01 0.04 0.02 0.03 -0.01
-0.13 -0.02 -0.08 0.19 -0.07 -0.02 0.04 -0.01 0.07 1.00 -0.04 0.16 0.05 -0.03 -0.12 -0.01 -0.07 -0.20 -0.06 -0.12 -0.22 -0.09 -0.15 -0.19
0.02 -0.02 -0.22 -0.07 0.03 -0.12 -0.08 -0.06 -0.05 -0.05 -0.04 1.00 -0.21 -0.48 -0.26 -0.16 0.06 0.19 0.05 0.08 0.17 0.09 -0.17 -0.02 0.02
0.13 0.12 -0.05 0.06 0.02 -0.02 -0.03 0.12 -0.42 0.14 -0.34 0.16 -0.21 1.00 0.01 0.01 0.04 -0.16 -0.16 -0.07 -0.18 -0.20 -0.12 -0.04 -0.07 -0.04
-0.02 -0.15 -0.24 -0.19 -0.10 0.10 -0.02 0.02 0.04 0.02 0.03 0.05 -0.48 0.01 1.00 0.53 0.10 0.71 0.39 0.07 0.44 0.19 0.01 0.11 -0.02 -0.03 -0.01
-0.01 0.09 -0.04 0.13 0.06 -0.40 -0.30 0.03 0.03 0.02 -0.03 -0.26 0.01 0.53 1.00 0.37 0.31 0.70 0.47 0.08 0.29 0.25 0.08 0.11 0.13
-0.15 0.14 0.12 0.13 0.13 0.01 -0.07 0.01 -0.11 0.04 0.02 -0.12 -0.16 0.04 0.10 0.37 1.00 -0.02 0.24 0.55 0.05 0.27 0.46 0.25 0.35 0.40 -0.23
-0.03 -0.25 -0.32 -0.34 -0.07 0.10 0.08 -0.02 0.02 -0.02 0.04 -0.01 0.06 -0.16 0.71 0.31 -0.02 1.00 0.51 0.09 0.66 0.42 0.12 0.07 0.02 -0.01
-0.01 -0.09 -0.05 -0.07 0.09 -0.45 -0.13 0.02 -0.01 0.02 -0.07 0.19 -0.16 0.39 0.70 0.24 0.51 1.00 0.49 0.35 0.57 0.38 0.04 0.15 0.15
-0.20 0.12 0.10 0.16 0.22 -0.05 -0.08 0.02 -0.08 0.05 0.01 -0.20 0.05 -0.07 0.07 0.47 0.55 0.09 0.49 1.00 0.18 0.54 0.74 0.31 0.53 0.61 0.01 0.01
-0.08 -0.21 -0.10 -0.34 0.21 0.25 -0.02 -0.03 -0.02 0.06 -0.06 0.08 -0.18 0.44 0.08 0.05 0.66 0.35 0.18 1.00 0.56 0.33 0.24 0.25 0.22
-0.10 -0.03 0.09 -0.15 0.21 -0.05 0.23 0.01 0.02 0.03 -0.12 0.17 -0.20 0.19 0.29 0.27 0.42 0.57 0.54 0.56 1.00 0.68 0.33 0.50 0.50 0.01
-0.21 0.08 0.14 0.11 0.25 0.11 0.12 0.03 -0.09 0.01 -0.22 0.09 -0.12 0.01 0.25 0.46 0.12 0.38 0.74 0.33 0.68 1.00 0.42 0.68 0.76 0.01 0.01
-0.12 0.07 0.11 0.07 0.11 0.23 0.11 -0.03 -0.08 -0.01 0.04 -0.09 -0.17 -0.04 0.11 0.08 0.25 0.07 0.04 0.31 0.24 0.33 0.42 1.00 0.43 0.45 -0.25
-0.12 0.13 0.12 0.14 0.29 0.22 0.09 -0.01 -0.05 0.05 0.02 -0.15 -0.07 -0.02 0.11 0.35 0.02 0.15 0.53 0.25 0.50 0.68 0.43 1.00 0.69 0.01
-0.15 0.15 0.13 0.15 0.24 0.23 0.07 -0.04 -0.10 0.04 0.03 -0.19 -0.02 -0.04 -0.03 0.13 0.40 -0.01 0.15 0.61 0.22 0.50 0.76 0.45 0.69 1.00 0.01 0.01
0.01 -0.23 0.01 0.01 0.01 1.00
0.01 0.01 0.02 0.01 -0.01 0.02 -0.01 0.01 0.01 0.01 -0.25 0.01 0.01 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 120: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
169
2. Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV, Experimental cut: pBℓ > 1.0 GeV,2086
MX < 1.7 GeV2087
0
200
400
600
800
1000
1200
events
signalpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sidebandpre-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
200
400
600
800
1000
1200
events
signalpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
0
5000
10000
15000
20000
25000
30000
35000
40000
events
sidebandpost-fitother_bkg
XclnuXulnu_out
Xulnu_in
UncertaintyData
2 4 6 8 10 12pB : q2 [GeV:GeV2]0.5
0.75
1.0
1.25
data / model
FIG. 121: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV
plb20882089
170
DFN[1]
mu_signal_Xclnu
gammaSFEI_B0
MCStatsignal[11]mu_sideband_Xclnu
FEI_Bpf+-/00leptonID[0]
HybridModel
0.05
0.00
0.05
bf_B0topilnubf_BptoDstetalnuMCStatsignal[0]bf_Bptorholnubf_B0torholnuMCStatsignal[8]MCStatsignal[6]Trackingff_Pion[3]bf_charm_decays
0.05
0.00
0.05
bf_Bptopilnu
DFN[2]
MCStatsignal[5]Cont.Norm.[0]bf_BptoomegalnuleptonID[3]Slow_Pi0[0]
ff_Rho[9]leptonID[1]
MCStatsignal[10]
0.05
0.00
0.05
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 122: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV
171
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.037±0.014G = 1.007±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.020±0.014G = 1.003±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = 0.012±0.014G = 1.010±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 0.9985±0.0023) in (0.0005±0.0021)
```
FIG. 123: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV,
```
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV. Top left: signal pulls; top right: Xcℓν
```
```
factor pulls (bin 3); bottom left: Xcℓν factor pulls (10); bottom right: linearity test
```
172
FEI_B0Slow_Pi0[0]Slow_Pi0[1]bf_B0toDetalnubf_B0toDstetalnubf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaS
mu_signal_Xulnu_inmu_sideband_Xclnumu_signal_Xclnumu_Xclnu_shape[0]mu_Xclnu_shape[1]mu_Xclnu_shape[2]mu_Xclnu_shape[3]mu_Xclnu_shape[4]mu_Xclnu_shape[5]mu_Xclnu_shape[6]mu_Xclnu_shape[7]mu_Xclnu_shape[8]mu_Xclnu_shape[9]mu_Xclnu_shape[10]mu_Xclnu_shape[11]
FEI_B0
Slow_Pi0[0]
Slow_Pi0[1]
bf_B0toDetalnu
bf_B0toDstetalnu
bf_BptoDetalnu
bf_BptoDstetalnu
bf_charm_decays
ff_DststBroad[0]
DFN[1]
HybridModel
gammaS
mu_signal_Xulnu_in
mu_sideband_Xclnu
mu_signal_Xclnu
mu_Xclnu_shape[0]
mu_Xclnu_shape[1]
mu_Xclnu_shape[2]
mu_Xclnu_shape[3]
mu_Xclnu_shape[4]
mu_Xclnu_shape[5]
mu_Xclnu_shape[6]
mu_Xclnu_shape[7]
mu_Xclnu_shape[8]
mu_Xclnu_shape[9]
mu_Xclnu_shape[10]
mu_Xclnu_shape[11]
1.00 0.04 0.12 0.10 0.03 0.07 0.06 0.08 0.25 0.04 0.08 0.03 0.15 0.09 -0.09 -0.12 -0.07 -0.12 -0.02 0.01 -0.02 0.05 0.12 0.12 0.15
0.04 1.00 0.04 -0.02 0.02 0.03 -0.04 -0.02 -0.03 0.01 0.12 0.01 0.02 -0.05 0.04 -0.18 -0.21 -0.33 -0.21 -0.22 -0.35 -0.26 -0.29 -0.38 -0.29 -0.31 -0.36
0.12 0.04 1.00 0.10 0.02 0.04 0.06 0.02 0.18 0.03 -0.01 0.02 0.03 0.08 -0.02 -0.03 0.08 0.02 -0.03 0.06 0.10 0.07 0.11 0.21 0.21 0.22
0.10 -0.02 0.10 1.00 0.01 0.04 -0.01 -0.01 0.16 0.03 0.12 0.01 0.04 -0.39 -0.29 -0.10 -0.34 -0.30 -0.14 -0.17 -0.16 -0.08 0.03 0.02 0.03
0.03 0.02 0.02 0.01 1.00 -0.01 0.01 0.04 0.02 0.08 0.01 -0.01 0.02 0.02 -0.21 -0.13 -0.04 -0.21 -0.19 -0.09 -0.18 -0.16 -0.10 -0.03 -0.02 -0.01
0.07 0.03 0.04 0.04 1.00 0.01 0.04 0.08 0.01 0.06 0.02 0.02 0.02 -0.50 -0.33 -0.13 -0.48 -0.30 -0.18 -0.34 -0.20 -0.11 -0.02 -0.04 -0.03
0.06 -0.04 0.06 -0.01 -0.01 0.01 1.00 0.04 0.02 0.05 0.10 0.01 -0.04 0.02 0.01 -0.34 -0.15 -0.03 -0.34 -0.23 -0.08 -0.30 -0.25 -0.10 -0.03
0.08 -0.02 0.02 -0.01 0.01 0.04 0.04 1.00 -0.01 0.03 0.09 0.01 0.04 0.02 0.02 -0.37 -0.36 -0.47 -0.42 -0.40 -0.50 -0.51 -0.56 -0.55 -0.49 -0.62 -0.56
0.25 -0.03 0.18 0.16 0.04 0.08 0.02 -0.01 1.00 0.05 0.15 0.04 0.03 0.05 -0.01 -0.37 -0.66 -0.35 -0.26 -0.60 -0.40 -0.05 -0.27 -0.18 0.17 0.13 0.12
0.04 0.01 0.03 0.03 0.02 0.01 0.05 0.03 0.05 1.00 -0.10 0.03 -0.59 0.03 0.01 -0.07 -0.07 -0.04 -0.07 -0.07 -0.05 -0.06 -0.06 -0.04 -0.04 -0.03 -0.04
0.08 0.12 -0.01 0.12 0.08 0.06 0.10 0.09 0.15 -0.10 1.00 0.12 0.04 0.16 -0.51 -0.28 -0.28 -0.27 -0.28 -0.29 -0.28 -0.26 -0.28 -0.27 -0.18 -0.18 -0.19
0.03 0.01 0.02 0.01 0.01 0.02 0.01 0.01 0.04 0.03 0.12 1.00 0.27 0.02 -0.04 -0.03 -0.05 -0.03 -0.03 -0.04 -0.02 -0.01 -0.03 -0.03 -0.04 0.02
0.15 0.02 0.03 -0.01 0.02 -0.04 0.04 0.03 -0.59 0.04 0.27 1.00 0.12 -0.39 -0.01 -0.03 -0.03 -0.01 -0.03 -0.03 -0.02 -0.03 -0.01 -0.01
0.09 -0.05 0.08 0.04 0.02 0.02 0.02 0.02 0.05 0.03 0.16 0.02 0.12 1.00 0.05 -0.36 -0.38 -0.46 -0.39 -0.40 -0.49 -0.45 -0.47 -0.51 -0.41 -0.46 -0.49
0.04 -0.02 0.02 0.01 0.02 -0.01 0.01 -0.51 -0.04 -0.39 0.05 1.00 -0.04 -0.04 -0.03 -0.04 -0.04 -0.05 -0.05 -0.06 -0.06 -0.04 -0.05 -0.05
-0.09 -0.18 -0.39 -0.21 -0.50 -0.34 -0.37 -0.37 -0.07 -0.28 -0.03 -0.01 -0.36 -0.04 1.00 0.89 0.70 0.97 0.92 0.80 0.85 0.86 0.74 0.45 0.53 0.53
-0.12 -0.21 -0.03 -0.29 -0.13 -0.33 -0.15 -0.36 -0.66 -0.07 -0.28 -0.05 -0.03 -0.38 -0.04 0.89 1.00 0.81 0.84 0.98 0.89 0.72 0.85 0.77 0.40 0.51 0.52
-0.33 0.08 -0.10 -0.04 -0.13 -0.03 -0.47 -0.35 -0.04 -0.27 -0.03 -0.03 -0.46 -0.03 0.70 0.81 1.00 0.71 0.81 0.91 0.73 0.85 0.88 0.62 0.74 0.76
-0.07 -0.21 0.02 -0.34 -0.21 -0.48 -0.34 -0.42 -0.26 -0.07 -0.28 -0.03 -0.01 -0.39 -0.04 0.97 0.84 0.71 1.00 0.89 0.81 0.90 0.89 0.79 0.53 0.62 0.62
-0.12 -0.22 -0.03 -0.30 -0.19 -0.30 -0.23 -0.40 -0.60 -0.07 -0.29 -0.04 -0.03 -0.40 -0.04 0.92 0.98 0.81 0.89 1.00 0.91 0.78 0.90 0.82 0.46 0.56 0.57
-0.02 -0.35 0.06 -0.14 -0.09 -0.18 -0.08 -0.50 -0.40 -0.05 -0.28 -0.02 -0.03 -0.49 -0.05 0.80 0.89 0.91 0.81 0.91 1.00 0.81 0.94 0.95 0.65 0.78 0.80
0.01 -0.26 0.10 -0.17 -0.18 -0.34 -0.30 -0.51 -0.05 -0.06 -0.26 -0.01 -0.45 -0.05 0.85 0.72 0.73 0.90 0.78 0.81 1.00 0.90 0.86 0.68 0.77 0.78
-0.02 -0.29 0.07 -0.16 -0.16 -0.20 -0.25 -0.56 -0.27 -0.06 -0.28 -0.03 -0.02 -0.47 -0.06 0.86 0.85 0.85 0.89 0.90 0.94 0.90 1.00 0.95 0.69 0.81 0.82
0.05 -0.38 0.11 -0.08 -0.10 -0.11 -0.10 -0.55 -0.18 -0.04 -0.27 -0.03 -0.03 -0.51 -0.06 0.74 0.77 0.88 0.79 0.82 0.95 0.86 0.95 1.00 0.75 0.89 0.91
0.12 -0.29 0.21 0.03 -0.03 -0.02 -0.03 -0.49 0.17 -0.04 -0.18 -0.04 -0.41 -0.04 0.45 0.40 0.62 0.53 0.46 0.65 0.68 0.69 0.75 1.00 0.80 0.81
0.12 -0.31 0.21 0.02 -0.02 -0.04 -0.62 0.13 -0.03 -0.18 0.02 -0.01 -0.46 -0.05 0.53 0.51 0.74 0.62 0.56 0.78 0.77 0.81 0.89 0.80 1.00 0.94
0.15 -0.36 0.22 0.03 -0.01 -0.03 -0.56 0.12 -0.04 -0.19 -0.01 -0.49 -0.05 0.53 0.52 0.76 0.62 0.57 0.80 0.78 0.82 0.91 0.81 0.94 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 124: Variable: pBℓ :q2, Phase-space region: pBℓ > 1.0 GeV, MX < 1.7 GeV,
Experimental cut: pBℓ > 1.0 GeV, MX < 1.7 GeV
173
G. KL2090
KL are poorly detected by the KLM detector and most of them are missed. As they are2091
produced in charm decays, they can therefore lead to mismodelling of the Xcℓν component2092
in our study. As shown in Section 7 and in particular in Fig. 39, in our case they are not2093
expected to represent the main source of data-MC disagreement. However, the KL rates in2094
the signal region and orthogonal CR0,low, could be different. As we use the later region to2095
```
correct the Xcℓν component in the former region, this difference could (at least partially)2096
```
invalidate the correction procedure. This difference is therefore discussed in this Section.2097
2098
By comparing Figures 125 to 128, the following observations can be made. First of all,2099
events with K0L seem to be well rejected by the Xcℓν MVA classifier. However, since we can2100
only reject K+ and K0S , the K veto used to define the signal region doesn’t reject events2101
where K0L are found. Being able to reject K0L could help reduce the Xcℓν background even2102
further. The different relative rates of KL events in the signal and CR0,low region used as2103
```
control region in the signal extraction procedure (c.f Section 8), could lead to a different2104
```
data-MC disagreement between the two regions. In the signal region, the KL event yields2105
are about 20% of the B → Xuℓν yields and the relative rate of KL events is about 3 times2106
higher in CR0,low than in SR so the KL modelling could impact the Xcℓν correction. In the2107
uncertainties, we factor in the different Xcℓν composition between the CR and the SR as2108
discussed in Section 8 8 which should partially cover the KL rate difference between these2109
two regions. In order to complete the study made in Section 7 3 1, we repeat the pseudo-data2110
fit described in Section 8 8 by up-scaling KL events by 30%. The branching fraction in that2111
```
case is measured to be ∆B(B → Xuℓν) = (1.58 ± 0.14) · 10−3 which differs by about 1%2112
```
```
from the Asimov result ∆B(B → Xuℓν) = (1.60 ± 0.14) · 10−3. The difference is negligible2113
```
compared to the total uncertainty.2114
3.0 1.5 0.0 1.5 3.0 4.5 6.0 7.5 9.0
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.13 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Asimov Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (2 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Asimov Data
pB > 1 GeV
```
FIG. 125: M 2miss (left) and q2 (right) distributions in the signal region split into the
```
following three components: continuum, B events where a D → K0L decay is found and B
events where no D → K0L decay is found.
174
3.0 1.5 0.0 1.5 3.0 4.5 6.0 7.5 9.0
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.13 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (2 GeV
```
```
2)
```
×104Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
```
FIG. 126: M 2miss (left) and q2 (right) distributions in CR0,low split into the following three
```
```
components: continuum, B events where a D → K0L decay is found and B events where no
```
D → K0L decay is found.
3.0 1.5 0.0 1.5 3.0 4.5 6.0 7.5 9.0
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.13 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (2 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
```
FIG. 127: M 2miss (left) and q2 (right) distributions in CRK,high split into the following three
```
```
components: continuum, B events where a D → K0L decay is found and B events where no
```
D → K0L decay is found.
175
3.0 1.5 0.0 1.5 3.0 4.5 6.0 7.5 9.0
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.13 GeV
```
```
2)
```
×103Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
```
Events / (2 GeV
```
```
2)
```
×104Continuum
B without D K0L XB with D K0L X
MC Uncert.Data
pB > 1 GeV
```
FIG. 128: M 2miss (left) and q2 (right) distributions in CRK,low split into the following three
```
```
components: continuum, B events where a D → K0L decay is found and B events where no
```
D → K0L decay is found.
176
H. HADRON ID2115
We choose the kaon/pion ID likelihood-based score rather than the neural network one as2116
the relative amount of fakes is much lower. We show below the efficiency and fake rate for2117
kaons and pions for both types of scores. We use the nominal sample after preselection.2118
Only tracks covered by the ROE mask are considered.2119
0.2 0.4 0.6 0.8 1.0ID cut
14
16
18
20
22
24
%
Efficiency
kaonIDkaonIDNN
0.2 0.4 0.6 0.8 1.0ID cut
5
10
15
20
25
30
%
Fake rate
kaonIDkaonIDNN
```
FIG. 129: Efficiency and fake rate for different likelihood-based (kaonID) and
```
```
neural-network-based (kaonIDNN) K± identification score cuts
```
0.2 0.4 0.6 0.8 1.0ID cut20
30
40
50
60
70
80
%
Efficiency
pionIDpionIDNN
0.2 0.4 0.6 0.8 1.0ID cut
2
4
6
8
10
12
14
%
Fake rate
pionIDpionIDNN
```
FIG. 130: Efficiency and fake rate for different likelihood-based (pionID) and
```
```
neural-network-based (pionIDNN) π± identification score cuts
```
177
I. FITS WITH CONTROL REGIONS2120
1. Fit 32121
We repeat for fit 3 the test that was detailed in Section 8 10 for fit 1. The CR’0,low Xcℓν2122
normalisation is equal to 1.16±0.04 and the VR’2 Xcℓν normalisation is equal to 1.18±0.04.2123
The obtained p-value is 0.62.2124
0
500
1000
1500
2000
2500
3000
3500
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
5 10 15 20 25
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
0
500
1000
1500
2000
2500
3000
3500
events
signal
post-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
5 10 15 20 25
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
5 10 15 20 25
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
102
103
104
105
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
5 10 15 20 25
```
pB : q2 [GeV:GeV2]
```
0.5
0.75
1.0
1.25
data / model
```
FIG. 131: Pre- (left) and post-fit (right) q2 distributions in VR’2 (top) and CR’0,low
```
```
(bottom) for fit 3.
```
178
0 5 10 15 20 25
```
pB : q2 [GeV:GeV2]
```
0.6
0.7
0.8
0.9
1.0
1.1
1.2
Xc shape factors
Fit output
Normalised data/MC ratio CR'0, low
Normalised data/MC ratio VR'2
FIG. 132: Comparison between the normalised Xcℓν data/MC ratio for regions CR’0,low
and VR’2 and the fit output Xcℓν shape factors.
179
3 6 9 12 15 18 21 24
```
pB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (1 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
3 6 9 12 15 18 21 24
```
pB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (1 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (2 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (2 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
```
FIG. 133: 2D pBℓ :q2 (top) and q2 (bottom) distributions in VR’2 before (left) and after
```
```
(right) applying the Xcℓν normalisation and shape corrections.
```
180
3 6 9 12 15 18 21 24
```
pB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (1 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
3 6 9 12 15 18 21 24
```
pB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
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
Events / (1 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (2 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (2 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
```
FIG. 134: 2D pBℓ :q2 (top) and q2 (bottom) distributions in CR’0,low before (left) and after
```
```
(right) applying the Xcℓν normalisation and shape corrections.
```
181
2. Fit 52125
We repeat for fit 5 the test that was detailed in Section 8 10 for fit 1. The CR’0,low Xcℓν2126
normalisation is equal to 1.22±0.02 and the VR’2 Xcℓν normalisation is equal to 1.24±0.06.2127
The obtained p-value is 0.64.2128
0
250
500
750
1000
1250
1500
1750
2000
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
pB [GeV]
0.5
0.75
1.0
1.25
data / model
0
250
500
750
1000
1250
1500
1750
2000
events
signal
post-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
pB [GeV]
0.5
0.75
1.0
1.25
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
pB [GeV]
0.5
0.75
1.0
1.25
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_out
Xulnu_in
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
pB [GeV]
0.5
0.75
1.0
1.25
data / model
```
FIG. 135: Pre- (left) and post-fit (right) q2 distributions in VR’2 (top) and CR’0,low
```
```
(bottom) for fit 5.
```
182
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75
pB [GeV]
0.85
0.90
0.95
1.00
1.05
1.10
Xc shape factors
Fit output
Normalised data/MC ratio CR'0, low
Normalised data/MC ratio VR'2
FIG. 136: Comparison between the normalised Xcℓν data/MC ratio for regions CR’0,low
and VR’2 and the fit output Xcℓν shape factors.
183
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.027 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.027 GeV)
```
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (2 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (2 GeV
```
```
2)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
```
FIG. 137: pBℓ (top) and q2 (bottom) distributions in VR’2 before (left) and after (right)
```
applying the Xcℓν normalisation and shape corrections.
184
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.027 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.027 GeV)
```
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (2 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (2 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
pB > 1 GeV
```
FIG. 138: pBℓ (top) and q2 (bottom) distributions in CR’0,low before (left) and after (right)
```
applying the Xcℓν normalisation and shape corrections.
185
J. LOW-LEPTON-MOMENTUM REGION2129
We show here kinematical distributions for a region with 0.5 < pBℓ < 1.0 GeV after applying2130
all preselections.2131
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.027 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Asimov Data
pB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Asimov Data
pB > 1 GeV
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.05 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Asimov Data
pB > 1 GeV
3.0 1.5 0.0 1.5 3.0 4.5 6.0 7.5 9.0
M2miss [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.13 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Uncert.Asimov Data
pB > 1 GeV
186
K. FIT WITH SPLIT LEPTON FLAVOUR2132
We present here the results of fit 1 with split lepton flavour.2133
Slow_Pi0[0]Slow_Pi0[1]bf_BptoDetalnubf_BptoDstetalnubf_charm_decaysff_DststBroad[0]DFN[1]HybridModelgammaSmu_signal_electron_Xulnu_inmu_signal_muon_Xulnu_inmu_sideband_electron_Xclnumu_other_bkg_electronmu_sideband_muon_Xclnumu_other_bkg_muonmu_signal_electron_Xclnumu_signal_muon_Xclnumu_Xclnu_electron_shape[0]mu_Xclnu_electron_shape[1]mu_Xclnu_electron_shape[2]mu_Xclnu_electron_shape[3]mu_Xclnu_electron_shape[4]mu_Xclnu_electron_shape[5]mu_Xclnu_electron_shape[6]mu_Xclnu_electron_shape[7]mu_Xclnu_electron_shape[8]mu_Xclnu_muon_shape[0]mu_Xclnu_muon_shape[1]mu_Xclnu_muon_shape[2]mu_Xclnu_muon_shape[3]mu_Xclnu_muon_shape[4]mu_Xclnu_muon_shape[5]mu_Xclnu_muon_shape[6]mu_Xclnu_muon_shape[7]mu_Xclnu_muon_shape[8]MCStatsignal_muon[0]
Slow_Pi0[0]Slow_Pi0[1]
bf_BptoDetalnubf_BptoDstetalnu
bf_charm_decaysff_DststBroad[0]
DFN[1]HybridModel
gammaSmu_signal_electron_Xulnu_in
mu_signal_muon_Xulnu_inmu_sideband_electron_Xclnu
mu_other_bkg_electronmu_sideband_muon_Xclnu
mu_other_bkg_muonmu_signal_electron_Xclnu
mu_signal_muon_Xclnumu_Xclnu_electron_shape[0]
mu_Xclnu_electron_shape[1]mu_Xclnu_electron_shape[2]
mu_Xclnu_electron_shape[3]mu_Xclnu_electron_shape[4]
mu_Xclnu_electron_shape[5]mu_Xclnu_electron_shape[6]
mu_Xclnu_electron_shape[7]mu_Xclnu_electron_shape[8]
mu_Xclnu_muon_shape[0]mu_Xclnu_muon_shape[1]
mu_Xclnu_muon_shape[2]mu_Xclnu_muon_shape[3]
mu_Xclnu_muon_shape[4]mu_Xclnu_muon_shape[5]
mu_Xclnu_muon_shape[6]mu_Xclnu_muon_shape[7]
mu_Xclnu_muon_shape[8]MCStatsignal_muon[0]
1.00 0.23 0.04 0.04 0.26 0.27 -0.01 0.17 -0.06 0.05 -0.01 -0.17 0.14 -0.07 0.25 0.28 -0.33 -0.42 -0.46 -0.51 -0.54 -0.53 -0.50 -0.45 -0.37 -0.21 -0.34 -0.40 -0.42 -0.41 -0.40 -0.36 -0.32 -0.27 0.010.23 1.00 0.01 0.14 0.26 0.30 0.01 0.05 -0.02 -0.01 -0.04 0.09 -0.05 -0.08 0.06 0.04 -0.12 -0.23 -0.25 -0.22 -0.17 -0.14 -0.09 -0.03 0.01 0.03 -0.12 -0.16 -0.13 -0.08 -0.05 0.05 0.09
0.04 0.01 1.00 -0.13 -0.04 0.05 0.01 0.09 -0.03 -0.01 0.01 0.04 -0.09 -0.15 0.04 0.07 -0.42 -0.33 -0.23 -0.14 -0.09 -0.04 -0.03 -0.02 -0.02 -0.15 -0.18 -0.12 -0.03 0.04 0.07 0.07 0.08 0.09 0.020.04 0.14 -0.13 1.00 0.12 0.08 0.02 0.10 -0.01 -0.03 -0.07 -0.09 0.06 0.06 0.18 0.14 0.14 -0.32 -0.28 -0.22 -0.17 -0.11 -0.09 -0.07 -0.03 -0.01 -0.36 -0.38 -0.31 -0.23 -0.17 -0.15 -0.12 -0.11 -0.11 0.01
0.26 0.26 -0.04 0.12 1.00 0.25 -0.01 0.14 -0.05 -0.01 -0.02 -0.18 0.17 0.04 0.04 0.20 0.30 -0.40 -0.49 -0.54 -0.62 -0.66 -0.64 -0.55 -0.42 -0.28 -0.30 -0.46 -0.54 -0.59 -0.60 -0.57 -0.49 -0.39 -0.25 -0.010.27 0.30 0.05 0.08 0.25 1.00 0.04 0.17 -0.03 0.03 -0.06 -0.16 0.03 -0.27 -0.29 0.24 0.17 -0.17 -0.57 -0.66 -0.58 -0.39 -0.28 -0.19 -0.09 -0.03 0.15 -0.29 -0.44 -0.34 -0.15 -0.06 0.03 0.11 0.17 0.03
-0.01 0.01 0.01 0.02 -0.01 0.04 1.00 0.09 -0.06 -0.42 -0.49 -0.01 0.02 -0.02 -0.05 0.03 0.04 -0.02 -0.03 -0.02 -0.01 -0.02 -0.10 0.03 0.01 0.01 0.02 0.02 0.03 0.01 -0.060.17 0.05 0.09 0.10 0.14 0.17 0.09 1.00 0.13 -0.24 -0.12 0.03 0.07 0.04 -0.09 -0.02 0.06 -0.23 -0.27 -0.27 -0.26 -0.24 -0.23 -0.24 -0.23 -0.20 -0.09 -0.18 -0.21 -0.21 -0.18 -0.17 -0.18 -0.18 -0.17
-0.06 -0.02 -0.01 -0.05 -0.03 -0.06 0.13 1.00 0.11 0.29 -0.06 0.01 -0.06 -0.21 0.06 -0.01 0.04 0.06 0.07 0.08 0.09 0.08 0.08 0.09 0.17 0.16 0.15 0.13 0.12 0.11 0.09 0.09 0.08 -0.020.05 -0.01 -0.03 -0.03 -0.01 0.03 -0.42 -0.24 0.11 1.00 0.29 0.23 -0.40 -0.03 -0.21 0.01 0.24 0.16 0.12 0.10 0.10 0.11 0.13 0.14 0.17 0.04 0.03 0.02 0.03 0.03 0.03 0.04 0.05 0.08
-0.01 -0.01 -0.07 -0.02 -0.06 -0.49 -0.12 0.29 0.29 1.00 0.01 0.19 -0.09 -0.02 -0.18 0.10 0.11 0.10 0.09 0.07 0.07 0.07 0.07 0.08 0.06 0.06 0.03 -0.02 -0.05 -0.07 -0.08 -0.08 -0.04 0.05-0.17 -0.04 0.01 -0.09 -0.18 -0.16 -0.01 0.03 -0.06 0.23 0.01 1.00 -0.13 0.08 0.01 0.16 -0.14 0.04 0.02 -0.04 -0.12 -0.16 -0.20 -0.24 -0.19 0.10 0.18 0.19 0.17 0.13 0.11 0.08 0.05 0.03 -0.01
0.14 0.09 0.04 0.06 0.17 0.03 0.02 0.07 0.01 -0.40 -0.13 1.00 0.03 0.01 0.06 0.07 -0.68 -0.55 -0.50 -0.50 -0.52 -0.54 -0.55 -0.53 -0.53 -0.07 -0.10 -0.11 -0.12 -0.13 -0.13 -0.12 -0.10 -0.07-0.07 -0.05 -0.09 0.06 0.04 -0.27 -0.02 0.04 -0.06 -0.03 0.19 0.08 0.03 1.00 0.36 -0.10 0.55 0.04 0.14 0.15 0.11 0.04 0.01 -0.01 -0.03 -0.02 -0.55 -0.46 -0.46 -0.57 -0.67 -0.70 -0.74 -0.76 -0.70 -0.05
-0.08 -0.15 0.18 0.04 -0.29 -0.05 -0.09 -0.21 -0.09 0.01 0.01 0.36 1.00 -0.02 -0.01 -0.03 0.09 0.12 0.08 0.02 -0.01 -0.02 -0.04 -0.02 -0.77 -0.53 -0.39 -0.35 -0.35 -0.35 -0.37 -0.40 -0.46 -0.250.25 0.06 0.04 0.14 0.20 0.24 0.03 -0.02 0.06 -0.21 -0.02 0.16 0.06 -0.10 -0.02 1.00 0.17 -0.31 -0.38 -0.39 -0.40 -0.37 -0.35 -0.31 -0.26 -0.20 -0.13 -0.24 -0.26 -0.22 -0.17 -0.14 -0.10 -0.07 -0.04 0.01
0.28 0.04 0.07 0.14 0.30 0.17 0.04 0.06 -0.01 0.01 -0.18 -0.14 0.07 0.55 -0.01 0.17 1.00 -0.26 -0.31 -0.31 -0.32 -0.30 -0.28 -0.24 -0.19 -0.14 -0.40 -0.54 -0.60 -0.65 -0.66 -0.64 -0.62 -0.57 -0.47 -0.02-0.33 -0.12 -0.42 -0.32 -0.40 -0.17 -0.02 -0.23 0.04 0.24 0.10 -0.68 0.04 -0.03 -0.31 -0.26 1.00 0.89 0.80 0.78 0.76 0.74 0.72 0.65 0.57 0.42 0.52 0.49 0.43 0.37 0.33 0.29 0.23 0.18 -0.02
-0.42 -0.23 -0.33 -0.28 -0.49 -0.57 -0.03 -0.27 0.06 0.16 0.11 0.04 -0.55 0.14 0.09 -0.38 -0.31 0.89 1.00 0.97 0.93 0.85 0.78 0.72 0.62 0.51 0.30 0.58 0.63 0.54 0.42 0.35 0.27 0.19 0.11 -0.02-0.46 -0.25 -0.23 -0.22 -0.54 -0.66 -0.02 -0.27 0.07 0.12 0.10 0.02 -0.50 0.15 0.12 -0.39 -0.31 0.80 0.97 1.00 0.97 0.89 0.82 0.75 0.64 0.52 0.24 0.56 0.64 0.58 0.46 0.38 0.30 0.21 0.12 -0.02
-0.51 -0.22 -0.14 -0.17 -0.62 -0.58 -0.01 -0.26 0.08 0.10 0.09 -0.04 -0.50 0.11 0.08 -0.40 -0.32 0.78 0.93 0.97 1.00 0.96 0.91 0.85 0.74 0.60 0.25 0.54 0.64 0.61 0.53 0.47 0.38 0.29 0.19 -0.01-0.54 -0.17 -0.09 -0.11 -0.66 -0.39 -0.24 0.09 0.10 0.07 -0.12 -0.52 0.04 0.02 -0.37 -0.30 0.76 0.85 0.89 0.96 1.00 0.97 0.93 0.83 0.68 0.28 0.49 0.58 0.60 0.57 0.54 0.47 0.39 0.29
-0.53 -0.14 -0.04 -0.09 -0.64 -0.28 -0.23 0.08 0.11 0.07 -0.16 -0.54 0.01 -0.01 -0.35 -0.28 0.74 0.78 0.82 0.91 0.97 1.00 0.95 0.86 0.72 0.28 0.44 0.52 0.57 0.57 0.54 0.49 0.42 0.32-0.50 -0.09 -0.03 -0.07 -0.55 -0.19 -0.24 0.08 0.13 0.07 -0.20 -0.55 -0.01 -0.02 -0.31 -0.24 0.72 0.72 0.75 0.85 0.93 0.95 1.00 0.87 0.74 0.27 0.39 0.45 0.51 0.52 0.51 0.47 0.42 0.33
-0.45 -0.03 -0.02 -0.03 -0.42 -0.09 -0.02 -0.23 0.09 0.14 0.07 -0.24 -0.53 -0.03 -0.04 -0.26 -0.19 0.65 0.62 0.64 0.74 0.83 0.86 0.87 1.00 0.72 0.23 0.30 0.35 0.41 0.45 0.45 0.42 0.39 0.32 0.01-0.37 0.01 -0.02 -0.01 -0.28 -0.03 -0.10 -0.20 0.17 0.08 -0.19 -0.53 -0.02 -0.02 -0.20 -0.14 0.57 0.51 0.52 0.60 0.68 0.72 0.74 0.72 1.00 0.17 0.20 0.24 0.29 0.33 0.33 0.32 0.30 0.27 0.01
-0.21 0.03 -0.15 -0.36 -0.30 0.15 0.03 -0.09 0.17 0.04 0.06 0.10 -0.07 -0.55 -0.77 -0.13 -0.40 0.42 0.30 0.24 0.25 0.28 0.28 0.27 0.23 0.17 1.00 0.88 0.76 0.73 0.72 0.71 0.70 0.69 0.67 0.15-0.34 -0.12 -0.18 -0.38 -0.46 -0.29 0.01 -0.18 0.16 0.03 0.06 0.18 -0.10 -0.46 -0.53 -0.24 -0.54 0.52 0.58 0.56 0.54 0.49 0.44 0.39 0.30 0.20 0.88 1.00 0.96 0.91 0.83 0.78 0.73 0.67 0.61 0.11
-0.40 -0.16 -0.12 -0.31 -0.54 -0.44 -0.21 0.15 0.02 0.03 0.19 -0.11 -0.46 -0.39 -0.26 -0.60 0.49 0.63 0.64 0.64 0.58 0.52 0.45 0.35 0.24 0.76 0.96 1.00 0.96 0.88 0.82 0.77 0.69 0.60 0.08-0.42 -0.13 -0.03 -0.23 -0.59 -0.34 0.01 -0.21 0.13 0.03 -0.02 0.17 -0.12 -0.57 -0.35 -0.22 -0.65 0.43 0.54 0.58 0.61 0.60 0.57 0.51 0.41 0.29 0.73 0.91 0.96 1.00 0.96 0.93 0.88 0.81 0.69 0.06
-0.41 -0.08 0.04 -0.17 -0.60 -0.15 0.02 -0.18 0.12 0.03 -0.05 0.13 -0.13 -0.67 -0.35 -0.17 -0.66 0.37 0.42 0.46 0.53 0.57 0.57 0.52 0.45 0.33 0.72 0.83 0.88 0.96 1.00 0.98 0.95 0.89 0.77 0.05-0.40 -0.05 0.07 -0.15 -0.57 -0.06 0.02 -0.17 0.11 0.03 -0.07 0.11 -0.13 -0.70 -0.35 -0.14 -0.64 0.33 0.35 0.38 0.47 0.54 0.54 0.51 0.45 0.33 0.71 0.78 0.82 0.93 0.98 1.00 0.97 0.91 0.79 0.05
-0.36 0.07 -0.12 -0.49 0.03 0.03 -0.18 0.09 0.04 -0.08 0.08 -0.12 -0.74 -0.37 -0.10 -0.62 0.29 0.27 0.30 0.38 0.47 0.49 0.47 0.42 0.32 0.70 0.73 0.77 0.88 0.95 0.97 1.00 0.92 0.81 0.06-0.32 0.05 0.08 -0.11 -0.39 0.11 0.01 -0.18 0.09 0.05 -0.08 0.05 -0.10 -0.76 -0.40 -0.07 -0.57 0.23 0.19 0.21 0.29 0.39 0.42 0.42 0.39 0.30 0.69 0.67 0.69 0.81 0.89 0.91 0.92 1.00 0.81 0.06
-0.27 0.09 0.09 -0.11 -0.25 0.17 -0.06 -0.17 0.08 0.08 -0.04 0.03 -0.07 -0.70 -0.46 -0.04 -0.47 0.18 0.11 0.12 0.19 0.29 0.32 0.33 0.32 0.27 0.67 0.61 0.60 0.69 0.77 0.79 0.81 0.81 1.00 0.080.01 0.02 0.01 -0.01 0.03 -0.02 0.05 -0.01 -0.05 -0.25 0.01 -0.02 -0.02 -0.02 -0.02 -0.01 0.01 0.01 0.15 0.11 0.08 0.06 0.05 0.05 0.06 0.06 0.08 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
FIG. 139: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
1. Electron2134
187
DFN[1]
mu_other_bkg_electron
HybridModel
mu_signal_electron_Xclnumu_sideband_electron_Xclnu
gammaSFEI_B0leptonID[0]Slow_Pi0[0]
MCStatsignal_electron[8]
0.05
0.00
0.05
FEI_Bpf+-/00
MCStatsignal_electron[7]MCStatsignal_electron[6]
bf_B0topilnubf_BptoXulnu
MCStatsignal_electron[5]
bf_charm_decaysbf_B0toXulnu
mu_sideband_muon_Xclnu
0.05
0.00
0.05
leptonID[1]ff_Pion[3]
mu_signal_muon_Xclnu
bf_Bptorholnubf_B0torholnubf_BptoDetalnuff_DststBroad[0]
MCStatsignal_electron[0]
bf_BptopilnuTracking
0.05
0.00
0.05
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 140: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
188
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.014±0.014G = 0.996±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.009±0.014G = 0.999±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.021±0.014G = 1.006±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 1.003±0.004) in (0.009±0.004)
```
FIG. 141: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom left: Xcℓν factor
```
```
pulls (bin 6); bottom right: linearity test
```
189
2. Muon2135
DFN[1]gammaS
mu_sideband_muon_Xclnumu_signal_muon_Xclnu
mu_other_bkg_muon
HybridModel
FEI_B0
MCStatsignal_muon[8]
FEI_Bp
bf_BptoDstetalnu
0.050
0.025
0.000
0.025
0.050
bf_BptoXulnu
MCStatsignal_muon[6]
bf_B0toXulnu
f+-/00
MCStatsignal_muon[7]bf_B0toDstetalnuMCStatsignal_muon[5]MCStatsignal_muon[0]
bf_B0topilnubf_B0toDetalnu
0.050
0.025
0.000
0.025
0.050
bf_B0torholnuff_Pion[3]bf_BptorholnuleptonID[0]bf_BptopilnuleptonID[1]ff_DststBroad[0]Slow_Pi0[1]bf_BptoDetalnu
MCStatsignal_muon[4]
0.050
0.025
0.000
0.025
0.050
2
1
0
1
2
```
(
```
```
) /
```
= + = = + = pulls
2
1
0
1
2
```
(
```
```
) /
```
2
1
0
1
2
```
(
```
```
) /
```
FIG. 142: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
GeV
190
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.032±0.014G = 1.017±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
250
Trials
```
G = 0.003±0.014G = 1.012±0.010
```
```
4 2 0 2 4(
```
```
in)/
```
0
50
100
150
200
Trials
```
G = -0.047±0.014G = 1.000±0.010
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8in
0.6
0.8
1.0
1.2
1.4
```
( 1.0013±0.0027) in (0.0001±0.0025)
```
FIG. 143: Variable: q2, Phase-space region: pBℓ > 1.0 GeV, Experimental cut: pBℓ > 1.0
```
GeV. Top left: signal pulls; top right: Xcℓν factor pulls (bin 1); bottom left: Xcℓν factor
```
```
pulls (bin 6); bottom right: linearity test
```
191
L. CONTINUUM REWEIGHTING VARIABLES2136
The variables used for continuum reweighting before and after reweighting are shown here.2137
A few variables not used for the training are also shown to illustrate the correction.2138
1. Before applying corrections2139
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
1
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
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
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
3
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
4
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
192
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
5
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
6
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
7
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
8
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
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
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
193
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos B O
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.02)
```
×103
ddss
uucc
MC Uncert.Data
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos Bz
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
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
Events / (0.02)
```
×102
ddss
uucc
MC Uncert.Data
0.00 1.25 2.50 3.75 5.00 6.25 7.50 8.75 10.00
Et, CS [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.2 GeV)
```
×102
ddss
uucc
MC Uncert.Data
10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0
m2miss, CS [GeV2]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.4 GeV
```
```
2)
```
×103
ddss
uucc
MC Uncert.Data
194
0.000 0.075 0.150 0.225 0.300 0.375 0.450oo
0
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.01)
```
×103
ddss
uucc
MC Uncert.Data
5.00 3.75 2.50 1.25 0.00 1.25 2.50 3.75 5.00oo
1 ×10 2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.002)
```
×102
ddss
uucc
MC Uncert.Data
0.09 0.06 0.03 0.00 0.03 0.06 0.09 0.12 0.15oo
2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.005)
```
×102
ddss
uucc
MC Uncert.Data
4 3 2 1 0 1 2 3 4oo
3 ×10 2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.0016)
```
×103
ddss
uucc
MC Uncert.Data
195
0.04 0.02 0.00 0.02 0.04 0.06 0.08 0.10oo
4
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.003)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8so
00
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.06)
```
×102
ddss
uucc
MC Uncert.Data
0.6 0.4 0.2 0.0 0.2 0.4 0.6so
01
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.028)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2so
02
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.03)
```
×102
ddss
uucc
MC Uncert.Data
196
0.500 0.375 0.250 0.125 0.000 0.125 0.250 0.375 0.500so
03
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.02)
```
×102
ddss
uucc
MC Uncert.Data
0.6 0.4 0.2 0.0 0.2 0.4 0.6so
04
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.028)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00so
10
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.04)
```
×102
ddss
uucc
MC Uncert.Data
0.30 0.15 0.00 0.15 0.30 0.45 0.60 0.75so
12
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.024)
```
×102
ddss
uucc
MC Uncert.Data
197
0.300 0.225 0.150 0.075 0.000 0.075 0.150 0.225 0.300so
14
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.012)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4so
20
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.03)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7so
22
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.018)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.1 0.0 0.1 0.2 0.3 0.4 0.5so
24
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.014)
```
×103
ddss
uucc
MC Uncert.Data
198
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
R2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.016)
```
×102
ddss
uucc
MC Uncert.Data
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| B|
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.01)
```
×102
ddss
uucc
MC Uncert.Data
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| O|
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.01)
```
×102
ddss
uucc
MC Uncert.Data
199
0 3 6 9 12 15 18 21 24
NCS
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
Events
×102
ddss
uucc
MC Uncert.Data
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
NCStr
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×103
ddss
uucc
MC Uncert.Data
200
2.8 2.4 2.0 1.6 1.2 0.8 0.4 0.0
log10 FEI
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.06)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8
pB [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.06 GeV)
```
×103
ddss
uucc
MC Uncert.Data
0 4 8 12 16 20 24 28
q2 [GeV2]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.6 GeV
```
```
2)
```
×103
ddss
uucc
MC Uncert.Data
0 1 2 3 4 5 6 7
MX [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.14 GeV)
```
×102
ddss
uucc
MC Uncert.Data
201
2. After applying corrections2140
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
1
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
3
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
4
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.12)
```
×102
ddss
uucc
MC Uncert.Data
202
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
5
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
6
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
7
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
0.00 0.75 1.50 2.25 3.00 3.75 4.50 5.25 6.00
8
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
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
Events / (0.12)
```
×103
ddss
uucc
MC Uncert.Data
203
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos B O
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.02)
```
×103
ddss
uucc
MC Uncert.Data
0.000 0.125 0.250 0.375 0.500 0.625 0.750 0.875 1.000
cos Bz
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
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
Events / (0.02)
```
×102
ddss
uucc
MC Uncert.Data
0.00 1.25 2.50 3.75 5.00 6.25 7.50 8.75 10.00
Et, CS [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.2 GeV)
```
×102
ddss
uucc
MC Uncert.Data
10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0
m2miss, CS [GeV2]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.4 GeV
```
```
2)
```
×103
ddss
uucc
MC Uncert.Data
204
0.000 0.075 0.150 0.225 0.300 0.375 0.450oo
0
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.01)
```
×103
ddss
uucc
MC Uncert.Data
5.00 3.75 2.50 1.25 0.00 1.25 2.50 3.75 5.00oo
1 ×10 2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.002)
```
×102
ddss
uucc
MC Uncert.Data
0.09 0.06 0.03 0.00 0.03 0.06 0.09 0.12 0.15oo
2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.005)
```
×102
ddss
uucc
MC Uncert.Data
4 3 2 1 0 1 2 3 4oo
3 ×10 2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.0016)
```
×103
ddss
uucc
MC Uncert.Data
205
0.04 0.02 0.00 0.02 0.04 0.06 0.08 0.10oo
4
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.003)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8so
00
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.06)
```
×102
ddss
uucc
MC Uncert.Data
0.6 0.4 0.2 0.0 0.2 0.4 0.6so
01
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.028)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2so
02
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.03)
```
×102
ddss
uucc
MC Uncert.Data
206
0.500 0.375 0.250 0.125 0.000 0.125 0.250 0.375 0.500so
03
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.02)
```
×102
ddss
uucc
MC Uncert.Data
0.6 0.4 0.2 0.0 0.2 0.4 0.6so
04
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
```
Events / (0.028)
```
×102
ddss
uucc
MC Uncert.Data
0.00 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00so
10
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.04)
```
×102
ddss
uucc
MC Uncert.Data
0.30 0.15 0.00 0.15 0.30 0.45 0.60 0.75so
12
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.024)
```
×102
ddss
uucc
MC Uncert.Data
207
0.300 0.225 0.150 0.075 0.000 0.075 0.150 0.225 0.300so
14
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
```
Events / (0.012)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4so
20
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.03)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7so
22
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
```
Events / (0.018)
```
×102
ddss
uucc
MC Uncert.Data
0.2 0.1 0.0 0.1 0.2 0.3 0.4 0.5so
24
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.014)
```
×103
ddss
uucc
MC Uncert.Data
208
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
R2
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.016)
```
×102
ddss
uucc
MC Uncert.Data
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| B|
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
```
Events / (0.01)
```
×102
ddss
uucc
MC Uncert.Data
0.525 0.600 0.675 0.750 0.825 0.900 0.975
| O|
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
```
Events / (0.01)
```
×102
ddss
uucc
MC Uncert.Data
209
0 3 6 9 12 15 18 21 24
NCS
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
2.00
4.00
6.00
8.00
Events
×102
ddss
uucc
MC Uncert.Data
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
NCStr
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×103
ddss
uucc
MC Uncert.Data
210
2.8 2.4 2.0 1.6 1.2 0.8 0.4 0.0
log10 FEI
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
```
Events / (0.06)
```
×102
ddss
uucc
MC Uncert.Data
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8
pB [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
```
Events / (0.06 GeV)
```
×103
ddss
uucc
MC Uncert.Data
0 4 8 12 16 20 24 28
q2 [GeV2]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.6 GeV
```
```
2)
```
×103
ddss
uucc
MC Uncert.Data
0 1 2 3 4 5 6 7
MX [GeV]
0.50
1.00
1.50
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 43 fb
1
0.00
1.00
2.00
3.00
4.00
```
Events / (0.14 GeV)
```
×102
ddss
uucc
MC Uncert.Data
211
M. TRACK AND CLUSTER MULTIPLICITIES2141
We show in this Appendix the track and cluster multiplicities for Xu and Xc events in the2142
B → Xℓν region and the signal region.2143
0 1 2 3 4 5 6# tracks0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
```
Region: B X
```
XcX
u
0 1 2 3 4 5 6# neutral clusters0.00
0.05
0.10
0.15
0.20
0.25
```
Region: B X
```
XcX
u
0 1 2 3 4 5 6N
tracks
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
1.60
Events
×105Continuum
FakeSecondary
XcXu
Xu ×10MC Uncert.
Data
pB > 1 GeV, B X
0 1 2 3 4 5 6N
neu. clusters.
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
Events
×104Continuum
FakeSecondary
XcXu
Xu ×10MC Uncert.
Data
pB > 1 GeV, B X
```
FIG. 144: The track (left) and neutral cluster (right) multiplicities in the B → Xℓν region.
```
The top plot only compares the normalised MC B → Xcℓν and B → Xuℓν components.
212
0 1 2 3 4 5 6# tracks0.0
0.1
0.2
0.3
0.4
0.5
```
Region: SR
```
XcX
u
0 1 2 3 4 5 6# neutral clusters0.00
0.05
0.10
0.15
0.20
0.25
```
Region: SR
```
XcX
u
0 1 2 3 4 5 6N
tracks
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
7.00
8.00
Events
×103Continuum
FakeSecondary
XcXu
Xu ×10MC Uncert.
Asimov Data
pB > 1 GeV, Signal region
0 1 2 3 4 5 6N
neu. clusters.
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
Events
×103Continuum
FakeSecondary
XcXu
Xu ×10MC Uncert.
Asimov Data
pB > 1 GeV, Signal region
```
FIG. 145: The track (left) and neutral cluster (right) multiplicities in the signal region.
```
The top plot only compares the normalised MC B → Xcℓν and B → Xuℓν components.
213
N. LOW FEI CUT STUDIES2144
We document in this Section a few tests performed on a sample with an FEI cut PFEI > 0.0012145
instead of PFEI > 0.01 as it is set in out nominal sample. We show in Figures 146 and 1472146
the data-MC agreement for the three main kinematical variables for the B → Xℓν and2147
CR0,low regions respectively. We show in Figure 148 the residuals for q2 for different FEI2148
cuts. Finally, we performed a fit using the low FEI cut sample by repeating exactly the same2149
procedure as described in Section 8 for the nominal fit. The pre- and post-fit q2 distributions2150
are shown in Figure 149. From the Asimov fit, the obtained uncertainty is comparable to2151
the one obtained in our nominal fit.2152
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B X
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B X
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.50
1.00
1.50
2.00
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, B X
FIG. 146: Kinematic variables in B → Xℓν region
214
0.0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7
pB [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
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
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, CR0, low
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
```
Events / (0.25 GeV
```
```
2)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, CR0, low
0.00 0.75 1.50 2.25 3.00 3.75 4.50M
X [GeV]
0.75
1.00
1.25
Data/MC
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 364 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
```
Events / (0.05 GeV)
```
×104Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×10
MC Stat. Uncert.Data
pB > 1 GeV, CR0, low
FIG. 147: Kinematic variables in B → Xℓν region
215
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0
q2 Residual
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Arbitrary Normalisation
3 < log < : RMS = 2.2310
2 < log < : RMS = 2.0661
1 < log : RMS = 2.0582
FIG. 148: q2 residuals for different FEI score windows
216
0
500
1000
1500
2000
events
signal
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.5
0.75
1.0
1.25
data / model
0
500
1000
1500
2000
events
signal
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.5
0.75
1.0
1.25
data / model
0
20000
40000
60000
80000
100000
events
sideband
pre-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.5
0.75
1.0
1.25
data / model
0
20000
40000
60000
80000
100000
events
sideband
post-fit
other_bkg
Xclnu
Xulnu_in
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.5
0.75
1.0
1.25
data / model
```
FIG. 149: Signal region (top) and control region (bottom) pre- (left) and post-fit (right) q2
```
distributions
217
O. STRANGE QUARK FRAGMENTATION2153
1. γs2154
```
We use the two most recent measurements of γs from JADE [11] (0.27±0.06) and TASSO [12]2155
```
```
(0.35 ± 0.05). To cover the full range of values covered by these two measurements we2156
```
```
choose a 1σ range of 0.30 ± 0.09 (the value of 0.30 is also used at LHCb though at much2157
```
```
higher energies). After discussing directly with the Pythia authors we summarise here2158
```
the conclusions. The default Pythia value of 0.217 comes from the Monash tune which is2159
```
dominated by LEP data (the γs parameter is called StringFlav:probStoUD in Pythia 8.3).2160
```
```
In Figure 150 (left) it can be seen that this value yields a good agreement for the average2161
```
kaon multiplicity for high energies. However, at low energies the data undershoots the2162
Pythia prediction. The same distribution with a value of γs = 0.35 is shown in Figure 1502163
```
(right). The plot suggests that a more correct value should rather be somewhere in the2164
```
range 0.25 - 0.30 for low energies. However, the key issue is that there are no recent reliable2165
measurements for γs for low energies. In our case, the hadronisation processes occur below2166
5 GeV, mostly in the range 1-3 GeV. Therefore, based on all the available information the2167
most reasonable choice is to use a rather broad range between 0.21 - 0.39 which covers all2168
the different values quoted here.2169
14 22 29 35 44 58 91 91 91 91 133 161 183 189 200 250 350 500 1000
>Ch
<n
0
20
40
60
Average Charged Multiplicity vs ECM
Pythia 8.185Data from HEPDATA
HEPDATA
```
PY8 (Monash)
```
```
PY8 (Default)
```
```
PY8 (Fischer)
```
bins/N25%χ0.0±0.3
0.0±0.2
0.0±0.2
V I N C I A R O O T
hadrons→ee
```
(not to scale)cmE
```
14 22 29 35 44 58 91 91 91 91 133 161 183 189 200 250 350 500 1000
Theory/Data
0.6
0.8
1
1.2
1.4
>K
<n
0
2
4
6
Multiplicity vs ECM+/-Average K
Pythia 8.185Data from HEPDATA
```
HEPDATAPY8 (Monash)
```
```
PY8 (Default)PY8 (Fischer)
```
bins/N25%χ0.0±0.6
0.0±2.00.0±1.8
V I N C I A R O O T
hadrons→ee
```
(not to scale)cmE
```
14 22 35 44 91 91 133 161 183 189 250 350 500 1000
Theory/Data0.60.8
1
1.2
1.4
>Λ
<n
0
0.2
0.4
0.6
0.8
1
1.2Multiplicity vs ECM0ΛAverage
Pythia 8.185Data from HEPDATA
```
HEPDATAPY8 (Monash)
```
```
PY8 (Default)PY8 (Fischer)
```
bins/N25%χ0.0±0.6
0.1±2.20.1±1.8
V I N C I A R O O T
hadrons→ee
```
(not to scale)cmE
```
14 35 91 91 91 91 133 200 250 350 500 1000
Theory/Data0.60.8
1
1.2
1.4
Figure 25: e+e− → hadrons. Energy scaling of 〈nCh〉, 〈nK± 〉, and 〈nΛ〉, in e+e− → q ¯q events,
including comparisons to measurements from HEPDATA for CM energies from 14 GeV to 200 GeV.
Also shown are model extrapolations up to 1000 GeV.
35
0
2
4
6
8>K
<n Multiplicity vs ECM
+/-Average K
LiveDisplays
DELPHI
SLD
TASSO
Pythia-8.311-Ps0.35
Vincia 2.202
Pythia 8.230
qq→Z
14 22 35 44 91 91 133 161 183 189
```
(not to scale)cmE
```
0.6
0.8
1
1.2
1.4
Theory/Data
FIG. 150: Kaon multiplicity at different energies for different measurements and Pythia
```
tunes. On the left plot the Pythia 8.3 parameter StringFlav:probStoUD (γs) is set to
```
0.217 and on the right it is set to 0.35.
2. Fraction of kaons before/after hybridisation2170
Kaons in B → Xuℓν decays are only produced in non-resonant events which are scaled down2171
by the hybrid procedure and replaced by resonant events. Therefore, the number of kaon2172
events is reduced by the hybrid procedure which can impact the reconstruction efficiency of2173
B → Xuℓν events since kaons are rejected in the signal regions used in our fits. The impact2174
218
of such an effect will be limited by the hadronic mass necessary to produce a pair of kaons2175
```
(∼ 1 GeV whereas the threshold to produce the lowest non-resonant hadronic system is2176
```
```
twice the pion mass so ∼ 0.3 GeV). Kaon events represent about 5%-15% of all B → Xuℓν2177
```
events in all fit regions.2178
2179
After applying the hybrid procedure, the number of kaon events among all inclusive2180
B → Xuℓν events is reduced by 10%, 20% and 30% in fit regions 1, 3 and 5, respec-2181
tively. As described in the previous section, we vary the value of γs, and therefore the2182
number of kaon events, by 30% which covers the shifts caused by the hybrid method.2183
2184
Besides, the kaon event shift could also be different for charged and neutral B decays2185
because of the kaon charges. Before applying the hybrid method to the inclusive sample2186
of B → Xuℓν events, there’s about 1-2% more kaon events in B+ decays than in B0 de-2187
cays depending on the region. Afterwards, this difference shifts to 2-8% and so the hybrid2188
weights introduce a difference of about 2-5%. This effect is larger in the broader regions of2189
phase-space. The unbalance introduced by this effect is of the same order as the uncertainty2190
assigned on f ±/00. It is also worth noting that some of the B → Xuℓν modelling uncertain-2191
ties are quite conservative, the pion multiplicity in regions 3 and 5 in particular. Therefore,2192
any effect caused by the shift in the number of kaons due to the hybrid procedure is already2193
well covered by the assigned uncertainties.2194
219
P. VARIABLE DEPENDENT EFFICIENCY2195
We show here the MC signal efficiency as a function of pBℓ , MX and q2 at the generator level.2196
The efficiency is defined as the fraction of MC generated signal events that are selected by2197
```
the signal region fit 1 cuts (see the main text for a detail description of all these selections).2198
```
The selection pBℓ > 1.0 GeV is already applied. The efficiency is shown in percentage.2199
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75pB [GeV]
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
%
Xu efficiency
Total efficiency
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5MX [GeV]
0.0
0.2
0.4
0.6
0.8
1.0
%
Xu efficiency
Total efficiency
0 5 10 15 20 25q2 [GeV2]
0.2
0.4
0.6
0.8
1.0
%
Xu efficiency
Total efficiency
FIG. 151: Total generator level signal efficiency
220
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75pB [GeV]
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
%
Xu efficiency
Total efficiencyResonance efficiency
Non-resonance efficiencyResonant
Non-resonant
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5MX [GeV]
0.0
0.2
0.4
0.6
0.8
%
Xu efficiency
Total efficiencyResonance efficiency
Non-resonance efficiencyResonant
Non-resonant
0 5 10 15 20 25q2 [GeV2]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
%
Xu efficiency
Total efficiencyResonance efficiency
Non-resonance efficiencyResonant
Non-resonant
FIG. 152: Total generator level resonant and non-resonant signal efficiency
221
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75pB [GeV]
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
%
Xu efficiency
+0
+
0
′
X +u
X0u
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5MX [GeV]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
%
Xu efficiency
+0
+
0
′
X +u
X0u
0 5 10 15 20 25q2 [GeV2]
0.0
0.5
1.0
1.5
2.0
%
Xu efficiency
+0
+
0
′
X +u
X0u
FIG. 153: Total generator level signal efficiency broken down in different resonant and
non-resonant modes
222
Q. VR2 FITS2200
1. Fit 32201
0
1000
2000
3000
4000
5000
6000
events
VR2
pre-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
1000
2000
3000
4000
5000
6000
events
VR2
post-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
10000
20000
30000
40000
50000
60000
events
CR0, low
pre-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
0
10000
20000
30000
40000
50000
60000
events
CR0, low
post-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.68
0.84
1.0
1.16
1.32
data / model
FIG. 154: Pre and postfit EBℓ :q2 distributions of the CR0,low - VR2 fit 3.
223
FEI_B0FEI_BpKshortVetoSlow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Tracking
bf_B0toDetalnubf_B0toDlnubf_B0toDonelnubf_B0toDoneprimelnubf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnu
2
0
2
```
(
```
```
) /
```
bf_BptoDstzerolnubf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]kaonIDVetoleptonID[0]leptonID[1]leptonID[2]leptonID[3]
DFN[1]DFN[2]HybridModelbf_B0toXulnubf_B0topilnu
bf_B0torholnu
2
0
2
```
(
```
```
) /
```
bf_BptoXulnubf_Bptoetalnu
bf_Bptoetaprimelnubf_Bptoomegalnu
bf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]ff_Rho[4]
2
0
2
```
(
```
```
) /
```
ff_Rho[5]ff_Rho[6]ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaSCont.Norm.[0]Cont.Norm.[1]
Cont.Reweight[0]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]Cont.Reweight[4]Cont.Reweight[5]mu_sideband_Xclnumu_signal_XclnuMCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsideband[10]MCStatsideband[11]MCStatsignal[0]MCStatsignal[1]
2
0
2
```
(
```
```
) /
```
MCStatsignal[2]MCStatsignal[3]MCStatsignal[4]MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]MCStatsignal[10]MCStatsignal[11]
2
0
2
```
(
```
```
) /
```
FIG. 155: CR0,low - VR2 fit 3 nuisance parameter pulls
224
0 2 4 6 8 10 12
```
EB : q2 [GeV:GeV2]
```
0.8
0.9
1.0
1.1
Xc Data/MC ratio
CR0, low
VR2
Fit factors
```
FIG. 156: Comparison of the normalised prefit (fit 3) Xcℓν data/MC ratios in CR0,low and
```
VR2 with statistical uncertainties and Xcℓν shape factors with full fit uncertainties.
225
0
500
1000
1500
2000
2500
3000
3500
events
VR2
pre-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
2500
3000
3500
events
VR2
post-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
2500
3000
events
VR2
pre-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
2500
3000
events
VR2
post-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
VR2
pre-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0M
X [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
10000
12000
14000
events
VR2
post-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[11]
Xclnu[10]
Xclnu[0]
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0M
X [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
FIG. 157: Projections of the EBℓ :q2 fit 3 on EBℓ , q2 and MX .
226
2. Fit 52202
0
500
1000
1500
2000
events
VR2
pre-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
events
VR2
post-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
2500
5000
7500
10000
12500
15000
17500
20000
events
CR0, low
pre-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
2500
5000
7500
10000
12500
15000
17500
20000
events
CR0, low
post-fit
Other bkg.
Xc
Xu -out
Xu
Uncertainty
Data
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
FIG. 158: Pre and postfit EBℓ distributions of the CR0,low - VR2 fit 5.
227
FEI_B0FEI_BpKshortVetoSlow_Pi0[0]Slow_Pi0[1]Slow_Pi0[2]Slow_Pip[0]Slow_Pip[1]Slow_Pip[2]Tracking
bf_B0toDetalnubf_B0toDlnubf_B0toDonelnubf_B0toDoneprimelnubf_B0toDpipilnubf_B0toDstetalnubf_B0toDstlnubf_B0toDstpipilnubf_B0toDsttwolnubf_B0toDstzerolnubf_BptoDetalnubf_BptoDlnubf_BptoDonelnubf_BptoDpipilnubf_BptoDsKlnubf_BptoDsstKlnubf_BptoDstetalnubf_BptoDstlnubf_BptoDstpipilnubf_BptoDsttwolnu
2
0
2
```
(
```
```
) /
```
bf_BptoDstzerolnubf_charm_decays
f+-/00
ff_DandDst[0]ff_DandDst[1]ff_DandDst[2]ff_DandDst[3]ff_DandDst[4]ff_DandDst[5]ff_DandDst[6]ff_DandDst[7]ff_DandDst[8]ff_DststBroad[0]ff_DststBroad[1]ff_DststBroad[2]ff_DststNarrow[0]ff_DststNarrow[1]ff_DststNarrow[2]ff_DststNarrow[3]kaonIDVeto[0]kaonIDVeto[1]leptonID[0]leptonID[1]leptonID[2]
DFN[1]DFN[2]HybridModelbf_B0toXulnubf_B0topilnu
bf_B0torholnu
2
0
2
```
(
```
```
) /
```
bf_BptoXulnubf_Bptoetalnu
bf_Bptoetaprimelnubf_Bptoomegalnu
bf_Bptopilnubf_Bptorholnuff_Eta[1]ff_Etaprime[1]ff_Omega[0]ff_Omega[10]ff_Omega[1]ff_Omega[2]ff_Omega[3]ff_Omega[4]ff_Omega[5]ff_Omega[6]ff_Omega[7]ff_Omega[8]ff_Omega[9]ff_Pion[0]ff_Pion[1]ff_Pion[2]ff_Pion[3]ff_Pion[4]ff_Rho[0]ff_Rho[10]ff_Rho[1]ff_Rho[2]ff_Rho[3]ff_Rho[4]
2
0
2
```
(
```
```
) /
```
ff_Rho[5]ff_Rho[6]ff_Rho[7]ff_Rho[8]ff_Rho[9]gammaSCont.Norm.[0]Cont.Norm.[1]
Cont.Reweight[0]Cont.Reweight[10]Cont.Reweight[11]Cont.Reweight[12]Cont.Reweight[13]Cont.Reweight[14]Cont.Reweight[1]Cont.Reweight[2]Cont.Reweight[3]Cont.Reweight[4]Cont.Reweight[5]Cont.Reweight[6]Cont.Reweight[7]Cont.Reweight[8]Cont.Reweight[9]mu_sideband_Xclnumu_signal_XclnuMCStatsideband[0]MCStatsideband[1]MCStatsideband[2]MCStatsideband[3]MCStatsideband[4]
2
0
2
```
(
```
```
) /
```
MCStatsideband[5]MCStatsideband[6]MCStatsideband[7]MCStatsideband[8]MCStatsideband[9]MCStatsignal[0]MCStatsignal[1]MCStatsignal[2]MCStatsignal[3]MCStatsignal[4]MCStatsignal[5]MCStatsignal[6]MCStatsignal[7]MCStatsignal[8]MCStatsignal[9]
2
0
2
```
(
```
```
) /
```
FIG. 159: CR0,low - VR2 fit 5 nuisance parameter pulls
228
1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75
EB [GeV]
0.8
0.9
1.0
1.1
1.2
Xc Data/MC ratio
CR0, low
VR2
Fit factors
```
FIG. 160: Comparison of the normalised prefit (fit 5) Xcℓν data/MC ratios in CR0,low and
```
VR2 with statistical uncertainties and Xcℓν shape factors with full fit uncertainties.
229
0
500
1000
1500
2000
2500
3000
3500
events
VR2
pre-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[0]
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.68
0.84
1.0
1.16
1.32
data / model
0
500
1000
1500
2000
2500
3000
3500
events
VR2
post-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[0]
Uncertainty
Data
0 5 10 15 20 25
q2 [GeV2]
0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
events
VR2
pre-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[0]
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0M
X [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
0
2000
4000
6000
8000
events
VR2
post-fit
other_bkg
Xulnu_out
Xulnu_in
Xclnu[9]
Xclnu[8]
Xclnu[7]
Xclnu[6]
Xclnu[5]
Xclnu[4]
Xclnu[3]
Xclnu[2]
Xclnu[1]
Xclnu[0]
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0M
X [GeV]
0.68
0.84
1.0
1.16
1.32
data / model
FIG. 161: Projections of the EBℓ fit 5 on q2 and MX .
230
R. SIGNAL REGION DISTRIBUTIONS2203
1. Splits in lepton flavour2204
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 28.8/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
4.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
0 3 6 9 12 15 18 21 24q2 [GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 32.9/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
2.50
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0EB : q2 [GeV:GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 30.1/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2MX [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 36.8/11
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
2.00
4.00
6.00
8.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0M2
miss [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 23.6/8
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
5.2700 5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900mbc [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 75.1/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, e±
FIG. 162: Signal region distributions for Xueν.
231
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6EB [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 68.2/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
0 3 6 9 12 15 18 21 24q2 [GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 68.7/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0EB : q2 [GeV:GeV2]0.75
1.00
1.25
Data/MC
2/d. o. f = 61.8/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2MX [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 68.9/11
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.20
0.40
0.60
0.80
1.00
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0M2
miss [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 62.9/8
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
5.2700 5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900mbc [GeV]0.75
1.00
1.25
Data/MC
2/d. o. f = 117.3/19
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Simulation dt = 365 fb 1
0.00
1.00
2.00
3.00
4.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuMC Stat. Uncert.
Data
EB > 1 GeV, SR, ±
FIG. 163: Signal region distributions Xuµν.
232
2. Fit 3 region: EBℓ > 1.0 GeV, MX < 1.7 GeV2205
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 10.1/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
2.00
4.00
6.00
8.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 8.4/10
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0
```
EB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
2/d. o. f = 16.0/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8M
X [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 3.0/2
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
FIG. 164: Signal region distributions for fit 3.
233
3. Fit 5 region: EBℓ > 1.0 GeV, MX < 1.7 GeV2206
1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6
EB [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 5.4/12
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
1.00
2.00
3.00
4.00
5.00
6.00
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
0 3 6 9 12 15 18 21 24
q2 [GeV2]
0.75
1.00
1.25
Data/MC
2/d. o. f = 2.1/6
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.50
1.00
1.50
2.00
2.50
3.00
3.50
Events
×102Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0
```
EB : q2 [GeV:GeV2]
```
0.75
1.00
1.25
Data/MC
2/d. o. f = 1.4/4
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8M
X [GeV]
0.75
1.00
1.25
Data/MC
2/d. o. f = 0.8/2
0.0 0.2 0.4 0.6 0.8 1.00.0
0.2
0.4
0.6
0.8
1.0 Belle II Internal dt = 365 fb
1
0.00
0.20
0.40
0.60
0.80
1.00
1.20
1.40
Events
×103Continuum
FakeSecondary
D* *GapD* *
D*D
XuXu ×0
MC Uncert.Data
EB > 1 GeV
FIG. 165: Signal region distributions for fit 5.
234
S. ADDITIONAL FIT CORRECTIONS2207
1. Fit 32208
0.85 0.90 0.95 1.00 1.05 1.10 1.15 1.20 1.25
Injected signal normalisation
0.85
0.90
0.95
1.00
1.05
1.10
1.15
Measured normalisation
```
( 0.988±0.008) in+(0.025±0.008)
```
FIG. 166: Distribution of output vs input normalisations of the signal injected CRK,low –
CRK,high fit setup described in the text.
0.925 0.950 0.975 1.000 1.025 1.050 1.075 1.100
```
( in)/
```
0
10
20
30
40
50
60
Trials
```
G = 1.0120±0.0007
```
```
G = 0.0213±0.0005
```
FIG. 167: Distribution of output normalisations with 1,000 toys created by varying the
data yields in CRK,high within their statistical uncertainties. The normalisation of the
signal injected in data is chosen to be 1.
235
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
1.006
1.008
1.010
1.012
1.014
1.016
```
Measured signal normalisation(-0.032±0.014) in+(1.046±0.015)
```
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
0.992
0.994
0.996
0.998
1.000
1.002
1.004
```
Measured signal normalisation(-0.033±0.014) in+(1.033±0.015)
```
FIG. 168: Distribution of output signal normalisations vs Xcℓν overestimation factor in
the signal injected CRK,low – CRK,high fit setup described in the text. In the right-hand
plot, the first source of bias described above has been corrected for. The normalisation of
the injected signal is equal to 1.
1.00 1.05 1.10 1.15 1.20 1.25 1.30B Xc overestimation factor0.9900
0.9925
0.9950
0.9975
1.0000
1.0025
1.0050
1.0075
1.0100
Output corrected signal normalisation
FIG. 169: Output signal normalisation corrected by the two corrections described in the
text vs different Xcℓν overestimation factors. The uncertainty is the one added for the
second source of bias.
236
2. Fit 52209
0.85 0.90 0.95 1.00 1.05 1.10 1.15 1.20 1.25
Injected signal normalisation
0.85
0.90
0.95
1.00
1.05
1.10
1.15
Measured normalisation
```
( 0.957±0.009) in+(0.050±0.009)
```
FIG. 170: Distribution of output vs input normalisations of the signal injected CRK,low –
CRK,high fit setup described in the text.
0.94 0.96 0.98 1.00 1.02 1.04 1.06 1.08
```
( in)/
```
0
5
10
15
20
25
30
Trials
```
G = 1.0043±0.0007
```
```
G = 0.0164±0.0005
```
FIG. 171: Distribution of output normalisations with 1,000 toys created by varying the
data yields in CRK,high within their statistical uncertainties. The normalisation of the
signal injected in data is chosen to be 1.
237
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
0.990
0.995
1.000
1.005
1.010
1.015
```
Measured signal normalisation(-0.105±0.015) in+(1.115±0.016)
```
1.00 1.05 1.10 1.15 1.20 1.25B Xc overestimation factor
0.980
0.985
0.990
0.995
1.000
1.005
```
Measured signal normalisation(-0.110±0.015) in+(1.113±0.017)
```
FIG. 172: Distribution of output signal normalisations vs Xcℓν overestimation factor in
the signal injected CRK,low – CRK,high fit setup described in the text. In the right-hand
plot, the first source of bias described above has been corrected for. The normalisation of
the injected signal is equal to 1.
1.00 1.05 1.10 1.15 1.20 1.25 1.30B Xc overestimation factor
0.97
0.98
0.99
1.00
1.01
1.02
1.03
Output corrected signal normalisation
FIG. 173: Output signal normalisation corrected by the two corrections described in the
text vs different Xcℓν overestimation factors. The uncertainty is the one added for the
second source of bias.
238
[1] S. Choudhury et al., Belle Collaboration, Measurement of the B+/B0 production ratio in2210
```
e+e− collisions at the Υ(4S) resonance using B → J/ψ(ℓℓ)K decays at Belle, Phys. Rev. D2211
```
```
107 (Feb, 2023) L031102. https://link.aps.org/doi/10.1103/PhysRevD.107.L031102.2212
```
[2] M. Hohmann et al., Inclusive search for the Weak Annihilation contribution to Charmless2213
```
Semileptonic B Decays at Belle II , Belle II Intern. Note (2023) .2214
```
```
https://docs.belle2.org/record/3927/files/BELLE2-NOTE-PH-2023-060.pdf.2215
```
[3] Particle Data Group, Particle Data Group ,2216
```
https://pdg.lbl.gov/2023/reviews/contents_sports.html.2217
```
```
[4] F. De Fazio and M. Neubert, B → Xuℓ¯νℓ Decay Distributions to Order αs, JHEP 06 (1999)2218
```
no. 06, 017, arxiv:hep-ph/9905351. http://arxiv.org/abs/hep-ph/9905351.2219
[5] O. L. Buchm¨uller and H. U. Fl¨acher, Fit to moments of inclusive B → Xcℓν and B → Xsγ2220
decay distributions using heavy quark expansions in the kinetic scheme, Phys. Rev. D 732221
```
(Apr, 2006) 073008. https://link.aps.org/doi/10.1103/PhysRevD.73.073008.2222
```
[6] B. O. Lange, M. Neubert, and G. Paz, Theory of Charmless Inclusive B Decays and the2223
```
Extraction of Vub, Phys. Rev. D 72 (2005) no. 7, 073006, arxiv:hep-ph/0504071.2224
```
```
http://arxiv.org/abs/hep-ph/0504071.2225
```
[7] C. Bourrely, I. Caprini, and L. Lellouch, Model-Independent Description of B → πℓν Decays2226
```
and a Determination of |Vub|, Phys. Rev. D 79 (2009) no. 1, 013008, arxiv:0807.27222227
```
[hep-ph]. https://link.aps.org/doi/10.1103/PhysRevD.79.013008. [Erratum:2228
```
Phys.Rev.D 82, 099902 (2010)].2229
```
```
[8] Y. Aoki, T. Blum, G. Colangelo, et al., Flavour Lattice Averaging Group (FLAG), FLAG2230
```
```
Review 2021 , Eur. Phys. J. C 82 (Oct., 2022) 869, arxiv:2111.09849 [hep-lat].2231
```
```
http://arxiv.org/abs/2111.09849.2232
```
[9] F. U. Bernlochner, M. T. Prim, and D. J. Robinson, B → ρℓ¯ν and ωℓ¯ν in and beyond the2233
```
Standard Model: Improved Predictions and |Vub|, Phys. Rev. D 104 (Aug., 2021) 034032,2234
```
```
arxiv:2104.05739 [hep-ph].2235
```
```
https://link.aps.org/doi/10.1103/PhysRevD.104.034032.2236
```
```
[10] G. Duplancic and B. Melic, Form Factors of B, Bs → η(′) and D, Ds → η(′) Transitions from2237
```
```
QCD Light-Cone Sum Rules, JHEP 11 (Nov., 2015) 138, arxiv:1508.05287 [hep-ph].2238
```
```
http://arxiv.org/abs/1508.05287.2239
```
[11] W. Bartel, L. Becker, C. Bowdery, et al., JADE, Charged Particle and Neutral Kaon2240
```
Production in e+e− Annihilation at PETRA, Z. Phys. C - Particles and Fields 20 (Sept.,2241
```
```
1983) 187–206. https://doi.org/10.1007/BF01574851.2242
```
[12] M. Althoff, W. Braunschweig, F. Kirschfink, et al., TASSO, A Detailed Study of Strange2243
```
Particle Production in e+e− Annihilation at High-energy, Z. Phys. C 27 (1985) no. 1, 27.2244
```
```
https://doi.org/10.1007/BF01642477.2245
```
[13] C. Ramirez, J. F. Donoghue, and G. Burdman, Semileptonic b → u Decay, Phys. Rev. D 412246
```
(1990) no. 5, 1496. https://link.aps.org/doi/10.1103/PhysRevD.41.1496.2247
```
[14] C. Boyd, B. Grinstein, and R. F. Lebed, Constraints on Form-Factors for Exclusive2248
```
Semileptonic Heavy to Light Meson Decays, Phys. Rev. Lett. 74 (1995) no. 23, 4603–4606,2249
```
```
arxiv:hep-ph/9412324. https://link.aps.org/doi/10.1103/PhysRevLett.74.4603.2250
```
[15] F. U. Bernlochner, Z. Ligeti, M. Papucci, M. T. Prim, D. J. Robinson, and C. Xiong,2251
```
Constrained Second-Order Power Corrections in HQET: R(D(∗)), |Vcb|, and New Physics,2252
```
239
```
Phys. Rev. D 106 (Nov., 2022) 096015, arxiv:2206.11281 [hep-ph].2253
```
```
http://arxiv.org/abs/2206.11281.2254
```
[16] F. U. Bernlochner, S. Duell, Z. Ligeti, M. Papucci, and D. J. Robinson, Das Ist Der2255
```
HAMMER: Consistent New Physics Interpretations of Semileptonic Decays, Eur. Phys. J. C2256
```
```
80 (Sept., 2020) 883, arxiv:2002.00020 [hep-ph]. http://arxiv.org/abs/2002.00020.2257
```
[17] F. U. Bernlochner, Z. Ligeti, and D. J. Robinson, Model Independent Analysis of2258
```
Semileptonic B Decays to D∗∗ for Arbitrary New Physics, Phys. Rev. D 97 (Apr., 2018)2259
```
075011, arxiv:1711.03110 [hep-ph]. http://arxiv.org/abs/1711.03110.2260
[18] R. Workman, V. Burkert, V. Crede, et al., Particle Data Group, Review of Particle Physics,2261
```
PTEP 2022 (Aug., 2022) 083C01.2262
```
[19] F. U. Bernlochner, Z. Ligeti, and S. Turczyk, A proposal to solve some puzzles in2263
```
semileptonic B decays, Phys. Rev. D 85 (May, 2012) 094033.2264
```
```
https://link.aps.org/doi/10.1103/PhysRevD.85.094033.2265
```
[20] H. Junkerkalefeld, P. Rocchetti, P. Lewis, M. Milesi, F. Bernlochner, J. Dingfelder, and2266
P. Urquijo, Test of Lepton Universality in Inclusive, Semileptonic and Semitauonic B Meson2267
```
Decays at Belle II , Belle II Intern. Note (July, 2023) .2268
```
```
https://docs.belle2.org/record/3755/.2269
```
[21] S. Jadach, B. Ward, Z. Was, S. Yost, and A. Siodmok, Multi-photon Monte Carlo event2270
generator KKMCee for lepton and quark pair production in lepton colliders, Computer2271
```
Physics Communications 283 (2023) 108556.2272
```
```
https://www.sciencedirect.com/science/article/pii/S0010465522002752.2273
```
[22] F. Bernlochner and M. Welsch, Measurement of Moments of the q2 Spectrum in Inclusive2274
```
B → Xcℓν Decays, Belle II Intern. Note (Jan., 2021) .2275
```
```
https://docs.belle2.org/record/2204.2276
```
[23] L. Cao, W. Sutcliffe, R. Van Tonder, et al., Belle, Measurement of Differential Branching2277
```
Fractions of Inclusive B → Xu ℓ+ νℓ Decays, Phys. Rev. Lett. 127 (Dec., 2021) 261801,2278
```
```
arxiv:2107.13855 [hep-ex]. http://arxiv.org/abs/2107.13855.2279
```
[24] R. van Tonder, L. Cao, W. Sutcliffe, et al., Belle, Measurements of q2 Moments of Inclusive2280
```
B → Xcℓ+νℓ Decays with Hadronic Tagging, Phys. Rev. D 104 (Dec., 2021) 112011,2281
```
```
arxiv:2109.01685 [hep-ex, physics:hep-ph]. http://arxiv.org/abs/2109.01685.2282
```
[25] F. U. Bernlochner, D. Biedermann, H. Lacker, and T. L¨uck, Constraints on Exclusive2283
```
Branching Fractions Bi(B+ → Xicl+ν) from Moment Measurements in Inclusive B → Xclν2284
```
```
Decays, Eur. Phys. J. C 74 (June, 2014) 2914, arxiv:1402.2849 [hep-ph].2285
```
```
http://link.springer.com/10.1140/epjc/s10052-014-2914-3.2286
```
[26] N. Toutounji, K. Varvell, M. Bauer, and P. Goldenzweig, Exclusive B →Xu ν Tagged with2287
```
Hadronic Full-Event-Interpretation in 362 Fb−1 of Belle II Data, Belle II Intern. Note (Feb.,2288
```
```
2023) . https://docs.belle2.org/record/3426.2289
```
[27] D. Dorner, P. Rados, and C. Schwanda, Relative tracking efficiency study of charged, low2290
momentum pions, BELLE2-NOTE-PH-2023-035 .2291
```
https://docs.belle2.org/record/3694/files/BELLE2-NOTE-PH-2023-035.pdf.2292
```
[28] T. Koga, Measurement of momentum dependent π0 reconstruction efficiency with D decays,2293
BELLE2-NOTE-PH-2020-061 .2294
```
https://docs.belle2.org/record/2096/files/ver6-0.pdf.2295
```
[29] T. Koga and S. Selce, A. anf Stengel, Optimization of π0 reconstruction selection and first2296
```
systematic uncertainty evaluation of the efficiencies, Belle II Intern. Note (2020) .2297
```
```
https://docs.belle2.org/record/1823/files/BELLE2-NOTE-PH-2020-003.pdf.2298
```
240
[30] M. Milesi, J. Tan, and P. Urquijo, Lepton Identification in Belle II Using Observables from2299
```
the Electromagnetic Calorimeter and Precision Trackers, EPJ Web Conf. 245 (2020) 06023.2300
```
```
https://www.epj-conferences.org/articles/epjconf/pdf/2020/21/epjconf_2301
```
chep2020_06023.pdf.2302
[31] D. Martschei, M. Feindt, S. Honc, and J. Wagner-Kuhr, Advanced Event Reweighting Using2303
```
Multivariate Analysis, J. Phys. Conf. Ser. 368 (2012) no. 1, 012028.2304
```
```
https://dx.doi.org/10.1088/1742-6596/368/1/012028.2305
```
[32] M. Prim, F. Bernlochner, P. Goldenzweig, et al., Belle, Search for B+ → µ+ νµ and2306
```
B+ → µ+ N with Inclusive Tagging, Phys. Rev. D 101 (Feb., 2020) 032007,2307
```
```
arxiv:1911.03186 [hep-ex].2308
```
```
https://link.aps.org/doi/10.1103/PhysRevD.101.032007.2309
```
[33] L. Feld, Continuum Reweighting - Data-Driven Improvement of the Continuum Monte Carlo2310
```
Simulation for Belle and Belle II , Master’s thesis, Karlsruhe Institute of Technology (KIT),2311
```
2020. https://publish.etp.kit.edu/record/22016.2312
[34] D. Asner, M. Athanas, D. Bliss, et al., CLEO, Search for Exclusive Charmless Hadronic B2313
```
Decays, Phys. Rev. D 53 (1996) 1039–1050, arxiv:hep-ex/9508004.2314
```
```
https://arxiv.org/abs/hep-ex/9508004.2315
```
[35] G. C. Fox and S. Wolfram, Observables for the Analysis of Event Shapes in e+ E-2316
```
Annihilation and Other Processes, Phys. Rev. Lett. 41 (1978) no. 23, 1581.2317
```
```
https://link.aps.org/doi/10.1103/PhysRevLett.41.1581.2318
```
```
[36] S. Lee, K. Suzuki, K. Abe, et al., Belle, Evidence for B0 → π0π0, Phys. Rev. Lett. 91 (2003)2319
```
261801, arxiv:hep-ex/0308040. https://arxiv.org/abs/hep-ex/0308040.2320
[37] J. Bergstra, D. Yamins, and D. Cox, Making a Science of Model Search: Hyperparameter2321
Optimization in Hundreds of Dimensions for Vision Architectures, in Proc. 30th Int. Conf.2322
Mach. Learn., pp. 115–123. PMLR, Feb., 2013.2323
```
https://proceedings.mlr.press/v28/bergstra13.html.2324
```
[38] J. Bergstra, B. Komer, C. Eliasmith, D. Yamins, and D. D. Cox, Hyperopt: A Python2325
```
Library for Model Selection and Hyperparameter Optimization, Comput. Sci. Discov. 8 (July,2326
```
```
2015) 014008. https://dx.doi.org/10.1088/1749-4699/8/1/014008.2327
```
[39] T. Keck, FastBDT: A Speed-Optimized Multivariate Classification Algorithm for the Belle II2328
```
Experiment, Comput. Softw. Big Sci. 1 (Sept., 2017) 2.2329
```
```
http://arxiv.org/abs/1609.06119.2330
```
[40] L. S. Shapley, A Value for N-Person Games, tech. rep., RAND Corporation, Mar., 1952.2331
```
https://www.rand.org/pubs/papers/P295.html.2332
```
[41] S. M. Lundberg and S.-I. Lee, A Unified Approach to Interpreting Model Predictions, in Adv.2333
Neural Inf. Process. Syst., vol. 30. Curran Associates, Inc., 2017. https://proceedings.2334
neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html.2335
[42] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin, B. Nair, R. Katz,2336
J. Himmelfarb, N. Bansal, and S.-I. Lee, From Local Explanations to Global Understanding2337
```
with Explainable AI for Trees, Nat Mach Intell 2 (Jan., 2020) 56–67.2338
```
```
https://www.nature.com/articles/s42256-019-0138-9.2339
```
[43] P. Ramachandran, B. Zoph, and Q. V. Le, Searching for Activation Functions, Oct., 2017.2340
```
arxiv:1710.05941 [cs], http://arxiv.org/abs/1710.05941.2341
```
[44] I. Loshchilov and F. Hutter, Decoupled Weight Decay Regularization, in 7th Int. Conf.2342
Learn. Represent. ICLR 2019 New Orleans USA May 6-9 2019. OpenReview.net, 2019.2343
```
https://openreview.net/forum?id=Bkg6RiCqY7.2344
```
241
[45] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair,2345
A. Courville, and Y. Bengio, Generative Adversarial Networks, 2014. arXiv:1406.26612346
[stat.ML].2347
[46] G. Kasieczka and D. Shih, Robust Jet Classifiers through Distance Correlation, Phys. Rev.2348
```
Lett. 125 (Sept., 2020) 122001, arxiv:2001.05310 [hep-ph].2349
```
```
http://arxiv.org/abs/2001.05310.2350
```
[47] eFFORT , B2-hive, May, 2022. https://github.com/b2-hive/eFFORT.2351
```
[48] D. Bigi and P. Gambino, Revisiting B → Dℓν, Phys. Rev. D 94 (Nov, 2016) 094008.2352
```
```
https://link.aps.org/doi/10.1103/PhysRevD.94.094008.2353
```
[49] T. Keck et al., The Full Event Interpretation – An exclusive tagging algorithm for the Belle2354
II experiment, arXiv:1807.08680 [hep-ex].2355
[50] W. Sutcliffe, N. Rout, L. M., V. Vobbilisetti, T. K., and B. F., Combination of calibration2356
factors for hadronic tagging, BELLE2-NOTE-PH-2023-029 .2357
```
https://docs.belle2.org/record/3642/files/BELLE2-NOTE-PH-2023-029_v2.0.pdf.2358
```
[51] S. Banerjee, E. Ben-Haim, F. Bernlochner, E. Bertholet, M. Bona, A. Bozek, C. Bozzi,2359
J. Brodzicka, V. Chobanova, M. Chrzaszcz, U. Egede, M. Gersabeck, P. Goldenzweig,2360
N. Gharbi, L. Grillo, K. Hayasaka, T. Humair, D. Johnson, T. Kuhr, O. Leroy, A. Lusiani,2361
H. L. Ma, M. Margoni, R. Mizuk, P. Naik, T. N. Petri, A. P. Castro, M. Prim, M. Roney,2362
M. Rotondo, O. Schneider, C. Schwanda, A. J. Schwartz, J. Serrano, B. Shwartz, A. Soffer,2363
M. Whitehead, and J. Yelton, Averages of b-hadron, c-hadron, and τ -lepton properties as of2364
2023 , arXiv:2411.18639 [hep-ex]. https://arxiv.org/abs/2411.18639.2365
[52] H. Junkerkalefeld et al., Probing lepton universality in inclusive, semileptonic B meson2366
```
decays into light (R(Xe/µ)) and heavy (R(Xτ /ℓ)) leptons at Belle II), Belle II Intern. Note2367
```
```
(2023) .2368
```
```
https://docs.belle2.org/record/3755/files/BELLE2-NOTE-PH-2023-037-v504.pdf.2369
```
[53] A. Glazov et al., Studies of B → K+ν ¯ν decays using inclusive and hadronic tagging methods2370
```
based on data collected before LS1., Belle II Intern. Note (2023) .2371
```
```
https://docs.belle2.org/record/3223/files/BELLE2-NOTE-PH-2022-045.pdf.2372
```
[54] Y. S. Amhis, S. Banerjee, E. Ben-Haim, et al., HFLAV, Averages of b-Hadron, c-Hadron,2373
```
and τ -Lepton Properties as of 2021 , Phys. Rev. D 107 (Mar., 2023) 052008,2374
```
```
arxiv:2206.07501 [hep-ex]. http://arxiv.org/abs/2206.07501.2375
```
[55] P. Gambino, K. J. Healey, and C. Mondino, Neural Network Approach to B → Xuℓν, Phys.2376
```
Rev. D 94 (July, 2016) 014031, arxiv:1604.07598 [hep-ph].2377
```
```
http://arxiv.org/abs/1604.07598.2378
```
[56] J. R. Andersen and E. Gardi, Inclusive Spectra in Charmless Semileptonic B Decays by2379
```
Dressed Gluon Exponentiation, JHEP 01 (2006) no. 01, 097, arxiv:hep-ph/0509360.2380
```
```
http://arxiv.org/abs/hep-ph/0509360.2381
```
[57] U. Aglietti, F. Di Lodovico, G. Ferrera, and G. Ricciardi, Inclusive Measure of |Vub| with the2382
```
Analytic Coupling Model , Eur. Phys. J. C 59 (2009) no. 4, 831–840, arxiv:0711.08602383
```
[hep-ph]. http://arxiv.org/abs/0711.0860.2384
[58] L. Cao, W. Sutcliffe, R. Van Tonder, et al., Belle, Measurements of Partial Branching2385
```
Fractions of Inclusive B → Xu ℓ+ νℓ Decays with Hadronic Tagging, Phys. Rev. D 104 (July,2386
```
```
2021) 012008, arxiv:2102.00020 [hep-ex]. http://arxiv.org/abs/2102.00020.2387
```
[59] P. Gambino, P. Giordano, G. Ossola, and N. Uraltsev, Inclusive Semileptonic B Decays and2388
```
the Determination of |Vub|, JHEP 10 (2007) no. 10, 058, arxiv:0707.2493 [hep-ph].2389
```
```
http://arxiv.org/abs/0707.2493.2390
```
242