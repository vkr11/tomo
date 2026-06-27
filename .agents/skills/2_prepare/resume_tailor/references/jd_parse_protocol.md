# Job Description Parse Protocol

> Reference for `resume_builder`, `resume_match_scorer`, `cover_letter_writer`.
> All three skills start here. The output is a structured **JD Profile** the rest of the pipeline consumes.

## Step A: Ingest the JD

Accept the JD in any of these forms:
- **Pasted text** — use directly.
- **URL** — capture it to Markdown with the `web_capture` skill:
  ```bash
  SKILL=/Users/vikashrungta/code/tomo/.agents/skills/web_capture/scripts/capture.py
  python3 "$SKILL" "<JD_URL>" -m /tmp/jd.md
  ```
  Many job boards are JS-rendered (Workday, Greenhouse, Lever) — `web_capture` handles those where `curl` fails. If the page is gated/blocked, ask the user to paste the text.
- **From the pipeline** — a role already logged in `users/vikash/strategy/interview_pipeline.md` by `job_scanner`. Use the stored URL.

Always save the captured JD into the application folder as `_jd.md` (with source URL + retrieval date header), so the artifact is reproducible.

## Step B: Extract the JD Profile

Produce this structured object. It drives selection, keyword alignment, and the match report.

```markdown
## JD Profile: {Company} — {Role Title}

- **Title (verbatim):** {exact title as posted}
- **Level / seniority:** {IC vs manager; L-level / Director / Principal if stated or inferable}
- **Location / work model:** {city; remote/hybrid/onsite}
- **ATS:** {Workday | Greenhouse | Lever | Ashby | Taleo | iCIMS | unknown}  ← infer from URL/page
- **Company archetype:** {Frontier AI Lab | AI Platform | Consumer/Marketplace | Enterprise Tech}
  ← map via linkedin_optimizer Part 4 archetype table

### Must-haves (knockouts — auto-reject if unmet)
- {years of experience}, {required degree}, {work auth}, {specific platform/domain}

### Core responsibilities (what the role DOES)
- {ranked, most-emphasized first — emphasis = repetition + position in the post}

### Hard-skill / tool / methodology keywords (verbatim)
- {RLHF, experimentation, SQL, roadmap, GTM, LLM eval, ... — copy the JD's exact spelling}

### Domain keywords
- {responsible AI, ads ranking, marketplace, agentic systems, ...}

### Scope signals
- {team size expected, P&L, cross-functional partners, scale language}

### Implicit priorities ("the real job")
- {read between the lines: what problem is this hire actually solving? what's the unstated #1?}
```

## Step C: Classify the archetype (drives framing)

Map the company to one of `linkedin_optimizer`'s four archetypes, because **what to foreground differs by archetype** (and the anti-keywords tell you what to *de-emphasize*):

| Archetype | Foreground (Vikash's matching assets) | De-emphasize |
|---|---|---|
| **Frontier AI Lab** (Anthropic, OpenAI, DeepMind) | Llama alignment/RLHF/SFT, red-teaming, safety evals, first-principles, founder DNA | P&L, ARR, ads GTM mechanics |
| **AI Platform** (Google, MSFT AI, Nvidia) | Llama as a platform/dev surface, research-to-production, enterprise deployment, APIs | Consumer growth metrics, deep alignment internals |
| **Consumer / Marketplace** (Uber, DoorDash, Coupang) | WhatsApp MM revenue unlock, A/B testing, growth, unit economics, real-world graph | LLM safety internals, RLHF detail |
| **Enterprise Tech** (Apple, Netflix, Intuit) | GTM strategy, platform thinking, cross-functional at scale, regulated-domain product | Frontier-research terminology |

**Do not blend archetypes.** A resume that foregrounds both "model alignment" and "P&L / ARR growth" reads as unfocused to *both* a frontier-lab reviewer and a consumer-growth reviewer. Pick the archetype the JD belongs to and commit the framing to it. (This mirrors the GLMix "don't blend keywords" insight from `linkedin_optimizer`.)

## Step D: Hand off

- `resume_builder` → uses the JD Profile to select arc, order bullets, align keywords.
- `resume_match_scorer` → scores coverage of must-haves + keyword list, computes fit, lists gaps.
- `cover_letter_writer` → uses "implicit priorities" + archetype to choose the 2–3 stories to tell.

## Quality bar for the parse
- **Verbatim keywords.** Copy the JD's spelling; do not normalize "experimentation" → "A/B testing." Capture both if both appear.
- **Rank by emphasis.** A requirement repeated in summary + responsibilities + qualifications is the real priority. Surface it.
- **Find the unstated #1.** Most JDs bury the actual hiring trigger. Name it — it's what the summary line and top bullet should answer.
