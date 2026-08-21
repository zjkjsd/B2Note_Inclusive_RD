Belle
```
Measurement of R(D∗) and R(D) with hadronic FEI tagging
```
method using the 365 fb−1 data at Belle II
Lin Wang∗1, Taichiro Koga†2, Kodai Matsuoka‡2, Qi-Dong Zhou§1, Koji Hara¶2,
Toru Iijima‖2,3,4, and Katsuro Nakamura∗∗2
1Institute of Frontier and Interdisciplinary Science, Shandong University, Qingdao, China
```
2High Energy Accelerator Research Organization (KEK), Tsukuba, Japan
```
3Graduate School of Science, Nagoya University, Nagoya, Japan
```
4Kobayashi-Maskawa Institute (KMI), Nagoya University, Nagoya, Japan
```
August 13, 2025
BELLE2-NOTE-PH-2024-056
Version 3.0
Abstract
```
Measurement of branching ratio R(D(∗)) of B → D(∗)τ ντ relative to B → D(∗)ℓνℓ1
```
decays with hadronic tagging is performed by using data sample of 365f b−1 collected2
```
at the Υ(4S) resonance with the Belle II detector at the SuperKEKB asymmetric-3
```
energy e+e− collider. The analysis uses hadronic reconstruction of the tag-side B4
meson based on hadronic FEI and purely leptonic τ decays on signal-side B meson.5
```
We find R(D∗) = 0.242 ± 0.019(stat.) ± 0.016(syst.), R(D) = 0.439 ± 0.055(stat.) ±6
```
```
0.045(syst.), and their correlations ρ = −0.40(stat.) − 0.20(syst.) .7
```
∗202217005@mail.sdu.edu.cn
†taichiro@post.kek.jp
‡matsuoka@post.kek.jp
§qzhou@sdu.edu.cn
¶koji.hara@kek.jp
‖iijima@hepl.phys.nagoya-u.ac.jp
∗∗katsuro@post.kek.jp
Contents
1 Introduction 1
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Analysis over view . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
2 Dataset 2
2.1 Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 basf2 release . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3 Selection 4
3.1 Tag side B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 Signal side B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2.1 Final state particles . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2.2 D, D∗ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
```
3.2.3 Bsig → D(∗)τ ν, Υ(4S) . . . . . . . . . . . . . . . . . . . . . . . . . . 7
```
3.3 Rest of events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.4 Best candidate selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4 Correction 18
4.1 Correction of detector performance . . . . . . . . . . . . . . . . . . . . . . 18
4.2 Correction of branching ratios . . . . . . . . . . . . . . . . . . . . . . . . . 18
```
4.2.1 Branching ratio of B → D(∗)ℓν . . . . . . . . . . . . . . . . . . . . 19
```
4.2.2 Branching ratio of τ → ℓνν . . . . . . . . . . . . . . . . . . . . . . 19
4.2.3 Branching ratio of D∗ . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.2.4 Branching ratio of D . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.2.5 Branching ratio of hadronic B decay . . . . . . . . . . . . . . . . . 20
4.2.6 Branching ratio of B → D∗∗ℓν decay . . . . . . . . . . . . . . . . . 20
4.3 Correction of form factors . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5 Data/MC comparison in side-band 27
5.1 q2 side-band . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.1.1 Data yield and efficiency . . . . . . . . . . . . . . . . . . . . . . . . 27
5.1.2 EECLextra PDF shape . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
5.1.3 M 2miss PDF shape . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
```
5.1.4 Fraction of correctly reconstructed D(∗) . . . . . . . . . . . . . . . . 33
```
5.2 π0 veto side-band . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
```
5.3 D(∗) mass sideband . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
```
6 Signal extraction 40
6.1 Sample and PDF category . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
6.2 Fit parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6.3 Likelihood function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
6.4 Asimov fit sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
6.5 Fitter validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
7 Systematics uncertainties 52
7.1 B → D∗∗ℓ−νℓ and gap mode branching fractions . . . . . . . . . . . . . . . 52
7.2 Hadronic B decay branching fractions . . . . . . . . . . . . . . . . . . . . . 54
7.3 FEI Efficiency correction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
i
7.4 Other efficiency corrections . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
7.5 FEI Efficiency difference of signal and normalization mode . . . . . . . . . 56
7.6 Form factors correction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.7 Continuum background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.8 MC statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.9 Fitter bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.10 τ − → ℓ−ντ νℓ branching fractions . . . . . . . . . . . . . . . . . . . . . . . . 57
```
7.11 Fraction of correctly reconstructed D(∗) . . . . . . . . . . . . . . . . . . . . 57
```
7.12 yield of D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.13 M 2miss resolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
7.14 Total uncertainty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
8 Results of Asimov Fit 60
9 Data fit 61
9.1 Fit in q2 sideband . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
9.2 Fit in π0 ROE sideband . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
9.3 Data fit to selected events . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
9.3.1 Sanity check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
10 Results 78
11 Comparison with past measurements 78
A PDF 79
ii
Version Date Section Changes
1.0 Sep.30, 2024 All Initial note for the internal check.
2.0 Feb.2, 2025 All 1st version of official note for WG review.
2.1 Feb.6, 2025 Systematic form factor systematic is updated
2.2 Feb.13, 2025 modify text following Markus’s comment
2.3 Feb.20, 2025 update with new BR and form factor
2.4 Feb.25, 2025 modify text following Lu’s comment
2.5 Mar.6, 2025 systematics, all reflect Marcel’s comment at WG1 review
reflect Michele’s comment at WG1 review
2.6 Mar.23, 2025 selection, all reflect second comments at WG1 review
modify selection to add eta veto in ROE
Bug fix of global tag for lepton PID
2.6.1 Mar.26, 2025 systematics bug fix in Table 7.1
2.7 Apr.18, 2025 after WG1 review
update BR of D∗∗τ ν
separate gap mode template in fitting
```
add D(∗) mass sideband
```
add M 2miss systematics
2.8 May.22, 2025 reflect first comment at RC review
change binning to reduce MC statistics error
2.8.2 June.24, 2025 reflect second comment at RC review
2.9 Jul.17, 2025 increase endcap gamma energy threshold
partial unbox
3.0 Aug.14, 2025 full unbox
Update from the last version is written by red characters.
iii
1 Introduction8
1.1 Introduction9
```
In the Standard Model (SM) of particle physics, semileptonic B decays at the quark10
```
level proceed via b → c or b → u transitions that are mediated by a W boson and11
produce a charged lepton and its corresponding neutrino. The W boson couples identically12
to the three lepton generations [1], a symmetry known as Lepton Flavour Universality13
```
(LFU) that is a fundamental postulate of the SM. LFU can be tested by measuring14
```
```
R(D(∗)) = BR(B→D
```
```
(∗)τ ν)
```
```
BR(B→D(∗)ℓν) : where the denominator is referred to as the normalization mode15
```
with ℓ = e or µ. Semileptonic B decays involving a τ lepton are sensitive to new physics16
```
(NP) models [2, 3, 4, 5] and their decays are less constrained by data than are semileptonic17
```
decays to electrons and muons. While the couplings to all lepton flavors are the same in18
```
the SM, the larger τ mass results in a smaller phase space factor, so R(D∗) is expected19
```
```
to be 0.254 ± 0.003 [6] by the SM. R(D(∗)) has been measured by the BaBar [7, 8],20
```
Belle [9, 10, 11], and LHCb [12, 13, 14, 15] collaborations. The combined results of these21
measurements exceed the SM expectation by approximately 3 σ [6].22
```
In 2023, Belle II measured the R(D∗) with hadronic tag by using 189 f b−1 data [16]:23
```
```
R(D∗) = 0.262+0.041−0.039(stat.)+0.035−0.032(syst.). Due to low efficiency of hadronic tag (=low24
```
```
branching ratio of hadronic decays), the statistical uncertainty has been the largest er-25
```
```
ror source. In this time, we update the analysis to measure R(D∗) and R(D) with LS126
```
dataset. Followings are major changes from the last analysis:27
• Data statistics increased from 189 f b−1 to 365 f b−128
• MC sample is updated from MC14 run independent to MC15 run dependent29
```
• B → Dτ ν sample is reconstructed and added to fit, in order to measure R(D)30
```
```
• Additional D(∗) decay modes are reconstructed to increase statistics31
```
• Selection criteria of daughter particles is modified32
• Selection criteria of ROE is modified to remove fake photons and beam background33
photons with MVA variables34
• ”isSignal” requirement is removed from definition of signal and background, in order35
to increase statistics, avoid complex of the MC matching, and avoid difficulty to36
evaluate data/MC agreement of the MC matching37
• Kernel density estimation is not applied to PDF for signal extraction. Instead,38
binning of PDF is optimised to reduce fitter bias from MC statistics.39
This note explains the analysis method in detail. Dataset is described in Sec. 2. Selection40
criteria and general corrections are in Sec. 3,4. Data/MC comparison at side-band and41
additional corrections are in Sec. 5. Signal extraction method is in Sec. 6, and systematic42
uncertainties are in Section 7.43
1.2 Analysis over view44
```
In order to measure R(D(∗)), we reconstruct B → D(∗)ℓν (ℓ = e, µ) (normalization mode)45
```
```
and B → D(∗)τ ν (signal mode) simultaneously and take ratio of their branching ratios.46
```
1
```
Figure 1.1 shows a schematic view of the signal reconstruction. The D(∗) decays are47
```
```
reconstructed by combination of daughter particles (π, K, π0 → γγ, K0s → ππ) detected by48
```
```
Belle II. In order to increase statistics, several kind of D(∗) decay modes are reconstructed.49
```
```
The ℓ is selected by lepton particle identification (PID). The τ is reconstructed by leptonic50
```
decays of τ → eνν and τ → µνν, in order to reject hadronic background. Because51
the reconstructed final state particles of the signal mode are the same as that of the52
normalization mode, many systematics uncertainties are canceled in this method. On the53
other hand, identification of signal and normalization modes is difficult due to missing54
neutrinos. In order to measure the missing neutrinos mass for the signal identification,55
```
tag-side B (Btag) is fully reconstructed with hadronic Full Event Interpretation (FEI)56
```
```
algorithm. In the rest of event (ROE), no charged tracks and π0 candidates are allowed57
```
to reject background.58
One of the major background in this analysis is B → D∗∗ℓν, where the D∗∗ is excited59
```
charm-meson cascade decays of D∗0 , D1, D′1, D∗2 to D(∗) ground state. When one or more60
```
```
daughter particles (π, π0, γ etc.) from D∗∗ is mis-reconstructed, it can be identified as61
```
```
B → D(∗)ℓν. Because part of the branching ratio of B → D∗∗ℓν decays have not been62
```
measured so far, their systematic uncertainties are estimated conservatively by following63
the present understanding of the branching ratios. Gap mode, which is the difference64
of exclusive and sum of inclusive B → D∗∗ℓν branching ratio measurements, is mainly65
```
modeled by B → D(∗)ηℓ. Another major background is hadronic B decays of B →66
```
```
D(∗)D(∗), B → D(∗)D(∗)K, and B → D(∗)nπ(π0) etc. Their uncertainties are estimated67
```
based on the past branching ratio measurements on PDG.68
The signal mode, normalization modes and backgrounds are extracted by fitting two69
```
dimensional distributions of energy sum of ECL clusters in the rest of events (EECLextra) and70
```
```
Missing neutrino mass squared (M 2miss):71
```
```
M 2miss = (Pbeam − PBtag − PD∗ − Pℓ)2 (1.1)72
```
, where P is four momentum. The signal mode has multiple neutrinos in the final state and73
tends to have large M 2miss. On the other hand, the normalization mode has one neutrino74
and M 2miss is peaked around zero. The other background with additional daughter particles75
can be identified by large EECLextra, because no remained particles are expected for signal76
and normalization modes. The fit range of M 2miss and EECLextra are widely taken to constrain77
the backgrounds by the fitting. The PDF templates of M 2miss and EECLextra are obtained by78
MC. The data/MC agreement of the PDF shape is validated at side-band with low M 2miss79
and side-band with additional π0 candidates in ROE.80
The physics sensitivity and fitter performance are evaluated by Asimov data and toy81
experiments. The systematic uncertainties from detector response, background, signal82
efficiencies and PDF are evaluated by using toys. Due to low efficiency of hadronic tag,83
the statistical uncertainty is expected to be the largest error source.84
2 Dataset85
2.1 Dataset86
Below data is used for the analysis:87
• FEI skimmed proc13+prompt data, 365 f b−1. The collection is88
”/belle/collection/Data/proc13prompt skim 11180500 v2”.89
2
Figure 1.1: Schematic view of the signal reconstruction. The signal side B is reconstructed
```
by combination of ℓ (electron or muon) and D or D∗. The tag side B is reconstructed by
```
hadronic FEI. No additional track is allowed in the rest of events.
Below MC samples are used:90
• FEI skimmed MC15rd generic BB, cc, uu, dd, and ss samples equivalent to 1444 f b−1.91
The collections are92
”/belle/collection/MC/MC15rd BB skim 11180500 v2”,93
”/belle/collection/MC/MC15rd ccbar skim 11180500 v2”,94
”/belle/collection/MC/MC15rd uds skim 11180500 v2”.95
• FEI skimmed MC15rd B → D∗∗ℓν background MC equivalent to 8M events. The96
collection is97
”/belle/group/physics/SLME/FEI Dgap signal”.98
• unskimmed MC15rd generic BB sample equivalent to 699 f b−1for correcting D99
branching ratio in Sec. 4.2.4.100
The generic MC15rd is used to simulate both signal and background. Part of B → D∗∗ℓν101
decays in the generic MC is replaced with the background MC to improve their modeling.102
Detail explanation is in Sec. 4.2.103
2.2 basf2 release104
We used basf2 release of ”light-2405-quaxo” for reconstruction and analysis. The analysis105
code is in ”https://gitlab.desy.de/belle2/analyses/wg1 dtaunu hadtag p13rel06”.106
3
Table 3.1: Selection criteria of event and tag side B.
variable selection criteria
```
The number of clean track in an event (nCleanedTrack) nCleanedTrack> 4
```
```
FEI signal probability (pFEI) pFEI > 0.01
```
```
Beam constrained mass (Mbc =
```
p
```
(Ebeam)2 − |⃗p Btag |2) Mbc > 5.27 GeV
```
```
Angle between thrust axis of the Btag and others (cosTBTO) cosTBTO<0.9
```
```
Energy difference (∆E = EBtag − Ebeam) −0.15 < ∆E < 0.1 GeV
```
```
5.25 5.255 5.26 5.265 5.27 5.275 5.28 5.285 5.29 5.295 5.3Mbc (GeV)0
```
1000020000
3000040000
5000060000
7000080000
90000data
BB
continuum
MC is luminosity normalized
5.25 5.255 5.26 5.265 5.27 5.275 5.28 5.285 5.29 5.295 5.300.20.4
0.60.811.2
1.41.61.82
data/MC ratio
```
0.2− 0.15− 0.1− 0.05− 0 0.05 0.1 0.15 0.2deltaE (GeV)0
```
20
40
60
80
100
120310×data
BB
continuum
MC is luminosity normalized
0.2− 0.15− 0.1− 0.05− 0 0.05 0.1 0.15 0.200.20.4
0.60.811.2
1.41.61.82
data/MC ratio
1− 0.8− 0.6− 0.4− 0.2− 0 0.2 0.4 0.6 0.8 1cotTBTO0
2040
6080
100120
140160
180200
310×
data
BB
continuum
MC is luminosity normalized
1− 0.8− 0.6− 0.4− 0.2− 0 0.2 0.4 0.6 0.8 100.20.4
0.60.811.2
1.41.61.82
data/MC ratio
```
Figure 3.1: Btag variables of Mbc (left), deltaE (middle), cosTBTO (right) used for the
```
selection. All Btag selections are applied except for cosTBTO<0.9. Because track momen-
tum scale correction is applied to data after the selection, there are data points outside
the selection criteria in the plots. The same way is used for the FEI calibration analysis.
3 Selection107
Signal reconstruction procedure is explained in this section.108
3.1 Tag side B109
```
The tag side B (Btag) is reconstructed with hadronic FEI. The standard preselection,110
```
which is used for other analysis of FEI efficiency calibration with B → Xℓν and B →111
```
D(∗)π [17], is applied to the Btag candidates. The selections are summarized in Table 3.1112
```
and Fig. 3.1. The signal probability of FEI is required to be more than 0.01. Although113
data/MC agreement is not perfect, we use the same criteria as the other analysis of FEI114
calibration, in order to use the calibrated data efficiency provided by them. All Btag115
candidates in an event are used to increase statistics, although only one Btag candidate116
with the highest signal probability in an event is used for the FEI calibration analysis.117
3.2 Signal side B118
After the Btag reconstruction, the remaining tracks and clusters in each event are at-119
tributed to the signal B meson candidates of B → D∗τ ν, B → D∗ℓν, B → Dτ ν and120
B → Dℓν decays. Bsig is reconstructed through the following combinations of a D∗121
meson and a lepton candidate:122
• B0sig → D∗−ℓ+, where ℓ = e or µ, D∗− → D0π− or D∗− → D−π0123
• B+sig → ¯D∗0ℓ+, where ℓ = e or µ, D∗0 → D0π0 or D∗0 → D0γ124
• B0sig → D−ℓ+, where ℓ = e or µ125
4
Table 3.2: List of reconstructed D0 decay modes.
Decay Branching ratio on PDG
```
D0 → K−π+π0 (14.4 ±0.50)%
```
```
D0 → K−π+π−π+ (8.23 ±0.14)%
```
```
D0 → K0S π+π−π0 (5.20 ±0.60)%
```
```
D0 → K−π+ (3.95 ±0.03)%
```
```
D0 → K0S π+π− (2.80 ±0.18)%
```
```
D0 → K0S π0 (1.24 ±0.02)%
```
```
D0 → K−K+ (0.41 ±0.01)%
```
Table 3.3: List of reconstructed D+ decay modes. The D+ decay modes in gray-shaded
lines are newly added.
Decay Branching ratio on PDG
```
D+ → K−π+π+ (9.38 ±0.16)%
```
```
D+ → K0S π+π0 (7.36 ±0.21)%
```
```
D+ → K−π+π+π0 (6.25 ±0.18)%
```
```
D+ → K0S π+π−π+ (3.10 ±0.09)%
```
```
D+ → K0S π+ (1.56 ±0.03)%
```
```
D+ → K−K+π+ (0.968 ±0.018)%
```
```
D+ → K0S K+ (0.304 ± 0.01)%
```
• B+sig → ¯D0ℓ+, where ℓ = e or µ126
```
the D0 (D+) candidates are reconstructed with seven (seven) decay modes, as listed in127
```
Table 3.2-3.3. These modes are selected because their branching ratios are relatively large128
and multiplicity is relatively small. Here, charge conjugation is implied and is considered129
in all the steps of the analysis.130
3.2.1 Final state particles131
The selection criteria are optimized as shown in Table 3.4. On the Bsig side, all e, µ, K, π132
tracks must fulfill the requirements dr < 2.0 cm, |dz| < 4.0 cm, pT > 0.1 GeV/c. Lepton133
candidates are required to satisfy global particle-identification requirements for an electron134
```
(muon) with a BDT (likelihood) greater than 0.9. p>0.4(0.7) GeV is required to electron135
```
```
(muon) in order to reach ECL (KLM). Bremsstrahlung correction is applied to electron136
```
by using correctBremsBelle module with default arguments. It is required that PID137
correction is available at region of p and costheta of the lepton candidates. If not, the138
candidates are removed.139
```
Kaon (Pion) candidates are required to satisfy binary PID > 0.1 with likelihood.140
```
Neural Network based PID is not used due to smaller coverage of the PID correction141
table at low momentum, provided by systematic framework. p>0.3 GeV is required to142
Kaon because fake rate correction is not available below 0.3 GeV. No PID is required to143
```
low momentum pion (p < 0.3 GeV) to keep statistics. No nCDCHits cut is applied to144
```
increase statistics. For the slow charged pion, refers to the π+slow daughter produced in the145
D∗+ → D0π+slow decay, different cut of p > 0.05 GeV/c is used without PID.146
5
Table 3.4: Selection criteria on signal side B.
Particles Selections
good track dr < 2 cm, |dz| < 4 cm, pT > 0.1 GeV/c
```
e− good track, p > 0.4 GeV , Pglobale > 0.9 (BDT), Bremss correction
```
```
µ− good track, p > 0.7 GeV , Pglobalµ > 0.9 (likelihood)
```
π+ good track, Pbinaryπ > 0.1 or p < 0.3 GeV
K+ good track, PbinaryK > 0.1 and p > 0.3 GeV
π+slow dr < 2 cm, |dz| < 4 cm, p > 0.05 GeV/c
π0 pi0:eff40 May2020, γ: |clusterTiming| < 200 ns,
122.4 < Mπ0 < 143.0 MeV, Eq:3.1
π0slow pi0:eff50 May2020, γ: |clusterTiming| < 200 ns,
118.3 < Mπ0 < 147.0 MeV, Eq:3.1
K0S ksSelector “standard”, 0.47 < MK0S < 0.52 GeV
D mode dependent MD cut, Table 3.6
D∗ mode dependent ∆MD∗ cut, Table 3.6
Bsig χ2 of vertex fit >0, q2 > 4.0 GeV2
```
π0 (slow π0) is reconstructed with pi0:eff40 (pi0:eff50) selections with a cus-147
```
```
tomized mass window of [122.4, 143.0] MeV ([118.3, 147.0] MeV). In addition, |clusterTiming| <148
```
200ns, minC2TDist and clusterZernikeMVA based cuts are applied:149

minC2TDist
X cm
2
+

clusterZernikaMVA
Y
2
```
> 1.0 (3.1)150
```
where X and Y are constants summarized in Table 3.5. The same selections as slow π0151
are used for slow photon.152
Candidates K0S are reconstructed via K0S → π−π+, where all candidates pass the153
“standard” selection in the ksSelector module of basf2. In addition, loose mass selection154
of 0.47 < MK0S < 0.52 GeV is applied.155
3.2.2 D, D∗156
Using the final state particles in Sec. 3.2.1, D and D∗ candidates are reconstructed as157
shown in Fig. 3.2–3.4 with treeFit. The window of D mass and mass difference of D∗ and158
D are optimized based on figure of merit as shown in Table 3.6-3.7.159
```
Below is detail of the optimization. First, we evaluated mass resolution (σ) for each160
```
MD and ∆MD∗ distributions MC and data. The resolution is defined asymmetrically in161
```
the lower side (σL) and the higher side (σH) from the reconstructed mass peak. They162
```
are estimated by fitting the mass distribution. We use following fitting functions: signal163
of a double-sided Gaussian, peaking background of Gaussian or Crystal ball, and non-164
peaking background of 1st Chebychev. When MC is fitted, all parameters are floated. The165
measured σL and σH of the double Gaussian by MC are summarized in Table 3.7. Data166
is fitted by the same functions. Normalization parameters of signal and background, and167
```
a resolution parameter(Rσ), which scales the sigma of Gaussians of signal and peaking168
```
background commonly, are floated for the data fit. Other parameters are fixed with169
6
```
Table 3.5: Parameter values of the cut function eq. 3.1 for γ selections. γhigh(low) denotes
```
```
either photons of π0 daughters with higher(lower) energy.
```
Candidates cluster region Parameter values
X [cm] Y
π0 daughters in D decays
γhigh
Forward 85 0.65
Barrel 85 0.60
Backward 85 0.55
γlow
Forward 85 0.45
Barrel 85 0.45
Backward 40 0.65
π0 daughters in D∗ decays
γhigh
Forward 70 0.45
Barrel 70 0.30
Backward 60 0.45
γlow
Forward 40 0.70
Barrel 40 0.40
Backward 85 0.20
the post-fit parameters obtained by MC. The estimated Rσ is shown in Table 3.7. To170
determine mass window of MC, we define figure of merit as follows: FoM= S/
p
```
(S + N ),171
```
```
where S is the number of correctly reconstructed D(∗) and B is the number of incorrectly172
```
```
reconstructed D(∗). When figure of merit is evaluated, σL and σH are varied with common173
```
fraction and point with maximum FoM is chosen as the selection criteria. For example, 2σ174
```
in Table 3.6 represents that lower(higher) mass window of MC is set to 2σL (2σH ). Finally,175
```
mass window of data is determined by scaling that of MC by the resolution parameter,176
in order to take account the difference of mass resolution. For example, 2σ in Table 3.6177
```
represents that lower(higher) mass window of data is set to 2RσσL (2RσσH ).178
```
```
3.2.3 Bsig → D(∗)τ ν, Υ(4S)179
```
```
Each D(∗) is then combined with a lepton candidate to form the Bsig. The vertex of the180
```
```
D(∗)ℓ combination is fitted while constraining all daughters K0S s and π0s to the nominal181
```
```
mass, respectively. Any Bsig candidate that fails this fit is discarded (χ2 > 0). The square182
```
of momentum transfer to a lepton system in the signal B decays, q2, is required to more183
```
than 4.0 (GeV/c)2 in order to enhance signal mode. Finally, the candidate Bsig is then184
```
```
combined with the Btag to form the Υ(4S) → B+B−, mixed and unmixed B0B0.185
```
3.3 Rest of events186
```
After the Υ(4S) reconstruction, remaining tracks and clusters are attributed to the187
```
```
rest-of-the-event (ROE). Table 3.8 shows the used ROE mask. Energy threshold of188
```
photon at barrel is set to 50 MeV, because data/MC agreement is poor below the189
50 MeV. FakephotonSuppressionMVA>0.2 and beamBackgroundSuppressionMVA>0.5190
are required to reject fake photon and beam background, as shown in Fig. 3.5. No charged191
tracks are allowed in the ROE. In addition, no π0 candidates are required in ROE with192
```
pi0:eff30 selection. At the previous version of note, η → γγ veto was applied to ROE. We193
```
7
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID10_11.pdfFigures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmFigures/plot_rdst_15/sel_noDmas
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID10_14.pdfFigures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmFigures/plot_rdst_15/sel_noDmas
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID10_17.pdf
Figure 3.2: Invariant mass of D0 in each decay mode before applying the mass selection.
Mass width and purity are different in each mode due to the difference of daughter par-
ticles.
8
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID20_21.pdfFigures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmFigures/plot_rdst_15/sel_noDmas
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID20_24.pdfFigures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmFigures/plot_rdst_15/sel_noDmas
Figures/plot_rdst_15/sel_noDmass/Bsig_d0_M_before2_data_dmID20_27.pdf
Figure 3.3: Invariant mass of D+ in each decay mode before applying the mass selection.
Mass width and purity are different in each mode due to the difference of daughter par-
ticles.
9
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2
```
) mass difference (GeV)π0->D*+D* and D (D
```
0
500
1000
1500
2000
2500
3000 data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is luminosity normalized
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.20.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2
```
) mass difference (GeV)0π+->D*+D* and D (D
```
0
50
100
150
200
250
300
350
400
data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is luminosity normalized
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.20.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2
```
) mass difference (GeV)0π0->D*0D* and D (D
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
1800
data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is luminosity normalized
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.20.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2
```
) mass difference (GeV)γ0->D*0D* and D (D
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
900data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is luminosity normalized
0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.20.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
Figure 3.4: Mass differences of D∗ and D in each decay mode before applying the mass
selection. Mass width and purity are different in each mode due to the difference of
charged slow π, slow π0, and slow γ.
10
```
Table 3.6: Signal regions on MD and ∆MD∗ . The D(∗) decay modes in gray-shaded lines
```
are newly added in this analysis.
D∗ decays D decays MD ∆MD∗
D∗+ → D0π+
D0 → K−π+π0 2.5σ 3.3σ
D0 → K−π+π−π+ 4.1σ 4.9σ
D0 → K0S π+π−π0 1.8σ 2.6σ
D0 → K−π+ 5.0σ 5.0σ
D0 → K0S π+π− 4.3σ 4.7σ
D0 → K0S π0 2.4σ 3.6σ
D0 → K−K+ 4.9σ 3.0σ
D∗+ → D+π0
D+ → K−π+π+ 3.8σ 3.6σ
D+ → K0S π+π0 3.3σ 2.5σ
D+ → K−π+π+π0 1.6σ 2.1σ
D+ → K0S π+π−π+ 1.6σ 2.3σ
D+ → K0S π+ 4.6σ 1.5σ
D+ → K−K+π+ 2.4σ 1.5σ
D+ → K0S K+ 1.2σ 2.7σ
D∗0 → D0π0
D0 → K−π+π0 1.4σ 2.1σ
D0 → K−π+π−π+ 2.6σ 2.3σ
D0 → K0S π+π−π0 1.4σ 1.4σ
D0 → K−π+ 5.0σ 2.5σ
D0 → K0S π+π− 3.8σ 2.2σ
D0 → K0S π0 1.8σ 2.5σ
D0 → K−K+ 3.9σ 2.0σ
D∗0 → D0γ
D0 → K−π+π0 1.4σ 2.1σ
D0 → K−π+π−π+ 3.4σ 4.4σ
D0 → K0S π+π−π0 1.4σ 1.7σ
D0 → K−π+ 4.6σ 5.0σ
D0 → K0S π+π− 2.5σ 3.4σ
D0 → K0S π0 1.9σ 4.3σ
D0 → K−K+ 1.5σ 3.9σ
D0
D0 → K−π+π0 2.1σ
D0 → K−π+π−π+ 4.4σ
D0 → K0S π+π−π0 1.7σ
D0 → K−π+ 5.0σ
D0 → K0S π+π− 3.4σ
D0 → K0S π0 4.3σ
D0 → K−K+ 3.9σ
D+
D+ → K−π+π+ 4.1σ
D+ → K0S π+π0 1.6σ
D+ → K−π+π+π0 1.5σ
D+ → K0S π+π−π+ 2.2σ
D+ → K0S π+ 3.1σ
D+ → K−K+π+ 2.5σ
D+ → K0S K+ 2.5σ
11
Table 3.7: MD and ∆MD∗ resolutions.
```
D(∗) decays σL [MeV/c2] (MC) σH [MeV/c2](M C) data/MC ratio of σ (Rσ)
```
D0 → K−π+π0 15.85 10.47 0.954
D0 → K−π+π−π+ 4.58 3.48 1.087
D0 → K0S π+π−π0 11.60 8.33 1.052
D0 → K−π+ 4.24 3.92 1.127
D0 → K0S π+π− 4.02 3.43 0.984
D0 → K0S π0 22.46 14.70 0.725
D0 → K−K+ 4.31 3.60 0.862
D+ → K−π+π+ 4.18 3.65 0.925
D+ → K0S π+π0 16.30 10.30 1.079
D+ → K−π+π+π0 12.36 8.56 1.051
D+ → K0S π+π−π+ 3.89 3.23 1.004
D+ → K0S π+ 3.89 3.63 1.232
D+ → K−K+π+ 3.57 3.05 0.814
D+ → K0S K+ 4.57 4.42 1.250
D∗+ → D0π+ 0.701 0.694 1.141
D∗+ → D+π0 1.080 1.185 0.819
D∗0 → D0π0 1.230 1.156 1.125
D∗0 → D0γ 9.909 6.817 0.987
removed the η veto in order to constrain gap mode by fitting.194
3.4 Best candidate selection195
```
There are multiple Y (4S) candidates in an event as shown in Figure 3.6 and Table 3.10.196
```
A best candidate selection is thus applied following five steps in chronological order:197
1. Btag probability: the candidates with the highest pF EI are selected. B0tag and B+tag198
are selected independently.199
2. D∗ mode selection:D∗+ → D0π+ candidates are selected at the first priority, D∗+ →200
D+π0 at the second priority, D∗0 → D0π0 at the third priority, D∗0 → D0γ at the201
fourth priority, D0 at the fifth priority, and D+ at the sixth priority.202
3. D∗-mode-dependent selections: the candidates in Table 3.9 are selected.203
4. D mode selection: the candidates with D mode with highest branching ratio is204
selected.205
5. Random: Finally, one of the remaining multiple candidates are selected randomly.206
Main reasons of the high multiplicity are multiple Btag candidates found by FEI, and207
D∗ candidates which are double counted to D∗ sample and D sample. After step2., the208
multiplicity is small as shown in Figure 3.6.209
Table 3.11 shows the simulated events after passing all selections including the best210
candidate selections. The number of selected B → D∗τ ν, B → Dτ ν,B → D∗ℓν, B → Dℓν211
are about 600, 300, 15000, and 4000, respectively. The main backgrounds are B → D∗∗ℓν212
12
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
fakephotonSuppressionMVA
0
5000
10000
15000
20000
25000
30000
```
isSignal==1γ
```
isSignal!=1γ
MC is luminosity normalized
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
beamBackgroundSuppressionExpert
0
10000
20000
30000
40000
50000
60000
70000
80000
```
isSignal==1γ
```
isSignal!=1γ
MC is luminosity normalized
```
Figure 3.5: FakephotonSuppressionMVA (left) and beambackgroundSuppressionMVA
```
```
(right) of the photons in the rest of the events.
```
Table 3.8: Selection criteria for the rest of events.
Particles Selections
ROE mask
Tracks dr < 5 cm, |dz| < 10 cm, pT > 0.1 GeV/c, nCDCHits > 0
```
Clusters energy > 0.10(FW), 0.05(BR), 0.10 GeV(BW),|clusterTiming| < 200 ns,
```
minC2TDist > 15 cm,
fakePhotonSuppressionMVA>0.2,
beambackgroundPhotonSuppressionMVA>0.5
Charged track roeCharge == 0, nROE Tracks < 1
```
Neutral cluster N (π0) < 1 with eff30
```
Table 3.9: D∗ mode dependent best candidate selection for step 3.
D∗ mode Selection
D∗+ → D0π+ The maximum χ2 probability of the second Bsig vertex fit
```
D∗+ → D+π0 The minimum χ2(Mπ0 )
```
```
D∗0 → D0π0 The minimum χ2(Mπ0 )
```
D∗0 → D0γ The most energetic γlow
Table 3.10: The averaged number of event multiplicity of data. Values in parentheses
show that of MC.
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
```
before step 1. 1.26 (1.26) (Btag)
```
```
after step 1. 1.19 (1.21)
```
```
after step 2. 1.01(1.01) 1.03(1.04) 1.04(1.04) 1.07(1.08) 1.03(1.03) 1.01 (1.02)
```
```
after step 3. 1.00(1.00) 1.01(1.01) 1.00(1.01) 1.00(1.00) 1.03(1.03) 1.01 (1.02)
```
```
after step 4. 1.00(1.00) 1.01(1.01) 1.00(1.01) 1.00(1.00) 1.02(1.02) 1.01 (1.01)
```
```
after step 5. 1.00 (1.00) 1.00 (1.00) 1.00 (1.00) 1.00 (1.00) 1.00 (1.00) 1.00 (1.00)
```
13
0 1 2 3 4 5 6 7 8 9 10
tagsignal probability rank of B
0
5000
10000
15000
20000
25000
30000
35000
40000
45000 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(a) before step 1.
```
0 1 2 3 4 5 6 7 8 9 10
sigThe number of B
0
5000
10000
15000
20000
25000
30000 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(b) after step 1.
```
0 1 2 3 4 5 6 7 8 9 10
sigThe number of B
0
5000
10000
15000
20000
25000
30000
35000
40000 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(c) after step 2.
```
0 1 2 3 4 5 6 7 8 9 10
sigThe number of B
0
5000
10000
15000
20000
25000
30000
35000
40000
45000data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(d) after step 3.
```
0 1 2 3 4 5 6 7 8 9 10
sigThe number of B
0
5000
10000
15000
20000
25000
30000
35000
40000
45000data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(e) after step 4.
```
0 1 2 3 4 5 6 7 8 9 10
sigThe number of B
0
5000
10000
15000
20000
25000
30000
35000
40000
45000 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 1 2 3 4 5 6 7 8 9 100.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(f) after step 5.
```
```
Figure 3.6: Multiplicity of Y(4S) candidates in each event after the selection. The rank of
```
```
Btag ordered by FEI signal probability before the best candidate selection (top left) and
```
```
the number of Bsig candidates in each step (other five plots) are shown.
```
14
Table 3.11: Expected yields of candidate categories and D∗ modes at 365 fb−1 in MC after
```
all selections. The world average R(D(∗)) values are assumed for yields of B → D∗τ −ντ .
```
Category Expected yields in MC
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
B → D∗τ ν 107 14 63 104 372 61
B → Dτ ν 0 0 1.4 21 240 101
B → D∗ℓν 2366 294 1306 2379 9788 1478
B → Dℓν 0.9 2.9 6.9 216 2920 1229
B → D∗∗ℓν, D∗∗τ ν and gap 196 37 120 442 1583 557
hadronic B decay 86 14 44 162 605 279
continuum 2.1 0.8 2.2 33 181 84
others 0.2 0 0 0.1 0.8 4.2
Total 2758 360 1543 3358 15686 3793
and hadronic B decays. In D∗+ → D0π+, D∗+ → D+π0 and D∗0 → D0π0 samples,213
B → D∗τ ν and B → D∗ℓν are selected with high purity. In D∗0 → D0γ sample, B → Dτ ν214
and B → Dℓν are contaminated due to low purity of slow γ. In D samples, the D∗ and215
D are contaminated due to missed slow pions and slow gamma. Especially, in D0 sample,216
feed down from D∗+ → D0π+, D∗0 → D0π0, and D∗0 → D0γ are large. Figure 3.7–3.9217
show distributions of the M 2miss and EECLextra. The signal mode has multiple neutrinos in the218
final state and tends to have large M 2miss. On the other hand, the normalization mode has219
one neutrino and M 2miss is peaked around zero. The background with additional daughter220
particles can be identified by large EECLextra, because no remaining particles are expected for221
signal and normalization modes peaked at EECLextra = 0. The signal mode can be extracted222
from the small EECLextra with high M 2miss as shown in Fig. 3.9.223
15
```
2− 0 2 4 6 8 10 12)2(GeV2
```
missM
1−10
1
10
210
310 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
2− 0 2 4 6 8 10 12
```
)2(GeV2missM
```
1−10
1
10
210 ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 0 2 4 6 8 10 12)2(GeV2
```
missM
1−10
1
10
210
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10 12)2(GeV2
```
missM
1−10
1
10
210
310 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
2− 0 2 4 6 8 10 12
```
)2(GeV2missM
```
1−10
1
10
210
310ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(e) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10 12)2(GeV2
```
missM
1−10
1
10
210
310 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(f) B0 → D+τ ν
```
```
Figure 3.7: MC distributions of the M 2miss in each D(∗) decay mode. The signal mode (red
```
```
and light blue) has multiple neutrinos in the final state and tends to have large M 2miss. On
```
```
the other hand, the normalization mode (orange and blue) has one neutrino and M 2miss is
```
peaked around zero.
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
200
400
600
800
1000
1200 ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
20
40
60
80
100
120
140
160 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
100
200
300
400
500
600
700 ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
200
400
600
800
1000ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
500
1000
1500
2000
2500
3000
3500 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(e) B+ → D0τ ν
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
100200
300400
500
600700
800900
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(f) B0 → D+τ ν
```
```
Figure 3.8: MC distributions of the EECLextra in each D(∗) decay mode. The y-axis is linear
```
```
scale and only normalization mode (orange and blue) are visible. Because no remained
```
```
particles are expected for normalization modes, they are peaked at EECLextra = 0. In D0 (e)
```
```
and D+ (f) samples, D∗ℓν is peaked around 0.2 GeV due to γ from slow π0.
```
16
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
10
20
30
40
50ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
1
2
3
4
5
6
7 ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
5
10
15
20
25
30ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
10
20
30
40
50
60 ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
20
40
60
80
100
120
140 ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
```
(e) B+ → D0τ ν
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2
```
(GeV)ECLextraE
```
0
10
20
30
40
50ντD*
ντDνD*l
νDl
D**hadron
continuumOther
MC is luminosity normalized
```
(f) B0 → D+τ ν
```
```
Figure 3.9: MC distributions of the EECLextra with high Missing mass square cut (1.5<
```
```
Mmiss2 < 6.0 GeV2 for D∗, 3.0< Mmiss2 < 8.0 GeV2 for D ) in each D(∗) decay mode.
```
```
Because no remained particles are expected for signal modes (red and light blue), they
```
are peaked at EECLextra = 0. Distribution is not smooth due to MC statistics uncertainty.
For fitting, coarser binning is used.
17
4 Correction224
Several corrections are applied to data and MC, in order to improve data/MC agreement.225
In this section, general corrections following recommendations from physics performance226
group, WG1, and PDG are explained. In this note, all corrections are applied to all plots227
and tables, if nothing mentioned.228
4.1 Correction of detector performance229
Several corrections are applied based on the recommendations from physics performance230
group. Detail explanations are in https://xwiki.desy.de/xwiki/rest/p/3f4b5 . Below cor-231
rections are applied to data:232
```
• track momentum scaling (tracking data Moriond23 v1)233
```
```
• photon energy bias (PhotonEnergyBiasCorrection MC15rd June2023)234
```
Below corrections are applied to MC:235
```
• hadron PID correction (systematic framework)236
```
```
• lepton PID correction (leptonid official rel6 mc15rd, chargedpidmva rel6 v5, sys-237
```
```
tematic framework)238
```
```
• slow π± efficiency (provided by tracking group on the above xwiki)239
```
```
• γ efficiency (PhotonEfficiencyDataMCRatio Run1MC15rd April2024)240
```
```
• π0 efficiency (provided by neutral group locally by using our π0 selection)241
```
• mode-dependent FEI efficiency provided by git@gitlab.desy.de:belle2/performance/correction-242
tables.git243
The weights are applied to each event. Total weight of an event is multiplication of all244
weights of the listed corrections.245
Track momentum scaling is applied after Btag selection, because track momentum246
scaling is not applied in the FEI efficiency calibration analysis of B → Xℓν and B →247
```
D(∗)π.248
```
The slow π, π0, and γ efficiencies are applied to not only D∗ samples but also D249
samples, because if the slow particles are missed in an event, only D is reconstructed and250
selected by the best candidate selection. They are fully anti-correlated between D∗ and251
D samples. Below is detail of the correction method: we checked events in which both D∗252
and D candidates with additional slow π or γ are reconstructed. Usually, a D* candidate253
is selected in an event by the ROE and best candidate selection. When we apply slow π254
or γ correction, we assume that D∗ candidate is missed and D candidate is selected with255
the corrected weight probability.256
π0 efficiency corrections are applied to correctly reconstructed candidates, following257
the same way as the measurement of π0 efficiency performed by neutral group.258
4.2 Correction of branching ratios259
Values of the branching ratios of signal and background are different between the Belle II260
simulation and PDG. The differences are evaluated and corrections are applied to MC.261
18
```
4.2.1 Branching ratio of B → D(∗)ℓν262
```
```
Branching ratio of B → D(∗)ℓν decays in the Belle II simulation (decfiles/dec/DECAY BELLE2.DEC)263
```
are listed in Table 4.1. During WG review, the values are updated following PDG live264
```
and the latest BR(B → Dℓν) measurement by Belle II.265
```
```
Table 4.1: Branching ratio of B → D(∗)ℓν decays.
```
Decay MC PDG and BelleII
B0 → D∗+eν 0.0511 0.0487 ± 0.0009
B0 → D∗+µν 0.0511 0.0487 ± 0.0009
B0 → D+eν 0.0214 0.0206 ± 0.0005 ± 0.0010
B0 → D+µν 0.0214 0.0206 ± 0.0005 ± 0.0010
B− → D∗0eν 0.0549 0.0526 ± 0.0010
B− → D∗0µν 0.0549 0.0526 ± 0.0010
B− → D0eν 0.0231 0.0231 ± 0.0004 ± 0.0009
B− → D0µν 0.0231 0.0231 ± 0.0004 ± 0.0009
4.2.2 Branching ratio of τ → ℓνν266
Branching ratio of τ → ℓνν decays in the simulation and PDG 2025 are listed in Table 4.2.267
They are identical and no corrections are applied.268
Table 4.2: Branching ratio of τ leptonic decays.
Decay MC PDG
τ → eνν 0.178175 0.1782 ± 0.004
τ → µνν 0.173937 0.1739 ± 0.0004
4.2.3 Branching ratio of D∗269
Branching ratio of D∗ decays in the simulation and PDG 2025 are listed in Table 4.3.270
They are consistent and no corrections are applied.271
Table 4.3: Branching ratios of D∗decays.
Decay MC PDG
D∗+ → D0π+ 0.677 0.677 ± 0.005
D∗+ → D+π0 0.307 0.307 ± 0.005
D∗0 → D0π0 0.647 0.647 ± 0.009
D∗0 → D0γ 0.353 0.353 ± 0.009
19
4.2.4 Branching ratio of D272
The branching ratios of D on PDG are listed in Table3.2,3.3. We counted the number273
```
of produced D decays in B → D(∗)ℓν in generic MC sample by using MC generator274
```
information, and compared them with the expectations from PDG 2025 as shown in275
Table 4.4. The ratio is applied to MC as an event by event weight.276
```
Table 4.4: The number of simulated D decays in B → D(∗)ℓν MC and corrections of
```
branching ratios. 699f b−1 equivalent generic MC is used without FEI skim. Old values
were copied from the old version of note wrongly. They are fixed in v3.0.
```
D decays MC PDG Ratio(correction factor)
```
D0 → K−π+π0 7522524 7103608 1.0589
D0 → K−π+π−π+ 4775228 4059910 1.1762
D0 → K0S π+π−π0 1841432 1772545 1.0388
D0 → K−π+ 1929107 1948560 0.9900
D0 → K0S π+π− 946747 954449 0.9919
D0 → K0S π0 410943 422678 0.9722
D0 → K−K+ 199526 201263 0.9913
D+ → K−π+π+ 2054800 2098307 0.9792
D+ → K0S π+π0 1097158 1137685 0.9643
D+ → K−π+π+π0 1933500 1398125 1.3829
D+ → K0S π+π−π+ 421483 479185 0.8795
D+ → K0S π+ 235347 241448 0.9743
D+ → K−K+π+ 217910 216543 1.0063
D+ → K0S K+ 45927 46986 0.9774
4.2.5 Branching ratio of hadronic B decay277
We categorized the hadronic B decays, reconstructed as Bsig, based on MC generator278
information with GenMCTagTool [18], as shown in Fig. 4.1 and 4.2. We listed up the279
```
major hadronic B decays, by selecting the number of expected events more than 2(4)280
```
```
for B0(B+) as shown in Table 4.5. Most of the decay modes can be categorized to281
```
```
B → D(∗)D(∗), B → D(∗)D(∗)K, and B → D(∗)nπ(π0). Their branching ratios on PDG282
```
2025 are compared with decay file configuration used for the Belle II simulation. In the283
case that the measured branching ratios are listed on PDG, they are consistent with each284
other and no correction is applied. If the decays are not listed on PDG, no correction285
is applied and the values on Belle II simulation is used with 100% uncertainty. The286
treatment of uncertainty is explained in Sec. 7.287
4.2.6 Branching ratio of B → D∗∗ℓν decay288
```
The D∗∗ represents the D∗(0,+)0 (2400), D(0,+)1 (2420), D
```
```
′(0,+)
```
```
1 (2430), D
```
```
∗(0,+)
```
```
2 (2460) states,289
```
```
and the non-resonant contributions (D∗∗ → ηD(∗), πD(∗)). They are excited charm-meson290
```
cascade decays to D ground state. Table 4.6 shows the branching fractions of B → D∗∗ℓν291
decays. The values are taken from the HFLAV2023 and recommendation from WG1292
group. It is difficult to measure each decay mode independently, and a few branching293
20
1600 1620 1640 1660 1680 1700 1720 1740 1760 1780 1800
decay mode ID
0
20
40
60
80
100
ντD*
ντD
νD*l
νDl
D**
hadron
continuum
Other
MC is luminosity normalized
Figure 4.1: Decay mode ID of hadronic B− decays after event selection.
```
1681-1684,1725-1728: D(∗)(s) D(∗)
```
```
1685-1690: D(∗)s D(∗)1,2
```
```
1691-1700: D(∗)s Dnπ
```
```
1701-1724: D(∗)D(∗)K(∗)
```
1729-1748: D∗nπ
```
1764-1767,1773-1774:D(∗)s0,s1D∗
```
1800 1820 1840 1860 1880 1900 1920 1940 1960 1980 2000
decay mode ID
0
10
20
30
40
50
60 ντD*
ντD
νD*l
νDl
D**
hadron
continuum
Other
MC is luminosity normalized
Figure 4.2: Decay mode ID of hadronic B0 decays after event selection.
```
1829-1836: D(∗)(s) D(∗)
```
```
1837-1842: D(∗)s D(∗)1,2
```
```
1843-1852: D(∗)s Dnπ
```
```
1853-1876: D(∗)D(∗)K(∗)
```
1877-1893,1998: D∗nπ
```
1928-1931:D(∗)s0,s1D∗
```
1939-1940: D′s1D∗
1990: D∗pπ
21
Table 4.5: Branching ratios of hadronic B+ decays.
Decay decayModeID B in MC B in PDG[10−3] [10−3]
```
D(∗)D(∗)
```
B+ → D+s D 1681 9.0 9.3 ± 0.6
B+ → D+s D∗ 1682 8.2 7.0 ± 1.0
B+ → D∗s +D 1683 7.6 7.6 ± 1.6
B+ → D∗s +D∗ 1684 17.1 17.1 ± 2.4
B+ → D∗20D+s 1689 4.2 –
B+ → D∗20D∗+s 1690 4.0 –
B+ → D∗0D+ 1727 0.63 0.63 ± 0.17
B+ → D0D∗+s0 1764 7.6 –
B+ → D0D′+s1 1773 0.45 0.4 ± 0.1
B+ → D∗0D′+s1 1774 0.94 0.94 ± 0.42
B0 → D+s D− 1833 7.2 8.1 ± 0.6
B0 → D+s D∗− 1834 8.0 8.2 ± 0.8
B0 → D∗+s D− 1835 7.4 7.4 ± 1.6
B0 → D∗s +D∗− 1836 17.7 17.7 ± 1.4
B0 → D∗−2 D+s 1841 4.2 –
B0 → D∗−2 D∗+s 1842 4.0 –
B0 → D∗+s0 D− 1928 7.4 –
B0 → D∗+s0 D∗− 1929 17.7 –
B0 → D′+s1 D− 1939 0.43 0.43 ± 0.17
B0 → D′+s1 D∗− 1940 0.83 0.83 ± 0.28
```
D(∗)D(∗)K
```
B+ → D0D+K0 1701 1.55 1.55 ± 0.21
B+ → D0D∗+K0 1702 3.8 3.8 ± 0.4
B+ → D∗0D+K0 1703 2.1 2.1 ± 0.5
B+ → D∗0D∗+K0 1704 9.2 9.2 ± 1.2
B+ → D0D∗0K+ 1707 6.3 6.3 ± 0.5
B+ → D∗0D∗0K+ 1708 11.2 11.2 ± 1.3
B0 → D∗−D∗0K+ 1856 10.6 10.6 ± 0.9
B0 → D−D+K0 1857 0.75 0.75 ± 0.17
B0 → D∗−D+K0 1858 1.7 1.7 ± 0.1
B0 → D−D∗+K0 1859 4.8 4.8 ± 0.4
B0 → D∗−D∗+K0 1860 8.1 8.1 ± 0.7
B0 → D−D+K∗0 1869 2.5 –
B0 → D∗−D∗+K∗0 1872 5.0 –
```
D∗nπ(π0) etc.
```
B+ → D+s D0π0 1692 1.8 –
B+ → D∗+s D0π0 1694 1.8 –
B+ → D∗−π0π+π+ 1746 15 15± 7
B+ → ρ+D0 1731 13.4 9.7 ± 1.1
B+ → ρ+D∗0 1732 9.8 9.8 ± 1.7
B+ → D∗0a+1 1740 19 19 ± 5
B0 → D+s D−π0 1845 1.8 –
B0 → D∗+s D0π− 1846 3.7 –
B0 → D+s D−π0π0 1848 2.2 –
B0 → ρ+D− 1879 7.6 7.6 ± 1.2
B0 → ρ+D∗− 1880 6.8 6.8 ± 0.9
B0 → D∗−π+π0 1882 8.35 8.2 ± 0.5
B0 → a+1 D− 1886 6.0 6.0 ± 3.3
B0 → a+1 D∗− 1893 13.0 13.0 ± 0.27
B0 → D∗π+π+π−π0 1998 17.6 17.6 ± 2.7
B0 → D∗−p+n0 1990 1.5 –
22
ratios are estimated by subtraction of multiple measurements. Detail explanations are in294
[19] and https://xwiki.desy.de/xwiki/rest/p/ab7ff.295
Part of B → D∗∗ℓν decays in the generic MC is replaced with the background MC as296
shown in Table 4.7, in order to improve modeling of gap mode, which is the difference297
of the sum of exclusive and of inclusive B → Xℓν branching ratio measurements. In the298
generic MC, the decays are generated based on phase space with multi-body decays. On299
the other hand, in the background MC, they are simulated through D∗0 or D′1 resonances.300
Detail explanations are in https://xwiki.desy.de/xwiki/rest/p/ab7ff . The composition of301
```
gap mode is not understood well and large uncertainty is assigned for D∗∗ → ηD(∗) and302
```
```
D∗∗ → D(∗)ππ decay.303
```
4.3 Correction of form factors304
```
Table 4.8 shows the form factors used in the Belle II simulation for B → D(∗)τ ν, B →305
```
```
D(∗)ℓν, and B → D∗∗ℓν. The form factors and their correlations are updated based on the306
```
angular measurements of B → D∗ℓν listed in Table 4.9, by using a tool named Hammer307
[20].308
23
Table 4.6: Branching ratios of B → D∗∗ℓ−νℓ decays.
```
Decay BR in MC (×10−3) BR from HFLAV2023 (×10−3)
```
```
B0 → D∗0 +(→ Dππ)ℓ−νℓ – (8M events) (0.7 ± 0.8)/2
```
```
B0 → D′1+(→ Dππ)ℓ−νℓ – (8M events) (0.7 ± 0.8)/2
```
```
B0 → D∗0 +(→ D∗ππ)ℓ−νℓ – (8M events) (2.0 ± 1.0)/2
```
```
B0 → D′1+(→ D∗ππ)ℓ−νℓ – (8M events) (2.0 ± 1.0)/2
```
```
B0 → D∗0 +(→ Dη)ℓ−νℓ – (8M events) 8.8 ± 8.8
```
```
B0 → D′1+(→ D∗η)ℓ−νℓ – (8M events) 8.8 ± 8.8
```
B0 → D∗0π+ℓ−νℓ 0.92 0
B0 → D0π+ℓ−νℓ 0.92 0
B0 → D∗+π0ℓ−νℓ 0.46 0
B0 → D+π0ℓ−νℓ 0.46 0
B0 → D+1 ℓ−νℓ 7.04 5.9 ± 1.0
B0 → D∗+0 ℓ−νℓ 3.62 1.2 ± 1.8
B0 → D′+1 ℓ−νℓ 4.01 2.6 ± 0.4
B0 → D∗+2 ℓ−νℓ 3.47 2.99 ± 0.27
B0 → D+1 τ −ντ 1.3 0.59 ± 0.59
B0 → D∗+0 τ −ντ 1.3 0.96 ± 0.96
B0 → D′+1 τ −ντ 2.0 0.13 ± 0.13
B0 → D∗+2 τ −ντ 2.0 0.21 ± 0.21
```
B− → D∗0 0(→ Dππ)ℓ−νℓ – (8M events) (0.7 ± 0.9)/2
```
```
B− → D′10(→ Dππ)ℓ−νℓ – (8M events) (0.7 ± 0.9)/2
```
```
B− → D∗0 0(→ D∗ππ)ℓ−νℓ – (8M events) (2.2 ± 1.0)/2
```
```
B− → D′10(→ D∗ππ)ℓ−νℓ – (8M events) (2.2 ± 1.0)/2
```
```
B− → D∗0 0(→ Dη)ℓ−νℓ – (8M events) 9.2 ± 9.2
```
```
B− → D′10(→ D∗η)ℓ−νℓ – (8M events) 9.2 ± 9.2
```
B− → D∗0π0ℓ−νℓ 0.50 0
B− → D0π0ℓ−νℓ 0.50 0
B− → D∗+π−ℓ−νℓ 1.00 0
B− → D+π−ℓ−νℓ 1.00 0
B− → D∗+s K−ℓ−νℓ 0.30 0.29 ± 0.19
B− → D+s K−ℓ−νℓ 0.30 0.30 ± 0.13
B− → D01 ℓ−νℓ 7.57 6.4 ± 1.0
B− → D∗00 ℓ−νℓ 3.89 1.3 ± 1.9
B− → D′01 ℓ−νℓ 4.31 2.8 ± 0.4
B− → D∗02 ℓ−νℓ 3.73 3.21 ± 0.29
B− → D01 τ −ντ 1.3 0.64 ± 0.64
B− → D∗00 τ −ντ 1.3 0.10 ± 0.10
B− → D′01 τ −ντ 2.0 0.14 ± 0.14
B− → D∗02 τ −ντ 2.0 0.22 ± 0.22
24
Table 4.7: Simulated B → D∗∗ℓ−νℓ decays.
Event type Decay MC
```
1196700003 B0 → D∗0 +(→ Dππ)ℓ−νℓ background MC
```
```
1196700001 B0 → D′1+(→ Dππ)ℓ−νℓ background MC
```
```
1196700004 B0 → D∗0 +(→ D∗ππ)ℓ−νℓ background MC
```
```
1196700002 B0 → D′1+(→ D∗ππ)ℓ−νℓ background MC
```
```
1196708001 B0 → D∗0 +(→ Dη)ℓ−νℓ background MC
```
```
1196708000 B0 → D′1+(→ D∗η)ℓ−νℓ background MC
```
B0 → D∗0π+ℓ−νℓ generic MC
B0 → D0π+ℓ−νℓ generic MC
B0 → D∗+π0ℓ−νℓ generic MC
B0 → D+π0ℓ−νℓ generic MC
B0 → D+1 ℓ−νℓ generic MC
B0 → D∗+0 ℓ−νℓ generic MC
B0 → D′+1 ℓ−νℓ generic MC
B0 → D∗+2 ℓ−νℓ generic MC
B0 → D+1 τ −ντ generic MC
B0 → D∗+0 τ −ντ generic MC
B0 → D′+1 τ −ντ generic MC
B0 → D∗+2 τ −ντ generic MC
```
1296700003 B− → D∗0 0(→ Dππ)ℓ−νℓ background MC
```
```
1296700001 B− → D′10(→ Dππ)ℓ−νℓ background MC
```
```
1296700004 B− → D∗0 0(→ D∗ππ)ℓ−νℓ background MC
```
```
1296700002 B− → D′10(→ D∗ππ)ℓ−νℓ background MC
```
```
1296708001 B− → D∗0 0(→ Dη)ℓ−νℓ background MC
```
```
1296708000 B− → D′10(→ D∗η)ℓ−νℓ background MC
```
B− → D∗0π0ℓ−νℓ generic MC
B− → D0π0ℓ−νℓ generic MC
B− → D∗+π−ℓ−νℓ generic MC
B− → D+π−ℓ−νℓ generic MC
B− → D∗+s K−ℓ−νℓ generic MC
B− → D+s K−ℓ−νℓ generic MC
B− → D01 ℓ−νℓ generic MC
B− → D∗00 ℓ−νℓ generic MC
B− → D′01 ℓ−νℓ generic MC
B− → D∗02 ℓ−νℓ generic MC
B− → D01 τ −ντ generic MC
B− → D∗00 τ −ντ generic MC
B− → D′01 τ −ντ generic MC
B− → D∗02 τ −ντ generic MC
25
Table 4.8: Summary of form factor used in Belle II simulation
Decay configuration in dec file
B → D∗τ ν HQET3 0.912 1.205 1.15 1.404 0.854
B → Dτ ν HQET3 1.0541 1.128 1.0
B → D∗0 , D′1τ ν LLSW 0.68 -0.2 0.3
B → D1, D∗2 τ ν LLSW 0.71 -1.6 -0.5 2.9
B → D∗ℓν BGL 0.02596 -0.06049 0.01311 0.01713 0.00753 -0.09346
B → Dℓν BGL 0.0126 -0.094 0.34 -0.1 0.0115 -0.057 0.12 0.4
B → D∗0 , D′1ℓν LLSW 0.68 -0.2 0.3
B → D1, D∗2 ℓν LLSW 0.71 -1.6 -0.5 2.9
Table 4.9: Summary of paper used for form factor correction by Hammer
Decay model paper
```
B → D(∗)τ ν BLPRXP 2206.11281
```
```
B → D(∗)ℓν BLPRXP 2206.11281
```
B → D∗∗ℓν BLR 1711.03110, 1606.09300
B → D∗∗τ ν BLR 1711.03110, 1606.09300
26
5 Data/MC comparison in side-band309
The data-MC difference is studied with side-band regions, as summarized in Table 5.1.310
In the low q2 side-band, the normalization mode is enhanced which allows to validate the311
```
data-MC differences of the ECL energy sum in ROE (EECLextra) and Missing mass squared312
```
```
(M 2miss), which are used for signal extraction in Sec. 6. Because the final states of the313
```
normalization and signal modes are very similar, the validation is effective for the signal314
mode too. In addition, background yield and PDF shapes are studied in π0 veto side-band.315
```
PDF shapes of wrongly reconstructed D(∗) are studied in D(∗) mass sideband.316
```
Table 5.1: Summary of side-band regions
Side-band Selection Enhanced mode Check items
```
q2 side-band q2 < 3.5 (GeV/c)2 B → D∗ℓ−νℓ FEI efficiency
```
signal PDF shapes
π0 veto side-band Nπ0ROE > 0, B → D∗∗ℓ−νℓ, BG yield, PDF
EextraECL > 1.0 GeV, hadron
M 2miss > 2 GeV2
```
D(∗) mass side-band outside of Table 3.6 wrongly reconstructed D∗ PDF
```
5.1 q2 side-band317
5.1.1 Data yield and efficiency318
Although the absolute number of normalization mode and signal mode are canceled for319
```
R(D(∗)) measurement, we checked absolute data yield of normalization mode, in order to320
```
check how well it is modeled by MC. Table 5.2 shows the number of selected events in the321
q2 side-band. The data yield is consistent with MC expectation within a few percents.322
These are reasonable, because a few percent systematic errors are expected from FEI323
efficiency and other detector performances. Data yield of D∗+ → D+π0 is lower than324
MC expectation by about 2σ of statistical error, which can be statistical fluctuation.325
Figure 5.1–5.3 show the D mass and mass difference of D∗ and D. The data yield of326
D+ → Kπππ0, D0 → Kπππ, D0 → KK, D+ → KS ππ0 are about 20-30% different from327
```
MC (more than 2σ of statistical error). The difference is taken as systematic error in328
```
Sec. 7.329
Figure 5.4 shows decay mode ID of Btag. Although FEI efficiency is calibrated in each330
```
decay mode by using B → Xℓν and B → D(∗)π, the data yield does not agree with MC331
```
expectation in some decay modes. In order to cover these data/MC difference, systematic332
error is estimated in Sec. 7. Figure 5.5 shows lepton momentum in each decay mode. The333
data agree with MC within statistical error.334
27
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)0ππ->K0D020
```
4060
80100
120140
160180
200220 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=51.1/28
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)πππ->K0D0
```
50
100
150
200
250
300 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=42.3/17
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)0πππs->K0D0
```
510
1520
2530
35 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=11.7/11
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)π->K0D0
```
50
100
150
200
250
300 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=43.3/17
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)ππs->K0D0
```
20
40
60
80
100 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=17.8/8
```
1.76 1.78 1.8 1.82 1.84 1.86 1.88 1.9 1.92 1.94mass (GeV)0πs->K0D02
```
46
810
1214
1618
2022 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.76 1.78 1.8 1.82 1.84 1.86 1.88 1.9 1.92 1.945−4−3−
2− 1−01
2345pull
chi2/ndf=7.4/6
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9->KK mass (GeV)0D0
```
510
1520
2530
35 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=15.7/5
Figure 5.1: Invariant mass of D0 in each decay mode in the q2 sideband with all selections
including the mass selection.
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)ππ->K+D0
```
50
100
150
200
250
300 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=20.2/15
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)0ππs->K+D0
```
5
10
15
20
25 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=6.1/12
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)0πππ->K+D0
```
10
20
30
40
50 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=36.6/13
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)πππs->K+D0
```
510
1520
2530
35 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=10.0/5
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)πs->K+D0
```
510
1520
2530
35 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=2.4/5
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9mass (GeV)π->KK+D0
```
10
20
30
40
50data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=5.4/4
```
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.9K mass (GeV)s->K+D0
```
12
34
56
78
9 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is luminosity normalized
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.95−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
Figure 5.2: Invariant mass of D+ in each decay mode in the q2 sideband with all selections
including the mass selection.
28
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.15
```
) mass difference (GeV)π0->D*+D* and D (D
```
0
100
200
300
400
500
600
700 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.155−4−
3−2− 1−
012
345pull
chi2/ndf=17.7/12
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.15
```
) mass difference (GeV)0π+->D*+D* and D (D
```
0
5
10
15
20
25
30
35
40data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.155−4−
3−2− 1−
012
345pull
chi2/ndf=6.6/6
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.15
```
) mass difference (GeV)0π0->D*0D* and D (D
```
0
20
40
60
80
100
120
140
160 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0.136 0.138 0.14 0.142 0.144 0.146 0.148 0.155−4−
3−2− 1−
012
345pull
chi2/ndf=10.1/14
0.12 0.125 0.13 0.135 0.14 0.145 0.15 0.155 0.16
```
) mass difference (GeV)γ0->D*0D* and D (D
```
0
20
40
60
80
100
120
140 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0.12 0.125 0.13 0.135 0.14 0.145 0.15 0.155 0.165−4−
3−2− 1−
012
345pull
chi2/ndf=30.0/24
Figure 5.3: Mass differences of D∗ and D in each decay mode in the q2 sideband with all
selections including the mass selection.
Table 5.2: Data/MC comparison of the number of selected events in the q2 side-band.
The error shows statistical error of data. systematic error is not included in the error.
```
Category The number of selected events)
```
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
Data 1422 144 712 1481 5585 1988
Total MC 1432 170 707 1476 5443 1928
Data/MC ratio 0.993 0.848 1.007 1.004 1.026 1.032
```
(stat. error) ± 0.026 ± 0.071 ± 0.038 ± 0.026 ± 0.014 ± 0.023
```
29
0 5 10 15 20 25 30 35 40
Btag decay mode
0
100
200
300
400
500
600 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 5 10 15 20 25 30 35 400.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(a) B0tag
```
0 5 10 15 20 25 30 35 40
Btag decay mode
0
200
400
600
800
1000
1200
1400
1600
1800data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
0 5 10 15 20 25 30 35 400.80.85
0.90.95
11.05
1.11.15
1.2
data/MC ratio
```
(b) B+tag
```
Figure 5.4: Btag decay mode ID in the q2 side-band. Major decay modes are
```
B0 → D−π+(0), D−π+π0(1), D−π+π+π−(3), D−π+π+π−π0(4), D0π+π−(5), D∗−π+(15),
```
```
D∗−π+π0(16), D∗−π+π+π−(18), D∗−π+π+π−π0(19), Λ−c pπ+π−(26),
```
```
B+ → D0π+(0), D0π+π0 (1), D0π+π+π− (3), D0π+π+π−π0 (4), D∗0π+ (15), D∗0π+π0
```
```
(16), D∗0π+π+π− (18), D∗0π+π+π−π0 (19), D−π+π+ (23), D−π+π+π0 (24), Λ−c pπ+π−π+
```
```
(30).
```
```
0 0.5 1 1.5 2 2.5 3(GeV)ECLE0
```
100
200
300
400
500data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=13.0/8
```
(a) B0 → D∗+τ ν
```
```
0 0.5 1 1.5 2 2.5 3(GeV)ECLE020
```
4060
80100
120140
160180
200 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=5.7/8
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.5 1 1.5 2 2.5 3(GeV)ECLE0
```
50100
150200
250300
350400
450data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=1.8/8
```
(c) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.5 1 1.5 2 2.5 3(GeV)ECLE0
```
200400
600800
10001200
14001600 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=7.4/9
```
(d) B+ → D0τ ν
```
```
0 0.5 1 1.5 2 2.5 3(GeV)ECLE0
```
100
200
300
400
500
600 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=15.7/8
```
(e) B0 → D+τ ν
```
```
Figure 5.5: Distributions of the lepton momentum in each D(∗) decay mode in the q2
```
side-band with fine binning.
30
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100200
300400
500600
700 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=12.5/15
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1020
3040
5060
70 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=4.2/5
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
50100
150200
250300
350 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=9.2/11
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100
200
300
400
500
600 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=11.6/16
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0200
```
400600
8001000
12001400
16001800
20002200 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=33.6/23
```
(e) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100200
300400
500600
700800
900 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=16.5/17
```
(f) B0 → D+τ ν
```
```
Figure 5.6: Distributions of the EECLextra in each D(∗) decay mode in the q2 side-band. The
```
data agree with MC within statistical error.
5.1.2 EECLextra PDF shape335
Figure 5.6 shows the EECLextra distribution. In order to compare shape, MC is area normal-336
ized. The data agree with MC within statistical error.337
5.1.3 M 2miss PDF shape338
Figure 5.7 shows the M 2miss distribution. In order to compare shape, MC is area normal-339
ized. The data agree with MC within statistical error. A coarse binning is chosen because340
the same binning is used for the fitting.341
Figure 5.8 shows the same distribution with fine binning. Small discrepancies in peak342
widths are observed between data and MC simulations. We apply a MC correction to343
cover this difference as follows. To evaluate the M 2miss width, the M 2miss distributions in344
data and MC are fitted by combinations of Gaussian and Crystal Ball functions, as shown345
in Table 5.3. When data is fitted, shape parameters of these functions are determined346
from MC, with a floating normalization parameter and a single floating shape parameter347
```
(Rres) which scales all of the sigma of Gaussians commonly. Table 5.4 shows the fitted348
```
```
Rres and a weighted average of fitted Gaussians’s sigma in MC (σMC). Due to the limited349
```
statistics of the D∗+ → D+π0 decay channel, it is combined with the D∗+ → D0π+350
channel. In order to correct the M 2miss of MC to data, the M 2miss of MC is smeared in each351
event by352
```
M 2miss = M 2miss + Gauss(0, ∆σ) (5.1)353
```
where Gauss is a random number generated by Gaussian with mean of 0 and width of354
∆σ = σMC
p
```
(R2res − 1). The uncertainty of the fit is taken into account as systematic355
```
error as described in Sec. 7.356
31
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
200
400
600
800
1000 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=4.4/4
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
20
40
60
80
100data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/2
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100
200
300
400
500 data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is luminosity normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=3.3/3
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100200
300400
500600
700800
900 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=7.7/7
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
5001000
15002000
25003000
3500 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=8.6/7
```
(e) B+ → D0τ ν
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 30sžºÿ•0
200400
600800
1000
1200dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=5.6/6
```
(f) B0 → D+τ ν
```
```
Figure 5.7: Distributions of the M 2miss in each D(∗) decay mode in the q2 side-band. The
```
data agree with MC within statistical error.
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100200
300400
500600
700800dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=19.1/9
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
1020
3040
5060
70 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=0.1/2
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
50100
150200
250300
350 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=5.3/6
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100
200
300
400
500 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=21.7/19
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
200400
600800
10001200
14001600
18002000 dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=39.2/25
```
(e) B+ → D0τ ν
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100200
300400
500600
700800
900 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=38.9/16
```
(f) B0 → D+τ ν
```
```
Figure 5.8: Distributions of the M 2miss in each D(∗) decay mode in the q2 side-band with
```
fine binning.
32
Table 5.3: Modeling functions on M 2miss
D decay signal background
D∗+ triple gaussian double gaussian + crystall ball
D∗0 → D0π0 triple gaussian double gaussian + crystall ball
D∗0 → D0γ triple gaussian triple gaussian
D0 triple gaussian double gaussian + crystall ball
D+ triple gaussian double gaussian + crystall ball
Table 5.4: Resolution and smearing factors in the M 2miss distributions in the q2 side-band
region
```
D decay Rres σMC(GeV2) ∆σ (GeV2)
```
D∗+ 1.132±0.009 0.0750±0.0011 0.0398±0.0037
D∗0 → D0π0 1.039±0.003 0.0883±0.0025 0.0249±0.0129
D∗0 → D0γ 1.076±0.006 0.1187±0.0018 0.0472±0.0070
D0 1.083±0.007 0.0960±0.0026 0.0399±0.0098
D+ 1.144±0.008 0.0811±0.0023 0.0450±0.0070
```
5.1.4 Fraction of correctly reconstructed D(∗)357
```
Figure 5.9-5.10 show EECLextra and M 2miss distributions, categorized by correctly and incor-358
```
rectly D(∗) distribution. Their PDF shape is different at low EECLextra region mainly. These359
```
distribution will be used to estimate a fraction of correctly reconstructed D∗ candidates360
in Sec. 7.361
33
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100200
300400
500600
700data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=12.5/15
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1020
3040
5060
70data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=4.2/5
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
50100
150200
250300
350 data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=9.2/11
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100
200
300
400
500
600data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=11.6/16
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0200
```
400600
8001000
12001400
16001800
20002200data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=33.6/23
```
(e) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100200
300400
500600
700800
900data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=16.5/17
```
(f) B0 → D+τ ν
```
```
Figure 5.9: Distributions of the EECLextra in each D(∗) decay mode in the q2 side-band. MC
```
```
is categorized by correctly and incorrectly reconstructed D(∗).
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
200
400
600
800
1000data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=4.4/4
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
20
40
60
80
100
data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/2
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100
200
300
400
500
data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is luminosity normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=3.9/3
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
100200
300400
500600
700800
900data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=7.7/7
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3)2(GeV2missM0
```
5001000
15002000
25003000
3500data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=8.6/7
```
(e) B+ → D0τ ν
```
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 3À7ìý•0
200400
600800
1000
1200 data
```
D(*) isSignal==1
```
```
D(*) isSignal!=1
```
MC is area normalized
2− 1.5− 1− 0.5− 0 0.5 1 1.5 2 2.5 35−4−3−
2− 1−01
2345pull
chi2/ndf=5.6/6
```
(f) B0 → D+τ ν
```
```
Figure 5.10: Distributions of the M 2miss in each D(∗) decay mode in the q2 side-band. MC
```
```
is categorized by correctly and incorrectly reconstructed D(∗).
```
34
Table 5.5: Data/MC comparison of the number of selected events in the π0 veto side-
band. The error shows statistical error of data.
Category The number of selected events
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
Data 85 24 49 397 1421 764
```
(± stat.) ± 9 ± 5 ± 7 ± 20 ± 38 ± 28
```
MC B → D∗∗ℓν, gap mode 22 3.1 19 79 354 131
MC hadronic B decay, unmeasured BR 28 11 17 90 287 293
MC B → D∗∗ℓν, non-gap mode 13 1.4 9.9 34 191 78
MC hadronic B decay, measured BR 34 11 31 124 420 215
MC continuum 5.5 3.6 5.5 67 348 199
```
MC others, B → D(∗)ℓν 10.4 1.5 4.4 15 118 30
```
MC Total 116 31.7 86.9 408.8 1718 946
```
(± 100% error of unmeasured BR) ± 22 ± 28 ± 3.1 ± 11 ± 19 ± 17 ± 79 ± 90 ± 354 ± 287 ± 131 ± 293
```
```
Data/MC (stat.) 0.75 ± 0.08 0.76 ± 0.15 0.56 ± 0.08 0.97 ± 0.05 0.83 ± 0.02 0.81 ± 0.03
```
```
(± 100% error of unmeasured BR) ± 0.17 ± 0.25 ± 0.09 ± 0.44 ± 0.15 ± 0.15 ± 0.24 ± 0.28 ± 0.22 ± 0.17 ± 0.13 ± 0.36
```
5.2 π0 veto side-band362
Table 5.5 shows the number of selected events in the π0 veto side-band. The data yield is363
10-40% smaller than MC expectation in each sample. In order to investigate this issue,364
new MC category of ”un-measured hadronic B decay” and ”D∗∗ℓν gap mode”, where their365
branching ratios are not measured so far on PDG, are added to the table. Because their366
```
branching ratio uncertainty is large (±100%), the MC expectation has large uncertainty367
```
and it covers the data/MC difference. Then, systematic uncertainties from their branching368
ratios is estimated in Sec. 7, and no additional systematic uncertainties are added. The369
```
other analysis of B → D(∗)ℓν [21] reported the similar observation at their control region:370
```
the data suggest a configuration with a substantially smaller fraction of gap modes.371
Figure 5.11 and 5.12 show the EECLextra and M 2miss distributions. The data agree with MC372
within statistical error and the branching ratio error. Then we do not apply additional373
corrections and systematics by using this side-band. The distribution suggests a configu-374
ration with a substantially smaller fraction of gap modes too. In order to constrain gap375
mode from data, gap mode is independently categorized from other D∗∗ℓν and floated for376
the fitting, as described in Sec. 6.377
35
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
5
10
15
20
25data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
12
34
56
78data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
24
68
1012
1416
18
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1020
3040
5060
7080dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
50
100
150
200
250
300data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(e) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
2040
6080
100120
140160data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 20.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(f) B0 → D+τ ν
```
```
Figure 5.11: Distributions of the EECLextra in each D(∗) decay mode in the π0 veto side-band.
```
The ”D∗∗ gap” and ”hadron unmeasued BR” have about 100% error of their branching
ratio.
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
5
10
15
20
25
30data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
1
2
3
4
5
6
7
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM02
```
46
810
1214
1618
2022data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
1020
3040
5060
7080dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
50
100
150
200
250
300
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(e) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
2040
6080
100120
140
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 100.80.850.9
0.9511.05
1.11.151.2
data/MC ratio
```
(f) B0 → D+τ ν
```
```
Figure 5.12: Distributions of the M 2miss in each D(∗) decay mode in the π0 veto side-band.
```
The ”D∗∗ gap” and ”hadron unmeasued BR” have about 100% error of their branching
ratio.
36
```
Table 5.6: Data/MC comparison of the number of selected events in the D(∗) mass side-
```
band with M 2miss > 2GeV2 and EROEextra > 1 GeV. The error shows statistical error of data.
Systematic error is not included in the error.
Category The number of selected events
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
Data 6 2 15 89 58 68
```
(± stat.) ± 2 ± 1 ± 4 ± 9 ± 8 ± 8
```
MC B → D∗∗ℓν, gap mode 0.3 0.7 4.2 32 6.0 6.6
MC hadronic B decay, unmeasured BR 0.9 1.7 2.2 14 7.0 19
MC B → D∗∗ℓν, non-gap mode 0.6 0.5 1.6 9.9 4.6 4.7
MC hadronic B decay, measured BR 0.9 1.2 4.6 23 8.4 15
MC continuum 0 1.5 3.6 18 18 13
```
MC others, B → D(∗)ℓν 0 0.3 3.6 19 7.9 4.7
```
MC Total 2.7 5.9 19.8 117 51.5 63.3
```
Data/MC (stat.) 2.3 ± 0.92 0.34 ± 0.24 0.76 ± 0.20 0.76 ± 0.08 1.13 ± 0.15 1.07 ± 0.13
```
```
Table 5.7: Data/MC comparison of the number of selected events in the D(∗) mass side-
```
band with M 2miss < 1GeV2. The error shows statistical error of data. Systematic error is
not included in the error.
```
Category The number of selected events)
```
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
Data 48 46 206 1953 383 305
Total MC 44.0 42.2 237 1836 387 289
Data/MC ratio 1.09 1.09 0.870 1.06 0.99 1.06
```
(stat. error) ± 0.16 ± 0.16 ± 0.06 ± 0.02 ± 0.05 ± 0.06
```
```
5.3 D(∗) mass sideband378
```
```
In order to check PDF shape of wrongly reconstructed D(∗), events outside of D(∗) mass379
```
```
window (D(∗) mass sideband) are used. The sideband is separated into two regions: one380
```
requires M 2miss > 2GeV2 and EROEextra > 1 GeV to enhance background, another requires381
M 2miss < 1GeV2 to enhance normalization mode. Table 5.6, Figure 5.13-5.14 show the382
EROEextra and M 2miss distributions in the background enhanced region. The same tendency383
is seen as the π0 veto side-band and data suggest a configuration with a substantially384
smaller fraction of gap modes. Table 5.7, Figure 5.15-5.16 show the EROEextra and M 2miss in385
the signal enhanced region. The same tendency is seen in the q2 sideband and data/MC386
agrees within their errors.387
37
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
0.5
1
1.5
2
2.5data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
0.20.4
0.60.8
11.2
1.4
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1
2
3
4
5
6
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
5
10
15
20
25
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=11.4/5
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
24
68
1012
14data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(e) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE02
```
46
810
1214
1618
20
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=2.1/1
```
(f) B0 → D+τ ν
```
```
Figure 5.13: Distributions of the EECLextra in each D(∗) decay mode in the D(∗) mass side-
```
band with M 2miss > 2 GeV2, EROEextra > 1 GeV.
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
0.5
1
1.5
2
2.5data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
0.20.4
0.60.8
11.2
1.41.6data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
1
2
3
4
5data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
5
10
15
20
25
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=8.9/6
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
2
4
6
8
10
12
14
dataD** gap
hadron unknown BRD** non-gap
hadron known BRcontinuum
ν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(e) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
24
68
1012
1416
18data
D** gaphadron unknown BR
D** non-gaphadron known BR
continuumν, DlνOther, D*l
MC is luminosity normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.0/0
```
(f) B0 → D+τ ν
```
```
Figure 5.14: Distributions of the M 2miss in each D(∗) decay mode in the D(∗) mass side-
```
band with M 2miss > 2 GeV2, EROEextra > 1 GeV.
38
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
5
10
15
20
25dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.7/1
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
5
10
15
20
25 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=0.6/1
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1020
3040
5060
7080
90 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=2.8/6
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
100200
300400
500600
700 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=10.9/11
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
20
40
60
80
100
120 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=5.3/8
```
(e) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)ECLextraE0
```
1020
3040
5060
7080
90data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−3−
2− 1−01
2345pull
chi2/ndf=3.1/8
```
(f) B0 → D+τ ν
```
```
Figure 5.15: Distributions of the EECLextra in each D(∗) decay mode in the D(∗) mass side-
```
band with M 2miss < 1 GeV2.
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
510
1520
2530
35 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.4/2
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
5
10
15
20
25
30
35data
ντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=4.2/2
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
2040
6080
100120
140 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=4.3/4
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
200
400
600
800
1000dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=8.4/5
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
2− 0 2 4 6 8 10)2(GeV2missM020
```
4060
80100
120140
160180
200220
240 dataντD*
ντDνD*l
νDlD**
hadroncontinuum
Other
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=0.3/4
```
(e) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2(GeV2missM0
```
2040
6080
100120
140160
180200dataντD*ντD
νD*lνDl
D**hadron
continuumOther
MC is area normalized
2− 0 2 4 6 8 105−4−3−
2− 1−01
2345pull
chi2/ndf=2.8/4
```
(f) B0 → D+τ ν
```
```
Figure 5.16: Distributions of the M 2miss in each D(∗) decay mode in the D(∗) mass side-
```
band with M 2miss < 1 GeV2.
39
6 Signal extraction388
6.1 Sample and PDF category389
```
R(D∗) and R(D) are extracted through a two-dimensional extended binned maximum390
```
```
likelihood fit. The two-dimensional probability density functions (PDFs) are constructed391
```
independently in each of five fit samples:392
• B0sig → D∗−ℓ+, where ℓ = e or µ, D∗− → D0π− or D∗− → D−π0393
394
• B+sig → ¯D∗0ℓ+, where ℓ = e or µ, D∗0 → D0π0395
• B+sig → ¯D∗0ℓ+, where ℓ = e or µ, D∗0 → D0γ396
397
• B0sig → D−ℓ+, where ℓ = e or µ398
399
• B+sig → ¯D0ℓ+, where ℓ = e or µ.400
The latter three samples are newly added in this analysis. The D∗− → D0π− and D∗− →401
D−π0 are combined due to low statistics of the D∗− → D−π0. A simultaneous fit is402
performed across the five samples. The variables used in the fit are EECLextra and M 2miss.403
Their binnings are:404
• EECLextra:405
[0.00,0.05,0.10,0.20,0.3,0.4,0.6,0.8,1.0,2.0] GeV406
• M 2miss:407
[-2,-0.5,0.0,0.5,1.0,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0,10.0] GeV 2.408
The number of bins in each sample is 9×13 = 117. The binnings are optimized to improve409
```
R(D(∗)) sensitivity, while keeping small, less than 2%, fitter bias from MC statistics410
```
uncertainty. The binning is updated again in version 2.8 of the note, because MC statistics411
error is increased by separating gap mode template from D∗∗ modes. Narrow bin width412
are set around the peak of signal mode, and coarse bin width are set low statistic region.413
In each sample, nine PDF categories are used:414
• B → D∗τ ν415
• B → Dτ ν416
• B → D∗ℓν417
• B → Dℓν418
• D∗∗ℓν gap mode419
• B → D∗∗τ, ℓν420
• Hadronic B decay421
• Continuum422
40
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDstTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDstTv
```
(a) B → D∗τ ν
```
SignalDTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDTv
```
(b) B → Dτ ν
```
00.02
0.040.06
0.080.1
0.120.14
0.160.18
```
0.2)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDstlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDstlv
```
(c) B → D∗ℓν
```
0
0.05
0.1
0.15
0.2
```
0.25 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDlv
```
(d) B → Dℓν
```
0
0.01
0.02
0.03
0.04
```
0.05 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststgap
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststgap
```
(e) B → D∗∗ℓν gap mode
```
0
0.01
0.02
0.03
0.04
```
0.05 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststlv
```
(f) B → D∗∗ℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
HadB
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
HadB
```
(g) hadronic B decay
```
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Continuum
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Continuum
```
(h) Continuum
```
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
```
0.8)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
OtherBG
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
OtherBG
```
(i) Other
```
Figure 6.1: PDF of each category in B0 → D∗−ℓ+ sample. z-axis is probability.
• Other423
they are categorized based on the generated decay mode id, obtained from GenMCTag-424
Tool. ”isSignal” and any MCmatching information are not used for the categorization.425
Figure 6.1 and 1.1–1.4 in appendix A show the two dimensional PDF in each sample426
and category. The B → D∗τ ν and B → Dτ ν signals are peaked at low EECL and high427
M 2miss in D∗ and D samples. The D∗ samples are sensitive to the B → D∗τ ν. The D428
samples are sensitive to sum of B → Dτ ν and B → D∗τ ν, because there is no large429
PDF difference between them. The normalization modes of B → D∗ℓν and B → Dℓν430
are peaked at low EECL and low M 2miss with large yield and high purity. The other431
backgrounds of D∗∗, hadronic B decays, continuum are distributed at high EECL and432
high M 2miss regions. Amount of other backgrounds are small and negligible.433
41
Table 6.1: Parameters used for the fit
parameters floated/fixed note
```
R(D∗) floated one parameter, common for all samples
```
```
R(D) floated one parameter, common for all samples
```
```
BR(B → D∗ℓν) floated one parameter, common for all samples
```
```
BR(B → Dℓν) floated one parameter, common for all samples
```
```
N (B → D∗∗τ, ℓν) floated independent five parameters in five samples
```
```
N (gap mode) floated independent five parameters in five samples
```
```
N (hadronic B ) floated independent five parameters in five samples
```
```
N (continuum) fixed independent five parameters in five samples
```
```
N (other) fixed independent five parameters in five samples
```
εD∗τ ν fixed independent five parameters in five samples
εDτ ν fixed independent five parameters in five samples
εD∗ℓν fixed independent five parameters in five samples
εDℓν fixed independent five parameters in five samples
f00 floated one parameter, common for all samples
f+− floated one parameter, common for all samples
NBB floated one parameter, common for all samples
6.2 Fit parameter434
```
Table 6.1 summarizes parameters used for the fit. R(D∗) is described using the number435
```
of reconstructed signal and normalization events and reconstruction efficiencies,436
```
R(D(∗)) =
```
```
B(B → D(∗)τ −ν)
```
```
B(B → D(∗)ℓ−ν)
```
```
, (ℓ = e, µ) (6.1)437
```
=
```
ND(∗)τ ν
```
```
(ND(∗)ℓν /2)
```
·
```
εD(∗)ℓν
```
```
εD(∗)τ ν
```
```
, (6.2)438
```
```
where ND(∗)τ (ℓ)ν is the observed number of B → D(∗)τ −ντ (D(∗)ℓ−νℓ) candidates in the439
```
```
data and εD(∗)τ (ℓ)ν is reconstruction efficiency of reconstructed B → D(∗)τ −ντ (D(∗)ℓ−νℓ)440
```
candidates. The factor 2 in the denominator averages the summed yield from two light441
```
leptons, ℓ ∈ {e, µ}. Here, the reconstruction efficiencies are defined as follows,442
```
```
εD(∗)τ (ℓ)ν =
```
```
N recD(∗)τ (ℓ)ν
```
```
N genD(∗)τ (ℓ)ν
```
```
, (6.3)443
```
```
where N recD(∗)τ (ℓ)ν and N genD(∗)τ (ℓ)ν are the number of reconstructed and generated B →444
```
```
D(∗)τ −ντ (D(∗)ℓ−νℓ) decays, respectively. N genD(∗)τ (ℓ)ν is derived by Eq. (6.4) and Eq. (6.5),445
```
```
N genD(∗)τ ν = N genBB · 2B(B → D(∗)τ −νtau)gen (6.4)446
```
```
N genD(∗)ℓν = N genBB · 2
```

```
B(B → D(∗)e−νe)gen + B(B → D(∗)µ−νµ)gen
```

```
. (6.5)447
```
```
Here N genBB is the number of BB pairs generated in the simulation, and B(B → X)gen448
```
refers to a simulated branching fraction for B → X decay. The number of generated449
```
B → D(∗)ℓ−νℓ decays is twice the individual counts from one of the BB pair, which is450
```
```
represented by the factor of 2 in Eq. (6.5). We assume R(D(∗)) holds a consistent value451
```
42
Table 6.2: The fixed or constrained input parameters for the fitting.
Parameter Values
f00 0.4861 ± 0.0080
f+− 0.5113 ± 0.0108
NBB [106] 387.1 ± 5.6
D∗+ D∗0 → D0π0 D∗0 → D0γ D0 D+
εD∗τ ν [10−5] 1.208 0.623 1.034 3.691 0.616
εDτ ν [10−5] 0 0.028 0.430 4.766 2.018
εD∗ℓν [10−5] 3.408 1.666 3.054 12.506 1.910
εDℓν [10−5] 0.011 0.020 0.644 8.647 3.677
```
between B0 and B+ decays under the isospin symmetry, setting R(D(∗)) = R(D(∗)+) =452
```
```
R(D(∗)0). All five samples take the common value during the fit for the signal extraction.453
```
```
Furthermore, B(B0 → D(∗)+ℓ−νℓ) is required to be the same in all five samples. The454
```
efficiencies and the number of BB pairs are estimated from MC and fixed in the fit, as455
shown in Table 6.2. Effect from their uncertainties are evaluated as systematic errors.456
The number of reconstructed backgrounds, B → D∗∗τ, ℓν and hadronic B decays, are457
```
floated independently in each D(∗) mode. The number of continuum and other back-458
```
grounds are fixed in the fit and their fluctuation is estimated as systematic error in Sec. 7.459
Therefore, the fit involves a total of 21 floated parameters.460
Systematic parameters are not included in the fit, and nominal PDF and input values461
are used to determine the best fit point. Effect from their uncertainties are evaluated as462
systematic error by using toy ensemble and re-fitting method as described in Sec. 7.463
6.3 Likelihood function464
```
We perform an extended binned maximum likelihood. The likelihood(L) is defined as465
```
L

⃗n⃗ λ

≡
NsampleY
```
i=1
```
NbinY
```
j=1
```

```
(Pij )nij
```
nij !
· e−Pij

```
, (6.6)466
```
where nij represents the observed number of events in the j-th bin for the i-th sample, and467
⃗n represents the collection of these observed counts.⃗ λ consists of 16 fit parameters floated468
```
in the fit, which includes R(D(∗)). The indices i and j run fit samples and bins in two469
```
dimensions, up to Nsample = 5 and Nbin = 260, respectively. The PDF Pij is constructed470
as a sum of the PDF components from nine categories:471
Pij

⃗λ

=
NcategoryX
```
k=1
```
h
νki

⃗λ

f kij
i
```
. (6.7)472
```
Here, νki is the expected yield of the k-th category in the i-th sample, and f kij corresponds473
to the PDF component in the j-th bin for this candidate category. Empty bins, where474
the expected number of MC events is zero, are removed from likelihood calculation.475
43
6.4 Asimov fit sensitivity476
```
Fit is performed to Asimov data assuming R(D∗) = 0.254 and R(D) = 0.300. When477
```
```
Asimov data is generated, the branching ratios of B → D(∗)ℓν is fixed following Table 4.1,478
```
```
and branching ratios of B → D(∗)τ ν is weighted following the R(D(∗)) assumptions. The479
```
fit results are480
```
R(D∗) = 0.254 ± 0.022(stat.), (6.8)481
```
```
R(D) = 0.300 ± 0.051(stat.), (6.9)482
```
```
ρ = −0.42(stat.). (6.10)483
```
Figure 6.2–6.5 show the projection of the fitted distributions.484
6.5 Fitter validation485
Fitter performance is validated by using toy ensemble. 1000 set of toy is generated by486
```
fluctuating statistic in each bin assuming Poisson distribution. R(D(∗)) is fixed to 0.254487
```
and 0.300 in this study. They are fitted and their pull is estimated as shown in Fig. 6.6-488
6.10. They are consistent with Gaussian of mean 0, sigma 1. In Figure 6.9, the pull489
```
of N (gap) differs from 1 about 3σ in D0 mode. This is newly found after separating490
```
gap mode templates from others. The reason is not clearly understood, but one possible491
explanation is that the templates are similar between gap mode and hadronic B decay in492
the D0 mode, as shown in Fig. 1.3. The deviation of the pull is small, 2.3%, and impact493
```
to R(D(∗)) is negligible.494
```
```
In addition, linearity test is performed by varying R(D∗) = 0.1 − 0.4 and R(D) =495
```
```
0.1 − 0.5 with 0.003 and 0.004 intervals. Depending on value of R(D∗) and R(D), small496
```
fitter bias is seen, as shown in Fig. 6.11. This will be taken into systematic error in Sec. 7.497
44
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
```
700)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
1000
2000
3000
4000
5000
```
6000)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 6.2: Asimov fit projection to the M 2miss in each sample. Data point shows Asimov
```
data assuming R(D∗) = 0.254 and R(D) = 0.300.
```
45
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
180)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
10
20
30
40
50
60
70
```
80)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
```
160)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
```
700)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
```
160)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 6.3: Asimov fit projection to the M 2miss in each sample. Data point shows Asimov
```
data assuming R(D∗) = 0.254 and R(D) = 0.300. y axis is zoomed.
```
46
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
200
400
600
800
1000
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
800
900
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
500
1000
1500
2000
2500
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 6.4: Asimov fit projection to the EECLextra in each sample. Data point shows Asimov
```
data assuming R(D∗) = 0.254 and R(D) = 0.300.
```
47
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
5
10
15
20
25
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
20
40
60
80
100
120
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
5
10
15
20
25
30
35
40
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
```
Figure 6.5: Asimov fit projection to the EECLextra at 1.5 GeV 2 < M 2miss (3.0 GeV 2 < M 2miss) for
```
```
D∗(D) sample in each sample. Data point shows Asimov data assuming R(D∗) = 0.254
```
```
and R(D) = 0.300.
```
48
```
5− 4− 3− 2− 1− 0 1 2 3 4 5error)/R(D*)nominalpull=(R(D*)-R(D*)0
```
50
100
150
200
250
300
350
400
/ ndf2χ 78.15 / 69
Constant 4.8±391.7Mean 0.0102±0.0244−
Sigma 0.007±1.011
```
5− 4− 3− 2− 1− 0 1 2 3 4 5error)/R(D)nominalpull=(R(D)-R(D)0
```
50
100
150
200
250
300
350
400
/ ndf2χ 88.04 / 68
Constant 4.9±397.8Mean 0.010103±0.002035−
Sigma 0.0072±0.9948
```
Figure 6.6: Pull of R(D∗) (left) and R(D) (right) with 10000 toys. Only statistical error
```
is fluctuated and other parameters are fixed for toy generation. f00 and NBB are fixed for
the fitting.
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(D**lv) D* sample/ ndf2χ 60.57 / 69
```
Constant 4.8±395Mean 0.010117±0.003132−
Sigma 0.007±1.005
```
N(D**lv) D* sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
0 D0 sampleπN(D**lv) D*0 ->/ ndf2χ 59.6 / 70
```
Constant 4.9±400Mean 0.009980±0.008684−
Sigma 0.0071±0.9918
```
0 D0 sampleπN(D**lv) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
450D0 sampleγN(D**lv) D*0 ->/ ndf2χ 77.37 / 68Constant 4.9±402.1
```
Mean 0.009939±0.004324Sigma 0.0068±0.9852
```
D0 sampleγN(D**lv) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(D**lv) D0 sample/ ndf2χ 62.74 / 73
```
Constant 4.9±397.5Mean 0.0100±0.0122−
Sigma 0.0070±0.9976
```
N(D**lv) D0 sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(D**lv) D+ sample/ ndf2χ 52.95 / 66
```
Constant 4.9±401.5Mean 0.00997±0.02872−
Sigma 0.007±0.989
```
N(D**lv) D+ sample
```
```
Figure 6.7: Pull of nuisance parameters, N (B → D∗∗ℓν), with 10000 toys. Only statistical
```
error is fluctuated and other parameters are fixed for toy generation. f00 and NBB are
fixed for the fitting.
49
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
450
```
N(hadron) D* sample/ ndf2χ 118.9 / 73
```
Constant 4.8±396.3Mean 0.01015±0.02007−
Sigma 0.0069±0.9951
```
N(hadron) D* sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
0 D0 sampleπN(hadron) D*0 ->/ ndf2χ 120.2 / 77
```
Constant 5.0±392.9Mean 0.0103±0.0105−
Sigma 0.008±1.004
```
0 D0 sampleπN(hadron) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
D0 sampleγN(hadron) D*0 ->/ ndf2χ 48.56 / 68
```
Constant 5.0±397.4Mean 0.0101±0.0312−
Sigma 0.0±1
```
D0 sampleγN(hadron) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(hadron) D0 sample/ ndf2χ 51.72 / 70
```
Constant 4.9±400.8Mean 0.00997±0.01222−
Sigma 0.0070±0.9908
```
N(hadron) D0 sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
450
```
N(hadron) D+ sample/ ndf2χ 75.79 / 68
```
Constant 4.9±400.6Mean 0.0100±0.0151−
Sigma 0.0072±0.9889
```
N(hadron) D+ sample
```
```
Figure 6.8: Pull of nuisance parameters, N (hadron), with 10000 toys. Only statistical
```
error is fluctuated and other parameters are fixed for toy generation. f00 and NBB are
fixed for the fitting.
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(gap) D* sample/ ndf2χ 63.83 / 70
```
Constant 4.9±401Mean 0.009944±0.003084−
Sigma 0.007±0.989
```
N(gap) D* sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
0 D0 sampleπN(gap) D*0 ->/ ndf2χ 107.2 / 75
```
Constant 4.9±398.3Mean 0.0101±0.0253−
Sigma 0.007±0.991
```
0 D0 sampleπN(gap) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
D0 sampleγN(gap) D*0 ->/ ndf2χ 77.2 / 70
```
Constant 4.9±400Mean 0.0100±0.0132
Sigma 0.0069±0.9901
```
D0 sampleγN(gap) D*0 ->
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(gap) D0 sample/ ndf2χ 60.35 / 73
```
Constant 4.9±399.7Mean 0.00997±0.01378
Sigma 0.0069±0.9923
```
N(gap) D0 sample
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
N(gap) D+ sample/ ndf2χ 93.53 / 74
```
Constant 4.9±400.2Mean 0.00995±0.01563
Sigma 0.0069±0.9878
```
N(gap) D+ sample
```
```
Figure 6.9: Pull of nuisance parameters, N (gap), with 10000 toys. Only statistical error
```
is fluctuated and other parameters are fixed for toy generation. f00 and NBB are fixed for
the fitting.
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
BR(B->D*lv)/ ndf2χ 70.28 / 69
```
Constant 4.9±398.4Mean 0.010009±0.004606
Sigma 0.0069±0.9946
```
BR(B->D*lv)
```
5− 4− 3− 2− 1− 0 1 2 3 4 5pull0
50100
150200
250300
350400
```
BR(B->Dlv)/ ndf2χ 67.93 / 67
```
Constant 4.9±395.8Mean 0.01011±0.01288−
Sigma 0.007±1.002
```
BR(B->Dlv)
```
```
Figure 6.10: Pull of nuisance parameters, BR(B → D(∗)ℓν), with 10000 toys. Only
```
statistical error is fluctuated and other parameters are fixed for toy generation. f00 and
NBB are fixed for the fitting.
50
0.01−
0.008−
0.006−
0.004−
0.002−
0
0.002
0.004
0.006
0.008
0.01
```
0.1 0.15 0.2 0.25 0.3 0.35 0.4input R(D*)0.1
```
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
```
input R(D)
```
0.01−
0.008−
0.006−
0.004−
0.002−
0
0.002
0.004
0.006
0.008
0.01
```
0.1 0.15 0.2 0.25 0.3 0.35 0.4input R(D*)0.1
```
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
```
input R(D)
```
```
Figure 6.11: Fitter bias of R(D∗)(left) and R(D)(right) with Asimov fit. x and y axis
```
```
are input value of R(D∗) and R(D) , and z axis is the bias defined as (R(D(∗)) −
```
```
R(D(∗))input)/R(D(∗))input.
```
51
Table 7.1: Summary of the systematic uncertainties.
```
Error source R(D∗) R(D) ρ
```
B → D∗∗ℓ−νℓ branching fractions 0.6% 1.3% 0.02
MC statistics 4.2% 8.2% -0.40
gap mode branching fractions ±100% 0.1-6.5% 0.1-6.3% 0.0
gap mode branching fractions 1.6% 2.1% -0.49
Hadronic B decay branching fractions 1.7% 2.9% 0.06
Continuum background 1.4% 1.9% 0.95
Slow π0,γ efficiency 1.5% 3.0% 0.99
Other efficiency corrections 1.0% 1.0% 0.80
FEI efficiency of data 0.3% 1.1% -1.0
FEI efficiency of B → Dτ ν 0.1% 2.4% 1.0
M 2miss resolution 0.3% 0.9% 0.55
```
Fraction of fake D(∗) 0.7% 1.4% 0.08
```
Fitter bias 0.3% 1.4% 0.00
Form factors correction 0.4% 1.0% -0.34
Total systematic uncertainty 5.1-8.3% 10.6-12.4% -0.20
Table 7.2: Break down of other efficiency corrections.
```
Error source R(D∗) R(D) ρ
```
FEI efficiency calibration 0.9% 1.0% 0.80
Tracking <0.1% <0.1% -0.12
Lepton PID 0.3% 0.5% 0.64
Hadron PID 0.8% 0.8% -0.87
Slow π 0.3% 0.8% 0.97
Slow π0,γ 1.5% 3.0% 0.99
π0 efficiency 0.7% 0.3% 0.84
7 Systematics uncertainties498
Table 7.1 shows a summary of systematic uncertainties. We account for uncertainties in499
detector responses, underlying physics processes, and discrepancies between the data and500
MC simulation. Details of each error source will be explained in each sub-section. The501
```
small errors (< 0.2%) are not listed in the table but explained in the sub-sections.502
```
```
We generated a Asimov data, assuming R(D∗) = 0.254 and R(D) = 0.300 without503
```
systematic uncertainties. For systematic evaluation, we fixed the Asimov data to the504
nominal expectation and refit it with new PDF templates and efficiency, which are fluctu-505
ated according to the systematic uncertainties. After data is unblinded, the Asimov data506
will be replaced with data.507
7.1 B → D∗∗ℓ−νℓ and gap mode branching fractions508
The branching fractions of B → D∗∗ℓ−νℓ decays and gap modes listed in Table 4.6 are509
fluctuated following their errors to generate 1000 toys. Branching ratio of each decay510
52
```
Table 7.3: Change of R(D(∗)) by varying branching ratio of B → D(∗)ηℓν by ±100%.
```
```
Error source R(D∗) R(D)
```
```
BR(B0 → D∗0 +(→ Dη)ℓ−νℓ ) +100% 0.5% 0.6%
```
```
BR(B0 → D∗0 +(→ Dη)ℓ−νℓ ) −100% 6.5% 4.0%
```
```
BR(B0 → D′1+(→ D∗η)ℓ−νℓ) +100% 0.4% 0.1%
```
```
BR(B0 → D′1+(→ D∗η)ℓ−νℓ) −100% 0.7% 6.3%
```
```
BR(B− → D∗0 0(→ Dη)ℓ−νℓ ) +100% 0.6% 0.1%
```
```
BR(B− → D∗0 0(→ Dη)ℓ−νℓ ) −100% 4.7% 0.2%
```
```
BR(B− → D′10(→ D∗η)ℓ−νℓ ) +100% 0.4% 0.2%
```
```
BR(B− → D′10(→ D∗η)ℓ−νℓ ) −100% 1.5% 3.2%
```
```
Table 7.4: Change of R(D(∗)) by varying branching ratio of B → D(∗)ηℓν by ±100%. We
```
used another Asimov data without gap mode. PDF template is nominal.
```
Error source R(D∗) R(D)
```
```
BR(B0 → D∗0 +(→ Dη)ℓ−νℓ ) +100% 0.1% 0.1%
```
```
BR(B0 → D∗0 +(→ Dη)ℓ−νℓ ) −100% 0.1% 0.1%
```
```
BR(B0 → D′1+(→ D∗η)ℓ−νℓ) +100% 0.1% 0.1%
```
```
BR(B0 → D′1+(→ D∗η)ℓ−νℓ) −100% 0.1% 0.1%
```
```
BR(B− → D∗0 0(→ Dη)ℓ−νℓ ) +100% 0.1% 0.1%
```
```
BR(B− → D∗0 0(→ Dη)ℓ−νℓ ) −100% 0.1% 0.1%
```
```
BR(B− → D′10(→ D∗η)ℓ−νℓ ) +100% 0.1% 0.1%
```
```
BR(B− → D′10(→ D∗η)ℓ−νℓ ) −100% 0.1% 0.1%
```
53
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
100
200
300
400
500/ ndf
2χ 0.0001582 / 1norm 24.3±611.2
mean 0.000378±0.001044sigmaL 0.000272±0.005159
sigmaR 0.000235±0.005297
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
50
100
150
200
250
300
/ ndf2χ 0.3034 / 4norm 12.8±329.4
mean 0.000839±0.004152−sigmaL 0.000541±0.009282
sigmaR 0.00054±0.01011
0100
200300
400500
600700
800
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.1: Comparison of Asimov fit results with nominal PDF and varied PDF with
```
D∗∗ℓν branching fractions uncertainty, except for B → D(∗)ηℓν.
```
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
50
100
150
200
250
300/ ndf2χ 86.48 / 10norm 11.8±231mean 0.000±0.012sigmaL
0.00096±0.02839sigmaR 06−5.274e±06−1.148e
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
50
100
150
200
250
300
/ ndf2χ 169.7 / 16norm 13.6±173.2
mean 0.00125±0.00335−sigmaL 0.00151±0.01763
sigmaR 0.00158±0.01297
0
100
200
300
400
500
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.2: Comparison of Asimov fit results with nominal PDF and varied PDF with
```
D(∗)ηℓν branching fractions uncertainty.
```
mode is randomly fluctuated independently following Gaussian function. If the measured511
branching ratio is not available, it is fluctuated ± 100% by uniform function. For each512
toy, PDF is regenerated and Asimov fit is performed as shown in Fig. 7.1-7.2. Because513
```
of large uncertainty, B → D(∗)ηℓν is plotted separately. The R(D) (R(D∗)) fit results514
```
of 1000 toys are fitted by double-side Gaussian. When mean of the double-side gaussian515
is 0, the larger sigma of the double-side gaussians is assigned as a systematic error of516
```
R(D(∗)). When the mean is different from 0 more than 1.5σ of fitting error, the larger517
```
```
one of abs(mean - lower sigma) or abs(mean + higher sigma) is assigned as a systematic518
```
```
error. Pearson’s correlation coefficient (ρ) of R(D∗) and R(D) is estimated by using519
```
the toys. This toy based method will be used to estimate other systematic uncertainties520
in later sub-sections.521
```
Additional case study is performed in Table 7.3. Branching ratio of B → D(∗)ηℓν522
```
±100% and Asimov fit is performed. Because gap mode is separated from D∗∗ decays,523
```
PDF shape is not changed by enlarging the BR by +100%, then impact to the R(D(∗)) is524
```
small. When the BR is changed by −100%, PDF shape is changed largely and the impact525
is large. Table 7.4 shows the same study with different Asimov data, by setting branching526
ratio of gap mode to zero, which is indicated by sideband. Only fitted data is replaced527
with the different Asimov data, and PDF templates are nominal one. As expected, the528
```
impact to R(D(∗)) is small, because no gap mode is found in the fitted data.529
```
7.2 Hadronic B decay branching fractions530
The branching fractions of hadronic B decays are fluctuated following their errors in531
Table 4.5 to generate 1000 toys. Branching ratio of each decay mode is fluctuated inde-532
pendently by assuming Gaussian function. If the measured branching ratio is not available533
on PDG, they are fluctuated ± 100% by uniform function. The branching fractions for534
each toy, PDF is regenerated and Asimov fit is performed as shown in Fig. 7.3. They are535
54
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
50
100
150
200
250
300
350 / ndf2χ 1.589 / 4norm 13.3±338.8
mean 0.00092±0.00512sigmaL 0.00053±0.00675
sigmaR 0.00064±0.01204
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
20
40
60
80
100
120/ ndf
2χ 10.22 / 13norm 4.8±124.6
mean 0.002555±0.004185sigmaL 0.00186±0.02622
sigmaR 0.00144±0.02512
0
50
100
150
200
250
300
350
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.3: Comparison of Asimov fit results with nominal PDF and varied PDF with
hadronic B decay branching fractions uncertainty.
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
2040
6080
100120
140160
180200
/ ndf2χ 13.88 / 10norm 7.4±192.1
mean 0.001422±0.003501−sigmaL 0.00078±0.01484
sigmaR 0.00095±0.01794
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
20
40
60
80
100
120 / ndf2χ 17.54 / 17norm 4.6±117.3mean 0.002663±0.009698
sigmaL 0.00184±0.03377sigmaR 0.00157±0.01979
0
50
100
150
200
250
300
350
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.4: Comparison of Asimov fit results with nominal PDF and varied PDF with
performance corrections uncertainty.
fitted by double-side Gaussian then systematic error is estimated.536
7.3 FEI Efficiency correction537
The number of reconstructed Btag mode at q2 side-band is different from MC expectation,538
as shown in Fig. 5.4. The MC is weighted by the data/MC ratio in each decay mode539
to regenerate PDF and signal efficiency. The difference of Asimov fit results between540
nominal PDF and regenerated PDF is taken as a systematic error.541
7.4 Other efficiency corrections542
Uncertainty of below correction in Sec.4.1 are estimated:543
• hadron PID correction544
• lepton PID correction545
• slow π± efficiency546
• γ efficiency547
```
• π0 efficiency (provided by neutral group locally)548
```
• mode-dependent FEI efficiency549
The correction factors are varied following their errors to generate 1000 toys. For each550
toy, PDF and efficiency are regenerated and Asimov fit is performed as shown in Fig. 7.4.551
They are fitted by double-side Gaussian then systematic error is estimated. Breakdown552
of each error is shown in Table 7.2.553
55
Figure 7.5: decay mode ID of Btag in signal mode and normalization mode. The plots are
area normalized. Error bar shows MC statistics error.
7.5 FEI Efficiency difference of signal and normalization mode554
Figure 7.5 shows decay mode ID of Btag by MC. The figures are area normalized to555
compare fraction of each decay mode. The fraction of ID=4, B0 → D−ππππ0 and B+ →556
D0ππππ0, is different between the B → Dτ ν and B → Dℓν. Although several variables557
of Btag and Bsig are checked, we do not understand the reason of the difference. In order558
to estimate possible systematic error conservatively, we performed Asimov fit study. We559
regenerate PDF and efficiency by applying a weight to scale efficiency of B → Dτ ν at560
```
ID=4 to be same as that of B → Dℓν, then Asimov fit is performed. The impact to561
```
```
R(D∗)(R(D)) is 0.1% (2.0%). These are assigned as systematic error.562
```
7.6 Form factors correction563
```
The uncertainty of form factor parameters of B → (D, D∗, D∗∗)(ℓ, τ )ν are fluctuated by564
```
Hammer, including the correlation of the parameters, to generate 1000 toy of PDF and565
signal efficiency. For each toy, Asimov fit is performed with the new PDF and efficiency,566
as shown in Fig. 7.6. They are fitted by double-side Gaussian then systematic error is567
estimated.568
7.7 Continuum background569
Continuum background is fixed in the fit. We changed weight of the continuum back-570
ground ±100% uniformly to generate 1000 toys. Because their distribution is uniform,571
the systematic error is estimated by taking the maximum difference from 0.572
56
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D*)nominal(R(D*)-R(D*)0
```
50
100
150
200
250 / ndf2χ 10.36 / 8norm 9.4±229.4mean 0.0002771±0.0002057
sigmaL 0.000206±0.003768sigmaR 0.000204±0.003155
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D)nominal(R(D)-R(D)0
```
1020
3040
5060
7080
90/ ndf2χ 18.79 / 26norm 3.50±88.87mean 0.0008243±0.0006731
sigmaL 0.00057±0.01012sigmaR 0.000528±0.007521
0
50
100
150
200
250
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D)nominal(R(D)-R(D)0.1−
```
0.08−0.06−
0.04−0.02−
00.02
0.040.06
0.080.1nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.6: Comparison of Asimov fit results with nominal PDF and varied PDF with
form factor uncertainty.
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
100200
300400
500600
700800
900/ ndf2χ 22.51 / 30norm 11.0±881.8mean 0.00095±0.01869−
sigmaL 0.00061±0.03472sigmaR 0.00065±0.03752
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
50100
150200
250300
350400
450/ ndf2χ 55.67 / 62norm 5.4±437.9mean 0.00189±0.02795−
sigmaL 0.00119±0.06812sigmaR 0.00124±0.07688
0
100
200
300
400
500
600
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.7: Comparison of Asimov fit results with nominal PDF and varied PDF with
the MC statistics uncertainty.
7.8 MC statistics573
MC statistics uncertainty is estimated by bootstrap method. MC event is re-sampled574
following poisson distribution. PDF and signal efficiency are regenerated with the re-575
sampled MC, and Asimov fit is performed. This is repeated 10000 times as shown in576
Fig. 7.7. They are fitted by double-side Gaussian then systematic error is estimated.577
7.9 Fitter bias578
```
As shown in Figure 6.11, fitter bias is seen depending on R(D∗) and R(D) input values.579
```
The maximum bias in the figure is taken as systematic error.580
7.10 τ − → ℓ−ντ νℓ branching fractions581
The branching fractions of τ − → ℓ−ντ νℓ is used for efficiency estimation. We assume582
```
BR(τ − → ℓ−ντ νℓ) = 0.1739 ± 0.0004(0.1782 ± 0.0004) in e (µ) mode. In the fit, it is fixed583
```
to the central value. It is varied ±1σ and Asimov fit is re-performed. The difference of584
Asimov fit result is negligible, 0.2%. Then no systematic error is assigned.585
```
7.11 Fraction of correctly reconstructed D(∗)586
```
The number of incorrectly reconstructed D can be estimated from D mass distribution,587
as shown in Figure 3.2-3.3. It is reliably estimated by MC, because the data agree with588
MC well and there is no peaking structure.589
On the other hand, the number of incorrectly reconstructed D∗ can not be estimated590
precisely from mass difference of D∗ − D as shown in Figure 3.4, because there is peaking591
structure in D∗+ → πD0, D∗0 → π0D0 and D∗0 → π0D0. In order to estimate the592
57
Table 7.5: Data/MC comparison of the number of selected events at q2 side-band. The
error shows statistical error of data. systematic error is not included in the error.
```
Category Fraction of correctly reconstructed D∗)
```
D∗+ → D0π+ D∗+ → D+π0 D∗0 → D0π0 D∗0 → D0γ D0 D+
before fit 0.929 0.853 0.850 0.500 0.907 0.919
after fit 1.000 0.831 1.000 0.501 0.865 0.892
± 0.043 ± 0.137 ± 0.151 ± 0.070 ± 0.034 ± 0.065
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
100
200
300
400
500
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(a) B0 → D∗+τ ν(D∗+ → D0π)
```
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
10
20
30
40
50
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(b) B0 → D∗+τ ν(D∗+ → D+π0)
```
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
50
100
150
200
250
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(c) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
50
100
150
200
250
300
350
400
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(d) B+ → D∗0τ ν(D∗0 → D+γ)
```
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
200
400
600
800
1000
1200
1400
1600
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(e) B+ → D0τ ν
```
```
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1E extra (GeV)0
```
100
200
300
400
500
600
```
Events / ( 0.05 )
```
```
A RooPlot of "E extra (GeV)"A RooPlot of "E extra (GeV)"
```
```
(f) B0 → D+τ ν
```
```
Figure 7.8: Distributions of the EECLextra in each D(∗) decay mode at q2 side-band after the
```
```
fit. Straight (dotted) line is correctly (incorrectly) reconstructed signal.
```
fraction from sideband, EECLextra distribution is fitted at q2 sideband. The PDF is categorized593
```
by correctly and incorrectly reconstructed D(∗) as shown in Figure 5.9 and fraction of594
```
```
correctly reconstructed D(∗) is floated as free parameter. Then fit is performed as shown595
```
in Figure 7.8 and Table 7.5. The fit results are consistent with MC prediction.596
```
Finally, the effect to R(D(∗)) is estimated by Asimov fit. The fraction of correctly597
```
```
reconstructed D(∗) is reweighted following the fit results at q2 sideband and PDF is regen-598
```
erated, then Asimov fit is performed. This is repeated 1000 times as shown in Fig. 7.9.599
7.12 yield of D600
As shown in Figure 5.1-5.2, the data yield of D+ → Kπππ0, D0 → KK, D+ → KS ππ0601
```
are about 20-30% different from MC expectation (more than 2σ of statistical error). The602
```
MC is weighted by the data/MC ratio to adjust the fraction of the three channels based603
on data, and new PDF and efficiency are generated. With the generated PDF, Asimov604
```
data is fitted and result is compared with nominal PDF. The impact to R(D∗) is small,605
```
0.1%, and no systematic uncertainty is assigned.606
58
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D*)nominal(R(D*)-R(D*)0
```
20
40
60
80
100
120
140
160 / ndf2χ 25.39 / 15norm 6.0±151.8mean 0.000538±0.002214−
sigmaL 0.000304±0.004625sigmaR 0.000350±0.005632
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D)nominal(R(D)-R(D)0
```
10
20
30
40
50
60
70
80/ ndf2χ 26.49 / 33norm 2.76±67.02mean 0.001109±0.003969
sigmaL 0.0008±0.0128sigmaR 0.00078±0.01055
0
20
40
60
80
100
120
```
0.1− 0.08− 0.06− 0.04− 0.02− 0 0.02 0.04 0.06 0.08 0.1nominal)/R(D)nominal(R(D)-R(D)0.1−
```
0.08−0.06−
0.04−0.02−
00.02
0.040.06
0.080.1nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.9: Comparison of Asimov fit results with nominal PDF and varied PDF with
```
fraction of correctly reconstructed D(∗) uncertainty.
```
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D*)nominal(R(D*)-R(D*)0
```
200
400
600
800
1000
/ ndf2χ 49.84 / 26norm 13.5±1059
mean 0.000778±0.003348sigmaL 0.00056±0.03238
sigmaR 0.00049±0.02615
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0
```
100
200
300
400
500
600
/ ndf2χ 43.62 / 46norm 8.3±658.3
mean 0.0013±0.0111−sigmaL 0.00087±0.04948
sigmaR 0.00084±0.04476
0
200
400
600
800
1000
```
0.4− 0.3− 0.2− 0.1− 0 0.1 0.2 0.3 0.4nominal)/R(D)nominal(R(D)-R(D)0.4−
```
0.3−
0.2−
0.1−
0
0.1
0.2
0.3
0.4nominal
```
)/R(D*)nominal
```
```
(R(D*)-R(D*)
```
Figure 7.10: Comparison of Asimov fit results with nominal PDF and varied PDF with all
systematic uncertainty, except for MC statistics, FEI efficiency correction, FEI efficiency
difference of signal and normalization mode, and fitter bias.
7.13 M 2miss resolution607
The uncertainty of M 2miss correction is taken into account as systematic error. The PDF608
shape is varied following the uncertainty in Table 5.4 and Asimov fit is performed.609
7.14 Total uncertainty610
In order to estimate total systematic uncertainty, PDF and efficiencies are fluctuated611
following all explained error sources, except for MC statistics, to generate 10000 toys. For612
each toy, PDF is regenerated and Asimov fit is performed as shown in Fig. 7.10. They are613
fitted by double-side Gaussian then systematic error is estimated. The uncertainties of MC614
statistics, FEI efficiency correction, FEI efficiency difference of signal and normalization615
mode, and fitter bias are not included in the toy. Their errors are added to total error by616
```
taking quadratic sum of them. Because not only sigma but also mean (bias) of double-617
```
sided gaussian is included in each systematic source in Table 7.1, quadratic sum of each618
uncertainty is different from the total uncertainty.619
59
8 Results of Asimov Fit620
The results of Asimov fit with statistics and systematic error are621
```
R(D∗) = 0.254 ± 0.022(stat.) ± 0.013 − 0.021(syst.), (8.1)622
```
```
R(D) = 0.300 ± 0.051(stat.) ± 0.032 − 0.037(syst.), (8.2)623
```
```
ρ = −0.42(stat.) − 0.20(syst.). (8.3)624
```
The systematic error depends on amount of gap mode in the fitted Asimov data.625
60
Table 9.1: Fitted parameters in the q2 sideband
parameters prefit postfit with stat. error
```
BR(B → D∗ℓν) 0.1013 0.1038 ± 0.0027
```
```
BR(B → Dℓν) 0.0437 0.0436 ± 0.0012
```
f00 0.4861 ± 0.0080 0.4861 ± 0.0080
f+− 0.5113 ± 0.0108 0.5112 ± 0.0108
NBB 387.1 ± 5.6 387.2 ± 5.6
```
Table 9.2: Comparison of the measured BR(B → D(∗)ℓν) with this analysis and previous
```
measurements. HFLAV 2022 is used for input of FEI efficiency calibration analysis of
```
B → Xℓν. Sum of BR(B0 → D(∗)ℓν) and BR(B+ → D(∗)ℓν) are shown.
```
pdg live HFLAV 2022 this analysis this analysis
q2 sideband selected events
```
BR(B → D∗ℓν) 0.1013 0.1071 0.1038 0.1101
```
```
±0.0013 (stat.+sys.) ±0.0026 (stat.+sys.) ±0.0027(stat.) ±0.0025(stat.)
```
```
±0.0070(sys.) ±0.0070(sys.)
```
```
BR(B → Dℓν) 0.0436 0.0466 0.0436 0.0431
```
```
±0.0010 (stat.+sys.) ±0.0013 (stat.+sys.) ±0.0012(stat.) ±0.0013(stat.)
```
9 Data fit626
9.1 Fit in q2 sideband627
For consistency check, fit is performed in the q2 sideband. Because amount of background628
is very small and fit is failed with the default fit configuration, the background parameters629
```
and R(D(∗)) are specially fixed. Figures 9.1-?? show postfit distributions of the fit vari-630
```
```
ables. Table 9.1 shows the pre and post fit parameters. The measured BR(B → D(∗)ℓν)631
```
```
is consistent with the past measurement, as shown in Table 9.2. The BR(B → D(∗)ℓν)632
```
from HFLAV2022 is used as an input to the FEI calibration analysis of B → Xℓν. This633
```
assumption can affect our measured BR(B → D(∗)ℓν). Because the BR (absolute yield634
```
```
of the normalization mode) will be canceled for the R(D(∗)), such effect is not estimated635
```
quantitatively in this analysis.636
61
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
700
800
```
900)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
50
100
150
200
250
300
350
```
400)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
```
700)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
500
1000
1500
2000
2500
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
```
1000)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.1: Post fit projection to the M 2miss in each sample in q2 sideband.
62
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
50
100
150
200
250
300
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
200
400
600
800
1000
1200
1400
1600
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.2: Post fit projection to the EECLextra in each sample in q2 sideband.
63
Table 9.3: Fitted parameters in π0 ROE sideband
parameters prefit postfit with stat. error
```
R(D∗) – 0.215 ± 0.037
```
```
R(D) – 0.463 ± 0.131
```
```
BR(B → D∗ℓν) 0.1013 0.1055 ± 0.0028
```
```
BR(B → Dℓν) 0.0437 0.0431 ± 0.0013
```
```
N (gap mode), B0 → D∗+τ ν 148.08 72.0 ± 36.6
```
```
N (gap mode), B+ → D∗0τ ν(D∗0 → π0D0) 89.259 35.1 ± 23.7
```
```
N (gap mode), B+ → D∗0τ ν(D∗0 → γD0) 342.39 −96.3 ± 71.0
```
```
N (gap mode), B+ → D0τ ν 1060.3 −60.8 ± 173
```
```
N (gap mode), B0 → D+τ ν 409.50 237.1 ± 107
```
```
N (D∗∗ℓν), B0 → D∗+τ ν 157.29 134.8 ± 39.3
```
```
N (D∗∗ℓν), B+ → D∗0τ ν(D∗0 → π0D0) 71.475 74.0 ± 24.6
```
```
N (D∗∗ℓν), B+ → D∗0τ ν(D∗0 → γD0) 248.90 247.47 ± 70.5
```
```
N (D∗∗ℓν), B+ → D0τ ν 1130.6 1303.0 ± 185
```
```
N (D∗∗ℓν), B0 → D+τ ν 474.84 356.4 ± 105
```
```
N (hadronic B ), B0 → D∗+τ ν 167.67 134.2 ± 22.5
```
```
N (hadronic B ), B+ → D∗0τ ν(D∗0 → π0D0) 87.558 50.413 ± 49.6
```
```
N (hadronic B ), B+ → D∗0τ ν(D∗0 → γD0) 369.30 589.66 ± 39.6
```
```
N (hadronic B ), B+ → D0τ ν 1210.9 1515.3 ± 89.6
```
```
N (hadronic B ), B0 → D+τ ν 784.18 730.6 ± 49.6
```
f00 0.4861 ± 0.0080 0.4861 ± 0.0080
f+− 0.5113 ± 0.0108 0.5113 ± 0.0108
NBB 387.1 ± 5.6 387.1 ± 5.6
9.2 Fit in π0 ROE sideband637
For consistency check, fit is performed in the π0 ROE sideband. Figures 9.3-9.4 show the638
projected distributions of the fit variables at postfit. M 2miss and EECLextra cuts are removed639
from selection to unbox entire region. Table 9.3 shows the prefit and postfit parameters.640
The measured gap mode is lower than nominal value of the MC expectation, as discussed641
in Sec. 5.642
64
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
50
100
150
200
250
300
```
350)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
180)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
50
100
150
200
250
300
350
400
```
450)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
500
1000
1500
2000
```
2500)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
```
600)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.3: Post fit projection to the M 2miss in each sample in π0 ROE sideband.
65
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
20
40
60
80
100
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
5
10
15
20
25
30
35
40
45
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
60
70
80
90
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
20
40
60
80
100
120
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.4: Post fit projection to the EECLextra in each sample in π0 ROE sideband.
66
Table 9.4: Fitted parameters to the selected events
parameters prefit postfit with stat. error
```
R(D∗) – 0.242 ± 0.019
```
```
R(D) – 0.439 ± 0.055
```
```
BR(B → D∗ℓν) 0.1013 0.1101 ± 0.0025
```
```
BR(B → Dℓν) 0.0437 0.0431 ± 0.0013
```
```
N (gap mode), B0 → D∗+τ ν 118.27 21.4 ± 24.8
```
```
N (gap mode), B+ → D∗0τ ν(D∗0 → π0D0) 70.996 41.6 ± 15.1
```
```
N (gap mode), B+ → D∗0τ ν(D∗0 → γD0) 229.43 53.4 ± 49.6
```
```
N (gap mode), B+ → D0τ ν 776.79 240.3 ± 93.5
```
```
N (gap mode), B0 → D+τ ν 271.10 89.5 ± 46.4
```
```
N (D∗∗ℓν), B0 → D∗+τ ν 110.70 60.1 ± 31.2
```
```
N (D∗∗ℓν), B+ → D∗0τ ν(D∗0 → π0D0) 46.964 28.9 ± 23.9
```
```
N (D∗∗ℓν), B+ → D∗0τ ν(D∗0 → γD0) 206.19 190.5 ± 58.3
```
```
N (D∗∗ℓν), B+ → D0τ ν 774.99 731.1 ± 134.0
```
```
N (D∗∗ℓν), B0 → D+τ ν 283.32 294.2 ± 63.5
```
```
N (hadronic B ), B0 → D∗+τ ν 98.644 86.0 ± 25.3
```
```
N (hadronic B ), B+ → D∗0τ ν(D∗0 → π0D0) 41.766 3.5 ± 12.2
```
```
N (hadronic B ), B+ → D∗0τ ν(D∗0 → γD0) 157.28 165.6 ± 38.2
```
```
N (hadronic B ), B+ → D0τ ν 566.68 469.2 ± 94.6
```
```
N (hadronic B ), B0 → D+τ ν 266.88 125.6 ± 25.3
```
f00 0.4861 ± 0.0080 0.4861 ± 0.0080
f+− 0.5113 ± 0.0108 0.5113 ± 0.0108
NBB 387.1 ± 5.6 387.1 ± 5.6
9.3 Data fit to selected events643
```
The fit is performed to the selected events. Figures 9.5-9.8 (9.9-9.12) show projected644
```
```
distributions of the fit variables at the prefit (postfit). There is no local deviation more645
```
than 3σ in the postfit distributions. After the fitting, global χ2/ndf= 1.15. It indicates646
the data/MC agreement has no problem at the postfit. Table 9.4 shows the fit parameters.647
```
For consistency check, we compared the measured value of BR(B → D∗ℓν) and648
```
```
BR(B → Dℓν), as shown in Table 9.2. They agree each other within systematic er-649
```
ror. The measured BR at q2 sideband and selected events are 1.5σ different in each other,650
because some of systematics error is canceled and relative systematic error is reduced to651
```
1.6%. In order to evaluate its impact on R(D∗), sanity check is performed as in Sec. 9.3.1.652
```
The measured gap mode is lower than nominal value of the MC expectation. It is653
consistent with the π0 ROE sideband. Figure ?? show the comparison of the background654
parameters between the selected events and π0 ROE sideband. In the plot, systematic655
error of continuum background is included, because amount of continuum background is656
large in the π0 ROE sideband and it affects amount of the fitted yield of hadronic back-657
ground. The background yields agree between the selected events and π0 ROE sideband658
within the error.659
```
Table 9.5 shows the estimated systematic uncertainties on R(D(∗)) by using real data,660
```
instead of Asimov data in Sec. 7. Because amount of gap mode is smaller than the MC,661
systematic uncertainty of the gap mode branching fractions is smaller than Asimov data662
in Table 7.1.663
67
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
1400
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
700
```
800)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
1000
2000
3000
4000
5000
6000
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.5: Pre fit projection to the M 2miss in each sample.
68
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
180)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
10
20
30
40
50
60
70
80
```
90)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
```
160)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
700
```
800)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.6: Pre fit projection to the M 2miss in each sample.
69
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
200
400
600
800
1000
1200
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
800
900
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
500
1000
1500
2000
2500
3000
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.7: Pre fit projection to the EECLextra in each sample.
70
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
5
10
15
20
25
30
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
20
40
60
80
100
120
140
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
```
Figure 9.8: Pre fit projection to the EECLextra at 1.5 GeV 2 < M 2miss (3.0 GeV 2 < M 2miss) for
```
```
D∗(D) sample in each sample.
```
71
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
1400
```
1600)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
700
```
800)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
1000
2000
3000
4000
5000
6000
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
200
400
600
800
1000
1200
```
1400)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.9: Post fit projection to the M 2miss in each sample.
72
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
180)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
νD*lνDl
D**gapD**
hadroncontinuum
Other
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
10
20
30
40
50
60
70
80
```
90)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
```
160)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
100
200
300
400
500
600
700
```
800)2)2c
```
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
2− 0 2 4 6 8 10)2)2c((GeV/2missM0
```
20
40
60
80
100
120
140
160
```
)2)2
```
c
```
Events / ( 0.5 (GeV/
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
2− 0 2 4 6 8 105−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.10: Post fit projection to the M 2miss in each sample. y axis is zoomed.
73
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
200
400
600
800
1000
1200
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
800
900
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
500
1000
1500
2000
2500
3000
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
100
200
300
400
500
600
700
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
Figure 9.11: Post fit projection to the EECLextra in each sample.
74
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
Data
ντD*νD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(a) B0 → D∗+τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
5
10
15
20
25
30
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(b) B+ → D∗0τ ν(D∗0 → D0π0)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(c) B+ → D∗0τ ν(D∗0 → D0γ)
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
20
40
60
80
100
120
140
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(d) B+ → D0τ ν
```
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE0
```
10
20
30
40
50
```
Events / ( 0.05 GeV )
```
DataντD*
ντDνD*l
νDlD**gap
D**hadron
continuumOther
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 25−4−
3−2− 1−
012
345Pull
```
(e) B0 → D+τ ν
```
```
Figure 9.12: Post fit projection to the EECLextra at 1.5 GeV 2 < M 2miss (3.0 GeV 2 < M 2miss) for
```
```
D∗(D) sample in each sample.
```
75
Table 9.5: Summary of the systematic uncertainties.
```
Error source R(D∗) R(D) ρ
```
B → D∗∗ℓ−νℓ branching fractions 0.3% 1.3% 0.25
MC statistics 4.8% 8.4% -0.44
gap mode branching fractions ±100% 2.6% 2.6% 0.0
gap mode branching fractions 0.5% 0.3% -0.06
Hadronic B decay branching fractions 1.6% 1.5% -0.26
Continuum background 2.4% 2.1% 0.93
Slow π0,γ efficiency 2.2% 2.4% 0.99
Other efficiency corrections 0.7% 1.4% 0.92
FEI efficiency of data 0.9% 1.8% -1.0
FEI efficiency of B → Dτ ν 0.1% 1.8% 1.0
M 2miss resolution 0.5% 0.8% 0.48
```
Fraction of fake D(∗) 0.5% 1.2% 0.00
```
Fitter bias 0.3% 1.2% 0.00
Form factors correction 0.5% 0.9% -0.70
Total systematic uncertainty 6.7% 10.2% -0.20
9.3.1 Sanity check664
For sanity check, data sample is split as follows:665
• D0 mode and D+ mode666
• electron mode and muon mode667
• data in exp7-18 and exp20-26668
• add q2 sideband to the fit669
```
In each case, fit is re-performed and fitted values of R(D(∗)) are checked as shown in670
```
```
Table 9.6. They agree each other within statistical error. The R(D) is different by 1.37671
```
σ between electron and muon mode.672
76
```
Table 9.6: Comparison of R(D(∗)) by splitting the data set for sanity check. Only statis-
```
tical error is shown.
```
Sample R(D∗) R(D) ρ
```
Nominal 0.242 ± 0.019 0.439 ± 0.055 -0.40
D0 mode only 0.246 ± 0.021 0.411 ± 0.069 -0.43
D+ mode only 0.214 ± 0.068 0.484 ± 0.927 -0.41
electron mode only 0.265 ± 0.024 0.360 ± 0.065 -0.40
muon mode only 0.218 ± 0.029 0.505 ± 0.084 -0.41
exp7-18 only 0.245 ± 0.027 0.408 ± 0.074 -0.39
exp20-26 only 0.247 ± 0.029 0.480 ± 0.079 -0.41
add q2 sideband 0.246 ± 0.020 0.403 ± 0.052 -0.41
77
10 Results673
The results of data fit are674
```
R(D∗) = 0.242 ± 0.019(stat.) ± 0.016(syst.), (10.1)675
```
```
R(D) = 0.439 ± 0.055(stat.) ± 0.045(syst.), (10.2)676
```
```
ρ = −0.40(stat.) − 0.20(syst.). (10.3)677
```
11 Comparison with past measurements678
78
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDstTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDstTv
```
(a) B → D∗τ ν
```
00.02
0.040.06
0.080.1
0.120.14
0.160.18
```
0.2)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDTv
```
(b) B → Dτ ν
```
0
0.020.04
0.06
0.08
0.10.12
0.14
0.160.18
```
0.2)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDstlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDstlv
```
(c) B → D∗ℓν
```
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDlv
```
(d) B → Dℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststgap
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststgap
```
(e) B → D∗∗ℓν gap mode
```
0
0.01
0.02
0.03
0.04
0.05
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststlv
```
(f) B → D∗∗ℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
HadB
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
HadB
```
(g) hadronic B decay
```
0
0.02
0.04
0.06
0.08
0.1
0.12
```
0.14 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Continuum
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Continuum
```
(h) Continuum
```
OtherBG
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
OtherBG
```
(i) Other
```
```
Figure 1.1: PDF of each category in B+ → D∗0ℓ+ (D∗0 → D0π0) sample. z-axis is
```
probability.
Appendix A PDF679
Figure 1.1–1.4 show the PDF in each sample and category.680
79
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDstTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDstTv
```
(a) B → D∗τ ν
```
0
0.02
0.04
0.06
0.08
```
0.1)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDTv
```
(b) B → Dτ ν
```
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDstlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDstlv
```
(c) B → D∗ℓν
```
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
```
0.18 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDlv
```
(d) B → Dℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststgap
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststgap
```
(e) B → D∗∗ℓν gap mode
```
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
```
0.045 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststlv
```
(f) B → D∗∗ℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
```
0.08 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
HadB
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
HadB
```
(g) hadronic B decay
```
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
```
0.09 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Continuum
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Continuum
```
(h) Continuum
```
0
0.1
0.2
0.3
0.4
0.5
```
0.6)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
OtherBG
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
OtherBG
```
(i) Other
```
```
Figure 1.2: PDF of each category in B+ → D∗0ℓ+ (D∗0 → D0γ) sample. z-axis is
```
probability.
80
0
0.01
0.02
0.03
0.04
0.05
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDstTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDstTv
```
(a) B → D∗τ ν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
```
0.09 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDTv
```
(b) B → Dτ ν
```
0
0.02
0.04
0.06
0.08
0.1
0.12
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDstlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDstlv
```
(c) B → D∗ℓν
```
00.02
0.040.06
0.08
0.10.12
0.14
0.160.18
```
0.2)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDlv
```
(d) B → Dℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststgap
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststgap
```
(e) B → D∗∗ℓν gap mode
```
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
```
0.045 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststlv
```
(f) B → D∗∗ℓν
```
0
0.01
0.02
0.03
0.04
0.05
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
HadB
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
HadB
```
(g) hadronic B decay
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Continuum
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Continuum
```
(h) Continuum
```
0
0.05
0.1
0.15
0.2
0.25
```
0.3)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
OtherBG
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
OtherBG
```
(i) Other
```
Figure 1.3: PDF of each category in B+ → D0ℓ+ sample. z-axis is probability.
81
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDstTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDstTv
```
(a) B → D∗τ ν
```
0
0.02
0.04
0.06
0.08
```
0.1)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
SignalDTv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
SignalDTv
```
(b) B → Dτ ν
```
0
0.02
0.04
0.06
0.08
0.1
```
0.12 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDstlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDstlv
```
(c) B → D∗ℓν
```
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
```
0.18 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
NormDlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
NormDlv
```
(d) B → Dℓν
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststgap
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststgap
```
(e) B → D∗∗ℓν gap mode
```
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
```
0.04 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Dststlv
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Dststlv
```
(f) B → D∗∗ℓν
```
0
0.01
0.02
0.03
0.04
```
0.05 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
HadB
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
HadB
```
(g) hadronic B decay
```
0
0.01
0.02
0.03
0.04
0.05
0.06
```
0.07 )2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
Continuum
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
Continuum
```
(h) Continuum
```
0
0.02
0.04
0.06
0.08
```
0.1)2)2c
```
```
Events / ( 0.222222 GeV x 0.923077 (GeV/
```
OtherBG
```
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2(GeV)extraECLE2−
```
0
2
4
6
8
```
10)2)2c
```
```
((GeV/2miss
```
M
OtherBG
```
(i) Other
```
Figure 1.4: PDF of each category in B0 → D−ℓ+ sample. z-axis is probability.
82
References681
[1] Georges Aad et al. Test of the universality of τ and µ lepton couplings in W -boson682
```
decays with the ATLAS detector. Nature Phys., 17(7):813–818, 2021.683
```
[2] Z. R. Huang, Y. Li, C. D. Lu, M. A. Paracha and C. Wang. Footprints of New684
```
Physics in b → cτ ν Transitions. Phys. Rev. D, 98(095018), 2018.685
```
[3] S. Boucenna, A. Celis, J. Fuentes-Martin, A. Vicente and J. Virto. Phenomenology686
```
of an SU(2) × SU(2) × U(1) model with lepton-flavour non-universality,. JHEP,687
```
```
1612(059), 2016.688
```
[4] A. Andrei, Becirevic D., A. Darius , F. Jaffredo and O. Sumensari. On the single689
```
leptoquark solutions to the B-physics anomalies . Phys. Rev. D, 104(055017), 2021.690
```
[5] David London and Joaquim Matias. B Flavour Anomalies: 2021 Theoretical Status691
Report. Ann. Rev. Nucl. Part. Sci., 72:37–68, 2022.692
[6] E. Ben-Haim Y. Amhis, S. Banerjee et al. Averages of b-hadron, c-hadron, and693
```
τ -lepton properties as of 2018. Eur. Phys. J. C, 81(226), 2021.694
```
```
[7] J. P. Lees et al. Evidence for an excess of B → D(∗)τ −ντ decays. Phys. Rev. Lett.,695
```
109:101802, Sep 2012.696
```
[8] J. P. Lees and others. Measurement of an Excess of B → D(∗)τ −ντ Decays and697
```
```
Implications for Charged Higgs Bosons. Phys. Rev. D., 88(072012), 2013.698
```
```
[9] G. Caria et al. . Measurement of R(D) and R(D∗) with a semileptonic tagging699
```
```
method. Phys. Rev. Lett., 124(161803), 2020.700
```
[10] Y. Sato et al. Measurement of the branching ratio of b0 → D∗+τ −ντ relative to701
b0 → D∗+ℓ−νℓ decays with a semileptonic tagging method. Phys. Rev. D, 94:072007,702
Oct 2016.703
```
[11] S. Hirose et al. Measurement of the τ lepton polarization and r(D∗) in the decay704
```
B → D∗τ −ντ with one-prong hadronic τ decays at belle. Phys. Rev. D, 97:012004,705
Jan 2018.706
[12] R. Aaij and others. Test of Lepton Flavor Universality by the measurement of707
the B0 → D∗τ ν branching fraction using three-prong τ decays. Phys. Rev. D.,708
```
97(072013), 2018.709
```
```
[13] R. et al Aaij. Measurement of the ratio of branching fractions B(b0 →710
```
```
D∗+τ −ντ )/B(b0 → D∗+µ−νµ). Phys. Rev. Lett., 115:111803, Sep 2015.711
```
[14] Roel Aaij et al. Tests of lepton universality using B0 → K0S ℓ+ℓ− and B+ → K∗+ℓ+ℓ−712
```
decays. Phys. Rev. Lett., 128(19):191802, 2022.713
```
```
[15] R. Aaij and others. Measurement of the ratios of branching fractions R(D∗) and714
```
```
R(D0). arXiv:2302.02886, 2023.715
```
[16] K.Kojima and others. B2N-2022-32. 2023.716
[17] R. Aaij and others. B2N-2024-036. 2023.717
83
[18] S.Patra and V.Bhardwaj. B2N-2021-002. 2021.718
[19] https://indico.belle2.org/event/12225/contributions/79423/attachments/29422/43491/gapupdate.719
[20] Florian U. Bernlochner et al. Das ist der hammer: consistent new physics interpre-720
tations of semileptonic decays. The European Physical Journal C, 80, Sep. 2020.721
[21] M.Dorigo and M.Mantovano. Belle2-note-ph-2024-045.722
84