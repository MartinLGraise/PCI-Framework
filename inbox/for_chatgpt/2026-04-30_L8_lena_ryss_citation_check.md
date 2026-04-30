# L8 — Lena Ryss "Seven Degrees of Freedom" Citation Check

**Tool combo:** Live web search + reasoning (NO deep research, NO GitHub connector needed)
**Lane:** L8
**Target use:** One-shot due diligence — has any legitimate G₂ literature cited Ryss?
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 5-10 minutes

---

## Prompt to send

```
You are doing a one-shot citation due-diligence check.

Subject: Lena Ryss, "Seven Degrees of Freedom in G₂ Geometry"
(or similar title variants — exact title may vary).

Context: This paper has been flagged as crank-adjacent in
prior analysis. I want to know whether any legitimate G₂
mathematical-physics literature has cited it. I am NOT asking
you to evaluate the paper itself or summarize its claims.
This is purely a citation-network sanity check.

Tasks:

1. Search Google Scholar, Semantic Scholar, INSPIRE-HEP, and
   arXiv (via web search) for citations to Ryss's paper(s)
   on G₂, octonions, or "seven degrees of freedom" (any of
   her work, not just one paper).

2. For each citation found, classify the citing venue:
   - LEGIT: Peer-reviewed mathematical physics, geometry, or
     theoretical physics journal (Comm. Math. Phys., J. Geom.
     Phys., Adv. Math., Phys. Rev. D, JHEP, etc.) or arXiv
     paper by an established researcher with a track record
   - NEUTRAL: Preprint with no peer-review track record, but
     by author with some legitimate prior work
   - QUESTIONABLE: Self-published, predatory journal, or by
     authors who appear in fringe venues
   - SELF: Citations by Ryss herself in subsequent work

3. For each LEGIT or NEUTRAL citation, briefly note (one line)
   how Ryss's work is used: cited as authority? cited critically?
   cited in passing?

Deliverable format:

Section A: Total citations found, broken down by category
Section B: Table of LEGIT citations (citing paper, venue,
           DOI, how Ryss is used)
Section C: Table of NEUTRAL citations (same format)
Section D: Brief assessment — is the citation network
           consistent with treating Ryss as a non-authority
           in the legitimate G₂ literature?

Be conservative. If you find zero legitimate citations, say
so explicitly — that IS the answer to the question. If you
find unexpected legitimate citations, flag them so I can
re-evaluate.

Cite each citing paper with a DOI or arXiv ID. Do not include
my prior assessment of Ryss in your output — I want a fresh
independent check.
```

---

## Notes for C-7RO when response comes back

If zero legitimate citations: lane closes confirming our verdict, no action needed in any paper. Update RESEARCH_LANES.md to ⚫ CLOSED.

If unexpected legitimate citations: pause, re-read what Ryss actually claims, and reconsider whether Paper 10 §8 needs to differentiate from her work explicitly.

Most likely outcome: zero or near-zero. This is a 5-minute prompt that closes the lane forever.
