---
name: resume_tailor
description: >
  Build a JD-tailored resume and score its match against a target role. Trigger on:
  "build a resume for [role/company]", "tailor my resume", "score my resume against this JD",
  "how well do I match this role", "resume for this job", "ATS-optimize my resume".
  Combines resume generation with JD-match scoring into a single skill.
---

# Resume Tailor

Builds a role-specific resume from verified career sources and scores it against a target job description. Produces an ATS-optimized resume and a match report with gap analysis.

## References
- `references/career_sources.md` — Verified career facts and accomplishments
- `references/ats_mechanics.md` — ATS parsing rules and keyword optimization
- `references/jd_parse_protocol.md` — How to parse and profile a JD
- `references/resume_standards.md` — Resume formatting and content standards

## Templates
- `templates/resume_template.md` — Standard resume output format
- `templates/match_report_template.md` — JD match scoring report format

## Output
```
users/vikash/applications/{company}-{role-slug}/resume.md
users/vikash/applications/{company}-{role-slug}/match_report.md
```

## When to Use
- "Build/tailor a resume for {role/company}"
- "Score my fit for this JD"
- "How well do I match this role?"
- Before running `application_writer` for a cover letter
