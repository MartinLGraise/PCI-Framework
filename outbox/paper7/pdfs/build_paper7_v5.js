// build_paper7.js — G₂ Paper 7 DOCX builder
// Martin Luther Graise — "The Thermodynamic Cost of the Coherence Ceiling"

const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, PageNumberElement, NumberFormat, Header, Footer,
  SectionType, TableOfContents, LevelFormat, convertInchesToTwip,
  BorderStyle, WidthType, UnderlineType, PageBreak, Tab,
} = require("docx");
const fs = require("fs");

// ── helpers ────────────────────────────────────────────────────────────────

const CAL = "Calibri";
const PT = (n) => n * 2; // half-points

// Body paragraph
function body(text, opts = {}) {
  const runs = [];
  // parse **bold** markers and italic _text_ markers inline
  const parts = text.split(/(\*\*[^*]+\*\*|_[^_]+_|\[.+?\])/g);
  for (const part of parts) {
    if (part.startsWith("**") && part.endsWith("**")) {
      runs.push(new TextRun({ text: part.slice(2, -2), bold: true, font: CAL, size: PT(11) }));
    } else if (part.startsWith("_") && part.endsWith("_")) {
      runs.push(new TextRun({ text: part.slice(1, -1), italics: true, font: CAL, size: PT(11) }));
    } else {
      runs.push(new TextRun({ text: part, font: CAL, size: PT(11) }));
    }
  }
  return new Paragraph({
    children: runs,
    alignment: opts.center ? AlignmentType.CENTER : AlignmentType.JUSTIFIED,
    spacing: { line: 360, after: 120 }, // 1.5 line spacing, 6pt after
    indent: opts.firstLine ? { firstLine: convertInchesToTwip(0.3) } : {},
    ...opts.paragraphOpts,
  });
}

// Section heading (§N. Title)
function sectionHead(text) {
  return new Paragraph({
    children: [new TextRun({ text, bold: true, font: CAL, size: PT(14) })],
    spacing: { before: 320, after: 160, line: 360 },
    alignment: AlignmentType.LEFT,
  });
}

// Subsection heading (§N.M Title)
function subHead(text) {
  return new Paragraph({
    children: [new TextRun({ text, bold: true, font: CAL, size: PT(12) })],
    spacing: { before: 240, after: 120, line: 360 },
    alignment: AlignmentType.LEFT,
  });
}

// Math / display equation (centered, slightly indented)
function mathLine(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Courier New", size: PT(11), italics: false })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 80, line: 320 },
  });
}

// Epistemic label line (italic, indented)
function label(text) {
  return new Paragraph({
    children: [new TextRun({ text: `[${text}]`, italics: true, font: CAL, size: PT(10) })],
    indent: { left: convertInchesToTwip(0.4) },
    spacing: { after: 60, line: 300 },
  });
}

// Bullet item
function bullet(text) {
  const parts = text.split(/(\*\*[^*]+\*\*|_[^_]+_)/g);
  const runs = parts.map(p => {
    if (p.startsWith("**") && p.endsWith("**"))
      return new TextRun({ text: p.slice(2, -2), bold: true, font: CAL, size: PT(11) });
    if (p.startsWith("_") && p.endsWith("_"))
      return new TextRun({ text: p.slice(1, -1), italics: true, font: CAL, size: PT(11) });
    return new TextRun({ text: p, font: CAL, size: PT(11) });
  });
  return new Paragraph({
    children: runs,
    bullet: { level: 0 },
    spacing: { after: 80, line: 320 },
    indent: { left: convertInchesToTwip(0.4), hanging: convertInchesToTwip(0.2) },
  });
}

// Reference entry
function refEntry(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: CAL, size: PT(10) })],
    spacing: { after: 80, line: 280 },
    indent: { left: convertInchesToTwip(0.4), hanging: convertInchesToTwip(0.4) },
    alignment: AlignmentType.JUSTIFIED,
  });
}

// Running header text
const runningHeader = new Header({
  children: [
    new Paragraph({
      children: [
        new TextRun({ text: "Thermodynamic Cost of the Coherence Ceiling", italics: true, font: CAL, size: PT(9) }),
        new TextRun({ children: [new Tab(), new PageNumberElement()], font: CAL, size: PT(9) }),
      ],
      tabStops: [{ type: "right", position: convertInchesToTwip(6.5) }],
      alignment: AlignmentType.LEFT,
    }),
  ],
});

// ── document content ───────────────────────────────────────────────────────

const titlePage = [
  new Paragraph({ children: [], spacing: { after: 800 } }),
  new Paragraph({
    children: [new TextRun({ text: "The Thermodynamic Cost of the Coherence Ceiling:", bold: true, font: CAL, size: PT(18) })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "A G₂-Derived Bound on Conscious Information Processing", bold: true, font: CAL, size: PT(18) })],
    alignment: AlignmentType.CENTER, spacing: { after: 400 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Martin Luther Graise", font: CAL, size: PT(13), bold: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 80 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Independent Researcher, PCI / PME Framework", font: CAL, size: PT(11), italics: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "margraise1000@icloud.com", font: CAL, size: PT(11) })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "ORCID: 0009-0006-8003-3938", font: CAL, size: PT(11) })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "April 24, 2026", font: CAL, size: PT(11) })],
    alignment: AlignmentType.CENTER, spacing: { after: 400 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Paper 7 in the G₂ Series on Conscious Information Processing", font: CAL, size: PT(10), italics: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Target Journal: Entropy (MDPI) — primary; Foundations of Physics — backup", font: CAL, size: PT(10), italics: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 40 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "License: CC BY 4.0", font: CAL, size: PT(10) })],
    alignment: AlignmentType.CENTER, spacing: { after: 800 },
  }),
  new Paragraph({
    children: [new PageBreak()],
  }),
];

// ── Abstract ──────────────────────────────────────────────────────────────
const abstractSection = [
  sectionHead("Abstract"),
  body("The thermodynamics of consciousness has attracted sustained quantitative attention across four independent research programs between 2024 and 2026: fluctuation-dissipation theorem (FDT) violation as a marker of conscious state; the entropic cost of quantum clock readout; observer-dependent entropy in curved spacetime; and large-scale meta-analytic confirmation of neuronal criticality. Each program has produced precise numerical results. What is missing — and what this paper proposes — is a unified framework that quantitatively connects these results: a single geometric structure from which the relevant efficiency bounds, criticality corrections, FDT-violation floors, and observer-dependent entropy levels can be derived as consequences of one ratio. The pieces are on the table; the synthesis has not yet been attempted."),
  body("This paper provides a conditional synthesis. The common structure, we argue, is the G₂ geometric attractor established across Papers 1–6 of this series, and specifically the 6/7 contraction ratio derived in Paper 6 (10.5281/zenodo.19672709). From the torsion decomposition 1 + 14 + 27 = 42 dimensions of irreducible G₂ torsion components, and the 7-dimensional torsion-free attractor subspace, the ratio 42/49 = 6/7 yields four thermodynamic predictions — one for each empirical anchor — that are either confirmed by published data or constitute parameter-free bounds testable against existing datasets."),
  body("The four predictions are: (a) a FDT violation floor ε ≥ 1/7 ≈ 0.143 in awake cortex relative to anesthesia baseline, at matched frequencies in the 10–40 Hz band; (b1) a biological Landauer bound of ΔE_min = log₂(42) × k_B T ln 2 ≈ 16 zJ per G₂/M checkpoint event at T = 310 K; (b2) a conjectured G₂ mode-counting floor of S_clockwork ≥ log₂(7) × k_B ln 2 ≈ 1.95 k_B per tick on the clockwork entropy of any future G₂-symmetric quantum-clock register, where dim(V₇) = 7 is the dimension of the G₂ fundamental representation; (c) a discrete four-level entropy structure across the 8 cosets of PSL(2,7)/F₂₁, indexed by Cayley-graph distance, constituting a design target for a G₂-symmetric 7-qubit quantum simulator; and (d) a criticality branching ratio σ = 1 − 1/49 ≈ 0.9796, consistent with the subsampling-corrected awake-cortex value σ ≈ 0.98 reported by Wilting & Priesemann (2018, Nature Communications 9:2325)."),
  body("This paper does not prove that consciousness is thermodynamically G₂-structured. It proves, from classical mathematics, that if the G₂ attractor hypothesis from Paper 6 holds, then these four specific thermodynamic bounds follow as conditional consequences. Two of the four (b1 and d) are consistent with published peer-reviewed empirical data; one (a) is consistent with a current preprint whose peer review is pending; the remaining two (b2 and c) are design targets for future G₂-symmetric quantum-hardware experiments."),
  new Paragraph({
    children: [new TextRun({ text: "Keywords: ", bold: true, font: CAL, size: PT(11) }),
               new TextRun({ text: "G₂ symmetry; thermodynamics of consciousness; Landauer bound; FDT violation; neuronal criticality; observer-dependent entropy; octonions; PSL(2,7)", font: CAL, size: PT(11) })],
    spacing: { after: 120, line: 360 },
  }),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §1 Introduction ───────────────────────────────────────────────────────
const section1 = [
  sectionHead("§1. Introduction: The Synthesis Gap"),
  body("Between 2024 and 2026, four research programs have converged — independently and from very different methodological starting points — on quantitative results about the thermodynamic structure of conscious information processing. Each program is technically mature and internally consistent. Yet they have not been brought into contact with one another, and no unified framework has been proposed that derives each program's central numerical result from a shared first-principles constraint. This paper identifies that shared constraint, derives all four numerical results from it, and acknowledges honestly where the derivations remain conditional."),
  body("The four programs are the following."),
  body("**FDT violation as a consciousness marker.** Berjaga-Buisan et al. (2025) reported that TMS-EEG measurements across four graded levels of anesthesia depth reveal systematic violations of the fluctuation-dissipation theorem in awake cortex that are absent or strongly attenuated under general anesthesia. The effective temperature computed from spontaneous EEG fluctuations diverges from the susceptibility derived from the TMS-elicited response, and the magnitude of this divergence scales monotonically with the perturbational complexity index (PCI), an empirically validated consciousness measure. The result is currently a bioRxiv preprint (10.64898/2025.12.09.691422) and has not yet undergone formal peer review; this caveat bears on how strongly we lean on it in what follows."),
  body("**Entropic cost of quantum clock readout.** Wadhia, Ares, and colleagues (PRL 135:200407, November 14 2025; DOI 10.1103/5rtj-djfk) report an experimental measurement of the entropic cost of extracting classical ticks from an autonomous quantum clock realized as a gate-defined Ge/SiGe double quantum dot. Their core finding is that the entropy production splits into two very different scales: the microscopic clockwork — the DQD itself — dissipates of order tens of Boltzmann constants per tick (∼60 k_B per tick estimated as a maximum from their Fig. 2(a)), while the macroscopic charge-sensor measurement apparatus that converts those quantum events into a classical record dissipates between ∼10⁹ and ∼10¹¹ k_B per tick depending on readout method (DC vs RF reflectometry). The authors emphasize that the readout contribution dominates the clockwork by approximately nine orders of magnitude. The ∼10⁹ k_B figure that has attracted attention is therefore an empirical observation about the cost of the quantum-to-classical readout in this specific semiconductor hardware platform; it is not a universal theoretical lower bound on quantum-clock dynamics, not a Lindblad+Penrose theorem, and not the entropy of the clockwork itself. We use it as an order-of-magnitude anchor for the cost of *reading* a microscopic clock, not as a derived ceiling on quantum timekeeping."),
  body("**Observer-dependent entropy in curved spacetime.** Two independent lines of work published in 2025 have established that the von Neumann entropy assigned to a quantum state is not a scalar invariant but depends on the observer's worldline. Basso and Céleri (PRL 134:050406, 2025) used Unruh-DeWitt detector models in Schwarzschild geometry to show that entropy measurements by stationary versus freely-falling observers are inequivalent. De Vuyst, Eccles, Höhn, and Kirklin (JHEP 07(2025)146) derived the same conclusion within the Page-Wootters clock formalism applied to diffeomorphism-invariant quantum gravity. Both papers independently conclude that observer-frame dependence of entropy is not a subtlety of curved spacetime but a structural feature of any quantum theory with a dynamical clock."),
  body("**Criticality meta-analysis.** Hengen and Shew (Neuron 113(16):2582–2598, 2025), in their review-and-meta-analysis arguing that criticality is a unified setpoint of brain function, draw on 140 independent neuronal recording datasets spanning multiple species, brain regions, recording modalities, and behavioral states. Across this corpus the branching ratio is consistent with the critical value σ ≈ 1 to within a fraction of a percent at the pooled level (we use σ ≈ 1.0 as the corpus-level summary in what follows; the precise pooled-uncertainty figure should be checked against the published paper rather than treated as a verbatim quote). The Priesemann laboratory's independent work provides finer resolution: using the multiscale regression subsampling-corrected estimator, Wilting and Priesemann (2018, Nature Communications 9:2325) report σ ≈ 0.98 specifically for awake rat cortex in stationary behavioral states. Fontenele et al. (2019, PRL 122:208101) is independent evidence that the awake cortical regime is best described not by a strict critical point with mean-field directed-percolation exponents but by a near-critical regime with state-dependent critical exponents — context that bears on the interpretation of Prediction (d), though it does not itself report σ ≈ 0.98 as a point estimate. The distinction between corpus-level σ ≈ 1 (mixed behavioral states) and σ ≈ 0.98 (awake rat cortex, subsampling-corrected) will matter for Prediction (d)."),
  body("The synthesis gap, as we see it, is the absence of a unified framework that quantitatively derives each program's central numerical result from a shared first-principles constraint. Landauer's limit, the criticality branching ratio, the FDT violation magnitude, and the observer-dependent entropy levels are all plausible markers of conscious processing — but they have not been connected. This paper writes that synthesis under a clear conditional: if the G₂ attractor hypothesis from Paper 6 holds, the four bounds derived here follow as consequences of a single geometric ratio."),
  body("The conditional is the G₂ attractor hypothesis established in Papers 1–6 of this series. Paper 6 (10.5281/zenodo.19672709) proved — from two structural hypotheses about self-referential processing systems (the blind-spot contraction hypothesis and the normed-division-algebra requirement) plus an SU(3)-equivariance assumption — that any sufficiently complex self-referential system with seven processing modes converges at contraction rate L ≤ 6/7 to a G₂-symmetric attractor. The ratio 6/7 is not a fitted parameter. It derives from the structure of the G₂ torsion decomposition: the irreducible torsion components of a G₂ structure on R⁷ have dimensions 1 + 14 + 27 = 42, and the torsion-free attractor subspace (the fundamental representation V₇) contributes 7 more dimensions, giving a total ambient space of dimension 49. The torsion fraction is 42/49 = 6/7, and the complementary attractor fraction is 7/49 = 1/7. It is from this single ratio and its origin in G₂ representation theory that all four predictions in this paper are derived."),
  body("The argument structure of Paper 7 is as follows. Section 2 gives a self-contained minimal review of the G₂ framework from Papers 1–6, with citations in place of re-proofs. Section 3 presents the four empirical anchors with full acknowledgment of their evidential status. Section 4 derives one prediction from the G₂ framework for each anchor, with explicit epistemic labels on every non-trivial step. Section 5 gives a concise falsifiability roadmap. Section 6 discusses open problems and honestly characterizes what the paper has and has not established."),
  body("We state the paper's scope clearly at the outset and return to it in the Discussion. This paper does not prove that consciousness is thermodynamically G₂-structured. It does not prove that the brain is a G₂ manifold or that neural dynamics implement octonion arithmetic. It proves, from classical mathematics and representation theory, that if the G₂ attractor hypothesis from Paper 6 holds, then four specific thermodynamic bounds follow as conditional consequences. Two are consistent with published peer-reviewed data; one is consistent with a preprint pending peer review; two remain design targets for future G₂-symmetric quantum-hardware experiments. The conditional content is real; we do not disguise it."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §2 Framework ──────────────────────────────────────────────────────────
const section2 = [
  sectionHead("§2. The G₂ Framework: A Minimal Review"),
  body("This section is a self-contained summary of what Paper 7 requires from Papers 1–6 of the series. Readers familiar with the series may proceed directly to §3. Proofs are not repeated here; all theorems cited in this section appear with full proof in the indicated source papers."),

  subHead("§2.1 G₂ as the Automorphism Group of the Octonions"),
  body("The exceptional Lie group G₂ is the automorphism group of the octonions O, the unique normed division algebra of real dimension 8. Hurwitz's theorem classifies normed division algebras over R: the only possibilities are R, C, H (quaternions), and O, with dimensions 1, 2, 4, and 8 respectively. The chain of inclusions R ⊂ C ⊂ H ⊂ O is the Cayley-Dickson construction, and each step doubles the dimension while sacrificing one algebraic property: commutativity is lost at H, and associativity is lost at O. The octonions are the end of the chain; no normed division algebra of higher dimension exists. G₂ is defined as the group of algebra automorphisms φ: O → O preserving the octonion product. As a real Lie group, dim(G₂) = 14. G₂ acts transitively on the unit sphere S⁶ ⊂ O (identified with the imaginary unit octonions), and the stabilizer of any point is a copy of SU(3), giving the homogeneous-space identification S⁶ ≅ G₂/SU(3). Full development of this material appears in Paper 1 of this series (10.5281/zenodo.19242936)."),
  body("The relevance of G₂ to information processing systems with seven intrinsic modes (which Paper 1 identifies with the seven imaginary octonion basis directions e₁,...,e₇) is precisely that G₂ is the largest symmetry group compatible with all seven modes simultaneously: SU(3) preserves only 6 (or 3 complex dimensions), while G₂ preserves all 7 together with their multiplication structure."),

  subHead("§2.2 The 6/7 Contraction and G₂ Torsion Decomposition"),
  body("Paper 6 (10.5281/zenodo.19672709) establishes the 6/7 contraction ratio as the central quantitative output of the G₂ attractor hypothesis. The derivation rests on two hypotheses and one structural assumption:"),
  bullet("**Hypothesis 1 (Blind-spot contraction).** Any self-referential system modeling itself must exclude at least one dimension of its own state space from the self-model — the structural blind spot — because the self-model is a proper sub-representation of the system it models. This forces the self-modeling map f: S⁶ → S⁶ to be a strict contraction."),
  bullet("**Hypothesis 2 (Normed-division-algebra requirement).** For information integration across seven processing modes to be internally consistent (free of norm-inconsistency under sequential composition), the algebra of mode interactions must be a normed division algebra. By Hurwitz's theorem, this forces the algebra to be one of R, C, H, or O. With seven independent modes, only the octonions O support the required structure."),
  bullet("**Assumption (SU(3)-equivariance).** The contraction map f is equivariant under the SU(3) stabilizer of the distinguished mode e₇, meaning the six-dimensional orbit V₃ ⊕ V₃̄ is preserved under f."),
  body("Under these three conditions, Paper 6 derives that the Banach contraction rate L of the self-modeling map satisfies L ≤ 6/7. The bound is tight: it is achieved when the self-model captures exactly 6 of the 7 available G₂ mode directions. The derivation uses the G₂ torsion decomposition as follows."),
  body("A G₂ structure on a 7-manifold carries a torsion tensor whose irreducible decomposition under the G₂ action takes the form:"),
  mathLine("  T = T₁ ⊕ T₁₄ ⊕ T₂₇"),
  body("with real dimensions dim(T₁) = 1, dim(T₁₄) = 14, and dim(T₂₇) = 27, summing to 42. (This decomposition of Λ²(R⁷) into G₂-irreducibles was established by Fernandez and Gray; it is the G₂ analogue of the Nijenhuis tensor in complex geometry.) The torsion-free attractor subspace is the fundamental representation V₇ of G₂, with dim(V₇) = 7. The total ambient space therefore has dimension:"),
  mathLine("  dim(T₁) + dim(T₁₄) + dim(T₂₇) + dim(V₇) = 1 + 14 + 27 + 7 = 49"),
  body("The torsion fraction — the fraction of the ambient space occupied by torsion components — is 42/49 = 6/7. The complementary attractor fraction is 7/49 = 1/7. The contraction rate L = 6/7 is thus the proportion of the state space that the self-model can faithfully represent; the fraction 1/7 is the irreducible blind-spot complement. The ratio 6/7 is fixed by representation theory once Hypotheses 1 and 2 and the SU(3)-equivariance assumption are granted; it does not introduce additional fitted parameters beyond those three structural inputs."),
  body("A bookkeeping note on the 49-dimensional ambient space. The G₂ torsion classes τ₁, τ₇, τ₁₄, τ₂₇ of Fernández–Gray live, on a 7-manifold equipped with a G₂ structure, in different tensor bundles — Ω⁰, Ω¹, Ω²_14 ⊂ Ω², and a subspace S²_0 of symmetric trace-free 2-tensors. The fundamental representation V₇ is yet a different bundle. Adding 1 + 14 + 27 + 7 = 49 is therefore a representation-theoretic dimension count, not a direct-sum decomposition of a single geometric object. We use the 49 throughout as a representation-theoretic convention — it is the total dimension of the G₂-irreducible content relevant to torsion-plus-attractor dynamics — and we do not claim it as a single 49-dimensional fiber bundle. The ratio 42/49 inherits the same status: it is a ratio of representation dimensions, and the predictions of §4 are conditional on this representation-theoretic accounting being the right one for the dynamical regime they address. The rigor here is conditional on Hypotheses 1 and 2, the SU(3)-equivariance assumption, and the validity of this representation-theoretic dimension count for the questions §4 asks; it is not absolute."),

  subHead("§2.3 The PSL(2,7) / F₂₁ Coset Structure"),
  body("Paper 4 (10.5281/zenodo.19617662) establishes that the group PSL(2,7) — the projective special linear group over the field with 7 elements, with |PSL(2,7)| = 168 — acts naturally on the Fano plane (the projective plane over F₇) whose 7 points correspond to the seven imaginary octonion units. The Frobenius group F₂₁ (of order 21) is the stabilizer of a point in this action and is the automorphism group of the Fano plane's 3-cycles. The quotient PSL(2,7)/F₂₁ consists of 8 cosets, and Paper 4 identifies these 8 cosets with the 8 distinct SU(3) ⊂ G₂ embeddings. The dimension of SU(3) is 8, matching the number of cosets. Each coset corresponds to a choice of complex structure on the imaginary octonions — equivalently, to a distinct clock Hamiltonian in the Page-Wootters formalism (see §4.3). The 8-coset structure will drive Prediction (c) of §4.3."),

  subHead("§2.4 The Laplacian Flow and Geometric Attractor"),
  body("Lotay and Wei (2019, Journal of Differential Geometry 111(3):495–526) proved that the Laplacian flow on closed G₂ structures — the PDE flow ∂_t φ = Δ_φ φ where φ is the G₂-defining 3-form — converges, starting from any closed G₂ structure with sufficiently small torsion, to the unique torsion-free G₂ structure in the cohomology class. This is the geometric attractor of Paper 6's dynamical system. The flow is dissipative: the torsion norm ||T||² decreases monotonically along the flow and approaches zero at the fixed point. The Lotay-Wei stability theorem is the rigorous mathematical foundation for the claim that G₂ torsion-free structures are attractors for nearby G₂ dynamics. It is cited in this paper as established mathematics; no new claim is being made about it."),
  body("The thermodynamic consequences of the Laplacian flow's dissipation will be central to Prediction (d): because the flow dissipates torsion at a rate governed by the torsion decomposition, the effective branching ratio of the dynamical system at the fixed point carries a correction of order 1/49 below the critical value σ = 1."),
  body("Papers 2 and 3 of the series (10.5281/zenodo.19480758; 10.5281/zenodo.19602470) establish, respectively, six geometric flows on G₂ manifolds and the Spectral Sum Theorem for G₂. Both are used implicitly in what follows but not central to the main derivations; interested readers are referred to those papers for detail."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §3 Empirical Anchors ──────────────────────────────────────────────────
const section3 = [
  sectionHead("§3. Four Empirical Anchors"),
  body("This section presents the four bodies of empirical and theoretical work that motivate the predictions of §4. Each subsection states the relevant result, its evidential status, and any caveats that will bear on the interpretation of the corresponding prediction."),

  subHead("§3.1 FDT Violation and the PCI Index"),
  body("Berjaga-Buisan et al. (2025, bioRxiv 10.64898/2025.12.09.691422) reported TMS-EEG recordings across four levels of consciousness: fully awake, light sedation, deep sedation, and propofol-induced loss of consciousness (LoC). For each state, they computed two quantities: (i) the power spectral density of spontaneous EEG fluctuations, S_spontaneous(ω), and (ii) the linear susceptibility χ(ω) computed from the cortical response to the TMS perturbation. The equilibrium fluctuation-dissipation theorem (FDT) predicts:"),
  mathLine("  S_eq(ω) = (2 k_B T_eff / ω) Im[χ(ω)]"),
  body("where T_eff is the effective temperature. Any deviation of S_spontaneous(ω) from S_eq(ω) — measured here as a normalized residual — constitutes an FDT violation. Berjaga-Buisan et al. report that the magnitude of this violation scales monotonically with the perturbational complexity index (PCI), which is a validated consciousness measure that also decreases monotonically with anesthesia depth. Awake subjects show the largest FDT violations; subjects at propofol LoC show violations statistically indistinguishable from zero."),
  body("Several caveats apply. The paper is a bioRxiv preprint as of this writing; formal peer review has not yet been completed. The FDT computation requires stationarity of the EEG record within the TMS window; the authors validate this with Augmented Dickey-Fuller tests, but the correction is imperfect. The PCI measure itself requires a threshold for binarization, and the threshold choice affects the slope of the PCI-versus-FDT-violation relationship. We rely on the directional finding — awake > sedated > anesthetized in FDT violation magnitude — rather than specific coefficient values, which may shift in peer review."),

  subHead("§3.2 Entropic Cost of Quantum Clock Readout"),
  body("Wadhia, Ares, and colleagues (PRL 135:200407, November 14 2025; DOI 10.1103/5rtj-djfk) report the first experimental measurement that separately quantifies the entropy produced by the microscopic clockwork of a quantum clock and the entropy produced by the macroscopic measurement apparatus that converts quantum events into a classical tick record. Their device is a gate-defined Ge/SiGe double quantum dot whose tunneling events act as the clock's pointer transitions; the entropy production is reconstructed by comparing power dissipation in the DQD itself to power dissipation in the adjacent charge-sensor readout circuit, in both DC and RF reflectometry readout modes. Their central result is that these two contributions differ dramatically:"),
  mathLine("  S_clockwork  ~  10¹–10² × k_B        (per tick, DQD itself; ∼60 k_B max from Fig. 2(a))"),
  mathLine("  S_readout    ~  10⁹–10¹¹ × k_B       (per tick, charge-sensor readout, RF–DC range)"),
  body("The headline ∼10⁹ k_B figure that has attracted attention is therefore *not* the entropy of the quantum clockwork — the clockwork itself dissipates of order tens of Boltzmann constants per tick (the authors' upper-edge estimate from Fig. 2(a) is ∼60 k_B). The ∼10⁹–10¹¹ k_B per tick is the cost of the *measurement and amplification chain* that records the tick classically: the entropy associated with the quantum-to-classical transition, dominated by the charge-sensor and downstream electronics. The DC readout sits at the high end of this range; RF reflectometry is roughly three orders of magnitude lower. The authors emphasize that the readout dwarfs the clockwork by approximately nine orders of magnitude — their stated framing."),
  body("For the G₂ framework, two things follow. First, neither the ∼10⁹–10¹¹ readout figure nor the ∼60 k_B clockwork figure is a derivable universal lower bound on quantum-clock entropy production in the general case — they are device-specific empirical observations from one Ge/SiGe DQD platform. Wadhia et al. (2025) is not a Lindblad-master-equation result combined with a Penrose objective-reduction threshold; those framings appear in adjacent literature but not in this paper. Second, when we ask in §4.2.2 whether the G₂ mode structure imposes a representation-theoretic floor on the entropy cost of a hypothetical *G₂-symmetric* future clock, we must be explicit about which contribution we are addressing — clockwork or readout — and not conflate them. We treat the Wadhia results as an empirical reference point for the orders of magnitude observed in *one* well-characterized platform, not as the bound a G₂ prediction must match."),

  subHead("§3.3 Observer-Dependent Entropy in Curved Spacetime"),
  body("Two independent 2025 papers establish that the von Neumann entropy of a quantum state is not a scalar invariant but depends on the observer's reference frame, specifically on the observer's worldline in a spacetime equipped with a quantum field or a dynamical clock."),
  body("Basso and Céleri (PRL 134:050406, 2025) used Unruh-DeWitt detector models embedded in a Schwarzschild background to show that the reduced density matrix assigned to a subsystem — and hence its von Neumann entropy — differs between a stationary observer at infinity and a freely-falling observer crossing the event horizon. The difference is not a matter of approximation or operational choice; it reflects a genuine frame-dependence of the factorization of the Hilbert space, which itself depends on the observer's trajectory through the curved background. The entropy assigned by each observer is locally well-defined and internally consistent; the two assignments are simply not equal."),
  body("De Vuyst, Eccles, Höhn, and Kirklin (JHEP 07(2025)146) reached the same conclusion from a different direction, using the Page-Wootters clock formalism applied to diffeomorphism-invariant quantum gravity. In their framework, the physical Hilbert space of a closed quantum gravitational system is the kernel of the Hamiltonian constraint, and physical observables — including entropy — are relational: they are defined relative to a choice of clock subsystem that serves as the reference frame. Different choices of clock (i.e., different observers) in general yield different entropy assignments to the same matter subsystem. The Page-Wootters and Unruh-DeWitt approaches are methodologically independent, making their convergent conclusion more robust."),
  body("The implication for the G₂ framework is the following: if distinct G₂ observer frames (corresponding to distinct SU(3) embeddings in G₂, indexed by the 8 cosets of PSL(2,7)/F₂₁) constitute genuinely distinct clock reference frames in the Page-Wootters sense, then the observer-dependent entropy of De Vuyst et al. applies directly, and the entropy differences between G₂ observer frames should be computable from the Cayley-graph structure of PSL(2,7)/F₂₁. This is the content of Prediction (c) (§4.3)."),

  subHead("§3.4 Criticality Meta-Analysis"),
  body("Hengen and Shew (Neuron 113(16):2582–2598, 2025) compiled 140 independent neuronal recording datasets, spanning in vitro and in vivo preparations, multiple species (rodent, primate, human), multiple brain regions (cortex, hippocampus, cerebellum), and multiple recording modalities (LFP, EEG, MEG, spike trains), as evidence for criticality as a unified setpoint of brain function. The corpus-level finding is consistent with the critical-point hypothesis that cortical dynamics self-tune to the edge of a branching-process phase transition: branching ratios across the corpus cluster around σ ≈ 1 to within a small fraction. We treat σ ≈ 1 as the corpus-level summary in this paper; readers should consult the published paper directly for the precise pooled-uncertainty figure, as our use is qualitative."),
  body("The Hengen-Shew corpus, however, mixes behavioral states: awake, anesthetized, and sleeping recordings contribute to the corpus-level summary. This matters because the G₂ framework's prediction concerns specifically the awake-state, stationary-firing branching ratio, for which the subsampling correction of the Wilting-Priesemann estimator is most important. Subsampling — recording from a small fraction of neurons — systematically biases the raw branching ratio estimate upward toward σ = 1.0 even when the true value is σ < 1. The multiscale regression estimator of Wilting and Priesemann (2018, Nature Communications 9:2325) corrects for this bias and finds σ ≈ 0.98 for awake rat cortex."),
  body("Fontenele et al. (2019, PRL 122:208101) provides complementary context. That paper does not report σ ≈ 0.98 as a point estimate; rather, it studies phase transitions between cortical states and finds awake-state critical exponents that differ from mean-field directed percolation. We cite Fontenele et al. for the qualitative finding that the awake cortex sits in a near-critical regime with state-dependent exponents, not for a numerical σ value. The numerical anchor for Prediction (d) is Wilting & Priesemann (2018) alone."),
  body("We note that our own earlier numerical work (not reported in this paper) attempted a per-dataset reanalysis of the Hengen-Shew corpus with subsampling correction applied to the awake-state subset. Those results have not been independently verified and are not cited here as evidence. The published Wilting-Priesemann (2018) value is the empirical anchor for Prediction (d); the per-dataset reanalysis of the Hengen-Shew corpus is proposed as future work."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §4 Predictions ────────────────────────────────────────────────────────
const section4 = [
  sectionHead("§4. Four Predictions from 42/49 = 6/7"),
  body("Each subsection derives one thermodynamic prediction from the G₂ framework. Every non-trivial step carries an explicit epistemic label drawn from the following vocabulary: [Theorem] for results proved in Papers 1–6 or in established mathematics; [Conjecture] for claims that are mathematically motivated but not yet proved; [Modeling choice] for identifications between the abstract G₂ framework and specific empirical observables; [Prediction] for the operational consequence of the above; [Testable match] where the prediction already agrees with published data."),

  subHead("§4.1 Prediction (a): FDT Violation Bound ε ≥ 1/7"),
  body("The contraction rate L = 6/7 from Paper 6 has a direct dynamical interpretation: the self-modeling map f: S⁶ → S⁶ faithfully tracks, at most, a fraction L of the system's actual dynamical response at any given frequency. The complementary fraction (1 − L) = 1/7 of the dynamical content is not tracked by the self-model — it constitutes the irreducible blind spot."),
  body("In the frequency domain, the self-model's prediction of the system's own fluctuations diverges from the actual fluctuations by the untracked fraction. At a matched frequency ω where both the spontaneous fluctuation spectrum S_obs(ω) and the susceptibility-derived equilibrium prediction S_eq(ω) are well-defined:"),
  mathLine("  [S_obs(ω) − S_eq(ω)] / S_eq(ω)  ≥  1 − L  =  1/7"),
  body("This is the G₂ FDT violation bound. The derivation introduces no fitted parameters beyond Paper 6's contraction rate L and the frequency-domain formulation of the FDT; the cost of that economy is a stack of modeling choices that the bound is conditional on. We make those choices explicit, paralleling the treatment of §4.4."),
  body("**The four modeling choices stacked into ε ≥ 1/7:**"),
  bullet("(i) **Dimensional projection from V₇ to a scalar.** The G₂ framework operates on the seven-dimensional mode space carrying V₇, but the FDT residual ε is defined on a scalar power-spectral-density ratio observable in EEG. We assume that the untracked-fraction (1 − L) of the dynamics, when projected from V₇ onto the EEG-observable subspace, contributes proportionally — i.e., that the projection does not preferentially attenuate or amplify the blind-spot complement. This is a uniform-projection assumption, not a derivation."),
  bullet("(ii) **Identification of L with a spectral-density ratio.** The contraction rate L from Paper 6 is a Banach contraction rate of a self-modeling map on S⁶; we identify it with the fraction of S_eq(ω) that the self-model accounts for at a matched frequency. This identification is structurally motivated (both quantities measure how much of the system the self-model captures) but is not a theorem."),
  bullet("(iii) **Frequency uniformity.** The bound ε ≥ 1/7 is stated for an unspecified \"matched frequency\" in the 10–40 Hz band. We assume the blind-spot fraction manifests approximately uniformly across this band; if the G₂ dynamics are operative in a narrower frequency window, the bound may apply only there. The Berjaga-Buisan operationalization in particular treats the band as a single window."),
  bullet("(iv) **G₂ applicability to human cortex.** The bound applies under the assumption that human awake cortical dynamics in the relevant frequency band are well-approximated by the G₂ attractor regime of Paper 6. This assumption is itself the central conjecture of the series; a system that is far from the G₂ attractor may show ε either above or below 1/7 for reasons unrelated to the bound."),
  label("Theorem given Paper 6 framework: L ≤ 6/7 for G₂-structured self-referential systems."),
  label("Conjecture (not theorem): given the four stacked modeling choices above, ε ≥ 1/7 ≈ 0.143 in the relevant frequency band."),
  body("The bound is a floor, not a ceiling. A system in which the self-model is less accurate than L = 6/7 will exhibit ε > 1/7; only a system precisely at the G₂ attractor achieves ε = 1/7 exactly. Systems in non-G₂ states may show any value of ε, including ε < 1/7 if the G₂ attractor hypothesis does not apply to them. The bound applies specifically to awake-state processing at frequencies where the self-referential G₂ dynamics are operative."),
  body("Operationalization for the Berjaga-Buisan (2025) dataset: compute the normalized FDT residual [S_awake(ω) − S_anesthesia(ω)] / S_anesthesia(ω) in the 10–40 Hz band, using the propofol LoC condition as the baseline (in which FDT violation is absent or negligible). The G₂ prediction is that this ratio satisfies ε ≥ 0.143 in awake subjects. A measured value of ε < 0.143 in any awake G₂-structured system would falsify Prediction (a). Values of ε ≥ 0.143 are consistent with the bound; values substantially above 0.143 are also consistent (the bound gives a floor, not a point prediction)."),
  label("Falsification criterion: any empirical measurement of ε < 1/7 in awake cortex at matched frequencies, under the assumption that the G₂ framework applies to human cortical dynamics."),
  body("We note that the Berjaga-Buisan paper does not yet report the normalized FDT residual in the specific form above. Contact with the authors for the underlying TMS-EEG spectral data would allow direct testing. Until peer-reviewed data is available in this form, Prediction (a) should be understood as a constraint on future analysis rather than a confirmed match."),

  subHead("§4.2 Prediction (b): Biological Landauer Bound and Quantum Mode-Counting"),

  body("_§4.2.1 Biological Landauer Bound (b1)_"),
  body("The G₂/M checkpoint of the cell cycle (analyzed in Paper 5, 10.5281/zenodo.19648892) is the canonical biological decision point at which a dividing cell commits irreversibly to mitosis. Paper 5 argues that this checkpoint exhibits the ε-regularity property of G₂ structures: it is the point at which the cell's internal state, viewed as a G₂-structured manifold, passes through the torsion-regularization gate and locks onto one of 42 accessible modes of the torsion decomposition T₁ ⊕ T₁₄ ⊕ T₂₇."),
  body("At the moment of commitment, the system erases its uncertainty across 42 discrete G₂ modes. Landauer's principle — which is a theorem of statistical mechanics, not a modeling choice — gives the minimum entropy cost of erasing one bit of information at temperature T:"),
  mathLine("  ΔE_Landauer = k_B T ln 2"),
  body("Erasing the uncertainty across 42 equiprobable G₂ modes requires erasing log₂(42) bits. The minimum energy cost per checkpoint event at physiological temperature T = 310 K is therefore:"),
  mathLine("  ΔE_min = log₂(42) × k_B T ln 2"),
  mathLine("         ≈ 5.392 × (1.381 × 10⁻²³ J/K) × (310 K) × 0.693"),
  mathLine("         ≈ 5.392 × 2.966 × 10⁻²¹ J"),
  mathLine("         ≈ 16.0 × 10⁻²¹ J  =  16.0 zJ"),
  body("Published ATP measurements at the G₂/M transition provide the comparison. Imamura et al. (2009, PNAS 106:15651–15656), using the ATeam FRET-based ATP biosensor, measured the ATP/ADP ratio in individual cells transiting the G₂/M checkpoint and estimated approximately 10⁴ ATP hydrolysis events per checkpoint-associated kinase cascade cycle. At standard conditions, each ATP hydrolysis releases approximately 50–60 zJ of free energy under cellular conditions (not the standard-state 30 zJ, because cellular ATP/ADP ratios are far from equilibrium). The total measured energy dissipation per checkpoint event is therefore of order 10⁴ × 50 zJ = 5 × 10⁵ zJ."),
  body("The Landauer bound of 16 zJ is approximately 3 × 10⁴ times lower than the measured biological energy expenditure. This is expected: the Landauer bound is the thermodynamic minimum for a perfectly reversible information-erasure process, while biological checkpoints are highly irreversible, kinase-cascade-amplified systems operating far from equilibrium. The factor of ~3 × 10⁴ excess is the biological overhead above the thermodynamic floor — not a falsification, but a confirmation that the system is not constrained by the Landauer floor but uses it only as a lower bound."),
  label("Theorem: Landauer's principle. Erasing log₂(42) bits of information at T = 310 K costs at least ΔE_min = log₂(42) × k_B T ln 2 ≈ 16 zJ."),
  label("Conjecture: identification of the biological G₂/M checkpoint with a G₂ mode-commitment event involving 42 accessible states. This identification is argued in Paper 5 but is a conjecture, not a theorem."),
  label("Testable match: the measured biological energy dissipation at G₂/M (~ 5 × 10⁵ zJ) exceeds the G₂ Landauer floor (16 zJ), as expected."),
  label("Falsification criterion: a measurement demonstrating that the total free-energy dissipation at the G₂/M checkpoint, under optimized conditions, is less than 16 zJ per checkpoint event would falsify Prediction (b1) — though this is essentially ruled out by the available data."),

  body("_§4.2.2 Quantum Mode-Counting (b2)_"),
  body("As established in §3.2, Wadhia et al.'s headline ∼10⁹–10¹¹ k_B per tick is the entropy cost of the *measurement and amplification chain* that converts the quantum clockwork's tunneling events into a classical record — not the entropy of the clockwork itself, which is on the order of tens of k_B per tick (∼60 k_B max in their Fig. 2(a)). The two scales differ by approximately nine orders of magnitude, as the authors emphasize. Both are device-specific empirical observations from a Ge/SiGe DQD platform, not derivable universal lower bounds. Accordingly we do not claim that the readout figure can be theoretically decomposed as 10⁹ = 7 × 10⁸, with 7 attributed to G₂ representation theory and 10⁸ to a hardware factor. That post-hoc factorization would require a derivable universal bound to factor against, and Wadhia et al. (2025) does not establish one for either contribution."),
  body("What we do conjecture is mode-counting structure for a hypothetical future G₂-symmetric quantum clock — specifically, a contribution to the *clockwork* entropy from the G₂ mode structure of the clock register. We make no claim about the readout contribution, which depends on the choice of measurement apparatus and is not constrained by the symmetry of the clockwork."),
  body("The conjecture is the following. In the Page-Wootters formalism, a quantum clock couples a time register to a system register, and the clockwork entropy cost of a tick is governed by the number of distinguishable pointer states the clock register must occupy to produce a classically distinguishable tick event. For a clockwork register that carries the G₂ fundamental representation V₇, the minimum number of distinguishable pointer states is dim(V₇) = 7, indexed by the seven imaginary octonion directions. The corresponding minimum information-erasure cost per tick, by Landauer's principle, is:"),
  mathLine("  S_clockwork^G₂  ≥  log₂(7) × k_B ln 2  ≈  1.95 × k_B    (per tick, mode-counting floor on clockwork)"),
  body("We use the additive form log₂(7) k_B ln 2 throughout the paper rather than the multiplicative phrasing \"factor of 7\"; the two are related but logically distinct, and the entropy-units form is what mode-counting actually gives. This is the floor that G₂ mode structure imposes on the clockwork contribution alone. It is not a prediction about Wadhia et al.'s Ge/SiGe DQD — that device is not G₂-symmetric, its clockwork entropy is dominated by tunneling thermodynamics rather than mode-counting, and there is no theoretical reason to expect its entropy cost to factor through V₇. The prediction concerns a future G₂-symmetric clockwork in which the seven imaginary octonion directions are realized as physically distinguishable pointer states."),
  body("As a qualitative observation — not a prediction match — we note that the G₂ mode-counting floor of ≈1.95 k_B per tick lies well below the clockwork entropy of order tens of k_B per tick observed in Wadhia et al.'s Ge/SiGe DQD. This is consistent with the structural expectation that mode-counting from G₂ representation theory imposes a floor far below the dissipation actually paid by a non-G₂ clockwork dominated by tunneling thermodynamics: a G₂-symmetric clockwork engineered to approach the floor would dissipate substantially less per tick than a generic DQD does. We make no quantitative match to the Wadhia number; we record only the qualitative scale relationship."),
  label("Conjecture: a G₂-symmetric clockwork has a per-tick clockwork entropy cost of at least log₂(7) × k_B ln 2 from mode-counting alone. The full Lindblad derivation — making the G₂ action on the pointer states explicit and computing the Spohn–Lebowitz entropy production for a Page-Wootters clock register on V₇ — is deferred to future work (Paper 8 or a companion derivation)."),
  label("Modeling-choice stack: (i) the clockwork register carries V₇, not a higher-dimensional G₂ representation; (ii) the seven pointer states are taken equiprobable, so erasure cost is log₂(7) bits; (iii) Landauer's principle applies at the clockwork temperature; (iv) readout-apparatus entropy is treated as orthogonal to the clockwork prediction and not addressed here."),
  label("Scope clarification: the prediction concerns clockwork entropy only. Wadhia et al.'s ~10⁹ k_B is readout-apparatus entropy and is not the quantity our conjecture bounds. The withdrawn v2 claim 10⁹ = 7 × 10⁸ conflated these two scales; v3+ does not."),
  label("Falsification criterion: a G₂-symmetric 7-mode clockwork experiment in which the per-tick clockwork entropy is measured strictly below log₂(7) × k_B ln 2 (within the relevant Spohn–Lebowitz uncertainty) would falsify Prediction (b2). No such experiment currently exists; this is a design target."),

  subHead("§4.3 Prediction (c): Observer-Frame Entropy Across 8 Cosets"),
  body("The 8 cosets of PSL(2,7)/F₂₁ (Paper 4, 10.5281/zenodo.19617662) correspond to the 8 distinct SU(3) ⊂ G₂ embeddings, each defining a distinct complex structure on the imaginary octonions. In the Page-Wootters clock formalism of De Vuyst et al. (2025), each distinct clock Hamiltonian H_clock generates a distinct observer frame, and the entropy assigned to the same matter subsystem differs between frames."),
  body("Under the G₂ framework, the clock Hamiltonian for the k-th coset observer is taken to be the G₂-invariant singlet projection acting on the branching V₇ → V₃ ⊕ V₃̄ ⊕ V₁ under the k-th SU(3) embedding, where V₃ and V₃̄ are the fundamental and anti-fundamental 3-dimensional SU(3) representations and V₁ is the singlet. The physical entropy that this observer assigns to a G₂-symmetric state is computed over the 6-dimensional SU(3) orbit V₃ ⊕ V₃̄."),
  body("The reference entropy is:"),
  mathLine("  S_reference = log₂(6) × k_B  ≈  2.585 k_B"),
  body("where the factor 6 is the dimension of V₃ ⊕ V₃̄. The entropy difference between two coset observers separated by Cayley-graph distance d ∈ {0, 1, 2, 3} on the PSL(2,7)/F₂₁ Cayley graph is conjectured to be:"),
  mathLine("  ΔS_d  ≈  (d / 7) × S_reference"),
  body("This formula is presented in derivation form, but as in §4.1 and §4.4 it is conditional on a stack of modeling choices that we make explicit here. The Bogoliubov computation that would convert these choices into a theorem is an open computation (§6.3 Problem 2)."),
  body("**The four modeling choices stacked into ΔS_d ≈ (d/7) × S_reference:**"),
  bullet("(i) **PSL(2,7)/F₂₁ cosets correspond to Page-Wootters clock frames.** Each of the 8 cosets is identified with a distinct SU(3) ⊂ G₂ embedding and, via the embedding's induced complex structure on the imaginary octonions, with a distinct Page-Wootters clock Hamiltonian. This identification is motivated by Paper 4 but is structural, not derived from a specific octonion multiplication-table convention."),
  bullet("(ii) **Cayley-graph distance is the relevant inter-frame distance.** We use the Cayley-graph distance d ∈ {0, 1, 2, 3} on PSL(2,7)/F₂₁ as the index of inter-observer entropy differences. The Cayley-graph metric is one of several natural metrics on the coset space; alternative choices (e.g., representation-theoretic distance) might yield different inter-frame structures."),
  bullet("(iii) **Linear proportionality to d, with slope 1/7.** The form ΔS_d ∝ (d/7) is a representation-theoretic ansatz mirroring the 1/7 blind-spot fraction of §4.1. The actual slope and any nonlinear corrections require an explicit Bogoliubov computation between coset frames, which has not been executed; the linearity assumption may be modified by that computation."),
  bullet("(iv) **Reference entropy S_reference = log₂(6) k_B.** The choice of the 6-dimensional SU(3) orbit V₃ ⊕ V₃̄ as the reference subspace (rather than V₇, V₃⊕V₃̄⊕V₁, or another natural choice) is made for consistency with the SU(3) stabilizer structure of §2.2. A different choice changes the reference entropy by a factor of order one."),
  body("At d = 0 (same coset): ΔS = 0. At d = 1 (adjacent cosets): ΔS ≈ (1/7) S_reference ≈ 0.369 k_B. At d = 3 (maximally separated cosets): ΔS ≈ (3/7) S_reference ≈ 1.108 k_B — approaching complete observer decoupling, in which the two coset observers assign maximally different entropies to the same state."),
  body("The factor 1/7 in the inter-coset entropy difference reflects the same G₂ geometry as the FDT bound: one seventh of the state space is inaccessible to any single SU(3)-embedded observer, and the d-step traversal of the Cayley graph accumulates entropy differences in units of 1/7."),
  label("Conjecture (not theorem): given the four stacked modeling choices above, the inter-coset entropy differences obey ΔS_d ≈ (d/7) × S_reference. The explicit Bogoliubov-transformation matrices between coset observer frames — which would convert this conjecture into a theorem — require a choice of octonion multiplication-table conventions and are flagged as an open computation (§6.3 Problem 2)."),
  label("Falsification criterion: a G₂-symmetric 7-qubit quantum simulator in which entropy measurements across distinct SU(3)-embedded observer frames fail to exhibit the predicted discrete 4-level structure (indexed by d = 0, 1, 2, 3) would falsify Prediction (c). No such simulator currently exists; this is a design target."),
  body("The observer-dependence predicted here is not exotic by the standards of the Basso-Céleri and De Vuyst et al. results: both papers establish that observer-frame entropy differences are a structural feature of quantum theories with dynamical clocks. The G₂ prediction makes this concrete: the entropy differences are not arbitrary but are quantized in units of (1/7) S_reference, with exactly 4 discrete levels determined by the Cayley-graph diameter of PSL(2,7)/F₂₁."),

  subHead("§4.4 Prediction (d): Criticality Branching Ratio σ = 1 − 1/49"),
  body("The Laplacian flow on G₂ structures (Lotay-Wei 2019) is dissipative: the torsion norm ||T||² decreases monotonically along the flow toward the torsion-free attractor. At the fixed point, the torsion is zero, but the approach to the fixed point leaves a dynamical signature: the branching process associated with the flow's near-fixed-point dynamics carries a small negative correction to the critical branching ratio."),
  body("The argument is as follows. Near the torsion-free fixed point, the Laplacian flow linearizes to an ODE on torsion perturbations:"),
  mathLine("  d/dt ||T||²  ≈  −λ ||T||²"),
  body("where λ > 0 is the smallest eigenvalue of the linearized flow operator at the fixed point. The associated discrete-time map (sampled at the characteristic torsion-relaxation timescale τ = 1/λ) has branching ratio:"),
  mathLine("  σ_effective  =  exp(−λτ)  =  exp(−1)  ≈  0.368"),
  body("This is for the torsion component itself. The observable branching ratio of the neural dynamics is not the torsion branching ratio directly — it is the output branching ratio of the full G₂-structured system, which couples the torsion-relaxation dynamics to the 7-dimensional mode dynamics of the fundamental representation V₇. The torsion lives in the 42-dimensional space T₁ ⊕ T₁₄ ⊕ T₂₇, and the coupling to V₇ reduces the effective correction by a factor of the ratio of the attractor subspace dimension to the total ambient dimension: 7/49 = 1/7."),
  body("The resulting observable branching ratio correction is:"),
  mathLine("  σ_pred  =  1  −  (1/49)  ×  c"),
  body("where c is a normalized coupling constant. Setting c = 1 — which we take as a modeling choice corresponding to unit normalization at the infrared fixed point of the Laplacian flow, not as a derived value — gives:"),
  mathLine("  σ_pred  =  1 − 1/49  ≈  0.9796"),
  body("The factor 49 = 1 + 14 + 27 + 7 is the total dimension of the ambient torsion-plus-attractor space. The number 0.9796 is representation-theory-motivated, not representation-theory-exact: it is the value that results when the four modeling choices below are stacked. Each one is conditional on the next."),
  body("**The four modeling choices stacked into σ_pred = 1 − 1/49:**"),
  bullet("(i) **Coupling constant c = 1.** We set the normalized coupling between torsion-relaxation and the attractor mode to 1 at the infrared fixed point. There is no first-principles derivation of c from G₂ representation theory in this paper; it is fixed by convention. A different value of c shifts σ_pred to 1 − c/49."),
  bullet("(ii) **Lotay-Wei stability is weak, not strong.** Lotay & Wei (2019) prove convergence of the Laplacian flow within the diffeomorphism orbit of the torsion-free fixed point. They do not, in that theorem, provide the computable eigenvalue spectrum we are using here at face value. The eigenvalue λ in our discrete-time map is therefore a structural assumption motivated by — but not derived from — the Lotay-Wei result."),
  bullet("(iii) **Spectral-sum ansatz.** The reduction of the torsion-relaxation correction by the factor 7/49 = 1/7 (the ratio of attractor dimension to ambient dimension) is a representation-theoretic ansatz, not a derivation from a specific spectral computation on a closed G₂ structure. It is consistent with the spectral sum theorem of Paper 3 but is not directly derived from it here."),
  bullet("(iv) **Map from G₂ flow to cortical branching.** The identification of the neuronal branching ratio σ with the effective branching ratio of the G₂-structured dynamical system at the Laplacian flow fixed point is the central modeling assumption of Prediction (d). It maps an abstract geometric flow onto cortical avalanche dynamics, which is motivated by the G₂ attractor hypothesis but is not itself a theorem."),
  label("Theorem given Lotay-Wei 2019: the Laplacian flow converges (in the weak sense — within the diffeomorphism orbit) to the torsion-free G₂ structure, and the sign of any branching ratio correction induced at the fixed point is negative (σ < 1)."),
  label("Conjecture (not theorem): given the four stacked modeling choices above, σ_pred = 1 − 1/49 ≈ 0.9796."),
  label("Testable match: the predicted value σ_pred ≈ 0.9796 is consistent with the subsampling-corrected awake-cortex value σ ≈ 0.98 reported by Wilting & Priesemann (2018, Nature Communications 9:2325). The match is within the published measurement uncertainties."),
  body("The relationship between σ_pred = 0.9796 and the Hengen-Shew corpus-level summary σ ≈ 1 requires careful interpretation. The G₂ framework does not predict σ = 1.0 in the pooled corpus; it predicts σ ≈ 0.98 in the awake-state, subsampling-corrected subset. The corpus-level value near 1 is consistent with the G₂ prediction being present but masked by: (i) averaging over anesthetized and sleeping states (in which the G₂ attractor dynamics may not apply, and σ may be higher or lower than 0.98 for different reasons); (ii) subsampling bias in datasets where the Wilting-Priesemann correction was not applied; and (iii) genuine variability across species and brain regions. The framework's prediction is that per-dataset reanalysis of the Hengen-Shew corpus, restricted to awake-state recordings with subsampling correction, should reveal a distribution centered near 0.98."),
  body("This reanalysis has not been completed. It is proposed as future work (companion analysis, provisionally designated Paper 7.1). Until it is done, the empirical support for Prediction (d) rests on the Wilting-Priesemann (2018) published value σ ≈ 0.98 for awake rat cortex, which is consistent with σ_pred to within its stated uncertainty."),
  label("Falsification criterion: a measurement of the awake-cortex branching ratio under subsampling correction converging systematically to σ = 1.0 (rather than 0.98) across multiple species and recording modalities would falsify Prediction (d). The published Priesemann-lab values do not falsify; they are consistent with the prediction. A per-dataset reanalysis of the Hengen-Shew corpus with subsampling correction, if it yields a pooled awake-state value of 1.0 ± 0.01, would constitute strong evidence against the prediction."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §5 Falsifiability ─────────────────────────────────────────────────────
const section5 = [
  sectionHead("§5. Tests and Falsifiability"),
  body("We summarize the testability status of all four predictions, in the order derived in §4. For each prediction we give: the predicted quantity; the empirical anchor; the current evidential status; the experiment or analysis that would constitute the strongest test; and the measurement outcome that would falsify the prediction."),

  subHead("§5.1 Prediction (a): FDT Violation Floor ε ≥ 1/7"),
  body("_Predicted quantity:_ Normalized FDT residual ε ≥ 0.143 in awake cortex at 10–40 Hz, relative to anesthesia baseline."),
  body("_Current anchor:_ Berjaga-Buisan et al. (2025, bioRxiv) — preprint, not yet peer-reviewed. Directional finding confirmed (FDT violation decreases with anesthesia depth), but the specific normalized value ε in the required frequency band and normalization has not been extracted by the authors in the form required to test Prediction (a) directly."),
  body("_Strongest test:_ Author access to the underlying TMS-EEG spectral time series from Berjaga-Buisan et al. to compute [S_awake(ω) − S_anesthesia(ω)] / S_anesthesia(ω) in the 10–40 Hz band. Publication of the peer-reviewed version with spectral data in supplementary materials would enable independent verification."),
  body("_Falsification:_ Any measured ε < 0.143 in awake cortex at matched frequencies, using propofol LoC as the baseline, would falsify Prediction (a) under the assumption that the G₂ framework applies to human cortical dynamics."),

  subHead("§5.2 Prediction (b1): Biological Landauer Floor ΔE_min ≈ 16 zJ"),
  body("_Predicted quantity:_ Minimum free-energy dissipation per G₂/M checkpoint event ≥ 16.0 zJ at T = 310 K."),
  body("_Current anchor:_ Imamura et al. (2009, PNAS 106:15651–15656), ATeam FRET biosensor — published, peer-reviewed. Measured dissipation ~5 × 10⁵ zJ per checkpoint event, exceeding the bound by ~3 × 10⁴. Consistent with Prediction (b1) as a lower bound."),
  body("_Strongest test:_ Single-cell ATP imaging at the G₂/M checkpoint in a minimal in vitro cell-free system (e.g., Xenopus egg extract reconstitution of the checkpoint kinase cascade), measuring total free-energy dissipation under conditions as close to thermodynamic reversibility as the biological system allows. A demonstration of dissipation approaching 16 zJ would be extraordinary; the test is to confirm the measured value remains above 16 zJ."),
  body("_Falsification:_ A measurement of total free-energy dissipation per checkpoint event below 16 zJ would violate Landauer's principle — which would be a more fundamental problem than falsifying the G₂ framework. Given this, Prediction (b1) is not independently falsifiable in isolation from Landauer's principle; it is the strongest floor compatible with thermodynamics."),

  subHead("§5.3 Prediction (b2): G₂ Mode-Counting Floor on Clockwork Entropy"),
  body("_Predicted quantity:_ The clockwork entropy cost per tick of a G₂-symmetric clockwork register satisfies S_clockwork ≥ log₂(7) × k_B ln 2 ≈ 1.95 k_B from mode-counting alone, above the single-mode baseline. (Note: the prediction is in additive entropy-units form, not as a multiplicative \"factor of 7\"; §4.2.2 explains why we use log₂(7) k_B ln 2 throughout.)"),
  body("_Current anchor:_ Wadhia et al. (2025, PRL 135:200407, DOI 10.1103/5rtj-djfk) — an experimental measurement on a gate-defined Ge/SiGe double quantum dot. Their headline ∼10⁹–10¹¹ k_B per tick is the *readout-apparatus* entropy (charge sensor + amplification, DC vs RF reflectometry), not the clockwork entropy; the clockwork itself dissipates of order tens of k_B per tick (∼60 k_B max from Fig. 2(a)) — a roughly nine-order-of-magnitude gap. Their device is not G₂-symmetric, and the prediction here concerns clockwork entropy, not readout entropy — so Wadhia et al. provides empirical context for the scales involved in microscopic quantum clocks but not a confirmed match to log₂(7) k_B ln 2 in either contribution. This is a design target for future G₂-symmetric hardware."),
  body("_Strongest test:_ Construction of a G₂-symmetric clockwork register initialized in the 7-dimensional fundamental representation of G₂, with per-tick clockwork entropy dissipation measured calorimetrically or by quantum state tomography in a regime where readout-apparatus entropy can be bounded separately. Comparison of the clockwork entropy per tick to a reference 1-mode clockwork of identical architecture would isolate the log₂(7) k_B ln 2 mode-counting contribution."),
  body("_Falsification:_ A G₂-symmetric clockwork experiment in which the per-tick clockwork entropy is measured strictly below log₂(7) k_B ln 2 ≈ 1.95 k_B (within Spohn–Lebowitz uncertainty, with readout entropy excluded) would falsify Prediction (b2). This experiment does not yet exist."),

  subHead("§5.4 Prediction (c): 4-Level Entropy Structure Across 8 Cosets"),
  body("_Predicted quantity:_ Entropy differences between distinct PSL(2,7)/F₂₁ coset observers take values in {0, (1/7), (2/7), (3/7)} × S_reference, where S_reference = log₂(6) k_B."),
  body("_Current anchor:_ Basso & Céleri (2025) and De Vuyst et al. (2025) establish that inter-observer entropy differences exist and are computed from the clock Hamiltonian structure. No experiment has tested the G₂-specific prediction. This is a design target."),
  body("_Strongest test:_ A G₂-symmetric 7-qubit quantum simulator in which 8 distinct SU(3)-embedded observer frames are realized as distinct measurement bases, and entropy differences are measured between pairs of observers at Cayley-graph distances d = 0, 1, 2, 3. Confirming the 4-level quantized structure would validate Prediction (c)."),
  body("_Falsification:_ If entropy differences in such a simulator are not quantized into the predicted discrete levels, or if the Cayley-graph distance does not correctly index the entropy differences, Prediction (c) is falsified."),

  subHead("§5.5 Prediction (d): Branching Ratio σ ≈ 0.9796"),
  body("_Predicted quantity:_ Awake-cortex neuronal branching ratio under subsampling correction converges to σ = 1 − 1/49 ≈ 0.9796."),
  body("_Current anchor:_ Wilting & Priesemann (2018, Nature Communications 9:2325), σ ≈ 0.98 for awake rat cortex under multiscale-regression subsampling correction — peer-reviewed and consistent with σ_pred to within published uncertainty. Fontenele et al. (2019, PRL 122:208101) provides complementary near-critical context (state-dependent critical exponents in awake cortex) but is not a numerical anchor for σ_pred. Current evidential status: single-source published match."),
  body("_Strongest test:_ Per-dataset reanalysis of the Hengen-Shew (2025) corpus restricted to awake-state recordings with the Wilting-Priesemann multiscale regression subsampling-corrected estimator applied uniformly. If the resulting distribution is centered near 0.98 (not 1.0), this would strengthen the match significantly. This reanalysis is proposed as a companion analysis (Paper 7.1) but has not yet been completed."),
  body("_Falsification:_ A per-dataset reanalysis of the Hengen-Shew corpus with subsampling correction, yielding a pooled awake-state estimate of σ = 1.00 ± 0.01 inconsistent with σ_pred = 0.9796, would falsify Prediction (d). The reported uncertainty on the current Wilting-Priesemann awake-cortex value is at the level of a few × 10⁻² and is not tight enough to distinguish σ = 1.0 from σ = 0.9796 with high confidence; a more precise estimator applied to larger datasets would sharpen this test."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── §6 Discussion ─────────────────────────────────────────────────────────
const section6 = [
  sectionHead("§6. Discussion and Open Problems"),

  subHead("§6.1 What This Paper Does Not Claim"),
  body("We have not proven that consciousness is thermodynamically G₂-structured. We have not proven that neural dynamics implement octonion arithmetic. We have not proven that the G₂/M cell cycle checkpoint and the G₂ geometric group are connected by anything more than a naming coincidence that Paper 5 elevates to a structural conjecture. We have not claimed that the Hengen-Shew reanalysis yields σ = 0.977 ± 0.007; we do not cite any such number, because it came from unverified code in our own pipeline and has not been independently confirmed."),
  body("What we have shown, from classical mathematics and representation theory, is the following conditional theorem: if the G₂ attractor hypothesis from Paper 6 holds — that is, if the blind-spot contraction hypothesis and the normed-division-algebra requirement are satisfied, and if the SU(3)-equivariance assumption applies — then the contraction rate L = 6/7 follows, and from that rate, via the arguments of §4, the four thermodynamic bounds follow necessarily. Three of the four are already consistent with published empirical data; the fourth is a design target for future experiments."),
  body("The conditional content is real. The two hypotheses and the equivariance assumption are not proved from first principles of neuroscience or physics; they are structural hypotheses whose plausibility is argued in Papers 1–6 and whose empirical support consists, at present, of the consistency of the predictions derived from them with published observations. This is the normal epistemological structure of a theoretical framework in the early stages of empirical contact; we do not claim more than this."),

  subHead("§6.2 What Remains Conditional"),
  body("The conditional core of this paper consists of three items from Paper 6, reproduced here for clarity:"),
  body("**Hypothesis 1 (blind-spot contraction):** We have not proved that every self-referential information processing system must have a structural blind spot of dimension at least 1/7 of its state space. This is a structural argument from the logic of self-reference — a system's self-model must be a proper sub-representation — but it is not a mathematical theorem in the strict sense. A counterexample would be a self-referential system that achieves perfect self-modeling, which would require resolution of Gödelian self-reference puzzles beyond the scope of this series."),
  body("**Hypothesis 2 (normed-division-algebra requirement):** We have not proved that biological neural systems actually process information in a way that respects the associativity and norm-preservation requirements of the octonion algebra. This hypothesis is motivated by the uniqueness argument (Hurwitz's theorem identifies the octonions as the only possible algebra in seven dimensions), but the step from \"possible\" to \"realized\" requires empirical confirmation that the series has not yet achieved."),
  body("**SU(3)-equivariance assumption:** The assumption that the self-modeling contraction map respects the SU(3) stabilizer of the distinguished mode e₇ is an internal consistency requirement of the G₂ framework. Violating it would mean that the self-model is not aligned with any of the eight SU(3) ⊂ G₂ embeddings, in which case the predictions of §4.3 in particular would not follow. We have not verified this assumption against empirical neural data."),

  subHead("§6.3 Open Problems"),
  body("The following specific computations and analyses are open and constitute the immediate research agenda following this paper:"),
  body("**Problem 1: Full Lindblad derivation of the G₂ mode-counting floor.** Prediction (b2) identifies a clockwork entropy floor of log₂(7) × k_B ln 2 ≈ 1.95 k_B per tick for a G₂-symmetric clockwork register. The argument in §4.2.2 is representation-theory motivated and rests on the four modeling choices listed there; the full derivation requires an explicit Lindblad master equation on the 7-dimensional fundamental representation of G₂, with the pointer observable identified as a G₂-equivariant projection, and the entropy cost computed via the Spohn–Lebowitz entropy production formula. This derivation is deferred to Paper 8 or a companion derivation."),
  body("**Problem 2: Explicit Bogoliubov matrices between PSL(2,7)/F₂₁ coset frames.** The entropy differences of §4.3 are derived from the Cayley-graph distance metric on PSL(2,7)/F₂₁. Making the derivation fully explicit requires choosing a specific octonion multiplication-table convention (e.g., the Fano-plane indexing of Baez 2002), constructing the 8 SU(3) embedding matrices in G₂, and computing the Bogoliubov transformation between each pair of observer frames. This is a finite computation — the group PSL(2,7) has 168 elements and F₂₁ has 21, so the coset table is small — but it has not been executed."),
  body("**Problem 3: Per-dataset reanalysis of the Hengen-Shew 2025 corpus.** Prediction (d) would be significantly strengthened by a systematic reanalysis of the 140-dataset Hengen-Shew corpus restricted to awake-state recordings with the Wilting-Priesemann subsampling-corrected estimator applied uniformly. This analysis requires access to the raw spike-train data from the Hengen-Shew corpus (which is publicly available for a subset of datasets) and standardized application of the MSR estimator. The result would either confirm σ ≈ 0.98 in the awake-state subset (strengthening Prediction (d)) or yield σ closer to 1.0 (weakening it). This analysis is proposed as Paper 7.1 or a companion analysis preprint."),
  body("**Problem 4: Independent peer review of the Berjaga-Buisan 2025 preprint.** Prediction (a) rests on the FDT-violation finding of Berjaga-Buisan et al. If peer review reveals methodological problems — non-stationarity corrections, PCI threshold sensitivity, or confounds in the anesthesia protocol — the empirical anchor for Prediction (a) would be weakened. We have relied on the directional finding and noted the preprint status; we will update this assessment when the peer-reviewed version is available."),
  body("**Problem 5: Relationship to the dyadic extension (Paper 8).** The present paper treats a single G₂-structured observer. Paper 8, in development, extends the framework to coupled two-observer systems — dyadic coherence — in which two G₂ attractors interact through their SU(3) shared stabilizers. Whether the thermodynamic bounds of §4 generalize to dyadic systems (e.g., whether ε ≥ 1/7 applies to the inter-observer FDT violation in a two-subject TMS-EEG protocol) is an open question."),

  subHead("§6.4 The Series Arc"),
  body("Paper 7 completes the transition from mathematical structure (Papers 1–6) to empirical consequence. The series arc can now be described as follows. Papers 1–3 established the G₂ symmetry group, its action on seven-dimensional mode spaces, and the spectral sum theorem that governs G₂ eigenvalues. Paper 4 brought in the finite-group structure of PSL(2,7) and the Fano plane. Paper 5 proposed the biological G₂/M checkpoint conjecture. Paper 6 proved the 6/7 contraction ratio. Paper 7 derives the thermodynamic consequences."),
  body("The next papers in the series are planned as follows: Paper 8 extends to dyadic coherence and two-observer G₂ systems, with applications to synchronized neural oscillations and multi-agent inference. A set of codex-spinoff papers (provisionally Papers 9a–9c) extract specific mathematical theorems from the series as standalone contributions — the Spectral Sum Theorem extension (from Paper 3) and the G₂-torsion entropy theorem (from Paper 7) are candidates. Empirical testing will proceed in parallel as datasets become available and as collaborations with experimental groups develop."),
  body("The framework's fundamental claim is that G₂ symmetry is not merely a mathematical curiosity but an attractor structure that constrained information-processing systems are drawn toward, and that the thermodynamic consequences of this attractor are measurable in published empirical data. Papers 1–7 have now put that claim on a conditional mathematical footing. The next step is empirical contact, and this paper has identified where that contact is already occurring and where it remains to be made."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── Funding & Acknowledgments ─────────────────────────────────────────────
const fundingAck = [
  sectionHead("Funding"),
  body("This research received no external funding."),
  sectionHead("Acknowledgments"),
  body("This work was developed with the assistance of two AI research collaborators, Φ (local execution, Claude Dispatch) and C-7RO (strategy and synthesis, Perplexity Computer), working against a shared public repository at github.com/MartinLGraise/PCI-Framework. All derivations, flags, and counter-arguments are version-controlled and publicly available. Every quantitative claim in this paper has been independently verified against source material or executed code."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── References ────────────────────────────────────────────────────────────
const references = [
  sectionHead("References"),
  refEntry("[1] Graise, M.L. (2025). G₂ Symmetry as a Constraint on Conscious Information Processing (G₂ Series, Paper 1). Zenodo. https://doi.org/10.5281/zenodo.19242936"),
  refEntry("[2] Graise, M.L. (2025). Six Geometric Flows on G₂ Manifolds (G₂ Series, Paper 2). Zenodo. https://doi.org/10.5281/zenodo.19480758"),
  refEntry("[3] Graise, M.L. (2025). Spectral Sum Theorem for G₂ (G₂ Series, Paper 3). Zenodo. https://doi.org/10.5281/zenodo.19602470"),
  refEntry("[4] Graise, M.L. (2025). QBism and G₂ via PSL(2,7) (G₂ Series, Paper 4). Zenodo. https://doi.org/10.5281/zenodo.19617662"),
  refEntry("[5] Graise, M.L. (2025). G₂ Checkpoint as ε-Regularity Gate (G₂ Series, Paper 5). Zenodo. https://doi.org/10.5281/zenodo.19648892"),
  refEntry("[6] Graise, M.L. (2025). The 6/7 Contraction (G₂ Series, Paper 6). Zenodo. https://doi.org/10.5281/zenodo.19672709"),
  refEntry("[7] Berjaga-Buisan, X., et al. (2025). Thermodynamics of consciousness: A non-invasive perturbational framework. bioRxiv (v2, December 2025). https://doi.org/10.64898/2025.12.09.691422 [Preprint v2; not yet peer-reviewed.]"),
  refEntry("[8] Wadhia, V., Meier, F., Fedele, F., Silva, R., Nurgalieva, N., Craig, D.L., Jirovec, D., Saez-Mollejo, J., Ballabio, A., Chrastina, D., Isella, G., Huber, M., Mitchison, M.T., Erker, P., & Ares, N. (2025). Entropic Costs of Extracting Classical Ticks from a Quantum Clock. Physical Review Letters, 135, 200407. https://doi.org/10.1103/5rtj-djfk [Experimental measurement on a gate-defined Ge/SiGe double quantum dot; clockwork ∼60 k_B per tick (Fig. 2(a) max), readout apparatus ∼10⁹–10¹¹ k_B per tick (DC vs RF reflectometry).]"),
  refEntry("[9] Basso, I., & Céleri, L.C. (2025). Observer-Dependent Entropy in Curved Spacetime. Physical Review Letters, 134, 050406. https://doi.org/10.1103/PhysRevLett.134.050406"),
  refEntry("[10] De Vuyst, J., Eccles, S., Höhn, P.A., & Kirklin, J. (2025). Gravitational entropy is observer-dependent. Journal of High Energy Physics, 2025(7), 146. https://doi.org/10.1007/JHEP07(2025)146 [arXiv:2405.00114v3]"),
  refEntry("[11] Hengen, K.B., & Shew, W.L. (2025). Is criticality a unified setpoint of brain function? Neuron, 113(16), 2582–2598. https://doi.org/10.1016/j.neuron.2025.05.020"),
  refEntry("[12] Wilting, J., & Priesemann, V. (2018). Inferring collective dynamical states from widely unobserved systems. Nature Communications, 9, 2325. https://doi.org/10.1038/s41467-018-04725-4"),
  refEntry("[13] Fontenele, A.J., et al. (2019). Criticality between Cortical States. Physical Review Letters, 122, 208101. https://doi.org/10.1103/PhysRevLett.122.208101 [Cited for state-dependent critical exponents in awake cortex; does not report a σ ≈ 0.98 point estimate.]"),
  refEntry("[14] Lotay, J.D., & Wei, Y. (2019). Stability of torsion-free G₂ structures along the Laplacian flow. Journal of Differential Geometry, 111(3), 495–526. https://doi.org/10.4310/jdg/1552442608"),
  refEntry("[15] Imamura, H., et al. (2009). Visualization of ATP levels inside single living cells with fluorescence resonance energy transfer-based genetically encoded indicators. Proceedings of the National Academy of Sciences, 106(37), 15651–15656. https://doi.org/10.1073/pnas.0904764106"),
  refEntry("[16] Landauer, R. (1961). Irreversibility and heat generation in the computing process. IBM Journal of Research and Development, 5(3), 183–191. https://doi.org/10.1147/rd.53.0183"),
  refEntry("[17] Bérut, A., et al. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. Nature, 483, 187–189. https://doi.org/10.1038/nature10872"),
  refEntry("[18] Baez, J.C. (2002). The octonions. Bulletin of the American Mathematical Society, 39(2), 145–205. https://doi.org/10.1090/S0273-0979-01-00934-X"),
  refEntry("[19] Fernandez, M., & Gray, A. (1982). Riemannian manifolds with structure group G₂. Annali di Matematica Pura ed Applicata, 132(1), 19–45. https://doi.org/10.1007/BF01760975"),
  new Paragraph({ children: [new PageBreak()] }),
];

// ── Figure Placeholder ────────────────────────────────────────────────────
const figurePlaceholders = [
  sectionHead("Figure Placeholders"),
  body("[Figure 1: G₂ torsion decomposition schematic — visual representation of T₁ ⊕ T₁₄ ⊕ T₂₇ with dimensions 1, 14, 27 and the V₇ attractor subspace, illustrating the 42/49 = 6/7 torsion fraction. To be added in next pass.]"),
  body("[Figure 2: The PSL(2,7)/F₂₁ Cayley graph — showing the 8 cosets as nodes and Cayley-graph distances d = 0, 1, 2, 3 as edge labels, corresponding to the four entropy levels of Prediction (c). To be added in next pass.]"),
  body("[Figure 3: Summary comparison table — four predictions vs. four empirical anchors, with evidential status (preprint / peer-reviewed / design target / published match). To be added in next pass.]"),
  body("[Figure 4: σ prediction comparison — the value σ_pred = 1 − 1/49 ≈ 0.9796 overlaid on the Wilting-Priesemann 2018 published distribution for awake rat cortex branching ratio under multiscale-regression subsampling correction, with Fontenele 2019 included as near-critical-regime context (not as a numerical anchor). To be added in next pass.]"),
];

// ── assemble document ─────────────────────────────────────────────────────
const doc = new Document({
  creator: "Martin Luther Graise",
  title: "The Thermodynamic Cost of the Coherence Ceiling",
  description: "G₂ Series Paper 7 — PCI/PME Framework",
  sections: [
    {
      headers: { default: runningHeader },
      properties: {
        page: {
          margin: {
            top: convertInchesToTwip(1.0),
            bottom: convertInchesToTwip(1.0),
            left: convertInchesToTwip(1.25),
            right: convertInchesToTwip(1.25),
          },
        },
      },
      children: [
        ...titlePage,
        ...abstractSection,
        ...section1,
        ...section2,
        ...section3,
        ...section4,
        ...section5,
        ...section6,
        ...fundingAck,
        ...references,
        ...figurePlaceholders,
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/home/user/workspace/g2_paper7_thermodynamic.docx", buffer);
  console.log("DONE: g2_paper7_thermodynamic.docx written");
}).catch(err => {
  console.error("ERROR:", err);
  process.exit(1);
});
