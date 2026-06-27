# Resume Standards & Formatting Rules

> Reference for `resume_builder`. The format contract for the **ATS-plain Markdown** output.

## Document shape (senior PM, Balanced tailoring)

- **Length:** 2 pages. Vikash is senior (Director/Principal-level) with a 25-year arc — one page truncates legitimate scope. Two pages is correct; three is padding.
- **Format:** reverse-chronological, single column. The only ATS-safe structure (see `ats_mechanics.md`).
- **Section order:**
  1. **Header** — name, location, phone, email, LinkedIn. Plain text lines (never a header/footer region).
  2. **Summary** — 2–3 lines, retargeted per JD. This is the only section rewritten heavily for every application.
  3. **Experience** — reverse-chron. Meta roles stacked under one company with sub-roles (mirrors the `linkedin_optimizer` Poincaré "role stacking" trajectory signal and reads as promotion, not lateral moves).
  4. **Earlier Experience** — condensed one-liners for pre-2013 / less-relevant roles, to control length while preserving the arc.
  5. **Education**
  6. **Skills** — a keyword-aligned block (high ATS value).
  7. *(Optional)* **Speaking & Teaching** / **Founder Experience** when the JD rewards it.

## Section headings (ATS-recognized — use these exact words)

`Summary` · `Experience` (or `Work Experience`) · `Education` · `Skills`. Do **not** rename to creative headers — the parser keys on these.

## The bullet formula

```
[Strong action verb] + [what you did] + [scope/scale] + [quantified outcome] (+ mirrored JD keyword)
```

- **Lead with the verb.** Led, Shipped, Launched, Built, Drove, Owned, Scaled, Unblocked, Mitigated.
- **Scope before story.** The first bullet of each role states the altitude: what you owned, team size, scale, revenue/risk. A recruiter reads it in the 6-second scan.
- **Results > responsibilities.** Every bullet answers "so what?" with an outcome. A bullet with no outcome is a responsibility — cut or fix it.
- **One number per bullet, minimum, where one exists in the sources.** Numbers stop the scanning eye. If no traceable number exists, keep the qualitative outcome — never fabricate (see `career_sources.md`).
- **Mirror the JD's exact keyword** when it fits naturally. "experimentation" if the JD says experimentation; "Go-to-Market" if it says GTM.
- **3–5 bullets** for the most relevant 2–3 roles; **1–2 bullets** for older/less-relevant roles.

### Example transform
- Weak: "Responsible for WhatsApp messaging monetization initiatives."
- Strong: "Unblocked ~34% of Marketing Messages revenue by launching Web Custom Audiences, bridging Ads Manager signals into WhatsApp's encrypted messaging surface." *(scope + verified metric + domain keywords)*

## The summary block (retargeted every time)

2–3 lines. Not "I am a passionate PM." Structure:
1. **What you are + your strongest relevant proof,** in the JD's level/domain language.
2. **The differentiated combination** that fits this archetype (e.g., "foundation-model alignment *and* billion-user consumer AI" for a frontier lab).
3. *(Optional)* one scale/credibility anchor.

Pull the framing from the matched archetype (see `jd_parse_protocol.md` Step C). The summary is where Balanced tailoring does most of its work.

## Tailoring philosophy: BALANCED (the chosen default)

- **Keep the full career arc.** Do not delete roles to chase a one-pager. The complete trajectory is itself a senior-credibility signal.
- **Retarget, don't rebuild.** Heavily rewrite the summary and the top 2–3 roles' bullets to the JD; lightly touch older roles.
- **Reorder within a role,** not across the timeline. Put the JD-relevant bullet first within each role; keep roles in reverse-chron.
- **Foreground by archetype.** Promote matching achievements to the top bullets; demote (don't delete) off-archetype ones.
- **Condense the tail.** Pre-2013 roles collapse to one line each unless the JD specifically rewards them (e.g., a hardware/infra role rewards the Cisco ASIC depth).

## ATS-plain formatting rules (Markdown)

- **No tables for resume content.** Tables are for *this* reference doc, not the resume — ATS parsers drop them. Use plain lines and `-` bullets.
- **No columns, text boxes, images, icons, or emoji.**
- Bold (`**`) for company / title / section emphasis is fine; it degrades gracefully to plain text.
- Dates as plain text on the role line: `**Lead PM, Meta Superintelligence Labs** — 2024–Present`.
- Consistent date format throughout (`YYYY–YYYY`, `Mon YYYY`, or `–Present`). Pick one.
- One space, standard punctuation, no fancy Unicode separators beyond `·` and `—` in the header/role lines.

## Anti-buzzword list (strip these)

Inherited from `linkedin_optimizer`: *passionate, innovative, strategic, experienced, motivated, results-oriented, guru, thought leader, synergy, dynamic, go-getter.* No recruiter searches for them; they read as filler. Replace with the concrete thing you did.

## Voice & consistency

- Third-person-implied, no "I." Bullets start with verbs.
- Past tense for past roles; present tense for the current role's ongoing work.
- **Consistency with LinkedIn:** titles, dates, and headline scope numbers must match `linkedin_optimizer/vikash_context/`. A recruiter comparing the two looks for discrepancies.

## Final pre-ship checklist

- [ ] Every quantified claim traces to a source file (`career_sources.md`)
- [ ] JD's top 3 must-have keywords appear naturally in summary + experience
- [ ] Strongest relevant title + scope visible in the top third (Gate 2)
- [ ] No buzzwords; every bullet has a "so what"
- [ ] Standard section headings; single column; no content tables
- [ ] 2 pages; tail roles condensed
- [ ] Any unfillable metric marked `[NEEDS INPUT]`, not invented
- [ ] Contact block confirmed with user
