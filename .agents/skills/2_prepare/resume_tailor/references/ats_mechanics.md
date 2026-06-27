# How Resume Screening Actually Works (The Machine)

> Reference for `resume_builder`, `resume_match_scorer`, `cover_letter_writer`.
> The companion to `linkedin_optimizer`'s recruiter-search pipeline. LinkedIn gets you *found*; the resume gets you *advanced*. Different machine, same discipline: understand which gate you're failing at, then fix that specific thing.

A resume passes through **three sequential gates**. Each can eliminate you. Optimizing the wrong gate wastes effort.

```
Submit resume
      │
      ▼
┌────────────────────────────┐
│ GATE 1: ATS PARSE + FILTER │  Machine reads the file. Knockout questions + keyword search.
│ (structured-data extraction)│  Bad layout → garbled fields. Missing must-have keywords → never surfaced.
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ GATE 2: RECRUITER 6-SEC SCAN│  Human skims top third. Title, current company, dates, scope.
│ (yes / no / maybe pile)     │  Reverse-chron, scannable, quantified results, no gaps.
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ GATE 3: HIRING-MANAGER READ │  Deep read for relevance + altitude. Does the *story* fit the role?
│ (interview / pass decision) │  Narrative coherence, scope match, domain proof, "so what" of each bullet.
└────────────────────────────┘
```

---

## Gate 1: The ATS (Parse + Filter)

An **Applicant Tracking System** is the database every mid-to-large company runs applications through. The major systems behave differently — know which one you're facing (often visible in the application URL or page chrome):

| ATS | Behavior | Implication |
|---|---|---|
| **Workday** | Form-heavy. Re-keys your resume into structured fields; knockout questions (years, work auth, location, degree). | Parsing quality matters most. Answer knockouts honestly — they auto-reject. |
| **Greenhouse** | Recruiter-driven, light auto-reject. Resume stored + keyword-searchable. | Keyword coverage for *recruiter search* matters more than auto-filters. |
| **Lever** | Similar to Greenhouse — relationship/search oriented. | Same as Greenhouse. |
| **Taleo / iCIMS** | Older, stricter parsers. Choke on columns, tables, headers/footers. | Use the most conservative single-column layout. |
| **Ashby** | Modern parser, decent on layout, strong search/ranking. | Keyword relevance + clean structure both matter. |

### What ATS parsers extract
The parser converts your document into structured fields: **Contact → Work Experience (company, title, dates, bullets) → Education → Skills**. Anything that breaks this extraction makes you a low-confidence or empty record.

**Parsing killers — never do these:**
- Multi-column layouts (parser reads left-to-right across columns and scrambles text)
- Tables and text boxes for content (often dropped entirely)
- Contact info in the header/footer region (frequently not parsed)
- Skills/titles rendered as icons, graphics, or images (invisible to the parser)
- Non-standard section headings ("Where I've Made Impact" instead of "Experience")
- Fancy fonts, columns of dates misaligned from their roles

**Parsing-safe — always do these:**
- Single column, top-to-bottom reading order
- Standard headings the parser recognizes: `Summary`, `Experience` / `Work Experience`, `Education`, `Skills`
- Company · Title · Dates on plain text lines, consistent order every entry
- Reverse-chronological (functional and hybrid formats confuse parsers and read as "hiding something")
- Real text, never images, for anything that must be searchable

> Because the chosen output is **ATS-plain Markdown**, these rules are mostly automatic — Markdown is single-column plain text by construction. The discipline that remains: standard headings, consistent entry structure, and no tables for resume *content*.

### Keyword matching
Recruiters and some ATS rank/filter on keywords drawn from the job description. The highest-signal keywords, in order:
1. **Hard skills / tools / methodologies** — "RLHF", "experimentation", "SQL", "A/B testing", "roadmap", "Go-to-Market"
2. **Domain terms** — "responsible AI", "ads ranking", "marketplace", "LLM evaluation"
3. **Title / level language** — mirror the JD's title and seniority words
4. **Certifications / requirements** — degrees, clearances, specific platforms

**The mirroring rule:** use the JD's *exact* phrasing. If the JD says "experimentation," write "experimentation" — not only "A/B testing." If both appear in the JD, include both. Keyword variants do not always resolve to the same token in a recruiter's search the way LinkedIn's skill graph resolves adjacencies. Spell it the way they wrote it.

**Knockout questions (Gate 1, Workday/Taleo):** "Do you have X years of Y?" / "Are you authorized to work in Z?" These auto-reject. They are answered in the application form, not the resume — but the resume must *substantiate* the answer (if you claim 8 years of PM, the dates must add up).

---

## Gate 2: The Recruiter 6-Second Scan

A recruiter skims, they do not read. Eye-tracking (TheLadders, N=30, 2012/2018 — the same study cited in `linkedin_optimizer`) shows the gaze lands on: **name → current title & company → current dates → previous title & company → education**. ~6 seconds to sort into yes / no / maybe.

**What wins the scan:**
- **Strongest, most relevant title visible at the top.** Reverse-chron means your current role leads — make sure it reads as a match for the target level.
- **Scope legible in the first line of each role.** Team size, P&L, user scale, what you owned. Not "responsible for various initiatives."
- **Quantified results.** 58% of recruiters say measurable achievements make a resume stand out; 34% call lack of results a dealbreaker (Jobscan recruiter survey — also cited in `linkedin_optimizer`). Numbers stop the scanning eye.
- **No unexplained gaps, no title regression** that reads as a demotion without context.
- **Clean visual hierarchy.** Bold company/title, consistent dates, generous whitespace.

**What loses the scan:** dense paragraphs, buzzword soup, responsibilities with no outcomes, the most relevant experience buried on page 2.

---

## Gate 3: The Hiring-Manager Read

If you survive the scan, a hiring manager reads for *fit and altitude*. They are asking: "Has this person done a version of the job I'm hiring for, at the scope I need?"

**What they evaluate:**
- **Narrative coherence** — does the career arc tell a story that leads logically to *this* role? (This is why **Balanced** tailoring keeps the full arc but retargets the framing.)
- **Scope / altitude match** — Director roles want org-scale and cross-functional leadership; IC roles want depth and shipped impact. The bullets must prove the *level*, not just the function.
- **Domain proof** — concrete evidence in the JD's domain (e.g., "shipped LLM safety evals" for an AI safety role), not adjacent hand-waving.
- **The "so what" of every bullet** — each line should answer "why did this matter to the business / users?" A bullet without an outcome is a responsibility, and responsibilities are forgettable.

---

## The Three-Gate Checklist

| Gate | Owner | Lever | The resume_builder move |
|---|---|---|---|
| 1. ATS parse + filter | Machine | Clean structure + JD keyword coverage | Single-column MD, standard headings, mirror JD hard-skill terms |
| 2. Recruiter scan | Human, 6s | Title + scope + quantified results, top-third | Strong title line, scope in first bullet, numbers up front |
| 3. Hiring-manager read | Human, deep | Narrative + altitude + domain proof | Retarget summary, select relevant arc, "so what" on every bullet |

**Cross-skill note:** `linkedin_optimizer` argues "LinkedIn hooks, the resume closes." This is the closing instrument. The two should agree — same titles, same scope numbers, same domain positioning — because a recruiter often views both side by side. Inconsistency between them is a credibility flag.
