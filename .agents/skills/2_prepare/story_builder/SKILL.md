---
name: story_builder
description: >
  Generate interview-ready behavioral stories using the Saga Method — organize Vikash's career into
  Sagas → Epics → Stories, then produce fully-developed keyframe answers (hook + STAR+ + multi-lens
  Principle closes + likely pushback + company-rubric mappings), plus the Build View (source of truth)
  and Lookup View (cheat sheet). Trigger on: "build my stories", "generate a story for [question]",
  "give me a conflict/failure/0-to-1 story", "tell this for Amazon/Google/Anthropic", "story for this
  JD", "where am I thin on stories", "build my story bank", "saga method". Grounded only in Vikash's
  verified career sources — never invents facts.
---

# Story Builder — The Saga Method

Turns raw career material into interview-ready behavioral stories. Implements **The Saga Method** (full guide: [`framework/saga-method/the_saga_method.md`](../../../../framework/saga-method/the_saga_method.md)).

## The Method in one screen

```
SUPPLY (your career, fixed)        DEMAND (per company/question, flexes)
Saga  — a career chapter            Question Category — conflict, failure,
  └ Epic — a multi-quarter          ambiguity, execution, technical bet,
      initiative                    leadership
      └ Story — a keyframe          Principle — your portable operating
        moment (the answer)         system; company rubrics plug onto it

THE MOVE: one Story, retold through a different PRINCIPLE LENS per question.
The raw event is fixed; the Principle decides what you foreground and how you close.

OUTPUTS: Build View (source of truth tree)  →  Lookup View (5-min cheat sheet)
```

## On invocation, read
1. [`framework/saga-method/the_saga_method.md`](../../../../framework/saga-method/the_saga_method.md) — the canonical framework + generic templates.
2. `./references/career_sources.md` — the verified source files + the prime directive (never invent a fact).
3. `./references/principle_library.md` — Vikash's 10 portable Principles + company-rubric map (the lens layer).
4. `./references/question_to_story_map.md` — question category → which Saga/Epic/Story to grab.
5. `./references/delivery_and_calibration.md` — STAR+/Freytag/DIGS, IC7/D1 calibration, surviving pushback.

The 5 Sagas already exist in `users/vikash/stories/story_bank.md`; the keyframe inventory in `users/vikash/stories/11_story_to_pillar_mapping.md`. Don't re-derive them — read and build on them.

---

## Modes (pick by request)

### Mode A — Generate one keyframe Story
"Give me a conflict story" / "a 0→1 story for Anthropic" / "a story for this JD."
1. Map the request to a **Question Category** + target company (→ `question_to_story_map.md`).
2. Pick the strongest keyframe; pull its facts from the sources (traceable only).
3. Choose the **Principle lens** the role rewards (→ `principle_library.md`).
4. Render with `./templates/story_keyframe_template.md`: 10-sec hook → STAR+ (timing 10/10/60/20) → **2+ Principle-lens closes** → likely pushback → company tailoring → reflection/gaps.
5. Save to `users/vikash/stories/keyframes/{saga}__{story-slug}.md`.

### Mode B — Build / refresh the whole bank
"Build my story bank" / "set up the Saga Method."
1. Confirm the 5 Sagas (from `story_bank.md`); expand each into Epics (from `project_inventory.md`).
2. Mine 3–6 keyframes per Epic (seed from `11_story_to_pillar_mapping.md`); generate the high-priority ones as full keyframe files.
3. Build the **Build View** (`./templates/build_view_template.md`) → `users/vikash/stories/build_view.md`.
4. Derive the **Lookup View** (`./templates/lookup_view_template.md`) → `users/vikash/stories/lookup_view.md`.

### Mode C — Re-angle an existing Story (the signature move)
"Tell the WCA story for a failure question instead."
- Keep the raw event; swap the **Principle lens**. Re-foreground the action beats and rewrite the close. Show the before/after so Vikash feels the shift.

### Mode D — Tailor the bank for a company
"Prep my stories for Amazon / Google / Anthropic."
- Translate each Story's Principles to that company's rubric (→ `principle_library.md` map; use `companies/{name}/` dossier if present). For Amazon, map every story to an LP and force "I" voice. Produce a company-specific Lookup View.

### Mode E — Coverage / gap analysis
"Where am I thin?"
- Check the Build View against: the **5 Essential Stories** and the **8 pillars**. Report Principles with only one Story (over-reliance) and pillars with none (gaps: currently Sense, Metrics, Management depth). Ask for real moments to fill gaps — never fabricate.

---

## Non-negotiables
- **Never invent a fact.** Metrics, names, quotes, dates, outcomes all trace to a source file or become `[NEEDS INPUT: ...]`. Interviewers push hard (see `sample_interview_tradeoff.md`) — a fabricated number dies live.
- **A Story is neutral; the Principle is the lens.** Generate the raw event once, then provide multiple closes. Don't bake one interpretation into the event.
- **Calibrate to IC7/D1.** "I" for decisions/influence, "we" for team execution; 60% on Action; quantified results; second-order effects. Strip the weak-answer anti-patterns.
- **Every Story ships with pushback prep.** Process probe, value challenge, bias test.
- **Honor the existing structure.** Build on `story_bank.md` and `11_story_to_pillar_mapping.md`; keep the Build View the single source and the Lookup View derived from it.

## Output map
```
users/vikash/stories/
├── story_bank.md                    # existing — the 5 Sagas (read, don't overwrite)
├── 11_story_to_pillar_mapping.md    # existing — keyframe inventory (read)
├── build_view.md                    # generated — Saga→Epic→Story tree, Principle-tagged
├── lookup_view.md                   # generated — reverse index cheat sheet
└── keyframes/
    └── {saga}__{story-slug}.md      # generated — full keyframe Stories
```

## When to Use
- "Build / generate my interview stories", "story for this question/JD", "tell it for [company]", "where am I thin", "re-angle this story".

**Not for:** the resume (→ `resume_tailor`), LinkedIn (→ `linkedin_optimizer`), company culture/loop research (→ `company_researcher`), or extracting principles from *other people's* blogs (→ `pm_principles_extractor`). This skill is about generating *Vikash's own* stories.

## Files
- references: `career_sources.md` · `principle_library.md` · `question_to_story_map.md` · `delivery_and_calibration.md`
- templates: `story_keyframe_template.md` · `build_view_template.md` · `lookup_view_template.md`
- canonical method: `framework/saga-method/the_saga_method.md`
