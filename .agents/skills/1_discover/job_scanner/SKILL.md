---
name: job_scanner
description: Scans career pages and Applicant Tracking Systems (ATS) for open Product Manager roles at target companies. Extracts role titles, locations, and links, and logs them into an interview pipeline tracker. Use whenever the user says "scan for jobs at [company]", "find open PM roles", "check careers for [company]", or wants to update their interview pipeline with active job postings.
---

# Job Scanner

Automates finding and tracking open Product Manager roles at target tech companies. Given a company or list of companies, it navigates to their specific career portals, searches for relevant senior roles, and logs them into a central tracker.

## Setup Requirements

1. The tomo repo must exist at the path defined by `TOMO_REPO` env var (default: `~/code/tomo`)
2. The tracking file must exist at `users/vikash/strategy/interview_pipeline.md` (or similar configured path)
3. If a target uses an ATS that blocks standard web crawlers (like some Workday instances), the agent may need to use `playwright_automator` instead of `search_web`.

## Scan Protocol

Follow these 3 steps in order.

### Step 1: Locate

For each target company, consult `references/company_boards.md` to find:
- The official careers URL
- The ATS type (Workday, Greenhouse, Lever, Custom)
- Any specific search string modifiers (e.g., `jobFamily=Product%20Management`)

If the company is not in the reference list, use `search_web` to find their primary careers page first: `{company} careers product management`.

### Step 2: Scan & Extract

Navigate to the target URL and search for **Senior/Principal/Director Product Manager** roles.

**Method A: Targeted Web Search (Preferred)**
Use `search_web` with precise keywords restricted to the company's career domain.
*Example: `site:jobs.netflix.com "Product Manager" ("L6" OR "Senior" OR "Principal")`*

**Method B: Browser Automation (Fallback)**
If the site requires heavy JS rendering, pagination, or blocks search indexers (common with Workday), load the URL using the `playwright_automator` script, interact with the UI to filter by "Product", and extract the resulting HTML/text.

**Extraction Targets:**
For every matching role, extract:
1. Exact Job Title (e.g., "Senior Product Manager, Llama Safety")
2. Location(s) (e.g., "Menlo Park, CA" or "Remote")
3. Direct URL to the job description
4. Quick summary of the team/org if visible in the preview

*Filter out:* Junior roles, internships, non-product roles (Program Manager, Project Manager), and contract roles unless otherwise specified.

### Step 3: Log

Append the extracted roles to the user's tracking document (default: `users/vikash/strategy/interview_pipeline.md`).

For each newly discovered role, add a formatted entry under a **"Backlog / Recently Scanned"** section:

```markdown
- [ ] **{Company}**: [{Job Title}]({URL}) — {Location} | *Scanned: {YYYY-MM-DD}*
```

Do not overwrite existing entries. If the role already exists in the file, skip it.

## Examples

**Example 1: Single Company Scan**
> User: "Scan Netflix for new L6 PM roles"
> Agent: Checks `references/company_boards.md` for Netflix's URL. Runs a targeted web search on `jobs.netflix.com`. Finds 2 new roles ("Senior PM, Recommendations" and "L6 PM, Payments"). Opens `interview_pipeline.md` and appends the links.

**Example 2: Batch Target List**
> User: "Run the job scanner on my desired companies list"
> Agent: Reads `users/vikash/desired_companies.md`. For each company, locates their career board, scans for Senior PM roles, and generates a consolidated list of 8 new openings. Appends them all to the tracker.

## When to Use

- User says "scan for jobs at {company}" or "find open PM roles"
- User wants to update their interview pipeline with fresh links
- User asks "are there any senior roles open at {company} right now?"

- NOT for: Scraping non-job information (use `deep_research` or `company_researcher`)
- NOT for: Auto-applying to the jobs (this skill only extracts and logs links)
