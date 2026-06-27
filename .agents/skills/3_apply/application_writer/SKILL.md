---
name: application_writer
description: >
  Write a tailored cover letter for a specific job description, in Vikash's voice. Trigger on:
  "write a cover letter for [role/company]", "cover letter for this JD", "draft a note to the
  hiring manager", "intro letter for this job". Reuses the JD Profile and verified career sources
  from resume_builder, picks ONE story that maps to the role, and produces a tight (<350 word)
  letter argued — not summarized — into users/vikash/applications/. Best paired with a resume from
  resume_builder.
---

# Cover Letter Writer

Writes a short, specific, in-voice cover letter that *argues why Vikash fits this role* — the thing a resume's bullets can't say. Companion to `resume_builder`; reuses the same JD parse and verified facts.

## Shared machinery (reference, don't duplicate)
- **Source of truth:** `../resume_builder/references/career_sources.md` — same verified files; no invented facts; the letter must not contradict the resume.
- **JD parsing:** `../resume_builder/references/jd_parse_protocol.md` — reuse the JD Profile (especially the **unstated #1 priority** and the **archetype**).
- **Stories:** `users/vikash/stories/story_bank.md` and `users/vikash/background/project_inventory.md` — where the one story comes from.
- **Company specifics:** `companies/{name}/` if a `company_researcher` dossier exists — fuel for the "why this company" paragraph.
- **Principles + format:** `./references/cover_letter_principles.md` and `./templates/cover_letter_template.md`.

## Protocol

### Step 0 — Decide if it's worth it
Per `cover_letter_principles.md`: invest real effort for stretch roles, narrative pivots, referrals, mission-driven companies (frontier labs), explicit requests, and small companies. For a high-volume Workday application, keep it to a tight 3 paragraphs. If a resume was just built, reuse its `_jd.md` and match report.

### Step 1 — Load the inputs
- The JD Profile (parse it now if not already done; save `_jd.md`).
- The matched archetype → sets the letter's lead angle.
- The role's unstated #1 priority → the hook answers it.
- The resume (if one exists in the application folder) → ensure consistency, and pick a story the resume *doesn't* already tell in full.

### Step 2 — Pick ONE story
Choose the single story from `story_bank.md` / `project_inventory.md` that best maps to the role's core challenge. One vivid, quantified story beats a list. (E.g., PETs/W3C for an ambiguity-heavy frontier role; WhatsApp MM revenue unlock for a consumer-monetization role; HUD/VRS for a regulated-domain role.)

### Step 3 — Write it
Use `./templates/cover_letter_template.md` and `cover_letter_principles.md`:
- Hook tied to the unstated #1 → one proof story → genuinely company-specific fit → confident close.
- Vikash's voice: direct, builder-oriented, evidence-backed, no buzzwords, no groveling.
- < 350 words. Archetype-tuned lead.
- Every claim traces to the sources; nothing contradicts the resume.

### Step 4 — Write output
```
users/vikash/applications/{company}-{role-slug}/cover_letter.md
```
(Same folder as the resume and match report, so an application is one self-contained directory.)

### Step 5 — Report back
Note which story you used and why, and flag the company-specific paragraph if a dossier didn't exist (it may need the user's input or a `company_researcher` run to be truly specific).

## Non-negotiables
- **One story, told well** — never a list of accomplishments.
- **Paragraph 3 must be specific and true** to the company — if you can't be, say so and recommend a `company_researcher` dossier first.
- **No new facts** beyond the sources; **no contradiction** with the resume.
- **< 350 words**, Vikash's voice.

## When to Use
- "Write a cover letter for {role/company}" / "draft a note to the hiring manager".
- Alongside a `resume_builder` run for a stretch, referral, or mission-driven application.

**Not for:** the resume itself (→ `resume_builder`), fit scoring (→ `resume_match_scorer`), or LinkedIn (→ `linkedin_optimizer`).
