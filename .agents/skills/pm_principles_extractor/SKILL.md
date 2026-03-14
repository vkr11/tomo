---
name: pm_principles_extractor
description: Extract and synthesize PM interview-ready leadership principles from a directory of markdown files (blog posts, transcripts, essays). Use whenever the user asks to "extract principles", "summarize blogs for interviews", "get PM takeaways", "analyze leadership posts", or wants to convert a collection of articles into a structured interview prep guide.
---

# PM Principles Extractor

Convert a directory of markdown blog posts, transcripts, or essays into a structured set of Product Management interview principles. Works with any author — the skill is author-agnostic and discovers recurring themes automatically.

## Setup Requirements

None. This is a prompt-only skill — no scripts, dependencies, or API keys required.

## How to Use

### Step 1 — Gather Inputs

| Input | Required | Source |
|---|---|---|
| **Directory path** | Yes | Path to a folder of `.md` files (e.g., `~/code/tomo/reference/boz/posts/`) |
| **Author name** | Yes | Infer from directory name or ask the user |
| **Source URL** | Optional | The blog's URL (e.g., `boz.com`, `debliu.substack.com`) |
| **Max principles** | Optional | Default: 7-10. The user can request fewer for a tighter summary. |

### Step 2 — Read and Analyze

1. Read all `.md` files in the specified directory. For large collections (>50 files), sample broadly — read at least 20-30 representative posts spanning different dates and topics. Use `grep_search` to identify thematic clusters before deep-reading.
2. Identify the author's 7-10 most recurring and distinctive themes. Look for:
   - Concepts the author names explicitly (e.g., "Demand Side Problems", "CTFOIGT")
   - Frameworks or mental models they return to across multiple posts
   - Contrarian or distinctive positions (not just generic advice)
   - Actionable leadership patterns (not just philosophical musings)
3. For each theme, identify the 2-3 strongest source posts that articulate it.

### Step 3 — Generate the Principles Document

Use the following template. Replace `{PLACEHOLDERS}` with discovered content.

---

**PROMPT START**

You are a senior PM career coach creating an interview preparation guide from a leader's written body of work. Your audience is experienced product managers preparing for behavioral interviews at top tech companies.

**INPUTS:**
- Author: `{AUTHOR_NAME}`
- Source: `{SOURCE_URL}`
- Number of posts analyzed: `{N_POSTS}`
- Post titles and content: `{POSTS}`

**OUTPUT FORMAT — follow this template exactly:**

```markdown
# {Author Name} — PM Interview Principles

> Extracted from {N} posts at {source_url}

---

## 1. {Principle Name}

**One-liner:** {A single sharp sentence capturing the principle — something quotable.}

**Sources:** {Post title 1}, {Post title 2}

**The Insight:** {2-3 sentences on what the author argues in their own framing. Use their terminology and specific examples. Don't genericize — preserve what makes this author's take distinctive.}

**Interview Application:** {When asked about [specific interview question type], use this principle to frame your answer. Be concrete about which behavioral question this maps to.}

**Example Phrasing:** {A sample sentence a candidate could naturally use in an interview, e.g., "In my experience, I've found that the marginal value of more information often falls below the cost of delay, so I..."}

---

## 2. {Principle Name}
...
```

**RULES:**
1. **7-10 principles max.** Quality over quantity. Each principle should be genuinely distinct — if two principles feel like the same idea, merge them.
2. **Preserve the author's voice.** Use their exact terminology (e.g., Boz says "CTFOIGT", not "calm things down"). The specificity is what makes this useful.
3. **Map to real interview questions.** The "Interview Application" section should reference specific question archetypes: "Tell me about a time you disagreed with leadership", "How do you handle ambiguity", "Describe a failure", etc.
4. **Actionable example phrasing.** The "Example Phrasing" should sound natural in conversation, not like a textbook. Use first person.
5. **Cite specific posts.** Every principle must reference at least 2 source posts by title to show it's a recurring theme, not a one-off.
6. **Prioritize contrarian takes.** Generic advice ("communication is important") is less valuable than distinctive frameworks ("Layer your message for second-order audiences"). Prefer the latter.
7. **No filler.** If you can't find 7 genuinely distinct principles, output fewer. Never pad.

**PROMPT END**

---

### Step 4 — Save the Output

Save the generated markdown file in the same parent directory as the posts:

```
{directory}/
├── posts/
│   ├── post-1.md
│   └── post-2.md
└── {author}_pm_principles.md   ← output goes here
```

Use the naming convention `{author_slug}_pm_principles.md` (e.g., `boz_pm_principles.md`, `debliu_pm_principles.md`).

## Examples

### Example 1: Single author directory

```
User: Extract PM principles from the boz blog posts in ~/code/tomo/reference/boz/posts/
```

The agent reads the posts, identifies recurring themes, and generates `~/code/tomo/reference/boz/boz_pm_principles.md`.

### Example 2: Batch processing multiple authors

```
User: Generate PM principles for all the blogs in ~/code/tomo/reference/
```

The agent finds all subdirectories with a `posts/` folder, processes each one, and saves a `{author}_pm_principles.md` in each.

### Example 3: Focused extraction

```
User: Extract PM principles about leadership and conflict from the amivora posts
```

The agent reads the posts but focuses specifically on the requested themes, producing a narrower set of principles.

## When to Use

- When the user asks to extract PM principles or interview insights from a collection of blog posts
- When the user asks to "summarize" or "analyze" a leader's blog for interview preparation
- When the user has downloaded blog posts and wants a structured study guide
- When the user says "create principles from these posts" or "what can I learn from this blog"
- NOT for: summarizing a single blog post (just read it directly)
- NOT for: generating key takeaways from video transcripts (use `video_key_takeaways` instead)
- NOT for: general web research (use `deep_research` instead)
