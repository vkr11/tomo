# Career Sources — Single Source of Truth

> Reference for `resume_builder`, `resume_match_scorer`, `cover_letter_writer`.
> The resume may contain **only facts traceable to the files below.** This document is the anti-hallucination contract.

## The Prime Directive

**Never invent a metric, title, date, scope number, or achievement.** If a bullet would be stronger with a number you cannot trace to a source file, do one of two things:
1. Use the qualitative claim without the fabricated number, OR
2. Emit a `[NEEDS INPUT: <what's missing>]` marker in the resume draft and list it in the match report's "Gaps to fill before submitting" section.

A fabricated metric that surfaces in an interview is a credibility kill. A `[NEEDS INPUT]` marker the user fills in 30 seconds is a non-event. Always prefer the marker.

## Source Files (read these, in priority order)

| Priority | File | What it provides | Trust level |
|---|---|---|---|
| 1 | `users/vikash/background/career_summary.md` | Roles, dates, project→impact map, business-impact table, org scope | High — but watch for `TODO` / `$XB` placeholders |
| 2 | `users/vikash/background/project_inventory.md` | Per-epic detail, external-verified context & metrics (downloads, run-rate, %) | High |
| 3 | `users/vikash/background/meta_psc/*.txt` | Performance reviews — the richest source of **specific, verified metrics** and scope per half | Highest for numbers — these are contemporaneous records |
| 4 | `users/vikash/stories/story_bank.md` | STAR narratives — for cover letters and to verify the "so what" behind a bullet | High |
| 5 | `users/vikash/background/resume/original/` | Prior tailored resumes (`.docx` + `_extracted.md`) — phrasing, format precedent, per-company angle | Medium — older roles; verify dates against career_summary |
| 6 | `users/vikash/profile.md` | Contact block (name, phone, email, LinkedIn) for the header | High — but confirm which email/phone to use per application |
| 7 | `.agents/skills/linkedin_optimizer/vikash_context/` | Positioning, archetype keyword tiers, target domains | High for *framing*, not for facts |

### How to use them together
- **Structure & arc** → `career_summary.md` §4 (Career Timeline) is canonical for roles, titles, dates.
- **Best numbers** → cross-reference `project_inventory.md` "Context & Evidence" blocks and `meta_psc/*.txt`. Example verified metrics already on file: ~34% of MM revenue unblocked (WCA); $235M ads revenue risk mitigated (WA Integrity); Llama >100M downloads; DOJ variance <10% for 91.7% of housing ads; eLagaan 30K customers; FPGA Central 45K members; 800+ PMs trained; 7,500+ candidates reached.
- **Framing per target** → `linkedin_optimizer/vikash_context/keywords/keyword_critique.md` and `linkedin_core_identity.md` give the archetype keyword tiers (Frontier Lab vs AI Platform vs Consumer vs Enterprise). Use these to decide *which* facts to foreground — not to add new ones.

## Known gaps in the source data (as of last review)

These are unfilled in `career_summary.md` / `project_inventory.md`. When a target JD makes one of them load-bearing, flag it as `[NEEDS INPUT]` rather than guessing:
- Team sizes / # of PMs managed per role (career_summary §7 has `TODO`s)
- Several STAR results (Llama Safety result metrics, HUD settlement dollar value)
- Patents, publications, external talks (career_summary §12)
- Exact revenue figures for older ads roles (prior resumes show `$XB` placeholder)
- Consulting/side-project outcomes (Ezcater, Commerce MCP, GEO, Alloi, AI SRE)

## Contact & identity note

`profile.md` lists `hellovkr@gmail.com`; the most recent extracted resume header used `vikashrungta@gmail.com`. **Default to the resume header in `profile.md`, but confirm with the user which contact set to use** when generating a submission-ready artifact — this is the one field a typo makes catastrophic.

## The traceability habit

While drafting, keep a mental (or scratch) note of which source each quantified claim came from. The match report should be able to answer "where did this number come from?" for every figure in the resume. If you can't answer it, the number doesn't ship.
