---
name: company_researcher
description: Research a company's culture, values, leadership principles, and interview process for PM interview preparation. Produces a standardized dossier with raw web dumps and synthesized files. Use whenever the user mentions "research [company]", "interview prep for [company]", "build a dossier for [company]", "company research", or wants to prepare for interviews at a specific company.
---

# Company Researcher

Automates interview prep research for a target company. Given a company name, discovers their culture/values, interview process, and recent strategic context — then produces a standardized dossier in the tomo repo.

## Setup Requirements

1. The tomo repo must exist at the path defined by `TOMO_REPO` env var (default: `~/code/tomo`)
2. The `companies/` directory must exist in the tomo repo (with the standard template from `companies/README.md`)
3. No API keys needed — uses `search_web` and `read_url_content` tools only

## Research Protocol

Follow these 4 steps in order.

### Step 1: Discover

Run **5-8 targeted searches** to gather raw material. Use these search patterns (replace `{company}` with the target):

**Culture & Values (required):**
1. `{company} leadership principles values culture official`
2. `{company} company culture what we believe core values`

**Interview Process (required):**
3. `{company} PM product manager interview process 2025 2026 loop rounds`
4. `{company} behavioral interview questions STAR method tips`

**Strategic Context (recommended):**
5. `{company} product strategy 2025 2026 recent launches`
6. `{company} PM role what they look for senior principal`

**Community Intel (recommended):**
7. `site:glassdoor.com {company} product manager interview`
8. `site:reddit.com {company} PM interview experience`

For each search, identify 2-4 high-quality URLs and read them with `read_url_content`. Prioritize:
- Official company pages (aboutamazon.com, careers.google.com, etc.)
- Established prep sites (Exponent, IGotAnOffer, RocketBlocks, Product Alliance)
- Recent content (last 12 months preferred)

Refer to `references/research_sources.md` for a curated list of known-good sources per company.

### Step 2: Dump

Save all raw web content as Markdown files into the company's `_raw/` folder:

```
companies/{company_name}/_raw/
├── official_culture_page.md
├── exponent_interview_guide.md
├── glassdoor_interview_reviews.md
├── stratechery_analysis.md
└── ...
```

**Naming convention**: Use lowercase with underscores. Name files by source and content type, not by URL. Example: `exponent_pm_interview_guide.md` not `https_tryexponent_com_abc123.md`.

Each raw dump file should start with a YAML-like header:

```markdown
# {Title}
> Source: {URL}
> Retrieved: {YYYY-MM-DD}

{content}
```

### Step 3: Synthesize

Using the raw material from Step 2, produce two standardized dossier files. Use the exact templates from `references/dossier_template.md`.

#### 3a. `culture_principles.md`

For each principle/value the company has:
- Exact name and official definition
- An **Interview Signal** — what "strong" looks like when demonstrating this in an answer
- A prioritization tier (Tier 1 = always tested → Tier 3 = nice to have)

If the company doesn't have formalized principles (e.g., startups), synthesize their implicit culture from job postings, blog posts, and founder interviews.

#### 3b. `interview_process.md`

Cover:
- Interview stages (screen → loop → offer)
- Round-by-round breakdown with focus areas
- Special rounds (Bar Raiser, cross-functional, presentations, take-homes)
- Communication style expectations
- Tips specific to this company's culture

### Step 4: Register

1. **Create `companies/{company_name}/README.md`** with:
   - A file index linking to `culture_principles.md`, `interview_process.md`, and `_raw/`
   - Cross-references to the user's story mappings in `users/vikash/stories/`
   - A prep checklist (unchecked items)

2. **Update `users/vikash/desired_companies.md`** — change the company's status from 🔴 to 🟢

## Output Structure

After running, the company folder should look like:

```
companies/{company_name}/
├── README.md                  # Overview + prep checklist
├── culture_principles.md      # Synthesized principles with interview signals
├── interview_process.md       # Synthesized interview loop guide
└── _raw/                      # Raw web dumps
    ├── official_culture.md
    ├── interview_guide.md
    └── ...
```

## Examples

**Example 1: Well-documented company**
> User: "Research Netflix for interview prep"
> Agent: Runs 6 searches, reads 12 sources, dumps 8 raw files. Produces `culture_principles.md` (Netflix Culture Memo: Freedom & Responsibility, Keeper Test, Context Not Control, etc.) and `interview_process.md` (phone screen → case study → onsite loop). Updates tracker to 🟢.

**Example 2: Smaller/newer company**
> User: "Build a dossier for Anthropic"
> Agent: Runs 7 searches, reads 10 sources. Finds limited public interview process info. Produces `culture_principles.md` (safety-first, intellectual honesty, alignment focus) with confidence notes. `interview_process.md` includes a Gaps section noting limited public data on loop structure. Updates tracker to 🟢.

**Example 3: Batch mode**
> User: "Research all companies on my list that are still 🔴"
> Agent: Reads `desired_companies.md`, identifies unstarted companies, runs the protocol for each sequentially.

## When to Use

- User says "research {company}", "interview prep for {company}", "build a dossier"
- User asks about a company's culture, values, or interview process
- User wants to fill in their company research tracker
- User says "research all companies" or "fill in the red ones"

- NOT for: General PM interview frameworks (that's the `framework/` directory)
- NOT for: Personal story writing (that's the `users/vikash/stories/` directory)
- NOT for: Scheduling or calendar management
