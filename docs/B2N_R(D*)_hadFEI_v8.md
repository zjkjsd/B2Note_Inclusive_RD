Belle
BELLE2-NOTE-PH-2025-031
Version 4.2
December 8, 2025
```
Measurement of the R(D∗) ratio and Pτ in
```
hadronic 1-prong τ decays with the hadronic
FEI
Ilias Tsaklidis1, Florian Bernlochner1,
Markus Prim1, Agrim Aggarwal1,
Slavomira Stefkova1, Valerio Bertacchi1, Jochen Dingfelder1
1 University of Bonn
Abstract
```
This note presents a measurement of the R(D∗) ratio defined as B→D∗τ νB→D∗ℓν and1
```
```
the polarization of the τ lepton (Pτ ) in hadronic one-prong τ decays using the2
```
hadronic Full Event Interpretation. The analysis is based on the full Long Shut-3
down 1 dataset, corresponding to an integrated luminosity of 365.29 ± 1.70 fb−1 col-4
```
lected on the Υ (4S) resonance. This represents the first simultaneous measurement5
```
```
of R(D∗) and Pτ at Belle II. The analysis aims to shed light on the longstanding6
```
```
R(D∗) anomaly — the discrepancy between experimental measurements and Stan-7
```
dard Model predictions observed over the past 15 years — and to explore potential8
contributions from New Physics, to which Pτ is particularly sensitive. We report9
```
R(D∗) = xxx ± xxx(stat) ± xxx(syst.) and Pτ = xxx ± xxx(stat) ± xxx(syst.) with10
```
a correlation coefficient of ρ = xxx as determined from the simultaneous fit.11
Todo list
1
Contents
0 Changelog 5
1 Introduction 7
2 Physics motivation 9
2.1 Theoretical motivations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2 Experimental landscape . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 Datasets and software 13
3.1 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.1.1 basf2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.1.2 rdstar1prong . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.1.3 pyhf . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.1.4 SysVar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.1.5 cabinetry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.1.6 HAMMER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.2 Simulation Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
```
3.2.1 Full Event Interpretation (FEI) skims . . . . . . . . . . . . . . . . . 18
```
```
3.2.2 Generic Monte Carlo (MC) . . . . . . . . . . . . . . . . . . . . . . 18
```
3.2.3 Gap modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3 Experimental data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
```
3.3.1 Experimental data Υ (4S) . . . . . . . . . . . . . . . . . . . . . . . 22
```
3.3.2 Off-resonance data . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 Online reconstruction 24
4.1 Event signature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2 Global tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3 Event-wise selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.4 Tag side reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.5 Final state particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.5.1 Photons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.5.2 Leptons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.5.3 Charged hadrons . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.6 Composite particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6.1 π0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6.2 K0S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6.3 ρ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6.4 Charmed mesons . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.6.5 B meson candidates . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
```
4.7 Υ (4S) and Rest of Event . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
```
2
5 Offline processing 32
5.1 Truth-matching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.1.1 Btag and Bsig . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.1.2 Bsig decay category . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5.1.3 D∗ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5.1.4 τ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5.1.5 Hadronic decays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.1.6 Final truth matched categories . . . . . . . . . . . . . . . . . . . . 35
5.2 Helicity angle calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.3 Definition of Signal Region . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.4 Best Candidate Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.5 Corrections from the Performance group . . . . . . . . . . . . . . . . . . . 42
5.5.1 Luminosity scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.2 Tracking efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.3 Tracking momentum scale . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.4 Photon energy bias . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.5 Photon efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.5.6 π0 efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.5.7 πs efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
```
5.5.8 PID (with the systematics framework) . . . . . . . . . . . . . . . . 44
```
```
5.5.9 PID (custom corrections) . . . . . . . . . . . . . . . . . . . . . . . . 47
```
5.6 Branching Fraction corrections . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.6.1 Charmed mesons . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.6.2 τ lepton . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.6.3 Double charm background . . . . . . . . . . . . . . . . . . . . . . . 48
5.6.4 Prompt hadronic background . . . . . . . . . . . . . . . . . . . . . 49
5.7 Gap replacement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
```
5.8 Form Factor (FF) reweighing . . . . . . . . . . . . . . . . . . . . . . . . . 51
```
5.9 D0 mass calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.10 Continuum calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.11 FEI calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.12 Photon multiplicity reweighting . . . . . . . . . . . . . . . . . . . . . . . . 58
6 Signal extraction 62
```
6.1 R(D∗) parametrization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
```
6.2 Pτ parametrization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
6.3 Sideband and Control regions . . . . . . . . . . . . . . . . . . . . . . . . . 69
6.4 Sensitivity on Asimov data . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
```
6.5 Statistical validation of R(D∗) and Pτ fit . . . . . . . . . . . . . . . . . . . 78
```
7 Systematics 84
```
7.1 Systematic budget for the R(D∗) and Pτ fit . . . . . . . . . . . . . . . . . 85
```
3
8 Agreement of simulated and experimental data 87
8.1 Off-resonance data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
8.2 Control Region fits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
8.3 Correctly reconstructed events with constrained normalization . . . . . . . 91
8.4 Correctly reconstructed events with free normalization . . . . . . . . . . . 94
8.5 Misreconstructed events with constrained normalization . . . . . . . . . . . 95
8.6 Misreconstructed events with free normalization . . . . . . . . . . . . . . . 97
9 Results 100
9.1 Box-opening strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
9.2 Box-closed results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
9.3 Box opened results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
A SysVar 102
B PDG codes 109
C Multinomial errors 110
D D0 mass calibration 111
```
E Form Factor (FF) model parameters 114
```
F FEI calibration fit validation 123
G Statistical tests 125
H Helicity angle window optimization 128
I Selection of D0 modes 129
J Background composition checks 131
K FEI calibration postfit plots 143
L Free parameters of the fit 146
References 200
4
0 Changelog
1. v1.0
```
(a) Initial commit.
```
```
(b) Setting b2template and document structure.
```
2. v1.0 → v2.0
```
(a) Added b2note number
```
3. v2.0 → v3.0
```
(a) Added proper changelog
```
```
(b) Fixed failing references
```
```
(c) Corrected spelling typos across the document using ispell
```
4. v3.0 → v3.1
```
(a) Added dedicated section L for working group review answers.
```
```
(b) Answered to Michele Mantovano’s questions
```
```
(c) Removed some text and the Table with the MC15ri luminosities 3.2.2 as part
```
of WG-review answer
```
(d) Updated Table 10 with some global tags that been included but the note was
```
not up-to-date.
```
(e) Added a comment in Section 5.1.4 in line 622 about the problems in the τ
```
decay mode truth matching.
```
(f) Removed misinformation sentence from Section 5.5.5 about the application of
```
photon efficiency corrections to the ROE.
```
(g) Removed all information about the background reweighting from Section 6.3
```
as a result of Michele’s question 20.
```
(h) Updated Figure 56 using the MINOS error for Pτ as a result of Michele’s
```
question 24.
```
(i) Modified the text in Section to avoid confusion about event level cuts. Brought
```
up in Koga-san’s question 34.
```
(j) Modified the text in sections 8.5 and 8.6 to make it more clear that the photon
```
multiplicity reweighting has been used for these Data/MC checks.
```
(k) Added Appendix I as part of answer to Question 41. The D0 → K−K+ and
```
D0 → π−π+ are now excluded from the analysis. I updated Sections 4.6.4 and
5.9.
```
(l) Updated Table 6 as part of Question 32.
```
5. v3.1 → v3.2
5
```
(a) Updated online cuts for D0 and ρ mesons in Section 4
```
```
(b) Updated final selection and SR definition in Section 5.3
```
```
(c) Added a linearity study for Pτ in Section 6.5.
```
```
(d) Added new Section 5.10 for continuum calibration based on off-resonance data.
```
```
(e) Updated FEI calibration in Section 5.11. We now switched to a mode-by-mode
```
calibration contrary to the previous flat calibration factors.
```
(f) Updated all plots in Section 6 with the new coarse binning for the leptonic
```
reconstruction and new EextraECL range for the hadronic reconstruction.
```
(g) Rearanged Section 6 for better flow and clarity since based on the WG-reviewer
```
comments some parts read of a bit misleading. Added Section 5.10 that outlines
our new continuum calibration based on off-resonance data.
```
(h) Updated all plots in Section 8.
```
6. v3.2 → v4.0
```
(a) Move table of contents to the very top of the document.
```
```
(b) Add and answer comments and questions from FSR.
```
```
(c) Complete answers from WGR.
```
```
(d) Added a new template for the τ crossfeed semitauonic events as described in
```
Question 93.
7. v4.0 → v4.1
```
(a) Updated Table 44 with systematic budget.
```
```
(b) Moved questions and answers from WGR to the end of the document.
```
```
(c) Moved List of Figures, Tables and Acronyms after the Appendices
```
8. v4.1 → v4.2
```
(a) Updated text in 4.5.1 to match Table 14. Missmatch pointed out by the RC.
```
```
(b) Renamed Section 5.5.8 and added Section 5.5.9 for the customly derived effi-
```
ciency corrections for muons faking pions.
```
(c) Added explanation about electron momentum used for momentum correction
```
bin with respect to Brems recovery in Line 796.
```
(d) Updated Table 44 with systematic budget, including fake rates where a muon
```
is faking a pion.
6
1 Introduction12
```
The Standard Model of Particle Physics (SM) provides a solid description of the Universe13
```
at the elementary level but fails to account for several well-established phenomena docu-14
mented in the scientific literature. Therefore, a primary goal of the physics community is15
to develop a more comprehensive framework that incorporates the SM while addressing16
```
these unexplained observations [1]. Lepton Flavour Universality (LFU) is a fundamental17
```
postulate of the SM that can be tested experimentally. Any observed discrepancies from18
its predictions could serve as a gateway to new physics beyond the SM [2].19
Over the past decade, several experimental results have hinted at the existence of20
```
Lepton Flavor Violating processes [3]. In this analysis, we aim to measure the R(D∗)21
```
ratio which is defined as22
```
B(B → D∗τ ν)
```
```
B(B → D∗ℓν)
```
```
(1)23
```
```
using 1-prong hadronic τ decays. The R(D∗) ratio is an excellent test of LFU since24
```
it has a relatively clear theoretical prediction with several factorizable experimental and25
theoretical uncertainties canceling in the ratio. Additionally, since the τ lepton decays into26
```
two particles (a charged hadron and a neutrino), we can also determine the polarization27
```
of the τ lepton Pτ . Such a measurement becomes impractical for leptonic τ decays where28
two undetectable neutrinos are present.29
```
This will be the first measurement of R(D∗) in hadronic τ decays using Belle II data.30
```
Furthermore, it will mark only the second-ever measurement of Pτ in B-semileptonic31
decays—the first being a Belle result from 2017 [4]. The theoretical and experimental32
motivation for carrying out this measurement are outlined in 2.33
```
We analyze the Long Shudown 1 (LS1) dataset which accounts to collisions of an34
```
```
integrated luminosity of 365.29 ± 1.70 fb−1 on the Υ (4S) production energy. The datasets35
```
and the software used to analyze the data are described in section 3.36
```
For the reconstruction of events we first use the Full Event Interpretation (FEI) al-37
```
gorithm [5] to reconstruct the second B meson of the event in fully hadronic modes and38
kinematically constrain the signal B meson of interest. We then combine D∗ candidates39
with a charged π meson or a charged ρ meson for the signal B meson reconstruction. For40
```
the denominator of R(D∗) in equation 1 i.e. the normalization mode, we combine the D∗41
```
candidates with an electron or a muon. We ignore any neutrinos from the reconstruction42
as these will not be captured by the Belle II detector. We then combine the above with43
```
the candidate from the FEI to build Υ (4S) candidates. We select only events where no44
```
extra charged tracks can be found. Naturally correctly reconstructed B → D∗τ ν and45
B → D∗ℓν decays will peak at small values of the extra energy in the calorimeter, since46
all particles have been assigned either to the signal or to the tag side B meson, with47
background decays being assigned a higher value for the aforementioned quantity. Our48
reconstruction is described step by step in section 4.49
In order to account for any mismodelling effects in the simulation we correct our50
simulated dataset by considering three different kinds of corrections. Firstly the ones51
```
recommended by the Belle II Performance group [6]. Branching Fraction (BF) corrections52
```
where we correct the values of the DECAY.dec file according to the latest values of the53
7
```
Particle Data Group (PDG) [7]. Lastly calibrations of the hadronic FEI algorithm and54
```
background reweighing to account for composition differences in the background decays55
in the signal enriched region and other regions used for calibrations. All the above are56
described in section 5.57
In order to extract our signal we perform a binned maximum likelihood fit [8]. We58
implement a simultaneous two dimensional fit using pyhf [9], [10] in bins of the missing59
mass squared and the extra energy in the calorimeter in a kinematic region where we60
```
expect to be signal enriched. The main challenge of measuring R(D∗) in hadronic τ decays61
```
compared to the leptonic modes is the significantly higher contamination of the retained62
sample from background events, mainly from fully hadronic decays and continuum events.63
Many of the former ones have never been measured experimentally, so the assumed BF64
is often purely a guess. Continuum events often also suffer from mismodelling effects65
given that the PYTHIA [11] parameters are not finely tuned in the Belle II simulation.66
```
Several Control Region (CR)s are added in order to normalize the background in the67
```
signal enriched region. The signal extraction method, the definition of the CR and the68
systematic uncertainties are discussed in sections 6 and ??.69
We perform several tests to ensure that the modeling in our corrected simulated data70
is good. All these tests are described in section 8. Lastly we present our results in section71
9.72
8
2 Physics motivation73
In the SM semileptonic B decays involving a D∗ meson proceed via tree level Feynman74
diagrams with couplings to the W ± boson. Figure 1 shows the Feynman diagram at the75
quark level. The relatively large value of |Vcb| makes such a decay process experimentally76
favorable, as it provides sufficient data compared to other rare processes [7]. The coupling77
```
of the W boson to both light leptons (e and µ) and to the heavier τ lepton should be78
```
identical according to the LFU [12] except for kinematic phase-space differences which79
are calculated trivially. This enables the conduction of LFU tests as the couplings of the80
W boson to the leptons are precisely predicted within the SM.81
Figure 1: Feynman diagram of a b → c transition at the quark level.
2.1 Theoretical motivations82
The b → c transition at the quark level is not directly accessible in experiments, as quarks83
are confined within hadrons [13]. Instead, one studies the transition at the hadronic level,84
where the B meson decays into a D∗ meson along with a lepton-neutrino pair. This process85
is governed by the weak interaction, but due to the presence of strong interactions, the86
hadronic effects must be carefully modeled.87
```
To describe the hadronic transition between the B and D∗ mesons, form factors (Form88
```
```
Factor (FF)s) are introduced to parameterize the non-perturbative QCD effects governing89
```
the decay. These FFs encapsulate the dynamics of the heavy-to-heavy quark transition90
and depend on the squared four-momentum transfer, q2, between the initial and final91
hadronic states. The FFs are essential in determining the decay rate and kinematic92
distributions of B → D∗τ ν decays [14].93
```
While the R(D∗) ratio directly probes the decay rate of B → D∗τ ν decays, an addi-94
```
tional key observable is the polarization of the τ lepton, denoted as Pτ . Pτ is determined95
by the spin structure of the underlying interaction and depends on the helicity amplitudes96
of the B → D∗ transition. These amplitudes are directly influenced by the FFs, which97
govern the relative strength of different helicity contributions. Thus, a measurement of98
9
Pτ provides valuable insight into the balance between longitudinal and transverse helicity99
states of the D∗, complementing differential decay rate measurements [15].100
Furthermore in the SM, the τ lepton is expected to be highly polarized due to the101
purely left-handed chiral structure of the weak interaction. The polarization is sensitive102
to different helicity structures of the b → c transition and can be affected by new physics103
contributions. For instance, if tensor or scalar interactions exist, they would introduce104
right-handed or mixed-chirality contributions. Scalar interactions could be explained by105
the existence of a charged Higgs boson described in Two-Higgs Doublet Models [16].106
Tensor interactions could be mediated by hypothetical particles called leptoquarks, that107
couple to both leptons and quarks [17], while a heavy W ’ boson could alter the chirality108
of the b → c transition by introducing right handed currents [18]. Precise measurements109
```
of Pτ , in combination with R(D∗) would provide a robust way to differentiate between110
```
these new physics scenarios and test the validity of SM predictions.111
2.2 Experimental landscape112
The consistent study of B-hadrons started with B-factories such as the KEKB collider in113
Japan [19] and the PEP-II collider in the United-States [20], even though the bottom quark114
has been observed already in 1977 [21]. The reason for that is the challenging experimental115
environment, especially in semileptonic decays due to the presence of missing, undetected116
```
neutrinos. Several measurements of R(D∗) have been carried out since the beginning117
```
of the B-factory era. The first measurement was conducted by BABAR in 2012 [22]. It118
used hadronic tagging to and leptonic τ decays and reported a tension of 2.7 σ from the119
SM expectation. To this date this is measurement with the largest discrepancy. Several120
```
measurement followed from Belle that used hadronic or SemiLeptonic (SL) tagging and121
```
leptonic or hadronic τ decays demonstrated similar tensions, without however being able122
to rule out or confirm the discrepancy reported by BABAR. In recent years new results123
from LHCb and Belle II have reported newest results but still haven’t give a final answer124
to the discrepancy due to the lack of statistical precision. The results mentioned above125
are summarized in Table 1 with the first uncertainty being statistical and the second126
systematic.127
The experimental average of all those measurements is determined by the Heavy Flavor128
```
Averaging Group (HFLAV) [3]. The average is found to be 0.287 ± 0.012 with a total129
```
tension of 2.54σ All the above results are summarized in Figure 2130
```
In contrast to R(D∗), the Pτ has been measured only once by the Belle collaboration131
```
```
[4]. The measured value of Pτ at Belle is −0.38 ± 0.51 (stat) +0.21−0.16 (syst), which is in132
```
agreement with the Standard Model, excluding polarization values greater than 0.5 at133
the 90% confidence level. The measurement of Pτ is not feasible in leptonic τ decays134
due to the presence of two missing neutrinos, while resolution effects make it particularly135
challenging in three-prong hadronic decays. At present, Belle II is the only experiment136
capable of measuring Pτ with the current experimental techniques used by both Belle II137
and LHCb. An improved measurement of the polarization with reduced uncertainty138
would further constrain form factor models and provide valuable insights into potential139
new physics contributions, as previously discussed.140
10
```
Table 1: Overview of experimental measurements of R(D∗) [23]
```
```
Experiment R(D∗) Tension Year Tagging τ Decays Reference
```
BABAR 0.332 ± 0.024 ± 0.018 2.7σ 2012 Hadronic τ → ℓντ νℓ [22]
Belle 0.293 ± 0.038 ± 0.015 1.8σ 2015 Hadronic τ → ℓντ νℓ [24]
Belle 0.270 ± 0.035±+0.028−0.025 0.4 σ 2017 Hadronic τ → πντ [4]τ → ρν
τ
Belle 0.283 ± 0.018 ± 0.014 1.1σ 2020 SL τ → ℓντ νℓ [25]
LHCb 0.281 ± 0.018 ± 0.024 0.9σ 2023 - τ → µντ νµ [26]
LHCb 0.267 ± 0.012 ± 0.019 0.7σ 2023 - τ → πππντ [27]
Belle II 0.262 ±+0.041−0.039 ±+0.035−0.032 0.2σ 2024 Hadronic τ → ℓντ νℓ [28]
a LHCb 0.402 ± 0.081 ± 0.085 1.3σ 2024 - τ → ℓντ νℓ [29]
τ → πππντ
Belle II 0.306 ± 0.034 ± 0.018 1.3σ 2025 acsl τ → ℓντ νℓ [30]
0.1 0.2 0.3 0.4
```
R(D*)
```
BaBar, had. tag0.018±0.024±0.332
, had. tagaBelle 0.015±0.038±0.293
```
, (hadronic tau)bBelle 0.027±0.035±0.270
```
, sl.tagcBelle 0.014±0.018±0.283
aLHCb 0.024±0.018±0.281
```
, (hadronic tau)bLHCb 0.020±0.012±0.267
```
, had.tagaBelle II 0.031±0.040±0.267
cLHCb 0.085±0.081±0.402
, sl.tagbBelle II 0.018±0.034±0.306
Average0.012±0.288
SM average0.005±0.254
```
EPJC 80 (2020) 2, 740.006±0.247
```
```
PRD 106 (2022) 0960150.003±0.249
```
```
JHEP 01 (2024) 0220.012±0.258
```
```
PRL 123 (2019) 9,0918010.005±0.253
```
```
PLB 795 (2019) 3860.007±0.254
```
```
EPJC 84 (2024) 4000.009±0.262 HFLAV
```
Spring 2025
Figure 2: Recent experimental results and theoretical predictions from HFLAV [23]
11
𝜈𝜏
|𝑝𝜏|
𝜈𝜏-rest frame 𝜏-rest frame
𝜈𝜏
in the rest frame of the τ − ¯ντ system and in the rest frame of τ .
```
(GeV)ECLE
```
1 1.2 1.4
hel
1 0 10
200
400
600
800
```
Events / (1.0)
```
1000
cosθhel
Fake D* and q q
Data
```
R(D*)
```
0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45
```
(D*)τ
```
P
2−
1.5−
1−
0.5−
0
0.5
1
1.52χ
∆
0
1
2
3
4
```
) and Pτ (D∗) measurement using hadronic τ decays. (left) Fit result projected to
```
```
) Comparison of our result (star for the best-fit value and 1 σ, 2σ, 3σ contours)
```
he shaded vertical band shows the world average without this result.
Figure 3: Unique experimental result of the Pτ in B semitauonic decays by Belle. The
```
result is presented in contour with the measured value of R(D∗) in the same event topology
```
and with the same dataset. [4]
12
3 Datasets and software141
The following section outlines the software and the simulated and experimental data that142
```
are used for the analysis. Extracting the R(D∗) ratio and the Pτ requires a series of oper-143
```
ations on the data, namely, reconstructing the decays of interest, correcting the simulated144
data with respect to the experimental data, developing a statistical inference model to145
extract information from the experimental data, and understanding the complicated cor-146
relations at play in order to assign consistent systematic uncertainties. Therefore a brief147
overview of the main software utilized throughout the different steps of the analysis is148
presented below. Furthermore a description of the official simulated and experimental149
data is provided.150
3.1 Software151
In what follow we describe the main software that is used for the analysis.152
3.1.1 basf2153
```
The Belle II Analysis Software Framework (basf2) is a software developed by the Belle II154
```
collaboration to carry out several tasks across the data processing chain [31]. For the anal-155
ysis described in this document, only the high-level features of the software are required.156
```
These high-level features allow the user to build Final State Particle (FSP) candidates157
```
from tracks and clusters in the detector. These FSP candidates are then combined into158
composite particles, e.g., B mesons. A set of different algorithms performs various tasks159
```
such as building the Rest of Event (ROE), i.e. collecting all the tracks and clusters that160
```
```
do not belong to the particle of interest like the Υ (4S) resonance, vertex fitting, B-meson161
```
tagging, suppressing light quark processes, which we term as continuum, etc. Throughout162
the analysis, the light release light-2403-persian of basf2 is used. [32]163
3.1.2 rdstar1prong164
For the purposes of this analysis we have developed a python library based on basf2.165
The library firstly wraps the reconstruction code around basf2. Secondly it implements166
all the functionalities necessary to perform a post-basf2 reconstruction which we term167
offline processing. This includes the calculation of several quantities outside of basf2.168
It also enables the extraction of generator level information of the decay termed truth169
matching, useful for the identification of different decay processes in simulated data. It170
also applies all the necessary corrections on simulated data, and selects sub samples of the171
dataset that basf2 outputs in order to define of kinematic regions enriched in signal or172
other background processes. Lastly it implements the plotting code necessary to visualize173
our findings. All the figures illustrating information extracted from simulated and exper-174
imental data are produced with the rdstar1prong library unless stated otherwise. Most175
importantly the rdstar1prong library implements a task pipeline around the b2luigi176
software [33] that automates the basf2 reconstruction and the offline processing. The177
programming language that we use in the rdstar1prong library is python and the code178
lives in a gitlab repository [34].179
13
3.1.3 pyhf180
When presented with a dataset comprising of a mixture of different physical processes,181
inferring the number of events coming from a particular one requires the design of a182
statistical model that compares the measured data to the theoretical expectations. In183
cases that the underlying observable distributions cannot be expressed analytically, it184
is a common practice to build non-parametric functions from simulated data. Such an185
```
approach is termed as a Monte Carlo (MC)-template fit [35]. In this analysis no parametric186
```
functions that describe the signal extraction observables can be easily found, therefore,187
we also adopt such a strategy.188
In order to perform a binned maximum likelihood MC-template fit we use the pyhf189
library [9], [10]. pyhf provides a python implementation of the HistFactory method190
```
[36] which has been well established in Large Hadron Collider (LHC) experiments. The191
```
HistFactory method provides as set of tools to build complex statistical models, in the192
form of a likelihood function. Such models are built from non parametric probability193
density functions, which have been derived by histogramming simulated data. It also194
allows the user to introduce systematic uncertainties and correlate those across different195
reconstruction channels and templates. A more detailed explanation of the HistFactory196
method can be found in [36].197
We choose to use pyhf as our fitting framework as it is currently the state-of-the-art198
```
fitting software in the python ecosystem of the High Energy Physics (HEP) community.199
```
The software is well tested and documented and the increasing community spans across200
different experiments. Furthermore publishing the full likelihood model that is used to201
derive an experimental result is technically trivial in pyhf. This is something that the202
theory and the statistics communities have been persistently advocating for [37], as it203
simplifies the theoretical reinterpretation of a result, enables the combination of different204
measurements etc. [38].205
In the following we introduce some nomenclature that stems from the HistFactory206
method and is established across the pyhf community. We only present the minimum207
information necessary to follow the statistical inference part described in 6 and the system-208
atic uncertainties in ??. For a more detailed discussion the reader is referred to [9], [10],209
[36]. pyhf uses a JSON data format to define the statistical model in a declarative way.210
The contents of such a JSON file constitute a pyhf workspace. pyhf allows to perform si-211
multaneous fits across different reconstruction channels. Usage of the iminuit minimizer212
[39], the scipy minimizer [40] or a combination of both is possible. pyhf is implementing213
nuisance parameters to model systematic uncertainties in a source-wise fashion. That is,214
every template, or sample, undergoes modifications through modifiers which implement215
different constraint terms and different correlations across channels or samples. For a full216
list of the available modifications in pyhf we point the reader to [9], [10], [36]. In Table217
2 we present the modifiers that are used throughout the analysis under consideration.218
pyhf allows to fully correlate systematic uncertainties across different samples, mean-219
ing that the same nuisance parameter can be used across different templates with the220
only thing changing being the error amplitude in the respective template. As it is clear221
from Table 2 pyhf also allows to fully correlate systematics across all bins. However in222
certain cases, arbitrary correlations with coefficients between zero and one might need to223
14
Table 2: List of pyhf modifier used in this analysis. All the above modifier are controlled
by a single nuisance parameter. The subscripts stand for: s for sample, c for channel, b
for bin. f and g are functions determined by interpolating the nominal template between
- 1 and −1 sigma. a is an auxiliary measurement and delta is the relative uncertainty of
a template in a particular bin with respect to the total uncertainty.
Modifier Modification Constraint term Input Short description
normfactor - - -
This is a free
unconstrained parameter.
It is primarily used to
determine the yields or
strengths of different
template components.
```
staterror κscb(γb) = γbQb Gauss (aγb = 1| γb, δb) δ2b = Ps δ2sb
```
Implements the lightweight
Barlow-Beeston method [41]
for MC-stat errors.
One nuisance parameter.
per bin is assigned.
The error amplitude.
associated to each template
depends on the relative
contribution to every
particular bin
```
normsys κscb(α) = gp α κscb,α=−1, κscb,α=1 Gauss (a = 0| α, σ = 1) κscb,α=±1
```
Normalization factor.
This accounts for a flat
up or down shift
of the whole template
in all bins.
```
histosys ∆scb(α) = fp α ∆scb,α=−1, ∆scb,α=1 Gauss′s (a = 0| α, σ = 1) ∆scb,α=±1
```
Correlated shape.
Implements a shape
uncertainty, fully correlated
across all bins.
The error amplitudes
depend per bin on the
template variations with
respect to the nominal one .
be deployed. Currently there is no implementation in pyhf that can take into account224
an arbitrary correlation matrix between the different bins of the signal extraction fitted225
variable. However we can achieve the same effect by performing a Principal Compo-226
```
nent Analysis (PCA) in a space defined by the product of the number of reconstruction227
```
channels, templates and bins [42].228
PCA is a statistical technique used for dimensionality reduction, while preserving as229
much of the original information as possible. The main idea is that a set of correlated230
variables are transformed into a smaller number of uncorrelated variables which are called231
principal components. The first principal component describes the direction with the232
largest variability of the data. The second principal component describes the direction233
with the second largest variability of the data orthogonal to the first and so on and so forth.234
Describing each principal component with a histosys modifier is effectively equivalent235
to implementing nuisance parameters with an arbitrary correlation across different bins.236
In the following we describe in more detail how we carry out the PCA for the needs of237
this analysis.238
15
3.1.4 SysVar239
We have developed the SysVar software library [43] in order to treat the systematic240
uncertainties of the analysis in a consistent fashion. Performing a PCA in the context of241
a template-fit requires:242
1. computing a covariance matrix across all reconstruction channels, templates and243
bins.244
2. performing the eigendecomposition of this matrix245
3. determining the necessary number of principal components to describe the original246
correlation247
An excellent explanation of such a procedure in a Belle II analysis that uses pyhf has248
```
already been given in [44] (Belle II internal) In the following we try to reiterate the most249
```
important points.250
The covariance between the bins of the signal extraction variable, associated with a251
particular source of systematic uncertainty can be expressed as252
```
Cijsyst =
```
NvX
```
v=1
```
NcX
```
c=1
```
NsX
```
s=1
```
```
ΓvcsiΓvcsj (2)253
```
where Γvcsi describes the variation v of bin i in template s in reconstruction channel c,254
with respect to the bin content of the nominal histogram, due to a particular systematic255
source. The various variations v are typically drawn from distributions that are normally256
distributed around the nominal correction event weights. Building the full covariance257
matrix becomes trivial by extending Eq. 2 to all bins. Then the covariance matrix can258
be decomposed into its principal components as259
```
Csyst = V U V T = (V
```
√
```
U )(V
```
√
```
U )T = Γ′Γ′T (3)260
```
where V is a matrix describing the eigenvectors and U is the diagonalized matrix with261
the eigenvalues. Now the eigenvariation is defined as262
Γ′= V
√
```
U (4)263
```
A covariance matrix C′syst can be computed using the eigenvariations from Eq. 4264
plugged in Eq. 2. If all the eigenvariations are considered then the original covariance265
matrix Csyst and the new one from the eigendecomposition C′syst are completely identical.266
Thankfully it is observed empirically that only a handful of orthogonal principal compo-267
nents are necessary to describe the original covariance matrix to a, subjectively defined,268
acceptable precision. This significantly reduces the number of nuisance parameters that269
are needed to be implemented in the signal extraction fit e.g. in pyhf.270
With all the above in mind we have developed SysVar which carries out the following271
```
tasks:272
```
1. Applying corrections to a MC dataframe273
16
2. Generating variations of the Data/MC corrections274
3. Histogramming simulated and experimental data to create the nominal templates275
for the fit.276
4. Producing eigenvariations in the space of reconstruction channels, templates, bins.277
5. Determining the number of necessary eigendirections to be implemented in the fit.278
6. Saving the nominal templates and the eigenvariations of it in a format that the can279
be used to build a statistical model in pyhf280
```
For a more detailed discussion the reader should refer to Appendix A, [45] (technical281
```
```
talk at the analysis tools meeting), [46] (recommendations talk for end users at the (S)L282
```
```
working group meeting). Furthermore [47] outlines new gateways that are opening for283
```
measurement combinations with SysVar.284
3.1.5 cabinetry285
We use the cabinetry python library to define pyhf workspaces in a very intuitive and286
```
declarative way [48]. One needs to define the Parameter Of Interest (POI)s, the input data287
```
or histograms, the reconstruction channels, the templates and the systematics that have to288
be considered in a YAML format. cabinetry then used the YAML files to read the data289
and create the pyhf workspace. It also provides a visualization module that helps the user290
to debug the statistical model during development and enables high level visualization of291
the results. For all the plots that we have generated through the cabinetry API we add292
a respective note in the caption in the rest of the document.293
3.1.6 HAMMER294
The simulated data produced by the Belle II experiment assumes certain FF parametriza-295
tions for hadronic decays. Even if the state-of-the-art FF models are used at the time of296
the generation of the simulated data, often enough these turn out to be outdated when297
a physics analysis is performed. As described in 2 the FF model and its parametrization298
can alter the decay rates as well as the kinematic and angular distributions of physical299
processes. Therefore the choice of the FF parametrization in the generated simulated data300
may bias the measured result, since non-parametric signal extraction fits make use of the301
MC template method. Reproducing MC samples with a different FF parametrizations in302
order to study such biases is computationally unsustainable for the large samples that are303
required for B-semileptonic analyses.304
```
We use the Helicity Amplitute Module for Matrix Element Reweighting (HAMMER)305
```
software [49] to get a handle on the FF parametrization that is used throughout the306
analysis. The HAMMER software library provides an interface that allows the reweighing307
of a dataset from an assumed FF parametrization to a target one, implemented as event308
weights circumventing the need to reproduce large MC samples. The event weights can309
then be included when building the template histograms. Such an approach accounts for310
the alteration of efficiencies or acceptances that may arise from the usage of different FF311
17
parametrizations. For a more detailed description of the HAMMER software we refer the312
reader to [50]313
3.2 Simulation Datasets314
3.2.1 FEI skims315
In order to avoid using unnecessary computational resources we analyze simulated and316
experimental data skimmed with the hadronic FEI algorithm [5] The FEI is B-tagging317
algorithm implemented in basf2. The FEI utilizes an array of Boosted Decision Tree318
```
(BDT)s to reconstruct B-meson candidates in a hierarchical manner starting from tracks319
```
and clusters. Subsequently in FSPs and composite particles are reconstructed in six320
distinct steps. These can be see in Figure 4.3213
ay channels further complicate the re-
d require tight selection criteria.
ic tagging considers only semileptonic
B ! D ⇤ `⌫ decay channels [3, Section
presence of a high-momentum lepton
nels can be easily identified and the
gging usually yields a higher tag-side ef-
ed to hadronic tagging due to the large
anching fractions. On the other hand,
c tag will miss kinematic information
no in the final state of the decay.
le is not as pure as in the hadronic
, the FEI provides a hadronic and semilep-±
and B 0 mesons. This enables the mea-
usive decays with several neutrinos and
. In both cases the FEI provides an ex-
cay chain with an associated probabil-
thm follows a hierarchical approach with
lized in Figure 2. Final-state parti-
re constructed using the reconstructed
ers, and combined to intermediate par-
al B candidates are formed. The prob-
ndidate to be correct is estimated by
lassifier. A multivariate classifier maps
```
ures (e.g. the four-momentum or the
```
to a real-valued output, which can be
robability estimate. The multivariate
nstructed by optimizing a loss-function
```
ssification rate) on Monte Carlo simu-
```
ents and are described later in detail.
e algorithm are configurable. There-
annels used, the cuts employed, the
ut features, and hyper-parameters of
e classifiers depend on the configuration.
description of the algorithm and the
ation can be found in Keck [ 4] and in
give a brief overview over the key as-
ithm.
n of Candidates
Tracks Displaced Vertices Neutral Clusters
⇡0
K0L
K0S
⇡ +e + µ + K+  
D⇤0 D⇤+ D⇤s
B0 B+
D0 D+ Ds
J/
K0S
Fig. 2: Schematic overview of the FEI. The algorithm
operates on objects identified by the reconstruction
software of the Belle II detectors: charged tracks, neu-
tral clusters and displaced vertices. In six distinct
stages, these basics objects are interpreted as final-state
```
particles (e + , µ + , K + , ⇡ + , K 0L ,   ) combined to form in-
```
```
termediate particles (J/ , ⇡ 0 , K 0S , D, D ⇤ ) and finally
```
form the tag-side B mesons.
to create a ⇡ + candidate can originate from a pion
```
traversing the detector (signal), from a kaon traversing
```
```
the detector (background) or originates from a random
```
```
combination of hits from beam-background (also back-
```
```
ground).
```
All candidates available at this stage are combined
to intermediate particle candidates in the subsequent
stages, until candidates for the desired B mesons are
created. Each intermediate particle has multiple possi-
ble decay channels, which can be used to create valid
candidates. For instance, a B   candidate can be created
by combining a D 0 and a ⇡   candidate, or by combin-
ing a D 0 , a ⇡   and a ⇡ 0 candidate. The D 0 candidate
could be created from a K   and a ⇡ + , or from a K 0S
and a ⇡ 0 .
The FEI reconstructs more than 100 explicit decay
```
channels, leading to O(10000) distinct decay chains.
```
2.2 Multivariate Classification
The FEI employs multivariate classifiers to estimate the
probability of each candidate to be correct, which can
Figure 4: Overview of the FEI hierarchical reconstruction approach. At first step clusters
and tracks are used to form finals state particle candidates. These are given as input to
subsequent BDTs in order to build composite particle candidates until a valid B-meson
candidate is formed.
The FEI skim selects applies event-wise selections to ensure that B-meson candidates322
in the tag side can be reconstructed [51]. It later reconstructs B-meson candidates and323
```
performs a Best Candidate Selection (BCS) retaining the first twenty best candidates324
```
based on the signal probability. The FEI skim selections are outlined in Table 3325
Unless stated otherwise all the simulated and experimental data mentioned in the326
```
document have been centrally FEI skimmed by the Belle II Data Production (DP) group327
```
[52].328
3.2.2 Generic MC329
For the nominal version of the analysis we use the official generic MC15rd generated by330
the DP group [52].331
The amount of MC15rd available is less by roughly a factor of two compared to MC15ri332
which however comes with the advantage of better modeling of the beam conditions,333
18
Table 3: Pre-selection cuts of the FEI skim.
Category Cuts
```
CleanedTrackCuts abs(z0) < 2.0 and abs(d0) < 0.5 and pt > 0.1
```
CleanedClusterCuts E > 0.1 and 0.296706 < theta < 2.61799
EventCuts nCleanedTracks >= 3
and nCleanedECLClusters >= 3
and visibleEnergyOfEventCMS > 4
B-meson Cuts Mbc > 5.2 GeV
|∆E| < 0.3 GeV
```
signal probability > 0.001 (omitted for decay mode 23)
```
BCS 20 candidates with highest signal probability
therefore better Data/MC agreement in certain quantities. The luminosity used per334
production and per sample for the generic MC15rd campaign can be see in Table 4.335
Table 4: Luminosity for different samples in the Generic MC for MC15rd
```
Data Processing Sample Luminosity ( fb−1)
```
proc13 exp 7-18
mixed 744.764
charged 744.764
ccbar 744.764
ssbar 744.764
uubar 744.764
ddbar 744.764
prompt exp 20-26
mixed 699.235
charged 699.235
ccbar 699.235
ssbar 699.235
uubar 699.235
ddbar 699.235
3.2.3 Gap modes336
The experimentally measured BF of inclusive B → Xcℓν decays does not agree with the337
sum of the BFs measured in exclusive modes [53]. This mismatch is commonly referred to338
as the gap. To address this gap several non-resonant decay modes that might contribute,339
but have never been experimentally measured, have been added to the Belle II generic MC.340
```
The non-resonant decays include B → D(∗)ππν and B → D(∗)ην final states. However341
```
such non-resonant multi-body decays result in a much softer momentum spectrum for the342
lepton, which as observed in previous Belle II analyses is not representative of the observed343
experimental data [54]. To resolve this issue it has become standard practice within344
19
Belle II to replace these final states with a dedicated signal MC production containing345
modes produced through one of the excited D∗∗ resonances. A detailed discussion on the346
matter can be found in [55].347
Since the DP group provides us only the number of generated events, we have to348
calculate the luminosity ourselves. This is because the assumed BFs for the gap modes are349
only educated guesses, and their estimation depends on new experimental and theoretical350
results. The usual luminosity equation L = Neventsσ holds here, which transforms into351
Equation 5.352
```
L =
```
Nevents
2 × NBB × Nleptons × f × BF
```
(5)353
```
where the factor 2 comes from the fact that we can have two B mesons in the event,354
both of which can decay into the final state of interest. NBB is the number of BB355
pairs assumed per 100 fb−1. Nleptons accounts for the fact that the gap samples are not356
generated separately for the two light lepton generations. An extra factor f needs to be357
added as multiple resonances can contribute to the same final state. The assumed BFs358
for the gap modes are taken from the latest HFLAV averages [3]359
All the above information for the light lepton gap modes are provided in Table 5. NBB360
is assumed to be 5.1 × 104 per fb−1 for B0 and 5.4 × 104 per fb−1 for B+ as per the official361
DECAY.dec file of the Belle II simulated data.362
Table 5: Event types and corresponding decays with number of events and luminosity for
gap modes including light leptons. Nleptons has been set 2 in Eq 5 to account for the fact
that the light lepton gap modes are not produced separately. The calculated luminosity
is used to scale the events that survive the full set of event selections to the luminosity of
experimental data.
```
Decay Event Type Prod. Nevents(106) f BF (10−2) L ( fb−1)
```
```
B0 → D′1(Dππ)ℓ− ¯νℓ 1196700001 26218 8 0.5 0.07 ± 0.08 11,204.48
```
```
B0 → D′1(D∗ππ)ℓ− ¯νℓ 1196700002 26222 8 0.5 0.20 ± 0.10 3,921.57
```
```
B0 → D∗0(Dππ)ℓ− ¯νℓ 1196700003 26224 8 0.5 0.07 ± 0.08 11,204.48
```
```
B0 → D∗0(D∗ππ)ℓ− ¯νℓ 1196700004 26228 8 0.5 0.20 ± 0.10 3,921.57
```
```
B0 → D′1(D∗η)ℓ− ¯νℓ 1196708000 26220 8 1.0 0.86 ± 0.19 456.0
```
```
B0 → D∗0(Dη)ℓ− ¯νℓ 1196708001 26226 8 1.0 0.86 ± 0.19 456.0
```
```
B+ → D′1(Dππ)ℓ− ¯νℓ 1296700001 26235 8 0.5 0.07 ± 0.09 10,582.01
```
```
B+ → D′1(D∗ππ)ℓ− ¯νℓ 1296700002 26239 8 0.5 0.22 ± 0.10 3,367.0
```
```
B+ → D∗0(Dππ)ℓ− ¯νℓ 1296700003 26241 8 0.5 0.07 ± 0.09 10,582.01
```
```
B+ → D∗0(D∗ππ)ℓ− ¯νℓ 1296700004 26245 8 0.5 0.22 ± 0.10 3,367.0
```
```
B+ → D′1(D∗η)ℓ− ¯νℓ 1296708000 26237 8 1.0 0.90 ± 0.20 411.52
```
```
B+ → D∗0(Dη)ℓ− ¯νℓ 1296708001 26243 8 1.0 0.90 ± 0.20 411.52
```
We follow a similar procedure for the gap modes that include a τ lepton. However,363
in this case, we must first determine the predicted BF for the semitauonic gap modes, as364
they are not provided in the latest averages by HFLAV [3]. To achieve this, we start with365
```
the BFs of the gap modes involving a light lepton and the predicted averages for R(D(∗))366
```
```
from [3]. We then incorporate the predicted R(Hc) ratios from [56] to calculate the BFs367
```
20
of the corresponding semitauonic decays, where Hc represents the excited D mesons. For368
the non-resonant modes, since these are in the end produced via an excited resonance in369
the MC, we apply the same ratio used for the experimentally measured modes involving370
excited D mesons. All the above information is summarize in Table 6.371
```
Table 6: Latest values of BFs for the light lepton B → Hcℓν decays and R(Hc) ratios.
```
```
The BF of the semitauonic modes is calculated using R(Hc) = B→Hcτ νB→Hcℓν
```
```
hadronic system B(B → Hcℓν) (%) R(Hc) B(B → Hcτ ν) (%)(measured) (prediction) (prediction)
```
B0 B± B0/B± B0 B±
D 2.11 ± 0.05 [3] 2.27 ± 0.06 [3] 0.296 ± 0.06 [3] 0.62 ± 0.02 0.67 ± 0.02
D∗ 4.90 ± 0.11 [3] 5.27 ± 0.12 [3] 0.254 ± 0.005 [3] 1.24 ± 0.04 1.34 ± 0.04
D∗0 0.12 ± 0.26[3] 0.13 ± 0.19[3] 0.08 ± 0.03 [56] 0.0096 ± 0.0211 0.0104 ± 0.0235
D′1 0.26 ± 0.04 [3] 0.28 ± 0.04 [3] 0.05 ± 0.02 [56] 0.013 ± 0.0056 0.014 ± 0.0059
D∗1 0.59 ± 0.10 [3] 0.64 ± 0.10 [3] 0.10 ± 0.02 [56] 0.059 ± 0.015 0.064 ± 0.016
D∗2 0.299 ± 0.027 [3] 0.321 ± 0.029 [3] 0.07 ± 0.01 [56] 0.021 ± 0.0035 0.022 ± 0.0038
```
P D(∗,∗∗) 8.23 ± 0.17 8.86 ± 0.18 - 1.968 ± 0.044 2.117 ± 0.048
```
Xc 10.27 ± 0.15 [3] 10.99 ± 0.16 [3] 1 0.223 ± 0.005 [56] 2.290 ± 0.061 2.451 ± 0.066
```
D π π (via D′1) 0.07 ± 0.08 [3] 0.07 ± 0.09 [3] -
```
0.3221 ± 0.0756 0.3335 ± 0.0816D
```
∗ π π (via D∗0 ) 0.20 ± 0.10 [3] 0.22 ± 0.10 [3] -
```
```
D∗ η (via D′1) 0.86 ± 0.19 [3] 0.90 ± 0.20 [3] -
```
```
D η (via D∗0 ) 0.86 ± 0.19 [3] 0.90 ± 0.20 [3] -
```
To calculate the luminosity corresponding to the semitauonic gap MC samples, we372
use Equation 5 once again. The value of NBB remains unchanged from the case of gap373
modes involving light leptons, as it corresponds to generic MC. For Nleptons, we set it to374
1, since the τ lepton samples are generated separately. Additionally, the extra factor f is375
assigned a value of 1. This is because, in the production of semitauonic gap modes, which376
```
followed the one for the light lepton modes, the B → D(∗)ππν decays are merged into a377
```
single resonance. The decision to merge them stems from the realization that the 50-50378
split assumed for the light modes was arbitrary and introduced unnecessary technical379
```
complexity (for more details, see the corresponding PR [57]). The calculated BFs and the380
```
corresponding luminosity are presented in Table 7.381
3.3 Experimental data382
We use the LS1 dataset acquired by the Belle II detector between 2019-2023. In the383
following we outline the different collision energies, data processing, and luminosity of the384
experimental data.385
1We have excluded D+s K and D+s K∗ from the inclusive calculation
21
Table 7: Event types and corresponding decays with number of events and luminosity for
gap semitauonic modes. The calculated luminosity is used to scale the events that survive
the full set of event selections to the luminosity of experimental data.
```
Decay Event Type Prod. Nevents(106) f BF (10−2) L ( fb−1)
```
```
B0 → D′1(Dππ)τ − ¯ντ 1196300001 28067 3 1/8
```
0.3221 ± 0.0756
24,350.01
```
B0 → D∗0(D∗ππ)τ − ¯ντ 1196300004 28068 3 3/8 73,050.02
```
```
B0 → D′1(D∗η)τ − ¯ντ 1196308000 28069 3 3/8 73,050.02
```
```
B0 → D∗0(Dη)τ − ¯ντ 1196308001 28070 3 1/8 24,350.01
```
```
B+ → D′1(Dππ)τ − ¯ντ 1296300001 28072 3 1/8
```
0.3335 ± 0.0816
23,517.65
```
B+ → D∗0(D∗ππ)τ − ¯ντ 1296300004 28073 3 3/8 70,552.96
```
```
B+ → D′1(D∗η)τ − ¯ντ 1296308000 28074 3 3/8 70,552.96
```
```
B+ → D∗0(Dη)τ − ¯ντ 1296308001 28075 3 1/8 23,517.65
```
```
3.3.1 Experimental data Υ (4S)386
```
We use the on resonance data to reconstruct the signal processes of interest. The total387
luminosity that correspond to the on resonance LS1 dataset is 365.29 ± 1.70 fb−1 as per388
the calculation of the Data Production group [52]. This dataset contains the officially389
```
reprocessed data (proc) and data that a revision of the processing strategy might occur390
```
```
in the future (buckets). An overview of the different experiments and the corresponding391
```
luminosity for on resonance data can be found in Table 8.392
Table 8: Experiment Offline Luminosity for 4S
```
Experiment Processing Offline Luminosity (fb−1)
```
26 bucket35-bucket36 54.795 ± 0.009 ± 0.351
24 bucket30-bucket33 85.642 ± 0.011 ± 0.549
22 bucket28-bucket29 32.060 ± 0.007 ± 0.206
20 bucket26 3.788 ± 0.003 ± 0.025
18
proc13
89.900 ± 0.011 ± 0.576
17 10.715 ± 0.004 ± 0.069
16 10.294 ± 0.004 ± 0.066
14 16.500 ± 0.006 ± 0.106
12 54.373 ± 0.005 ± 0.350
10 3.655 ± 0.002 ± 0.024
8 1.663 ± 0.003 ± 0.011
7 0.506 ± 0.002 ± 0.004
Total
all proc13 & prompt 365.29 ± 1.70 fb−1
22
3.3.2 Off-resonance data393
Off-resonance data is acquired with the Belle II detector at energies less that the Center-394
```
Of-Mass (CoM) energies necessary to produced the Υ (4S) resonance. Therefore this395
```
data sample is rich in q ¯q processes, since the collision energy is not sufficient enough to396
produce a B ¯B pair. The off-resonance sample is a great choice for checking the Data/MC397
modeling of the continuum processes. An overview of the different experiments and the398
corresponding luminosity for off-resonance data can be found in Table 9.399
Table 9: Experiment Offline Luminosity for 4S offres
```
Experiment Processing Offline Luminosity (fb−1)
```
25 bucket35 24.574 ± 0.006 ± 0.158
18
proc13
8.482 ± 0.004 ± 0.055
12 8.691 ± 0.002 ± 0.056
8 0.808 ± 0.001 ± 0.006
Total
all proc13 & prompt 42.556 ± 0.007 ± 0.273
23
4 Online reconstruction400
In the following section we’re outlining the online reconstruction strategy and the offline401
selections we are applying in our analysis.402
4.1 Event signature403
```
The overarching goal of this analysis is to measure R(D∗) in hadronic 1-prong τ decays.404
```
```
Therefore a fully hadronic Final State (FS) is reconstructed on the signal side. Figure 5405
```
illustrates the reconstruction on the signal and tag side.406
```
Y(4S)
```
e- e+
BsigBtag
D*, D
K*, K
π
D*
τ
ν
ν
π,ρ
Figure 5: Illustration of event reconstruction for signal.
We’re using the FEI to reconstruct fully hadronic states on the tag side. On the signal407
side we’re building D∗ candidates by combining D0 candidates with charged or neutral408
slow pions. We then combine the D∗ candidates with one charged pion or one charged pion409
and one neutral pion to reconstruct signal B-meson candidates. The latter one facilitates410
the reconstruction of τ → ρντ candidates, since the ρ+ meson decays almost exclusively in411
this mode. Since the τ lepton decays into a charged particle and one undetectable neutrino412
in the decays modes of interest, it is not necessary to reconstruct the τ lepton explicitly.413
The two τ decay modes considered here account for ≃ 36.31 % of the total BF of the414
τ lepton, as illustrated in Figure 6. The relatively large BF is however counterbalanced415
by experimental challenges. Such a fully hadronic FS is susceptible to a large number416
of different hadronic backgrounds that can imitate the signal. This is contrary to the417
leptonic τ decays where only a handful of background processes such as B → D∗∗ℓν may418
imitate the intended mode of reconstruction.419
```
For the normalization mode which appears in the denominator of R(D∗) we combine420
```
the D∗ candidates with a light lepton i.e. an electron or a muon.421
In the rest of this section we describe in detail the reconstruction steps and all the422
selections applied in basf2 online reconstruction.423
24
Figure 6: Overview of τ lepton BFs
4.2 Global tags424
At the beginning of our steering file we use the following global tags to align with the425
recommendations of the Performance group.426
Table 10: Global tags used in the steering file. The names of the global tags are used as
input to the basf2 helper function b2.conditions.prepend globaltag
```
ma.getAnalysisGlobaltag()
```
analysis tools light-2305-korat
analysis tools light-2403-persian
data beam conditions proc13prompt
tracking data Moriond23 v1
neutrals 2024
```
Legacy CollisionAxisCMS (only for gap samples)
```
leptonid official rel6 mc15rd
chargedpidmva rel6 v5
4.3 Event-wise selection427
As mentioned already in Section 3.2.1 we use the hadronic FEI skims. A pre-selection428
of events is carried out by the skim to ensure that the reconstruction of hadronic Btag429
candidates is possible. These selections have been oulined already in Table 3. These430
selections exclude events where there are insufficient particle candidates to reconstruct at431
least one hadronic B meson decay. [51] We do not apply any futher event-level filtering432
of the events.433
25
4.4 Tag side reconstruction434
The first step after the event preselection is to select suitable Btag candidates. We load435
the B0:feiHadronic and B+:feiHadronic ParticleLists provided by the FEI skim. We436
first suppress continuum events. To that end we reconstruct an ROE against the Btag437
candidates from the skim. We will refer to this ROE as BtagROE . The tracks and clusters438
that are considered for the construction of the BtagROE are summarized in Table 11439
Table 11: Selections for tracks and cluster considered in the BtagROE
tracks
| dr | < 2 cm
| dz | < 4 cm
pT > 0.2 GeV
```
thetaInCDCAcceptance == 1
```
clusters
clusterNHits > 1.5
```
((clusterReg==1 and E > 0.080 GeV) or
```
```
(clusterReg==2 and E > 0.030 GeV) or
```
```
(clusterReg==3 and E > 0.060 GeV))
```
0.2967 < clusterTheta < 2.6180
| clusterTiming | < 200 ns
Once the BtagROE is build we retain only candidates whose cosTBTO is smaller than 0.9.440
cosTBTO is the cosine of the angle between the thrust axis of the Btag and the thrust441
axis of BtagROE . Such a variable provides discrimination power between B ¯B and q ¯q events442
as the latter have a more jet like event shape. That is contrary to the former where443
the momentum is distributed more spherically because of the small available kinematic444
```
phase-space, between the mass of the Υ (4S) and the sum of the masses of the two B445
```
mesons.446
We then keep only Btag candidates whose Mbc is larger than 5.272 GeV and ∆E447
between -0.150 and 0.100 GeV. These last two selections are commonly used for Btag448
candidates in Belle II analyses. For a definition of Mbc and ∆E the reader is referred to449
[2].450
Lastly we keep only one Btag candidate based on the SignalProbability i.e. the451
output BDT score of the FEI algorithm. We keep only one Btag candidate before re-452
constructing the Bsig meson in an attempt to keep the Btag and Bsig reconstruction453
efficiencies as factorizable as possible. This effect has been very nicely illustrated in this454
Belle II Physics week talk [58]. The factorizability of these efficiencies becomes crucial455
```
at a later stage of the analysis. When measuring ratios like R(D∗), the assumption is456
```
that most efficiencies not dependent on the Bsig will cancel out. By selecting the Btag457
candidate completely independently of the Bsig, we are following the safest approach to458
avoid mingling the two efficiencies.459
If no Btag candidate survives the process described above, we skip the event in order460
to avoid wasting CPU time.461
26
4.5 Final state particles462
After having selected a single Btag candidate we proceed with reconstructing FSPs that463
will be used for Bsig.464
4.5.1 Photons465
All the photon candidates we select are later used to reconstruct π0 candidates. Since466
the π0 candidates are divided in two categories i.e. normal π0 with p > 0.2 GeV and soft467
π0 with p < 0.2, we collect photons in two ParticleLists. The first ParticleList is used468
for the normal π0. In this case the cluster selection criteria that we apply for the photon469
candidates are identical to the ones prescribed from the π0 eff40 list recommendations470
from the Neutrals Group [59]. For the soft photons we use the π0 eff50 recommendations471
[59] but we additionally require | clusterTiming | < 200 ns and an extra selection on a472
combination of minC2Dist and clusterZernikeMVA for the three different ECL regions as473
outlined in Table 14. The extra cuts are aligned with the ones used for the determination474
of Data/MC ratios for soft π0 specifically [60].475
4.5.2 Leptons476
For electrons and muons we follow the recommendations of the Lepton IDentification477
```
(LID) group [61]. We first require that the lepton candidates satisfy | dr | < 2 cm and |478
```
dz | < 4 cm. We then profit by the predefined std.Charged lists in basf2 [32] and the479
options we are using are summarized in Table 12480
Table 12: LID selection criteria
e µ
working point FixedThresh09 FixedThresh09
method bdt likelihood
classification global global
lid weights gt leptonid official rel6 mc15rd leptonid official rel6 mc15rd
release 6 6
brems angleThreshold 0.2 -
4.5.3 Charged hadrons481
For charged hadrons i.e. pions and kaons we again require that the track candidates satisfy482
| dr | < 2 cm and | dz | < 4 cm. We then discard track candidates with less than 20 hits in483
```
the CDC to ensure high performance on Hadron IDentification (HID) [62]. Lastly we use484
```
the global PID variables of basf2 based on the likelihood method and apply pionID>0.1485
for pions and kaonID>0.1 for kaons.486
27
4.6 Composite particles487
After having selected the FSP we then combine those to form composite particle candi-488
dates.489
4.6.1 π0490
As already mentioned in ?? we reconstruct π0 candidates using the π0 eff40 recommenda-491
tions. As its name indicates this set of selections target an overall reconstruction efficiency492
of 40% for π0 candidates. For normal π0 we apply a mass window on the invariant mass493
of the candidate between 0.120 and 0.145 GeV, as prescribed by the recommendations of494
the Neutrals Group. For soft π0 this invariant mass range is relaxed to a range or 0.105495
and 0.150 GeV. For both lists we accept only candidates that have a non-failing vertex496
fit using the kFit algorithm with an additional mass constrain on the mass of the π0.497
4.6.2 K0S498
We reconstruct K0S candidates using the predefined helper function stdKshorts from the499
stdV0s module in basf2. stdKshorts combines two oppositely charged pions into a500
K0S candidate by. Only candidates that survive a vertex fit and with an invariant mass501
between 0.450 and 0.550 GeV are kept [63]. We additionally apply as set of selections502
```
adopted from a previous R(D∗) analysis at Belle II [64]. These selections require that503
```
the flightDistance and the logarithm of the significanceOfDistance are positive.504
Additionally the cosinus of the angle between the momentum and the vertex vector has505
to be larger than 0.8.506
4.6.3 ρ507
We combine a charged and a neutral pion into ρ candidates. These are only used for the508
τ decay of the signal. We require that the invariant mass of the pair of pions is between509
0.560 and 1.060 GeV.510
4.6.4 Charmed mesons511
We present the reconstruction modes of D∗ and D0 in Table 13 along with their BFs taken512
from [7]. The charge conjugate reconstruction is implied in the rest of the document unless513
stated otherwise. We avoid reconstructing decay modes with two π0 as empirically we514
have observed that these are very noisy. A longer discussion on our final choice of D0515
reconstruction modes is given in Appendix I.516
For the D0 meson candidates we require a loose mass window between 1.78 and 1.90517
GeV. After combining the D0 candidates with a soft pion we require that the mass518
difference between the D∗ and the D0 candidates is between 0.130 and 0.170 GeV for519
D∗± and between 0.100 and 0.170 for D∗0. Since the reconstruction of the latter includes520
a soft pion we expect a worse resolution, hence the looser mass difference window. The521
difference between the two invariant masses is preferred over the invariant mass of the D∗522
alone, as systematic effects present in both reconstructions cancel out in the subtraction,523
```
making the peak in ∆M(D∗) more prominent. We also require that the momentum of524
```
28
Table 13: Charmed meson reconstruction modes
```
Decay mode BF (%)
```
D∗+ → D0 π+ 67.7 ± 0.5
D∗0 → D0 π0 64.7 ± 0.9
D0 → K−π+ 3.95 ± 0.03
D0 → K0S π0 1.24 ± 0.02
D0 → K−π+π0 14.40 ± 0.60
D0 → K0S π+π− 2.80 ± 0.18
D0 → K0S K+K− 0.44 ± 0.03
D0 → K−π+π−π+ 8.22 ± 0.14
all D∗ candidates is less than 2.5 GeV as this suppresses continuum events, candidates525
originating from ccbar events in particular.526
4.6.5 B meson candidates527
We combine the D∗ candidates with either a charged pion, a charged rho or a lepton to528
reconstruct the two tauonic signal modes, or the normalization mode respectively. We529
also add an extra reconstruction channel by combining D∗ candidates with a light lepton530
and a pion, which defines a CR, enriched in B → D∗∗ℓν decays. The only requirement on531
the Bsig candidates whose vertex fit did not fail are kept.532
```
4.7 Υ (4S) and Rest of Event533
```
```
We lastly combine the two B meson into an Υ (4S) candidate. We take into account the534
```
charge allowed combinations i.e. B0 B0 and B+ B−. For the neutral B mesons we also535
considered charge combinations which are not allowed i.e. B0 B0 and its charge conjugate.536
We assume that any flavor inference inconsistencies will not affect the measurement of537
```
R(D∗), but they will increase the available statistics. We define the ROE with respect to538
```
```
the Υ (4S) candidate. Only tracks and clusters that satisfy the selections of Table 15 are539
```
taken into account.540
```
We keep only Υ (4S) candidates whose ROE contains one or none extra charged tracks.541
```
The latter enables us to kinematically constraint the Bsig decays of interest with missing542
neutrinos, given that the Btag is reconstructed fully in hadronic modes. The sample with543
one extra charged tracks is saved for later sideband checks. All the reconstruction channels544
are summarized in Table 16.545
29
Table 14: Overview of online cuts for building B meson signal candidates
good track
dr < 2 cm and |dz| < 4 cm and nCDCHits > 20
unflavored hadrons
π+ [good track] and pionID > 0.1
π+slow p > 0.05 GeV
K+ [good track] and kaonID > 0.1
π0 pi0:eff40 May2020
π0soft
```
pi0:eff50 May2020 and |clusterTiming| < 200 ns and 0.1183 < Mγγ < 0.147 GeV and p > 0.05 GeV
```
```
(clusterReg == 1 and
```
  minC2Dist
40
2
+
  clusterZernikeMVA
0.7
2
> 1
or clusterReg == 2 and
  minC2Dist
40
2
+
  clusterZernikeMVA
0.4
2
> 1
or clusterReg == 3 and
  minC2Dist
85
2
+
  clusterZernikeMVA
0.2
2
```
> 1)
```
ρ+ 0.560 < Mπ+π0 < 1.060 GeV
leptons
e pidChargedBDTScore > 0.9 and brems angleThreshold:0.2
µ muonID noSVD > 0.9
flavored hadrons
K0S
0.450 < Mπ+π+ < 0.550 GeV and
flightDistance > 0 and
```
and log10(significanceOfDistance) > 0 and
```
cosAngleBetweenMomentumAndVertexVector > 0.8
D0 1.78 < MD0 < 1.90
D∗+ 0.130 < MD∗+ − MD0 < 0.170 GeV and p < 2.5 GeV
D∗0 0.100 < MD∗0 − MD0 < 0.170 GeV and p < 2.5 GeV
Bsig non-failed vertex fit
```
Table 15: Selections for tracks and cluster considered in the ROE against the Υ (4S)
```
candidate
tracks
| dr | < 2 cm
| dz | < 4 cm
```
thetaInCDCAcceptance == 1
```
clusters
clusterNHits > 1.5
```
((clusterReg==1 and E > 0.100 GeV) or
```
```
(clusterReg==2 and E > 0.060 GeV) or
```
```
(clusterReg==3 and E > 0.150 GeV))
```
clusterTheta > 0.2967 and clusterTheta < 2.6180
minC2TDist > 50 cm
30
```
Table 16: Υ (4S) reconstructions modes and decays of interest
```
Reconstruction mode Decay of interest
```
Btag D∗− π+ B0 → D∗− τ +(π+ ντ )ντ
```
```
Btag D∗− π+π0 B0 → D∗− τ +(ρ+ ντ )ντ
```
Btag D∗− e+ B0 → D∗− e+νe
Btag D∗− µ+ B0 → D∗− µ+νµ
```
Btag D∗0 π+ B+ → D∗0 τ +(π+ ντ )ντ
```
```
Btag D∗0 π+π0 B+ → D∗0 τ +(ρ+ ντ )ντ
```
Btag D∗0 e+ B+ → D∗0 e+νe
Btag D∗0 µ+ B+ → D∗0 µ+νµ
31
5 Offline processing546
A series of operations are applied after the online reconstruction. These include truth547
matching of decays in simulated data, kinematic selections that define the signal and548
normalization-enhanced regions, as well as sideband regions used for calibrations and549
Data/MC checks. Additionally, best candidate selection is performed, and various cor-550
rections are applied to simulated data. In the following section, we describe each of these551
steps in detail.552
5.1 Truth-matching553
In the following section we describe the truth-matching strategy. We based our truth554
matching on information that we save from the basf2 software and we later analyze555
offline. The truth matching is based on different modules which we describe below.556
5.1.1 Btag and Bsig557
We first try to identify the Btag meson. In order to do that we employ the mostcommonBTagIndex558
variable of basf2 [32]. This variable matches an arrayIndex, to a Btag FEI candidate.559
The arrayIndex is an internal enumerator for the particles that are generated from the560
```
MC generator. For B mesons originating from the Υ (4S) resonance, the arrayIndex must561
```
be either 1 or 2. The mostcommonBTagIndex determines the arrayIndex by traversing562
down the tree of the Btag FEI candidate. For every reconstructed object in the tree,563
basf2 tries to match this reconstructed object with a generator level particle. Then564
basf2 finds the arrayIndex of the B meson that the MC particle descends from. All565
these arrayIndexs are collected and stored. If no MC particle could be found, or if566
the MC particle does not descend from a B meson -1 is assigned. Out of this col-567
lection of arrayIndexs basf2 determines the most common one and assigns it to the568
mostcommonBTagIndex variable. For the rest of the truth matching purposes we consider569
that this arrayIndex correspond to the true particle in the generator level. Knowing570
the arrayIndex of the matched MC particle to the FEI Btag candidate enables us to571
determine the flavor of the B meson, through other basf2 functionalities. Clearly for all572
continuum events the entry of the mostcommonBTagIndex will always be -1. However we573
do not base the identification of these events on this variable. On the contrary we trace574
back the type of input file that a event originates from. The categories of files are defined575
in Table 23. If the event originates from a ccbar, ssbar, uubar or ddbar input file, then576
we consider this event a continuum event without carrying out any further checks.577
We base the rest of our truth matching on the lepton candidate or τ daughter can-578
didate that originates from the signal B meson candidate. We traverse the decay tree579
of the reconstructed signal B meson, starting from the lepton candidate or τ daughter580
candidate and up to five generations until we find a B meson on the generator level. If581
the arrayIndex of this true B meson is the same as the one we determined from the582
mostcommonBTagIndex, or if no true B meson could be found we consider this signal B583
meson candidate as combinatorial background. No further checks are carried out for com-584
binatorial background candidates. If the arrayIndex of the true B meson ancestor of the585
32
the lepton candidate or τ daughter candidate is different than the mostcommonBTagIndex,586
then we spawn a second layer of truth matching, that tries to identify the true generated587
decay of the B signal candidate. This is described in the following.588
5.1.2 Bsig decay category589
We traverse the B signal candidate tree again until we find the B meson from the same590
starting point as before. We then save the mcPDG of the first six daughters of the true B591
meson. Based on the mcPDG codes of those daughters we make a first rough categorization592
of the decay. The categories are summarized in Table 17.593
Table 17: Main decay truth matching categories. For D∗ both charged and neutral mesons
are considered. For D∗ and D, τ , ell, ν, charge conjugation is taken into account. The
definitions of the PDG codes that are used for D∗∗, Hc, Hgapc , Xgapu/s , Xs, and Xu are given
in Appendix B.
true B daughters
ID True decay 0 1 2 3 4 5
11 B → D∗τ ν D∗ τ ντ γ/NaN γ/NaN γ/NaN
12 B → Dτ ν D τ ντ γ/NaN γ/NaN γ/NaN
21 B → D∗ℓν D∗ ℓ νℓ γ/NaN γ/NaN γ/NaN
22 B → Dℓν D ℓ νℓ γ/NaN γ/NaN γ/NaN
31 B → D∗∗ℓν D∗∗ ℓ/τ νℓ/ντ γ/NaN γ/NaN -
32 B → D∗∗ℓν Hgapc ℓ/τ νℓ/ντ γ/NaN γ/NaN -
33 B → D∗∗ℓν Hgapc Xgapu/s Xgapu/s ℓ/τ νℓ/ντ γ/NaN
44 B → HcHc Hc Hc NaN NaN NaN -
443 B → HcHcXs Hc Hc Xs NaN NaN -
500 B → D∗ + n · hu D∗ Xu/γ/NaN Xu/γ/NaN Xu/γ/NaN Xu/γ/NaN Xu/γ/NaN
5.1.3 D∗594
We do not truth match the decay of the D∗, if this is found in the previous step of the595
truth matching. The reason is that we don’t really care about the reconstruction of the596
D∗, as long as the D∗ and the D candidates can be matched to a MC true particle and they597
both fall into the mass windows that we define in the reconstruction. Our reasoning here598
is that it is very likely that in the D∗ reconstruction the slow pion is misreconstructed,599
or in the D meson one of the daughters was missed, or a wrong particles was added.600
Cross-feeds between the different 8 D modes that we reconstruct are of course possible.601
For the reasons above we still accept such events as signal, without requiring that the D∗602
or the D mesons are correctly reconstructed.603
5.1.4 τ604
If we find a τ particle as a daughter of the B meson i.e. if the truth matched signal B605
meson falls into categories 11 or 12 as defined in Table 17, we then need to truth match606
33
the τ decay. We have observed an issue with the order of the generator level particles in τ607
decays. Event if the decay grammar instructs that the MC particles should be generated608
in mass descending order, a lot of times we truth match τ leptons whose daughters follow609
a random ordering. Another issue is that the decay τ → ρντ is never truth matched. A ρ+610
meson is never found as a descendant of the τ lepton, but the resonance is skipped in favor611
of the daughters of the ρ+ meson. As example we would expect to truth match a τ → ρντ612
but on the contrary we find ourselves truth matching τ → π+π0ντ . Furthermore we613
have found events where the truth matched τ decay is τ → ντ π+π0 or any other possible614
permutation of the τ daughters. The last element that adds an extra complexity to the τ615
truth matching is the presence of radiative photons. Strangely enough the order of those616
appears to be random in many cases in the Belle II MC. For example a τ → ντ π+γπ0617
could also be truth matched. We presume that such pathological cases arise from bugs of618
the TAUOLA MC generator. In order to face these unpredictable complications we have619
developed a dedicated truth matching algorithm for τ decays that considers all possible620
permutations of the τ daughters.621
During the WG review we found that such problems were more prominent in previous622
MC campaings and are not relevant for MC15rd anymore. These problems might have623
been solved by changes in the truth matching modules of basf2 or modification of the624
Nevertheless we still use the same algorithm that we had developed since it’s robust625
against correctly ordered and misordered τ daughters.626
We always consider the first 5 daughters of the τ decay in 15 distinct modes. There are627
presented in Table 18. In order to account for photons coming from Photos we pad the628
target queries for the τ daughters up to 5 daughters, with NaNs and photons. All possible629
combinations of NaNs and photons are considered as well as all possible permutations in630
conjunction with the true daughters of every decay mode.631
Table 18: τ decay truth matching categories. The order of the truth matched daughters
is not important as all possible permutation are considered.
ID True decay Daughters
1 τ → π+ντ [π+, ντ ]
2 τ → π+π0ντ [π+, π0, ντ ]
3 τ → π+π0π0ντ [π+, π0, π0, ντ ]
4 τ → π+π+π−ντ [π+, π+, π−, ντ ]
5 τ → µντ νµ [µ ντ , νµ]
6 τ → eντ νe [e ντ , νe]
7 τ → K+ντ [K+, ντ ]
8 τ → π+K0K0ντ [π+, K0, K0, ντ ]
9 τ → π+π0π0π0ντ [π+, π0, π0, π0, ντ ]
10 τ → π+K∗0, ντ [π+, K∗0, ντ ]
11 τ → π+π+π−π0ντ [π+, π+, π−, π0, ντ ]
12 τ → K+π+π−ντ [K+, π+, π−, ντ ]
13 τ → π+K0ντ [π+, K0, ντ ]
14 τ → K∗+ντ [K∗+, ντ ]
15 τ → π+K0π0ντ [π+, K0, π0, ντ ]
34
5.1.5 Hadronic decays632
In case a hadronic decay is truth matched in the first step i.e. categories 44, 443 or 500633
in Table 17 then we need to further identify the decay. This is important as some of634
the hadronic decays need to be calibrated or their BF need to be corrected. Since there635
is large number of possible hadronic backgrounds it becomes impractical to hard code636
these decays in the same way we do for the τ decays. To tackle this problem we adopt637
a different approach. We truth match all the daughters of the B meson and we create638
string with the absolute values of the PDG code of the B meson itself and the ones of its639
daughters. Before we create the string, we sort the absolute values of the PDG codes of640
the daughters in descending order. This makes our method robust against misorderings641
like the ones that we described for the τ truth matching. It is also true for fully hadronic642
decays that we often truth match the same decay in different orderings of the B meson643
daughters. Empirically we report that is true for decays that include modes that decay644
through complicated resonances. This approach allows us to distinguish all the possible645
hadronic decays that mimic our signal.646
5.1.6 Final truth matched categories647
We combine information from all the above truth matching queries to create final MC648
categories. Table 19 summarizes the final truth matching categories that are used for649
visualization purposes throughout the analysis. All the stacked histogram plots of simu-650
lated and experimental data in this document use the categories as defined in Table 19651
unless stated otherwise.652
Table 19: Final truth matching categories. The entries of the column Bsig mcID are
described in Table 17. The entries of the column τ mcID are described in Table 18.
MC category Bsig mcID τ mcID wrong B meson input file
```
B → D∗τ ν (τ → πντ ) 11 1 False mixed/charged/gap
```
```
B → D∗τ ν (τ → ρντ ) 11 2 False mixed/charged/gap
```
B → D∗ℓν 21 - False mixed/charged/gap
B → D∗∗ℓν 31, 32, 33 - False mixed/charged/gap
B → HcHcXs 44, 443 - False mixed/charged/gap
B → D∗ + n · hu 500 - False mixed/charged/gap
Other B ¯B -1, 12, 22 - False mixed/charged/gap
τ missID 11 not 1 and not 2 False mixed/charged/gap
Combinatorial - - True mixed/charged/gap
Continuum - - - ccbar/ssbar/uubar/ddbar
5.2 Helicity angle calculation653
As mentioned in 1 one of the main objectives of this analysis is to measure Pτ along654
```
R(D∗). Pτ can be defined through the differential decay rate as655
```
1
Γ
dΓ
```
d(cos θhel)
```
=
1
2
```
[1 + αPτ cos θhel] (6)656
```
35
where cos θhel is the helicity angle of the τ lepton and α is a coefficient expressing the657
sensitivity of the different τ decays to Pτ .658
We aim at measuring the polarization of τ lepton as an asymmetry between the forward659
and backward produced τ leptons in the helicity plane of the τ rest frame. Even though660
due to the missing neutrino in the event the helicity angle cannot be fully determined,661
equivalent kinematic information can be retrieved by using the τ ντ rest frame. The662
method for determining this kinematic information has been developed as part of the first663
Belle analysis [4]. however in this section we reiterate the method for completion.664
We begin by boosting the laboratory frame along with the three momentum component665
of the momentum transfer vector.666
```
q = pe+e− − ptag − pD∗ (7)667
```
where p denotes the four-momentum of the e+e− beam, the Btag and the D∗ respec-668
tively. Now in this frame one can extract the momentum and energy of the τ lepton669
as670
Eτ =
q2 + m2τ
2
p
q2
```
(8)671
```
pτ =
q2 − m2τ
2
p
q2
```
(9)672
```
where mτ is the mass of the τ lepton. cos θd is the angle between the the τ lepton and673
the charged hadron daughter of the τ in its two body decay and can be computed as674
cos θd =
2Eτ Ed − m2τ − m2d
2|⃗p τ ||⃗p d|
```
(10)675
```
The true momentum of the charged hadron in the τ rest frame can be calculated as676
```
pd = m
```
2τ −m2d
2mτ .677
Finally by boosting this frame to the τ ντ rest frame we obtain678
```
|⃗pτd | cos θhel = −γ|⃗β|Ed + γ|⃗p d| cos θd (11)679
```
with γ = Eτmτ and β = |⃗p τ |Eτ680
Now by integrating 6 in [0,1] and [-1, 0], we define Pτ as the asymmetry of forward-681
backward events in the helicity plane.682
Pτ =
2
α
NF − NB
NF + NB
```
(12)683
```
where NF and NB are events with positive and negative helicity angle respectively.684
For τ → πντ the coefficient α is 1 while for for τ → ρντ is 0.45 [65].685
36
5.3 Definition of Signal Region686
After truth matching the events, we apply a set of tighter selections on the events that687
survived the basf2 reconstruction. Such an approach enables the definitions of sidebands688
and the conduction of optimization tests without rerunning the basf2 reconstruction689
which is computationally intensive. In Table 20 we present the set of tight selections that690
we apply. For every selection, we save a sample with the respective anti-cut as well in691
a different file. That way we ensure that orthogonal samples can be used for sideband692
```
checks. This set of selections defines what we call Signal enhanced Region (SR) where we693
```
```
expect most of B → D∗τ ν events and Normalization enhanced Region (NR) where we694
```
expect most of B → D∗ℓν events in the rest of the document.695
Table 20: List of final tight cuts applied in the sample.
cut variable definition motivation region
```
nROE Charged < 1charged tracks Apply theSR, NRpresent in the completenessROE of Υ (4S) constraint
```
```
roeEextra < 1.25 GeVtotal energy in Signal peaking closeSR, NRthe ECL attributed to the to zero as no missingROE of Υ (4S) particles are expected
```
```
< 0.1413 ∆M(D∗±) < 0.154 GeV M(D∗±) - M(D0) Tighten D∗ mass window SR, NR< 0.135 ∆M(D∗0) < 0.149 GeV M(D∗0) - M(D0)
```
```
q2 > 4 GeV 2 q2 = (pbeam − pBtag − pD∗ )2 kinematic constraint from τ mass SR, NR
```
pleading FSP > 0.5 GeV lepton momentum or suppress fakes SR, NRcharged hadron momentum
```
-2 < cos θτhel < 2.2 in B0 → D∗−(D0 π−) π+−γβEd+γpd cos θτd
```
pτ restd
cosine of τ helicity angle
```
SR-1.2 < cos θτhel < 3 in B0 → D∗−(D0 π−) ρ+ that minimizes the uncertainty-2 < cos θτhel < 2.2 in B+ → D∗0(D0 π0) π+ of Pτ . Optimization procedure outlined
```
```
-1.2 < cos θτhel < 3 in B+ → D∗0(D0 π0) ρ+ in Appendix H
```
```
-1 < m2miss < 7 GeV 2 in B → D∗(D0 π) h+ Squared recoil mass of the signal side identify signal events SRthat peak in higher values
```
```
-1 < m2miss < 2 GeV 2 in B → D∗(D0 π) ℓ+ Squared recoil mass of the signal side identify normalization events NRthat peak around zero
```
```
1.84 < MD0 < 1.89 GeV M(D0) Tighten D0 mass window SR, NR
```
```
0.590 < Mρ+ < 1.050 GeV M(ρ+) Tighten ρ+ mass window SR
```
Figures 7, 8 and 9 present the impact of every offline selection in the B0 → D∗τ ν,696
B+ → D∗τ ν, B0 → D∗ℓν and B+ → D∗ℓν templates in the signal reconstruction channels697
in terms of number of candidates that survive, sample efficiency and sample purity. It698
clear that all selections have the desired impact since the purity is always increasing699
especially for the templates of interest if one ignores cross-feeds between the channels.700
Figures 10, 11 and 12 present the impact of every offline selection in the B0 → D∗τ ν,701
B+ → D∗τ ν, B0 → D∗ℓν and B+ → D∗ℓν templates in the normalization reconstruction702
channels in terms of number of candidates that survive, sample efficiency and sample703
purity. It clear that all selections have the desired impact since the purity is always704
increasing especially for the templates of interest if one ignores cross-feeds between the705
channels.706
37
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
1.2e+03 8.1e+02 7.6e+02 4.9e+02 4.8e+02 3.1e+02 2.9e+02 2.9e+02
1.3e+01 9.3 8.4 1.8 1.8 1.8 1.8 1.8
1.3e+03 9.1e+02 8.8e+02 6.2e+02 3.9e+02 3.6e+02 2.2e+02 2.2e+02
8.5e+01 2.5e+01 2.5e+01 3.5 3.1 0.92 0.53 0.53
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
1.5e+03 1.1e+03 1e+03 6.3e+02 6.2e+02 4.9e+02 4.6e+02 4.6e+02
2.1e+01 1.6e+01 1.6e+01 8.1 8.1 8.1 8.1 8.1
1.1e+03 8.9e+02 8.4e+02 5.5e+02 3.7e+02 3.6e+02 2.4e+02 2e+02
9.6e+01 2.9e+01 2.9e+01 2.5 2.0 1.6 0.76 0.76
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
3.3e+03 2e+03 1.8e+03 7.5e+02 7.4e+02 3.6e+02 3.5e+02 3.5e+02
2.1e+03 1.9e+03 1.8e+03 8.5e+02 8.4e+02 6.2e+02 6e+02 5.9e+02
5.2e+02 2.2e+02 2e+02 6.7e+01 5.5e+01 2.9e+01 2.4e+01 2.3e+01
4.5e+03 3.5e+03 3.4e+03 1.7e+03 1.3e+03 1.1e+03 9.2e+02 9.1e+02
```
B+ D*0(D0 0) +
```
Online reco.
Zero extra tracksEextraECL
< 1.5 GeVtight
MD
*
q2 > 4GeVtight cos
hel
ph+/
- > 0.5GeVtight
m2miss
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
5.2e+03 3.5e+03 3.1e+03 1.1e+03 1.1e+03 8.1e+02 7.9e+02 7.8e+02
3.8e+03 3.4e+03 3.2e+03 1.4e+03 1.4e+03 1.1e+03 1.1e+03 1.1e+03
4.7e+02 2.8e+02 2.6e+02 7.4e+01 5.9e+01 5.3e+01 4.5e+01 4e+01
6.6e+03 5.4e+03 5.3e+03 2.5e+03 2.1e+03 2e+03 1.4e+03 1.3e+03
```
B+ D*0(D0 0) +
```
100
101
102
103
Candidate number
100
101
102
103
Candidate number
102
103
Candidate number
102
103
Candidate number
Cutflow number of candidates
Figure 7: Total number of events that survive after every offline selection for the most
important templates in the signal reconstruction channels.
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 68.32% 64.36% 41.38% 40.81% 25.77% 24.30% 24.14%
100.00% 72.85% 66.14% 14.06% 14.06% 14.06% 14.06% 14.06%
100.00% 71.02% 68.94% 48.51% 30.42% 28.14% 17.00% 16.88%
100.00% 29.25% 28.82% 4.11% 3.58% 1.07% 0.62% 0.62%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 74.41% 69.06% 42.68% 42.16% 33.46% 31.40% 30.90%
100.00% 77.40% 77.40% 38.86% 38.86% 38.86% 38.86% 38.86%
100.00% 78.97% 74.44% 49.20% 32.45% 31.83% 21.14% 17.92%
100.00% 30.64% 30.23% 2.57% 2.12% 1.62% 0.79% 0.79%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 59.36% 53.20% 22.52% 22.27% 10.73% 10.59% 10.33%
100.00% 87.86% 83.48% 40.46% 40.09% 29.25% 28.69% 28.21%
100.00% 42.01% 38.38% 12.85% 10.49% 5.47% 4.58% 4.33%
100.00% 77.84% 75.11% 37.34% 28.63% 24.75% 20.48% 20.25%
```
B+ D*0(D0 0) +
```
Online reco.
Zero extra tracksEextraECL
< 1.5 GeVtight
MD
*
q2 > 4GeVtight cos
hel
ph+/
- > 0.5GeVtight
m2miss
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 67.19% 60.69% 22.12% 21.91% 15.59% 15.30% 15.17%
100.00% 89.17% 84.84% 35.95% 35.64% 29.89% 28.62% 28.43%
100.00% 58.80% 54.18% 15.74% 12.56% 11.27% 9.64% 8.48%
100.00% 82.63% 80.99% 37.87% 32.12% 30.63% 21.75% 19.80%
```
B+ D*0(D0 0) +
```
10 2
10 1
100
Candidate efficiency
10 2
10 1
100
Candidate efficiency
10 1
100
Candidate efficiency
10 1
100
Candidate efficiency
Cutflow efficiency
Figure 8: Efficiency after every offline selection for the most important templates in the
signal reconstruction channels.
38
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.87% 2.23% 3.52% 8.01% 9.94% 9.99% 11.73% 11.84%
0.01% 0.03% 0.04% 0.03% 0.04% 0.06% 0.07% 0.07%
0.93% 2.50% 4.06% 10.12% 7.98% 11.74% 8.84% 8.91%
0.06% 0.07% 0.11% 0.06% 0.06% 0.03% 0.02% 0.02%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.55% 1.45% 2.01% 4.86% 5.79% 5.65% 6.10% 6.07%
0.01% 0.02% 0.03% 0.06% 0.08% 0.09% 0.11% 0.11%
0.42% 1.18% 1.66% 4.29% 3.41% 4.12% 3.15% 2.70%
0.04% 0.04% 0.06% 0.02% 0.02% 0.02% 0.01% 0.01%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.33% 0.61% 1.04% 1.38% 1.53% 1.30% 1.38% 1.39%
0.21% 0.57% 1.03% 1.56% 1.73% 2.24% 2.36% 2.40%
0.05% 0.07% 0.12% 0.12% 0.11% 0.10% 0.09% 0.09%
0.44% 1.08% 1.97% 3.07% 2.64% 4.04% 3.59% 3.67%
```
B+ D*0(D0 0) +
```
Online reco.
Zero extra tracksEextraECL
< 1.5 GeVtight
MD
*
q2 > 4GeVtight cos
hel
ph+/
- > 0.5GeVtight
m2miss
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.22% 0.42% 0.63% 0.73% 0.80% 0.72% 0.77% 0.77%
0.17% 0.41% 0.65% 0.88% 0.96% 1.02% 1.07% 1.07%
0.02% 0.03% 0.05% 0.05% 0.04% 0.05% 0.04% 0.04%
0.29% 0.65% 1.07% 1.60% 1.49% 1.81% 1.40% 1.29%
```
B+ D*0(D0 0) +
```
10 4
10 3
10 2
10 1
Candidate purity
10 4
10 3
10 2
Candidate purity
10 3
10 2
Candidate purity
10 3
10 2
Candidate purity
Cutflow purity
Figure 9: Purity after every offline selection for the most important templates in the
signal reconstruction channels.
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
1.2e+03 8.1e+02 7.6e+02 4.9e+02 4.8e+02 3.1e+02 2.9e+02 2.9e+02
1.3e+01 9.3 8.4 1.8 1.8 1.8 1.8 1.8
1.3e+03 9.1e+02 8.8e+02 6.2e+02 3.9e+02 3.6e+02 2.2e+02 2.2e+02
8.5e+01 2.5e+01 2.5e+01 3.5 3.1 0.92 0.53 0.53
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
1.5e+03 1.1e+03 1e+03 6.3e+02 6.2e+02 4.9e+02 4.6e+02 4.6e+02
2.1e+01 1.6e+01 1.6e+01 8.1 8.1 8.1 8.1 8.1
1.1e+03 8.9e+02 8.4e+02 5.5e+02 3.7e+02 3.6e+02 2.4e+02 2e+02
9.6e+01 2.9e+01 2.9e+01 2.5 2.0 1.6 0.76 0.76
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
3.3e+03 2e+03 1.8e+03 7.5e+02 7.4e+02 3.6e+02 3.5e+02 3.5e+02
2.1e+03 1.9e+03 1.8e+03 8.5e+02 8.4e+02 6.2e+02 6e+02 5.9e+02
5.2e+02 2.2e+02 2e+02 6.7e+01 5.5e+01 2.9e+01 2.4e+01 2.3e+01
4.5e+03 3.5e+03 3.4e+03 1.7e+03 1.3e+03 1.1e+03 9.2e+02 9.1e+02
```
B+ D*0(D0 0) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
5.2e+03 3.5e+03 3.1e+03 1.1e+03 1.1e+03 8.1e+02 7.9e+02 7.8e+02
3.8e+03 3.4e+03 3.2e+03 1.4e+03 1.4e+03 1.1e+03 1.1e+03 1.1e+03
4.7e+02 2.8e+02 2.6e+02 7.4e+01 5.9e+01 5.3e+01 4.5e+01 4e+01
6.6e+03 5.4e+03 5.3e+03 2.5e+03 2.1e+03 2e+03 1.4e+03 1.3e+03
```
B+ D*0(D0 0) +
```
100
101
102
103
Candidate number
100
101
102
103
Candidate number
102
103
Candidate number
102
103
Candidate number
Cutflow number of candidates
Figure 10: Total number of events that survive after every offline selection for the most
important templates in the normalization reconstruction channels.
5.4 Best Candidate Selection707
```
The sample we’re left with after all selections still contains multiple Υ (4S) candidates. We708
```
have selected only one Btag candidate in the online reconstruction already as mentioned709
39
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 68.32% 64.36% 41.38% 40.81% 25.77% 24.30% 24.14%
100.00% 72.85% 66.14% 14.06% 14.06% 14.06% 14.06% 14.06%
100.00% 71.02% 68.94% 48.51% 30.42% 28.14% 17.00% 16.88%
100.00% 29.25% 28.82% 4.11% 3.58% 1.07% 0.62% 0.62%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 74.41% 69.06% 42.68% 42.16% 33.46% 31.40% 30.90%
100.00% 77.40% 77.40% 38.86% 38.86% 38.86% 38.86% 38.86%
100.00% 78.97% 74.44% 49.20% 32.45% 31.83% 21.14% 17.92%
100.00% 30.64% 30.23% 2.57% 2.12% 1.62% 0.79% 0.79%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 59.36% 53.20% 22.52% 22.27% 10.73% 10.59% 10.33%
100.00% 87.86% 83.48% 40.46% 40.09% 29.25% 28.69% 28.21%
100.00% 42.01% 38.38% 12.85% 10.49% 5.47% 4.58% 4.33%
100.00% 77.84% 75.11% 37.34% 28.63% 24.75% 20.48% 20.25%
```
B+ D*0(D0 0) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
100.00% 67.19% 60.69% 22.12% 21.91% 15.59% 15.30% 15.17%
100.00% 89.17% 84.84% 35.95% 35.64% 29.89% 28.62% 28.43%
100.00% 58.80% 54.18% 15.74% 12.56% 11.27% 9.64% 8.48%
100.00% 82.63% 80.99% 37.87% 32.12% 30.63% 21.75% 19.80%
```
B+ D*0(D0 0) +
```
10 2
10 1
100
Candidate efficiency
10 2
10 1
100
Candidate efficiency
10 1
100
Candidate efficiency
10 1
100
Candidate efficiency
Cutflow efficiency
Figure 11: Efficiency after every offline selection for the most important templates in the
normalization reconstruction channels.
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.87% 2.23% 3.52% 8.01% 9.94% 9.99% 11.73% 11.84%
0.01% 0.03% 0.04% 0.03% 0.04% 0.06% 0.07% 0.07%
0.93% 2.50% 4.06% 10.12% 7.98% 11.74% 8.84% 8.91%
0.06% 0.07% 0.11% 0.06% 0.06% 0.03% 0.02% 0.02%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.55% 1.45% 2.01% 4.86% 5.79% 5.65% 6.10% 6.07%
0.01% 0.02% 0.03% 0.06% 0.08% 0.09% 0.11% 0.11%
0.42% 1.18% 1.66% 4.29% 3.41% 4.12% 3.15% 2.70%
0.04% 0.04% 0.06% 0.02% 0.02% 0.02% 0.01% 0.01%
```
B0 D* (D0 ) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.33% 0.61% 1.04% 1.38% 1.53% 1.30% 1.38% 1.39%
0.21% 0.57% 1.03% 1.56% 1.73% 2.24% 2.36% 2.40%
0.05% 0.07% 0.12% 0.12% 0.11% 0.10% 0.09% 0.09%
0.44% 1.08% 1.97% 3.07% 2.64% 4.04% 3.59% 3.67%
```
B+ D*0(D0 0) +
```
B0 D* +
B+ D*0 +
B0 D* +
B+ D*0 +
0.22% 0.42% 0.63% 0.73% 0.80% 0.72% 0.77% 0.77%
0.17% 0.41% 0.65% 0.88% 0.96% 1.02% 1.07% 1.07%
0.02% 0.03% 0.05% 0.05% 0.04% 0.05% 0.04% 0.04%
0.29% 0.65% 1.07% 1.60% 1.49% 1.81% 1.40% 1.29%
```
B+ D*0(D0 0) +
```
10 4
10 3
10 2
10 1
Candidate purity
10 4
10 3
10 2
Candidate purity
10 3
10 2
Candidate purity
10 3
10 2
Candidate purity
Cutflow purity
Figure 12: Purity after every offline selection for the most important templates in the
normalization reconstruction channels.
in 4.4. Therefore the multiple candidates are arising from duplicate D0 candidates, πs710
candidates or multiple ℓ, π+ and ρ+ candidates. We have developed a multi-step BCS711
that is tackling this problem.712
40
```
In order to identify duplicate Υ (4S) candidates we create a unique eventID based713
```
on experiment , run , event and production for simulated data. For714
experimental data the production is redundant. The reasoning behind defining the715
uniqueness of an event is described very nicely in this Belle II internal forum [66]. We716
proceed with theBCS as follows:717
1. Drop all duplicate D0 candidates by keeping the one whose reconstructed invariant718
mass is closer to the the theoretical one, namely 1, 864.84 ± 0.05 GeV.719
2. Drop all duplicate πs candidates720
• For π±s we keep the candidate with the highest momentum721
• For π0s we keep the candidate whose reconstructed invariant mass is closer to722
the the theoretical one, namely 0.1349768 GeV.723
3. For the reconstruction of τ → ρντ modes, if multiple ρ+ candidates are recon-724
structed, we select the candidate whose π0 daughter satisfies the same criteria as725
those applied in the case of π0s .726
4. If duplicate B meson candidates are found between two signal reconstruction modes,727
we keep the one that has been reconstructed in the τ → ρντ mode instead of the728
τ → πντ mode as the former one has almost 2.5 times larger BF than the latter.729
This is also illustrated in Figure 6.730
5. For the reconstruction modes with the extra pion for the calibration of B → D∗∗ℓν731
decays we drop duplicate pion candidates using the same criteria we listed for πs732
candidates.733
6. If there are still multiple candidates in the sample, we pick one at random734
Tables 21 and 22 shows the effect of the series of BCSs in terms of number of candi-735
dates and signal and normalization efficiencies for charged and neutral B mesons for the736
different reconstruction channels. In the end if we find multiple candidates having been737
reconstructed in two types of reconstruction channels e.g. signal and normalization, then738
we keep one candidate at random.739
Table 21: BCS, number of candidates and event efficiencies for the signal reconstruction
channels. Results are not scaled to data luminosity.
```
BCS criterion B0 → D∗−(D0 π−) h+ B+ → D∗0(D0 π0) h+
```
# cand. multipl. B → D∗τ ν eff. # cand. multipl. B → D∗τ ν eff.
```
After offline selections 17,563 2.855 100% (781) 155,990 4.885 100% (1502)
```
Best D0 meson 13,967 2.27 100% 109,621 3.433 99.9%
Best πs 13,861 2.253 100% 78,449 2.457 99.9%
Best π0 from ρ+ 8,526 1.386 100% 44,835 1.404 99.9%
Favor τ → ρντ over τ → πντ 6,178 1.004 100% 32,160 1.007 99.9%
Random candidate 6,152 1.0 100% 31,933 1.0 99.9%
41
Table 22: BCS, number of candidates and event efficiencies the normalization reconstruc-
tion channels. Results are not scaled to data luminosity.
```
BCS criterion B0 → D∗−(D0 π−) ℓ+ B+ → D∗0(D0 π0) ℓ+
```
# cand. multipl. B → D∗ℓν eff. # cand. multipl. B → D∗ℓν eff.
```
After offline selections 18,192 1.074 100% (14,996) 62633 1.576 33390
```
Best D0 meson 16,970 1.002 100% 53,862 1.355 100%
Best πs 16,952 1.0 100% 39,816 1.002 100%
Random candidate 16,944 1.0 100% 39,745 1.0 100%
5.5 Corrections from the Performance group740
Here we describe the corrections that we use based on the recommendations of the Per-741
formance group.742
5.5.1 Luminosity scaling743
Due to the different luminosity assumed in the MC production we apply the scaling factors744
mentioned in Table 23 to the the respective samples.745
5.5.2 Tracking efficiency746
For the medium to high momentum tracks i.e. > 0.2 GeV, we assign a flat systematic747
uncertainty on the track finding efficiency as per the Tracking group’s recommendation748
[67]. No correction is applied on simulated data as the Data/MC ratio is expected to be749
one. We calculate the number of tracks on the signal side and assign a 0.27% uncertainty750
per track. Therefore the total uncertainty that is assigned per event is defined by Equation751
σtrack ef f. = 1.0027N B
sig
```
tracks − 1 (13)752
```
We do not take into account the number of tracks on the tag side, as these will be taken753
into account in the FEI calibration.754
5.5.3 Tracking momentum scale755
We scale the momentum of track on experimental data using the ma.scaleTrackMomenta756
helper function of basf2. The arguments used here are tracking scale factor payload:757
tracking momentumScaleFactor global and tracking scale factor name: sf global central758
as per the Performance group recommendation [68].759
5.5.4 Photon energy bias760
We account for the energy bias in photons on experimental data using the ma.correctEnergyBias761
helper function of basf2. We use the PhotonEnergyBiasCorrection MC15rd June2023762
option for the photon energy bias table [68].763
42
Table 23: Luminosity and scaling factors for different samples simulated data. The as-
sumed L for experimental data for the LS1 dataset is 365.29 ± 1.70 fb−1
```
Sample L (fb−1) in MC scaling factor
```
mixed
1,443.999 0.25045
charged
ccbar
ssbar
uubar
ddbar
```
B0 → D′1(Dππ)ℓ− ¯νℓ 11,204.48 0.0326
```
```
B0 → D′1(D∗ππ)ℓ− ¯νℓ 3,921.57 0.0931
```
```
B0 → D∗0(Dππ)ℓ− ¯νℓ 11,204.48 0.0326
```
```
B0 → D∗0(D∗ππ)ℓ− ¯νℓ 3,921.57 0.0931
```
```
B0 → D′1(D∗η)ℓ− ¯νℓ 456.0 0.8011
```
```
B0 → D∗0(Dη)ℓ− ¯νℓ 456.0 0.8011
```
```
B+ → D′1(Dππ)ℓ− ¯νℓ 10,582.01 0.0345
```
```
B+ → D′1(D∗ππ)ℓ− ¯νℓ 3,367.0 0.1085
```
```
B+ → D∗0(Dππ)ℓ− ¯νℓ 10,582.01 0.0345
```
```
B+ → D∗0(D∗ππ)ℓ− ¯νℓ 3,367.0 0.1085
```
```
B+ → D′1(D∗η)ℓ− ¯νℓ 411.52 0.8877
```
```
B+ → D∗0(Dη)ℓ− ¯νℓ 411.52 0.8877
```
```
B0 → D′1(Dππ)τ − ¯ντ 7,305.0 0.05
```
```
B0 → D∗0(D∗ππ)τ − ¯ντ 2,435.0 0.15
```
```
B0 → D′1(D∗η)τ − ¯ντ 2,435.0 0.15
```
```
B0 → D∗0(Dη)τ − ¯ντ 7,305.0 0.05
```
```
B+ → D′1(Dππ)τ − ¯ντ 6,663.33 0.0548
```
```
B+ → D∗0(D∗ππ)τ − ¯ντ 2,221.11 0.1645
```
```
B+ → D′1(D∗η)τ − ¯ντ 2,221.11 0.1645
```
```
B+ → D∗0(Dη)τ − ¯ντ 6,663.33 0.0548
```
5.5.5 Photon efficiency764
We do not correct the photon finding efficiency on simulated data for photons that are765
```
used to reconstruct π0 candidates. Discussions among members of the the S(L) working766
```
group lead to the conclusion that these are accounted in the π0 efficiency correction.767
5.5.6 π0 efficiency768
We follow the Neutrals group recommendations and we apply a momentum and cos θ de-769
pendent efficiency corrections for π0. The corrections and their uncertainties are provided770
in [69]771
5.5.7 πs efficiency772
We follow the Tracking and Neutrals groups recommendations and we apply a momentum773
dependent efficiency correction for πs. Table 24 shows the correction central values and774
the corresponding uncertainties as determined by the Tracking group [68].775
43
Table 24: Correction tables for π±s efficiency corrections derived by the Tracking group.
```
π±s p ( GeV) value stat. unc. correlated stat. unc. uncorrelated syst. unc.
```
0.05-0.12 0.947 0.011 0.016 0.0027
0.12-0.16 0.985 0.011 0.013 0.0028
0.16-0.20 0.983 0.011 0.015 0.0028
For π0s we apply corrections as describe in Table 25. Following private communication776
with the expert who derived the corrections we multiply by 0.818 in order to take the777
absolute corrections, as the ones mentioned on [68] are relative to the bin 0.2 - 0.4 GeV778
for the cancellation of systematics.779
Table 25: Correction tables for π0s efficiency corrections derived by the Neutrals group.
```
π0s p ( GeV) value stat. unc. syst. unc.
```
0.05-0.10 0.991 0.064 0.032
0.10-0.15 0.877 0.036 0.018
0.15-0.20 0.871 0.038 0.038
```
5.5.8 PID (with the systematics framework)780
```
We correct the lepton ID efficiency and fakes based on the recommendations of the LID781
group. For the efficiency corrections we use the centrally produced tables by the LID group782
```
under the version v0 coarse (which is just a symbolic link to v1 on kekcc) [70]. These783
```
corrections are summarized in Figures 13 and 14. For these and all figures that follow784
empty bins imply that control samples were not available in that particular kinematic785
region or that the statistics of the control samples were that low that the derived correction786
weight was negative, therefore no correction is applied.787
- - + - + - + - + - + -
theta [rad]
0.20.4
0.51.0
1.52.0
2.53.0
3.54.0
4.55.0
5.56.0
6.57.0
p [GeV]
1.10+0.080.08 0.89+0.140.14 0.91+0.10.1 0.95+0.070.07 1.06+0.120.12 0.82+0.150.15 0.94+0.160.16 0.66+0.460.46 1.11+0.720.721.00+0.010.01 0.97+0.010.01 0.99+0.00.0 1.02+0.010.0 1.00+0.00.0 1.03+0.010.0 1.00+0.00.0 0.98+0.010.02 0.95+0.00.0 0.96+0.010.0 0.86+0.00.0 0.86+0.00.0
1.02+0.00.0 1.06+0.010.01 1.00+0.010.01 1.00+0.010.01 1.01+0.00.0 1.01+0.00.0 1.01+0.00.0 1.01+0.010.01 0.94+0.010.0 0.95+0.010.01 0.73+0.00.0 0.68+0.010.01.01+0.00.0 1.05+0.030.02 1.02+0.00.02 1.00+0.00.0 1.01+0.00.01 1.00+0.00.0 1.01+0.00.0 1.00+0.00.0 1.01+0.00.0 0.98+0.00.0 0.95+0.010.01 0.93+0.00.05
1.01+0.00.0 1.01+0.00.0 1.00+0.00.0 0.99+0.00.0 1.01+0.00.0 1.00+0.00.0 1.01+0.00.0 1.01+0.00.0 1.01+0.010.0 0.99+0.010.01 0.90+0.010.01 0.95+0.020.020.99+0.090.01 1.05+0.010.01 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.010.01 0.99+0.00.0 1.01+0.010.01 0.99+0.010.01 1.01+0.010.01 0.96+0.050.04 0.95+0.380.01
1.00+0.020.02 1.01+0.030.03 1.00+0.00.0 1.01+0.00.0 1.01+0.00.0 1.00+0.00.0 1.00+0.00.0 0.96+0.050.0 0.97+0.010.01 0.99+0.010.01 0.93+0.090.09 0.89+0.040.040.98+0.060.06 0.98+0.030.03 1.00+0.00.0 0.99+0.010.01 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 0.98+0.20.2 0.98+0.010.01 0.93+0.080.08 0.94+0.010.01
0.98+0.110.11 0.97+0.050.05 1.00+0.00.0 0.99+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 0.98+0.020.02 0.98+0.020.02 0.95+0.020.02 0.94+0.030.030.98+0.050.05 0.97+0.020.02 1.00+0.00.0 0.99+0.010.01 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 0.98+0.10.1 0.99+0.020.02 0.95+0.080.08 0.92+0.090.09
0.98+0.020.02 0.99+0.020.02 1.00+0.00.0 1.00+0.010.01 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.01+0.010.01 1.00+0.10.1 1.00+0.010.01 0.69+0.70.70.99+0.020.02 0.97+0.070.07 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.00+0.00.0 1.02+0.020.02 1.00+0.020.02 0.72+1.01.0
0.99+0.030.03 0.98+0.050.05 1.00+0.00.0 0.99+0.010.01 1.00+0.00.0 0.99+0.010.010.99+0.020.02 0.99+0.030.03 0.99+0.010.01 0.99+0.010.01
0.98+0.020.02 0.98+0.010.01 1.01+0.020.02 0.97+0.030.03
```
Efficiency Table (eID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 13: eID efficiency tables.
For lepton fakes and hadron efficiencies and fake we generate corrections tables for788
using the Systematics Framework for PID [71]. We align the selections with for leptons789
and charged hadrons to the ones that are outlined in 4. We derive different corrections790
44
- - + - + - + - + - + - + - + -
theta [rad]
0.20.4
0.50.7
1.01.5
2.02.5
3.03.5
4.04.5
5.05.5
6.0
p [GeV]
1.81+0.110.11 2.06+0.160.16 2.20+0.110.11 2.08+0.120.12 0.96+0.030.03 0.88+0.030.03 0.90+0.010.01 0.89+0.010.01 0.90+0.010.01 0.93+0.010.01 0.90+0.020.02 0.86+0.010.01 1.77+3.081.771.07+0.010.01 1.11+0.020.02 0.81+0.010.01 0.80+0.010.01 0.86+0.010.0 0.85+0.00.0 0.85+0.010.01 0.85+0.010.01 0.86+0.010.01 0.87+0.010.01 0.79+0.010.01 0.79+0.010.0 0.23+0.010.01 0.26+0.020.02 0.45+0.050.05 0.45+0.050.05
1.03+0.00.0 1.01+0.00.0 0.82+0.010.01 0.80+0.010.0 0.83+0.010.01 0.82+0.010.01 0.85+0.010.01 0.84+0.010.01 0.88+0.010.01 0.88+0.010.01 0.82+0.010.0 0.81+0.00.0 0.32+0.010.0 0.35+0.010.01 0.50+0.00.0 0.53+0.010.00.98+0.010.01 0.97+0.010.01 0.78+0.010.01 0.75+0.010.01 0.91+0.00.0 0.90+0.00.0 0.93+0.00.0 0.93+0.00.0 0.95+0.00.0 0.95+0.00.0 0.92+0.00.0 0.92+0.00.0 0.79+0.00.0 0.80+0.00.0 0.79+0.00.0 0.80+0.00.0
0.96+0.00.0 0.96+0.00.0 0.94+0.00.0 0.93+0.00.0 0.95+0.00.0 0.95+0.00.0 0.96+0.00.0 0.96+0.00.0 0.97+0.00.0 0.97+0.00.0 0.95+0.020.0 0.96+0.00.01 0.91+0.00.0 0.92+0.00.0 0.91+0.090.0 0.94+0.090.020.97+0.00.0 0.97+0.030.0 0.96+0.00.0 0.96+0.00.0 0.97+0.00.0 0.97+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.96+0.00.0 0.96+0.00.0 0.89+0.00.0 0.90+0.00.0 0.95+0.00.0 0.95+0.00.0
0.99+0.00.0 0.99+0.00.0 0.96+0.00.0 0.96+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.95+0.00.0 0.96+0.00.0 0.84+0.00.0 0.87+0.00.0 0.97+0.00.0 0.98+0.00.00.99+0.00.0 0.99+0.00.0 0.97+0.00.0 0.97+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.95+0.00.0 0.95+0.00.0 0.82+0.00.0 0.86+0.00.0 0.97+0.00.0 0.98+0.00.0
1.04+0.090.15 0.88+0.050.18 0.97+0.030.04 0.84+0.070.07 0.97+0.010.01 0.97+0.010.01 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.95+0.00.0 0.95+0.00.0 0.83+0.010.01 0.88+0.010.01 0.98+0.00.0 0.99+0.00.00.99+0.020.02 0.97+0.030.03 0.98+0.010.01 0.97+0.020.01 0.97+0.00.0 0.97+0.010.01 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.95+0.00.0 0.96+0.00.0 0.84+0.00.0 0.89+0.00.0 0.98+0.00.0 0.98+0.00.0
0.99+0.010.01 0.99+0.010.01 0.96+0.00.0 0.98+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.96+0.00.0 0.96+0.00.0 0.84+0.00.0 0.88+0.00.0 0.95+0.00.0 0.98+0.00.00.99+0.00.0 1.00+0.00.0 0.96+0.00.0 0.98+0.00.0 0.98+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.97+0.00.0 0.97+0.00.0 0.82+0.010.01 0.84+0.010.01 0.85+0.030.03 0.93+0.040.04
0.99+0.00.0 0.99+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.99+0.00.0 0.98+0.00.0 1.02+0.020.02 0.97+0.030.02 1.14+0.260.18 1.20+0.410.240.99+0.00.0 0.99+0.00.0 0.96+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.99+0.00.0 0.99+0.00.0 0.95+0.070.04
```
Efficiency Table ( ID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.4 0.64 0.82 1.16 1.46 1.78 2.13 2.22 2.6
Figure 14: µID efficiency tables.
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
14.95+10.910.9 4.72+5.095.09 0.14+6.16.1 0.74+0.650.65 1.51+0.350.35 0.91+1.011.01 1.01+0.380.38 0.92+0.870.87 0.88+1.251.25 0.06+5.395.39 0.28+1.431.43
2.12+0.710.71 1.73+0.290.29 1.06+0.110.11 0.75+0.090.09 0.84+0.090.09 0.60+0.070.07 0.99+0.150.15 0.52+0.140.14 0.88+0.150.15 0.49+0.170.17 0.76+0.170.17 0.46+0.210.21
1.83+0.340.34 1.32+0.230.23 0.86+0.40.4 0.71+0.30.3 1.03+0.260.26 0.66+0.250.25 0.91+0.540.54 0.85+0.410.41 1.31+0.330.33 0.63+0.20.2 0.50+0.20.2 0.47+0.150.15
4.75+1.041.04 2.53+0.930.93 3.80+2.282.28 2.67+0.880.88 1.46+0.670.67 0.99+0.550.55 0.70+0.640.64 0.89+0.470.47 0.80+0.310.31
4.06+3.763.76 8.26+10.0810.08 0.77+1.211.21 0.89+0.920.92 1.85+0.460.46 0.15+2.492.49 1.45+0.950.95 0.35+6.526.52 0.03+16.9716.97 1.03+1.391.39 1.75+0.760.76
2.73+1.081.08 3.22+2.582.58 1.74+0.720.72 1.10+0.70.7 0.94+0.770.77 0.59+1.121.12 0.39+4.944.94 3.22+3.523.52 2.33+2.322.32 1.27+0.910.91
4.15+1.851.85 1.40+2.462.46 3.37+1.391.39 1.11+2.132.13 1.98+1.11.1 1.05+1.241.24 7.72+22.5322.53
1.34+5.155.15 1.50+4.334.33 0.33+14.0114.01 2.75+2.762.76 2.29+2.282.28 4.62+6.216.21 12.61+3.513.51 7.14+13.213.2
3.94+10.5910.59 4.72+4.584.58 9.90+43.8143.81 0.01+323.12323.12 0.20+2.052.05
```
Fake Rate (K/e) Table (eID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 15: eID fake rate tables where a kaon is faking an electron.
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
3.44+0.170.17 3.79+0.190.19 3.21+0.140.14 4.06+0.190.19 2.04+0.080.08 1.64+0.070.07 2.95+0.240.24 2.03+0.160.16 1.34+0.020.02 1.46+0.020.02 0.89+0.030.03 0.88+0.030.03
3.06+0.460.46 2.78+0.440.44 4.11+1.281.28 4.55+2.462.46 1.78+0.180.18 1.62+0.350.35 1.83+0.20.2 2.70+0.840.84 1.31+0.250.25 0.45+3.373.37 0.86+0.240.24 0.69+0.330.33
2.31+0.150.15 3.31+0.540.54 2.81+0.180.18 2.08+0.170.17 1.89+0.060.06 1.85+0.10.1 2.08+0.080.08 2.56+0.140.14 2.08+0.10.1 2.16+0.160.16 1.08+0.10.1 1.60+0.120.12
2.93+0.130.13 3.21+0.180.18 3.31+0.180.18 2.98+0.190.19 2.73+0.380.38 2.23+0.290.29 2.17+0.420.42 3.65+0.470.47 1.26+0.290.29 1.49+0.370.37 1.36+0.250.25 1.66+0.350.35
3.57+0.230.23 3.39+0.240.24 2.09+0.260.26 3.09+0.470.47 2.24+0.60.6 2.26+0.650.65 2.21+0.690.69 1.91+0.740.74 1.78+0.980.98 1.45+0.760.76 1.66+0.570.57 1.84+0.60.6
3.05+0.230.23 3.37+0.510.51 3.16+0.580.58 3.10+1.241.24 3.98+0.680.68 2.39+1.371.37 2.80+1.371.37 2.89+0.860.86 3.88+1.371.37 34.52+12.6512.65 3.73+1.61.6 2.24+0.720.72
3.00+0.540.54 2.86+1.011.01 4.55+0.510.51 2.94+1.491.49 4.06+1.241.24 2.80+1.531.53 1.43+2.82.8 2.00+1.471.47 2.34+1.411.41 1.06+2.642.64
2.98+0.860.86 3.83+3.113.11 3.91+1.51.5 8.50+2.82.8 4.95+3.933.93 0.78+6.16.1 9.73+18.3118.31 2.37+8.088.08 348.67+952.6952.6 0.80+1.371.37
1.54+1.411.41 3.17+2.932.93 1.41+8.118.11 134.21+66.2666.26 9.23+22.822.8 inf+1.411.41 10.62+7.137.13
```
Fake Rate ( /e) Table (eID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 16: eID fake rate tables where a pion is faking an electron.
- - + - + - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
10.12+31.2931.29 2.37+3.633.63 1.54+12.512.5 2.91+61.1161.11 2.53+2.182.18 4.17+2.232.23
1.12+0.420.42 1.31+0.430.43 0.60+0.860.86 0.79+0.730.73 0.80+0.310.31 0.83+0.350.35 0.84+0.20.2 0.80+0.260.26 0.81+0.230.23 0.72+0.240.24 0.79+0.370.37 0.75+0.40.4 0.71+0.260.26 0.73+0.30.3 0.55+0.130.13 0.56+0.170.17
1.10+0.10.1 1.16+0.110.11 0.97+0.120.12 0.84+0.160.16 0.98+0.080.08 1.09+0.090.09 1.11+0.070.07 1.28+0.080.08 0.93+0.10.1 1.27+0.120.12 0.96+0.110.11 1.12+0.130.13 0.75+0.090.09 1.35+0.110.11 0.49+0.070.07 0.76+0.090.09
1.02+0.070.07 1.07+0.090.09 1.19+0.080.08 1.15+0.10.1 1.14+0.050.05 1.37+0.060.06 1.21+0.050.05 1.53+0.060.06 1.26+0.050.05 1.70+0.070.07 1.38+0.070.07 1.41+0.080.08 0.88+0.090.09 1.14+0.110.11 0.77+0.060.06 0.73+0.090.09
1.00+0.070.07 0.89+0.090.09 1.13+0.080.08 1.18+0.10.1 1.30+0.040.04 1.32+0.050.05 1.24+0.040.04 1.54+0.050.05 1.34+0.040.04 1.49+0.050.05 1.46+0.050.05 1.53+0.060.06 0.88+0.10.1 0.88+0.120.12 0.84+0.070.07 0.85+0.090.09
0.91+0.070.07 1.03+0.080.08 1.15+0.070.07 1.00+0.080.08 1.40+0.030.03 1.46+0.050.05 1.33+0.030.03 1.48+0.040.04 1.38+0.040.04 1.56+0.050.05 1.21+0.050.05 1.46+0.060.06 0.64+0.140.14 0.95+0.140.14 0.73+0.10.1 0.60+0.140.14
0.91+0.070.07 0.92+0.080.08 1.16+0.070.07 1.16+0.080.08 1.31+0.040.04 1.48+0.040.04 1.29+0.040.04 1.47+0.050.05 1.30+0.050.05 1.48+0.070.07 1.55+0.060.06 1.22+0.080.08 0.82+0.220.22 0.64+0.260.26 0.78+0.170.17 0.69+0.210.21
0.98+0.060.06 0.87+0.080.08 1.15+0.080.08 1.02+0.10.1 1.44+0.040.04 1.47+0.060.06 1.31+0.050.05 1.38+0.070.07 1.61+0.080.08 1.54+0.090.09 1.35+0.130.13 1.32+0.160.16 0.49+0.610.61 1.50+0.530.53 0.13+1.391.39 0.21+1.71.7
0.78+0.080.08 0.83+0.10.1 1.01+0.120.12 0.87+0.150.15 1.42+0.070.07 1.57+0.090.09 1.29+0.090.09 1.22+0.120.12 1.74+0.190.19 2.49+0.20.2 3.33+0.660.66 2.42+0.980.98 1.75+2.592.59
```
Fake Rate (K/ ) Table ( ID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.4 0.64 0.82 1.16 1.46 1.78 2.13 2.22 2.6
Figure 17: µID fake rate tables where a kaon is faking a muon.
tables for kaons and for pions faking the reconstructed lepton. We present the correction791
for lepton fakes in Figures 15, 16, 17 and 18,792
45
- - + - + - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
4.13+0.010.01 3.90+0.010.01 1.65+0.010.01 1.66+0.010.01 0.99+0.010.01 0.97+0.010.01 1.03+0.010.01 1.05+0.010.01 1.06+0.010.01 1.12+0.010.01 0.97+0.010.01 0.99+0.010.01 0.37+0.130.13 0.29+0.130.13 0.37+0.20.2 0.25+0.210.21
1.56+0.010.01 1.65+0.010.01 0.93+0.00.0 0.90+0.00.0 0.94+0.010.01 0.91+0.00.0 0.89+0.010.01 0.91+0.010.01 1.03+0.010.01 1.03+0.010.01 0.89+0.010.01 0.92+0.010.01 0.45+0.030.03 0.44+0.030.03 0.46+0.020.02 0.45+0.020.02
0.94+0.020.02 0.92+0.020.02 0.68+0.020.02 0.64+0.020.02 0.87+0.020.02 0.85+0.020.02 0.88+0.020.02 0.85+0.020.02 0.95+0.020.02 0.94+0.020.02 0.85+0.020.02 0.88+0.020.02 0.65+0.050.05 0.62+0.050.05 0.59+0.040.04 0.58+0.040.04
0.75+0.040.04 0.71+0.040.04 0.75+0.040.04 0.79+0.040.04 0.84+0.030.03 0.78+0.040.04 0.89+0.040.04 0.77+0.040.04 0.93+0.040.04 0.83+0.040.04 0.84+0.040.04 0.82+0.040.04 0.69+0.080.08 0.61+0.090.09 0.60+0.080.08 0.60+0.080.08
0.67+0.050.05 0.62+0.050.05 0.64+0.070.07 0.64+0.060.06 0.74+0.040.04 0.81+0.040.04 0.80+0.050.05 0.82+0.040.04 0.91+0.040.04 0.87+0.050.05 0.80+0.050.05 0.82+0.050.05 0.57+0.120.12 0.46+0.120.12 0.46+0.130.13 0.56+0.110.11
0.54+0.060.06 0.48+0.060.06 0.62+0.070.07 0.60+0.060.06 0.79+0.050.05 0.77+0.050.05 0.84+0.050.05 0.75+0.050.05 0.74+0.050.05 0.90+0.050.05 0.82+0.060.06 0.74+0.060.06 0.46+0.180.18 0.50+0.170.17 0.43+0.180.18 0.27+0.250.25
0.44+0.070.07 0.41+0.070.07 0.64+0.080.08 0.65+0.070.07 0.76+0.050.05 0.75+0.050.05 0.73+0.060.06 0.78+0.060.06 0.81+0.070.07 0.77+0.070.07 0.80+0.090.09 0.59+0.110.11 0.53+0.390.39 0.42+0.370.37 0.45+0.40.4 0.34+0.450.45
0.41+0.080.08 0.38+0.080.08 0.52+0.10.1 0.57+0.090.09 0.71+0.070.07 0.83+0.060.06 0.84+0.080.08 0.85+0.080.08 0.84+0.120.12 0.86+0.120.12 0.60+0.310.31 0.68+0.310.31 0.77+0.980.98 1.74+1.71.7
0.29+0.120.12 0.29+0.120.12 0.91+0.110.11 0.53+0.120.12 0.86+0.090.09 0.76+0.090.09 0.74+0.190.19 0.70+0.180.18 1.67+0.520.52 1.29+0.40.4 0.22+3.583.58 1.75+8.148.14 inf+1.411.41 inf+1.411.41
```
Fake Rate ( / ) Table ( ID > 0.9)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.4 0.64 0.82 1.16 1.46 1.78 2.13 2.22 2.6
Figure 18: µID fake rate tables where a pion is faking a muon.
Figures 19, 20, 21 and 22 illustrate the HID Data/MC ratios that we derive using793
the Systematics Framework in bins of momentum and cos θ of the track for correctly794
reconstructed and misreconstructed hadrons.795
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
1.00+0.080.08 0.91+0.110.11 1.02+0.070.07 1.02+0.080.08 1.02+0.050.05 1.01+0.050.05 1.01+0.040.04 1.01+0.040.04 1.01+0.040.04 1.00+0.040.04 1.00+0.030.03 1.00+0.030.03
0.98+0.020.02 0.99+0.020.02 0.99+0.010.01 0.99+0.020.02 1.00+0.010.01 0.99+0.010.01 1.00+0.010.01 1.00+0.010.01 1.00+0.010.01 1.00+0.010.01 1.00+0.010.01 0.99+0.010.01
0.99+0.010.01 0.99+0.010.01 0.99+0.00.0 0.99+0.010.01 0.98+0.010.01 0.99+0.010.01 1.00+0.00.0 0.99+0.00.0 1.00+0.00.0 1.00+0.00.0 1.04+0.00.0 1.05+0.00.0
1.06+0.010.01 1.05+0.010.01 0.98+0.00.0 0.98+0.00.0 0.97+0.00.0 0.98+0.00.0 0.99+0.00.0 0.99+0.00.0 1.00+0.00.0 1.00+0.00.0 1.04+0.00.0 1.06+0.00.0
1.06+0.010.01 1.06+0.00.0 0.98+0.00.0 0.97+0.00.0 0.96+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 1.00+0.00.0 1.00+0.00.0 1.01+0.00.0 1.02+0.010.01
1.05+0.00.0 1.05+0.00.0 0.96+0.00.0 0.96+0.00.0 0.96+0.00.0 0.96+0.00.0 0.97+0.00.0 0.97+0.00.0 0.99+0.00.0 0.99+0.00.0 1.00+0.00.0 1.02+0.010.01
1.06+0.010.01 1.04+0.010.01 0.96+0.00.0 0.95+0.00.0 0.95+0.00.0 0.95+0.00.0 0.95+0.010.01 0.95+0.010.01 0.96+0.010.01 0.95+0.010.01 1.01+0.010.01 1.00+0.010.01
1.05+0.010.01 1.04+0.010.01 0.96+0.00.0 0.94+0.00.0 0.96+0.010.01 0.96+0.010.01 0.91+0.010.01 0.91+0.010.01 0.93+0.020.02 0.93+0.020.02 1.00+0.060.06 0.96+0.090.09
1.06+0.010.01 1.04+0.010.01 0.96+0.00.0 0.94+0.00.0 0.98+0.010.01 0.98+0.010.01 0.92+0.030.03 0.84+0.040.04 0.94+0.270.27 1.44+0.580.58
```
Efficiency Table (kID > 0.1)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 19: kaonID efficiency tables
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
4.50+0.640.64 3.30+0.630.63 1.88+0.080.08 1.79+0.090.09 3.17+0.260.26 3.25+0.290.29 2.36+0.140.14 2.44+0.150.15 1.72+0.070.07 1.68+0.070.07 6.59+2.592.59 20.13+14.8414.84
0.69+0.010.01 0.64+0.010.01 1.34+0.010.01 1.34+0.010.01 1.65+0.020.02 1.66+0.020.02 1.63+0.020.02 1.63+0.020.02 1.49+0.010.01 1.44+0.010.01 1.18+0.010.01 1.14+0.010.01
0.71+0.010.01 0.70+0.010.01 1.26+0.010.01 1.25+0.010.01 1.25+0.010.01 1.23+0.010.01 1.09+0.020.02 1.14+0.020.02 1.08+0.010.01 1.10+0.010.01 1.04+0.00.0 1.03+0.00.0
0.89+0.020.02 0.81+0.020.02 1.38+0.010.01 1.28+0.010.01 1.23+0.010.01 1.22+0.010.01 1.10+0.030.03 1.09+0.020.02 1.17+0.010.01 1.14+0.010.01 1.03+0.00.0 1.05+0.00.0
1.26+0.040.04 1.21+0.050.05 1.38+0.010.01 1.31+0.010.01 1.17+0.010.01 1.13+0.010.01 1.16+0.050.05 1.17+0.050.05 1.38+0.020.02 1.35+0.020.02 1.00+0.010.01 1.00+0.010.01
0.94+0.070.07 0.99+0.060.06 1.28+0.010.01 1.18+0.010.01 1.06+0.010.01 1.02+0.020.02 1.29+0.050.05 1.18+0.050.05 1.37+0.020.02 1.38+0.020.02 1.00+0.010.01 0.96+0.010.01
0.73+0.10.1 0.78+0.110.11 1.14+0.010.01 1.03+0.010.01 1.02+0.010.01 0.92+0.010.01 1.10+0.040.04 1.11+0.050.05 1.20+0.030.03 1.30+0.030.03 1.03+0.030.03 0.96+0.040.04
0.61+0.070.07 0.54+0.080.08 1.11+0.010.01 0.97+0.020.02 0.95+0.020.02 0.92+0.020.02 1.05+0.080.08 0.95+0.080.08 0.99+0.120.12 0.95+0.180.18 0.72+0.270.27 0.25+0.40.4
0.55+0.060.06 0.48+0.080.08 1.19+0.020.02 0.99+0.030.03 1.00+0.040.04 0.84+0.040.04 0.69+0.60.6 3.62+2.132.13 0.01+100.64100.64 0.28+2.62.6 0.22+1.811.81
```
Fake Rate ( /K) Table (kID > 0.1)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 20: kaonID fake rate tables where a pion is faking a kaon
```
A subtle but important point is that, since we recover the bremsstrahlung (Brems)796
```
momentum for electrons as described in Section 4.5.2, we use the electron momentum be-797
fore Brems recovery to determine the kinematic bin in which an event falls. This follows798
the LID recommendations [72], as all electron efficiency corrections in the Systematics799
Framework are derived without applying any Brems recovery. Accessing the pre-Brems800
momentum in basf2 is straightforward. When Brems recovery is performed using the ded-801
icated basf2 modules, the electron object before Brems recovery is stored as a daughter802
46
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
0.93+0.00.0 0.94+0.00.0 0.96+0.00.0 0.97+0.00.0 0.97+0.00.0 0.97+0.00.0 0.96+0.00.0 0.97+0.00.0 0.98+0.00.0 0.99+0.00.0 0.99+0.00.0 1.00+0.00.0
0.99+0.00.0 0.99+0.00.0 0.99+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.96+0.00.0 0.96+0.00.0 1.01+0.00.0 1.02+0.00.0 1.03+0.00.0 1.04+0.00.0
1.04+0.00.0 1.05+0.00.0 0.99+0.00.0 0.99+0.00.0 0.98+0.00.0 0.98+0.00.0 0.97+0.00.0 0.97+0.00.0 1.00+0.00.0 1.00+0.00.0 1.03+0.00.0 1.03+0.00.0
1.04+0.00.0 1.05+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.00.0 1.03+0.00.0 1.04+0.00.0
1.04+0.00.0 1.04+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.00.0 0.98+0.00.0 0.98+0.010.01 0.97+0.010.01 0.93+0.010.01 0.92+0.010.01 0.99+0.00.0 0.99+0.00.0
1.06+0.00.0 1.05+0.00.0 0.97+0.00.0 0.97+0.00.0 0.98+0.010.01 0.98+0.010.01 0.98+0.010.01 0.99+0.010.01 0.92+0.010.01 0.89+0.010.01 0.99+0.010.01 0.99+0.010.01
1.08+0.010.01 1.07+0.010.01 0.97+0.010.01 0.98+0.010.01 0.99+0.00.0 0.99+0.00.0 1.00+0.010.01 0.98+0.010.01 0.93+0.010.01 0.93+0.010.01 0.99+0.020.02 1.05+0.030.03
1.10+0.010.01 1.10+0.010.01 0.98+0.010.01 0.99+0.010.01 1.00+0.010.01 1.00+0.010.01 1.00+0.010.01 0.98+0.020.02 0.89+0.060.06 0.74+0.140.14 1.01+0.190.19 0.78+0.30.3
1.14+0.010.01 1.13+0.010.01 0.99+0.010.01 0.98+0.010.01 1.04+0.020.02 1.02+0.020.02 1.13+0.260.26 2.25+1.281.28
```
Efficiency Table ( ID > 0.1)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 21: πID efficiency tables
- - + - + - + - + - + -
theta [rad]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
p [GeV]
4.50+0.640.64 3.30+0.630.63 1.88+0.080.08 1.79+0.090.09 3.17+0.260.26 3.25+0.290.29 2.36+0.140.14 2.44+0.150.15 1.72+0.070.07 1.68+0.070.07 6.59+2.592.59 20.13+14.8414.84
0.69+0.010.01 0.64+0.010.01 1.34+0.010.01 1.34+0.010.01 1.65+0.020.02 1.66+0.020.02 1.63+0.020.02 1.63+0.020.02 1.49+0.010.01 1.44+0.010.01 1.18+0.010.01 1.14+0.010.01
0.71+0.010.01 0.70+0.010.01 1.26+0.010.01 1.25+0.010.01 1.25+0.010.01 1.23+0.010.01 1.09+0.020.02 1.14+0.020.02 1.08+0.010.01 1.10+0.010.01 1.04+0.00.0 1.03+0.00.0
0.89+0.020.02 0.81+0.020.02 1.38+0.010.01 1.28+0.010.01 1.23+0.010.01 1.22+0.010.01 1.10+0.030.03 1.09+0.020.02 1.17+0.010.01 1.14+0.010.01 1.03+0.00.0 1.05+0.00.0
1.26+0.040.04 1.21+0.050.05 1.38+0.010.01 1.31+0.010.01 1.17+0.010.01 1.13+0.010.01 1.16+0.050.05 1.17+0.050.05 1.38+0.020.02 1.35+0.020.02 1.00+0.010.01 1.00+0.010.01
0.94+0.070.07 0.99+0.060.06 1.28+0.010.01 1.18+0.010.01 1.06+0.010.01 1.02+0.020.02 1.29+0.050.05 1.18+0.050.05 1.37+0.020.02 1.38+0.020.02 1.00+0.010.01 0.96+0.010.01
0.73+0.10.1 0.78+0.110.11 1.14+0.010.01 1.03+0.010.01 1.02+0.010.01 0.92+0.010.01 1.10+0.040.04 1.11+0.050.05 1.20+0.030.03 1.30+0.030.03 1.03+0.030.03 0.96+0.040.04
0.61+0.070.07 0.54+0.080.08 1.11+0.010.01 0.97+0.020.02 0.95+0.020.02 0.92+0.020.02 1.05+0.080.08 0.95+0.080.08 0.99+0.120.12 0.95+0.180.18 0.72+0.270.27 0.25+0.40.4
0.55+0.060.06 0.48+0.080.08 1.19+0.020.02 0.99+0.030.03 1.00+0.040.04 0.84+0.040.04 0.69+0.60.6 3.62+2.132.13 0.01+100.64100.64 0.28+2.62.6 0.22+1.811.81
```
Fake Rate ( /K) Table (kID > 0.1)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.22 0.56 1.13 1.57 1.88 2.23 2.71
Figure 22: πID fake rate tables where a kaon is faking a pion.
of the post-Brems electron. This behaviour is also explained clearly in the correspond-803
ing Belle II discussion [73]. The considerations above apply to both the eID efficiency804
corrections and the fake-rate corrections.805
```
5.5.9 PID (custom corrections)806
```
In this analysis, a significant fraction of muons are observed to be misidentified as pions.807
```
This component plays a crucial role in our signal extraction, particularly for R(D∗),808
```
```
since the B0 → D∗−(D0 π−) π+and B+ → D∗0(D0 π0) π+are especially contaminated by809
```
B → D∗τ ν events where the τ lepton decays τ → µντ νµ. Such events have kinematic810
properties very similar to B → D∗τ ν events where the τ lepton decays as τ → πντ ,811
with the only differences being that the muon is misidentified as a pion and an additional812
neutrino is present in the event. Consequently, these events can be easily mistaken for the813
signal in the extraction fit, as their shapes closely resemble the correctly reconstructed814
signal component.815
```
Given their significant impact on the R(D∗) measurement, a reliable calibration of816
```
the muon-to-pion fake rate efficiency is essential. Unfortunately, the current Systematics817
Framework for PID [71] does not support corrections for muons faking pions in MC15rd.818
After consultation with PID experts, dedicated efficiency correction tables were derived819
specifically for this analysis. The samples used to derive these corrections are described820
in [74]. A clean sample of muons is obtained by reconstructing the process e+e− →821
e+e−µ+µ−. The muons are reconstructed using a tag-and-probe method. The probe822
muon selection is chosen to match our pion reconstruction criteria, as outlined in Section823
47
4.5.3. Although [74] details the reconstruction and efficiency correction derivation for824
```
MC13a and proc11, the methods and code used for and proc13 + prompt are identical;825
```
the only difference is that the code is run on different samples. The code used for these826
corrections is available in the GitLab repository [75].827
The resulting corrections are shown in Figure 23. The specified momentum and angu-828
lar ranges cover the majority of the relevant sample. Only 1.43 out of the 37.98 expected829
B → D∗τ ν events where the τ decays as τ → µντ νµ remain uncorrected, as they fall within830
the range 0 < θ < 0.4, for which corrections are not available from the e+e− → e+e−µ+µ−831
sample. This fraction is considered negligible, and no further corrections are applied to832
these events.833
- - + - + - + - + - + - + - + -
theta [rad]
0.5
0.75
1.0
1.25
1.5
2.0
p [GeV]
0.98+0.010.01 0.99+0.010.01 1.25+0.020.02 1.22+0.020.02 1.26+0.040.04 1.22+0.050.05 1.37+0.060.06 1.33+0.070.07 1.30+0.080.08 1.28+0.070.07 1.54+0.040.04 1.50+0.040.04 1.14+0.010.01 1.16+0.010.01 1.58+0.010.01 1.58+0.010.01
1.49+0.080.08 1.45+0.090.09 1.72+0.090.09 1.59+0.10.1 1.57+0.060.06 1.49+0.060.06 1.68+0.030.03 1.68+0.030.03 1.46+0.040.04 1.50+0.040.04 1.55+0.020.02 1.54+0.020.02 1.36+0.010.01 1.37+0.010.01 1.70+0.020.02 1.67+0.010.01
1.84+0.150.15 1.69+0.150.15 1.62+0.030.03 1.53+0.040.04 2.00+0.040.04 1.95+0.040.04 2.01+0.080.08 2.09+0.080.08 1.59+0.090.09 1.81+0.090.09 1.46+0.030.03 1.57+0.030.03 1.36+0.020.02 1.43+0.020.02 1.51+0.020.02 1.62+0.030.03
1.53+0.030.03 1.72+0.030.03 1.94+0.040.04 1.88+0.040.04 2.33+0.080.08 2.33+0.090.09 2.10+0.120.12 2.13+0.130.13 1.55+0.130.13 1.68+0.140.14 1.35+0.040.04 1.55+0.050.05 1.72+0.050.05 1.94+0.060.06 1.51+0.070.07 1.82+0.070.07
1.48+0.030.03 1.60+0.030.03 2.37+0.070.07 2.47+0.080.08 2.24+0.110.11 2.25+0.120.12 1.91+0.190.19 2.04+0.20.2
```
Fake Rate ( / ) Table ( ID > 0.1)
```
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
data_MC_ratio
0.4 0.64 0.82 1.16 1.46 1.78 2.13 2.22 2.6
Figure 23: πID fake rate tables where a muon is faking a pion.
5.6 Branching Fraction corrections834
We update the BFs of several reconstructed decays to align with the latest values from835
PDGLive. Each decay is identified using the truth matching strategy outlined in Section836
5.1 All the assumed values in the Belle II MC are taken from the DECAY.dec file of release837
6.838
5.6.1 Charmed mesons839
We update the BF of D0, D∗0 and D∗± meson decays with the ratios described in Table840
26841
5.6.2 τ lepton842
We update the BF of the τ lepton decays with the ratios described in Table 27843
5.6.3 Double charm background844
We update the BF of a handful of double charm decays with the ratios described in845
Table 28. These decays include decays where the B meson decays into two charmed846
mesons, excited or not and optionally a meson including an s quark. For decays where no847
prediction from PDG [7] or their final state is generated via PYTHIA [11] in the Belle II848
MC we attribute a correction weight of one and assign a 100% uncertainty on the BF.849
48
Table 26: BF corrections for charmed meson decays
DECAY.dec pdgLive
decay value line value entry ratio
D∗+ → D0π+ 0.677 7913 0.677 ± 0.0005 Γ1 1.0000 ± 0.0007
D∗+ → D+π0 0.307 7914 0.307 ± 0.0005 Γ2 1.0000 ± 0.0016
D∗+ → D+γ 0.016 7915 0.016 ± 0.0004 Γ3 1.0000 ± 0.0250
D∗0 → D0π0 0.647 7940 0.647 ± 0.0009 Γ1 1.0000 ± 0.0014
D∗0 → D0γ 0.353 7941 0.353 ± 0.0009 Γ2 1.0000 ± 0.0025
D0 → K−π+ 0.0395 8512 0.03947 ± 0.0030 Γ38 0.9992 ± 0.0759
D0 → K+K− 0.00408 8659 0.00408 ± 0.00006 Γ211 1.0000 ± 0.0147
D0 → π+π− 0.001455 8624 0.001454 ± 0.000024 Γ141 0.9993 ± 0.0165
D0 → K0S π0 0.0124 8514 0.0124 ± 0.00022 Γ38 1.0000 ± 0.0177
D0 → K−π+π0 0.144 8539 0.144 ± 0.006 Γ59 1.0000 ± 0.0417
D0 → K0S π+π− 0.028 8546 0.0280 ± 0.0018 Γ44 1.0000 ± 0.0643
D0 → K0S K+K− 0.00442 8606 0.00442 ± 0.00032 Γ126 1.0000 ± 0.0724
D0 → π+π−π0 0.0149 8629 0.0149 ± 0.0007 Γ141 1.0000 ± 0.0470
Table 27: BF corrections for τ lepton decays
DECAY.dec pdgLive
decay value line value entry ratio
τ → πν 0.1091 7855 0.1082 ± 0.0005 Γ9 0.9917 ± 0.0046
τ → ρν 0.2551 7857 0.2549 ± 0.0009 Γ14 0.9992 ± 0.0035
τ → ππ0π0ν 0.079301562 7859 0.0932 ± 0.0010 Γ19 1.1753 ± 0.0126
τ → πππν 0.0932 7874 0.0931 ± 0.0005 Γ67 0.9989 ± 0.0054
τ → µνν 0.170 7854 0.1739 ± 0.0004 Γ3 1.0229 ± 0.0024
τ → eνν 0.154002925 7853 0.1782 ± 0.0004 Γ5 1.1571 ± 0.0026
τ → Kν 0.00696 7856 0.00696 ± 0.0001 Γ10 1.0000 ± 0.0144
τ → πK0K0ν 0.0017 7869 0.00155 ± 0.0024 Γ47 0.9118 ± 1.4118
τ → ππ0π0π0ν 0.008508640 7861 0.0104 ± 0.0007 Γ27 1.2222 ± 0.0822
τ → K∗πν 0.0022 7892 0.0038 ± 0.0017 Γ140 1.7273 ± 0.7732
τ → ππππ0ν 0.0461 7875 0.0274 ± 0.0007 Γ76 0.5944 ± 0.0152
τ → Kππν 0.00342 7878 0.00345 ± 0.0007 Γ95 1.0088 ± 0.2041
τ → πK0ν 0.000319939 7876 0.000838 ± 0.00014 Γ36 2.61857 ± 0.4483
τ → K∗ν 0.012 7888 0.012 ± 0.0007 Γ136 1.0000 ± 0.0583
τ → πK0π0ν 0.004 7871 0.00382 ± 0.00013 Γ41 0.9550 ± 0.0325
5.6.4 Prompt hadronic background850
We update the BF of a handful of prompt hadronic decays with the ratios described in851
Table 29. These decays include decays where the B meson decays into a D∗ meson an a852
few light unflavored mesons. For decays where no prediction from PDG [7] or their final853
state is generated via PYTHIA [11] in the Belle II MC we attribute a correction weight854
of one and assign a 100% uncertainty on the BF.855
5.7 Gap replacement856
In Section 3.2.3, we outlined the way we calculate the luminosity for the dedicated samples857
```
that replace the gap modes. The gap modes include B → D(∗)ππν and B → D(∗)ην858
```
decays. Now, we replace all the non-resonant decays that have survived the reconstruction859
with their resonant counterparts. We expect that such a replacement will lead to an860
increase in the expected yields of B → D∗∗ℓν decays since the lepton momentum of the861
original four- and five-body decays present in the generic MC tends to be smaller. Such862
49
Table 28: BF corrections for double charm decays
DECAY.dec pdgLive
decay value line value entry ratio
B0 → D∗s0D∗ 0.017687170 l.734 0.0015 ± 0.006 Γ 96 0.0848 ± 0.339
B0 → Ds1D∗ 0 0 ± 0 Γ 96 1.0 ± 1.0
B0 → D∗DK0 0.001710000 l.620 0.0064 ± 0.0005 Γ 179 3.743 ± 0.293
B0 → D∗DK∗0 0.002500000 l.637 0 ± 0 1.0 ± 1.0
B0 → D∗D∗K0 0.008109240 l.622 0.0081 ± 0.0007 Γ 180 0.999 ± 0.086
B0 → D∗D∗K∗0 0.005000000 l.639 0 ± 0 1.0 ± 1.0
B0 → D∗0D∗K 0.010600000 l.616 0.0106 ± 0.00009 Γ 177 1.000 ± 0.009
B0 → DsD∗ 0.008044570 l.587 0.008 ± 0.0011 Γ 84 0.995 ± 0.137
B0 → D∗s D∗ 0.017700000 l.587 0.0177 ± 0.0014 Γ 86 1.000 ± 0.079
B0 → D∗s D∗2 0.004000000 l.595 0 ± 0 Γ 86 1.0 ± 1.0
B0 → D∗0D∗K0 0.004000000 l.595 0 ± 0 Γ 86 1.0 ± 1.0
B+ → D∗s0D0 0.007617290 l.4184 0.0008 ± 0.000145 Γ 173 0.105 ± 0.019
B+ → D∗s0D∗0 0.017063010 l.4185 0.0009 ± 0.0007 Γ 175 0.053 ± 0.041
B+ → Ds1D∗0 0.011960470 l.4342 0 ± 0 Γ 175 1.0 ± 1.0
B+ → D∗D0K0 0.003810000 l.4096 0.0038 ± 0.0004 Γ 203 0.997 ± 0.105
B+ → D∗0DK0 0.002060000 l.4097 0.0021 ± 0.0005 Γ 202 1.019 ± 0.242
B+ → D∗0DK∗0 0.002500000 l.4113 0 ± 0 1.0 ± 1.0
B+ → D∗0D∗K0 0.009170000 l.4098 0.0092 ± 0.0012 Γ 204 1.003 ± 0.131
B+ → D∗0D∗K∗0 0.005000000 l.4115 0 ± 0 1.0 ± 1.0
B+ → D∗0D0K 0.008580000 l.4102-4103 0.00856 ± 0.00055 Γ 206-207 0.998 ± 0.064
B+ → D∗0D0K∗ 0.005000000 l.4120 0 ± 0 1.0 ± 1.0
B+ → DsD0 0.009009770 l.4069 0.009 ± 0.0009 Γ 172 0.999 ± 0.100
B+ → DsD∗0 0.008218450 l.4070 0.0082 ± 0.0017 Γ 193 0.998 ± 0.207
B+ → DsD∗2 0.004200000 l.4077 0 ± 0 1.0 ± 1.0
B+ → D∗s D0 0.007600000 l.4071 0.0076 ± 0.0016 Γ 192 1.000 ± 0.211
B+ → D∗s D∗0 0.017100000 l.4072 0.0171 ± 0.0024 Γ 194 1.000 ± 0.140
B+ → D∗s D∗2 0.004000000 l.4078 0 ± 0 1.0 ± 1.0
Table 29: BF corrections for prompt hadronic decays
DECAY.dec pdgLive
decay value line value entry ratio
B0 → D∗π 0.002742680 l.649 0.00274 ± 0.00013 Γ 45 1.00098 ± 0.0474
B0 → D∗ππ0 0.01515771 l.656-657 0.015 ± 0.005 Γ 51 1.01052 ± 0.33674
B0 → D∗ππ0π0 0.002 l.678-679 0 ± 0 1.0 ± 1.0
B0 → D∗ππ0π0π0 0 0 ± 0 1.0 ± 1.0
B0 → D∗ππ0π0η 0 0 ± 0 1.0 ± 1.0
B0 → D∗ππ0η 0 0 ± 0 1.0 ± 1.0
B0 → D∗πππ 0.0187204 l.675 0.013 ± 0.0027 Γ 61 1.43926 ± 0.32385
B0 → D∗ππππ0 0.02006 l.769+745 0.02006 ± 0.002706 Γ 64 + Γ 66 1.000 ± 0.1349
B0 → D∗ππππ0π0 0.0047 l.770 0.0047 ± 0.0009 Γ 65 1.000 ± 0.191
B0 → D∗ππππ0π0π0 0 0 ± 0 1.0 ± 1.0
B0 → D∗πη 0.000256000 l.733 0 ± 0 1.0 ± 1.0
B0 → D∗ππππ0π0π0π0 0 0 ± 0 1.0 ± 1.0
B+ → D∗ππ0π0 0.01715771 l.4161-4162 0.015 ± 0.007 Γ 145 1.14385 ± 0.5332
B+ → D∗0π 0.004900860 l.4137 0.00517 ± 0.00015 Γ 127 0.94777 ± 0.02752
B+ → D∗0ππ0 0.01031176 l.4143-4144 0.0098 ± 0.0017 Γ 131 1.05234 ± 0.18178
B+ → D∗0ππ0η 0 0 ± 0 1.0 ± 1.0
B+ → D∗0πππ 0.0138 l.4150-4152 0.019 ± 0.005 Γ 140 0.72632 ± 0.19142
B+ → D∗0ππππ0 0.018000000 l.4292 0.018 ± 0.004 Γ 141 1.000 ± 0.2222
B+ → D∗0ππππ0π0 0 0 ± 0 1.0 ± 1.0
B+ → D∗0πππππ 0.0057 l.4198 0.0057 ± 0.0012 Γ 142 1.000 ± 0.21053
B+ → D∗0ππππ0π0π0 0 0 ± 0 1.0 ± 1.0
events are discarded due to the lower bound of the lepton momentum, which is set as863
described in Table 20.864
50
To test this assumption, we plot the momentum distribution of the charged hadron865
and lepton. We compare the the total MC expectation before and after the replacement.866
Figure 24 shows the momentum distribution for the three different reconstruction modes867
of B0 mesons. We observe an overall increase in the total yield expectation, which is more868
prominent in the lower momentum regions. 30 presents the expected percentage increase869
in the yield of different decay processes. The increase observed in processes other than870
B → D∗∗ℓν is due to the misreconstruction of the signal side. In the gap samples, the871
second B meson of the event decays generically, and the increase in the B ¯B category is872
attributed to events where the second B meson was reconstructed as a signal B meson873
instead of the resonant gap one.874
0
20
40
60
Events/0.1
```
Belle II L dt = 362 fb 1 B0 → D∗ − (D0 π−) π+
```
After GAP replacementBefore GAP replacement
0
50
100
```
B0 → D∗ − (D0 π−) ρ+
```
After GAP replacementBefore GAP replacement
0
100
200
```
B0 → D∗ − (D0 π−) ` +
```
After GAP replacementBefore GAP replacement
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
0.25
0.00
0.25
after
beforebefore
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
Figure 24: Change of total MC expectation for B0. The largest differences are observed
in the low momentum region of the charged hadron or lepton as expected.
Table 30: Percentage increase in MC expectation for different templates in the B0 recon-
struction
```
Percentage increase in MC expectation (%)
```
```
Decay process B0 → D∗−(D0 π−) π+ B0 → D∗−(D0 π−) ρ+ B0 → D∗−(D0 π−) ℓ+
```
B → D∗τ ν + 0.15 + 0.00 + 0.00
B → D∗ℓν + 0.00 + 0.00 + 0.01
B → D∗∗ℓν + 28.15 + 43.78 + 76.69
B ¯B + 1.06 + 1.38 + 1.97
q ¯q + 0.00 + 0.00 + 0.00
We present the same information for B+ mesons in Figure 25 and Table 31. A similar875
situation is observed with an total increase in the expected yield prominent in the low876
momentum region. The main contribution in this increase comes from B → D∗∗ℓν decays,877
with and additional small contribution from other B ¯B decays, due to reconstruction of878
the second B meson in the gap samples.879
5.8 FF reweighing880
As mentioned in 3.1.6 we use the HAMMER software to reweight the FF models and881
parameters of the B semileptonic decays that survive our full selection. In Table we882
51
0
100
200
300
Events/0.1
```
Belle II L dt = 362 fb 1 B+ → ¯D∗0(D0 π0) π+
```
After GAP replacementBefore GAP replacement
0
200
400
600
```
B+ → ¯D∗0(D0 π0) ρ+
```
After GAP replacementBefore GAP replacement
0
100
200
300
```
B+ → ¯D∗0(D0 π0) ` +
```
After GAP replacementBefore GAP replacement
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
0.25
0.00
0.25
after
beforebefore
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
0.5 1.0 1.5 2.0 2.5
plab+ [GeV]
Figure 25: Change of total MC expectation for B+. The largest differences are observed
in the low momentum region of the charged hadron or lepton as expected.
Table 31: Percentage increase in MC expectation for different templates in the B+ recon-
struction
```
Percentage increase in MC expectation (%)
```
```
Decay process B+ → D∗0(D0 π0) π+ B+ → D∗0(D0 π0) ρ+ B+ → D∗0(D0 π0) ℓ+
```
B → D∗τ ν + 0.00 + 0.00 + 0.00
B → D∗ℓν + 0.00 + 0.00 + 0.00
B → D∗∗ℓν + 16.71 + 17.99 + 119.27
B ¯B + 1.38 + 1.57 + 1.21
q ¯q + 0.00 + 0.00 + 0.00
provide and overview of the FF models and references of the values of the parameters883
that were assumed in the Belle II simulation as well as the target models and parameters884
that the events are reweighted to885
Table 32: FF models and parameters used for the HAMMER reweighting
Decay FF in DECAY.dec Parameters Target FF model Parameters
B → Dℓν BGL [76]
BLPRXP [77]B → Dτ ν CLN [78]B → D∗ℓν BGL [79]
B → D∗τ ν CLN [78]
B → D∗∗1 ℓν
BLR [80] BLR [81]
B → D∗∗1 τ ν
B → D∗∗0 ℓν
B → D∗∗0 τ ν
B → D∗∗1′ ℓν
B → D∗∗1′ τ ν
B → D∗∗2 ℓν
B → D∗∗2 τ ν
Below we provide the set of parameters that have been used for the production of886
52
signal decays with the CLN model in the Belle II MC and the set of BLPRXP parameters887
that we use as a target as an example. The rest set of source and target parameters are888
provided in t Appendix E.889
F1 RhoSq R0 R1 R2value 0.912 1.205 1.15 1.404 0.854
unc 0.014 0.026 0.0 0.032 0.02
F1 RhoSq R0 R1 R2FF model parameters
0.9
1.0
1.1
1.2
1.3
1.4
Value
F1 RhoSq R0 R1 R2FF model parameters
F1
RhoSq
R0
R1
R2
FF model parameters
1 0.34 0 -0.1 -0.071
0.34 1 0 0.57 -0.81
0 0 1 0 0
-0.1 0.57 0 1 -0.76
-0.071 -0.81 0 -0.76 1
Correlation matrix CLN B D*
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 26: Parameters used in the CLN parametrization for the generation of signal decays
in the Belle II MC
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
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
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
0.034 -0.056 0.008 0.009 1 -0.26 -0.094 -0.034 -0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075 -0.076 -0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089 -0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D*
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 27: Target parameters used in the BLPRX parametrization for the reweighting
with HAMMER
5.9 D0 mass calibration890
The mass resolution of the D0 meson is known to be overestimated in Belle II simulated891
data compared to experimental data. This mismatch likely arises from a combination892
of factors, including mismodelling of tracking parameters, the Belle II magnetic field,893
charged hadron identification performance, vertex fitting algorithm efficiency, and poten-894
tial inaccuracies in the simulation of the D0 decay resonance structure and associated fake895
rates for different reconstructed modes. To correct this effect, we use a control channel to896
calibrate the D0 mass resolution. We determine calibration factors, which are then ap-897
plied to smear the reconstructed invariant mass distribution of D0 mesons across different898
53
reconstruction modes. Our results are summarized in Table 33, and the method used to899
determine these factors is detailed in Appendix D.900
Table 33: Smearing factors determined for every different D0 decay mode reconstruction.
Reconstructed decay mode Smearing factor
D0 → K−π+ 0.00198
D0 → K0S π00.00236
D0 → K−π+π0
D0 → K0S π+π−0.00103
D0 → K0S K+K−
D0 → K−π+π−π+ 0.00193
5.10 Continuum calibration901
Since the quality of the modelling of q ¯q processes is a priori unkown in Belle II we use902
off resonance data to constrain the overall normalization of continuum. As described903
in Section 3.3.2 Belle II has collected 42.556 ± 0.007 ± 0.273 fb−1 of off-resonance data904
```
at center of mass energies below the Υ (4S) production energy. We reconstruct these905
```
experimental events using exactly the same reconstruction code and selections as for on-906
resonance experimental data and simulated data. The only difference is that we have to907
shift the cuts on BtagM bc and Btag∆E since the center or mass energy is different. The way that908
we shift the values of the observables is outlined in Appendix J.909
In order to extract scaling factors from the off-resonance data we have to compare the910
observed yield to an expected one based on simulated data. Since off-resonance MC is not911
available at Belle II, we still use the on-resonance one, but ideally the kinematic region912
that we will use has to be statistically independant from the on that is used for all other cal-913
```
ibrations and inference. To that end we choose the M(D0) ∈ [1.78, 1.84]U[1.89, 1.90] GeV914
```
sideband. We also include the double sidebands defined by the selections 1.5 < EECL < 2 GeV,915
1 extra charged track and 0.154 < ∆MD∗+ < 0.4 GeV for B0 and 0.149 < ∆MD∗0 < 0.170 GeV916
for B+, in order to increase statistics. These regions and the availabe statistics are pre-917
sented in Figure 28918
Deriving calibration factors corresponds to simply dividing the observed yield on ex-919
perimental off-resonance data and the expected yield on the continuum MC. For reasons920
that will be discussed further in Section 6.3 we extract calibration factors on a per charge,921
per reconstruction mode an per sign of helicity angle basis, without linking the categories922
```
between different charges or different reconstruction modes. For B0 → D∗−(D0 π−) ρ+and923
```
```
B+ → D∗0(D0 π0) ρ+we also calibrate the backgrounds in the two different regions of924
```
m2miss. Table 34 provides the calibration factors and their respective uncertainties. The925
uncertainties are purely statistical. For the rest of the document these factors are applied926
to all continuum processes on the hadronic reconstruction channels.927
54
Figure 28: Available statistics used for the off-resonance calibration of the continuum.
Table 34: Continuum calibration factors as derived by off-resonace data.
channel and selection q ¯q cal. factor
```
B+ → D∗0(D0 π0) π+ and cos θτhel < 0 1.118 ±0.078
```
```
B+ → D∗0(D0 π0) π+ and cos θτhel > 0 0.922 ±0.098
```
```
B+ → D∗0(D0 π0) ρ+ and cos θτhel < 0 and m2miss < 1 GeV2 0.858 ±0.221
```
```
B+ → D∗0(D0 π0) ρ+ and cos θτhel < 0 and m2miss > 1 GeV2 1.076 ±0.051
```
```
B+ → D∗0(D0 π0) ρ+ and cos θτhel > 0 and m2miss < 1 GeV2 0.916 ±0.107
```
```
B+ → D∗0(D0 π0) ρ+ and cos θτhel > 0 and m2miss > 1 GeV2 0.95 ±0.056
```
```
B0 → D∗−(D0 π−) π+ and cos θτhel < 0 0.957 ±0.162
```
```
B0 → D∗−(D0 π−) π+ and cos θτhel > 0 0.913 ±0.276
```
```
B0 → D∗−(D0 π−) ρ+ and cos θτhel < 0 and m2miss < 1 GeV2 1.215 ±0.64
```
```
B0 → D∗−(D0 π−) ρ+ and cos θτhel < 0 and m2miss > 1 GeV2 0.98 ±0.114
```
```
B0 → D∗−(D0 π−) ρ+ and cos θτhel > 0 and m2miss < 1 GeV2 1.077 ±0.293
```
```
B0 → D∗−(D0 π−) ρ+ and cos θτhel > 0 and m2miss > 1 GeV2 0.931 ±0.139
```
5.11 FEI calibration928
The performance of the FEI algorithm varies across simulated and experimental data,929
making it a common practice to calibrate these discrepancies using a control mode [82].930
```
We have chosen to not utilize the official FEI calibration factors. Currently, the S(L) group931
```
is discussing the potential impact of the signal side on the calibration of the tag side . As932
this issue remains unresolved, we have decided to be cautious and seek a relatively pure933
sideband region enriched in our normalization mode which we will use as a control mode.934
55
Given that B → D∗ℓν decays have been extensively studied in various experiments935
[83] and the BFs have been precisely measured [7], we do not anticipate any new physics-936
related effects in this mode. Although the choice of the FF parametrization might influ-937
ence the shape of the B → D∗ℓν spectrum for any given observable, the overall normal-938
ization should remain unaffected.939
The calibration factors we intend to derive will only be applied to B → D∗τ ν and940
B → D∗ℓν decays, i.e. to correctly reconstructed decays. For background processes, we941
will employ a different calibration strategy. This approach ensures that our signal side942
remains consistent for the normalization modes. The signal modes differ only by the943
```
presence of a charged pion (and an additional neutral pion in the case of τ → ρντ modes)944
```
compared to B → D∗ℓν decays, giving us confidence that the calibration factors will be945
applicable in the SR and NR.946
We choose m2miss as the fitting variable for the extraction of the calibration factors as it947
provides very good discrimination power between B → D∗ℓν decays and other processes.948
Since only an undetectable neutrino is present in correctly reconstructed B → D∗ℓν decays949
we expect these events to be distributed around zero. However since the q2 sideband is950
very clean we are going to perform the fit with a very coarse binning, as the extraction951
of the calibration factors is almost a counting experiment. Figure 29 shows the prefit952
distributions for B0 and B± respectively.953
0
200
400
600
800
1000
1200
1400
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 43.99 (0.0)
```
q2 < 4 GeV Pre-fit
Belle II Preliminary
0
250
500
750
1000
1250
1500
Events / Bin
```
B+ D*0(D0 0) +2 / 3 = 78.44 (0.0)
```
q2 < 4 GeV Pre-fit
```
dt = 362 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
```
Figure 29: Prefit distributions for the FEI calibration in the q2 sideband for B0 (left) and
```
```
B± (right).
```
The main source of background in this sideband is B → D∗∗ℓν decays in the high m2miss954
region. For B± we also find some background events in the negative m2miss region, mainly955
coming from B → Dℓν decays. This is also what motivates the binning of the fit. For B0956
we have one pure bin of B → D∗ℓν decays and second where both signal and background957
processes can be found. For B± we opt for the choice of three bins. The central bin is958
very pure in B → D∗ℓν decays, the first bin mainly contains B → Dℓν decays while the959
last is enriched in B → D∗∗ℓν decays. Before we perform the fit we additionally check960
the modeling of the m2miss observable. We normalize MC to the total number of events961
observed in experimental data and we plot the m2miss distribution with the same binning962
that will be used in the fit. The distributions are presented in Figure 30. The derived963
p-values from the χ2 test imply that the is no mismodelling of the shape of the variable964
at the 5% confidence level, making in it valid choice extracting the yield of B → D∗ℓν965
decays.966
56
0
200
400
600
800
1000
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 1.77 (0.17)
```
q2 < 4 GeV Normalized shapes
Belle II Preliminary
0
200
400
600
800
1000
1200
Events / Bin
```
B+ D*0(D0 0) +2 / 3 = 1.76 (0.15)
```
q2 < 4 GeV Normalized shapes
```
dt = 362 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
Figure 30: Shape comparison between simulated data and experimental data for the FEI
calibration in the q2 sideband.
We will derive the calibration factors using the same aggregation scheme that is being967
used for the official FEI calibration. That is, we calibrate 10 dinstinct modes for in the968
neutral B meson reconstruction and 11 distinct modes in the charged B meson reconstruc-969
tion. We then group all the rest modes that are reconstructed by the FEI in a common970
category. We fit these 23 FEI reconstuctions modes simultaneously. For every FEI re-971
construction mode we extract a calibration factor for the B → D∗ℓν decays while we are972
merging all the background processes into on common templates as we’re interested in973
the strength of B → D∗ℓν decays which will be later used as a calibration factor in the974
SR and NR. These free parameters are not shared between any of the FEI modes, mean-975
ing that the calibration factors are statistically independant across all FEI reconstruction976
modes. However the nuisance parameteres for systematic uncertainties are being shared977
between all reconstruction channels. Those have been derived with the SysVar software978
using the method that has been described in Section 3.1.4 and the eigenvariations have979
been computed simultaneously for all reconstruction channels.980
We first proceed by performing the fit on an Asimov dataset. In Tables 35 and 36981
we provide the expected uncertainties on the Asimov dataset. The first uncertainty is982
the statistical one, while the second one the systematic. For the systematic uncertainty983
we have considered mid to high momentum track finding efficiency, charged and neutral984
```
slow pion efficiency, mid to high energy neutral pion efficiency, D(∗)BF s,B → D∗∗ℓν BFs,985
```
lepton ID efficiency and pion and kaon fakes, hadron ID efficiency for pions and kaons986
and fakes, FF uncertainties and B → Dℓν BF uncertainties.987
We further conduct statistical tests to confirm the validity of the estimator, namely988
investigate potential biases on the calibration factors and test the linear responce of the989
estimator. These tests are presented in Appendix F. We conclude that our simultaneous990
fit is a good estimator of the calibration factors that are needed to tackle the Data/MC991
discrepancy of the FEI efficiency.992
Lastly we’re performing the fit on experimental data. Table 37 shows the extracted993
calibration factors on B0 and 38 on B+. We provide all the post fit distributions in994
```
Appendix K. We get a Goodness of Fit (GoF) p-value of 10.19%. In the rest of this995
```
document we use the values from Table 37 and 38 to scale B → D∗ℓν and B → D∗τ ν996
events in the SR and NR.997
57
Table 35: Signal strengths for B → D∗ℓν which are interpeted as the FEI calibration
factors fit on an Asimov dataset in the B0 channels. The first uncertainty is statistical
while the second is the total systematic uncertainty.
FEI mode calibration factor
D−π+ 1.0 ±0.122 ± 0.069
D−π+π0 1.0 ±0.101 ± 0.057
D−π+π+π− 1.0 ±0.078 ± 0.047
D−π+π+π−π0 1.0 ±0.085 ± 0.051
D0π+π− 1.0 ±0.128 ± 0.068
D−∗π+ 1.0 ±0.131 ± 0.071
D−∗π+π0 1.0 ±0.077 ± 0.047
D−∗π+π+π− 1.0 ±0.077 ± 0.048
D−∗π+π+π−π0 1.0 ±0.084 ± 0.05
Λ−c pπ+π− 1.0 ±0.216 ± 0.113
Rest 1.0 ±0.073 ± 0.045
Table 36: Signal strengths for B → D∗ℓν which are interpeted as the FEI calibration
factors fit on an Asimov dataset in the B+ channels. The first uncertainty is statistical
while the second is the total systematic uncertainty.
FEI mode calibration factor
D0π+ 1.0 ±0.087 ± 0.057
D0π+π0 1.0 ±0.075 ± 0.053
D0π+π+π− 1.0 ±0.064 ± 0.051
D0π+π+π−π0 1.0 ±0.069 ± 0.051
D0∗π+ 1.0 ±0.12 ± 0.072
D0∗π+π0 1.0 ±0.135 ± 0.08
D0∗π+π+π− 1.0 ±0.107 ± 0.065
D0∗π+π+π−π0 1.0 ±0.128 ± 0.074
D−π+π+ 1.0 ±0.2 ± 0.107
D−π+π+π0 1.0 ±0.152 ± 0.085
Λ−c pπ+π−π+ 1.0 ±0.156 ± 0.086
Rest 1.0 ±0.068 ± 0.051
5.12 Photon multiplicity reweighting998
Since several Belle II analysis have observed a mismodelling of the shape of EextraECL we999
are performing a reweighting of the number of photons that are found in the ROE1000
```
build against our Υ (4S) candidates. To that end we choose the ∆M(D∗) sideband in1001
```
```
the B0 → D∗−(D0 π−) ℓ+and B+ → D∗0(D0 π0) ℓ+reconstruction channels as these have1002
```
a significant fraction of correctly reconstructed events.1003
58
Table 37: Signal strengths for B → D∗ℓν and all other background processes in the FEI
calibration fit on experimental data in the B0 channels. The first uncertainty is statistical
while the second is the total systematic uncertainty. We get a GoF p-value of 10.19%.
FEI mode calibration factor
D−π+ 1.019 ±0.124 ± 0.069
D−π+π0 1.124 ±0.106 ± 0.064
D−π+π+π− 0.876 ±0.072 ± 0.041
D−π+π+π−π0 0.74 ±0.073 ± 0.037
D0π+π− 0.854 ±0.117 ± 0.061
D−∗π+ 1.252 ±0.146 ± 0.087
D−∗π+π0 0.499 ±0.054 ± 0.024
D−∗π+π+π− 0.583 ±0.059 ± 0.027
D−∗π+π+π−π0 0.673 ±0.069 ± 0.034
Λ−c pπ+π− 0.74 ±0.186 ± 0.084
Rest 1.091 ±0.066 ± 0.045
Table 38: Signal strengths for B → D∗ℓν and all other background processes in the FEI
calibration fit on experimental data in the B+ channels. The first uncertainty is statistical
while the second is the total systematic uncertainty. We get a GoF p-value of 10.19%.
FEI mode calibration factor
D−π+ 1.019 ±0.124 ± 0.069
D−π+π0 1.124 ±0.106 ± 0.064
D−π+π+π− 0.876 ±0.072 ± 0.041
D−π+π+π−π0 0.74 ±0.073 ± 0.037
D0π+π− 0.854 ±0.117 ± 0.061
D−∗π+ 1.252 ±0.146 ± 0.087
D−∗π+π0 0.499 ±0.054 ± 0.024
D−∗π+π+π− 0.583 ±0.059 ± 0.027
D−∗π+π+π−π0 0.673 ±0.069 ± 0.034
Λ−c pπ+π− 0.74 ±0.186 ± 0.084
Rest 1.091 ±0.066 ± 0.045
In order to derive the photon multiplicity weights we first normalize the MC expecta-1004
tion to the one observed in experimental data. The reason we are not applying the FEI1005
calibration factors that we derived in the low q2 sideband, is that in such case we would1006
```
have to confirm that the derived calibration factors are compatible with the ∆M(D∗)1007
```
sideband. However, since we’re not interested in deriving weights that would affect the1008
normalization of the EextraECL distribution but only the shape, we are argue that deriving1009
scaling factors on the normalized samples is a sufficiently good approximation.1010
We then split the sideband into two regions for every B meson charge, one which1011
is enriched in correctly reconstructed candidates and one enhanced in misreconstructed1012
59
ones. For B0 the selected range is m2miss ∈ [−1, 0.7] GeV 2 for correctly reconstructed1013
events and m2miss ∈ [0.7, 2] GeV 2 for misreconstructed ones. For B+ the selected range1014
is m2miss ∈ [−1, 1] GeV 2 for correctly reconstructed events and m2miss ∈ [1, 2] GeV 2 for1015
misreconstructed ones. Figure 31 shows the distributions based on which we do this split.1016
0
100
200
300
400
500
600
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.0 (1.0)MD* + > 0.148 GeV
```
Normalized shapes
Belle II Preliminary
0
500
1000
1500
2000
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.0 (1.0)MD*0 > 0.149 GeV
```
Normalized shapes
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2
miss in GeV2
-5-3-1
135
NData
NMC2NData + 2N
MC
Figure 31: Normalized shape distribution of m2miss which defines the correctly recon-
structed and misreconstructed enhanced regions where the photon multiplicity reweight-
```
ing i s derived for B0 (left) and B± (right).
```
The weights derived in the correctly reconstructed enhanced samples will be applied1017
to signal B → D∗τ ν events and normalization B → D∗ℓν events. Our Data/MC studies1018
```
which are outlined later in this document (Section 8) indicate that misreconstructed events1019
```
do not contribute to the mismodelling of the EextraECL observable, so it is not necessary to1020
apply correction weights to those events. The weights are derived by dividing the yield1021
in experimental data over the normalized expected one on simulated data in different1022
bins of the photon multiplicity in the ROE. Table 39 shows the derived weights and their1023
respective uncertainties. Figure 32 shows the actual distribution of the ROE photons.1024
The MC has been normalized to Data to isolate shape differences in this observable while1025
disregarding any overall normalization discrepancies that may occur in this sideband.1026
Table 39: Photon multiplicity weights for B0 and B+ for correctly and misreconstructed
events.
B0 B+
Nγ m2miss ∈ [−1, 0.7] GeV 2 m2miss ∈ [0.7, 2] GeV 2 Nγ m2miss ∈ [0, 1] GeV 2 m2miss ∈ [1, 2] GeV 2
0 0.92±0.20 2.3±1.5 0.0 1.30±0.10 2.7±1.0
1 1.10±0.23 0.49±0.30 1.0 1.06±0.06 1.37±0.29
2 1.09±0.26 1.1±0.5 2.0 1.06±0.07 1.08±0.19
3 1.3±0.4 1.5±0.6 3.0 0.86±0.07 0.85±0.16
4-10 0.57±0.22 0.65±0.25 4.0 0.73±0.09 0.82±0.16
5.0 0.49±0.10 0.98±0.24
6.0-10 0.47±0.11 0.52±0.20
60
0
100
200
300
400
Events / Bin
```
B0 D* (D0 ) +MD* + > 0.148 GeV
```
Normalized shapes
Belle II Preliminary
0
200
400
600
800
1000
1200
Events / Bin
```
B+ D*0(D0 0) +MD*0 > 0.149 GeV
```
Normalized shapes
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
0 2 4 6 8 10Number of Photons in ROE-5-3
-11
35
NData
NMC2NData +
2NMC
0 2 4 6 8 10Number of Photons in ROE-5-3
-11
35
NData
NMC2NData +
2NMC
Figure 32: Normalized shape distribution of the ROE photon multiplicity in the high
```
∆M(D∗) where the corrections of Table 39 are derived from for B0 (left) and B± (right)
```
61
6 Signal extraction1027
In Section 5, we have described the set of corrections applied to the simulated data. All1028
these corrections are implemented as correction weights. Table 16 provides an overview1029
```
of the SRs and NRs used to extract the numerator and denominator of R(D∗). For the1030
```
NR, we merge the electron and muon reconstruction modes, as we are not interested in1031
distinguishing between them.1032
In hadronically tagged analyses, extracting the yield of B → D∗ℓν decays is typically1033
achieved by fitting the m2miss distribution. This variable offers strong discriminating power,1034
as only one missing neutrino is expected in the event. Therefore, for B → D∗ℓν decays,1035
the m2miss distribution is expected to peak near zero, in contrast to other misreconstructed1036
decays, which will show larger values of m2miss. This trend is confirmed in Figure 33.1037
We also observe that the main source of background events in the NR are B → D∗∗ℓν1038
```
decays; however, these can be easily distinguished from B → D∗ℓν decays using the m2miss1039
```
distribution.1040
0
1000
2000
3000
4000
Events / Bin
```
B0 D* (D0 ) +NR
```
Belle II Preliminary
0
1000
2000
3000
4000
5000
6000
Events / Bin
```
B+ D*0(D0 0) +NR
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
-1.0 0.25 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
-1.0 0.2 1.1 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
Figure 33: m2miss distribution in the NR. B → D∗ℓν decays peak near zero while all other
contributions are spread in the tails of the distribution.
Even if most of B → D∗ℓν decays are around the peak at 0 GeV2 we still keep the1041
region up to 2 GeV2 in order to extrapolate the overall normalization of the yield for1042
```
background processes (mainly the B → D∗∗ℓν) component to the handful of events that1043
```
can be found under the m2miss peak. This becomes even more evident if we plot m2miss1044
using a log scale for the y-axis in Figure 34.1045
101
102
103
Events / Bin
```
B0 D* (D0 ) +NR
```
Belle II Preliminary
102
103
Events / Bin
```
B+ D*0(D0 0) +NR
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
-1.0 0.25 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
-1.0 0.2 1.1 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
Figure 34: m2miss distribution in the NR using a log scale on the y axis for better visibility
of the background distributions.
62
In B → D∗τ ν decays, where the τ lepton decays hadronically, there are two missing1046
neutrinos in the event. As a result, these decays do not peak at zero in the m2miss squared1047
distribution but instead exhibit a continuous spectrum with positive m2miss values. An-1048
other effective method for distinguishing such decays is by analyzing the extra energy1049
```
detected in the calorimeter (EextraECL ). Since the undetectable neutrinos leave no signal in1050
```
the detector, correctly reconstructed decays are expected to peak at values close to zero,1051
while background events typically result in larger values of EextraECL . This holds true for1052
nearly all background processes, except for cases where a lepton is mistakenly identified1053
as the charged hadron reconstructed as the daughter of the τ lepton. This is mainly true1054
for the reconstruction modes where the τ lepton decays into a charged pion and a neu-1055
trino. For the modes where the τ lepton decays into a ρ meson and a neutrino, this effect1056
is less prominent due to the presence of an additional neutral pion. This is illustrated in1057
Figure 35.1058
0
20
40
60
80
100
120
```
Events / (0.12 GeV)
```
```
B0 D* (D0 ) +SR
```
Belle II Preliminary
0
25
50
75
100
125
150
```
Events / (0.12 GeV)
```
```
B0 D* (D0 ) +SR
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
extra E in ECL in GeV-5-3
-113
5
NData
NMC
2NData +
2NMC
extra E in ECL in GeV-5-3
-113
5
NData
NMC
2NData +
2NMC
0
50
100
150
200
```
Events / (0.12 GeV)
```
```
B+ D*0(D0 0) +SR
```
0
100
200
300
400
```
Events / (0.12 GeV)
```
```
B+ D*0(D0 0) +SR B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC
2NData +
2NMC
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC
2NData +
2NMC
Figure 35: EextraECL distribution in the SR. B → D∗τ ν decays peak near zero. All other
background sources peak toward larger values of EextraECL except B → D∗ℓν decays, making
it hard to distinguish them from signal processes.
These fake hadrons correspond to B → D∗ℓν events, whose distribution of unassigned1059
energy in the calorimeter closely resembles that of B → D∗τ ν decays, making it extremely1060
challenging to distinguish between the two. Misreconstructed decays like these will peak1061
around zero in m2miss since they involve only one undetected neutrino. To improve sepa-1062
ration, we choose to fit the EextraECL distribution in two bins of m2miss: one for values around1063
0, i.e., [-1, 1] GeV, and another for higher m2miss values. This approach enhances the1064
discrimination power between signal and normalization events. The effectiveness of this1065
strategy is evident in Figure 36, where we present the final 2D projections for the SR and1066
the m2miss distributions for the NR.1067
In Figure 36 a finer categorization of the events has been chosen for illustration pur-1068
63
0
500
1000
1500
2000
2500
Events / Bin
```
B0 D* (D0 ) +NRBelle II Preliminary
```
020
4060
80100
120
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +SR m2miss [ 1, 1] m2miss (1, 7]
```
0
50
100
150
200
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +SR m2miss [ 1, 1] m2miss (1, 7]
```
```
dt = 365 fb 1B D* ( )
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccMC stat. unc.
Asimov Data
m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
EECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
EECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
500
1000
1500
2000
2500
Events / Bin
```
B+ D*0(D0 0) +NR
```
0
50
100
150
200
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +SR m2miss [ 1, 1] m2miss (1, 7]
```
0
200
400
600
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +SR m2miss [ 1, 1] m2miss (1, 7] B D* ( )B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccMC stat. unc.
Asimov Data
-1.0 0.2 1.1 2.0m2miss in GeV2-5-3-1
135NData NMC2NData + 2NMC
0.125 0.375 0.625 0.825 0.125 0.125 0.375 0.625 0.825 0.125EECL in GeV-5-3-1
135NData NMC2NData + 2NMC
0.125 0.375 0.625 0.825 0.125 0.125 0.375 0.625 0.825 0.125EECL in GeV-5-3-1
135NData NMC2NData + 2NMC
```
Figure 36: Final fit distributions used for the R(D∗) fit.
```
```
poses. We will perform the final fit for the extraction of R(D∗) in five different categories1069
```
as this gives us the highest sensitivity. The final categories for the fit are presented in1070
Table 40.1071
Table 40: Final templates for the fit
```
B0 → D∗τ ν B0 → D∗τ (π ν) ν , B0 → D∗τ (ρ ν) ν
```
```
B+ → D∗τ ν B+ → D∗τ (π ν) ν , B+ → D∗τ (ρ ν) ν
```
B0 → D∗ℓν B0 → D∗ℓν
B+ → D∗ℓν B+ → D∗ℓν
B → D∗∗ℓν B → D∗∗ℓν
```
tau misID B → D∗τ ν (τ crossfeed)
```
B ¯B B → D∗ + n · hu, B → HcHcXs, B → Dτ ν, B → Dℓν, other B ¯B
q ¯q uubar, ddbar, ssbar, ccbar
```
6.1 R(D∗) parametrization1072
```
```
The theoretical definition of R(D∗) is given by Equation 14, where ℓ stands for the two1073
```
light leptons, electrons and muons.1074
```
R(D∗) =
```
```
B(B → D∗τ ν)
```
```
B(B → D∗ℓν)
```
```
(14)1075
```
```
The R(D∗) ratio is an excellent test of LFU and is commonly preferred over a direct1076
```
determination of the B → D∗τ ν branching fraction. This preference is due to the assump-1077
tion that several systematic uncertainties, which are common to both the numerator and1078
denominator, will cancel out in the ratio. Experimentally, the ratio is typically expressed1079
```
as:1080
```
```
R(D∗) = 2 ·
```
νD∗0τ + · ϵ−1D∗0τ + + νD∗−τ + · ϵ−1D∗−τ +
νD∗0ℓ+ · ϵ−1D∗0ℓ+ + νD∗−ℓ+ · ϵ−1D∗−ℓ+
```
(15)1081
```
64
where, ν represents the determined yield of the fitted template, while ϵ accounts for1082
any reconstruction efficiency that needs to be considered when performing the fit. For1083
the assumption to hold when fitting neutral and charged B mesons simultaneously, the1084
reconstruction efficiencies for both charges must be identical. However, it is well known1085
within Belle II that certain reconstruction efficiencies differ between charged and neutral1086
B mesons. A key example, especially relevant for semileptonic analyses like this one, is1087
the discrepancy in the FEI reconstruction efficiency for the two B meson charges. This1088
effect becomes apparent when examining the official FEI calibration factors [82].1089
To address this issue, instead of directly fitting the yields of B → D∗τ ν and B → D∗ℓν,1090
```
we employ a parametrization based on isospin symmetry, allowing us to fit the R(D∗) ratio1091
```
directly. This approach ensures that most reconstruction efficiencies appear as ratios in1092
the parametrization, leading to the cancellation of common effects, while those that do1093
not cancel are accounted for appropriately. The first time that this parametrization was1094
```
used was in the hadronically tag R(D∗) measurement by Belle [84]. Here we derive the1095
```
parametrization again to adapt it to the terminology that is required for a fit implemented1096
with pyhf.1097
```
We begin considering only one charge for the B mesons. R(D∗) is expressed as1098
```
```
R(D∗) =
```
1
2
·
Ns
Nn
```
(16)1099
```
where Ns and Nn are the true signal and normalization events, while the factor of 21100
arises from the fact that two generation of light leptons are used in the denominator.1101
The true events are connected to the experimental yields via1102
νs/n = Ns/n · ϵs/n ·
KY
```
i=k
```
```
ζis/n (17)1103
```
where ν are the experimental yields, ϵ the reconstruction efficiency on MC and ζi the effi-1104
ciency associated a to normalization effect i arising from corrections applied to simulated1105
data, e.g. charged slow pion efficiency correction or LID efficiency correction etc. ζi con-1106
trols solely the impact of every systematic effect in the absolute yield of every templates1107
and doesn’t affect the shape of the template. The latter effect is treated separately.1108
Isospin symmetry connect the decay rates or BFs of for neutral and charged B mesons1109
as1110
τ M C+0 =
1
τ M C0+
=
τB±
τB0
=
```
Γ(B0)
```
```
Γ(B±)
```
=
```
B(B0)
```
```
B(B±)
```
```
(18)1111
```
where τB is the lifetime of B mesons and τ+0 the ratio of lifetimes for charged and1112
neutral B mesons.1113
By combining Equations 16, 17 and 18 we arrive at the base of our parametrization1114
for the experimental yields1115
65
νs0cb =
1
2
```
R(D∗) · νn±cb ·
```
ϵs0
ϵn±
· τ M C+0 ·
KY
```
i=k
```
ζsi0
ζin±
```
(19)1116
```
νs±cb =
1
2
```
R(D∗) · νn±cb ·
```
ϵs±
ϵn±
·
KY
```
i=k
```
ζis±
ζin±
```
(20)1117
```
νn0cb = νn±cb ·
ϵn0
ϵn±
· τ M C+0 ·
KY
```
i=k
```
ζin0
ζin±
```
(21)1118
```
```
νn±cb = νn±cb (22)1119
```
where the superscipt s0 denotes signal events in B0 meson decays, n0 B0 → D∗ℓν1120
decays and so on. The cb superscipt stands for channel and bin, as these are taken into1121
account separately when the likelihood is being built.1122
Now all the experimental yields associated with the signal and normalization processes1123
are a function of the experimental yield of charged B meson B → D∗ℓν processes νnB± .1124
As described in Table 2 the experimental yields are determined via normfactor modifiers1125
in pyhf. This translates the experimental yield of the charged B meson normalization1126
modes into:1127
```
νn± = µn± · N recon± (23)1128
```
where N reconB± are the reconstructed events of the charged B meson B → D∗ℓν template1129
in all the reconstruction regions and µnB± is the normfactor modifier associated to the1130
yield.1131
Now for the ratios of reconstruction efficiencies ϵ that appear in the parametrization1132
the usual efficiency formula hold ϵ = NrecoNgen with Ngen being the true number of generated1133
```
events Ngen = NB ¯B ·B(Υ (4S) → B ¯B)·2·B(decay of interest) with the factor of 2 appearing1134
```
since both B mesons of the event can decay into the decay of interest. Therefore the1135
relevant efficiencies transform into1136
ϵs0 =
N recos0
```
2 · NBB · B(Υ (4S) → B0B0) · B(B0 → D∗τ ν)
```
```
(24)1137
```
ϵs± =
N recos±
```
2 · NBB · B(Υ (4S) → B+B−) · B(B+ → D∗τ ν)
```
```
(25)1138
```
ϵn0 =
N recon0
```
2 · NBB · B(Υ (4S) → B0B0) · 2 · B(B0 → D∗ℓν)
```
```
(26)1139
```
ϵn± =
N recon±
```
2 · NBB · B(Υ (4S) → B+B−) · 2 · B(B+ → D∗ℓν)
```
```
(27)1140
```
with the extra factor of two appearing in the efficiencies of the normalization modes1141
if we assume that the BFs of B → D∗eν and B → D∗µν are exactly the same. Now if we1142
```
use Equation 18 to introduce isospin symmetry and consider the ratio of Υ (4S) to two1143
```
charged B mesons over neutral B mesons that was assumed in the Belle II simulation1144
66
f M C+0 =
f M C+−
f M C00
=
```
B(Υ (4S) → B+B−)
```
```
B(Υ (4S) → B0B0)
```
```
(28)1145
```
then the efficiencies become1146
ϵs0 =
N recos0
```
2 · NBB · B(Υ (4S) → B0B0) · B(B+ → D∗τ ν) · τ M C+0 ·
```
```
(29)1147
```
ϵs± =
N recos0
```
2 · NBB · f M C+0 · B(Υ (4S) → B0B0) · B(B+ → D∗τ ν)·
```
```
(30)1148
```
ϵn0 =
N recon0
```
2 · NBB · B(Υ (4S) → B0B0) · 2 · B(B+ → D∗ℓν) · τ M C+0 ·
```
```
(31)1149
```
ϵn± =
N recon±
```
2 · NBB · f M C+0 · B(Υ (4S) → B0B0) · 2 · B(B+ → D∗ℓν)·
```
```
(32)1150
```
Now if we also use Equation 23, Equations 19, 20, 21 and 22 become1151
```
νs0 = R(D∗) · µn± · N recos0 ·
```
f M C+0
R∗M C
KY
```
i=k
```
·
ζis0
ζin±
```
(33)1152
```
```
νs± = R(D∗) · µn± · N recos± ·
```
1
R∗M C
·
KY
```
i=k
```
ζis±
ζin±
```
(34)1153
```
νn0 = µn± · N recon0 · f M C+0 ·
KY
```
i=k
```
ζin0
ζin±
```
(35)1154
```
```
νn± = µn± · N recon± (36)1155
```
```
where R∗M C is the SM expectation for R(D∗), and f M C+0 the ratio of Υ (4S) that are1156
```
expected to decay into two charged B mesons over neutral B mesons as defined in Equation1157
28. This value is found to be 1.066 in the DECAY.dec file of relase-06, while the BF of1158
τ → πντ is 0.109 and the one of τ → ρντ 0.255. All of these values are the ones used in1159
the Belle II simulation. All other term that are appearing in the ratio are canceling out1160
as demonstrated in the above.1161
We implement the fit using the aforementioned parametrization as a maximum likeli-1162
hood fit using pyhf. The general from of the specified likelihood is1163
```
f (η, α|η, χ) =
```
Y
c∈channels
Y
b∈binsc
```
Pois(ncb|νcb(η, χ))
```
Y
χ∈χ
```
cχ(αχ|χ) (37)1164
```
where the second term constraints the χ terms from some auxiliary measurements αχ1165
```
of the parameters χ. The term νcb(η, χ) contains the set of unconstrained parameters1166
```
η and the constrained ones χ. Taking into account all the templates in the fit this is1167
```
expressed as;1168
```
67
X
s∈samples
```
νscb(η, χ) =
```
X
s∈samples
```
(
```
Y
```
κ ∈ κκscb(η, χ))(ν0scb(η, χ +
```
X
∆∈∆
```
∆scb(η, χ)) (38)1169
```
where the term
Q
```
κ ∈ κκscb(η, χ) is multiplied to the nominal rate ν0scb while the term1170 P
```
```
∆∈∆ ∆scb(η, χ) is being added to it. These terms are implemented as pyhf modifiers in1171
```
the fit as defined in Table 2.1172
6.2 Pτ parametrization1173
```
An important goal of this analysis is to measure Pτ simultaneously together with R(D∗).1174
```
As explained in 5.2 we aim at measuring Pτ as an asymmetry of positive and negative τ1175
helicity events. In order to incorporate Pτ into our parametrization we modify Equation1176
16 to 39 and we introduce Equation 40.1177
```
R(D∗) =
```
N θ+s + N θ−s
Nn
```
(39)1178
```
Pτ =
2
α
N θ+s − N θ−s
N θ+s + N θ−s
```
(40)1179
```
where N θ+s and N θ−s are events with positive and negative helicity angle respectively1180
and the coefficient α is a coefficient expressing the sensitivity of the different τ decays to1181
Pτ as explained in 5.2.1182
We are not deriving the full parametrization from scratch as all the steps are identical1183
to 6.1. The final parametrization differs only on an extra free and unconstrained factor1184
1 ± α2 Pτ and of course the indices of all efficiencies are modified to their new respective1185
templates.1186
```
νs0θ+ = R(D∗) · (1 +
```
α
2
```
Pτ ) · µn± · N recos0θ+·
```
f M C+0
```
R∗M C · (1 + α2 Pτ SM )
```
KY
```
i=k
```
·
ζis0
θ+
ζin±
```
(41)1187
```
```
νs0θ− = R(D∗) · (1 −
```
α
2
```
Pτ ) · µn± · N recos0θ−·
```
f M C+0
```
R∗M C · (1 − α2 Pτ SM )
```
KY
```
i=k
```
·
ζis0
θ−
ζin±
```
(42)1188
```
```
νs±θ+ = R(D∗) · (1 +
```
α
2
```
Pτ ) · µn± · N recos±
```
θ+
·
1
```
R∗M C · (1 + α2 Pτ SM )
```
·
KY
```
i=k
```
ζis±
θ+
ζin±
```
(43)1189
```
```
νs±θ− = R(D∗) · (1 −
```
α
2
```
Pτ ) · µn± · N recos±
```
θ−
·
1
```
R∗M C · (1 − α2 Pτ SM )
```
·
KY
```
i=k
```
ζis±
θ−
ζin±
```
(44)1190
```
νn0 = µn± · N recon0 · f M C+0 ·
KY
```
i=k
```
ζin0
ζin±
```
(45)1191
```
```
νn± = µn± · N recon± (46)1192
```
68
In order to be able to distinguish between events with positive and negative helicity1193
we now transform the 2D projections shown in Figure 36 into a 3D projection where we1194
include the reconstructed helicity angle. The way that we access this information has1195
been described in 5.2. The final distributions can be seen in Figure 37.1196
0
500
1000
1500
2000
2500
Events / Bin
```
B0 D* (D0 ) +NRBelle II Preliminary
```
0
20
40
60
80
100
120
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +SR
```
```
m2miss [ 1, 1] m2miss ( 1, 7]
```
cos hel [ 2, 0]
```
m2miss [ 1, 1] m2miss (1, 7]
```
cos hel [0, 3]0
50
100
150
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +SR
```
```
m2miss [ 1, 1] m2miss ( 1, 7]
```
cos hel [ 1.2, 0]
```
m2miss [ 1, 1] m2miss (1, 7]
```
cos hel [0, 3]
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
EECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
EECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
500
1000
1500
2000
2500
Events / Bin
```
B+ D*0(D0 0) +NR
```
0
50
100
150
200
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +SR
```
```
m2miss [ 1, 1] m2miss ( 1, 7]
```
cos hel [ 1.6, 0]
```
m2miss [ 1, 1] m2miss (1, 7]
```
cos hel [0, 3]0
100
200
300
400
500
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +SR
```
```
m2miss [ 1, 1] m2miss ( 1, 7]
```
cos hel [ 1, 0]
```
m2miss [ 1, 1] m2miss (1, 7]
```
cos hel [0, 3]
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
-1.0 0.2 1.1 2.0m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
0.156250.468750.781251.093750.156250.468750.781251.093750.156250.468750.781251.093750.156250.468750.781251.09375EECL in GeV
-5-3-1
135
NData
NMC2NData + 2NMC
0.156250.468750.781251.093750.156250.468750.781251.093750.156250.468750.781251.093750.156250.468750.781251.09375EECL in GeV
-5-3-1
135
NData
NMC2NData + 2NMC
```
Figure 37: Final fit distributions used for the R(D∗) and Pτ fit.
```
Of course we are interested in the true helicity angle and not the reconstructed one1197
as resolution effects that could lead to migrations are expected. We calculate the true1198
helicity angle and we provide the confusion matrices in Figure 38. We avoid displaying1199
information on the true helicity in Figure 37 to maintain readability on such an already1200
busy final distribution.1201
```
We now split our signal templates even further in order to fit Pτ alongside R(D∗). For1202
```
the template creation we use the true helicity angle and not the reconstructed one as this1203
```
makes a later unfolding of our result redundant. The final categories for the R(D∗) and1204
```
Pτ fit are presented in Table 41. The results of the Asimov fit are presented in 43.1205
6.3 Sideband and Control regions1206
Figure 36 shows that a few different backgrounds processes can fake the decays of interest,1207
namely B → D∗τ ν and B → D∗ℓν, even after the tighter selections. These can be1208
categorized in three main components: B → D∗∗ℓν decays, other BB and continuum1209
processes. Some of these processes such as B → D∗∗ℓν and the continuum decays are1210
well known to be mismodeled in the Belle II MC. q ¯q processes are well constrained by1211
our continuum calibration as this is described in 5.10. For BB processes the situation1212
depends heavily on the signal side reconstruction and the level to which these decays1213
are modeled correctly is not a priori known. The overall yield for these processes might1214
differ between simulated and experimental data. In order to ensure that these processes1215
```
will not affect the extraction of R(D∗) we need to find sideband regions which can be1216
```
used in order to constraint these background processes in the SR and NR. After extensive1217
69
```
(-1, 0] (0, 1]cos true
```
hel
```
(-2, 0]
```
```
(0, 3]
```
cos
recohel
53.9% 15.5%
6.9% 22.0%
```
B0 D* (D0 ) + (90.68 signal events)
```
```
(-1, 0] (0, 1]cos true
```
hel
```
(-1.2, 0.0]
```
```
(0.0, 3.0]
```
cos
recohel
28.2% 6.1%
17.4% 42.2%
```
B0 D* (D0 ) + (85.08 signal events)
```
```
(-1, 0] (0, 1]cos true
```
hel
```
(-1.6, 0.0]
```
```
(0.0, 3.0]
```
cos
recohel
54.7% 13.3%
7.3% 23.2%
```
B+ D*0(D0 0) + (196.98 signal events)
```
```
(-1, 0] (0, 1]cos true
```
hel
```
(-1, 0]
```
```
(0, 3]
```
cos
recohel
33.0% 7.5%
15.6% 41.5%
```
B+ D*0(D0 0) + (152.49 signal events)
```
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Figure 38: Confusion matrix between the true generated cosinus of the helicity angle and
the reconstructed one.
```
Table 41: Final templates for the R(D∗) and Pτ fit
```
```
B0 → D∗τ (→ πν)ν + B0 → D∗τ (π ν) ν and cos θτhel > 0
```
```
B0 → D∗τ (→ πν)ν − B0 → D∗τ (π ν) ν and cos θτhel < 0
```
```
B0 → D∗τ (→ ρν)ν + B0 → D∗τ (ρ ν) ν and cos θτhel > 0
```
```
B0 → D∗τ (→ ρν)ν − B0 → D∗τ (ρ ν) ν and cos θτhel < 0
```
```
B+ → D∗τ (→ πν)ν + B+ → D∗τ (π ν) ν and cos θτhel > 0
```
```
B+ → D∗τ (→ πν)ν − B+ → D∗τ (π ν) ν and cos θτhel < 0
```
```
B+ → D∗τ (→ ρν)ν + B+ → D∗τ (ρ ν) ν and cos θτhel > 0
```
```
B+ → D∗τ (→ ρν)ν − B+ → D∗τ (ρ ν) ν and cos θτhel < 0
```
B0 → D∗ℓν B0 → D∗ℓν
B+ → D∗ℓν B+ → D∗ℓν
B → D∗∗ℓν B → D∗∗ℓν
```
tau misID B → D∗τ ν (τ crossfeed)
```
B ¯B B → D∗ + n · hu, B → HcHcXs, B → Dτ ν, B → Dℓν, other B ¯B
q ¯q uubar, ddbar, ssbar, ccbar
studies in different sidebands we managed to find suitable regions that enable us to safely1218
constrain the different background processes in the SR and NR. Our studies tried to1219
ensure that the sidebands that were chosen demonstrate a similar perfomance of the FEI1220
on those events between the SR and the chosen sidebands. Another imporantan aspect is1221
that the contribution of the different individual decays that make up the aforementioned1222
BB subcategories are similar between the SR and the sidebands. Since a lot of these1223
decays have never been measured the assumed BFs in the Belle II DECAY.dec file are1224
most of the time purely educated guesses, so we wish to pursue a data driven strategy1225
70
of constraining these decays. We constrain the background processes on a per charge,1226
per reconstruction mode an per sign of helicity angle basis, without linking the categories1227
```
between different charges or different reconstruction modes. For B0 → D∗−(D0 π−) ρ+and1228
```
```
B+ → D∗0(D0 π0) ρ+we also calibrate the backgrounds in the two different regions of m2miss1229
```
as Data/MC studies have revealed that the normalization of the backgrounds in these two1230
kinematics regions is different.1231
In what follows we demonstrate why these kinematic regions are appropriate choices1232
for constraining certain types of background processes.1233
Generic B ¯B decays is a category of processes that is present in the SR but not well1234
modeled in the Belle II MC. The decay processes that are included in this category include1235
B → HcHcXs, B → D∗ +n·hu, Other B ¯B and the Combinatorial background. We use the1236
```
one extra charged track sideband to constrain BB decays in the B0 → D∗−(D0 π−) π+and1237
```
```
B+ → D∗0(D0 π0) π+and channels and the high EextraECL sideband defined as 1.5 < EextraECL <1238
```
```
2 GeV in the B0 → D∗−(D0 π−) ρ+and B+ → D∗0(D0 π0) ρ+to constrain these decays.1239
```
We first compare the performance of the FEI on misreconstructed B ¯B events between1240
four regions of interest. We include only the FEI modes in which we find at least 201241
events, so that the uncertainties and the χ2 statistic that we calculate are sensible.1242
Figure 39 and 40 shows the percentages of the different decay modes reconstructed1243
```
by the FEI for the four regions of interest for the B0 → D∗−(D0 π−) π+channel in the1244
```
positive and negative helicity bins. Since both the one extra charged track and the high1245
EextraECL regions are compatible with the SR we choose to use the one extrac charged track1246
region due to higher statistics and better compatiblity of the background composition.1247
In Appendix J we provide several plots that test the compatibility of the background1248
composition as per the request of the WG reviewers.1249
0.0 2.0 4.0 6.0 8.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
D + +
D + + 0
D * + 0
D * + +
Rest
```
B0 → D∗ − (D0 π−) π+ after all selections (cos θ τhel < 0)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 13.75/5, p = 0.017
5 0 5rSR rtrack√
2SR + 2track
2 = 8.98/5, p = 0.110
5 0 5rSR rECL√
2SR + 2ECL
2 = 4.55/5, p = 0.473
5 0 5rDst rtrack√
2Dst + 2track
2 = 9.67/5, p = 0.085
5 0 5rDst rECL√
2Dst + 2ECL
2 = 13.56/5, p = 0.019
5 0 5rtrack rECL√
2track + 2ECL
2 = 8.76/5, p = 0.119
```
Figure 39: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) π+in the
```
negative helicity bin.
```
Figures 41 - 44 provide the same test for the B0 → D∗−(D0 π−) ρ+. Based on these1250
```
findings we choose the high EextraECL sideband.1251
71
0.02.04.06.08.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
Rest
```
B0 → D∗ − (D0 π−) π+ after all selections (cos θ τhel > 0)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 0.00/1, p = 1.000
5 0 5rSR rtrack√
2SR + 2track
2 = 0.00/1, p = 1.000
5 0 5rSR rECL√
2SR + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rDst rtrack√
2Dst + 2track
2 = 0.00/1, p = 1.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rtrack rECL√
2track + 2ECL
2 = 0.00/1, p = 1.000
```
Figure 40: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) π+in the
```
positive helicity bin.
0.02.04.06.08.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
Rest
```
B0 → D∗ − (D0 π−) ρ+ after all selections (cos θ τhel < 0 & m2miss < 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 0.00/1, p = 1.000
5 0 5rSR rtrack√
2SR + 2track
2 = 0.00/1, p = 1.000
5 0 5rSR rECL√
2SR + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rDst rtrack√
2Dst + 2track
2 = 0.00/1, p = 1.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rtrack rECL√
2track + 2ECL
2 = 0.00/1, p = 1.000
```
Figure 41: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the
```
negative helicity bin and low m2miss.
```
Figures 45 and 46 provide the same test for the B+ → D∗0(D0 π0) π+. Based on these1252
```
findings we choose the one extra charged track sideband.1253
```
Figures 47 - 50 provide the same test for the B+ → D∗0(D0 π0) ρ+. Based on these1254
```
findings we choose the high EextraECL sideband.1255
For the extraction variable we fine tune 1D or 2D binnings of combinations of the1256
difference of the invariant masses of the D∗± and D0 mesons, mass of the D0 meson or1257
cosTBTO as they provide good discrimination power between B ¯B events compared to q ¯q,1258
which are the main backgrounds in these regions.1259
All the above results together with Appendix J indicate that the chosen sidebands are1260
72
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D +
D + 0
D + +
D + + 0
D0 +
D * + 0
D * + +
D * + + 0
c p +
Rest
```
B0 → D∗ − (D0 π−) ρ+ after all selections (cos θ τhel < 0 & m2miss > 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 54.26/10, p = 0.000
5 0 5rSR rtrack√
2SR + 2track
2 = 25.86/10, p = 0.004
5 0 5rSR rECL√
2SR + 2ECL
2 = 14.59/10, p = 0.148
5 0 5rDst rtrack√
2Dst + 2track
2 = 53.86/10, p = 0.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 26.43/10, p = 0.003
5 0 5rtrack rECL√
2track + 2ECL
2 = 9.61/10, p = 0.475
```
Figure 42: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the
```
negative helicity bin and high m2miss.
0.02.04.06.08.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
D + +
Rest
```
B0 → D∗ − (D0 π−) ρ+ after all selections (cos θ τhel > 0 & m2miss < 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 3.31/2, p = 0.191
5 0 5rSR rtrack√
2SR + 2track
2 = 0.25/2, p = 0.881
5 0 5rSR rECL√
2SR + 2ECL
2 = 0.82/2, p = 0.664
5 0 5rDst rtrack√
2Dst + 2track
2 = 4.35/2, p = 0.113
5 0 5rDst rECL√
2Dst + 2ECL
2 = 4.84/2, p = 0.089
5 0 5rtrack rECL√
2track + 2ECL
2 = 0.27/2, p = 0.875
```
Figure 43: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the
```
positive helicity bin and low m2miss.
appropriate regions for constraining the B ¯B events in the SR. Combining this with the1261
constraints determined on off-resonance data for q ¯q events, which will be applied on both1262
SR and control regions, we are confident that the main two background sources in the SR1263
will be properly constrained.1264
Rather than using a two-step calibration process —where we would first perform a1265
fit and then apply a calibration factor to the B ¯B events in the SR, we will fit these1266
control regions simultaneously with the SR and NR. This approach allows the yields of1267
B ¯B template in the SR and NR to be constrained directly from the control regions while1268
consistently addressing systematic uncertainties.1269
73
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D + 0
D + +
D + + 0
D * + 0
D * + +
D * + + 0
Rest
```
B0 → D∗ − (D0 π−) ρ+ after all selections (cos θ τhel > 0 & m2miss > 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 66.80/7, p = 0.000
5 0 5rSR rtrack√
2SR + 2track
2 = 22.02/7, p = 0.003
5 0 5rSR rECL√
2SR + 2ECL
2 = 4.52/7, p = 0.719
5 0 5rDst rtrack√
2Dst + 2track
2 = 52.95/7, p = 0.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 19.44/7, p = 0.007
5 0 5rtrack rECL√
2track + 2ECL
2 = 1.92/7, p = 0.964
```
Figure 44: FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the
```
positive helicity bin and high m2miss.
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D0 +
D0 + 0
D0 + 0 0
D0 + +
D0 + + 0
D0 * +
D0 * + 0
D0 * + +
D0 * + + 0
D + + 0
Rest
```
B+ → ¯D∗0(D0 π0) π+ after all selections (cos θ τhel < 0)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 6.90/11, p = 0.807
5 0 5rSR rtrack√
2SR + 2track
2 = 5.53/11, p = 0.903
5 0 5rSR rECL√
2SR + 2ECL
2 = 14.12/11, p = 0.227
5 0 5rDst rtrack√
2Dst + 2track
2 = 7.08/11, p = 0.793
5 0 5rDst rECL√
2Dst + 2ECL
2 = 15.06/11, p = 0.180
5 0 5rtrack rECL√
2track + 2ECL
2 = 16.67/11, p = 0.118
```
Figure 45: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) π+in the
```
negative helicity bin.
In Table 42 we present and overview of the definitions of the regions to be fitted, the1270
motivation, the observable that is fitted and the binning used.1271
6.4 Sensitivity on Asimov data1272
To validate that the maximum likelihood fit is performing as expected, we begin by per-1273
forming the fit on an Asimov dataset. Initially, we conduct the fit without including the1274
control regions that constrain the backgrounds, but instead fixing them to their expected1275
values. This represents an idealized scenario where we fully trust the Belle II MC. How-1276
74
0.0 2.0 4.0 6.0 8.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
D0 +
D0 + 0
D0 + +
D0 + + 0
Rest
```
B+ → ¯D∗0(D0 π0) π+ after all selections (cos θ τhel > 0)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 1.30/5, p = 0.935
5 0 5rSR rtrack√
2SR + 2track
2 = 1.79/5, p = 0.878
5 0 5rSR rECL√
2SR + 2ECL
2 = 5.91/5, p = 0.315
5 0 5rDst rtrack√
2Dst + 2track
2 = 6.14/5, p = 0.293
5 0 5rDst rECL√
2Dst + 2ECL
2 = 6.56/5, p = 0.256
5 0 5rtrack rECL√
2track + 2ECL
2 = 4.18/5, p = 0.524
```
Figure 46: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) π+in the
```
positive helicity bin.
0.02.04.06.08.010.012.014.016.018.020.022.024.026.028.030.0Tag decay mode contribution in %
Rest
```
B+ → ¯D∗0(D0 π0) ρ+ after all selections (cos θ τhel < 0 & m2miss < 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 0.00/1, p = 1.000
5 0 5rSR rtrack√
2SR + 2track
2 = 0.00/1, p = 1.000
5 0 5rSR rECL√
2SR + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rDst rtrack√
2Dst + 2track
2 = 0.00/1, p = 1.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 0.00/1, p = 1.000
5 0 5rtrack rECL√
2track + 2ECL
2 = 0.00/1, p = 1.000
```
Figure 47: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the
```
negative helicity bin and low m2miss.
ever, as discussed in Section 6.3, this assumption is unrealistic, as several B ¯B and q ¯q1277
processes are known to be mismodeled in the Belle II MC. Next, we explore the opposite1278
extreme, where all backgrounds are allowed to float freely in the fit. This combined with1279
```
the previous exercise provides the possible uncertainty range for R(D∗) based on the cur-1280
```
rent statistical power, as any background-constraining strategy would yield an uncertainty1281
that falls between these two extremes.1282
Before performing the full fit with all regions included, we first run the fit using only1283
the control regions. This step confirms that the chosen control regions offer better sensi-1284
tivity in estimating the background yields compared to the SR and NR. Thus, including1285
75
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D0 +
D0 + 0
D0 + 0 0
D0 + +
D0 + + 0
D0D0K +
D0 * +
D0 * + 0
D0 * + +
D0 * + + 0
D + +
D + + 0
c p + 0
c p + +
D0pp +
D0 * pp +
Rest
```
B+ → ¯D∗0(D0 π0) ρ+ after all selections (cos θ τhel < 0 & m2miss > 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 25.60/17, p = 0.082
5 0 5rSR rtrack√
2SR + 2track
2 = 61.60/17, p = 0.000
5 0 5rSR rECL√
2SR + 2ECL
2 = 20.65/17, p = 0.242
5 0 5rDst rtrack√
2Dst + 2track
2 = 58.32/17, p = 0.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 21.64/17, p = 0.199
5 0 5rtrack rECL√
2track + 2ECL
2 = 30.37/17, p = 0.024
```
Figure 48: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the
```
negative helicity bin and high m2miss.
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D0 +
D0 + 0
D0 + +
D0 + + 0
D0 * +
D0 * + +
D0 * + + 0
Rest
```
B+ → ¯D∗0(D0 π0) ρ+ after all selections (cos θ τhel > 0 & m2miss < 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 10.23/8, p = 0.249
5 0 5rSR rtrack√
2SR + 2track
2 = 13.76/8, p = 0.088
5 0 5rSR rECL√
2SR + 2ECL
2 = 2.54/8, p = 0.960
5 0 5rDst rtrack√
2Dst + 2track
2 = 5.33/8, p = 0.722
5 0 5rDst rECL√
2Dst + 2ECL
2 = 3.43/8, p = 0.904
5 0 5rtrack rECL√
2track + 2ECL
2 = 6.41/8, p = 0.601
```
Figure 49: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the
```
positive helicity bin and low m2miss.
them in the final fit provides a meaningful improvement. For this fit, we don’t allow the1286
SL templates B → D∗τ ν, B → D∗ℓν, and B → D∗∗ℓν to float freely, but we rather first1287
group B → D∗τ ν and B → D∗ℓν together and then let the templates float within 99%1288
of their expected values by implemented a Gaussian constrain on them. This approach1289
```
offers two key advantages. First, it completely masks the R(D∗) value, allowing us to1290
```
later run the fit on experimental data to confirm its stability and determine scaling fac-1291
tors without the risk of inadvertently ”opening the box.” This is particularly useful for1292
studying Data/MC agreement in other sidebands. Second, it enhances the sensitivity of1293
background yield estimations in the control region fits. Given the limited statistics for the1294
76
0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 22.0 24.0 26.0 28.0 30.0Tag decay mode contribution in %
D0 +
D0 + 0
D0 + 0 0
D0 + +
D0 + + 0
D0 * +
D0 * + 0
D0 * + +
D0 * + + 0
D + + 0
c p + +
D0pp +
Rest
```
B+ → ¯D∗0(D0 π0) ρ+ after all selections (cos θ τhel > 0 & m2miss > 1 GeV2)
```
BBbar in SRBBbar in Dst
BBbar in trackBBbar in ECL
5 0 5rSR rDst√
2SR + 2Dst
2 = 18.30/13, p = 0.147
5 0 5rSR rtrack√
2SR + 2track
2 = 24.87/13, p = 0.024
5 0 5rSR rECL√
2SR + 2ECL
2 = 13.91/13, p = 0.380
5 0 5rDst rtrack√
2Dst + 2track
2 = 40.03/13, p = 0.000
5 0 5rDst rECL√
2Dst + 2ECL
2 = 21.81/13, p = 0.058
5 0 5rtrack rECL√
2track + 2ECL
2 = 10.11/13, p = 0.685
```
Figure 50: FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the
```
positive helicity bin and high m2miss.
Table 42: Overview of fit regions
```
Reconstruction Target sample Label Extra cut (cf. SR) Variables (bins)
```
```
B0 → D∗−(D0 π−) π+ B → D∗τ ν SR cos θτhel > 0 m2miss (2), EextraECL (4)B0 → D∗−(D0 π−) π+ B → D∗τ ν SR cos θτ
```
```
hel < 0 m2miss (2), EextraECL (4)
```
```
B0 → D∗−(D0 π−) ρ+ B → D∗τ ν SR cos θτhel > 0 and m2miss < 1 GeV 2 EextraECL (4)B0 → D∗−(D0 π−) ρ+ B → D∗τ ν SR cos θτ
```
```
hel < 0 and m2miss < 1 GeV 2 EextraECL (4)B0 → D∗−(D0 π−) ρ+ B → D∗τ ν SR cos θτhel > 0 and m2miss > 1 GeV 2 EextraECL (4)
```
```
B0 → D∗−(D0 π−) ρ+ B → D∗τ ν SR cos θτhel < 0 and m2miss > 1 GeV 2 EextraECL (4)
```
```
B+ → D∗0(D0 π0) π+ B → D∗τ ν SR cos θτhel > 0 m2miss (2), EextraECL (4)B+ → D∗0(D0 π0) π+ B → D∗τ ν SR cos θτ
```
```
hel < 0 m2miss (2), EextraECL (4)
```
```
B+ → D∗0(D0 π0) ρ+ B → D∗τ ν SR cos θτhel > 0 and m2miss < 1 GeV 2 EextraECL (4)B+ → D∗0(D0 π0) ρ+ B → D∗τ ν SR cos θτ
```
```
hel < 0 and m2miss < 1 GeV 2 EextraECL (4)B+ → D∗0(D0 π0) ρ+ B → D∗τ ν SR cos θτhel > 0 and m2miss > 1 GeV 2 EextraECL (4)
```
```
B+ → D∗0(D0 π0) ρ+ B → D∗τ ν SR cos θτhel < 0 and m2miss > 1 GeV 2 EextraECL (4)
```
```
B0 → D∗−(D0 π−) ℓ+ B → D∗ℓν NR - m2miss (3)B+ → D∗0(D0 π0) ℓ+ B → D∗ℓν NR - m2
```
```
miss (3)
```
```
B0 → D∗−(D0 π−) π+ B ¯B BR01 pos 1 extra track and cos θτhel > 0 cosTBTO (2)B0 → D∗−(D0 π−) π+ B ¯B BR01 neg 1 extra track and cos θτ
```
```
hel < 0 cosTBTO (2)
```
```
B0 → D∗−(D0 π−) ρ+ B ¯B BR02 pos m1 1.5 < EextraECL < 2 GeV and cos θτhel > 0 and m2miss < 1 GeV 2 ∆M(D∗) (5)B0 → D∗−(D0 π−) ρ+ B ¯B BR02 neg m1 1.5 < Eextra
```
```
ECL < 2 GeV and cos θτhel < 0 and m2miss < 1 GeV 2 cosTBTO (2)B0 → D∗−(D0 π−) ρ+ B ¯B BR02 pos m2 1.5 < EextraECL < 2 GeV and cos θτ
```
```
hel > 0 and m2miss < 1 GeV 2 cosTBTO (2)B0 → D∗−(D0 π−) ρ+ B ¯B BR02 neg m2 1.5 < EextraECL < 2 GeV and cos θτhel < 0 and m2miss < 1 GeV 2 cosTBTO (2)
```
```
B+ → D∗0(D0 π0) π+ B ¯B BRp1 pos 1 extra track and cos θτhel > 0 cosTBTO (3) / M(D0) (5)B+ → D∗0(D0 π0) π+ B ¯B BRp1 neg 1 extra track GeV and cos θτ
```
```
hel < 0 cosTBTO (3) / M(D0) (5)
```
```
B+ → D∗0(D0 π0) ρ+ B ¯B BRp2 pos m1 1.5 < EextraECL < 2 GeV and cos θτhel > 0 and m2miss < 1 GeV 2 cosTBTO (2)B+ → D∗0(D0 π0) ρ+ B ¯B BRp2 neg m1 1.5 < Eextra
```
```
ECL < 2 GeV and cos θτhel < 0 and m2miss < 1 GeV 2 cosTBTO (2) / M(D0) (5)B+ → D∗0(D0 π0) ρ+ B ¯B BRp2 pos m2 1.5 < EextraECL < 2 GeV and cos θτ
```
```
hel > 0 and m2miss > 1 GeV 2 cosTBTO (2)B+ → D∗0(D0 π0) ρ+ B ¯B BRp2 neg m2 1.5 < EextraECL < 2 GeV and cos θτhel < 0 and m2miss > 1 GeV 2 cosTBTO (2) / M(D0) (5)
```
```
B0 → D∗−(D0 π−) ℓ+ B → D∗∗ℓν Dstst0 1 extra track m2miss (3)B+ → D∗0(D0 π0) ℓ+ B → D∗∗ℓν Dststp 1 extra track m2
```
```
miss (3)
```
SL processes in these regions, estimating two constrained nuisance parameters per region1295
is more manageable than minimizing three completely free parameters per regions, which1296
would be significantly more challenging.1297
Finally, we perform the fit with all regions included: SR, NR, BR, CR and BCR. We1298
77
confirm that the combined fit enhances sensitivity for all yields compared to individual1299
fits, with the most significant improvement observed for q ¯q processes, for which the control1300
```
regions offer greater sensitivity. The R(D∗) and Pτ uncertainties falls within the expected1301
```
range, as defined by the fits where all backgrounds are either fixed or allowed to float.1302
The results are summarized in Table 43.1303
No systematic effects have been included in these fits, so the uncertainties reported1304
are purely statistical. In all fits, closure is achieved, meaning all free parameters converge1305
to their nominal values. In Appendix L we provide a grid modifier plot that presents all1306
the free and fixed parameters of the fit, as this plot is provided by cabinetry. As this1307
plot spans across multiple pages we provide it in the Appendix to maintain flow in the1308
main text.1309
Table 43: Asimov fit uncertainties of all free unconstrained parameters for the simulta-
```
neous R(D∗) and Pτ fit. The uncertainties are presented in terms of percentages in case
```
the free parameter’s nominal value is not 1. The nominal values of all parameters is pre-
sented in parenthesis in the first column. We confirm that we observe full closure in all
our Asimov fits, i.e. all free parameters are minimized to their nominal values.
```
Scale factors/ Regions SR, NR (BKGs fixed) SR, NR, (BKGs floating) CRs SR, NR, CRs
```
```
R(D∗) (0.258) ±0.0330(12.79%) ±0.0443(16.66%) - ±0.0387(13.91%)Pτ (-0.497) ±0.7799 ±0.9281 - ±0.8223
```
```
B → D∗ℓν (1.0) ±0.0138 ±0.0142 - ±0.0141
```
```
B → D∗∗ℓν (B0B0) (1.0) - ±0.0624 ±0.1191 ±0.0552B → D∗∗ℓν (B+B−) (1.0) - ±0.0483 ±0.0842 ±0.0419
```
```
BB (B0B0, τ → πντ ) cos θτhel > 0 (1.0) - ±0.1765 ±0.1039 ±0.0894BB (B0B0, τ → πν
```
```
τ ) cos θτhel < 0 (1.0) - ±0.137 ±0.0567 ±0.0522
```
```
BB (B0B0, τ → ρντ ) cos θτhel > 0 m2miss < 1 (1.0) - ±0.308 ±0.3021 ±0.2155BB (B0B0, τ → ρν
```
```
τ ) cos θτhel > 0 m2miss > 1 (1.0) - ±1.2195 ±0.0754 ±0.0641BB (B0B0, τ → ρντ ) cos θτ
```
```
hel < 0 m2miss < 1 (1.0) - ±0.1081 ±0.164 ±0.09BB (B0B0, τ → ρντ ) cos θτhel < 0 m2miss > 1 (1.0) - ±0.073 ±0.1108 ±0.0605
```
```
BB (B+B−, τ → πντ ) cos θτhel > 0 (1.0) - ±0.1108 ±0.0623 ±0.0542BB (B+B−, τ → πν
```
```
τ ) cos θτhel < 0 (1.0) - ±0.1021 ±0.0353 ±0.0333
```
```
BB (B+B−, τ → ρντ ) cos θτhel > 0 m2miss < 1 (1.0) - ±0.0928 ±0.1257 ±0.0745BB (B+B−, τ → ρν
```
```
τ ) cos θτhel > 0 m2miss > 1 (1.0) - ±0.059 ±0.0854 ±0.0484BB (B+B−, τ → ρντ ) cos θτ
```
```
hel < 0 m2miss < 1 (1.0) - ±0.2371 ±0.2323 ±0.1659BB (B+B−, τ → ρντ ) cos θτhel < 0 m2miss > 1 (1.0) - ±0.0519 ±0.0582 ±0.0386
```
In Figure 51 we provide the correlation matrix for all free parameters in the fit. From1310
```
there one can extract the statistical correlation coefficient between R(D∗) and Pτ which1311
```
is 0.54. For comparison the reported correlation between the parameters in the Belle1312
analysis [4] was 0.29, however that was determined differently since the Belle analysis did1313
not extract the two parameters simultaneously.1314
In Figures 52 - 55 we present the post fit distributions on Asimov data. Not pulls are1315
observed in any of the bins.1316
```
6.5 Statistical validation of R(D∗) and Pτ fit1317
```
```
To confirm the statistical validity of the R(D∗) estimator, we conduct additional tests1318
```
using an Asimov dataset. Our primary goal is to ensure that the maximum likelihood fit1319
```
provides an unbiased estimate of R(D∗) and all other yields. To achieve this, we generate1320
```
pseudo datasets, referred to as ”toys.”1321
78
PtauBpDstnormRDstarDstst_yield_0
BBbar_yield_01_negContinuum_yield_01_negBBbar_yield_01_posContinuum_yield_01_posBBbar_yield_02_negContinuum_yield_02_negBBbar_yield_02_posContinuum_yield_02_posBBbar_yield_p2_neg_m1Continuum_yield_p2_neg_m1BBbar_yield_p2_neg_m2Continuum_yield_p2_neg_m2BBbar_yield_p2_pos_m1Continuum_yield_p2_pos_m1BBbar_yield_p2_pos_m2Continuum_yield_p2_pos_m2BBbar_yield_p1_negContinuum_yield_p1_negBBbar_yield_p1_posContinuum_yield_p1_posDstst_yield_pfree_BBbar_01_negfree_BBbar_01_posfree_BBbar_02_negfree_BBbar_02_posfree_BBbar_p1_negfree_BBbar_p1_pos
Ptau
BpDstnorm
RDstar
Dstst_yield_0
BBbar_yield_01_neg
Continuum_yield_01_neg
BBbar_yield_01_pos
Continuum_yield_01_pos
BBbar_yield_02_neg
Continuum_yield_02_neg
BBbar_yield_02_pos
Continuum_yield_02_pos
BBbar_yield_p2_neg_m1
Continuum_yield_p2_neg_m1
BBbar_yield_p2_neg_m2
Continuum_yield_p2_neg_m2
BBbar_yield_p2_pos_m1
Continuum_yield_p2_pos_m1
BBbar_yield_p2_pos_m2
Continuum_yield_p2_pos_m2
BBbar_yield_p1_neg
Continuum_yield_p1_neg
BBbar_yield_p1_pos
Continuum_yield_p1_pos
Dstst_yield_p
free_BBbar_01_neg
free_BBbar_01_pos
free_BBbar_02_neg
free_BBbar_02_pos
free_BBbar_p1_neg
free_BBbar_p1_pos
1.00 0.03 0.56 -0.10 -0.15 0.02 0.10 -0.12 0.14 0.01 -0.08 -0.09 -0.02 -0.03 -0.14 -0.01 0.05 0.01
0.03 1.00 -0.08 -0.10 -0.01 -0.16
0.56 -0.08 1.00 -0.22 -0.19 0.02 -0.04 -0.16 -0.13 -0.01 -0.08 -0.09 -0.08 -0.03 -0.20 -0.02 0.05 0.02
-0.10 -0.10 -0.22 1.00 0.01 0.01 0.02 0.02 0.02 0.01 0.06 -0.01
-0.15 -0.19 0.01 1.00 -0.54 0.03 0.01 0.02 0.02 0.01 0.01 0.04 0.40 -0.01
0.02 0.02 -0.54 1.00 -0.01 -0.74
0.10 -0.04 1.00 -0.35 0.04 0.01 0.01 0.19
-0.35 1.00 -0.55
-0.12 -0.16 0.03 1.00 -0.29 0.01 0.01 0.02 0.01 0.01 0.03 0.20 -0.01
-0.29 1.00 -0.68
0.14 -0.13 0.01 0.01 0.04 0.01 1.00 -0.20 0.02 0.02 0.13
0.01 -0.01 -0.20 1.00 -0.62
1.00 -0.75
-0.75 1.00
1.00 -0.79
-0.79 1.00
1.00 -0.70
-0.70 1.00
1.00 -0.76
-0.76 1.00
-0.08 -0.08 0.02 0.02 0.01 1.00 -0.62 0.01 0.35
-0.09 -0.09 0.02 0.02 0.02 -0.62 1.00 0.01 0.01 -0.56
-0.02 -0.01 -0.08 0.02 0.01 0.01 0.01 0.02 0.01 1.00 -0.52 0.01 0.24
-0.03 -0.03 0.01 0.01 0.01 -0.52 1.00 -0.47
-0.14 -0.16 -0.20 0.06 0.04 -0.01 0.01 0.03 0.02 0.01 0.01 0.01 1.00 -0.01
-0.01 -0.02 0.40 -0.74 1.00
0.19 -0.55 1.00
0.20 -0.68 1.00
0.13 -0.62 1.00
0.05 0.05 -0.01 -0.01 -0.01 0.35 -0.56 -0.01 1.00
0.01 0.02 0.24 -0.47 1.001.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
```
Figure 51: Statistical only correlation matrix of the Pτ and R(D∗) fit.
```
Each toy dataset is created by taking the expected event counts from the Asimov1322
dataset and re-sampling the counts for each bin from a Poisson distribution. We generate1323
2,500 toy datasets, where the event counts in each bin are replaced by random draws1324
from these Poisson distributions. We then fit each toy dataset to the nominal templates,1325
```
determining the value of R(D∗) and the scale factor for the yield of each decay process.1326
```
For each fitted parameter, we calculate the pull. The pull of an estimated parameter is1327
defined as1328
```
pull =
```
ˆθ − θtrue
σˆθ
```
(47)1329
```
We then histogram the pull distribution and fit it to a standard normal distribution.1330
If the maximum likelihood fit provides an unbiased estimate of the true value of the1331
parameter of interest, the pull distribution should be compatible with a standard normal.1332
When the pulls are symmetrically distributed around zero, the numerator of Equation 471333
is, on average, zero. This indicates that the estimator does not introduce any bias by1334
favoring larger or smaller values for the parameter.1335
79
0
10
20
30
40
50
60
70
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +
```
SR
cos hel < 0postfit
```
m2miss [ 1, 1] m2miss ( 1, 7]m2miss [ 1, 1] m2miss ( 1, 7]
```
Belle II Preliminary
0
10
20
30
40
```
Events / (1 GeV)
```
```
B0 D* (D0 ) +SRcos hel > 0
```
postfit
```
m2miss [ 1, 1] m2miss ( 1, 7]m2miss [ 1, 1] m2miss ( 1, 7]
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.0 0.3125 0.625 0.9375 0.0 0.3125 0.625 0.9375 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.3125 0.625 0.9375 0.0 0.3125 0.625 0.9375 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
100
200
300
400
```
Events / (0.45 )
```
```
B0 D* (D0 ) +
```
1 ext. track
cos hel < 0postfit
0
10
20
30
40
```
Events / (0.001 GeV)
```
```
B0 D* (D0 ) +1 ext. trackcos
```
hel > 0postfit
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.143 0.144 0.145 0.146 0.147 0.148MD* in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 52: Postfit distributions on Asimov in the SR and control regions for
```
B0 → D∗−(D0 π−) π+
```
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
```
Events / (0.31 GeV)
```
```
B0 D* (D0 ) +SRcos hel < 0 & m2miss [ 1, 1]
```
postfit
Belle II Preliminary
0
20
40
60
80
100
120
140
```
Events / (0.31 GeV)
```
```
B0 D* (D0 ) +
```
SR
cos hel < 0 & m2miss [ 1, 1]postfit
0
10
20
30
40
50
60
```
Events / (0.31 GeV)
```
```
B0 D* (D0 ) +SRcos hel > 0 & m2miss [1, 7]
```
postfit
0
20
40
60
80
```
Events / (0.31 GeV)
```
```
B0 D* (D0 ) +
```
SR
cos hel > 0 & m2miss [1, 7]postfit
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
2
4
6
8
10
12
```
Events / (0.45 )
```
```
B0 D* (D0 ) +
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
0
20
40
60
80
100
```
Events / (0.45 )
```
```
B0 D* (D0 ) +
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
0
5
10
15
20
```
Events / (0.45 )
```
```
B0 D* (D0 ) +
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
dt = 365 fb 1
```
0
10
20
30
40
50
```
Events / (0.45 )
```
```
B0 D* (D0 ) +
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 53: Postfit distributions on Asimov in the SR and control regions for
```
B0 → D∗−(D0 π−) ρ+
```
Furthermore, if the standard deviation of the pull distribution is close to one, we can1336
be confident that the estimated uncertainty of the parameter accurately reflects the true1337
```
variability due to statistical fluctuations. In Figure 56 we show the pull plots for R(D∗),1338
```
```
Pτ and the strength of the B → D∗ℓν template. For R(D∗) and the strength of the1339
```
80
0
25
50
75
100
125
150
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +
```
SR
cos hel < 0postfit
```
m2miss [ 1, 1] m2miss ( 1, 7]m2miss [ 1, 1] m2miss ( 1, 7]
```
Belle II Preliminary
0
20
40
60
80
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +SRcos hel > 0
```
postfit
```
m2miss [ 1, 1] m2miss ( 1, 7]m2miss [ 1, 1] m2miss ( 1, 7]
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.0 0.3125 0.625 0.9375 0.0 0.3125 0.625 0.9375 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.3125 0.625 0.9375 0.0 0.3125 0.625 0.9375 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
50
100
150
200
250
300
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +
```
1 ext. track
cos hel < 0postfit
```
cos TBTO [0.0, 3] cos TBTO [0.3, 0.6] cos TBTO (0.6, 0.9] 0
```
20
40
60
80
100
120
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +
```
1 ext. track
cos hel > 0postfit
```
cos TBTO [0.0, 3] cos TBTO [0.3, 0.6] cos TBTO (0.6, 0.9]
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 54: Postfit distributions on Asimov in the SR and control regions for
```
B+ → D∗0(D0 π0) π+
```
0
5
10
15
20
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +SRcos hel < 0 & m2miss [ 1, 1]
```
postfit
Belle II Preliminary
0
100
200
300
400
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +
```
SR
cos hel < 0 & m2miss [ 1, 1]postfit
0
20
40
60
80
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +SRcos hel > 0 & m2miss [1, 7]
```
postfit
0
50
100
150
200
250
300
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +
```
SR
cos hel > 0 & m2miss [1, 7]postfit
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.00 0.25 0.50 0.75 1.00 1.25extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
5
10
15
20
```
Events / (0.45 )
```
```
B+ D*0(D0 0) +
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
0
25
50
75
100
125
150
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
cos TBTO [0.0, 45]cos TBTO [0.45, 0.9] 0
20
40
60
80
```
Events / (0.45 )
```
```
B+ D*0(D0 0) +
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
dt = 365 fb 1
```
0
20
40
60
80
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
cos TBTO [0.0, 45]cos TBTO [0.45, 0.9]
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccMC stat. unc.
Asimov Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
1.841.851.861.871.881.841.851.861.871.881.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
1.841.851.861.871.881.841.851.861.871.881.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 55: Postfit distributions on Asimov in the SR and control regions for
```
B+ → D∗0(D0 π0) ρ+
```
B → D∗ℓν template we use the HESSE error from the fit. Since Pτ due to it’s definition1340
and range can have asymmetric errors, especially when throwing toys, we use the MINOS1341
error to calculate the pull of every toy. When the nominator of the pull is larger than zero,1342
we use the lower MINOS uncertainty. When the nominator of the pull is smaller than zero1343
81
we use the upper MINOS uncertainty. In Appendix G we provide the pull distributions for1344
all other free parameters of the fit. We observe that all pull distributions are compatible1345
with a standard normal, confirming that our maximum likelihood fit provides an unbiased1346
```
estimate of R(D∗) and all other yields, and that the uncertainties accurately represent1347
```
the true variability in the data.1348
2 0 2
```
R(D*) R(D*)SM
```
```
R(D*)
```
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402489 toys
= 0.0175 ± 0.0206= 1.0289 ± 0.0146
2 0 2
P PSM
P
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2489 toys= 0.0058 ± 0.0199= 0.9929 ± 0.0141
2 0 2
Pull for B+ D*0 + strength
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2489 toys= 0.0130 ± 0.0200
= 0.9953 ± 0.0141
```
Figure 56: Pull plots for toys for R(D∗). Pτ and the yield of B → D∗ℓν decays. The
```
MINOS error has been used to calculate the pull of Pτ for every toy. A negligeable amount
```
of toys (11/2500) did not converge, therefore we excluded them from the pull distribution.
```
The parameters of the gaussian fit are compatible with a standard normal.
Another important test is evaluating how our estimator responds to changes in the1349
observed data. To test this, we bias the Asimov dataset in favor of a specific decay1350
process. This is done by adjusting the event counts in the Asimov dataset according to1351
the distribution of a particular nominal template.1352
In Figure 57, we show this procedure, where the Asimov datasets are constructed with1353
contributions from each template varying from 50% to 200%. We fit these biased Asimov1354
datasets to the nominal templates and plot the estimated parameter values. In all cases,1355
```
we observe that the parameter estimates scale as expected. The estimated value of R(D∗)1356
```
scales linearly when the contribution from B → D∗τ ν decays is varied. Similarly, the yield1357
```
of B → D∗ℓν scales linearly, while R(D∗) scales as 1x when the B → D∗ℓν contribution1358
```
is modified. Finally, all background yields scale linearly with changes in their respective1359
```
contributions, while both R(D∗) and the yield of B → D∗ℓν remain constant.1360
```
All the above test give us confidence that the maximum likelihood fit that we have1361
```
implemented is a robust estimator of the R(D∗) and all other related yields.1362
```
Lastly we perform a linearity test for the polarization measurement as the linearity of1363
```
the estimator on R(D∗) the normalization strength and all the background scale factors1364
```
have been tested previously, but not the one of Pτ . In order to carry out the linearity1365
test on Pτ we evaluate the full likelihood with a certain set of parameters. We keep all1366
parameters to their nominal values excect Pτ which is varied from -0.9443 to -0.0497 in1367
20 steps of -0.0497. By evaluating the likelihood we get a new dataset every time that1368
corresponds to the expected observed data for this set of free parameters. We then fit1369
this expected dataset to our nominal templates. Figure 58 shows the results of this study.1370
82
```
0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0Expected R(D*)/R(D*)
```
SM yield
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25
Estimated yields
0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0Expected B D* + yield
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25
Estimated yields
0.50 0.75 1.00 1.25 1.50 1.75 2.00Expected B D* * + yield0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Estimated yields
0.50 0.75 1.00 1.25 1.50 1.75 2.00Expected BB yield0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Estimated yields
0.50 0.75 1.00 1.25 1.50 1.75 2.00Expected qq yield0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Estimated yields
```
R(D*)/R(D*)SMB D* +
```
B D* * + inB0ch.B D* * + inB+ch.
BB in B0 ch.BB in B+ ch.
qq in B0 ch.qq in B+ ch.
Figure 57: The response of the estimator scales as expected when we bias the Asimov
dataset.
Pτ scales as expected while the other POIs are minimized to their nominal values. We1371
conclude that the estimator’s response scales as expected.1372
0.0 0.5 1.0 1.5 2.0
Expected PτPSMτ
0.5
0.0
0.5
1.0
1.5
2.0
2.5
Estimated
PτPSMτ
```
y=x
```
0.5 1.0 1.5 2.0
Expected PτPSMτ
0.0
0.5
1.0
1.5
2.0
Estimated
```
R(D
```
```
∗)
```
```
R(D
```
```
∗)SM
```
0.0 0.5 1.0 1.5
Expected PτPSMτ
0.0
0.5
1.0
1.5
2.0
Estimated
B →
D∗
` ν
strength
Figure 58: Linearity test for the three POIs in the simultaneous fit. Pτ scales as expected
while the other POIs are minimized to their nominal values. We conclude that the esti-
mator’s response scales as expected.
83
7 Systematics1373
We adopt a unified framework for handling all systematic uncertainties. For each source of1374
systematic uncertainty, we apply the SysVar eigendecomposition procedure, as described1375
in Section 3.1.4. All systematic uncertainties considered in this analysis can be categorized1376
into three distinct classes:1377
1. Fully correlated correction weights1378
2. Uncorrelated correction weights1379
3. Partially correlated correction weights1380
SysVar has been designed to handle systematics with partial correlations, such as LID.1381
For the first two categories, the eigendecomposition procedure defaults to well-defined lim-1382
iting cases. In the fully correlated case, a single dominant eigendirection results in one1383
nuisance parameter in total. In the uncorrelated case, each correction weight1384
yields one nuisance parameter, corresponding to its own dominant eigendirection.1385
While implementing shape systematics for these two limiting cases is relatively straight-1386
forward without the full machinery of SysVar, we nonetheless perform the basis transfor-1387
mation to maintain a consistent treatment across all systematic uncertainties. This also1388
serves to validate SysVar’s behavior in these well-understood edge cases.1389
For each source of systematic uncertainty, the eigendecomposition is performed across1390
all relevant reconstruction channels—including those used in control regions for calibra-1391
tions, whether included in a simultaneous fit or not—and all applicable templates. For1392
```
instance, in the case of the tracking efficiency uncertainty (see Section 5.5.2), we include all1393
```
reconstruction channels and templates, as the impact of this effect is universal. Conversely,1394
```
for LID fake rates (see Section 5.5.8), we restrict the PCA to reconstruction channels that1395
```
involve actual lepton reconstruction, and exclude templates that cannot be affected by1396
fake leptons—such as the B → D∗ℓν template. As a final example, for uncertainties re-1397
```
lated to BF of the light lepton gap modes (see Section 5.7), we consider all reconstruction1398
```
channels but include only the relevant template—specifically, the B → D∗∗ℓν template.1399
```
For each systematic uncertainty, we account for both an additive (shape-related) com-1400
```
```
ponent and a multiplicative (normalization-related) component. The eigenvariations de-1401
```
rived from Equation 4 inherently capture both effects within each template. Disentangling1402
the normalization component is straightforward: we compute the sum of bin contents for1403
the up or down eigenvariation and divide it by the sum of the bin contents in the nomi-1404
nal histogram. This ratio gives the relative normalization effect of the systematic, which1405
can be directly implemented as a normsys modifier, as defined in Table 2 of the pyhf1406
framework. To isolate the shape-only effect, we divide each bin of the eigenvariation by1407
the relative normalization factor. This effectively re-normalizes the variation to match1408
the total yield of the nominal histogram, ensuring that the resulting histosys modifier1409
```
(also defined in Table 2) only alters the shape of the template without affecting its overall1410
```
normalization. Notably, the absolute up and down variations—whether normalized or1411
not—are already in the exact form required by pyhf to implement the histosys modifier,1412
making the technical implementation both clean and efficient. Accordingly, we introduce1413
two nuisance parameters per template per eigendirection: one to account for the additive1414
84
```
(shape) component, and one for the multiplicative (normalization) component. These1415
```
two nuisance parameters may be treated as either fully correlated or fully uncorrelated,1416
depending on the nature of the underlying systematic uncertainty. The choice of corre-1417
lation is made on a case-by-case basis, guided by physical intuition and the behavior of1418
each specific systematic.1419
For every source of systematic uncertainty we generate 500 variations of the corrections1420
weights. By building 500 template variations we get the full covariance matrix of the1421
analysis that is used for the eigendecomposition. In order to determine the important1422
number of eigendirections we set the precision to 10−8. That is we implement as many1423
eigendirections as fully correlated NPs as needed to reconstruct the original covariance1424
matrix with differences smaller than 10−8 in the orthogonal space.1425
In the following, we first present the full systematic uncertainty budget for the si-1426
```
multaneous R(D∗) and Pτ fit. We can provide detailed information for each individual1427
```
systematic uncertainty using SysVar’s visualization API per request during the review.1428
SysVar’s visualization API automatically plots the correction weight variations, the co-1429
variance matrix of the corrections, either explicitly defined or build from the different1430
set of uncertainties, the varied templates across all reconstruction channels and the full1431
correlation matrix across all bins, templates, reconstruction channels. We avoid providing1432
this information for all systematics by default in this document since this would result to1433
an extremely large number of plots.1434
We evaluate the systematic uncertainties in a unified way as follows: We first run1435
the nominal fit on an Asimov dataset without including any systematic uncertainties.1436
The uncertainty on the parameter of interest we acquire from this fit corresponds to the1437
statistical only uncertainty. We then include all NP for a particular source or category of1438
systematic uncertainties. We then determine the total uncertainty that includes both the1439
statistical and the uncertainty associated to that particular systematic effect. In order1440
to isolate the systematic part of the uncertainty we subtract those two in quadrature as1441
described in Equation 48, since the statistical and systematic part should be completely1442
independant from each other.1443
σsyst =
p
```
σ2tot − σ2stat (48)1444
```
```
In the following we present the systematic uncertainty per source for both R(D∗) and1445
```
Pτ .1446
```
7.1 Systematic budget for the R(D∗) and Pτ fit1447
```
85
Table 44: Summary of Systematic Uncertainties
uncertainties
```
Source # NP R(D∗) (0.258) % Pτ (-0.497) ρ (shape-norm)
```
data sample size - 13.91 0.8223 -
simulation sample size 138 7.011 0.4131 -
Prompt hadronic BFs 20 3.132 0.1257 1
Double Charm BFs 24 1.144 0.0330 1
D∗∗ and gap BF 16 0.301 0.0167 1
```
τ /D(∗) BFs 1+1+1+1 ∼ 0 ∼ 0 1
```
π0 efficiency 7 1.765 0.0125 0
πslow efficiency 3+3 0.472 0.0201 0
FEI efficiency 23 1.973 0.0283 0
tracking efficiency 1 0.795 0.0050 0
µID eff. 4 0.02 0.0008 0
eID eff. 8 0.006 ∼ 0 0
LID fakes 9+9+9+9 ∼ 0 0.009 0
kID 9+9 2.818 0.0196 0
πID 15+15 3.167 0.0206 0
µ fake π 22 2.526 0.0259 0
```
D(∗) FF 9 0.143 0.0067 1
```
```
D(∗∗) FF 4 1.319 0.0487 1
```
Photon multiplicity reweighting 14 1.283 0.0245 shape only
P σ
syst - 9.893 0.4404 -
Total systematic unc. - 10.094 0.4422 -
86
8 Agreement of simulated and experimental data1448
```
Before performing the measurement of R(D∗) and Pτ in the signal region (SR) and nor-1449
```
```
malization region (NR), we must ensure that all corrections and calibrations lead to an1450
```
accurate modeling of the data. To achieve this, we first run the signal extraction fit ex-1451
clusively in the control regions to extract scaling factors for the background templates,1452
specifically for the BB and q ¯q components. Our validation strategy follows a structured1453
approach. First, we verify that the signal extraction variables are well-modeled in regions1454
where the overall event normalization is already constrained, either through FEI calibra-1455
tion for correctly reconstructed events or through control fits for misreconstructed events.1456
Once this is established, we repeat the same tests in regions where the normalization1457
is not explicitly fixed. This allows us to simultaneously verify the shape consistency of1458
the observables of interest and assess the validity of the derived calibration and scaling1459
factors. The regions used in this validation process are summarized in Table 45.1460
Table 45: Sideband checks summary
Reconstruction Sideband Normalization Motivation Target Sample
```
B0 → D∗−(D0 π−) π+ off-resonance data
```
```
Free q ¯qB0 → D∗−(D0 π−) ρ+ off-resonance data Overall modellingB+ → D∗0(D0 π0) π+ off-resonance data in continuum MC
```
```
B+ → D∗0(D0 π0) ρ+ off-resonance data
```
```
B0 → D∗−(D0 π−) π+ 1 extra track
```
```
Fixed BB and q ¯qB0 → D∗−(D0 π−) ρ+ 1.5 < EextraECL < 2 GeV Observable modellingB+ → D∗0(D0 π0) π+ 1 extra track in misreconstructed events
```
```
B+ → D∗0(D0 π0) ρ+ 1.5 < EextraECL < 2 GeV
```
```
B0 → D∗−(D0 π−) ℓ+q2 < 4 GeV 2 Fixed Observable modelling B → D∗ℓν
```
```
B+ → D∗0(D0 π0) ℓ+ in correctly reconstructed events
```
```
B0 → D∗−(D0 π−) π+
```
```
1.25 < EextraECL < 1.5 GeV Free BB and q ¯qB0 → D∗−(D0 π−) ρ+ Overall agreementB+ → D∗0(D0 π0) π+ in misreconstructed events
```
```
B+ → D∗0(D0 π0) ρ+
```
```
B0 → D∗−(D0 π−) ℓ+NR Free Overall agreement B → D∗ℓν
```
```
B+ → D∗0(D0 π0) ℓ+ in correctly reconstructed events
```
In the rest of this section we present the Data/MC validation in more detail.1461
8.1 Off-resonance data1462
Since we calibrate the continuum processes using off resonance data in the sidebands that1463
are described in Section 5.10 we begin by applying the scaling factors to the SR and the1464
regions that are used to constrain BB processes. This tests serves as a way of validating1465
the overall normalization and shapes of important variables of continuum events. This1466
will give us confidence that any potential mismodelling we observe in those regions is not1467
coming from q ¯q events. Figures 63 - 66 show the Data/MC agreement on off resonance1468
data with the SR selection applied. Due to relatively low statistics we used a coarse1469
binning on EextraECL when needed to have a meaningful χ2 test. We conclude that with the1470
current statistical power there’s now disagreement in continuum events.1471
87
0
2
4
6
8
10
```
Events / (0.62 GeV)
```
```
B0 D* (D0 ) +2 / 2 = 0.52 (0.59)SR
```
Belle II Preliminary
0
2
4
6
8
10
12
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.73 (0.48)SR
```
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.72 (0.48)
```
```
SRdt = 365 fb
```
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
2 1 0 1cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 59: Fitting variables in continuum processes on off-resonance data in SR of
```
B0 → D∗−(D0 π−) π+
```
0.02.5
5.07.5
10.012.5
15.017.5
```
Events / (0.62 GeV)
```
```
B0 D* (D0 ) +
```
```
2 / 2 = 3.24 (0.04)
```
SRBelle II Preliminary
0.0
2.5
5.0
7.510.0
12.5
15.0
17.5
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.25 (0.78)SR
```
0
5
10
15
20
25
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.26 (0.77)
```
```
SRdt = 365 fb
```
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 60: Fitting variables in continuum processes on off-resonance data in SR of
```
B0 → D∗−(D0 π−) ρ+
```
0
5
10
15
20
25
30
Events / Bin
```
B+ D*0(D0 0) +2 / 3 = 0.59 (0.62)
```
SRBelle II Preliminary
0
10
20
30
40
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.09 (0.91)SR
```
0
10
20
30
40
50
60
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.05 (0.95)
```
```
SRdt = 365 fb
```
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 61: Fitting variables in continuum processes on off-resonance data in SR of
```
B+ → D∗0(D0 π0) π+
```
We continue by performing the same test on off resonance data but with the selection1472
that is used in the regions that constrain BB events. We see overall good agreement in1473
these regions as well, therefore we conclude that all continuum processes in the regions1474
that are included in the fit are well modelled.1475
8.2 Control Region fits1476
We first perform the fit in the control regions defined in Table 42. These regions are ini-1477
tially fitted separately and then simultaneously. Although the event yields are not linked1478
between the different regions, the nuisance parameters for most systematic uncertainties1479
88
0
10
20
30
40
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +
```
```
2 / 4 = 0.94 (0.44)
```
SRBelle II Preliminary
0
20
40
60
80
100
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 1.44 (0.24)SR
```
020
4060
80100
120140
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 2.43 (0.09)
```
```
SRdt = 365 fb
```
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 62: Fitting variables in continuum processes on off-resonance data in SR of
```
B+ → D∗0(D0 π0) ρ+
```
0.02.5
5.07.5
10.012.5
15.017.5
```
Events / (0.62 GeV)
```
```
B0 D* (D0 ) +
```
```
2 / 2 = 0.05 (0.95)
```
1 ext. trackBelle II Preliminary
0
5
10
15
20
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.47 (0.63)1 ext. track
```
0
5
10
15
20
25
30
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.03 (0.97)
```
1 ext. trackdt = 365 fb
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
2 1 0 1cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 63: Fitting variables in continuum processes on off-resonance data in SR of
```
B0 → D∗−(D0 π−) π+
```
0
2
4
6
8
10
12
```
Events / (0.5 GeV)
```
```
B0 D* (D0 ) +2
```
```
/ 1 = 0.02 (0.89)
```
1.5 < EECL < 2 GeVBelle II Preliminary
0
2
4
6
8
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 1.08 (0.34)1.5 < EECL < 2 GeV
```
0
2
4
6
8
10
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.02 (0.98)
```
1.5 < EECL < 2 GeVdt = 365 fb
1
uu/dd/ss/ccTotal MC unc.
Data
1.5 1.6 1.7 1.8 1.9 2.0extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 64: Fitting variables in continuum processes on off-resonance data in SR of
```
B0 → D∗−(D0 π−) ρ+
```
are shared as the eigendecomposition has taken place simultaneously with the SR. As a1480
result, we expect an improvement in the overall systematic uncertainty, as each region1481
benefits from the information contained in the others. The scaling factors derived for the1482
BB and q ¯q templates, along with the GoF p-values for all fits, are presented in Table 46.1483
In the last part of the table where we perform the fit simultaneously the first uncertainty1484
is the statistical one and the second the total systematic one. The same systematics1485
as in the signal regions are considered. The rest of the templates namely B → D∗τ ν,1486
B → D∗ℓν and B → D∗∗ℓν are allowed to float within 99% of their MC expectation1487
controlled by single NP with a Gaussian constraint. For the B → D∗∗ℓν events we have1488
a separate NP, while B → D∗τ ν and B → D∗ℓν events are controlled by a shared one, to1489
89
0
10
20
30
40
```
Events / (0.31 GeV)
```
```
B+ D*0(D0 0) +
```
```
2 / 4 = 0.52 (0.72)
```
1 ext. trackBelle II Preliminary
0
20
40
60
80
100
120
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 1.45 (0.23)1 ext. track
```
0
25
50
75
100
125
150
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 2.68 (0.07)
```
1 ext. trackdt = 365 fb
1
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 65: Fitting variables in continuum processes on off-resonance data in SR of
```
B+ → D∗0(D0 π0) π+
```
0
5
10
15
20
25
30
Events / Bin
```
B+ D*0(D0 0) +2 / 3 = 0.18 (0.91)
```
1.5 < EECL < 2 GeVBelle II Preliminary
0
10
20
30
40
50
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.11 (0.89)1.5 < EECL < 2 GeV
```
0
10
20
30
40
50
60
70
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.29 (0.75)
```
1.5 < EECL < 2 GeVdt = 365 fb
1
uu/dd/ss/ccTotal MC unc.
Data
1.5 1.6 1.7 1.8 1.9 2.0extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 66: Fitting variables in continuum processes on off-resonance data in SR of
```
B+ → D∗0(D0 π0) ρ+
```
```
avoid revealing any information about R(D∗) from the signal and normalization events1490
```
that are present in the sideband regions.1491
In Figures 67 - 70 we present the postfit distributions of the control fit. We observe a1492
good Data/MC agreement confirming the good GoF p-values that we get from the fit.1493
0
50
100
150
200
250
300
350
400
```
Events / (0.45 )
```
```
B0 D* (D0 ) +2 / 2 = 0.31 (0.73)
```
1 ext. track
cos hel < 0postfit
Belle II Preliminary
0
10
20
30
40
```
Events / (0.001 GeV)
```
```
B0 D* (D0 ) +2 / 5 = 0.61 (0.69)
```
1 ext. track
cos hel < 0postfit
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5
-3-1
13
5
NData
NMC2NData + 2NMC
0.143 0.144 0.145 0.146 0.147 0.148MD* in GeV-5
-3-1
13
5
NData
NMC2NData + 2NMC
```
Figure 67: Post fit distributions of the control fit for B0 → D∗−(D0 π−) π+that are con-
```
straining BB decays.
We apply these these scaling factors as well as the FEI calibration factors derived in1494
5.11 to all simulated data data for the rest of the Data/MC checks that we perform.1495
90
Table 46: Results for control fits
Reco channel BB GoF p-value
```
B0 → D∗−(D0 π−) π+cos θτhel > 0 0.6521 ± 0.1271 ± 0.0470
```
63.92%
```
B0 → D∗−(D0 π−) π+cos θτhel < 0 0.6735 ± 0.0792 ± 0.0489
```
```
B0 → D∗−(D0 π−) ρ+cos θτhel > 0 (m2miss < 1) 0.4604 ± 0.1228 ± 0.0672
```
```
B0 → D∗−(D0 π−) ρ+cos θτhel < 0 (m2miss < 1) 1.2749 ± 0.3563 ± 0.0837
```
```
B0 → D∗−(D0 π−) ρ+cos θτhel > 0 (m2miss > 1) 0.6704 ± 0.1202 ± 0.0423
```
```
B0 → D∗−(D0 π−) ρ+cos θτhel < 0 (m2miss > 1) 0.8999 ± 0.1079 ± 0.0129
```
```
B+ → D∗0(D0 π0) π+cos θτhel > 0 0.6396 ± 0.074 ± 0.0423
```
```
B+ → D∗0(D0 π0) π+cos θτhel < 0 0.7026 ± 0.0583 ± 0.0129
```
```
B+ → D∗0(D0 π0) ρ+cos θτhel > 0 (m2miss < 1) 0.2473 ± 0.1011 ± 0.0472
```
```
B+ → D∗0(D0 π0) ρ+cos θτhel < 0 (m2miss < 1) 0.3731 ± 0.1887 ± 0.1089
```
```
B+ → D∗0(D0 π0) ρ+cos θτhel > 0 (m2miss > 1) 0.7113 ± 0.0786 ± 0.0308
```
```
B+ → D∗0(D0 π0) ρ+cos θτhel < 0 (m2miss > 1) 0.7891 ± 0.0605 ± 0.0325
```
```
B0 → D∗−(D0 π−) ℓ+ 0.4379 ± 0.0631 ± 0.0325
```
```
B+ → D∗0(D0 π0) ℓ+ 0.4504 ± 0.042 ± 0.0225
```
0.0
2.5
5.0
7.5
10.0
12.5
15.0
```
Events / (0.45 )
```
```
B0 D* (D0 ) +2 / 2 = 1.09 (0.34)
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
Belle II Preliminary
0
5
10
15
20
```
Events / (0.45 )
```
```
B0 D* (D0 ) +2 / 2 = 0.33 (0.72)
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
dt = 365 fb 1
```
B D* *B Hc + n hu
B HcHc/XsOther BB
Combinatorialuu/dd/ss/cc
Total MC unc.Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0
20
40
60
80
100
```
Events / (0.45 )
```
```
B0 D* (D0 ) +2 / 2 = 2.29 (0.1)
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
0
10
20
30
40
50
```
Events / (0.45 )
```
```
B0 D* (D0 ) +2 / 2 = 0.21 (0.81)
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
Combinatorialuu/dd/ss/cc
Total MC unc.Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 68: Post fit distributions of the control fit for B0 → D∗−(D0 π−) ρ+that are con-
```
straining BB decays.
8.3 Correctly reconstructed events with constrained normaliza-1496
tion1497
Here we present the Data/MC agreement in the q2 sideband, mainly targeting the mod-1498
eling of important observables for correctly reconstructed B → D∗ℓν events, given that1499
the overall normalization in this region is constrained by the FEI calibration.1500
We begin checking distribution on the four reconstructed object that we combined to1501
```
build Υ (4S) candidates, namely the Btag meson, the D0, πs and the lepton. Figure 711502
```
```
show the Mbc, M(D0), lepton momentum and πs momentum for B0 candidates in the q21503
```
91
0
50
100
150
200
250
300
350
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +2 / 15 = 0.75 (0.74)
```
1 ext. track
cos hel < 0postfit
```
cos TBTO [0.0, 3] cos TBTO [0.3, 0.6] cos TBTO (0.6, 0.9]
```
Belle II Preliminary
0
20
40
60
80
100
120
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +2 / 15 = 0.36 (0.99)
```
1 ext. track
cos hel > 0postfit
```
cos TBTO [0.0, 3] cos TBTO [0.3, 0.6] cos TBTO (0.6, 0.9]
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5
-3-1
13
5
NData
NMC2NData + 2NMC
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5
-3-1
13
5
NData
NMC2NData + 2NMC
```
Figure 69: Post fit distributions of the control fit for B+ → D∗0(D0 π0) π+that are con-
```
straining BB decays.
0
5
10
15
20
```
Events / (0.45 )
```
```
B+ D*0(D0 0) +2 / 2 = 0.13 (0.88)
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
Belle II Preliminary
0
20
40
60
80
```
Events / (0.45 )
```
```
B+ D*0(D0 0) +2 / 2 = 0.0 (1.0)
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
```
dt = 365 fb 1
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8Bcos TBTOtag-5-3
-113
5
NData
NMC2NData + 2NMC
0
25
50
75
100
125
150
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +2 / 10 = 0.87 (0.56)
```
1.5 < EECL < 2 GeV
cos hel < 0 & m2miss [ 1, 1]postfit
cos TBTO [0.0, 45] cos TBTO [0.45, 0.9] 0
20
40
60
80
```
Events / (1 GeV)
```
```
B+ D*0(D0 0) +2 / 10 = 0.63 (0.79)
```
1.5 < EECL < 2 GeV
cos hel > 0 & m2miss [1, 7]postfit
cos TBTO [0.0, 45] cos TBTO [0.45, 0.9]
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
1.84 1.85 1.86 1.87 1.88 1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 70: Post fit distributions of the control fit for B+ → D∗0(D0 π0) ρ+that are con-
```
straining BB decays.
sidebands after applying the FEI calibration, for the electron and muon channels. All1504
quantities demonstrate good Data/MC agreement.1505
```
We continue with B± candidates. Figure 72 shows the Mbc, M(D0), lepton momentum1506
```
and πs momentum for B± candidates in the q2 sidebands after applying the FEI calibra-1507
tion. All quantities demonstrate good Data/MC agreement except for the momentum of1508
the slow neutral pion in the electron channel. We presume that there is something off with1509
the calibration of the neutral slow pions from the Performance group. The corrections1510
that we have applied have been presented in Table 25. Nevertheless we are confident that1511
any overall mismatch in the yield is taken care of by all our calibrations for all the differ-1512
ent components, therefore such a mismodelling will not affect our extracted parameters1513
of interest.1514
In Figure 73 we present the m2miss distribution of both B0 and B±. This uses the same1515
92
0
100
200
300
400
500
Events / Bin
```
B0 D* (D0 ) +2 / 6 = 0.8 (0.57)q2 < 4 GeV2
```
Belle II Preliminary
0
50
100
150
200
Events / Bin
```
B0 D* (D0 ) +2 / 11 = 0.92 (0.52)q
```
2 < 4 GeV2dt = 365 fb
1
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900MBtagbc in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.5 1.0 1.5 2.0 2.5plab+ in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
200
400
600
800
Events / Bin
```
B0 D* (D0 ) +2 / 5 = 1.17 (0.32)q2 < 4 GeV2
```
0
100
200
300
400
500
600
Events / Bin
```
B0 D* (D0 ) +2 / 4 = 2.39 (0.05)q
```
2 < 4 GeV2 B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p slow in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 71: Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and πs
```
```
momentum (bottom right) for the B0 → D∗−(D0 π−) e+in the q2 sideband.
```
0
100
200
300
400
500
600
Events / Bin
```
B+ D*0(D0 0) +2 / 6 = 0.96 (0.45)q2 < 4 GeV2
```
Belle II Preliminary
0
50
100
150
200
250
Events / Bin
```
B+ D*0(D0 0) +2 / 11 = 1.46 (0.14)q
```
2 < 4 GeV2dt = 365 fb
1
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900MBtagbc in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.5 1.0 1.5 2.0 2.5plab+ in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
200
400
600
800
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 0.97 (0.43)q2 < 4 GeV2
```
0
100
200
300
400
500
600
Events / Bin
```
B+ D*0(D0 0) +2 / 4 = 2.51 (0.04)q
```
```
2 < 4 GeV2 B D* ( )
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p slow in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 72: Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and πs
```
```
momentum (bottom right) for the B+ → D∗0(D0 π0) e+in the q2 sideband.
```
binning that will be used for the extraction of B → D∗ℓν decays in the NR.1516
93
0
200
400
600
800
1000
1200
Events / Bin
```
B0 D* (D0 ) +2 / 3 = 1.11 (0.34)q2 < 4 GeV2
```
Belle II Preliminary
0
200
400
600
800
1000
1200
1400
Events / Bin
```
B+ D*0(D0 0) +2 / 3 = 2.36 (0.07)q2 < 4 GeV2
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2miss in GeV2-5
-3-1
13
5
NData
NMC2NData + 2NMC
1.0 0.5 0.0 0.5 1.0 1.5 2.0m2miss in GeV2-5
-3-1
13
5
NData
NMC2NData + 2NMC
```
Figure 73: m2miss distribution for B0 (left) and B± (right) mesons in the q2 sideband
```
8.4 Correctly reconstructed events with free normalization1517
Here we present the Data/MC agreement in the NR, mainly targeting the modeling of1518
important observables for correctly reconstructed B → D∗ℓν events. Even though this1519
region is used in the final fit, we do not expect any new physics impact since B →1520
D∗ℓν decays have been measured multiple times in the past. We have also received WG1521
premission to look into this region. We first plot the EextraECL distribution first without1522
applying the photon multiplicity correction in Figure 74. We see that there is a severe1523
mismodelling of the EextraECL variable as observed in other analyses as well. We therefore1524
apply the photon multiplicity correction and in Figure 75 we observe that the Data/MC1525
agreement is restored.1526
0
500
1000
1500
2000
Events / Bin
```
B0 D* (D0 ) +2 / 5 = 8.08 (0.0)q2 > 4 GeV
```
Belle II Preliminary
0
500
1000
1500
2000
2500
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 11.96 (0.0)q2 > 4 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
0.0 0.2 0.4 0.6 0.8 1.0extra E in ECL in GeV-5-3
-11
35
NData
NMC2NData + 2N
MC
0.0 0.2 0.4 0.6 0.8 1.0extra E in ECL in GeV-5-3
-11
35
NData
NMC2NData + 2N
MC
```
Figure 74: EextraECL distribution for B0 (left) and B± (right) mesons in the NR sideband
```
In Figures 76 and 77 we plot the same variables that we plotted in the low q2 sideband,1527
except m2miss which is the fitting variable we’re going to use in the final fit.1528
We see that in all distributions except for the momentum of the slow pion -just like1529
in the case of the q2 sideband, the photon multiplicity correction is restoring Data/MC1530
agreement. We avoid looking at the m2miss distribution as this would essentially open1531
the box for one of our fitting distributions which we want to do at a later stage. We1532
conclude that no mismodelling is observed in the relevant observables and that the photon1533
multiplicity correction is restoring Data/MC agreement in the EextraECL distribution, therefore1534
can be safely applied to correctly reconstructed events, i.e. B → D∗τ ν events the SR.1535
94
0
500
1000
1500
2000
Events / Bin
```
B0 D* (D0 ) +2 / 5 = 1.03 (0.4)q2 > 4 GeV
```
Belle II Preliminary
0
500
1000
1500
2000
2500
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 0.89 (0.48)q2 > 4 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Data
0.0 0.2 0.4 0.6 0.8 1.0extra E in ECL in GeV-5-3
-11
35
NData
NMC2NData + 2N
MC
0.0 0.2 0.4 0.6 0.8 1.0extra E in ECL in GeV-5-3
-11
35
NData
NMC2NData + 2N
MC
```
Figure 75: EextraECL distribution for B0 (left) and B± (right) mesons in the NR sideband
```
after applying the photon multiplicity correction.
0
200
400
600
800
1000
1200
Events / Bin
```
B0 D* (D0 ) +2 / 6 = 1.12 (0.35)q2 > 4 GeV
```
Belle II Preliminary
0
100
200
300
400
500
600
Events / Bin
```
B0 D* (D0 ) +2 / 11 = 1.19 (0.28)q
```
2 > 4 GeVdt = 365 fb
1
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900MBtagbc in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.5 1.0 1.5 2.0 2.5plab+ in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
250
500
750
1000
1250
1500
1750
Events / Bin
```
B0 D* (D0 ) +2 / 5 = 1.53 (0.18)q2 > 4 GeV
```
0
200
400
600
800
1000
1200
1400
Events / Bin
```
B0 D* (D0 ) +2 / 4 = 0.89 (0.47)q
```
```
2 > 4 GeV B D* ( )
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p slow in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 76: Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and πs
```
```
momentum (bottom right) for the B0 → D∗−(D0 π−) ℓ+in the NR.
```
8.5 Misreconstructed events with constrained normalization1536
Here we present the Data/MC agreement in the regions used in the control fit. Since1537
the normalization here if fixed by the control fit we mainly seek to validate the shapes1538
of the imporantant variables that will be used in the final fit. In particular we’re looking1539
at the EextraECL distribution, the reconstructed helicity angle and m2miss since these are the1540
observables used in final fit in the SR. On top of the weights derived by the control fits we1541
also apply the photon multiplicity reweighting to ensure its validity in these constrained1542
sidebands. Figure 78 - 81 show the distributions of these variables in all the control1543
regions. Since the normalization of those is fixed by the control fit, we don’t expect any1544
significant differences in the overall yield. However the shape of those variables could be1545
mismodeled.1546
Based on Figures 78 - 81 we conclude the shape of all important variables is well1547
95
0
200
400
600
800
1000
1200
1400
Events / Bin
```
B+ D*0(D0 0) +2 / 6 = 0.77 (0.6)q2 > 4 GeV
```
Belle II Preliminary
0
100
200
300
400
500
600
700
Events / Bin
```
B+ D*0(D0 0) +2 / 11 = 0.94 (0.5)q
```
2 > 4 GeVdt = 365 fb
1
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
5.2725 5.2750 5.2775 5.2800 5.2825 5.2850 5.2875 5.2900MBtagbc in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.5 1.0 1.5 2.0 2.5plab+ in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0
500
1000
1500
2000
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 0.77 (0.57)q2 > 4 GeV
```
0
250
500
750
1000
1250
1500
1750
Events / Bin
```
B+ D*0(D0 0) +2 / 4 = 4.22 (0.0)q
```
```
2 > 4 GeV B D* ( )
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1.84 1.85 1.86 1.87 1.88 1.89MD0 in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p slow in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
```
Figure 77: Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and πs
```
```
momentum (bottom right) for the B+ → D∗0(D0 π0) ℓ+in NR.
```
0
100
200
300
400
500
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.03 (0.97)1 ext. track
```
Belle II Preliminary
0
100
200
300
400
500
600
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.18 (0.84)1 ext. track
```
0
20
40
60
80
100
```
Events / (0.12 GeV)
```
```
B0 D* (D0 ) +2 / 10 = 0.96 (0.47)1 ext. track
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
2 1 0 1cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 78: Data/MC aggreement of the fitting variables in the control fit region for
```
B0 → D∗−(D0 π−) π+
```
0
25
50
75
100
125
150
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.07 (0.94)1.5 < EECL < 2 GeV
```
Belle II Preliminary
0
50
100
150
200
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.07 (0.93)1.5 < EECL < 2 GeV
```
0
20
40
60
80
```
Events / (0.12 GeV)
```
```
B0 D* (D0 ) +2 / 4 = 0.67 (0.61)1.5 < EECL < 2 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.5 1.6 1.7 1.8 1.9 2.0extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 79: Data/MC aggreement of the fitting variables in the control fit region for
```
B0 → D∗−(D0 π−) ρ+
```
96
0
500
1000
1500
2000
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.06 (0.94)1 ext. track
```
Belle II Preliminary
0
500
1000
1500
2000
2500
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 1.35 (0.26)1 ext. track
```
0
50
100
150
200
250
300
```
Events / (0.12 GeV)
```
```
B+ D*0(D0 0) +2 / 10 = 0.35 (0.97)1 ext. track
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.5 1.0 0.5 0.0 0.5 1.0 1.5cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
0.0 0.2 0.4 0.6 0.8 1.0 1.2extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 80: Data/MC aggreement of the fitting variables in the control fit region for
```
B+ → D∗0(D0 π0) π+
```
0
200
400
600
800
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.28 (0.75)1.5 < EECL < 2 GeV
```
Belle II Preliminary
0
200
400
600
800
1000
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.25 (0.78)1.5 < EECL < 2 GeV
```
0
50
100
150
200
250
300
```
Events / (0.12 GeV)
```
```
B+ D*0(D0 0) +2 / 4 = 0.41 (0.8)1.5 < EECL < 2 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1.0 0.5 0.0 0.5 1.0 1.5cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.5 1.6 1.7 1.8 1.9 2.0extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 81: Data/MC aggreement of the fitting variables in the control fit region for
```
B+ → D∗0(D0 π0) ρ+
```
modeled in the relevant resolution of this analysis.1548
8.6 Misreconstructed events with free normalization1549
Here we present the Data/MC agreement in the validation region defined as 1.25 < EextraECL1550
< 1.5 GeV. Here we’re mainly targeting to confirm that the modeling of important1551
observables that play a significant role in the final for misreconstructed events are well1552
modeled. This also validates all the calibrations that we’re carrying out throughout the1553
```
analysis i.e. FEI calibration (5.11), photon multiplicity reweighting (5.12) and the control1554
```
```
fits (8.2), as all the relevant weights are applied in the following plots. In Figures 82- 851555
```
we present the Data/MC agreement for the four hadronic reconstruction channels in the1556
high EextraECL sidebandthat we keep for validation. This has been defined in Table 45. The1557
relative good p-values indicate that all our calibrations are sound and can be safely applied1558
to the SR.1559
We conclude that no mismodelling is observed in the relevant observables.1560
97
0
10
20
30
40
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 1.36 (0.26)1.25 < EECL < 1.5 GeV
```
Belle II Preliminary
0
10
20
30
40
50
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 1.7 (0.18)1.25 < EECL < 1.5 GeV
```
0
5
10
15
20
25
30
```
Events / (0.12 GeV)
```
```
B0 D* (D0 ) +2 / 2 = 2.01 (0.13)1.25 < EECL < 1.5 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
2 1 0 1cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.25 1.30 1.35 1.40 1.45 1.50extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 82: Data/MC aggreement of the fitting variables in the validation region for
```
B0 → D∗−(D0 π−) π+
```
0
20
40
60
80
100
120
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 0.81 (0.45)1.25 < EECL < 1.5 GeV
```
Belle II Preliminary
025
5075
100125
150175
Events / Bin
```
B0 D* (D0 ) +2 / 2 = 1.71 (0.18)1.25 < EECL < 1.5 GeV
```
0
10
20
30
40
50
Events / Bin
```
B0 D* (D0 ) +2 / 5 = 0.79 (0.55)1.25 < EECL < 1.5 GeV
```
```
dt = 365 fb 1
```
```
B D* ( )B D*
```
B D* *B Hc + n hu
B HcHc/XsOther BB
missIDCombinatorial
uu/dd/ss/ccTotal MC unc.
Data
1 0 1 2 3cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.25 1.30 1.35 1.40 1.45 1.50extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 83: Data/MC aggreement of the fitting variables in the validation region for
```
B0 → D∗−(D0 π−) ρ+
```
0
20
40
60
80
100
120
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 2.68 (0.07)1.25 < EECL < 1.5 GeV
```
Belle II Preliminary
0
25
50
75
100
125
150
175
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 2.46 (0.09)1.25 < EECL < 1.5 GeV
```
0
10
20
30
40
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 1.34 (0.24)
```
1.25 < EECL < 1.5 GeVdt = 365 fb
1
```
B D* ( )B D* *
```
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.5 1.0 0.5 0.0 0.5 1.0 1.5cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.25 1.30 1.35 1.40 1.45 1.50extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 84: Data/MC aggreement of the fitting variables in the validation region for
```
B+ → D∗0(D0 π0) π+
```
98
0
50
100
150
200
250
300
350
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.58 (0.56)1.25 < EECL < 1.5 GeV
```
Belle II Preliminary
0
100
200
300
400
500
Events / Bin
```
B+ D*0(D0 0) +2 / 2 = 0.9 (0.41)1.25 < EECL < 1.5 GeV
```
0
20
40
60
80
100
120
140
Events / Bin
```
B+ D*0(D0 0) +2 / 5 = 0.46 (0.81)
```
1.25 < EECL < 1.5 GeVdt = 365 fb
1
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
Total MC unc.Data
1.0 0.5 0.0 0.5 1.0 1.5cos hel-5-3
-113
5
NData
NMC2NData + 2NMC
0 2 4 6m2miss in GeV2-5-3
-113
5
NData
NMC2NData + 2NMC
1.25 1.30 1.35 1.40 1.45 1.50extra E in ECL in GeV-5-3
-113
5
NData
NMC2NData + 2NMC
Figure 85: Data/MC aggreement of the fitting variables in the validation region for
```
B+ → D∗0(D0 π0) ρ+
```
99
9 Results1561
In this sections we present the proposed box opening strategy and at a later stage of the1562
review, we will first present the boxed closed, partially box opened and fully box opened1563
results.1564
9.1 Box-opening strategy1565
```
We propose the the following distinct steps towards the full box opening of the R(D∗)1566
```
and Pτ result. Every step will be carried out once the previous step has been successfully1567
validated.1568
1. Fit in NR and validation region1569
• Check Data/MC agreement of m2miss in the NR. This is the only variable we1570
```
haven’t looked at in the NR since we’re fitting it. If no problems proceed to;1571
```
```
• Run fit including only B0 → D∗−(D0 π−) ℓ+and B+ → D∗0(D0 π0) ℓ+and hadronic1572
```
validation region of [1.25-1.5]. Check value of Re/µ.1573
• Check behavior of all nuisance parameters on experimental data. Provide pull1574
plots.1575
2. Fit in high EextraECL SR and NR region1576
• Check Data/MC agreement of signal extraction variable in the high EextraECL re-1577
```
gion [0.75, 1.25] GeV of the SR. If no problems proceed to;1578
```
• Run fit including NR and high EextraECL [0.75-1.25]. This region should have small1579
```
sensitivity on R(D∗) and Pτ .1580
```
• Repeat studies for behavior of nuisance parameters.1581
3. Fit in full EextraECL range of SR and NR region and splits.1582
• Check Data/MC agreement of signal extraction variables in the full EextraECL1583
```
range. If no problems proceed to;1584
```
```
• Run fit in SR with the R(D∗) and Pτ central values masked including only1585
```
```
all possible combinations of lepton (µ, e) and hadron channels (π, ρ). Include1586
```
splits based on proc/prompt, positive/negative lepton or hadron and evaluate1587
with 0. Evaluate that the difference of derived results from all the different1588
splits are compatible with 0.1589
• Repeat studies for the behavior of nuisance parameters.1590
4. Full unboxing of SR and final result.1591
9.2 Box-closed results1592
the title1593
100
9.3 Box opened results1594
The title1595
101
A SysVar1596
The software uses class composition and class inheritance as its main design patterns1597
making is easily extendable to any source of systematic uncertainty. An overview of the1598
software modules can be seen in Figure 861599
Core part of
the software
Figure 86: Module overview of the SysVar software
SysVar implements Data/MC corrections and their respective uncertainties based on1600
the recommendations of the performance group. A few examples are slow pion recon-1601
struction efficiencies, LID efficiencies or fake rates etc. It also allows for the creation of1602
custom corrections like BF corrections. Currently corrections for the MC15ri campaing1603
and for the Belle MC have been implemented. The SysVar package provides a growing1604
list of visualization methods that enable the user to follow all the steps in a educating1605
way and carefully run diagnostic tests. We provide a quick walkthrough of the SysVar1606
workflow using a toy example implementing a pseudocorrection.1607
Imagine a scenario where one wants to perform a simultaneous 2D fit in two recon-1608
struction channels usind the pseudovariables displayed in Figure 87.1609
Now imagine that there is a momentum dependant corrections that is applied on sim-1610
ulated data. The momentum dependance of the correction is displayed in Figure 88. The1611
histograms in Figure 88 are binned based on the bins of the pseudocorrection. The corre-1612
lations between the different correction bins may be well defined, however the correlation1613
effect that those may have on the different bins of the signal extraction variables is a1614
priori not known.1615
SysVar provides the used with the tools to visualize the Data/MC correction central1616
values, uncertainties and underlying correlations. The central values and the unceratinties1617
can be seen in 89. The correlations between the different corrections bins of course depend1618
on the way that the corrections have been determined. SysVar provides the tools to1619
102
0.0 0.2 0.4 0.6 0.8 1.0Pseudo fit-variable 10
10
20
30
40
50
60
Events
Reco channel 1
SignalBKG
0.0 0.2 0.4 0.6 0.8 1.0Pseudo fit-variable 10
10
20
30
40
50
60
Events
Reco channel 2
SignalBKG
1.0 1.5 2.0 2.5 3.0 3.5 4.0Pseudo fit-variable 20
20
40
60
80
100
Events
Reco channel 1
SignalBKG
1.0 1.5 2.0 2.5 3.0 3.5 4.0Pseudo fit-variable 20
20
40
60
80
100
Events
Reco channel 2
SignalBKG
Figure 87: Pseudovariables for signal extraction
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p corr. in GeV0
20
40
60
80
100
Events
Reco channel 1
SignalBKG
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40p corr. in GeV0
20
40
60
80
100
Events
Reco channel 2
SignalBKG
Figure 88: Pseudovariable for correction bins
visualize these correlation as well as can bee seen in Figures 90, 91 and 92.1620
SysVar subsequenty builds a total covariance matrix from the three different sources1621
of uncertainty on the correction central value. Such a covariance matrix is illustrated in1622
Figure 93a Then SysVar samples from multi gaussian distributions to generate variations1623
of the correction central values based on the total covariance matrix. The number of1624
variations has to be declared by the used. The variations can be found in 93b1625
SysVar will then histgram the simulated data data and will also create varied his-1626
tograms based on the correction weight variations. In this example 201 histograms will1627
be create. One for the nominal template and 200 with the varied correction weights. A1628
103
0.96 0.97 0.98 0.99 1.00 1.01 1.02Correction weight
0.05 < slow_pi_p < 0.12 GeV
0.12 < slow_pi_p < 0.16 GeV
0.16 < slow_pi_p < 0.2 GeV
p uncertainties
central value w/ total unc.
sys
stat_uncorr
stat_corr
Figure 89: Different corrections and error sources. In this example three sources of
uncertainty are considered for the correction. Two statistical in nature and one systematic
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
0.05 < slow_pi_p < 0.12 GeV
0.12 < slow_pi_p < 0.16 GeV
0.16 < slow_pi_p < 0.2 GeV
Correction bins
0.00048 0 0
0 0.00029 0
0 0 0.00036
Covariance matrix
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
Correction bins
1 0 0
0 1 0
0 0 1
Correlation matrix
0.0000
0.0001
0.0002
0.0003
0.0004
Covariance
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
stat_uncorr uncertainty
Figure 90
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
0.05 < slow_pi_p < 0.12 GeV
0.12 < slow_pi_p < 0.16 GeV
0.16 < slow_pi_p < 0.2 GeV
Correction bins
0.00022 0.00022 0.00022
0.00022 0.00022 0.00022
0.00022 0.00022 0.00022
Covariance matrix
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
Correction bins
1 1 1
1 1 1
1 1 1
Correlation matrix
0.00021
0.00022
0.00023
0.00024
Covariance
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
stat_corr uncertainty
Figure 91
set of overview plots allows the user to examine closely the effect of the variations in1629
each template. In Figure 94 we provide an example of the signal template in the first1630
reconstruction channel.1631
Finally SysVar performs the eigendecomposition simultaneously in all bins, for all1632
templates and for all reconstruction channels. This enables for consistent treatment of1633
104
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
0.05 < slow_pi_p < 0.12 GeV
0.12 < slow_pi_p < 0.16 GeV
0.16 < slow_pi_p < 0.2 GeV
Correction bins
0.00071 0.00022 0.00022
0.00022 0.00051 0.00022
0.00022 0.00022 0.00059
Covariance matrix
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
Correction bins
1 0 0
0 1 0
0 0 1
Correlation matrix
0.0003
0.0004
0.0005
0.0006
0.0007
Covariance
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
sys uncertainty
Figure 92
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
0.05 < slow_pi_p < 0.12 GeV
0.12 < slow_pi_p < 0.16 GeV
0.16 < slow_pi_p < 0.2 GeV
Correction bins
0.00071 0.00022 0.00022
0.00022 0.00051 0.00022
0.00022 0.00022 0.00059
Covariance matrix
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeVCorrection bins
Correction bins
1 0.37 0.35
0.37 1 0.41
0.35 0.41 1
Correlation matrix
0.0003
0.0004
0.0005
0.0006
0.0007
Covariance
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Total covariance for p
```
(a) The total covariance matrix from all corrections
```
0.05 < slow_pi_p < 0.12 GeV0.12 < slow_pi_p < 0.16 GeV0.16 < slow_pi_p < 0.2 GeV
0.9320.935
0.9380.941
0.9440.947
0.9510.954
0.9570.96
0.9630.966
0.970.973
0.9760.979
0.9820.985
0.9890.992
0.9950.998
1.0011.005
1.0081.011
1.0141.017
1.021.024
1.0271.03
1.0331.036
1.0391.043
1.0461.049
1.0521.055
1.058
Relative variation
0
2
4
6
8
10
12
14
```
(b) The vari-
```
ations of the
central values.
Here 200 vari-
ations have
been used.
Figure 93: A summary of the variations of the correction weights.
the correlations across all reconstruction channels and all templates. The correlation1634
matrix obtained can be seen in Figure 95.1635
SysVar allows to find the number of important eigendirections using two criteria:1636
105
0.0 0.2 0.4 0.6 0.8 1.0Bins0
20
40
60
80
Bins
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
fit variable bins
0.930.94
0.960.97
0.981.0
1.011.02
1.031.05
1.06
Relative variation
0
25
50
75
100
125
150
175
200
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
1.000.960.870.500.940.950.500.960.650.500.850.50 0.78
0.961.000.960.701.000.840.700.990.830.700.960.70 0.81
0.870.961.000.740.980.670.740.970.920.740.970.74 0.88
0.500.700.741.000.710.361.000.640.911.000.861.00 0.35
0.941.000.980.711.000.800.711.000.860.710.970.71 0.85
0.950.840.670.360.801.000.360.820.420.360.690.36 0.57
0.500.700.741.000.710.361.000.640.911.000.861.00 0.35
0.960.990.970.641.000.820.641.000.820.640.940.64 0.88
0.650.830.920.910.860.420.910.821.000.910.940.91 0.69
0.500.700.741.000.710.361.000.640.911.000.861.00 0.35
0.850.960.970.860.970.690.860.940.940.861.000.86 0.74
0.500.700.741.000.710.361.000.640.911.000.861.00 0.35
0.780.810.880.350.850.570.350.880.690.350.740.35 1.00
Correlation matrix
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
1.0
0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Template relative variation
Up variationDown variation
Stat error
0.0 0.2 0.4 0.6 0.8 1.0Fitting variable10 2
10 1
100
variation/stat error
Figure 94
• Taking the normalized differences of the reconstructed covariance matrix and the1637
initial covariance matrix.1638
• Calculating the trace in the eigenvalue space.1639
Here we present an example of comparing the reconstructed covariance matrix com-1640
pared to the original one. If the normalized difference of the two covariance matrices is1641
below 0.5% we conclude that the eigendirections describe the original covariance matrix1642
sufficiently enough. We keep those eigenvariations and we introduce one nuisance param-1643
eter per eigendirection in the signal extraction fit. The normalized differences of the two1644
covariance matrices can be seen in Figure 961645
For the treatment of the systematics uncertainties we make use of all the aforemen-1646
tioned features of SysVar. This approach provides a framework to consistently study and1647
evaluate systematic uncertainties by making all the steps of the PCA abundantly clear.1648
106
0246810121416182022242628303234363840424446485052545658
0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
Correlation matrix
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 95: The correlation matrix arising from all the varied templates. It is clear that
the correlation structure in this space becomes highly not trivial to model. Therefore
the eigendecomposition of it, provides a framework that simplifies the treatment of these
correlations in a easier way
107
10 0 10 20 30 40 50
Eigendirection
10 14
10 12
10 10
10 8
10 6
10 4
10 2
100
```
max(
```
|Cov
Cov
′|
Cov

```
)
```
Keeping 2/60 eigendirections
```
(first 50 considered only)
```
Figure 96: The normalized covariance matrix differences as a function of the eigendirec-
tions considered. The target precision at 0.5% is set arbitrarily by the user.
108
B PDG codes1649
Table 47: PDG codes of categories for the first layer of truth matching. Charge conjuga-
tion is used for all PDG codes.
Category PDG codes
D [411,421]
D∗ [413,423]
D∗∗ [415, 425, 10411, 10421, 10413, 10423, 20413, 20423]
Hgapc [411, 421, 413, 423, 431, 433]
Xgapu/s [111, 211, 221, 331, 321]
Hc[411, 421, 431, 413, 423, 433, 415, 425, 433,435, 10411, 10413, 10421, 10423, 10431, 10433, 20433, 20423, 20413]
Xs [130, 310, 311, 313, 321, 323, 333, 10313, 10323, 331]
Xu [43,44,111,113,221,223,331,211,213, 20113, 20213]
109
C Multinomial errors1650
In Figure 97 one can see how the difference of the ratio and the uncertainty of the ra-1651
tio calculated assuming a multinomial approximation, scales with the total number or1652
occurances. It is clear that for a small number of total occurances the multinomial ap-1653
proximation lead to unphysical values for the uncertainties as these lead to negative rates.1654
Therefore we need to be careful that the combination of total occurances and the rates1655
that are used in the FEI tag side mode composition do not lead to negative rates.1656
0.00 0.02 0.04 0.06 0.08 0.10
r
0.02
0.00
0.02
0.04
0.06
0.08
0.10
r
r
Multinomial errors
```
k = 10
```
```
k = 13
```
```
k = 20
```
```
k = 50
```
```
k = 100
```
```
k = 200
```
```
k = 500
```
```
k = 1000
```
```
k = 10000
```
Figure 97: Multinomial error scaling with number of total occurances and rates
110
D D0 mass calibration1657
We use the q2 sideband for this calibration, as it provides a clean sample of B → D∗ℓν1658
decays, meaning we have a large number of well-reconstructed D0 mesons. However, we1659
do not use true B → D∗ℓν decays to determine the calibration factors. Instead, we define1660
the signal differently:1661
• A perfectly reconstructed D0 meson with isSignal == 1, or1662
• An event where a D0 meson appears in the descendant tree of a B meson.1663
Using MC we first determine the shape of the signal by performing an unbinned likeli-1664
hood fit. Our study finds that a double Gaussian function best describes the distribution.1665
To assess the goodness of fit, we compute a pp-value, excluding the last 5% quantiles1666
since the fit lacks sensitivity in the tails of the distribution. This exclusion is justified as1667
we are primarily interested in the peak region rather than the tails.1668
The fitted Double Gaussian parameters are summarized in Table 33. Additionally, we1669
present the pre-fit signal shape, the post-fit distribution on both signal and background1670
and the goodness-of-fit test results comparing our parametric function to MC in Figures1671
98, 99, 100 and 101.1672
Figure 98: Signal shape, post fit distribution and goodness of fit for D0 → K−π+ ,
D0 → π−π+ and D0 → K−K+ on MC.
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90
```
M(D0) in GeV
```
0
200
400
600
Signal vs BKG
SignalBkg
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90
```
M(D0) in GeV
```
0
10
20
30Gauss I: 1.8648 ± 0.0186: 0.0049 ± 0.0004Gauss II: 1.8588 ± 0.0003: 0.0176 ± 0.0002
```
f : 0.2128 ± 0.0177
```
Post fit
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90
```
M(D0) in GeV
```
0
100
200
300
400
500 P-value: 7.36 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
D0 → Kππ0 and D0 → K0s π0
Figure 99: Signal shape, post fit distribution and goodness of fit for D0 → K0S π0 and
D0 → K−π+π0 on MC.
We repeat the same double Gaussian fit on experimental data. The corresponding fit1673
parameters are provided in Table 33. We also provide the postfit distributions and the1674
goodness of fit test for the fits that we run on experimental data in Figures 102, 103, 1041675
and 105.1676
```
Since our Probability Density Function (PDF) consists of multiple Gaussian compo-1677
```
```
nents, we employ the Central Limit Theorem (CLT) to estimate the overall resolution.1678
```
We first generate 20,000 toy experiments, sampling from a multivariate normal distri-1679
bution with the nominal fit parameters as means, and the covariance matrix from the1680
minimization procedure. Using the toy-generated parameters, we construct the Cumula-1681
```
tive Distribution Function (CDF) of the double Gaussian acpdf. For each toy experiment1682
```
111
1.84 1.85 1.86 1.87 1.88 1.89
```
M(D0) in GeV
```
0
100
200
300
Signal vs BKG
SignalBkg
1.84 1.85 1.86 1.87 1.88 1.89
```
M(D0) in GeV
```
0
25
50
75
100Gauss I: 1.8648 ± 0.0186: 0.0108 ± 0.0006Gauss II: 1.8646 ± 0.0001: 0.0026 ± 0.0002
```
f : 0.3288 ± 0.0337
```
Post fit
1.84 1.85 1.86 1.87 1.88 1.89
```
M(D0) in GeV
```
0
50
100
150P-value: 75.06 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
```
D0 → K0s h+h−(ππ, KK)
```
Figure 100: Signal shape, post fit distribution and goodness of fit for D0 → K0S π+π− and
D0 → K0S K+K− on MC.
1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90 1.91
```
M(D0) in GeV
```
0
100
200
300
400
500
Signal vs BKG
SignalBkg
1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90 1.91
```
M(D0) in GeV
```
0
25
50
75
100Gauss I: 1.8648 ± 0.0186: 0.0163 ± 0.0007Gauss II: 1.8641 ± 0.0001: 0.0028 ± 0.0001
```
f : 0.2488 ± 0.0167
```
Post fit
1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90 1.91
```
M(D0) in GeV
```
0
50
100
150
200 P-value: 76.24 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
D0 → K−π+π+π−
Figure 101: Signal shape, post fit distribution and goodness of fit for D0 → K−π+π−π+
on MC.
Figure 102: Signal shape, post fit distribution and goodness of fit for D0 → K−π+ ,
D0 → π−π+ and D0 → K−K+ on Data.
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90
```
M(D0) in GeV
```
0
10
20
30 Gauss I: 1.8648 ± 0.0186: 0.0051 ± 0.0004Gauss II: 1.8588 ± 0.0003: 0.0178 ± 0.0003
```
f : 0.2109 ± 0.0201
```
Post fit
1.82 1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90
```
M(D0) in GeV
```
0
100
200
300P-value: 1.38 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
D0 → Kππ0 and D0 → K0s π0
Figure 103: Signal shape, post fit distribution and goodness of fit for D0 → K0S π0 and
D0 → K−π+π0 on Data.
random values between 0 and 1 are drawn. These values are mapped onto the allowed1683
invariant mass range via the CDF. Finally the 68.3% quantile of the resulting distribution1684
is used to estimate the resolution of the fitted PDF.1685
To account for differences in mass resolution between MC and Data, we compute the1686
smearing factor as1687
```
r =
```
q
```
µ2M C − µ2DAT A (49)1688
```
This factor corrects the resolution mismatch between simulated and real events. The1689
results are presented in Table 33. Once the smearing factor is determined, we correct the1690
112
1.84 1.85 1.86 1.87 1.88 1.89
```
M(D0) in GeV
```
0
20
40
60
80
100 Gauss I: 1.8648 ± 0.0186: 0.011 ± 0.0008Gauss II: 1.8645 ± 0.0002: 0.003 ± 0.0002
```
f : 0.283 ± 0.0379
```
Post fit
1.84 1.85 1.86 1.87 1.88 1.89
```
M(D0) in GeV
```
0
20
40
60
80
100 P-value: 4.8 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
```
D0 → K0s h+h−(ππ, KK)
```
Figure 104: Signal shape, post fit distribution and goodness of fit for D0 → K0S π+π− and
D0 → K0S K+K− on Data.
1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90 1.91
```
M(D0) in GeV
```
0
20
40
60
80
100 Gauss I: 1.8648 ± 0.0186
: 0.0161 ± 0.0008
Gauss II: 1.8644 ± 0.0001
: 0.0032 ± 0.0001f : 0.253 ± 0.0199
Post fit
1.83 1.84 1.85 1.86 1.87 1.88 1.89 1.90 1.91
```
M(D0) in GeV
```
0
50
100
150 P-value: 65.65 %
Goodness of Fit testNo GoF < 5% quant.
No GoF > 95% quant.PDF pred.
MC
D0 → K−π+π+π−
Figure 105: Signal shape, post fit distribution and goodness of fit for D0 → K−π+π−π+
on Data.
reconstructed invariant mass for each event. A random shift is drawn from a Gaussian1691
distribution centered at zero with a width equal to the smearing factor. Finally this shift1692
is added to the originally reconstructed invariant mass, formally as1693
```
MD0 = MD0 + G(0, r) (50)1694
```
113
E FF model parameters1695
G1 RhoSq Deltavalue 1.0541 1.128 1.0
unc 0.0083 0.033 0.0
G1 RhoSq DeltaFF model parameters
1.00
1.02
1.04
1.06
1.08
1.10
1.12
1.14
1.16
Value
G1 RhoSq DeltaFF model parameters
G1
RhoSq
Delta
FF model parameters
1 0.75 0
0.75 1 0
0 0 1
Correlation matrix CLN B D
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 106: Parameters used in the CLN parameterization for the generation of B → Dτ ν
decays in the Belle II MC
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
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
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
0.034 -0.056 0.008 0.009 1 -0.26 -0.094 -0.034 -0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075 -0.076 -0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089 -0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 107: Target parameters used in the BLPRXP parameterization for the reweighting
of B → Dτ ν with HAMMER
114
F1 RhoSq R0 R1 R2value 0.912 1.205 1.15 1.404 0.854
unc 0.014 0.026 0.0 0.032 0.02
F1 RhoSq R0 R1 R2FF model parameters
0.9
1.0
1.1
1.2
1.3
1.4
Value
F1 RhoSq R0 R1 R2FF model parameters
F1
RhoSq
R0
R1
R2
FF model parameters
1 0.34 0 -0.1 -0.071
0.34 1 0 0.57 -0.81
0 0 1 0 0
-0.1 0.57 0 1 -0.76
-0.071 -0.81 0 -0.76 1
Correlation matrix CLN B D*
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 108: Parameters used in the CLN parameterization for the generation of B → D∗τ ν
decays in the Belle II MC
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
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
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
0.034 -0.056 0.008 0.009 1 -0.26 -0.094 -0.034 -0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075 -0.076 -0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089 -0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D*
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 109: Target parameters used in the BLPRXP parameterization for the reweighting
of B → D∗τ ν with HAMMER
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
Correlation matrix BGLB2 B D
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 110: Parameters used in the BGL parameterization for the generation of B → Dℓν
decays in the Belle II MC
115
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
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
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
0.034 -0.056 0.008 0.009 1 -0.26 -0.094 -0.034 -0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075 -0.076 -0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089 -0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 111: Target parameters used in the BLPRXP parameterization for the reweighting
of B → Dℓν with HAMMER
ag_0 ag_1 af_0 af_1 aF1_1 aF1_2
value 0.001 -0.0024 0.0005 0.0007 0.0003 -0.0037
unc 0.0 0.0 0.0 0.0 0.0 0.0
ag_0 ag_1 af_0 af_1 aF1_1 aF1_2
FF model parameters
0.003
0.002
0.001
0.000
0.001
Value
Figure 112: Parameters used in the BGL parameterization for the generation of B → D∗ℓν
decays in the Belle II MC
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
RhoStSq cSt mb DelMbc la2 eta1 rho1 chi21 phi1pFF model parameters
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
0.034 -0.056 0.008 0.009 1 -0.26 -0.094 -0.034 -0.006
0.42 0.38 -0.43 0.11 -0.26 1 -0.38 -0.37 0.19
-0.075 -0.076 -0.007 0.48 -0.094 -0.38 1 0.1 -0.28
-0.47 -0.65 0.37 -0.089 -0.034 -0.37 0.1 1 0.3
-0.63 -0.11 0.36 0.011 -0.006 0.19 -0.28 0.3 1
Correlation matrix BLPRXP B D*
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 113: Target parameters used in the BLPRXP parameterization for the reweighting
of B → D∗ℓν with HAMMER
t1 tp tau1 tau2value 0.71 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.6
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.83 0.66 -0.63
-0.83 1 -0.27 0.2
0.66 -0.27 1 -0.93
-0.63 0.2 -0.93 1
Correlation matrix BLR B D* *1
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 114: Parameters used in the BLR parameterization for the generation of B →
D∗∗1 ℓν decays in the Belle II MC
t1 tp tau1 tau2value 0.7 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.4
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.85 0.53 -0.49
-0.85 1 -0.17 0.086
0.53 -0.17 1 -0.89
-0.49 0.086 -0.89 1
Correlation matrix BLR B D* *1
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 115: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗1 ℓν with HAMMER
117
t1 tp tau1 tau2value 0.71 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.6
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.83 0.66 -0.63
-0.83 1 -0.27 0.2
0.66 -0.27 1 -0.93
-0.63 0.2 -0.93 1
Correlation matrix BLR B D* *1
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 116: Parameters used in the BLR parameterization for the generation of B →
D∗∗1 τ ν decays in the Belle II MC
t1 tp tau1 tau2value 0.7 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.4
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.85 0.53 -0.49
-0.85 1 -0.17 0.086
0.53 -0.17 1 -0.89
-0.49 0.086 -0.89 1
Correlation matrix BLR B D* *1
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 117: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗1 τ ν with HAMMER
zt1 ztp zeta1value 0.68 -0.2 0.3
unc 0.2 1.2 0.3
zt1 ztp zeta1FF model parameters1.5
1.0
0.5
0.0
0.5
1.0
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.35
-0.95 1 0.51
-0.35 0.51 1
Correlation matrix BLR B D* *0′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 118: Parameters used in the BLR parameterization for the generation of B →
D∗∗0 ℓν decays in the Belle II MC
118
zt1 ztp zeta1value 0.7 0.2 0.6
unc 0.21 1.4 0.3
zt1 ztp zeta1FF model parameters
1.0
0.5
0.0
0.5
1.0
1.5
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.44
-0.95 1 0.61
-0.44 0.61 1
Correlation matrix BLR B D* *0′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 119: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗0 ℓν with HAMMER
zt1 ztp zeta1value 0.68 -0.2 0.3
unc 0.2 1.2 0.3
zt1 ztp zeta1FF model parameters1.5
1.0
0.5
0.0
0.5
1.0
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.35
-0.95 1 0.51
-0.35 0.51 1
Correlation matrix BLR B D* *0′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 120: Parameters used in the BLR parameterization for the generation of B →
D∗∗0 τ ν decays in the Belle II MC
zt1 ztp zeta1value 0.7 0.2 0.6
unc 0.21 1.4 0.3
zt1 ztp zeta1FF model parameters
1.0
0.5
0.0
0.5
1.0
1.5
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.44
-0.95 1 0.61
-0.44 0.61 1
Correlation matrix BLR B D* *0′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 121: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗0 τ ν with HAMMER
119
zt1 ztp zeta1value 0.68 -0.2 0.3
unc 0.2 1.2 0.3
zt1 ztp zeta1FF model parameters1.5
1.0
0.5
0.0
0.5
1.0
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.35
-0.95 1 0.51
-0.35 0.51 1
Correlation matrix BLR B D* *1′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 122: Parameters used in the BLR parameterization for the generation of B →
D∗∗1′ ℓν decays in the Belle II MC
zt1 ztp zeta1value 0.7 0.2 0.6
unc 0.21 1.4 0.3
zt1 ztp zeta1FF model parameters
1.0
0.5
0.0
0.5
1.0
1.5
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.44
-0.95 1 0.61
-0.44 0.61 1
Correlation matrix BLR B D* *1′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 123: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗1′ ℓν with HAMMER
zt1 ztp zeta1value 0.68 -0.2 0.3
unc 0.2 1.2 0.3
zt1 ztp zeta1FF model parameters1.5
1.0
0.5
0.0
0.5
1.0
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.35
-0.95 1 0.51
-0.35 0.51 1
Correlation matrix BLR B D* *1′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 124: Parameters used in the BLR parameterization for the generation of B →
D∗∗1′ τ ν decays in the Belle II MC
120
zt1 ztp zeta1value 0.7 0.2 0.6
unc 0.21 1.4 0.3
zt1 ztp zeta1FF model parameters
1.0
0.5
0.0
0.5
1.0
1.5
Value
zt1 ztp zeta1FF model parameters
zt1
ztp
zeta1
FF model parameters
1 -0.95 -0.44
-0.95 1 0.61
-0.44 0.61 1
Correlation matrix BLR B D* *1′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 125: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗1′ τ ν with HAMMER
t1 tp tau1 tau2value 0.71 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.6
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.83 0.66 -0.63
-0.83 1 -0.27 0.2
0.66 -0.27 1 -0.93
-0.63 0.2 -0.93 1
Correlation matrix BLR B D* *2′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 126: Parameters used in the BLR parameterization for the generation of B →
D∗∗2 ℓν decays in the Belle II MC
t1 tp tau1 tau2value 0.7 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.4
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.85 0.53 -0.49
-0.85 1 -0.17 0.086
0.53 -0.17 1 -0.89
-0.49 0.086 -0.89 1
Correlation matrix BLR B D* *2′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 127: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗2 ℓν with HAMMER
121
t1 tp tau1 tau2value 0.71 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.6
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.83 0.66 -0.63
-0.83 1 -0.27 0.2
0.66 -0.27 1 -0.93
-0.63 0.2 -0.93 1
Correlation matrix BLR B D* *2′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 128: Parameters used in the BLR parameterization for the generation of B →
D∗∗2 τ ν decays in the Belle II MC
t1 tp tau1 tau2value 0.7 -1.6 -0.5 2.9
unc 0.07 0.2 0.3 1.4
t1 tp tau1 tau2FF model parameters2
1
0
1
2
3
4
Value
t1 tp tau1 tau2FF model parameters
t1
tp
tau1
tau2
FF model parameters
1 -0.85 0.53 -0.49
-0.85 1 -0.17 0.086
0.53 -0.17 1 -0.89
-0.49 0.086 -0.89 1
Correlation matrix BLR B D* *2′
0.0
0.2
0.4
0.6
0.8
1.0
Pearson coeff.
Figure 129: Target parameters used in the BLR parameterization for the reweighting of
B → D∗∗2 τ ν with HAMMER
122
F FEI calibration fit validation1696
3 2 1 0 1 2 3
FEIB0FEIB0SM
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 5000 toys
= 0.0091 ± 0.0142= 1.0022 ± 0.0100
3 2 1 0 1 2 3
BKGB0BKGB0SM
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 5000 toys
= 0.0161 ± 0.0144= 1.0167 ± 0.0102
3 2 1 0 1 2 3
FEIB±FEIB±SM
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 5000 toys= 0.0154 ± 0.0141= 0.9966 ± 0.0100
3 2 1 0 1 2 3
BKGB±BKGB±SM
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 5000 toys= 0.0120 ± 0.0140= 0.9888 ± 0.0099
Figure 130: Bias test for FEI calibration estimation. We throw 5000 toys of toy datasets
and refit the nominal model to them. All free parameters in the fit are not biased and the
uncertanties well estimated based on the mean and standard deviation of the standard
normal fit of the pull distribution.
123
0.50 0.75 1.00 1.25 1.50 1.75 2.00
Expected FEI cal. factor
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Estimated strength
B0
B D*
BKG
0.50 0.75 1.00 1.25 1.50 1.75 2.00
Expected FEI cal. factor
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Estimated strength
B+
B D*
BKG
Figure 131: Linearity test for FEI calibration estimation. We bias an asimov dataset
by artificially injecting B → D∗ℓν decays from the nominal histograms Then we fit this
biased asimov dataset to the nominal model. The extracted FEI calibration factors scale
as expected while the background strengths remains unnafected.
D0
h h
D0
h h
0
D0
K
S h h
D0
KB D
*e
B
D*
0.70
0.75
0.80
0.85
0.90
0.95
B0
D0
h h
D0
h h
0
D0
K
S h h
D0
KB D
*e
B
D*
0.60
0.65
0.70
0.75
0.80
0.85
B+
nominal central value
nominal±1
nominal±2
nominal±3
FEI calibration factors stability check
Figure 132: Stability test for FEI calibration. We extract the FEI calibraation factors
considering different multiplicities by deriving the factors for different D0 decays modes.
We also derive them again for electrons and muons separately. All are consistent within
2σ.
124
G Statistical tests1697
3 2 1 0 1 2 3
Pull for B D* * + strength inB0 reco.
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0203 ± 0.0200
= 0.9998 ± 0.0141
3 2 1 0 1 2 3
Pull for B D* * + strength in B+ reco.
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0144 ± 0.0203
= 1.0147 ± 0.0143
```
Figure 133: Pull plots for toys B → D∗∗ℓν yields for B0 and (left) and B+ (right)
```
```
reconstrution channels for the R(D∗) fit. The parameters of the gaussian fit are compatible
```
with a standard normal.
3 2 1 0 1 2 3Pull for BB strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0256 ± 0.0195= 0.9738 ± 0.0138
3 2 1 0 1 2 3Pull for BB strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402500 toys= 0.0500 ± 0.0197= 0.9868 ± 0.0140
3 2 1 0 1 2 3Pull for BB strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402500 toys= 0.0209 ± 0.0198= 0.9901 ± 0.0140
3 2 1 0 1 2 3Pull for BB strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0098 ± 0.0196= 0.9815 ± 0.0139
Figure 134: Pull plots for toys BB yields for B0 in the τ → πντ and τ → ρντ reconstruc-
tion channels and B+ in the τ → πντ and τ → ρντ reconstruction channels from left to
```
right for the R(D∗) fit. The parameters of the gaussian fit are compatible with a standard
```
normal.
125
3 2 1 0 1 2 3Pull for qq strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402500 toys= 0.0028 ± 0.0199= 0.9947 ± 0.0141
3 2 1 0 1 2 3Pull for qq strength in B0 reco.0.0
0.1
0.2
0.3
0.42500 toys= 0.0096 ± 0.0199= 0.9933 ± 0.0140
3 2 1 0 1 2 3Pull for qq strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0275 ± 0.0201
= 1.0026 ± 0.0142
3 2 1 0 1 2 3Pull for qq strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0276 ± 0.0200= 1.0002 ± 0.0141
Figure 135: Pull plots for toys q ¯q yields for B0 in the τ → πντ and τ → ρντ reconstruction
channels and B+ in the τ → πντ and τ → ρντ reconstruction channels from left to right
```
for the R(D∗) fit. The parameters of the gaussian fit are compatible with a standard
```
normal.
3 2 1 0 1 2 3
Pull for B D* * + strength inB0 reco.
0.0
0.1
0.2
0.3
0.4
2500 toys= 0.0060 ± 0.0195
= 0.9766 ± 0.0138
3 2 1 0 1 2 3
Pull for B D* * + strength in B+ reco.
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys
= 0.0147 ± 0.0204= 1.0191 ± 0.0144
```
Figure 136: Pull plots for toys B → D∗∗ℓν yields for B0 and (left) and B+ (right)
```
reconstrution channels for the Pτ fit. The parameters of the gaussian fit are compatible
with a standard normal.
3 2 1 0 1 2 3Pull for BB strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402500 toys= 0.0576 ± 0.0207
= 1.0350 ± 0.0146
3 2 1 0 1 2 3Pull for BB strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0398 ± 0.0198= 0.9912 ± 0.0140
3 2 1 0 1 2 3Pull for BB strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.402500 toys= 0.0313 ± 0.0198= 0.9911 ± 0.0140
3 2 1 0 1 2 3Pull for BB strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0135 ± 0.0199= 0.9950 ± 0.0141
Figure 137: Pull plots for toys BB yields for B0 in the τ → πντ and τ → ρντ reconstruc-
tion channels and B+ in the τ → πντ and τ → ρντ reconstruction channels from left to
right for the Pτ fit. The parameters of the gaussian fit are compatible with a standard
normal.
126
3 2 1 0 1 2 3Pull for qq strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0005 ± 0.0201= 1.0026 ± 0.0142
3 2 1 0 1 2 3Pull for qq strength in B0 reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0039 ± 0.0202= 1.0104 ± 0.0143
3 2 1 0 1 2 3Pull for qq strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0199 ± 0.0205= 1.0266 ± 0.0145
3 2 1 0 1 2 3Pull for qq strength in B+ reco.0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40 2500 toys= 0.0345 ± 0.0203= 1.0154 ± 0.0144
Figure 138: Pull plots for toys q ¯q yields for B0 in the τ → πντ and τ → ρντ reconstruction
channels and B+ in the τ → πντ and τ → ρντ reconstruction channels from left to right
for the Pτ fit. The parameters of the gaussian fit are compatible with a standard normal.
127
H Helicity angle window optimization1698
Even though the physical region of the cosine of the τ helicity angle is between -1 and 1 we1699
expect that resolution effects will make signal events be found in unphysical regions. We1700
perform the following optimization to define the best window per reconstruction channel.1701
```
We run the suimultaneous fit of R(D∗) and Pτ for a set of different −γβEd+γpd cos θτdpτ restdwin-1702
```
dows. For every fit we include only the relevan reconstruction channel. The CR regions1703
are not included in the optimization fit due to technical complications. All backgrounds1704
are allowed to float freely. Figure 139 presents the uncertainty of Pτ for every reconstruc-1705
tion channel as determined by the asimov fit. Based on these results we determine the1706
different cosine helicity angle windows as outlined in Table 20.1707
[-2.0, 1.0][-2.0, 1.4][-2.0, 1.8][-2.0, 2.2][-2.0, 2.6][-2.0, 3.0][-1.8, 1.0][-1.8, 1.4][-1.8, 1.8][-1.8, 2.2][-1.8, 2.6][-1.8, 3.0][-1.6, 1.0][-1.6, 1.4][-1.6, 1.8][-1.6, 2.2][-1.6, 2.6][-1.6, 3.0][-1.4, 1.0][-1.4, 1.4][-1.4, 1.8][-1.4, 2.2][-1.4, 2.6][-1.4, 3.0][-1.2, 1.0][-1.2, 1.4][-1.2, 1.8][-1.2, 2.2][-1.2, 2.6][-1.2, 3.0][-1.0, 1.0][-1.0, 1.4][-1.0, 1.8][-1.0, 2.2][-1.0, 2.6][-1.0, 3.0]tau helicity window
0.94
0.96
0.98
1.00
1.02
1.04
1.06
1.08
```
(P )
```
```
B0 D* (D0 ) +
```
[-2.0, 1.0][-2.0, 1.4][-2.0, 1.8][-2.0, 2.2][-2.0, 2.6][-2.0, 3.0][-1.8, 1.0][-1.8, 1.4][-1.8, 1.8][-1.8, 2.2][-1.8, 2.6][-1.8, 3.0][-1.6, 1.0][-1.6, 1.4][-1.6, 1.8][-1.6, 2.2][-1.6, 2.6][-1.6, 3.0][-1.4, 1.0][-1.4, 1.4][-1.4, 1.8][-1.4, 2.2][-1.4, 2.6][-1.4, 3.0][-1.2, 1.0][-1.2, 1.4][-1.2, 1.8][-1.2, 2.2][-1.2, 2.6][-1.2, 3.0][-1.0, 1.0][-1.0, 1.4][-1.0, 1.8][-1.0, 2.2][-1.0, 2.6][-1.0, 3.0]tau helicity window
0.90
0.95
1.00
1.05
1.10
1.15
```
(P )
```
```
B0 D* (D0 ) +
```
[-2.0, 1.0][-2.0, 1.4][-2.0, 1.8][-2.0, 2.2][-2.0, 2.6][-2.0, 3.0][-1.8, 1.0][-1.8, 1.4][-1.8, 1.8][-1.8, 2.2][-1.8, 2.6][-1.8, 3.0][-1.6, 1.0][-1.6, 1.4][-1.6, 1.8][-1.6, 2.2][-1.6, 2.6][-1.6, 3.0][-1.4, 1.0][-1.4, 1.4][-1.4, 1.8][-1.4, 2.2][-1.4, 2.6][-1.4, 3.0][-1.2, 1.0][-1.2, 1.4][-1.2, 1.8][-1.2, 2.2][-1.2, 2.6][-1.2, 3.0][-1.0, 1.0][-1.0, 1.4][-1.0, 1.8][-1.0, 2.2][-1.0, 2.6][-1.0, 3.0]tau helicity window
0.60
0.62
0.64
0.66
0.68
0.70
```
(P )
```
```
B+ D*0(D0 0) +
```
[-2.0, 1.0][-2.0, 1.4][-2.0, 1.8][-2.0, 2.2][-2.0, 2.6][-2.0, 3.0][-1.8, 1.0][-1.8, 1.4][-1.8, 1.8][-1.8, 2.2][-1.8, 2.6][-1.8, 3.0][-1.6, 1.0][-1.6, 1.4][-1.6, 1.8][-1.6, 2.2][-1.6, 2.6][-1.6, 3.0][-1.4, 1.0][-1.4, 1.4][-1.4, 1.8][-1.4, 2.2][-1.4, 2.6][-1.4, 3.0][-1.2, 1.0][-1.2, 1.4][-1.2, 1.8][-1.2, 2.2][-1.2, 2.6][-1.2, 3.0][-1.0, 1.0][-1.0, 1.4][-1.0, 1.8][-1.0, 2.2][-1.0, 2.6][-1.0, 3.0]tau helicity window
0.96
0.97
0.98
0.99
1.00
1.01
```
(P )
```
```
B+ D*0(D0 0) +
```
Figure 139: Channel dependant optimization of the helicity angle window
128
I Selection of D0 modes1708
Since the beginning of the analysis we have tried several different reconstruction modes for1709
the decay of D0. In the last version of the analysis before the WG review we reconstructed1710
D0 mesons in eight distinct modes. A final test on the impact of every mode in the1711
sensitiviy of the analysis made us keep only six modes.1712
In order to evaluate each D0 mode’s sensitivity in the analysis I run the Asimov fit1713
once includin all the D0 decay modes and once by excluding one mode at a time. The1714
results can be seen in Figure 140.
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+no D
0 → K+K−no D0 → π+π−
no D0 → K0s π0no D
0 → K−π+π0no D0 → K0s π+π−
no D0 → K0s K+K−no D
0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60 70P uncertainty in %
no D0 → K−π+no D
0 → K+K−no D0 → π+π−
no D0 → K0s π0no D
0 → K−π+π0no D0 → K0s π+π−
no D0 → K0s K+K−no D
0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 140: Impact of every D0 mode on the sensitivity of the parameters of interest.
The uncertainties are taken from an Asimov fit. We confirm that we observe closure in
```
the fit (the central values are minimized to the expected ones)
```
1715
It is very clear that the D0 → K−K+ mode has the worst sensitivity and it worsens1716
our sensitivity in both parameters of interest. We completely exclude this mode and the1717
repeat the test. The results are presented in Figure 141.1718
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+
no D0 → π+π−
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60P uncertainty in %
no D0 → K−π+
no D0 → π+π−
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 141: Impact of every D0 mode on the sensitivity of the parameters of interest. We
completely exclude the D0 → K−K+ mode from this test. The uncertainties are taken
```
from an Asimov fit. We confirm that we observe closure in the fit (the central values are
```
```
minimized to the expected ones)
```
We observe that the D0 → π−π+ mode still deteriorates the performance of our fit.1719
We completely exclude this mode and then repeat the test. The results are presented in1720
Figure 142.1721
Since no particular mode is making the performance worse, we decide to move one1722
the remaining six D0 modes.p D0 → K−K+ and D0 → π−π+ will be excluded from the1723
analysis from now on.1724
129
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60P uncertainty in %
no D0 → K−π+
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 142: Impact of every D0 mode on the sensitivity of the parameters of interest.
We completely exclude the D0 → K−K+ and D0 → π−π+ modes from this test. The
uncertainties are taken from an Asimov fit. We confirm that we observe closure in the fit
```
(the central values are minimized to the expected ones)
```
130
J Background composition checks1725
In order to check that the background composition of the prompt hadronic and double1726
charm decays between the SR and the control regions that are being used are compatible,1727
we’re performing the following check. We select the Prompt Hadronic and Double Charm1728
component for every reconstruction channel in the SR and every sideband as described in1729
Table 42. The reconstruction channel together with the helicity bin can be seen in the tile1730
of every figure. We split the components to positive and negative reconstructed helicity as1731
```
these are treated separately in the control fit. We use the total Data/MC weight (without1732
```
```
the luminosity one to increase the statistics) to count the occurances of every individual1733
```
decay that makes it into the BBbar template. We renormalize the overal number of events1734
```
of the most abundant region (SR or sideband) to the least abundant one, in order to not1735
```
increase our statistics artificially. The regions that has been used for the renormalization1736
can be seen at the title of every subfigure. We only plot decays where we find at least 51737
events in one of the two regions as the number of different decays that are reconstructed1738
in these categories is very large. We assume that at least 5 events could have an impact1739
in our determined scaling factors which arguably is a very conservative assumption. In1740
Figures 143 - 158 we present our findings. Event though the composition is not exactly the1741
same, the statistics of every decay mode are very low to claim that they could significantly1742
alter the overal scaling factors that we derive. All these decays contribute only a hanful of1743
events out of the hundred or thousand ones that are reconstructed in the BBbar template.1744
0.0 2.5 5.0 7.5 10.0 12.5 15.0
```
contr. in BB template (137.4)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
B0 → (D∗(2010)± π± π± π± π0 π0)
```
```
2/110 decays displayed (>5 events)Normalized to SR(448.2)
```
SR EextraECL in [0, 1.25]1 ext. track
0 1 2 3 4 5 6 7
```
contr. in BB template (52.2)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
1/105 decays displayed (>5 events)Normalized to SR(236.5)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B0 → D∗ − (D0 π−) π+ cos hel < 0
```
```
Figure 143: Background composition in the B0 → D∗−(D0 π−) π+channel for the Prompt
```
Hadronic component in the negative helicity bin.
131
0 5 10 15 20
```
contr. in BB template (68.0)
```
```
B0 → (D∗(2010)± π± π0)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
B0 → (D∗(2010)± π± η)
```
```
3/51 decays displayed (>5 events)Normalized to SR(448.2)
```
SR EextraECL in [0, 1.25]1 ext. track
0 2 4 6 8
```
contr. in BB template (26.0)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
1/41 decays displayed (>5 events)Normalized to SR(236.5)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B0 → D∗ − (D0 π−) π+ cos hel > 0
```
```
Figure 144: Background composition in the B0 → D∗−(D0 π−) π+channel for the Prompt
```
Hadronic component in the positive helicity bin.
0 5 10 15 20
```
contr. in BB template (137.4)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗(2010)± D∗(2010)± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
3/257 decays displayed (>5 events)Normalized to SR(448.2)
```
SR EextraECL in [0, 1.25]1 ext. track
0 2 4 6 8
```
contr. in BB template (52.2)
```
```
B0 → (D∗(2010)± D± K0)
```
```
1/243 decays displayed (>5 events)Normalized to SR(236.5)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B0 → D∗ − (D0 π−) π+ cos hel < 0
```
```
Figure 145: Background composition in the B0 → D∗−(D0 π−) π+channel for the Double
```
Charm component in the negative helicity bin.
132
0 2 4 6 8
```
contr. in BB template (68.0)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
2/72 decays displayed (>5 events)Normalized to SR(448.2)
```
SR EextraECL in [0, 1.25]1 ext. track
0.04 0.02 0.00 0.02 0.04
```
contr. in BB template (26.0)
```
```
0/63 decays displayed (>5 events)Normalized to SR(236.5)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B0 → D∗ − (D0 π−) π+ cos hel > 0
```
```
Figure 146: Background composition in the B0 → D∗−(D0 π−) π+channel for the Double
```
Charm component in the positive helicity bin.
0.04 0.02 0.00 0.02 0.04
```
contr. in BB template (121.9)
```
```
0/124 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0.04 0.02 0.00 0.02 0.04
```
contr. in BB template (88.0)
```
```
0/74 decays displayed (>5 events)Normalized to SR(401.6)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B0 → D∗ − (D0 π−) ρ+ cos hel < 0
```
```
Figure 147: Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Prompt
```
Hadronic component in the negative helicity bin.
133
0 2 4 6 8 10 12 14
```
contr. in BB template (115.2)
```
```
B0 → (D∗(2010)± π± π0)
```
```
B0 → (D∗(2010)± π± π0 π0)
```
```
B0 → (D∗(2010)± π± π0 π0 π0)
```
```
B0 → (D∗(2010)± π± π0 η)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
B0 → (D∗(2010)± π± π± π± π0 π0)
```
```
B0 → (D∗(2010)± π± η)
```
```
7/97 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 2 4 6 8 10
```
contr. in BB template (109.5)
```
```
B0 → (D∗(2010)± π± π0)
```
```
B0 → (D∗(2010)± π± π0 η)
```
```
B0 → (D∗(2010)± π± π± π± π0)
```
```
3/63 decays displayed (>5 events)Normalized to SR(401.6)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B0 → D∗ − (D0 π−) ρ+ cos hel > 0
```
```
Figure 148: Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Prompt
```
Hadronic component in the positive helicity bin.
0 2 4 6 8 10 12 14 16
```
contr. in BB template (121.9)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
2/260 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 5 10 15 20 25
```
contr. in BB template (121.9)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
2/140 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B0 → D∗ − (D0 π−) ρ+ cos hel < 0
```
```
Figure 149: Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Double
```
Charm component in the negative helicity bin.
134
0 2 4 6 8 10 12
```
contr. in BB template (115.2)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
2/136 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 2 4 6 8 10 12
```
contr. in BB template (115.2)
```
```
B0 → (D∗(2010)± D± K0)
```
```
B0 → (D∗ ±s D∗(2010)±)
```
```
2/83 decays displayed (>5 events)Normalized to Sideband(315.6)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B0 → D∗ − (D0 π−) ρ+ cos hel > 0
```
```
Figure 150: Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Double
```
Charm component in the positive helicity bin.
0 5 10 15 20 25
```
contr. in BB template (277.3)
```
```
B+ → (D∗(2007)0 π± π± π±)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
B+ → (D∗(2007)0 π± π± π± π0 π0)
```
```
3/239 decays displayed (>5 events)Normalized to SR(1170.0)
```
SR EextraECL in [0, 1.25]1 ext. track
0 1 2 3 4 5 6 7
```
contr. in BB template (82.5)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
1/227 decays displayed (>5 events)Normalized to SR(488.2)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B+ → ¯D∗0(D0 π0) π+ cos hel < 0
```
```
Figure 151: Background composition in the B+ → D∗0(D0 π0) π+channel for the Prompt
```
Hadronic component in the negative helicity bin.
135
0 10 20 30
```
contr. in BB template (196.4)
```
```
B+ → (D∗(2010)± π± π± π0)
```
```
B+ → (D∗(2007)0 π± π0)
```
```
B+ → (D∗(2007)0 π± π0 η)
```
```
B+ → (D∗(2007)0 π± π± π±)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
B+ → (D∗(2007)0 π± η)
```
```
6/100 decays displayed (>5 events)Normalized to SR(1170.0)
```
SR EextraECL in [0, 1.25]1 ext. track
0 2 4 6 8 10 12 14
```
contr. in BB template (70.6)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
1/92 decays displayed (>5 events)Normalized to SR(488.2)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B+ → ¯D∗0(D0 π0) π+ cos hel > 0
```
```
Figure 152: Background composition in the B+ → D∗0(D0 π0) π+channel for the Prompt
```
Hadronic component in the positive helicity bin.
0 2 4 6 8 10 12 14 16
```
contr. in BB template (277.3)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (Ds1(2460)± D∗(2007)0)
```
```
B+ → (D∗(2007)0 D∗(2010)± K0)
```
```
B+ → (D∗(2007)0 D∗(2007)0 K±)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
5/566 decays displayed (>5 events)Normalized to SR(1170.0)
```
SR EextraECL in [0, 1.25]1 ext. track
0.04 0.02 0.00 0.02 0.04
```
contr. in BB template (82.5)
```
```
0/537 decays displayed (>5 events)Normalized to SR(488.2)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B+ → ¯D∗0(D0 π0) π+ cos hel < 0
```
```
Figure 153: Background composition in the B+ → D∗0(D0 π0) π+channel for the Double
```
Charm component in the negative helicity bin.
136
0 5 10 15 20
```
contr. in BB template (196.4)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (Ds1(2460)± D∗(2007)0)
```
```
B+ → (D±s D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
4/149 decays displayed (>5 events)Normalized to SR(1170.0)
```
SR EextraECL in [0, 1.25]1 ext. track
0 2 4 6 8
```
contr. in BB template (70.6)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
2/133 decays displayed (>5 events)Normalized to SR(488.2)
```
SR EextraECL in [0, 0.5]1 ext. track
```
B+ → ¯D∗0(D0 π0) π+ cos hel > 0
```
```
Figure 154: Background composition in the B+ → D∗0(D0 π0) π+channel for the Double
```
Charm component in the positive helicity bin.
0 5 10 15 20 25
```
contr. in BB template (511.9)
```
```
B+ → (D∗(2007)0 π± π0 π0 η)
```
```
B+ → (D∗(2007)0 π± π0 η)
```
```
B+ → (D∗(2007)0 π± π± π±)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
B+ → (D∗(2007)0 π± π± π± π0 π0)
```
```
B+ → (D∗(2007)0 π± π± π± π0 π0 π0)
```
```
6/247 decays displayed (>5 events)Normalized to Sideband(1479.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 2 4 6 8
```
contr. in BB template (169.7)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
1/177 decays displayed (>5 events)Normalized to SR(836.4)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B+ → ¯D∗0(D0 π0) ρ+ cos hel < 0
```
```
Figure 155: Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Prompt
```
Hadronic component in the negative helicity bin.
137
0 5 10 15 20 25 30
```
contr. in BB template (323.5)
```
```
B+ → (D∗(2010)± π± π± π0)
```
```
B+ → (D∗(2007)0 π± π0 π0)
```
```
B+ → (D∗(2007)0 π± π0 π0 π0)
```
```
B+ → (D∗(2007)0 π± π0 π0 η)
```
```
B+ → (D∗(2007)0 π± π0 η)
```
```
B+ → (D∗(2007)0 π± π± π±)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
B+ → (D∗(2007)0 π± π± π± π0 π0)
```
```
B+ → (D∗(2007)0 π± η)
```
```
9/167 decays displayed (>5 events)Normalized to Sideband(1479.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
contr. in BB template (196.8)
```
```
B+ → (D∗(2007)0 π± π0 η)
```
```
B+ → (D∗(2007)0 π± π± π±)
```
```
B+ → (D∗(2007)0 π± π± π± π0)
```
```
3/122 decays displayed (>5 events)Normalized to SR(836.4)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B+ → ¯D∗0(D0 π0) ρ+ cos hel > 0
```
```
Figure 156: Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Prompt
```
Hadronic component in the positive helicity bin.
0 5 10 15 20 25
```
contr. in BB template (511.9)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (Ds1(2460)± D∗(2007)0)
```
```
B+ → (D∗(2007)0 D∗(2010)± K0)
```
```
B+ → (D∗(2007)0 D∗(2007)0 K±)
```
```
B+ → (D±s D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
6/528 decays displayed (>5 events)Normalized to Sideband(1479.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 2 4 6 8 10
```
contr. in BB template (169.7)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
2/331 decays displayed (>5 events)Normalized to SR(836.4)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B+ → ¯D∗0(D0 π0) ρ+ cos hel < 0
```
```
Figure 157: Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Double
```
Charm component in the negative helicity bin.
138
0 5 10 15 20
```
contr. in BB template (323.5)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (Ds1(2460)± D∗(2007)0)
```
```
B+ → (D±s D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
4/285 decays displayed (>5 events)Normalized to Sideband(1479.6)
```
SR EextraECL in [0, 1.25]1.5 < EECL < 2 GeV
0 5 10 15 20
```
contr. in BB template (196.8)
```
```
B+ → (D∗s0(2317)± D∗(2007)0)
```
```
B+ → (Ds1(2460)± D∗(2007)0)
```
```
B+ → (D±s D∗(2007)0)
```
```
B+ → (D∗ ±s D∗(2007)0)
```
```
4/180 decays displayed (>5 events)Normalized to SR(836.4)
```
SR EextraECL in [0, 0.5]1.5 < EECL < 2 GeV
```
B+ → ¯D∗0(D0 π0) ρ+ cos hel > 0
```
```
Figure 158: Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Double
```
Charm component in the positive helicity bin.
139
Derivation of Off-Resonance Cut Shifts1745
```
Let Eon and Eoff be the center-of-mass (CM) energies for on-resonance and off-resonance1746
```
data, respectively.1747
1. Shifting ∆E Cuts1748
The definition of ∆E for on-resonance data:1749
∆Eon = EonB −
Eon
2
1750
For off-resonance data:1751
∆Eoff = EoffB −
Eoff
2
1752
To compare off-resonance data with on-resonance cuts, we rescale EoffB :1753
∆Eshifted =
Eon
Eoff
EoffB −
Eon
2
1754
Suppose we want to apply the on-resonance cut a < ∆Eon < b to off-resonance data . We1755
solve for the equivalent range in ∆Eoff.1756
Set ∆Eshifted = x and solve for EoffB :1757
```
x =
```
Eon
Eoff
EoffB −
Eon
2
=⇒
Eon
Eoff
```
EoffB = x +
```
Eon
2
=⇒ EoffB =
x + Eon2
Eon
Eoff
1758
But EoffB = ∆Eoff + Eoff2 , so:1759
∆Eoff +
Eoff
2
=
x + Eon2
Eon
Eoff
=⇒ ∆Eoff =
x + Eon2
Eon
Eoff
−
Eoff
2
1760
Apply this to both lower and upper bounds a and b:1761
∆Eofflow =
a + Eon2
Eon
Eoff
−
Eoff
2
∆Eoffhigh =
b + Eon2
Eon
Eoff
−
Eoff
2
1762
2. Shifting Mbc Cuts1763
The definition of the beam-constrained mass:1764
```
Mbc =
```
s
Ebeam
2
2
− |⃗p B |21765
For off-resonance data, if we want to shift |⃗p B | to match on-resonance conditions, we1766
```
use:1767
```
M shiftedbc =
s
Eon
2
2
−

Eon
Eoff
2
|⃗p offB |21768
140
Suppose we want to apply the on-resonance cut M shiftedbc > Mcut, but on unshifted1769
off-resonance variables.1770
Set M shiftedbc = Mcut and solve for |⃗p offB |2:1771
M shiftedbc =
s
E2on
4
−

Eon
Eoff
2
|⃗p offB |21772
=⇒ M shifted 2bc =
E2on
4
−

Eon
Eoff
2
|⃗p offB |21773
=⇒

Eon
Eoff
2
|⃗p offB |2 =
E2on
4
− M 2cut1774
=⇒ |⃗p offB |2 =
E2off
E2on

E2on
4
− M 2cut

1775
Now, the unshifted off-resonance Mbc is:1776
M offbc =
r
E2off
4
− |⃗p offB |21777
Plug in the value for |⃗p offB |2:1778
M offbc cut =
s
E2off
4
−
E2off
E2on

E2on
4
− M 2cut

1779
=
s
E2off
4
−
E2off
E2on
·
E2on
4
+
E2off
E2on
M 2cut1780
=
s
E2off
4
−
E2off
4
+
E2off
E2on
M 2cut1781
=
s
E2off
E2on
M 2cut1782
=
Eoff
Eon
Mcut1783
Wait! This last step suggests a more direct result. Let’s verify:1784
From above:1785
M offbc cut =
s
E2off
4
−
E2off
E2on

E2on
4
− M 2cut

1786
```
But:1787
```
E2off
4
−
E2off
E2on
E2on
4
=
E2off
4
−
E2off
4
= 01788
```
So:1789
```
M offbc cut =
s
E2off
E2on
M 2cut =
Eoff
Eon
Mcut1790
141
3. Final Off-Resonance Cut Equations1791
For ∆E:
∆Eoff =
∆Eon + Eon2
Eon
Eoff
−
Eoff
2
1792
For Mbc:
M offbc =
Eoff
Eon
M onbc1793
4. Numerical Example1794
Given Eon = 10.58 GeV, Eoff = 10.52 GeV, M onbc = 5.272 GeV, and −0.150 < ∆Eon <1795
0.100 GeV:1796
Eoff
Eon
=
10.52
10.58
≈ 0.99431797
M offbc > 0.9943 × 5.272 ≈ 5.2401798
For ∆E:1799
∆Eofflow =
−0.150 + 5.29
1.0057
− 5.26 =
5.14
1.0057
− 5.26 ≈ 5.110 − 5.26 = −0.1501800
∆Eoffhigh =
0.100 + 5.29
1.0057
− 5.26 =
5.39
1.0057
− 5.26 ≈ 5.358 − 5.26 = 0.0981801
Therefore, the equivalent off-resonance cuts are:1802
M offbc > 5.2401803
1804
−0.150 < ∆Eoff < 0.0981805
142
K FEI calibration postfit plots1806
Post fit distritutions of the FEI calibration1807
0
20
40
60
80
100
events
B0_00post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(a) D−π+
```
0
25
50
75
100
125
150
175
events
B0_01post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(b) D−π+π0
```
0
50
100
150
200
events
B0_03post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(c) D−π+π+π−
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
events
B0_04post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(a) D−π+π+π−π0
```
0
10
20
30
40
50
60
70
80
events
B0_05post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(b) D0π+π−
```
0
20
40
60
80
100
events
B0_15post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(c) D−∗π+
```
143
0
20
40
60
80
100
120
events
B0_16post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(a) D−∗π+π0
```
0
25
50
75
100
125
150
events
B0_18post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(b) D−∗π+π+π−
```
0
20
40
60
80
100
120
140
events
B0_19post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(c) D−∗π+π+π−π0
```
0
5
10
15
20
events
B0_26post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(a) Λ−c pπ+π−
```
0
50
100
150
200
250
300
events
B0_99post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0bin0.5
0.751.0
1.25
data / model
```
(b) Rest
```
0
50
100
150
200
events
Bp_00post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(a) D0π+
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
events
Bp_01post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(b) D0π+π0
```
0
50
100
150
200
250
300
events
Bp_03post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(c) D0π+π+π−
```
144
0
50
100
150
200
events
Bp_04post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(a) D0π+π+π−π0
```
0
20
40
60
80
100
events
Bp_15post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(b) D0∗π+
```
0
20
40
60
80
100
events
Bp_16post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(c) D0∗π+π0
```
0
20
40
60
80
100
events
Bp_18post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(a) D0∗π+π+π−
```
0
10
20
30
40
50
60
70
events
Bp_19post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(b) D0∗π+π+π−π0
```
0
5
10
15
20
events
Bp_23post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(c) D−π+π+
```
0
5
10
15
20
25
events
Bp_24post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(a) D−π+π+π0
```
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
events
Bp_30post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(b) Λ−c pπ+π−π+
```
0
50
100
150
200
events
Bp_99post-fitBtoDstEllNu
BKG
Uncertainty
Data
0.0 0.5 1.0 1.5 2.0 2.5 3.0bin0.5
0.751.0
1.25
data / model
```
(c) Rest
```
145
L Free parameters of the fit1808
In this section we provide a grid plot of all the free and fixed parameters of the fit.1809
The titles of all the subfigures show the reconstruction channel that the parameters are1810
affecting. The y axis ticks show the template that the parameters is affecting. The x axis1811
ticks show the name of the parameters.1812
146
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ` + in NR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) π+ (cos helreco < 0) in SR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) π+ (cos helreco > 0) in SR
```
1813
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco < 0) and 1 < m2miss < 1 GeV2 in SR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco < 0) and 1 < m2miss < 7 GeV2 in SR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco > 0) and 1 < m2miss < 1 GeV2 in SR
```
1814
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco > 0) and 1 < m2miss < 7 GeV2 in SR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) π+ (cos helreco < 0) in 1 extra track
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) π+ (cos helreco > 0) in 1 extra track
```
1815
τ τ helB → D∗ ∗ `ν
`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco < 0) 1 < m2miss < 1 GeV2 in 1.5 < EECL < 2 GeV
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco < 0) 1 < m2miss < 7 GeV2 in 1.5 < EECL < 2 GeV
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco > 0) 1 < m2miss < 1 GeV2 in 1.5 < EECL < 2 GeV
```
none
1816
```
B → D τ (ρ+ ντ) ντ (cos hel < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B0 → D∗ − (D0 π−) ρ+ (cos helreco > 0) 1 < m2miss < 7 GeV2 in 1.5 < EECL < 2 GeV
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) π+ (cos helreco < 0) in 1 extra track
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) π+ (cos helreco > 0) in 1 extra track
```
normfactor
shapefactor
shapesys
lumi
staterror
normsys + histosys
histosys
normsys
none
1817
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco < 0) in 1.5 < EECL < 2 GeV and 1 < m2miss < 1 GeV2
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco < 0) in 1.5 < EECL < 2 GeV and 1 < m2miss < 7 GeV2
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco > 0) in 1.5 < EECL < 2 GeV and 1 < m2miss < 1 GeV2
```
1818
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco > 0) in 1.5 < EECL < 2 GeV and 1 < m2miss < 1 GeV2
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ` + in NR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) π+ (cos helreco < 0) in SR
```
1819
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) π+ (cos helreco > 0) in SR
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco < 0) in SR and 1 < m2miss < 1 GeV2
```
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco < 0) in SR and 1 < m2miss < 7 GeV2
```
1820
```
B → D τ (ρ ντ) ντ (cos hel > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco > 0) in SR and 1 < m2miss < 1 GeV2
```
Pτ
B+
→
¯D∗
0 `
+ν`
```
yieldR(D
```
```
∗)
```
```
R(D
```
```
∗)
```
```
1SM (fixed)fMC+0 (fixed)
```
```
(1 −
```
12 P
```
SMτ )
```
1
```
(fixed)
```
```
B(τ
```
→
π ν
```
) (fixed)
```
```
(1 +
```
12 P
```
SMτ )
```
1
```
(fixed)
```
```
(1 −
```
0.452
PSMτ
```
) 1
```
```
(fixed)
```
```
B(τ
```
→
ρ ν
```
) (fixed)
```
```
(1 +
```
0.452
PSMτ
```
) 1
```
```
(fixed)
```
B →
D∗ ∗
`ν`
yield in
B0
reco
B ¯B
yield in
B0
```
π (
```
cos
hel
reco
```
< 0)
```
B ¯B
yield in
B0
```
π (
```
cos
hel
reco
```
> 0)
```
B ¯B
yield in
B0
```
ρ (
```
cos
hel
reco
```
< 0) and
```
1 <
m2miss
< 1 GeV
2
B ¯B
yield in
B0
```
ρ (
```
cos
hel
reco
```
< 0) and 1 <
```
m2miss
< 7 GeV
2
B ¯B
yield in
B0
```
ρ (
```
cos
hel
reco
```
> 0) and
```
1 <
m2miss
< 1 GeV
2
B ¯B
yield in
B0
```
ρ (
```
cos
hel
reco
```
> 0) and 1 <
```
m2miss
< 7 GeV
2
B ¯B
yield in
B+
```
π (
```
cos
hel
reco
```
< 0)
```
B ¯B
yield in
B+
```
π (
```
cos
hel
reco
```
> 0)
```
B ¯B
yield in
B+
```
ρ (
```
cos
hel
reco
```
< 0) and
```
1 <
m2miss
< 1 GeV
2
B ¯B
yield in
B+
```
ρ (
```
cos
hel
reco
```
< 0) and 1 <
```
m2miss
< 7 GeV
2
B ¯B
yield in
B+
```
ρ (
```
cos
hel
reco
```
> 0) and
```
1 <
m2miss
< 1 GeV
2
B ¯B
yield in
B+
```
ρ (
```
cos
hel
reco
```
> 0) and 1 <
```
m2miss
< 7 GeV
2
B →
D∗ ∗
`ν`
yield in
Bp
reco
B0 → D∗ − ` +ν`
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B0 → D∗ − τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B ¯B
B+ → ¯D∗0 ` +ν`
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(π+ ντ) ντ (cos helgen > 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen < 0)
```
```
B+ → D∗ τ+(ρ+ ντ) ντ (cos helgen > 0)
```
B → D∗ ∗ `ν`
q¯q
```
B+ → ¯D∗0(D0 π0) ρ+ (cos helreco > 0) in SR and 1 < m2miss < 7 GeV2
```
1821Acronyms1822
basf2 Belle II Analysis Software Framework1823
BCS Best Candidate Selection1824
BDT Boosted Decision Tree1825
BF Branching Fraction1826
CDF Cumulative Distribution Function1827
CLT Central Limit Theorem1828
CoM Center-Of-Mass1829
CR Control Region1830
DP Data Production1831
FEI Full Event Interpretation1832
FF Form Factor1833
FS Final State1834
FSP Final State Particle1835
GoF Goodness of Fit1836
HAMMER Helicity Amplitute Module for Matrix Element Reweighting1837
HEP High Energy Physics1838
HFLAV Heavy Flavor Averaging Group1839
HID Hadron IDentification1840
LFU Lepton Flavour Universality1841
LHC Large Hadron Collider1842
LID Lepton IDentification1843
LS1 Long Shudown 11844
MC Monte Carlo1845
NR Normalization enhanced Region1846
PCA Principal Component Analysis1847
PDF Probability Density Function1848
156
PDG Particle Data Group1849
POI Parameter Of Interest1850
ROE Rest of Event1851
SL SemiLeptonic1852
SM Standard Model of Particle Physics1853
SR Signal enhanced Region1854
157
List of Figures1855
1 Feynman diagram of a b → c transition at the quark level. . . . . . . . . . 91856
2 Recent experimental results and theoretical predictions from HFLAV [23] 111857
3 Unique experimental result of the Pτ in B semitauonic decays by Belle.1858
```
The result is presented in contour with the measured value of R(D∗) in the1859
```
same event topology and with the same dataset. [4] . . . . . . . . . . . . . 121860
4 Overview of the FEI hierarchical reconstruction approach. At first step1861
clusters and tracks are used to form finals state particle candidates. These1862
are given as input to subsequent BDTs in order to build composite particle1863
candidates until a valid B-meson candidate is formed. . . . . . . . . . . . 181864
5 Illustration of event reconstruction for signal. . . . . . . . . . . . . . . . . 241865
6 Overview of τ lepton BFs . . . . . . . . . . . . . . . . . . . . . . . . . . . 251866
7 Total number of events that survive after every offline selection for the most1867
important templates in the signal reconstruction channels. . . . . . . . . . 381868
8 Efficiency after every offline selection for the most important templates in1869
the signal reconstruction channels. . . . . . . . . . . . . . . . . . . . . . . 381870
9 Purity after every offline selection for the most important templates in the1871
signal reconstruction channels. . . . . . . . . . . . . . . . . . . . . . . . . 391872
10 Total number of events that survive after every offline selection for the most1873
important templates in the normalization reconstruction channels. . . . . 391874
11 Efficiency after every offline selection for the most important templates in1875
the normalization reconstruction channels. . . . . . . . . . . . . . . . . . . 401876
12 Purity after every offline selection for the most important templates in the1877
normalization reconstruction channels. . . . . . . . . . . . . . . . . . . . . 401878
13 eID efficiency tables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441879
14 µID efficiency tables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451880
15 eID fake rate tables where a kaon is faking an electron. . . . . . . . . . . . 451881
16 eID fake rate tables where a pion is faking an electron. . . . . . . . . . . . 451882
17 µID fake rate tables where a kaon is faking a muon. . . . . . . . . . . . . 451883
18 µID fake rate tables where a pion is faking a muon. . . . . . . . . . . . . 461884
19 kaonID efficiency tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461885
20 kaonID fake rate tables where a pion is faking a kaon . . . . . . . . . . . . 461886
21 πID efficiency tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471887
22 πID fake rate tables where a kaon is faking a pion. . . . . . . . . . . . . . 471888
23 πID fake rate tables where a muon is faking a pion. . . . . . . . . . . . . 481889
24 Change of total MC expectation for B0. The largest differences are ob-1890
served in the low momentum region of the charged hadron or lepton as1891
expected. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511892
25 Change of total MC expectation for B+. The largest differences are ob-1893
served in the low momentum region of the charged hadron or lepton as1894
expected. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 521895
26 Parameters used in the CLN parametrization for the generation of signal1896
decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . . . . . 531897
158
27 Target parameters used in the BLPRX parametrization for the reweighting1898
with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531899
28 Available statistics used for the off-resonance calibration of the continuum. 551900
```
29 Prefit distributions for the FEI calibration in the q2 sideband for B0 (left)1901
```
```
and B± (right). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 561902
```
30 Shape comparison between simulated data and experimental data for the1903
FEI calibration in the q2 sideband. . . . . . . . . . . . . . . . . . . . . . . 571904
31 Normalized shape distribution of m2miss which defines the correctly recon-1905
structed and misreconstructed enhanced regions where the photon multi-1906
```
plicity reweighting i s derived for B0 (left) and B± (right). . . . . . . . . . 601907
```
32 Normalized shape distribution of the ROE photon multiplicity in the high1908
```
∆M(D∗) where the corrections of Table 39 are derived from for B0 (left)1909
```
```
and B± (right) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 611910
```
33 m2miss distribution in the NR. B → D∗ℓν decays peak near zero while all1911
other contributions are spread in the tails of the distribution. . . . . . . . 621912
34 m2miss distribution in the NR using a log scale on the y axis for better1913
visibility of the background distributions. . . . . . . . . . . . . . . . . . . 621914
35 EextraECL distribution in the SR. B → D∗τ ν decays peak near zero. All other1915
background sources peak toward larger values of EextraECL except B → D∗ℓν1916
decays, making it hard to distinguish them from signal processes. . . . . . 631917
```
36 Final fit distributions used for the R(D∗) fit. . . . . . . . . . . . . . . . . 641918
```
```
37 Final fit distributions used for the R(D∗) and Pτ fit. . . . . . . . . . . . . 691919
```
38 Confusion matrix between the true generated cosinus of the helicity angle1920
and the reconstructed one. . . . . . . . . . . . . . . . . . . . . . . . . . . 701921
```
39 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) π+in the1922
```
negative helicity bin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 711923
```
40 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) π+in the1924
```
positive helicity bin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 721925
```
41 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the1926
```
negative helicity bin and low m2miss. . . . . . . . . . . . . . . . . . . . . . . 721927
```
42 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the1928
```
negative helicity bin and high m2miss. . . . . . . . . . . . . . . . . . . . . . 731929
```
43 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the1930
```
positive helicity bin and low m2miss. . . . . . . . . . . . . . . . . . . . . . . 731931
```
44 FEI decay mode composition of B ¯B events in B0 → D∗−(D0 π−) ρ+in the1932
```
positive helicity bin and high m2miss. . . . . . . . . . . . . . . . . . . . . . 741933
```
45 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) π+in the1934
```
negative helicity bin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 741935
```
46 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) π+in the1936
```
positive helicity bin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 751937
```
47 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the1938
```
negative helicity bin and low m2miss. . . . . . . . . . . . . . . . . . . . . . . 751939
```
48 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the1940
```
negative helicity bin and high m2miss. . . . . . . . . . . . . . . . . . . . . . 761941
159
```
49 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the1942
```
positive helicity bin and low m2miss. . . . . . . . . . . . . . . . . . . . . . . 761943
```
50 FEI decay mode composition of B ¯B events in B+ → D∗0(D0 π0) ρ+in the1944
```
positive helicity bin and high m2miss. . . . . . . . . . . . . . . . . . . . . . 771945
```
51 Statistical only correlation matrix of the Pτ and R(D∗) fit. . . . . . . . . 791946
```
```
52 Postfit distributions on Asimov in the SR and control regions for B0 → D∗−(D0 π−) π+ 801947
```
```
53 Postfit distributions on Asimov in the SR and control regions for B0 → D∗−(D0 π−) ρ+ 801948
```
```
54 Postfit distributions on Asimov in the SR and control regions for B+ → D∗0(D0 π0) π+ 811949
```
```
55 Postfit distributions on Asimov in the SR and control regions for B+ → D∗0(D0 π0) ρ+ 811950
```
```
56 Pull plots for toys for R(D∗). Pτ and the yield of B → D∗ℓν decays.1951
```
The MINOS error has been used to calculate the pull of Pτ for every toy.1952
```
A negligeable amount of toys (11/2500) did not converge, therefore we1953
```
excluded them from the pull distribution. The parameters of the gaussian1954
fit are compatible with a standard normal. . . . . . . . . . . . . . . . . . 821955
57 The response of the estimator scales as expected when we bias the Asimov1956
dataset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 831957
58 Linearity test for the three POIs in the simultaneous fit. Pτ scales as1958
expected while the other POIs are minimized to their nominal values. We1959
conclude that the estimator’s response scales as expected. . . . . . . . . . 831960
59 Fitting variables in continuum processes on off-resonance data in SR of1961
```
B0 → D∗−(D0 π−) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 881962
```
60 Fitting variables in continuum processes on off-resonance data in SR of1963
```
B0 → D∗−(D0 π−) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 881964
```
61 Fitting variables in continuum processes on off-resonance data in SR of1965
```
B+ → D∗0(D0 π0) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 881966
```
62 Fitting variables in continuum processes on off-resonance data in SR of1967
```
B+ → D∗0(D0 π0) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 891968
```
63 Fitting variables in continuum processes on off-resonance data in SR of1969
```
B0 → D∗−(D0 π−) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 891970
```
64 Fitting variables in continuum processes on off-resonance data in SR of1971
```
B0 → D∗−(D0 π−) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 891972
```
65 Fitting variables in continuum processes on off-resonance data in SR of1973
```
B+ → D∗0(D0 π0) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 901974
```
66 Fitting variables in continuum processes on off-resonance data in SR of1975
```
B+ → D∗0(D0 π0) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 901976
```
```
67 Post fit distributions of the control fit for B0 → D∗−(D0 π−) π+that are1977
```
constraining BB decays. . . . . . . . . . . . . . . . . . . . . . . . . . . . 901978
```
68 Post fit distributions of the control fit for B0 → D∗−(D0 π−) ρ+that are1979
```
constraining BB decays. . . . . . . . . . . . . . . . . . . . . . . . . . . . 911980
```
69 Post fit distributions of the control fit for B+ → D∗0(D0 π0) π+that are1981
```
constraining BB decays. . . . . . . . . . . . . . . . . . . . . . . . . . . . 921982
```
70 Post fit distributions of the control fit for B+ → D∗0(D0 π0) ρ+that are1983
```
constraining BB decays. . . . . . . . . . . . . . . . . . . . . . . . . . . . 921984
160
```
71 Mbc (top left) and M(D0) (bottom left), lepton momentum (top right)1985
```
```
and πs momentum (bottom right) for the B0 → D∗−(D0 π−) e+in the q21986
```
sideband. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 931987
```
72 Mbc (top left) and M(D0) (bottom left), lepton momentum (top right)1988
```
```
and πs momentum (bottom right) for the B+ → D∗0(D0 π0) e+in the q21989
```
sideband. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 931990
```
73 m2miss distribution for B0 (left) and B± (right) mesons in the q2 sideband . 941991
```
```
74 EextraECL distribution for B0 (left) and B± (right) mesons in the NR sideband 941992
```
```
75 EextraECL distribution for B0 (left) and B± (right) mesons in the NR sideband1993
```
after applying the photon multiplicity correction. . . . . . . . . . . . . . . 951994
```
76 Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and1995
```
```
πs momentum (bottom right) for the B0 → D∗−(D0 π−) ℓ+in the NR. . . . 951996
```
```
77 Mbc (top left) and M(D0) (bottom left), lepton momentum (top right) and1997
```
```
πs momentum (bottom right) for the B+ → D∗0(D0 π0) ℓ+in NR. . . . . . 961998
```
78 Data/MC aggreement of the fitting variables in the control fit region for1999
```
B0 → D∗−(D0 π−) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 962000
```
79 Data/MC aggreement of the fitting variables in the control fit region for2001
```
B0 → D∗−(D0 π−) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 962002
```
80 Data/MC aggreement of the fitting variables in the control fit region for2003
```
B+ → D∗0(D0 π0) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 972004
```
81 Data/MC aggreement of the fitting variables in the control fit region for2005
```
B+ → D∗0(D0 π0) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 972006
```
82 Data/MC aggreement of the fitting variables in the validation region for2007
```
B0 → D∗−(D0 π−) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 982008
```
83 Data/MC aggreement of the fitting variables in the validation region for2009
```
B0 → D∗−(D0 π−) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 982010
```
84 Data/MC aggreement of the fitting variables in the validation region for2011
```
B+ → D∗0(D0 π0) π+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 982012
```
85 Data/MC aggreement of the fitting variables in the validation region for2013
```
B+ → D∗0(D0 π0) ρ+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 992014
```
86 Module overview of the SysVar software . . . . . . . . . . . . . . . . . . . 1022015
87 Pseudovariables for signal extraction . . . . . . . . . . . . . . . . . . . . . 1032016
88 Pseudovariable for correction bins . . . . . . . . . . . . . . . . . . . . . . . 1032017
89 Different corrections and error sources. In this example three sources of2018
uncertainty are considered for the correction. Two statistical in nature2019
and one systematic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042020
90 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042021
91 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042022
92 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1052023
93 A summary of the variations of the correction weights. . . . . . . . . . . . 1052024
94 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1062025
95 The correlation matrix arising from all the varied templates. It is clear2026
that the correlation structure in this space becomes highly not trivial to2027
model. Therefore the eigendecomposition of it, provides a framework that2028
simplifies the treatment of these correlations in a easier way . . . . . . . . 1072029
161
96 The normalized covariance matrix differences as a function of the eigendi-2030
rections considered. The target precision at 0.5% is set arbitrarily by the2031
user. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1082032
97 Multinomial error scaling with number of total occurances and rates . . . 1102033
98 Signal shape, post fit distribution and goodness of fit for D0 → K−π+ ,2034
D0 → π−π+ and D0 → K−K+ on MC. . . . . . . . . . . . . . . . . . . . 1112035
99 Signal shape, post fit distribution and goodness of fit for D0 → K0S π0 and2036
D0 → K−π+π0 on MC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1112037
100 Signal shape, post fit distribution and goodness of fit for D0 → K0S π+π−2038
and D0 → K0S K+K− on MC. . . . . . . . . . . . . . . . . . . . . . . . . . 1122039
101 Signal shape, post fit distribution and goodness of fit for D0 → K−π+π−π+2040
on MC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1122041
102 Signal shape, post fit distribution and goodness of fit for D0 → K−π+ ,2042
D0 → π−π+ and D0 → K−K+ on Data. . . . . . . . . . . . . . . . . . . 1122043
103 Signal shape, post fit distribution and goodness of fit for D0 → K0S π0 and2044
D0 → K−π+π0 on Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1122045
104 Signal shape, post fit distribution and goodness of fit for D0 → K0S π+π−2046
and D0 → K0S K+K− on Data. . . . . . . . . . . . . . . . . . . . . . . . . 1132047
105 Signal shape, post fit distribution and goodness of fit for D0 → K−π+π−π+2048
on Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1132049
106 Parameters used in the CLN parameterization for the generation of B →2050
Dτ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . . 1142051
107 Target parameters used in the BLPRXP parameterization for the reweight-2052
ing of B → Dτ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . 1142053
108 Parameters used in the CLN parameterization for the generation of B →2054
D∗τ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . . 1152055
109 Target parameters used in the BLPRXP parameterization for the reweight-2056
ing of B → D∗τ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . 1152057
110 Parameters used in the BGL parameterization for the generation of B →2058
Dℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . . 1152059
111 Target parameters used in the BLPRXP parameterization for the reweight-2060
ing of B → Dℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . 1162061
112 Parameters used in the BGL parameterization for the generation of B →2062
D∗ℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . . 1162063
113 Target parameters used in the BLPRXP parameterization for the reweight-2064
ing of B → D∗ℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . 1172065
114 Parameters used in the BLR parameterization for the generation of B →2066
D∗∗1 ℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1172067
115 Target parameters used in the BLR parameterization for the reweighting2068
of B → D∗∗1 ℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1172069
116 Parameters used in the BLR parameterization for the generation of B →2070
D∗∗1 τ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1182071
117 Target parameters used in the BLR parameterization for the reweighting2072
of B → D∗∗1 τ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1182073
162
118 Parameters used in the BLR parameterization for the generation of B →2074
D∗∗0 ℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1182075
119 Target parameters used in the BLR parameterization for the reweighting2076
of B → D∗∗0 ℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1192077
120 Parameters used in the BLR parameterization for the generation of B →2078
D∗∗0 τ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1192079
121 Target parameters used in the BLR parameterization for the reweighting2080
of B → D∗∗0 τ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1192081
122 Parameters used in the BLR parameterization for the generation of B →2082
D∗∗1′ ℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1202083
123 Target parameters used in the BLR parameterization for the reweighting2084
of B → D∗∗1′ ℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1202085
124 Parameters used in the BLR parameterization for the generation of B →2086
D∗∗1′ τ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1202087
125 Target parameters used in the BLR parameterization for the reweighting2088
of B → D∗∗1′ τ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1212089
126 Parameters used in the BLR parameterization for the generation of B →2090
D∗∗2 ℓν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1212091
127 Target parameters used in the BLR parameterization for the reweighting2092
of B → D∗∗2 ℓν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1212093
128 Parameters used in the BLR parameterization for the generation of B →2094
D∗∗2 τ ν decays in the Belle II MC . . . . . . . . . . . . . . . . . . . . . . . 1222095
129 Target parameters used in the BLR parameterization for the reweighting2096
of B → D∗∗2 τ ν with HAMMER . . . . . . . . . . . . . . . . . . . . . . . . 1222097
130 Bias test for FEI calibration estimation. We throw 5000 toys of toy datasets2098
and refit the nominal model to them. All free parameters in the fit are not2099
biased and the uncertanties well estimated based on the mean and standard2100
deviation of the standard normal fit of the pull distribution. . . . . . . . . 1232101
131 Linearity test for FEI calibration estimation. We bias an asimov dataset by2102
artificially injecting B → D∗ℓν decays from the nominal histograms Then2103
we fit this biased asimov dataset to the nominal model. The extracted2104
FEI calibration factors scale as expected while the background strengths2105
remains unnafected. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1242106
132 Stability test for FEI calibration. We extract the FEI calibraation factors2107
considering different multiplicities by deriving the factors for different D02108
decays modes. We also derive them again for electrons and muons sepa-2109
rately. All are consistent within 2σ. . . . . . . . . . . . . . . . . . . . . . 1242110
```
133 Pull plots for toys B → D∗∗ℓν yields for B0 and (left) and B+ (right)2111
```
```
reconstrution channels for the R(D∗) fit. The parameters of the gaussian2112
```
fit are compatible with a standard normal. . . . . . . . . . . . . . . . . . 1252113
134 Pull plots for toys BB yields for B0 in the τ → πντ and τ → ρντ reconstruc-2114
tion channels and B+ in the τ → πντ and τ → ρντ reconstruction channels2115
```
from left to right for the R(D∗) fit. The parameters of the gaussian fit are2116
```
compatible with a standard normal. . . . . . . . . . . . . . . . . . . . . . 1252117
163
135 Pull plots for toys q ¯q yields for B0 in the τ → πντ and τ → ρντ reconstruc-2118
tion channels and B+ in the τ → πντ and τ → ρντ reconstruction channels2119
```
from left to right for the R(D∗) fit. The parameters of the gaussian fit are2120
```
compatible with a standard normal. . . . . . . . . . . . . . . . . . . . . . 1262121
```
136 Pull plots for toys B → D∗∗ℓν yields for B0 and (left) and B+ (right)2122
```
reconstrution channels for the Pτ fit. The parameters of the gaussian fit2123
are compatible with a standard normal. . . . . . . . . . . . . . . . . . . . 1262124
137 Pull plots for toys BB yields for B0 in the τ → πντ and τ → ρντ recon-2125
struction channels and B+ in the τ → πντ and τ → ρντ reconstruction2126
channels from left to right for the Pτ fit. The parameters of the gaussian2127
fit are compatible with a standard normal. . . . . . . . . . . . . . . . . . 1262128
138 Pull plots for toys q ¯q yields for B0 in the τ → πντ and τ → ρντ recon-2129
struction channels and B+ in the τ → πντ and τ → ρντ reconstruction2130
channels from left to right for the Pτ fit. The parameters of the gaussian2131
fit are compatible with a standard normal. . . . . . . . . . . . . . . . . . 1272132
139 Channel dependant optimization of the helicity angle window . . . . . . . 1282133
140 Impact of every D0 mode on the sensitivity of the parameters of interest.2134
The uncertainties are taken from an Asimov fit. We confirm that we observe2135
```
closure in the fit (the central values are minimized to the expected ones) . 1292136
```
141 Impact of every D0 mode on the sensitivity of the parameters of interest.2137
We completely exclude the D0 → K−K+ mode from this test. The uncer-2138
tainties are taken from an Asimov fit. We confirm that we observe closure2139
```
in the fit (the central values are minimized to the expected ones) . . . . . 1292140
```
142 Impact of every D0 mode on the sensitivity of the parameters of interest.2141
We completely exclude the D0 → K−K+ and D0 → π−π+ modes from2142
this test. The uncertainties are taken from an Asimov fit. We confirm2143
```
that we observe closure in the fit (the central values are minimized to the2144
```
```
expected ones) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1302145
```
```
143 Background composition in the B0 → D∗−(D0 π−) π+channel for the Prompt2146
```
Hadronic component in the negative helicity bin. . . . . . . . . . . . . . . 1312147
```
144 Background composition in the B0 → D∗−(D0 π−) π+channel for the Prompt2148
```
Hadronic component in the positive helicity bin. . . . . . . . . . . . . . . 1322149
```
145 Background composition in the B0 → D∗−(D0 π−) π+channel for the Dou-2150
```
ble Charm component in the negative helicity bin. . . . . . . . . . . . . . 1322151
```
146 Background composition in the B0 → D∗−(D0 π−) π+channel for the Dou-2152
```
ble Charm component in the positive helicity bin. . . . . . . . . . . . . . 1332153
```
147 Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Prompt2154
```
Hadronic component in the negative helicity bin. . . . . . . . . . . . . . . 1332155
```
148 Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Prompt2156
```
Hadronic component in the positive helicity bin. . . . . . . . . . . . . . . 1342157
```
149 Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Dou-2158
```
ble Charm component in the negative helicity bin. . . . . . . . . . . . . . 1342159
```
150 Background composition in the B0 → D∗−(D0 π−) ρ+channel for the Dou-2160
```
ble Charm component in the positive helicity bin. . . . . . . . . . . . . . 1352161
164
```
151 Background composition in the B+ → D∗0(D0 π0) π+channel for the Prompt2162
```
Hadronic component in the negative helicity bin. . . . . . . . . . . . . . . 1352163
```
152 Background composition in the B+ → D∗0(D0 π0) π+channel for the Prompt2164
```
Hadronic component in the positive helicity bin. . . . . . . . . . . . . . . 1362165
```
153 Background composition in the B+ → D∗0(D0 π0) π+channel for the Dou-2166
```
ble Charm component in the negative helicity bin. . . . . . . . . . . . . . 1362167
```
154 Background composition in the B+ → D∗0(D0 π0) π+channel for the Dou-2168
```
ble Charm component in the positive helicity bin. . . . . . . . . . . . . . 1372169
```
155 Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Prompt2170
```
Hadronic component in the negative helicity bin. . . . . . . . . . . . . . . 1372171
```
156 Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Prompt2172
```
Hadronic component in the positive helicity bin. . . . . . . . . . . . . . . 1382173
```
157 Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Dou-2174
```
ble Charm component in the negative helicity bin. . . . . . . . . . . . . . 1382175
```
158 Background composition in the B+ → D∗0(D0 π0) ρ+channel for the Dou-2176
```
ble Charm component in the positive helicity bin. . . . . . . . . . . . . . 1392177
167 HID recommendations from charged hadrons as per the conference readi-2178
ness page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1712179
168 minC2TDist on the photons of the ROE in all three detector. Most of the2180
hadronic split-offs are discarded without any Data/MC disagreement being2181
introduced. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1732182
```
169 PDG codes of the daughters of the τ lepton in B0 → D∗τ (→ ρν)ν and2183
```
```
B+ → D∗τ (→ ρν)ν events . . . . . . . . . . . . . . . . . . . . . . . . . . . 1732184
```
170 Demonstration of proportions of fake and true leptons in the retained sam-2185
```
ples of B → D∗(D0 π) ℓ+. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1742186
```
171 Demonstration of proportions of fake and true leptons in the retained sam-2187
```
ples of B → D∗(D0 π) ℓ+. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1752188
```
172 Difference between the unconstrained factors in the control fits without and2189
with the background reweighting. . . . . . . . . . . . . . . . . . . . . . . . 1762190
173 Correlation matrix for unconstrained parameters of the fit if the control2191
regions have not been added. . . . . . . . . . . . . . . . . . . . . . . . . . 1782192
174 Impact of nCDCHits cut on fitting variable . . . . . . . . . . . . . . . . . 1812193
175 Data/MC comparison of the flight of distance of K0S in the low q2 sideband2194
```
in the B0 → D∗−(D0 π−) ℓ+channels (left) and B+ → D∗0(D0 π0) ℓ+channels2195
```
```
(right). The p-values indicate that the modelling of this observable is ac-2196
```
ceptable with our current statistical precision. . . . . . . . . . . . . . . . . 1812197
176 Invariant mass of the ρ meson . . . . . . . . . . . . . . . . . . . . . . . . . 1822198
177 Generated and reconstructed mass of the ρ+ meson in signal MC. . . . . . 1822199
178 ρ+ invariant mass cut at the Belle analysis. . . . . . . . . . . . . . . . . . 1822200
179 FOM for the ρ mass window. The best window is shown with a red square. 1832201
180 Invariant mass of the ρ meson with the optimized cut . . . . . . . . . . . 1832202
181 Invariant mass of D meson for different modes. . . . . . . . . . . . . . . . 1842203
182 Impact of every D0 mode on the sensitivity of the parameters of interest.2204
The uncertainties are taken from an Asimov fit. We confirm that we observe2205
```
closure in the fit (the central values are minimized to the expected ones) . 1842206
```
165
183 Impact of every D0 mode on the sensitivity of the parameters of interest.2207
We completely exclude the D0 → K−K+ mode from this test. The uncer-2208
tainties are taken from an Asimov fit. We confirm that we observe closure2209
```
in the fit (the central values are minimized to the expected ones) . . . . . 1852210
```
184 Impact of every D0 mode on the sensitivity of the parameters of interest.2211
We completely exclude the D0 → K−K+ and D0 → π−π+ modes from2212
this test. The uncertainties are taken from an Asimov fit. We confirm2213
```
that we observe closure in the fit (the central values are minimized to the2214
```
```
expected ones) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1852215
```
185 Cluster energy distributions of photons in the ROE in the three detector2216
regions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1862217
186 Reconstructed invariant mass of slow π0. A clear shift from the theoretical2218
value can be seen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1872219
187 Original finer binning in m2miss to extract the B → D∗ℓν yield. . . . . . . . 1902220
188 Updated coarse binning in m2miss to extract the B → D∗ℓν yield. . . . . . 1902221
189 Events that would be discarded by a tighter momentum cut at 0.7 GeV.2222
The impact on the signal template is larger than the normalization template2223
in our fitting variable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1912224
190 Pre and post fit impact of gap mode BF uncertainties in [30] . . . . . . . 1952225
191 Results by runnning toys with nuisance parameters on. . . . . . . . . . . . 1972226
192 Overview of different crossfeed modes of semitauonic B meson decays. . . 1982227
166
List of Tables2228
```
1 Overview of experimental measurements of R(D∗) [23] . . . . . . . . . . . 112229
```
2 List of pyhf modifier used in this analysis. All the above modifier are2230
controlled by a single nuisance parameter. The subscripts stand for: s2231
for sample, c for channel, b for bin. f and g are functions determined by2232
interpolating the nominal template between + 1 and −1 sigma. a is an2233
auxiliary measurement and delta is the relative uncertainty of a template2234
in a particular bin with respect to the total uncertainty. . . . . . . . . . . . 152235
3 Pre-selection cuts of the FEI skim. . . . . . . . . . . . . . . . . . . . . . . 192236
4 Luminosity for different samples in the Generic MC for MC15rd . . . . . . 192237
5 Event types and corresponding decays with number of events and luminos-2238
ity for gap modes including light leptons. Nleptons has been set 2 in Eq 5 to2239
account for the fact that the light lepton gap modes are not produced sep-2240
arately. The calculated luminosity is used to scale the events that survive2241
the full set of event selections to the luminosity of experimental data. . . . 202242
```
6 Latest values of BFs for the light lepton B → Hcℓν decays and R(Hc) ratios.2243
```
```
The BF of the semitauonic modes is calculated using R(Hc) = B→Hcτ νB→Hcℓν . . . 212244
```
7 Event types and corresponding decays with number of events and luminos-2245
ity for gap semitauonic modes. The calculated luminosity is used to scale2246
the events that survive the full set of event selections to the luminosity of2247
experimental data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222248
8 Experiment Offline Luminosity for 4S . . . . . . . . . . . . . . . . . . . . . 222249
9 Experiment Offline Luminosity for 4S offres . . . . . . . . . . . . . . . . . 232250
10 Global tags used in the steering file. The names of the global tags are used2251
as input to the basf2 helper function b2.conditions.prepend globaltag 252252
11 Selections for tracks and cluster considered in the BtagROE . . . . . . . . . . 262253
12 LID selection criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272254
13 Charmed meson reconstruction modes . . . . . . . . . . . . . . . . . . . . 292255
14 Overview of online cuts for building B meson signal candidates . . . . . . 302256
```
15 Selections for tracks and cluster considered in the ROE against the Υ (4S)2257
```
candidate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302258
```
16 Υ (4S) reconstructions modes and decays of interest . . . . . . . . . . . . . 312259
```
17 Main decay truth matching categories. For D∗ both charged and neutral2260
mesons are considered. For D∗ and D, τ , ell, ν, charge conjugation is taken2261
into account. The definitions of the PDG codes that are used for D∗∗, Hc,2262
Hgapc , Xgapu/s , Xs, and Xu are given in Appendix B. . . . . . . . . . . . . . . 332263
18 τ decay truth matching categories. The order of the truth matched daugh-2264
ters is not important as all possible permutation are considered. . . . . . . 342265
19 Final truth matching categories. The entries of the column Bsig mcID are2266
described in Table 17. The entries of the column τ mcID are described in2267
Table 18. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352268
20 List of final tight cuts applied in the sample. . . . . . . . . . . . . . . . . 372269
21 BCS, number of candidates and event efficiencies for the signal reconstruc-2270
tion channels. Results are not scaled to data luminosity. . . . . . . . . . . 412271
167
22 BCS, number of candidates and event efficiencies the normalization recon-2272
struction channels. Results are not scaled to data luminosity. . . . . . . . 422273
23 Luminosity and scaling factors for different samples simulated data. The2274
assumed L for experimental data for the LS1 dataset is 365.29 ± 1.70 fb−1 432275
24 Correction tables for π±s efficiency corrections derived by the Tracking2276
group. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442277
25 Correction tables for π0s efficiency corrections derived by the Neutrals group. 442278
26 BF corrections for charmed meson decays . . . . . . . . . . . . . . . . . . . 492279
27 BF corrections for τ lepton decays . . . . . . . . . . . . . . . . . . . . . . . 492280
28 BF corrections for double charm decays . . . . . . . . . . . . . . . . . . . . 502281
29 BF corrections for prompt hadronic decays . . . . . . . . . . . . . . . . . . 502282
30 Percentage increase in MC expectation for different templates in the B02283
reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512284
31 Percentage increase in MC expectation for different templates in the B+2285
reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 522286
32 FF models and parameters used for the HAMMER reweighting . . . . . . 522287
33 Smearing factors determined for every different D0 decay mode reconstruc-2288
tion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 542289
34 Continuum calibration factors as derived by off-resonace data. . . . . . . . 552290
35 Signal strengths for B → D∗ℓν which are interpeted as the FEI calibration2291
factors fit on an Asimov dataset in the B0 channels. The first uncertainty2292
is statistical while the second is the total systematic uncertainty. . . . . . 582293
36 Signal strengths for B → D∗ℓν which are interpeted as the FEI calibration2294
factors fit on an Asimov dataset in the B+ channels. The first uncertainty2295
is statistical while the second is the total systematic uncertainty. . . . . . 582296
37 Signal strengths for B → D∗ℓν and all other background processes in the2297
FEI calibration fit on experimental data in the B0 channels. The first un-2298
certainty is statistical while the second is the total systematic uncertainty.2299
We get a GoF p-value of 10.19%. . . . . . . . . . . . . . . . . . . . . . . . 592300
38 Signal strengths for B → D∗ℓν and all other background processes in the2301
FEI calibration fit on experimental data in the B+ channels. The first un-2302
certainty is statistical while the second is the total systematic uncertainty.2303
We get a GoF p-value of 10.19%. . . . . . . . . . . . . . . . . . . . . . . . 592304
39 Photon multiplicity weights for B0 and B+ for correctly and misrecon-2305
structed events. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 602306
40 Final templates for the fit . . . . . . . . . . . . . . . . . . . . . . . . . . . 642307
```
41 Final templates for the R(D∗) and Pτ fit . . . . . . . . . . . . . . . . . . . 702308
```
42 Overview of fit regions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 772309
43 Asimov fit uncertainties of all free unconstrained parameters for the si-2310
```
multaneous R(D∗) and Pτ fit. The uncertainties are presented in terms of2311
```
percentages in case the free parameter’s nominal value is not 1. The nomi-2312
nal values of all parameters is presented in parenthesis in the first column.2313
We confirm that we observe full closure in all our Asimov fits, i.e. all free2314
parameters are minimized to their nominal values. . . . . . . . . . . . . . 782315
44 Summary of Systematic Uncertainties . . . . . . . . . . . . . . . . . . . . . 862316
168
45 Sideband checks summary . . . . . . . . . . . . . . . . . . . . . . . . . . . 872317
46 Results for control fits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 912318
47 PDG codes of categories for the first layer of truth matching. Charge2319
conjugation is used for all PDG codes. . . . . . . . . . . . . . . . . . . . . 1092320
169
Working group review questions and answers2321
• Comments received on 27-05-2025 by WG reader Michele Mantovano2322
1. The FEI training with the MC15rd is already available (https: // docs. belle2.2323
```
org/ pub_ data/ documents/ 25/ ), so why are you still using the one for the2324
```
MC15ri?2325
I believe that the document that you sent refers to the MC15rd calibration of2326
the FEI. Even if the inference and the calibration of the efficiency on MC hap-2327
pens on the rd sample, to the best of my knowledge the training weights that2328
are used, still rely on the training on 200 fb−1 of MC15ri. Please let me know2329
if this is wrong. Nonetheless I removed the table with the MC15ri luminosities2330
to avoid confusion. The original plan to cross check the analysis by default on2331
MC15ri was too optimistic and will now pursue this only if requested. Let me2332
stress out that the official FEI calibration is not used throughout this analysis.2333
The argument in Section 3.2.1 was only meant to explain why we do not use2334
```
the full amount of generic MC15ri available ( potentially for RC readers outside2335
```
```
of the S(L) WG were not familiar with the ins and outs of the FEI).2336
```
2. Could you clarify that you’re setting Nlepton=2 in the calculation of the gap2337
modes with light leptons?2338
Yes we do. I explicitly now mention this in the caption of Table 5.2339
3. Tab.6: Could you clarify why you set f=0.5 in the luminosity calculation for2340
Dpipi and D*pipi?2341
In the MC cocktail that is recommended to use, the non resonant gap modes2342
are replaced by the same final state, through a resonant D∗∗ decay. In some2343
cases two different resonances are chosen to model the same final state. To2344
the best of my knowledge this is just a matter of choice and a by-product of2345
our ignorance on how the gap should be filled. If we examine the example of2346
B0 for the Dππ final state we see that two decay modes are being used, mode2347
1196700001 and mode 1196700003. In the first one the Dππ final state goes2348
through a D∗1 resonance and in the second through a D∗0 . Therefore half of2349
the Dππ events will be found in a D∗1 and the other half in D∗0 events, even2350
though they are meant to replace the same non-resonant final states. In order2351
to account for that we set the factor f to 0.5 for such cases. The full list of the2352
available modes can be found in this xwiki page.2353
4. Tab.6: The calculated luminosity values seem too large to me, especially for the2354
resonant Dππ modes — could you double-check them? I think the values for2355
```
the NBB are wrong; they should be 5.4e5 and 5.1e5.2356
```
You are right! Thank you! I changed the values for the number of B ¯B events.2357
Now Tables 5 and 23 should have the correct values for the luminosities and2358
the scaling factors.2359
5. Can you explain why the nominal values and uncertainties in Tab.7 of the gap2360
modes are different from those reported in Tab.6?2361
Apologies. There was an update in the values and I forgot to also update Table2362
6. Now both tables have the correct values.2363
170
6. Tab. 7, for the D*0 are you using only the measurement from Belle?2364
We’re using as input the latest values that Markus Prim has advertised in the2365
working group. I cannot give you definite answer on what measurements made2366
it into the HFLAV average calculation but by looking at table 37 of HFLAV2367
report [3] and comparing them to the values of Table 6 in this document, I2368
believe that both the Belle and BABAR measurements must have been used by2369
the HFLAV group. Please also see Question 32.2370
7. I think you should also include ’chargedpidmva rel6 v5’ as a global tag since2371
you’re using the BDT electron ID.2372
You’re absolutely right! I included this global tag in the last processing but2373
forgot to update Table 10. Now Table 10 is updated with all the global tags.2374
In the current and previous version of the note for all results the chargedpid-2375
mva rel6 v5 globaltag has been prepended. This oversight has affected only2376
Table 10.2377
8. Are you sure that the cuts —dr— < 2 cm and —dz— < 4 cm are the ones2378
recommended by the LID group?2379
I cannot find any official recommendation on the selections on dr and dz from2380
the LID group on their xwiki page. However I did find that the stdCharged2381
```
module (which is used for the reconstruction of leptons in this analysis as2382
```
mentioned in Section 4.5.2 is applying ipCuts as ipCut = ’dr < 0.5 and2383
```
abs(dz) < 2’ (link to documentation). These are tighter than the ones we2384
```
apply on all tracks, therefore our manually applied cuts on all all charged2385
```
tracks (including the leptons) should actually have zero impact as they are2386
```
covered by the cuts applied by the stdCharged module.2387
9. Are you sure that the cut on CDChits > 20 is still necessary to calculate the2388
hadron ID corrections? I remember that with the SF you can compute the cor-2389
rections even without this cut. Is it still recommended to use this cut?2390
Please see below in Figure 167 the latest recommendations from HID group2391
taken from Conference readiness page on xwiki It is recommended to use the
Figure 167: HID recommendations from charged hadrons as per the conference readiness
page.
2392
nCDCHits > 20 cut on charged hadrons. This cut has also been applied when2393
determining corrections with the systematics framework. As far as I know2394
from attending the HID meetings in the past this cut is used to ensure that the2395
charged tracks have reached the TOP detector which ensures good kaon/pion2396
separation. If a track has less than 20 hits in the CDC then it’s a very slow one2397
171
which will never reach the TOP detector. This means that the PID likelihood2398
will rely mainly on information from CDC which does not provide great dis-2399
crimination power between kaons and pions. We believe that this cuts should2400
```
remain as high HID performance is very important in this analysis (especially2401
```
```
for the pion coming from the τ lepton in the B → D∗(D0 π) h+reconstruction2402
```
channels.2403
FOLLOW-UP2404
Please see my follow up in Question 362405
10. For the Ks selection, you only require the flight distance and the significance of2406
the distance to be positive. Aren’t there any recommended cuts for the Ks? I2407
remember that a cut of significance of distance larger than 10 was imposed for2408
the Ks.2409
To the best of my knowledge there are no official recommendations for the2410
selections applied to K0S . I couldn’t find any official recommendations in the2411
conference readiness or the tracking group page on xwiki. Furthermore I do not2412
see any cuts applied on the flight distance or the significance of distance from2413
```
the stdKshorts module in basf2 (which is the one that is used in this analysis.2414
```
The only selection seems to be conf level = 0.0, imposed by treeFit.2415
11. Can you justify why you’re using minC2TDist > 50 cm? I remember that this2416
cut is no longer among the recommended ones.2417
I believe you’re referring to the cut on the photons of the ROE. As far as I know2418
there are not official recommendations on what cuts to apply on the objects that2419
make it into the ROE. The minC2TDist variable is one of the well-model ones as2420
```
per the recommendations of the Neutrals group (see https://indico.belle2.2421
```
org/event/13722/contributions/84645/attachments/31512/46646/2024_2422
```
11_17_ferber_ecl.pdf). During the work-shopping of the analysis I have2423
```
```
tried using at least eight different ROE masks (and their counterparts by ap-2424
```
```
plying the photon killing procedure) that have been used in other analyses2425
```
from WG1 and WG2 or have been recommended to me privately in the past.2426
Through these studies I have found that this mask is the one with the best2427
Data/MC agreement. Furthermore I have made extensive Data/MC agreement2428
studies on different observables for tracks and clusters that are used to build2429
```
the ROE (these are however not included in this note to avoid making this2430
```
```
document unnecessarily even longer). Regarding the cut in question I provide2431
```
Figure 168 that shows that a cut at 50 cm on the minC2TDist on the photons2432
of the ROE in all three detector regions discards most of the hadronic split-offs2433
```
without any Data/MC disagreement being introduced (the overall number of2434
```
photons on MC has been normalized to the one on data. Therefore these plots2435
```
are evaluating the modeling of the shape of minC2TDist)2436
```
12. Could you explain more clearly why the truth-matching doesn’t works for tau2437
→ rho nu? Are you running TauolaBelle for the truth-matching?2438
I looked closer into the DECAY.dec file and apparently the decay τ → ρντ is2439
commented out in favor of2440
0.255100000 pi- pi0 nu tau TAUHADNU -0.108 0.775 0.149 1.364 0.4002441
172
Figure 168: minC2TDist on the photons of the ROE in all three detector. Most of the
hadronic split-offs are discarded without any Data/MC disagreement being introduced.
```
0.001124109 nu tau gamma pi- pi0 PYTHIA 21;2442
```
I just checked again and apparently the misorderings of the radiative photons2443
are not there anymore. I had developed this truth matching code still on2444
MC14 when the problem was way more prominent. Perhaps some things have2445
changed since then, so I think that the algorithm is still robust against any2446
weird orderings just in case. For completion I paste below in Figure 169 the2447
```
PDG codes of the τ daughters of the truth matched B0 → D∗τ (→ ρν)ν and2448
```
```
B+ → D∗τ (→ ρν)ν events. I have added a respective comment in Section2449
```
5.1.4 in line 622. Regarding the TaulaBelle tool, as far as I understand this2450
is a tool meant to be used in τ -pair analyses and not supposed to be used to2451
truth match τ decays in B ¯B events. Please correct me if I’m wrong.2452
```
Figure 169: PDG codes of the daughters of the τ lepton in B0 → D∗τ (→ ρν)ν and
```
```
B+ → D∗τ (→ ρν)ν events
```
13. In Table 20, could you clarify why you are defining a signal region (SR) that2453
```
also includes the normalization region (NR) in Mmiss2 ? Isn’t the SR defined2454
```
```
for Mmiss2 > 2 GeV? Also because, in Fig. 38, I don’t see any signal (blue2455
```
```
components) in the NR region.2456
```
```
The NR is defined only for the B → D∗(D0 π) ℓ+reconstruction channels, while2457
```
```
the SR is defined only for the B → D∗(D0 π) h+reconstruction channels. If we2458
```
```
include the m2miss > 2 GeV 2 for channels B → D∗(D0 π) ℓ+we are effectively re-2459
```
peating the Hadronic FEI-leptonic tau measurement which we want to avoid as2460
```
this would complicate the setup significantly. For channels B → D∗(D0 π) h+we2461
```
173
```
still observe some events in the low m2miss region (better visible in Figure 362462
```
and this is why we do not discard this region. However since these are different2463
```
reconstruction channels (lepton vs hadron) there’s no overlap between them.2464
```
Any potential small overlap is already taken care of from the BCS. I updated2465
Table 20 so that it is clear for which reconstruction channels every m2miss cut is2466
referring to.2467
14. Why do you choose the pi slow candidate with the highest momentum when2468
there are multiple candidates?2469
This is what the Belle analysis did and we replicated their strategy on that one.2470
This criterion is relevant only for the charged slow pions which anyways do not2471
yield a lot of duplicates. In Table 21 you can see that choosing the slow pion2472
with the highest momentum changes the candidate multiplicity from 1.737 to2473
```
1.724 (only 55 duplicate candidates were discarded) therefore the effect of this2474
```
is expected to be minimal. If you have strong arguments against doing that2475
we can switch to a random selection of the charged slow pion.2476
15. Tab. 23 most likely has the same error in the calculated luminosity.2477
Answered above at 4.2478
16. Can you clarify how you apply the photon efficiency to the photons in the ROE?2479
Do you need to save all the photons in the ROE to apply the weight?2480
I doubled checked and we have the photon efficiency weights in the tuples for all2481
```
γ (daughters of π0 and photons in the ROE) but we consider none of them into2482
```
the final MC weight. I’m sorry for the oversight! I removed the misinformation2483
part from 5.5.5. It would be challenging to apply the photon efficiency weight2484
```
from the photons of the ROE to the Υ (4S) tuples, but we can look into it if2485
```
you think that this is necessary.2486
17. For the efficiency tables for lepton ID, the recommendation should be to use v12487
```
tables (/group/belle2/users2022/unok/leptonid/combination/perf/PID/methods/moriond 202488
```
instead of v0.2489
Thanks for the heads up! The LID xwiki page recommends to use v0 coarse.2490
When I check on kekcc v0 coarse is just a symbolic link to v1. So I am indeed2491
using v1, event if this was not very transparent... This is all shown in Fig-2492
ure 170. I updated the versioning information of section 5.5.8 with the above2493
details.
Figure 170: Demonstration of proportions of fake and true leptons in the retained samples
```
of B → D∗(D0 π) ℓ+.
```
2494
18. For the fake rate corrections (e.g., Figs. 15-18), how did you choose the bin-2495
```
ning? There are some bins with large uncertainties on the correction; have you2496
```
174
tried optimizing the binning?2497
The initial choice of the binning has been aligned with the one that is used for2498
the official efficiency correction tables. Of course this is the reason that the2499
uncertainties are much larger for the fake rate corrections as the control sam-2500
ples there are limited. We could consider optimizing this binning however as2501
you can see in Figure 171 the amount of fake leptons is very small in this anal-2502
ysis. Moreover since for signal decays we use the hadronic reconstruction, this2503
```
correction is affecting R(D∗) only partially through the yield of B → D∗ℓν de-2504
```
```
cays in the denominator (not relevant for the nominator where we reconstruct2505
```
```
a charged hadron). However the uncertainty of this yield is expected to be2506
```
already very small as you can see in Table 43 with our Asimov results. This2507
is also reflected in the systematic budget in Table ?? where the Lepton fakes2508
```
systematic impact on R(D∗) is already negligible, even with these statistically2509
```
inflated uncertainties for the fake rate corrections. We believe that changing2510
the binning of the fake rate corrections will not have any impact on the final2511
result of this analysis but let us know if you think differently.2512
Figure 171: Demonstration of proportions of fake and true leptons in the retained samples
```
of B → D∗(D0 π) ℓ+.
```
19. Are you sure that the BR(tau to 3pi) in the DECFILE is wrong by a factor of2513
```
10 (Tab.27)?2514
```
Sorry this is a typo. I confirmed that the values used in the code are the correct2515
ones. This typo affects only the documentation. I corrected Table 27.2516
20. In Fig. 29 (and 44, 46, 50, 58,etc.) there actually seems to be a difference in2517
shapes.2518
Yes you’re right, some of the Figures indeed demonstrate small differences in2519
the shape of some variables. Actually since the beginning of the WG review we2520
had some internal discussions about the adequacy of our background reweight-2521
ing. We have good reasons to believe that it’s not necessary in the end to2522
reweight the backgrounds the way we do. To test this hypothesis we ran the2523
control fits as described in Section 8.2 once with and once without including2524
the background reweighting. In Figure 172 we show the difference between all2525
the unconstrained factors of the control fit with and without the background2526
reweighing. Since in the two versions of the fit we fit the same data we expect2527
175
the two versions of the factors we extract to be highly correlated. We do not2528
expect the correlation to be exactly 1 since the weights are different and some2529
of them differ quite a lot from one and have sizeable uncertainties. Since we do2530
not know exact correlation between the two versions of the scaling factors we2531
decide to use a 95% correlation between them when we subtract them. Almost2532
all of the differences are consistent with zero within the uncertainties. There’s2533
one that demonstrates a ≃ 2σ diference and one of them a ≃ 1.3σ tensions2534
which we consider acceptable. We therefore conclude that since the impact2535
of the background reweighing on the central values that we derive is minimal,2536
it’s better if we completely drop it from the analysis. The main advantages2537
of such decision is that the analysis becomes much simpler and we get rid of2538
sizable extra systematics that we have already assigned as could be seen in2539
Table 46 of v3 of this note. We modify the text in Section 6.3 and we exclude2540
the description of the background reweighting from the documentation. We2541
also modify the systematic budget in Section ??.2542
0.4 0.2 0.0 0.2 0.4
```
Unlinked BB in B+ D*0(D0 0) + (cos hel > 0)
```
```
Unlinked BB in B+ D*0(D0 0) + (cos hel < 0)
```
```
Unlinked BB in B0 D* (D0 ) + (cos hel > 0)
```
```
Unlinked BB in B0 D* (D0 ) + (cos hel < 0)
```
```
Unlinked BB in B0 D* (D0 ) + (cos hel > 0)
```
```
Unlinked BB in B0 D* (D0 ) + (cos hel < 0)
```
```
qq in B+ D*0(D0 0) + (cos hel > 0)
```
```
BB in B+ D*0(D0 0) + (cos hel > 0)
```
```
qq in B+ D*0(D0 0) + (cos hel < 0)
```
```
BB in B+ D*0(D0 0) + (cos hel < 0)
```
```
qq in B0 D* (D0 ) + (cos hel > 0)
```
```
BB in B0 D* (D0 ) + (cos hel > 0)
```
```
qq in B0 D* (D0 ) + (cos hel < 0)
```
```
BB in B0 D* (D0 ) + (cos hel < 0)
```
```
qq in B0 D* (D0 ) + (cos hel > 0)
```
```
BB in B0 D* (D0 ) + (cos hel > 0)
```
```
qq in B0 D* (D0 ) + (cos hel < 0)
```
```
BB in B0 D* (D0 ) + (cos hel < 0)
```
```
qq in B+ D*0(D0 0) + (cos hel > 0) and m2miss > 1 GeV2
```
```
BB in B+ D*0(D0 0) + (cos hel > 0) and m2miss > 1 GeV2
```
```
qq in B+ D*0(D0 0) + (cos hel > 0) and m2miss < 1 GeV2
```
```
BB in B+ D*0(D0 0) + (cos hel > 0) and m2miss < 1 GeV2
```
```
qq in B+ D*0(D0 0) + (cos hel < 0) and m2miss > 1 GeV2
```
```
BB in B+ D*0(D0 0) + (cos hel < 0) and m2miss > 1 GeV2
```
```
qq in B+ D*0(D0 0) + (cos hel < 0) and m2miss < 1 GeV2
```
```
BB in B+ D*0(D0 0) + (cos hel < 0) and m2miss < 1 GeV2
```
w/o BKG rw w/i BKG rw
Figure 172: Difference between the unconstrained factors in the control fits without and
with the background reweighting.
2543
21. Fig. 42: Could you explain why for B0 → Dpi you use ’one extra charged2544
track’ as the sideband to constrain the BBbar, while for B0 → Drho you use2545
the region 1.5 < ECL < 2? Couldn’t you use the same regions for both?2546
One of the main effects that we’re trying to correct with our control regions2547
is the FEI efficiency of these background events. The criterion that we have2548
176
defined to ensure that the FEI performance between the SR and the control2549
regions is the similarity between the FEI decay mode distributions in the two2550
regions. Figures ?? shows that the FEI decay mode distributions in the one2551
extra charged track sideband is compatible with the one in the SR for the2552
τ → πντ channel. This is not the case for the τ → ρντ channel. As can2553
be seen in Figure ?? the 95% confidence interval that we set for the fraction2554
of the residuals that are within -1 and 1 does not cover the 68.3% for the2555
comparison between the SR and the one extra charged track sideband. There-2556
fore we conclude that the residuals are not normally distributed and therefore2557
the two orthogonal regions are not compatible. This is not the case for the2558
1.5 < EextraECL < 2 sideband where based on the statistical power of our test2559
we cannot exclude the possibility that the residuals are normally distributed.2560
Therefore we choose the high EextraECL sideband to constrain B ¯B decays in the2561
```
B0 → D∗τ (→ ρν)ν channel.2562
```
22. Line 1594: You say to normalize everything to the ssbar component, but in2563
Fig. 44 you say you normalize everything to the ccbar component. Could you2564
clarify this point?2565
```
Sorry for this typo! The title of plot contains the correct information (normal-2566
```
```
ized to ssbar) not the captions. I updated all the captions.2567
```
23. Fig. 76: Why do you observe a high correlation for some yields off the diagonal2568
as well?2569
The observed strong anti-correlation in the correlation matrix is coming from2570
the B ¯B and q ¯q templates. These have very similar shapes in the the observables2571
```
used for the extraction of R(D∗) and Pτ . This can be even better seen in Figure2572
```
173 which presents the correlation matrix of the unconstrained parameters in2573
```
a fit where the control regions have not been included (only the SR is being2574
```
```
fitted). We observe a strong anti-correlation between the B ¯B and the q ¯q yields2575
```
< −96%. Including the control regions helps in reducing the anti-correlation2576
```
between these yields (at least 20% decrease). Ideally if our control fits were2577
```
perfect this anti-correlation would completely vanish, but since all our control2578
regions are contaminated with both B ¯B and q ¯q decays, this is the best we can2579
do right now. The impact of including the control regions in the fit in terms2580
of the uncertainties of the parameters of interest can be seen in Table 43.2581
24. * Fig. 77: You have a bias in the mean of pT of about 3 sigma. Do you take2582
this into account as an additional systematic uncertainty?2583
Thank you for this question! In Figure 77 from v3 of the note, the HESSE error2584
has been used to calculate the pull distribution. Since Pτ due to it’s definition2585
```
(we measure it as an asymmetry) can have also asymmetric errors, especially2586
```
when throwing toys, we decided to use the MINOS error for the pulls of Pτ .2587
We now updated Figure 56 with the MINOS uncertainty. When the nominator2588
of the pull is larger than zero, we use the lower MINOS uncertainty. When the2589
nominator of the pull is smaller than zero we use the upper MINOS uncertainty.2590
With this modification one can see that the bias in the fit vanishes, therefore2591
no extra systematic uncertainty is required.2592
177
Figure 173: Correlation matrix for unconstrained parameters of the fit if the control
regions have not been added.
178
• Comments received on 01-06-2025 by WG reader Taichiro Koga2593
25. line 528 FEM -¿ FEI ?2594
Corrected the typo. Thanks!2595
26. -Figure1 Could you add c in the diagram ?2596
Thank you! I updated the diagram in Figure 1.2597
27. -Table1 Could you add Belle II semileptonic result ? You should add a caption2598
```
at the top of Table (not only this table but also all tables)2599
```
I updated Table 1 with our 2025 SL tagged result. Thank you for remarking2600
upon the proper position of the caption of the tables. I updated all tables in2601
the document and now the caption is on the top.2602
28. -Section3.1 I think the explanation is too detailed and part of them can be2603
moved to Appendix. Thank you for your suggestion regarding Section 3.1. I2604
intentionally chose to provide a more detailed overview of the software tools2605
early in the document as part of my narrative style. I believe this level of2606
detail will be particularly valuable for newcomers or future researchers who2607
may wish to repeat the measurements or build upon this work. From personal2608
experience, I’ve learned that clear documentation of tools and their purposes2609
can save considerable time and confusion—especially in the early stages of an2610
analysis. With these five pages, I’ve tried to be the kind of culture change I2611
hope to see in future documentation. That said, if you believe it’s truly essential2612
to reduce the length of this section, I’m open to condensing it and moving the2613
more technical parts to the Appendix, while keeping the core narrative intact.2614
29. -line 820 3 → Table 32615
Corrected.2616
30. -Table 4 Is this MCri ? Could you write so ?2617
This Table is now removed as part of Michele’s questions. For more please2618
refer to Question 1.2619
31. -Table 6,7 D(star)etaellnu branching ratio is different between Table 6 and2620
Table 7. Which is correct ?2621
You’re absolutely right. Apologies for the oversight. Michele had the same2622
question. This is now corrected, please refer to Question 5.2623
32. -Table 7 Branching ratio of D∗0 is different from https: // indico. belle2.2624
org/ event/ 14125/ contributions/ 89012/ attachments/ 32814/ 48431/ followup_2625
180225. pdf Could you confirm with Michele ?2626
Yes you’re right. I got the latest values by Markus for the reweighting, but2627
forgot to update Table 6. Now the Table is updated2628
33. -line 519, 889, Table 23 integrated luminosity is different in each other. Which2629
value is correct ?2630
Actually none of them. Sorry for the oversight. Now I aligned all the LS1 lu-2631
minosity references across the document using a custom command. The official2632
```
luminosity of the LS1 dataset on the Υ (4S) resonance as per the luminosity2633
```
page of the Data Production group should be 365.29 ± 1.70 fb−1.2634
179
34. -line 933 Does “three neutral clusters” include clusters from charged particles2635
? If so, could you modify the text ? If it is not, the selection looks too tight.2636
Apologies for the confusion. With the text in Section 4.3 I was aiming to refer2637
again to the pre-cuts that the FEI skim is applying to the events. I do not ex-2638
plicitly apply these event cuts as they would be redundant, since the FEI skim2639
```
is already applying them (see fei precuts method in https://software.2640
```
belle2.org/light-2503-ceres/sphinx/_modules/skim/WGs/fei.html#BaseFEISkim.2641
The only event cuts that I apply using the applyEventCuts module are the2642
ones mentioned in Line 460, and refer to discarding events were no FEI can-2643
didates were found. I modified the text in Section 4.3 by just referring back2644
to Table 3 to avoid the confusion of the reader thinking that I explicitly apply2645
these cuts in my steering file.2646
35. -line 977, table 13 Could you apply a lepton momentum cut ? At least p>0.2 is2647
needed, because p<0.2 is not available in Figure 13. If you prefer conservative2648
```
way, p>0.7GeV is needed for muon PID by reaching KLM. (at p<0.7GeV,2649
```
```
muon and pion can not be identified and both are included.)2650
```
Thank you for this comment! I can apply a pre-cut online at 0.2 on the leptons2651
as per your suggestion. However later offline we apply a cut at 0.5 GeV for e,2652
µ and π+ and ρ+ coming from the τ decay. This is documented in Table 20.2653
36. -line 984 If you require nCDCHit>20, signal efficiency will reduce significantly.2654
Could you optimize the number of CDCHits threshold ?2655
2656
Michele had the same question. Please see my answer to Question 9. Nonethe-2657
less optimizing this cut would require reprocessing online which would take2658
some extra time, so I will follow up in the next iteration.2659
FOLLOW-UP2660
I removed the nCDCHits online and in Figure 174 I’m showing the distribution2661
of events in the fitting variable that would be added in the analysis if we indeed2662
dropped the nCDCHits cut from all our hadrons. It is clear that only a handful2663
of signal events can be found in this range of nCDCHits. On the contrary we2664
see a lot of B → D∗ℓν events being included, confiriming hypothesis as de-2665
scripe in Question 9 that not requiring nCDCHits > 20 deteriorates hadronID2666
```
performance (these B → D∗ℓν event are events where we tried to reconstruct2667
```
```
a pion but actually picked up a lepton). Based on this plot we consider that2668
```
the removal of this cut will worsen our result, therefore we decide to keep it as2669
is i.e. apply nCDCHits > 20 to all pions and kaons that we reconstruct.2670
37. -line 1000 I think Ks efficiency correction needs to be done in each analysis, as2671
a function of flight distance. Could you show me data/MC comparison of the2672
flight distance ?2673
```
Due to a very naive bug (a simple typo) in our reconstruction code this variable2674
```
is not saved. We have to reprocess the tuples to give you this information. I2675
will follow up on that at a next iteration.2676
FOLLOW-UP2677
2678
180
Figure 174: Impact of nCDCHits cut on fitting variable
Please see in Figure 175 the Data/MC agreement for the flight of distance of2679
reconstructed K0S candidates in the low q2 sideband. All Data/MC weights and2680
the FEI calibration has been applied. The p-values indicate that the modelling2681
of this observable is acceptable with our current statistical precision, therefore2682
we argue that no efficiency corrections is required for this analysis.2683
0
20
40
60
80
Events / Bin
```
B0 D* (D0 ) +2 / 8 = 0.48 (0.87)q2 < 4 GeV2
```
Belle II Preliminary
0
20
40
60
80
Events / Bin
```
B+ D*0(D0 0) +2 / 8 = 0.88 (0.53)q2 < 4 GeV2
```
```
dt = 365 fb 1
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
uu/dd/ss/ccMC stat. unc.
Data
0 5 10 15 20 25 30 35 40dflight
KS in cm
-5-3-1
135
NData
NMC
2NData +
2NMC
0 5 10 15 20 25 30 35 40dflight
KS in cm
-5-3-1
135
NData
NMC
2NData +
2NMC
Figure 175: Data/MC comparison of the flight of distance of K0S in the low q2 sideband
```
in the B0 → D∗−(D0 π−) ℓ+channels (left) and B+ → D∗0(D0 π0) ℓ+channels (right). The
```
p-values indicate that the modelling of this observable is acceptable with our current
statistical precision.
38. -line 1009 Could you add an invariant mass distribution of rho ? How do you2684
optimize the 0.66 and 0.96 GeV ?2685
We adopted this cut from the Belle analysis. As can be seen in Figure 1762686
the window is indeed a bit narrow as it cuts off the tail of true ρ+ mesons2687
```
(especially on the lower end). Unfortunately this cut is applied online.2688
```
We generated some signal MC to study the properties of the ρ+ invariant mass.2689
This can be seen in Figure 177. The tails of the distribution of the generated2690
mass range from ≃ 0.35 to ≃ 1.4 GeV. Of course we cannot broaden the cut2691
by that much as this would significantly increase the background levels.2692
I couldn’t find reason that the Belle analysis chose exactly this cut, but I found2693
the distributions of true and fake ρ+, shown in Figure 178, from where it is clear2694
that the backgrounds steeply increase in the lower end of the distribution. I2695
181
Figure 176: Invariant mass of the ρ meson
0.4 0.6 0.8 1.0 1.2 1.4mass in GeV0
1
2
3
4
```
Probability density (1/GeV)
```
GeneratedReconstructed
Current window
Figure 177: Generated and reconstructed mass of the ρ+ meson in signal MC.
could broaden the online cut at a future processing if required and study offline2696
the effect of this tighter mass window in terms of sensitivity and Data/MC2697
impact. Please let me know about your thoughts on this.2698
Figure 178: ρ+ invariant mass cut at the Belle analysis.
FOLLOW-UP2699
We broaden the online cut of the reconstructed ρ invariant mass to [0.560, 1.060].2700
We tried broadening it even more however the combinatorics exploded due to2701
reconstruction of a ρ meson along side with a D∗ meson. The steering file was2702
taking way too long to go through and we were reaching 10,000 candidates per2703
```
event very often (when basf2 stops combining more candidates). We found2704
```
this range to be the best compromise between broadening the online cut and2705
keeping our online reconstruction feasible. We then optimized the mass win-2706
dow offline by maximizing the figure of merit S√S+B . Our results are shown in2707
182
Figure 179. We find that the best mass window is [0.590, 1.050] GeV, inside2708
the online mass window that we chose. We report that the FOM improves2709
from 5.28 to 6.19 when we switch from the old [0.660, 0.960] GeV window to2710
the optimized [0.590, 1.050] GeV. We will be using this cut for the rest of the2711
analysis. For completion we also provide the rho mass distribution with the2712
optimized cut in Figure 180.2713
Figure 179: FOM for the ρ mass window. The best window is shown with a red square.
Figure 180: Invariant mass of the ρ meson with the optimized cut
39. -Table 14 Could you add Kspipipi0 ? BF is about 5%. Is there any reason to2714
exclude it ?2715
We had including this mode initially in the analysis due to this BF argu-2716
ment. However our studies in the past have shown that this mode has very2717
```
low S/sqrt(S+B). This can be see in Figure 181 where we show the recon-2718
```
```
structed invariant mass of D0 in a broad window (without any offline cuts2719
```
```
applied). D0 → K0S π+π−π0 demonstrates a very low figure of merit com-2720
```
pared to the other modes as can be seen in the bottom right plot. We believe2721
that we cannot use this mode contrary to other semileptonic analyses due to2722
the fact that we reconstruct a fully hadronic final state with missing energy2723
for the signal, therefore it becomes very challenging to properly reconstruct2724
high multiplicity final states with many neutrals. In the worst case in the2725
```
B+ → D∗0(D0 π0) ρ+reconstruction we would reconstruct four neutral parti-2726
```
```
cles on the signal side (slow π0, π0 from ρ+, K0S and π0 from D0) which really2727
```
smears out the resolution and significantly increases the combinatorics. We2728
183
believe that is best if we do not include this mode. Please let us know if you2729
think differently.2730
Figure 181: Invariant mass of D meson for different modes.
40. -Table 14 BF of D→KK and D→pipi are opposite ?2731
You’re right, sorry for the typo. Corrected.2732
41. -Table 14 Could you show me that the figure of merit (or Asimov fit sensitivity)2733
is improved by adding each channel, after applying final tight selection ? I2734
```
worry some of the channels are dirty (or low signal statistics) and not useful2735
```
to improve the analysis sensitivity.2736
In order to evaluate each D0 mode’s sensitivity in the analysis I run the Asimov2737
fit once including all the D0 decay modes and once by excluding one mode at2738
a time. The results can be seen in Figure 182.
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+
no D0 → K+K−
no D0 → π+π−no D
0 → K0s π0no D
0 → K−π+π0no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60 70
P uncertainty in %
no D0 → K−π+
no D0 → K+K−
no D0 → π+π−no D
0 → K0s π0no D
0 → K−π+π0no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 182: Impact of every D0 mode on the sensitivity of the parameters of interest.
The uncertainties are taken from an Asimov fit. We confirm that we observe closure in
```
the fit (the central values are minimized to the expected ones)
```
2739
It is very clear that the D0 → K−K+ mode has the worst sensitivity and it2740
worsens our sensitivity in both parameters of interest. We completely exclude2741
this mode and the repeat the test. The results are presented in Figure 183.2742
184
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+
no D0 → π+π−
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60
P uncertainty in %
no D0 → K−π+
no D0 → π+π−
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 183: Impact of every D0 mode on the sensitivity of the parameters of interest. We
completely exclude the D0 → K−K+ mode from this test. The uncertainties are taken
```
from an Asimov fit. We confirm that we observe closure in the fit (the central values are
```
```
minimized to the expected ones)
```
We observe that the D0 → π−π+ mode still deteriorates the performance of2743
our fit. We completely exclude this mode and then repeat the test. The results2744
are presented in Figure 184.2745
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5
```
R(D*) uncertainty in %
```
no D0 → K−π+
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
0 10 20 30 40 50 60
P uncertainty in %
no D0 → K−π+
no D0 → K0s π0
no D0 → K−π+π0
no D0 → K0s π+π−
no D0 → K0s K+K−
no D0 → K−π+π+π−
```
stat error (all modes)stat error
```
Figure 184: Impact of every D0 mode on the sensitivity of the parameters of interest.
We completely exclude the D0 → K−K+ and D0 → π−π+ modes from this test. The
uncertainties are taken from an Asimov fit. We confirm that we observe closure in the fit
```
(the central values are minimized to the expected ones)
```
Since no particular mode is making the performance worse, we decide to move2746
on with the remaining six D0 modes. D0 → K−K+ and D0 → π−π+ will be2747
excluded from the analysis from now on.2748
I added Appendix I with this information and updated Section 4.6.42749
42. -Table 15 How do you optimize the energy threshold of ECL clusters ?2750
This is somehow linked to Question 11 by Michele. During the development2751
of the analysis we have tried several well motivated masks that have been2752
used also in other analyses at Belle II and this is the only one that give good2753
Data/MC agreement in the EextraECL distribution. Furthermore in Figure 185 I2754
provide a Data/MC check on the cluster energies of the photons in the ROE.2755
The dashed line shows the chosen cut. The MC has been normalized to data, so2756
here we’re comparing the shapes. Since our cuts are more or less on the switch2757
of the sign of the disagreement we are not introducing any extra normalization2758
185
or shape disagreement. This is also justified by our last checks on EextraECL 75,2759
Please let us know if you think we should further optimize this.
Figure 185: Cluster energy distributions of photons in the ROE in the three detector
regions.
2760
43. -Table 15 Did you try to improve ROE photon selection by using fakePhoton-2761
Suppression and beambackgroundPhotonSuppression ? If not, could you check2762
?2763
The Neutrals group has made public the list of ECL variables that are recom-2764
```
mended for use. (see https://indico.belle2.org/event/13722/contributions/2765
```
```
84645/attachments/31512/46646/2024_11_17_ferber_ecl.pdf). The clusterZernikeMV2766
```
has been used for the training which belongs to the non-recommended ones.2767
Nevertheless the Neutrals group recommends to Use the EextraECL distribution to2768
check for the data-MC agreement https://xwiki.desy.de/xwiki/bin/view/2769
BI/Belle%20II%20Internal/Physics%20Performance%20Webhome/Neutrals%2770
20Performance/. We can say that all masks that we have tried and included2771
the MVAs did not demonstrate good Data/MC agreement, therefore we have2772
decided to not use them.2773
44. -Table 20 Could you improve the format of the table ? It is difficult to see. (I2774
```
can not understand which left column corresponds to which right column.)2775
```
Apologies, I added horizontal lines between each cut, I hope it is more visible2776
now. Let me know if not.2777
45. -line1218, 1220 Reconstructed mass peak of pi0 can be different from the theo-2778
retical one, due to the response of ECL. Could you show me the reconstructed2779
pi0 mass distribution ?2780
You are right! I provide in Figure 186 the reconstructed mass of the slow2781
```
π0 in B+ → D∗0(D0 π0) ℓ+channel in the low q2 sideband after applying the2782
```
FEI calibration factor. This is a reconstruction that is affected by the BCS2783
as described in 5.4. Luckily the shift is common for MC and Data. The two2784
means are compatible with zero within the uncertainty. Since there’s no bias2785
introduced and we still keep all signal candidates as can be seen in Table 21 we2786
believe it’s okay to keep the BCS as it is. Please let us know if you disagree.2787
46. -line 1223 I think it is better to use purity than the BF in general. From figure2788
9, it looks like the purity of the pi channel is better than the rho channel. How2789
about prioritizing the pi channel rather than the rho channel ?2790
186
0
50
100
150
200
250
Events / Bin
```
B+ D*0(D0 0) +
```
```
2 / 10 = 0.54 (0.87)
```
q2 < 4 GeV2
MC Weighted mean: 0.13273 ± 0.00007
Data mean: 0.13249 ± 0.00017 MC - Data: 0.0002+/-0.0002
Belle II Preliminary
0.120 0.125 0.130 0.135 0.140 0.145
slowM in GeV
-5-3
-11
35
NData

NMC
2NData
+
2NMC
Figure 186: Reconstructed invariant mass of slow π0. A clear shift from the theoretical
value can be seen.
Thank you for this question! I tried both approaches and I found that with our2791
```
current strategy (prioritizing BF) the Asimov result fits are R(D∗) = 0.258 ±2792
```
0.0335 and Pτ = −0.4970 ± 0.2076. When we prioritize the τ → πντ mode2793
```
(prioritizing purity) the results are R(D∗) = 0.258±0.0363 and Pτ = −0.4970±2794
```
0.3045, worse than before, especially for Pτ . The main reason seems to be that2795
a lot of the duplicates are also found in the BB template. That means that2796
when we prioritize the τ → πντ channel we’re contaminating it with more2797
background events which messes up its relatively high purity observed with2798
the current strategy. Based on these results we decide to not change this step2799
of your BCS, but keep it as described in 5.4.2800
47. -line 1233 In the end if we find multiple candidates having been reconstructed2801
in two types of reconstruction channels e.g. signal and normalization, then we2802
keep one candidate at random. How frequently such a case happens ?2803
```
This happens in 314 out of 231,123 total events on MC (all reconstruction2804
```
```
channels and all sideband together) which represents a 0.136% ± 0.008% of2805
```
```
the total events. On Data this happens in 27 out of 38,310 total events (all2806
```
```
reconstruction channels and all sideband together) which represents 0.071% ±2807
```
0.014% of the total events. The errors on these ratios have been calculated2808
using the binomial approximation. Even if this happens at a different fre-2809
quency on Data and MC, we believe that choosing a random candidate does2810
not introduce any bias in our sample.2811
48. -line 1413 we also set a 95% Confidence Interval (CI) for the fraction of resid-2812
uals that are ±1 sigma for every comparison. Sorry, what do you mean ? The2813
187
1sigma does not equal 95% CI.2814
We are calculating the residuals for the fraction of events that are reconstructed2815
in every FEI decay mode. These residuals are expected to be normally dis-2816
tributed around 0 if the compositions of the different templates are compatible2817
with each other. In other words we expect 68.3% of the residuals to be within2818
[-1, 1] the composition of the modes that are reconstructed by the FEI is com-2819
patible across the templates. To test this we are calculating the 95% CI of2820
```
the fraction of the total number of the residuals (e.g. in Figure ?? we have 152821
```
```
residuals coming from 15 FEI decay modes), that are within ± 1 σ. If 68.3% is2822
```
covered by the CI then we argue that we have no statistical evidence that the2823
residuals are not normally distributed, since if we had 100 replicas of our MC2824
and we repeated the test 100 times, in 95 of them we would find the fraction2825
of residuals which are between ± 1 σ within the 95% CI which contains the2826
68.3%. I hope this clarifies our method. Please let me know if it is still unclear.2827
However this might be irrelevant once I follow up to Question 53.2828
49. -line 1414 If 68.3% is covered by the CI then we conclude that with the current2829
dataset we have no statistical evidence that the tag-side decay mode distribution2830
is different between the three modes of interest. Sorry, I can not understand2831
this statement. For example, in D*pipipipi0 mode, the fraction of green line2832
```
(B-¿D*taunu in SR) is significantly ( 3sigma) smaller than the others. So, we2833
```
have statistical evidence of the difference locally.2834
Yes you’re right, in Figure ?? there is one residual that is demonstrating a2835
slightly larger tension than 3σ. However we believe that only one mode is not2836
enough to make us argue that the FEI composition overall is not compatible2837
between two templates in two different regions. That is the reason that we2838
have developed the test that I tried to clarify further in my answer to Question2839
48. If we wanted to take into acount local differences and outliers we would2840
then need to come up with a reweighting strategy, which could be possible, but2841
needs to be discussed. In general I believe that quantifying such a test about2842
the FEI composition is an ill defined problem as many modes have very low2843
counts and the aggregation of several modes into the ”Rest” category, heavily2844
depends on the number of events that have reconstructed e.g. for the signal2845
template in SR we have in general way less events than in the normalization2846
templates in NR and the q2 sideband. So even if the test can be defined for2847
more modes for the normalization template, there’s certain modes that need2848
to be exluded when testing for the signal template, due to the lower expected2849
yield. However this might be irrelevant once I follow up to Question 53.2850
50. -Figure 29-32 Could you add error bars to the histograms ?2851
See Question 532852
51. -Figure30 Is the p-value calculated correctly ? For example, in the left figure,2853
four points are deviated more than 3sigma but p-value is high. I think there is2854
something wrong.2855
See Question 532856
52. -Figure 32 In the left plot, The pull distribution has a clear tendency (at low2857
188
Btag deltaE value, the blue line is smaller than the red line. at high value, the2858
```
blue line is larger. ). In this kind of case, even if the p-value is large, we should2859
```
```
conclude that there is a significant shape difference. (because the chi2 and p-2860
```
```
value do not take into account the sign of each bin.) Similar things happen to2861
```
```
Figure 30(left).2862
```
See Question 532863
53. -line1467, table 35 I think you are estimating the FEI efficiency correction2864
factor by integrating all Btag decay mode. However, the correction factor is2865
significantly different in each Btag decay mode. Is there any reason to esti-2866
mate the correction with integrated mode ? In order to check possible impact to2867
analysis, could you compare the PDF shape of fit variables in each Btag decay2868
mode ? If there is no difference, you do not need to estimate the correction2869
factor in each Btag decay mode. If there is a difference, you need to estimate2870
```
the correction factor in each Btag decay mode. (or assign systematic error.)2871
```
The reason for not deriving one calculation factor per FEI decay mode is of2872
course the complexity of the fit and the much lower statistics that would in-2873
crease the uncertainy of the per mode, calibration factors. Nonetheless since we2874
have all the technical tools available we will pursue a mode-by-mode calibration2875
and follow up on this in the next iteration of the note.2876
54. -line 1471 I think it is not enough to check B → D∗ℓν channel only for photon2877
multiplicity reweighting, because one of main reason of the data/MC inconsis-2878
tency is fake photon from hadronic particles. Depending on the final state of2879
the decay, the correction can be different. Because you are using tau hadronic2880
decay, you must check other sideband in the π and ρ channels.2881
I totally agree with you! Figures ?? - ?? and ??-?? present the EextraECL distribu-2882
tion among other observables and for all of those plots the photon multiplicity2883
reweighing has been applied on top of the weights derived from the control2884
regions to constrain the backgrounds. In Section 8.6 I had already mention2885
that in Line 1553. I updated the text in both Sections 8.5 and 8.6 to make it2886
more clear.2887
55. -Table 36 Could you show me the data/MC comparison plot of the photon2888
multiplicity ?2889
I added Figure 32 in Section 5.12.2890
189
• Comments received on 03-06-2025 by WG reader Taichiro Koga2891
56. -Figure40 Even in higher missing mass region, there are still B → D∗ℓν events2892
in τ → πντ sample. I think this is coming from the higher tail of Mmiss2 as2893
below plot. How do you validate the shape of the tail is correctly modeled by2894
```
MC ?(For example, in our analysis, we measured the resolution of Mmiss2 on2895
```
```
data and MC then applied correction.)2896
```
As shown in the main text we initially used a fine binning in the normalization2897
enhanced region to extract the B → D∗ℓν yield. The binning used so far can2898
be see in Figure 187.2899
0
1000
2000
3000
4000
Events / Bin
```
B0 D* (D0 ) +NR
```
Belle II Preliminary
0
1000
2000
3000
4000
5000
6000
Events / Bin
```
B+ D*0(D0 0) +NR
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
-1.0 -0.6 -0.2 0.2 0.6 1.0 1.4 1.7 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
-1.0 -0.6 -0.2 0.2 0.6 1.0 1.4 1.7 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
Figure 187: Original finer binning in m2miss to extract the B → D∗ℓν yield.
In order to avoid further complicating the analysis we tried to bin this region2900
much more coarsely as can be seen in Figure 188. Such a binning is not2901
sensitive to the missmodelling of the peak of the tail of the m2miss. In order to2902
evaluate what is the impact on our extracted parameters we ran the Asimov2903
fit using both binning scenarios. We found that the coarser binning worsens2904
```
the sensitivity by < 0.0002 for Pτ (nominal value -0.497), < 0.0001 for R(D∗)2905
```
```
(nominal value 0.258) and < 0.0004 for the strength of B → D∗ℓν decays2906
```
```
(nominal value 1.0). Therefore we conclude we were not gaining much by this2907
```
finer binning which was causing the mismodelling concerns in your question.2908
We decide to keep this coarse binning for the rest of the analysis.2909
0
1000
2000
3000
4000
5000
6000
Events / Bin
```
B0 D* (D0 ) +NR
```
Belle II Preliminary
0
2000
4000
6000
8000
Events / Bin
```
B+ D*0(D0 0) +NR
```
```
dt = 365 fb 1
```
```
B D* ( )B D* ( )
```
B D*B D* *
B Hc + n huB HcHc/Xs
Other BBmissID
Combinatorialuu/dd/ss/cc
MC stat. unc.Asimov Data
-1.0 0.25 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
-1.0 0.2 1.1 2.0m2miss in GeV2-5-3
-113
5
NData
NMC
2NData +
2NMC
Figure 188: Updated coarse binning in m2miss to extract the B → D∗ℓν yield.
57. -Figure40 Even in higher missing mass region, there are still B → D∗ℓν events2910
in τ → πντ sample. If you increase muon momentum threshold up to 0.7GeV,2911
190
how much the contaminated B → D∗ℓν is reduced ?2912
Thank you for this question. I believe your wanted to write pion momentum as2913
in the τ → πντ channel we’re not reconstructing a muon but a pion. I provide2914
Figure 189 where I show the reconstucted events in the range [0.5, 0.7] GeV2915
for three categories, signal, normalization and other background in the fitting2916
variable. If we discarded these events by tightening the pion momentum cut2917
we would be losing way more events from the signal template rather than from2918
the misreconstructed normalization events. We therefore think that such a cut2919
would worsen the sensitivity of our measurement, due to the large number of2920
discarded signal events. We do not worry that these B → D∗ℓν events would2921
```
impact our R(D∗) measurement by a lot as their yield is linked to the correctly2922
```
```
reconstructed B → D∗ℓν events from B → D∗(D0 π) ℓ+whose uncertainty is2923
```
very small. Therefore these misreconstructed events will be scaled properly by2924
the NR.2925
Figure 189: Events that would be discarded by a tighter momentum cut at 0.7 GeV. The
impact on the signal template is larger than the normalization template in our fitting
variable.
58. -Figure42 Could you prepare another table to list the name and definition of2926
```
selection criteria of all sideband ? (Figure42 is not enough to explain it, and2927
```
```
Table 42 is too late to appear)2928
```
Perhaps you missed Table 42? I added a dedicated reference in the text.2929
59. -line1575 What is the definition of Region01 and Region022930
The definition of all the control regions is given in Table 42.2931
60. -Figure 45 τ → πντ channel → τ → ρντ channel ?2932
You’re right! Sorry for that. These figures have been removed as part of2933
Michele’s Question 20.2934
61. -Figure 45, 47 Could you unify the name (label in the figure) of each sideband2935
?2936
Same as answer just above.2937
62. -line1654 I think there are many kind of decay modes in “Prompt hadronic”2938
and “Double charm”. I am not sure if the kind of decay mode in SR is similar2939
```
to that in BR01, BR02. Could you check the MC generated decay mode ID (by2940
```
191
```
mcGentool or Topoana or whatever) in each SR, BR01 and BR02 ? Please2941
```
```
check and compare it too with that at the lowest bin of EextraECL in the SR (signal2942
```
```
enhanced region).2943
```
In order to answer to this questions I had to produce a lot of plots which I put2944
in an Appendix. Please refer to Appendix J.2945
63. -line1736 Sorry, I can not understand the meaning of ζ. Could you add more2946
explanation ?2947
When we apply a Data/MC correction e.g. charged slow pion efficiency cor-2948
rection of LID efficiency correction, then these corrections can alter both the2949
```
normalization (overall number of events) and the shape (no change in the over-2950
```
```
all number of events). These two effects are disentangled in our setup and2951
```
treated separately. ζ controls the impact of the normalization part on the2952
yield of every template. Since this effect can alter the measured yield of every2953
template it has to be multiplied to the expected number of events and the free2954
parameters that are modifying the yield of every template. I’m added some2955
more text in Line 1106 to make this more clear.2956
64. -line1752 I think it is better to move Table2 and related explanations here.2957
Please see my answer to Question 28.2958
65. -line1764 What is NsB0 ? I firstly thought it is the number of reconstructed2959
signals as mentioned in line1760, but according to line 1732, N is defined as2960
the number of true generated events. Could you check and clarify ?2961
These were supposed to be the reconstructed events that are used to create2962
the templates, but my notation was somewhat unfortunate. I modified the2963
notation a bit to make it more clear. Now there events are denoted as N recosB0 .2964
66. line1782 What is NnB ± in bold ? Is that Σi NnB±i2965
Fixed by Question 65.2966
67. -line1764 What is B(Dstar →) ? Could you add a daughter state ?2967
Apologies for the ambiguous notation. I intended to denote the sum of exclusive2968
BFs of the D∗ or D0 mesons that have been used in the reconstruction, but this2969
```
was not a great choice. I updated all the equations from (D∗ →) to (D(∗) →)2970 P
```
```
i fi) which I believe it more clear. I explain that in text now in Line 1142.2971
```
Let me know if you still find the notation problematic.2972
68. -line1779 In order to connect this equation to Eq.(39), could you write down2973
not only v but also vcb ?2974
Good idea! Thank you! I added this and explain what the subscript cb is in2975
text. Also simplified a bit the notation for the superscript e.g. sB0 → s0. I2976
also explain the new notation in text.2977
69. Figure 69-71 There are no explanations in the main text ?2978
Fixed.2979
70. -Table43 Before showing this table, could you put all distributions used for the2980
```
fit with Asimov data and post fit distribution ? Please show the pull too. (In2981
```
```
Asimov fit, pull should stay 0 in all bins. We need to confirm it.) Similar2982
```
192
comment to table452983
I added Figures 52 - 55.2984
71. -Table43 I can not understand the meaning of the variable and values listed in2985
Table43. Before showing this table, could you list and explain all parameters2986
```
in your fit, and which parameters are fixed (f00, efficiency, tau branching ra-2987
```
```
tio,...) with their value, and which parameters are floated with their limit and2988
```
constraint ? Similar comment to table45.2989
I added Appendix L which present a modifier grid plot of all the free and fixed2990
parameters of the fit as provided by cabinetry. I also reference this explicitly2991
in Line 13062992
72. -Table43 I guess you are showing fit error only, but you should show the central2993
```
value of the fit. (you need to show the output of the fit is consistent with the2994
```
```
expected Asimov input.) Similar comment to table45.2995
```
Sorry this should have been clearer in these Tables. I confirm that in all of our2996
Asimofv fits we get full closure. All free parameters in the fit are minimized to2997
their nominal values. The nominal values were presented in parentheses in the2998
first column of both Tables. I now confirm in the captions that we get closure2999
in the central values of the free parameters.3000
73. -Section 6.3.1, 6.3.2 Is this study done by separating positive and negative3001
```
helicity angle bins ? If so, please move these study after line1910 (at the3002
```
```
beginning of section 6.4.1.) If not, please repeat the same study by separating3003
```
```
them. (I assume final result of paper will be given by the separated bin.)3004
```
This study is not carried out in the two helicity bins. This study serves only3005
```
as a proof of concept to show that fitting R(D∗) directly is possible. For the3006
```
```
final result the next study with the simultaneous fit of R(D∗) and Pτ will be3007
```
used which by design is performed in two bins of the helicity angle. Therefore3008
```
I think it is not necessary to perform the R(D∗) fit only in two helicity bins as3009
```
this fit will not actually be used for our result but is described in the note for3010
demonstration purposes. The reason that I did not show the simultaneous fit3011
straigh away is that it is a way more complicated fit, with an extra observable3012
and way more templates and free parameters. I thought it might be more3013
```
instructive to first demonstrate the method with a normal R(D∗) setup, which3014
```
is more intuitive to more people and then demonstrate the method to the more3015
complicated Pτ fit.3016
74. -Figure74 Sorry, I thought the sideband was fitted too simultaneously. Am I3017
```
correct ? If so, please add the distribution of sideband too. (even if it is shown3018
```
in previous pages, I think you need to show it again here. probably, Figure3019
```
69-71 should be moved here ? )3020
```
Indeed the sidebands are fitted simultaneously to the SR and NR. I’m adding3021
a reference in the text that the previously shown distributions are also fitter3022
simulatenously together with these distributions. All the regions that are fitted3023
simultaneously can now be seen in Figures 52 - 55.3024
75. -Figure 75 caption is wrong3025
Apologies! The caption of Figure 38 is now corrected.3026
193
76. -Figure 75 What is the reason for the large (>10%) fraction of the non-diagonal3027
term ?3028
We believe that the migrations to the opposite sign of the cosinus of the helicity3029
angle arises because of poor resolution in the reconstruction of the Btag and D∗3030
kinematics. Furthermore the migrations are more prominent for the τ → ρντ3031
channels which is not surprizing since in these modes we reconstruct one extra3032
π0.3033
77. -Figure 75, line1901-1909 Sorry, I can not understand how you are performing3034
the fitting with true helicity angle. I can not understand how Figure75 is used.3035
```
Could you explain the method (with equation if needed) ?3036
```
We use the true helicity angle in order to build the templates as they are3037
```
outlined in Table 41. e.g. B0 → D∗τ (π ν) ν and cos θτhel > 0 means that3038
```
we have a signal decay where the τ lepton decays as τ → ρντ and the true3039
```
helicity angle (not the reconstucted one) is positive. We still use two bins of3040
```
the reconstructed helicity angle for our MC and Data in the fit as illustrated3041
in Figure 37 but these two bins can have signal events with either positive or3042
negative generated helicity. Our assumption is that our fit is sensitive enough3043
to properly scale events e.g with true positive helicity reconstructed in the3044
positive or negative bin since the template is common. The confusion matrix3045
in Figure 38 is only presented for illustration purposes. Since we use the true3046
helicity angle to build the templates we do not need to do any unfolding and3047
this matrix is not futher used in the fit.3048
78. -page101 table is out of page and there is no caption3049
I removed this big table now.3050
79. -Figure77, middle By eye, the distribution is not modeled by Gaussian well.3051
By eye, the mean looks negative. Could you add chi2/ndf and error bar to3052
histogram ? If chi2 is bad, could you test asymmetric Gaussian ?3053
You’re absolutely right! This was adressed in Michele’es Question 24. Please3054
let me know if you still see a problem with Figure 56.3055
80. -line 1928 Explanation of Section 3.1.4 should be moved here.3056
Please refer to my answer in Question 28. I would prefer to keep the methods3057
and tools at the beginning of the document and refer back to them when they3058
are being used.3059
81. -line 1933 It seems you are focusing on the technical explanation of the tool3060
itself, but I feel the explanation of the analysis method is not enough. Could3061
you modify the text ? For example, could you add how the nuisance parameters3062
```
are implemented to yourlikelihood in Eq.39 ? (Could you write down the cx3063
```
```
with the nuisance parameter?)3064
```
Table 2 outlines the different kind of parameters that are being used in the pyhf3065
framework to build the likelihood. The column Constraint term shows how the3066
nuisance parameter is being implemented mathematically and I added a short3067
description in the last column where I explain the role of every parameter in3068
text. I also added Appendix L which present a modifier grid plot of all the free3069
and fixed parameters of the fit as provided by cabinetry.3070
194
82. -line 1952 This is general feature in any analysis tool (not only sysvar but also3071
all physics analysis has this kind of feature in order to estimate systematic3072
```
error), so probably you can reduce to emphasis it.3073
```
Excuse my enthousiasm, I spent quite some time developing SysVar and I’m3074
```
quite proud for some parts of it including how flexible and intuitive it is (and3075
```
```
of course not so proud of some other parts) I removed this sentence.3076
```
83. -line1988-1991 I surprised that explanation of systematics errors are not enough.3077
Could you explain how you evaluate each systematics one by one, by adding3078
each subsection?3079
We have a unified approach to all systematic uncertainties where we include and3080
exclude the NPs and the subtract the uncertainties we get in quadrature. This3081
is now described starting from Line 1435. Please let me know what additional3082
information you would require as I don’t see any other obvious information to3083
include besides Tables ?? and ??.3084
84. I thinkerror of branching ratio of D(*)etaellnu need to be assigned ±100% (er-3085
```
rors on Table 6 should not be used). How are you assigning errors for now ?3086
```
Does sysvar support uniform function ?3087
I agree that introducing a 100% BF error is a valid and conservative approach.3088
However, in practice, this introduces significant technical challenges in the fit.3089
```
From previous experience with the semileptonic tagged R(D∗) measurement3090
```
```
(see [30]), we observed that such a large prior tends to be overly conservative.3091
```
Below I show a part of Figure 8 from [30]. Even when a 100% prior was assigned3092
```
to gap modes, the post-fit impact on R(D∗) was substantially smaller. This3093
```
demonstrates that the fit can constrain these contributions in a data-driven3094
manner. Given that the 100% prior is somewhat arbitrary—reflecting our3095
current lack of precise knowledge about these branching fractions—and that3096
it may not materially affect the final result, we propose starting with a less3097
```
conservative prior (e.g., 50%). If the post-fit impact appears underestimated,3098
```
we can iteratively broaden the prior as needed.3099
Figure 190: Pre and post fit impact of gap mode BF uncertainties in [30]
195
Regarding the use of a uniform distribution: while this is valid for toy sampling3100
to estimate impact, it is not consistent with the Gaussian constraints used by3101
pyhf for NPs. Therefore, we prefer to stay within a Gaussian treatment for3102
consistency between toys and the statistical model.3103
The errors I’m assigning now are the ones assumed from the HFLAV average3104
as outlined in Table 6, but since you say that they should not be used I can3105
move to a more conservative approach as described above.3106
85. For major error, please3107
I think you didn’t finish this question.3108
86. -Table 47 What is the meaning of “Multiplicative” “Additive” “Combined ρ =3109
0” “Combined ρ = 1” ?3110
The meaning of the terms Multiplicative and Additive are given in the para-3111
graph starting from Line 1400. Multiplicative is the part of the systematic3112
uncertainty associated with changes in the overall yield of every template. Ad-3113
ditive is the part of the systematic uncertainty associated with changes in the3114
shape of the template that do not affect the overall yield. The reason that we3115
refer to them as Multiplicative and Additive becomes clear if one looks closer3116
at Equation 38 since the normalization related term multiply the nominal rate,3117
while the shape related terms are being added to it. Combined ρ = 0 means3118
that we treat the multiplicative NP and the additive NP of a given principal3119
component as fully uncorrelated, while ρ = 1 means that these two are treated3120
as fully correlated. For completion we presented both approaches. We will3121
follow up on our final decision on how to treat these two effect which will be3122
done case by case.3123
87. -Table 47 Could you add total systematics ?3124
Added in Table 44.3125
88. -Table47 Which is the error from fitter bias, mentioned in line 19223126
Since we argue that there is not bias in our measurement as per Question 24,3127
we are not modifying the Table. But you’re right, back then I should have3128
included the error. Sorry for that.3129
89. -Section 6 Are the Asimov and toy studies performed with the systematic error3130
explained in Section 7 ? If so, please explain it clearly. If not, please repeat3131
the same study with systematics3132
In Figure 191 we present our results from the toy studies with the NPs turned3133
on. The top row shows the mean of the pull distribution for every parameter3134
of the fit extracted by performing a single gaussian fit to the pull distribution3135
we acquire from the toys. The middle plot shows the withd extracted in the3136
same way. The bottom row shows the pull distribution for every parameter of3137
the fit. We choose to show those distributions in this way to avoid presenting3138
hundrends of pull distributions for every single parameter of the fit. We first3139
sample nuisance parameters based on a standard normal distribution. Then3140
we evaluate the likelihood on those nuisance parameters and the nominal free3141
uncronstrained parameters. Once we evaluate the likelihood we then sample3142
from a poisson distribution for every bin.3143
196
Figure 191: Results by runnning toys with nuisance parameters on.
The plots shown above have small caveat, we have excluded some regions with3144
very small bin counts, since the gaussian sampling of the nuisance parameters3145
was leading to negative yields for some bins in the toyes. Since Pτ is the3146
only parameter in the fit that can take both positiveand negative values, these3147
negative bin counts were always flipping the sign of Pτ to create negative yields,3148
introducing biases in the toy results. Of course such a scenario is unreaslistic3149
as we would never observe negative overall yields on the experimental dataset.3150
After removing these pathogenic regions, the toy fit results are more sensible.3151
90. -Section 6.4 You should perform linearity test (like Fig.73) of tau polarization3152
too3153
I added now Figure 58 which show the results of the linearity study as described3154
in Section 6.5.3155
91. Section 7 I think you should perform Asimov and toy study to check behavior of3156
the nuisanceparameters. Could you check the pre fit, post fit values and pulls of3157
all nuisance parameters by Asimov and the toy ? I worry the fit behavior can3158
be out of our understanding, because the number of nuisance parameters are3159
huge. What is the format of nuisance parameters ? Are those physics variables,3160
which behavior/meaning can be understandable by human ?3161
We performed a study with systematics on as described in questions 893162
197
• Comments received on 30-10-2025 during the Full Status Report3163
92. Quote your absolute systematic uncertainties for Ptau, not the percentage ones.3164
Updated Table 44.3165
93. What is the tau-missID component that has a similar distribution as your sig-3166
nal? How do you treat it ?3167
In Figure 192 we present the overview of the different τ modes that contribute3168
to this component. These are B meson semitauonic events where the τ lepton3169
has decayed in a different mode than the ones that we tried to reconstruct.3170
```
For comparison we always include the number of signal events (correctly re-3171
```
```
constructed τ mode) with the blue color. We present this information for all3172
```
eight diffent reconstruction modes. We see that for the τ → πντ modes a3173
muon that has faked a pion is the dominant crossfeed component. For the3174
τ → ρντ modes it’s mostly events where τ decayed into one charged and two3175
neutral pions where one of the two neutral pions has been missed. For the3176
leptonic reconstruction we see that we have a handful of semitauonic events3177
```
that survived our m2miss cut (we expect these semitauonic events to have higher3178
```
values of m2miss. However these events are very few compared to the overall3179
```
semileptonic yield (for electrons and muons.
```
0 5 10 15 20 25 30
00 0
e eK
K0K00 0 0
```
K*(892)00
```
KK0
```
K*(892)0K0 0
```
other
```
B0 D* (D0 ) +
```
0 10 20 30 40 50
```
B0 D* (D0 ) +
```
0 5 10 15 20 25 30 35
```
B+ D*0(D0 0) +
```
0 10 20 30 40 50 60
```
B+ D*0(D0 0) +
```
Signal templatestau_misID template
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5Events
00 0
e eK
K0K00 0 0
```
K*(892)00
```
KK0
```
K*(892)0K0 0
```
other
```
B0 D* (D0 ) e+
```
0 5 10 15 20Events
```
B0 D* (D0 ) +
```
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5Events
```
B+ D*0(D0 0) e+
```
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5Events
```
B+ D*0(D0 0) +
```
Figure 192: Overview of different crossfeed modes of semitauonic B meson decays.
3180
This component was mistakenly merged into the signal templates so far. This3181
```
is not a problem for R(D∗) however it would affect the estimation of Pτ , since3182
```
the helicity angle is not well defined for these decays. In order to cirvumvent3183
this problem, we decide to create a separate template for this componenet in3184
```
the fit. This component if fully linked via R(D∗) but does not affect Pτ .3185
```
Currently we do not have access to corrections for leptons faking pions for3186
the relevant momentum range within the systematics framework. However we3187
198
believe that this component is small enough to not really affect our extraction3188
```
of R(D∗). Nevertheless if the RC believes that we should treat this component3189
```
differently, we can assign a conservative 20% uncertainty to these τ → µντ νµ3190
```
events and evaluate the uncertainty on R(D∗).3191
```
We update Tables 40 and 41 with the overview of the templates and all respec-3192
tive results in the note by adding this extra template.3193
199
References3194
[1] E. Paudel, Problems of standard model, review, BMC Journal of Scientific3195
```
Research 4 (2022) .3196
```
[2] Ed. A. J. Bevan, B. Golob, Th. Mannel, S. Prell, and B. D. Yabsley, The3197
```
physics of the B factories, Eur. Phys. J. C74 (2014) 3026, arXiv:1406.6311.3198
```
[3] S. Banerjee et al., Averages of b-hadron, c-hadron, and τ -lepton properties as3199
of 2023, 2024.3200
```
[4] S. Hirose et al., Measurement of the τ lepton polarization and r(D∗) in the3201
```
decay B → D∗τ −ντ with one-prong hadronic τ decays at belle, Physical3202
```
Review D 97 (2018) .3203
```
[5] T. Keck et al., The Full Event Interpretation, Comput. Softw. Big Sci. 33204
```
(2019) 6, arXiv:1807.08680.3205
```
[6] T. B. I. collaboration, Conference Readiness webpage xwiki, 2025.3206
[7] Particle Data Group, R. L. Workman et al., Review of Particle Physics,3207
```
PTEP 2022 (2022) 083C01.3208
```
[8] G. Cowan, Statistical data analysis, Oxford University Press, USA, 1998.3209
[9] L. Heinrich, M. Feickert, and G. Stark, pyhf: v0.7.6, 2020.3210
[10] L. Heinrich, M. Feickert, G. Stark, and K. Cranmer, pyhf: pure-python3211
implementation of histfactory statistical models, Journal of Open Source3212
```
Software 6 (2021) 2823.3213
```
[11] T. Sj¨ostrand et al., An Introduction to PYTHIA 8.2, Comput. Phys.3214
```
Commun. 191 (2015) 159, arXiv:1410.3012.3215
```
[12] A. Pich, Precision tau physics, Progress in Particle and Nuclear Physics 753216
```
(2013) .3217
```
```
[13] M. Neubert, Heavy-quark symmetry, Physics Reports 245 (1994) 259.3218
```
[14] I. Caprini, L. Lellouch, and M. Neubert, Dispersive bounds on the shape of b3219
```
→ d()l v form factors, Nuclear Physics B 530 (1998) 153.3220
```
[15] M. A. Ivanov, J. G. K¨orner, and C. T. Tran, Probing new physics in3221
```
b0 → D(∗)τ −ντ using the longitudinal, transverse, and normal polarization3222
```
```
components of the tau lepton, Phys. Rev. D 95 (2017) 036021.3223
```
[16] G. C. Branco et al., Theory and phenomenology of two-higgs-doublet models,3224
```
Physics Reports 516 (2012) 1, Theory and phenomenology of3225
```
two-Higgs-doublet models.3226
[17] H. M. Lee, Leptoquark option for b-meson anomalies and leptonic signatures,3227
```
Phys. Rev. D 104 (2021) 015007.3228
```
[18] A. Maiezza, M. Nemevˇsek, F. Nesti, and G. Senjanovi´c, Left-right symmetry3229
```
at lhc, Phys. Rev. D 82 (2010) 055022.3230
```
[19] N. Toge, KEK B-factory Design Report, tech. rep., KEK, Tsukuba, 1995.3231
200
```
[20] SLAC-Berkeley(LBL)-LivermorePEP-IIDesignGroup, M. S. Zisman, The3232
```
```
PEP-II project: design status and Ramp;D results, tech. rep., Lawrence3233
```
Berkeley Nat. Lab., Berkeley, CA, 1993.3234
[21] E288, J. Yoh, The Discovery of the B quark at Fermilab in 1977: The3235
```
Experiment coordinator’s story, AIP Conf. Proc. 424 (1998) 29.3236
```
[22] BABAR Collaboration, J. P. Lees et al., Evidence for an excess of3237
```
B → D(∗)τ −ντ decays, Phys. Rev. Lett. 109 (2012) 101802.3238
```
[23] HFLAV Collaboration, Hflav semi-leptonic moriond 2024 results,3239
```
https://hflav-eos.web.cern.ch/hflav-eos/semi/moriond24/html/3240
```
RDsDsstar/RDRDs.html. Accessed: 2025-02-05.3241
[24] Belle Collaboration, M. Huschle et al., Measurement of the branching ratio of3242
```
B → D(∗)τ −ντ relative to B → D(∗)ℓ−νℓ decays with hadronic tagging at belle,3243
```
```
Phys. Rev. D 92 (2015) 072014.3244
```
```
[25] Belle Collaboration, G. Caria et al., Measurement of R(d) and R(D∗) with a3245
```
```
semileptonic tagging method, Phys. Rev. Lett. 124 (2020) 161803.3246
```
[26] LHCb Collaboration, R. Aaij et al., Measurement of the ratios of branching3247
```
fractions R(D∗) and R(D0), Phys. Rev. Lett. 131 (2023) 111802.3248
```
[27] LHCb Collaboration, R. Aaij et al., Test of lepton flavor universality using3249
```
B0 → D∗−τ +ντ decays with hadronic τ channels, Phys. Rev. D 108 (2023)3250
```
012018.3251
[28] B. I. Collaboration et al., A test of lepton flavor universality with a3252
```
measurement of r(d∗) using hadronic b tagging at the belle ii experiment,3253
```
2024.3254
[29] LHCb, C. Chen, b → cl¯ν decays at LHCb, in 58th Rencontres de Moriond on3255
QCD and High Energy Interactions, 5, 2024, arXiv:2405.08953.3256
[30] B. I. Collaboration, Test of lepton flavor universality with measurements of3257
```
r(d+) and r(d∗+) using semileptonic b tagging at the belle ii experiment, 2025.3258
```
[31] Belle II Framework Software Group, T. Kuhr et al., The Belle II Core3259
```
Software, Comput. Softw. Big Sci. 3 (2019) 1, arXiv:1809.04299.3260
```
```
[32] Belle II collaboration, Belle II Analysis Software Framework (basf2),3261
```
```
https://doi.org/10.5281/zenodo.5574115.3262
```
[33] M. Eliachevitch et al., belle2/b2luigi: v1.1.0, Jan., 2025.3263
```
doi: 10.5281/zenodo.14710343.3264
```
```
[34] T. Ilias, rdstar1prong: Analysis code for R(D∗) measurement,3265
```
```
https://gitlab.desy.de/itsaklid/rdstar1prong, 2024. Accessed:3266
```
2025-02-06.3267
[35] S. Baker and R. D. Cousins, Clarification of the use of chi-square and3268
likelihood functions in fits to histograms, Nuclear Instruments and Methods in3269
```
Physics Research 221 (1984) 437.3270
```
201
[36] ROOT, K. Cranmer et al., HistFactory: A tool for creating statistical models3271
for use with RooFit and RooStats, .3272
[37] CERN, Workshop on Confidence Limits: CERN, Geneva, Switzerland 17 - 183273
```
Jan 2000. 1st Workshop on Confidence Limits, (Geneva), CERN, 2000.3274
```
```
doi: 10.5170/CERN-2000-005.3275
```
[38] S. Kraml et al., Searches for new physics: Les houches recommendations for3276
```
the presentation of lhc results, The European Physical Journal C 72 (2012) .3277
```
[39] H. Dembinski and P. O. et al. scikit-hep/iminuit, .3278
[40] P. Virtanen et al., SciPy 1.0: Fundamental Algorithms for Scientific3279
```
Computing in Python, Nature Methods 17 (2020) 261.3280
```
[41] R. Barlow and C. Beeston, Fitting using finite monte carlo samples,3281
```
Computer Physics Communications 77 (1993) 219.3282
```
[42] F. L. Gewers et al., Principal component analysis: A natural approach to data3283
```
exploration, ACM Comput. Surv. 54 (2021) .3284
```
[43] P. M. Tsaklidis Ilias, Aggarwal Agrim and B. Florian, Sysvar: A new tool for3285
enhancing consistency in the treatment of systematics,3286
```
https://gitlab.desy.de/itsaklid/sysvar, 2024. Accessed: 2025-02-06.3287
```
[44] P. Feichtinger et al., Test of light-lepton universality using the decays at belle3288
ii, Tech. Rep. BELLE2-NOTE-3809, Belle II Collaboration, 2024. Belle II3289
Internal Note.3290
[45] T. Ilias, Presentation at analysis tools meeting,3291
```
https://indico.belle2.org/event/12666/, 2024. Accessed: 2025-02-06.3292
```
```
[46] T. Ilias, Presentation at (s)l working group meeting,3293
```
```
https://indico.belle2.org/event/12979/, 2024. Accessed: 2025-02-06.3294
```
```
[47] T. Ilias, A. Agrim, P. Markus, and B. Florian, Combining r(d*) measurements3295
```
at belle ii,3296
```
https://indico.cern.ch/event/1345421/contributions/6084737/, 2024.3297
```
Presentation at CERN Indico Event 1345421, Accessed: 2025-02-06.3298
[48] A. Held et al., scikit-hep/cabinetry: v0.6.0, Sept., 2023.3299
```
doi: 10.5281/zenodo.8360833.3300
```
[49] F. U. Bernlochner et al., Hammer - helicity amplitude module for matrix3301
element reweighting, May, 2024. doi: 10.5281/zenodo.11245573.3302
[50] F. U. Bernlochner et al., Das ist der hammer: consistent new physics3303
interpretations of semileptonic decays, The European Physical Journal C 803304
```
(2020) .3305
```
[51] B. I. Collaboration, Wg1 skimming advice and resources,3306
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/3307
```
Physics%20WebHome/Physics%20Working%20Groups/Physics%20SLMissing/3308
WG1%20Skimming%20Advice%20and%20Resources/3309
#HWherecanIseetheavailablecompletedskimsofsignalMC153F-1.3310
```
Accessed: 2025-02-09.3311
```
202
[52] B. I. Collaboration, Data production group webpage,3312
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/3313
```
Data%20Production%20WebHome/. Accessed: 2025-02-09.3314
[53] G. Ricciardi, Semileptonic and leptonicbdecays, circa 2016, Modern Physics3315
```
Letters A 32 (2017) 1730005.3316
```
```
[54] Belle II Collaboration, I. Adachi et al., First measurement of r(Xτ /ℓ) as an3317
```
```
inclusive test of the b → cτ ν anomaly, Phys. Rev. Lett. 132 (2024) 211804.3318
```
[55] B. I. Collaboration, Gap modes replacement strategy,3319
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/3320
```
Physics%20WebHome/Physics%20Working%20Groups/Physics%20SLMissing/3321
MC%20Samples%20WG1/Correction%20of%20BF%28B%20to%20Xc%20l%20%CE%3322
BD%29%20in%20generic%20MC/. Accessed: 2025-02-09.3323
[56] F. U. Bernlochner, Z. Ligeti, M. Papucci, and D. J. Robinson, Exploring the τ3324
```
polarization in b → xτ ν along different axes, Phys. Rev. D 107 (2023) 096008.3325
```
[57] B. I. Collaboration, Semitauonic gap modes dec files,3326
```
https://gitlab.desy.de/belle2/software/basf2/-/merge_requests/3327
```
671#cec53822aca440bde1c9eae569b263c0540294e0. Accessed: 2025-02-09.3328
[58] B. I. Collaboration, Fei efficiencies factorizability, talk at physics week in3329
valencia 2022, https://indico.belle2.org/event/7825/contributions/3330
49619/attachments/19751/29288/FEI.pdf. Accessed: 2025-02-09.3331
[59] B. I. Collaboration, π0 reconstruction recommendations from the neutrals3332
group, https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%3333
20Internal/Physics%20Performance%20Webhome/Neutrals%3334
20Performance/May2020%20pi0%20Recommendations/. Accessed:3335
2025-02-09.3336
[60] B. I. Collaboration, slow π0 efficiency corrections from the neutrals group,3337
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%3338
```
data-MC15rd/. Accessed: 2025-02-09.3339
[61] B. I. Collaboration, Lid recommendations,3340
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%3341
```
%20Moriond2024/. Accessed: 2025-02-09.3342
[62] B. I. Collaboration, Hid recommendations,3343
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%3344
```
%20release6%20%28Moriond2023%2C%20Moriond2024%29/. Accessed:3345
2025-02-09.3346
[63] B. I. Collaboration, stdkshort predefined lists in basf2,3347
```
https://software.belle2.org/light-2501-3348
```
betelgeuse/sphinx/analysis/doc/StandardParticles.htmlstdV0s.stdKshorts.3349
```
Accessed: 2025-02-09.3350
```
```
[64] B. I. Collaboration, Leptonic R(D∗) internal Belle II note,
```
```
https://docs.belle2.org/pubdata/documents/5/. Accessed : 2025 − 02 − 09.
```
203
[65] K. Hagiwara, A. D. Martin, and D. Zeppenfeld, polarization measurements at lep and3351
```
slc, Physics Letters B 235 (1990) 198.3352
```
[66] B. I. Collaboration, Belle II question explaining uniqueness of events,
```
https://questions.belle2.org/question/9704/where-can-i-rely-on-uniqueness-of-the-
```
experiment−r un−event−candidate
−combination/. Accessed:2025−02−09.
[67] B. I. Collaboration, Tracking efficiency recommendations from the performance group,
```
https://indico.belle2.org/event/10572/contributions/68899/attachments/25231/37323/tauef fmc15rdup
```
2025 − 02 − 09.
[68] B. I. Collaboration, Official conference recommendations from the performance group,3353
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%20Webhom3354
```
```
Accessed: 2025-02-09.3355
```
[69] B. I. Collaboration, π0 corrections from the neutrals group,3356
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%20Webhom3357
```
%20Tau%20studies%20overview/. Accessed: 2025-02-09.3358
[70] B. I. Collaboration, Lid group recommendations,3359
```
https://xwiki.desy.de/xwiki/bin/view/BI/Belle%20II%20Internal/Physics%20Performance%20Webhom3360
```
%20Moriond2024/. Accessed: 2025-02-09.3361
[71] B. I. Collaboration, Systematics corrections framework,3362
```
https://syscorrfw.readthedocs.io/en/latest/. Accessed: 2025-02-09.3363
```
[72] A. Gaz, Pid talk at physics week 2025,3364
```
https://indico.belle2.org/event/14981/contributions/98665/. slide 56.3365
```
[73] B. I. collaboration, Question about saving the momentum of an electron before the brems3366
recovery, https://questions.belle2.org/question/12505/leptonid-corrections-from-3367
electron-not-saved-after-brems-corrections/.3368
[74] Y. S. Akimasa Ishikawa, Lepton id efficiency correction and uncertainty in phase3 of3369
proc9 and bucket7 with two-photon process, Tech. Rep. BELLE2-NOTE-PH-2019-043,3370
Belle II Collaboration, 2020. Belle II Internal Note.3371
[75] K. Uno, Gitlab repository with code used to derive muons faking pions fake rate
corrections, https://gitlab.desy.de/kenta.uno/eelllid.
[76] Belle Collaboration, R. Glattauer et al., Measurement of the decay b → dℓνℓ in fully3372
reconstructed events and determination of the cabibbo-kobayashi-maskawa matrix3373
```
element |Vcb|, Phys. Rev. D 93 (2016) 032006.3374
```
```
[77] F. U. Bernlochner et al., Constrained second-order power corrections in hqet: r(D(∗)),3375
```
```
|Vcb|, and new physics, Phys. Rev. D 106 (2022) 096015.3376
```
[78] H. F. A. Group et al., Averages of b-hadron, c-hadron, and τ -lepton properties as of3377
summer 2016, 2018. doi: https://doi.org/10.1140/epjc/s10052-017-5058-4.3378
[79] D. Ferlewicz, P. Urquijo, and E. Waheed, Revisiting fits to B0 → D∗−ℓ+νℓ to measure3379
|Vcb| with novel methods and preliminary lqcd data at nonzero recoil, Phys. Rev. D 1033380
```
(2021) 073005.3381
```
204
```
[80] F. Bernlochner and Z. Ligeti, Semileptonic b(s) decays to excited charmed mesons with3382
```
```
e, µ, τ and searching for new physics with r(d∗∗), Physical Review D 95 (2016) .3383
```
[81] F. U. Bernlochner, Z. Ligeti, and D. J. Robinson, Model-independent analysis of3384
```
semileptonic b decays to D∗∗ for arbitrary new physics, Phys. Rev. D 97 (2018) 075011.3385
```
[82] Belle-II, F. Abudin´en et al., A calibration of the Belle II hadronic tag-side reconstruction3386
algorithm with B → Xℓν decays, arXiv:2008.06096.3387
```
[83] Belle-II, F. Abudin´en et al., Measurement of the branching fraction B( ¯B0 → D∗+ℓ− ¯νℓ)3388
```
with early Belle II data, arXiv:2004.09066.3389
```
[84] T. B. Collaboration, R(D∗) with leptonic and hadronic fei-tag at belle (internal),
```
```
https://docs.belle2.org/pubdata/documents/91/. Accessed : 2025 − 02 − 09.
```
205
Additional Material3390
This sections contains all figures and numbers that are requested to be approved for3391
public presentation.3392
206