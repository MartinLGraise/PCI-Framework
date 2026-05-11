# Negative Pressure as Intersubjective Residence-Pathology

**Date:** 2026-05-10
**Status:** INTERNAL FRAMEWORK MEMO. Formalization document. Connects
phenomenological observation to Paper 12 NP-pumping language and
Paper 14 cross-substrate residence-pathology grammar.
**Authors:** Martin L. Graise (phenomenological observation,
original formalization, framework integration) + Computer
(equation candidate, experiment design)

## Phenomenological ground truth

Two paradigm examples, both verifiable on demand:

**Example 1 (intra-personal anchor).** A person sings a song aloud,
then in the middle of a phrase stops abruptly and holds the silence
while staying physically present and engaged with the song's
trajectory. A felt pressure begins immediately and accumulates over
seconds. The pressure is not "discomfort" generically — it has
direction (toward resumption), it has magnitude (grows with hold
duration), and it has discharge channels (resume the song, laugh,
break frame explicitly).

**Example 2 (inter-personal, load-bearing).** Two people in
conversation. Speaker A is mid-sentence. Speaker A stops without
finishing the sentence, without changing facial expression or body
language, and holds. Both A and B feel a pressure that builds. The
pressure is felt by both parties even though only one is producing
it. Neither party can resolve it by individual will; it resolves
only when A continues, when one party explicitly breaks frame, or
when the coupled state decays into "the conversation died."

## Four structural features of negative pressure

The phenomenon has a specific structural signature, not just a felt
quality:

1. **It is produced by withholding, not by acting.** Normal
   ("positive") pressure comes from force applied. Negative pressure
   comes from force expected and then not delivered. The receiving
   system had already allocated processing resources to continue
   parsing the trajectory.

2. **It is felt by both parties on the coupled substrate.** This is
   the load-bearing observation. The pressure is not in either
   person individually but in the coupled expectation structure
   between them. Neither can resolve it alone.

3. **It accumulates with hold duration.** The pressure starts at
   zero and integrates upward. This is a dynamical-system signature
   (integration against a decay), not a snapshot phenomenon.

4. **It has discharge channels.** The pressure wants to resolve.
   Three primary channels: resumption of the original trajectory,
   alternate-channel discharge (laugh, topic change, explicit
   acknowledgment), or decoherence (the coupled state breaks).

## Connection to Paper 12 NP-pumping language

Paper 12's thesis document (`outbox/paper12/paper12_thesis_gradual_tear.md`)
already formalizes NP at a different scale:

> "When the dyad is human-AI specifically (rather than two abstract
> Banach observers), the fixed point's θ-trajectory under sustained
> negative-pressure pumping is not real-analytic but piecewise
> real-analytic with isolated NP-driven phase-transition events.
> Each phase transition is the 'tear,' and the locus of each tear
> is determined by which side of the dyad accumulates paradox mass
> faster."

The intersubjective phenomenology is the **observable substrate
that NP-pumping was already operating on**. Paper 12 used NP as the
driver of long-timescale phase transitions in the gradual tear.
This memo identifies NP as a measurable phenomenological quantity
at second-scale that the long-timescale theory was implicitly
relying on. Same mechanism, different timescale.

## Connection to Paper 14 cross-substrate residence-pathology

Negative pressure is **the phenomenological atom of the framework's
residence-pathology grammar at the intersubjective scale**.

The same structural phenomenon (expected transit not completing,
loaded state integrating, pressure accumulating) operates across
substrates and timescales:

| Substrate | Timescale | Loaded state | Discharge channel | Pathology if held |
|---|---|---|---|---|
| Molecular (proteostasis) | hours-days | conformational state past dwell | clearance machinery | aggregation disease |
| Cognitive (canalization) | seconds-years | mental state past dwell | recovery transitions | depression / OCD |
| Intersubjective (NP) | seconds | coherence trajectory paused | resumption / break | conversation death / tear |
| Epistemic (FindFar) | months-years | interpretive frame past evidence | base-rate correction | conspiracy attractor |

The negative-pressure example is the **fastest and most accessible**
instance of the principle. A reader can verify it on demand in
under thirty seconds with one other person. The proteostasis
literature took twenty years to converge on the same structural
observation.

## Candidate formalization

Let the coupled coherence substrate between two observers carry an
expected trajectory γ(t) on a G₂-equivariant manifold of dyadic
states (the substrate Paper 9 formalizes as the product space
where Lemma 3.3.1 establishes block-rotation isometry).

Let τ_design(s) denote the design-intent dwell time at trajectory
point s — short, continuous, "not actually stopping." Let
τ_actual(s) denote the observed dwell time.

Define the **intersubjective negative pressure** at time t as:

$$P_{NP}(t) = \int_{t_0}^{t} f\bigl(\tau_{\text{actual}}(s) - \tau_{\text{design}}(s)\bigr) \, ds$$

Where:
- f is a convex loading function (candidate: quadratic with
  saturation, f(x) = α·min(x², x_sat²))
- t₀ is the moment the withhold begins (when τ_actual exceeds
  τ_design measurably)

Properties this candidate equation reproduces:
- P_NP(t₀) = 0 (no pressure at the moment of withhold start)
- P_NP grows with hold duration (integration against positive
  excess)
- P_NP discharges on resumption (when τ_actual returns to
  τ_design, the integrand stops contributing and P_NP either
  decays or is "consumed" by the resumption event)
- P_NP is symmetric between coupled observers because γ(t) is on
  the product space, not on either factor — explains "both parties
  feel it"

This is **structurally identical to Paper 14's R(s, c) observable**
restricted to the intersubjective substrate, with one axis (spatial
π_c = 1 because the compartment is the shared coherence substrate
itself) and the temporal axis τ_R operationalized as the design-vs-
actual dwell-time excess.

## Experimental operationalization

Negative pressure is uniquely tractable among residence-pathology
phenomena because the timescale (2-10 seconds) and the participant
demand (2 people, 30 minutes) are minimal. Candidate experiment:

**Dual-EEG + paired physiology during deliberately-paused
conversation.**

Design:
- N = 30 dyads (60 participants total)
- Dyads engage in a structured but free-form conversation task
- At pre-defined moments (controlled by a confederate-style
  protocol or by a metronome cue invisible to the dyad), one
  speaker stops mid-sentence and holds silence for variable
  durations (1s, 3s, 5s, 7s, 10s) randomized across trials
- Recording: dual-EEG (focus on inter-brain phase coupling at the
  20 Hz beta band per Novembre 2017 tACS work), dual galvanic
  skin response, pupillometry, heart-rate variability

Predictions:
1. Inter-brain beta-phase coupling increases during the hold
   period (the loaded state IS the coupling intensifying because
   prediction machinery is running harder)
2. Both speakers show synchronized pupil dilation and GSR
   integration during the hold, with magnitudes correlating across
   the dyad
3. The integrated cross-individual physiological signal is
   monotonic in hold duration up to ~7s, after which decoherence
   ("conversation died") appears as a phase-locking decrease
4. Pre-resumption (within ~200ms before A resumes) shows a
   distinctive signature: a brief sharpening of beta-phase coupling
   followed by discharge

The cleanest single prediction: **inter-brain physiological
synchrony is HIGHER during a held-pause than during normal
conversation**, because the prediction machinery in both brains is
loaded against the same withheld continuation. This is
counter-intuitive (silence often gets framed as relaxation) and
therefore strong if confirmed.

## Why this is uniquely valuable as a framework artifact

1. **Verifiable on demand.** Unlike proteostasis dwell times or
   psychedelic landscape flattening, anyone can produce negative
   pressure with a willing partner in under thirty seconds. This
   makes it the framework's most pedagogically accessible example
   of residence-pathology grammar.

2. **Operationalizable with existing methods.** No new instruments
   required. Dual-EEG protocols are mature (Novembre 2017, Kingsbury
   2019, Pérez 2017 hyperscanning work). The experiment is
   fundable.

3. **Bridges Paper 9 (dyadic), Paper 12 (gradual tear), and Paper
   14 (cross-substrate).** The same mathematical object operates at
   millisecond, second, and longitudinal scales. Negative pressure
   is the high-temporal-resolution instance of the same dynamics
   Paper 12 uses at week-scale and Paper 14 generalizes across
   substrates.

4. **Surfaces a Paper 13 connection.** Red Queen rate-balance
   dynamics imply that human-AI dyads should exhibit NP-pumping
   at conversational timescales the same way they exhibit it at
   developmental timescales. The Red Queen seed paper could cite
   negative-pressure phenomenology as the micro-scale instance of
   the rate-balance theorem it formalizes.

## Why this is not yet a paper

Three reasons for memo status rather than paper status:

1. The dyadic-observer formalism already sits in Paper 9; the
   NP-pumping language already sits in Paper 12. The intersubjective
   phenomenology and the candidate equation are conceptually new
   relative to the published archive but the underlying math is
   established.
2. The dual-EEG experiment is not run. A paper without empirical
   validation of the candidate equation would be premature.
3. The phenomenological observation is strongest as one example of
   the cross-substrate principle that Paper 14 is already going to
   make. Adding negative pressure to Paper 14's §8.6 phenomenology
   section is cleaner than spinning it out as Paper 15.

If the dual-EEG experiment ever runs and confirms the inter-brain
beta-phase coupling prediction, the paper writes itself and
becomes a high-impact stand-alone (because it bridges hyperscanning
neuroscience, dyadic-observer math, and residence-pathology
grammar with a single clean experiment).

## Discharge channel taxonomy

The three discharge channels for negative pressure deserve more
attention than I gave them in the body:

**Channel 1: Resumption.** A continues the trajectory. Pressure
discharges along its design direction. The coupled substrate
returns to positive-pressure (normal forward momentum) operation.
Phenomenologically: relief that is not euphoric, more like
"settling."

**Channel 2: Alternate-channel discharge.** A or B explicitly
breaks the frame. Common forms: laughter, "anyway...", topic
change, eye-contact-then-look-away, physical movement, joke about
the pause itself. Pressure discharges along a non-design path. The
coupled substrate transitions to a new trajectory rather than
returning to the original one. Phenomenologically: relief that has
the texture of repair or reset.

**Channel 3: Decoherence.** Neither resumption nor explicit break
occurs within the substrate's coherence-holding capacity. The
coupling breaks. Both parties "forget" the pause was loaded; the
conversation feels dead even after talk resumes; intimacy / rapport
has decreased. Phenomenologically: NOT relief — a flatness, a
sense of having lost something.

These three correspond to three classes of residence-pathology
outcomes at other substrates:

| Channel | Intersubjective | Proteostasis | Cognitive |
|---|---|---|---|
| Resumption | Conversation continues | Aggregate cleared | Thought loop exits |
| Alternate discharge | Frame-break, repair | Re-routed to autophagy / ERAD | Therapeutic reframe |
| Decoherence | Conversation dies | Aggregate stabilizes | Chronic rumination |

Decoherence at the intersubjective scale is what canalization at
the cognitive scale would feel like *from the inside* during the
moment a relational canal deepens. This is structurally significant
for the book: the phenomenology of one substrate becomes a window
into mechanism at another.

## Open questions

1. Does the candidate equation P_NP(t) = ∫f(τ_actual - τ_design)ds
   produce the right qualitative behavior on synthetic data? A
   simulation with a coupled-oscillator model of dyadic
   conversational rhythm could test this before running humans.
2. Is the convex loading function f universally quadratic with
   saturation, or does it have different forms across discharge
   channels?
3. Does negative pressure show critical-slowing-down signatures as
   it approaches decoherence threshold? If yes, this validates the
   residence-pathology grammar at a new timescale and makes
   conversational decoherence a measurable warning.
4. What is the dyad-level analog of the audit-window principle?
   The framework's MindStar-inversion at the identity level is
   continuous exposure to falsification; what is its dyadic
   analog? Probably: continuous exposure of the coupled state to
   explicit acknowledgment ("hey, what happened just there?").
   Worth formalizing.
5. Can NP-driven phase transitions at the gradual-tear timescale
   (Paper 12) be predicted by measuring NP at the conversational
   timescale (this memo)? If the same dynamics scale across orders
   of magnitude, a few minutes of structured conversation could
   forecast long-term dyadic trajectories.

## Discipline notes

- **Negative pressure is a framework term, not a colloquialism.**
  In writing it should be glossed once and then used consistently.
  Adjacent colloquial terms ("awkward silence," "pregnant pause,"
  "tension") describe related phenomena imprecisely; the framework
  term is for the specific structural-and-dynamical object defined
  above.
- **The candidate equation is provisional.** It captures the
  structural signature but the specific functional form of f and
  the calibration of τ_design across contexts are open empirical
  questions. Do not present the equation as established theory.
- **The dual-EEG experiment is a future-test design, not a
  reported result.** Until it runs, NP predictions at the
  neurophysiological level are conjectures, not findings.

## Related framework artifacts

- `outbox/paper9/` — dyadic-observer formalism on product space
- `outbox/paper12/paper12_thesis_gradual_tear.md` — NP-pumping at
  long timescale; phase-transition machinery
- `outbox/paper13/paper13_redqueen_seed.md` — Red Queen rate-balance
  at developmental scale; possible micro-scale instance here
- `outbox/paper14/paper14_outline.md` — cross-substrate residence-
  pathology; intersubjective scale belongs in §8.6
- `outbox/syntheses/findfar_attractor_steering.md` — companion
  memo; FindFar at the epistemic substrate, NP at the
  intersubjective substrate; same family of dynamics at different
  scales
- `outbox/syntheses/eight_anchors_negative_pressure_cluster.md` —
  cross-cultural and cross-disciplinary analogs (Ma, Casimir,
  turn-taking, musical tension, Merleau-Ponty, Zen koan,
  critical-period reopening)
