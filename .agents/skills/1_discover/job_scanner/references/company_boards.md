# Company Career Boards Reference

A curated mapping of target companies to their official career pages and underlying ATS (Applicant Tracking Systems) to optimize the `job_scanner` extraction step.

## Target Companies

| Company | Careers URL | Platform / ATS | Notes & Queries |
|---|---|---|---|
| **Amazon** | [amazon.jobs](https://www.amazon.jobs/content/en/career-programs) | Custom (iCIMS backend) | Search param: `job_category[]=project-program-product-management-non-tech`. Often hides exact levels until the JD text. |
| **Google** | [careers.google.com](https://careers.google.com/jobs/results/) | Custom | Strongly indexed. Use `site:careers.google.com "Product Manager"`. Often requires JS rendering. |
| **Meta** | [metacareers.com](https://www.metacareers.com/jobs) | Custom | Parameter: `?roles=Product%20Management`. Requires scrolling/JS execution for full lists. |
| **Apple** | [jobs.apple.com](https://jobs.apple.com/en-us/search) | Custom | Highly walled. Use `site:jobs.apple.com "Product Manager"`. Levels (ICT4/ICT5) rarely stated explicitly in titles. |
| **Microsoft** | [jobs.careers.microsoft.com](https://jobs.careers.microsoft.com/global/en/search) | Custom | Good search indexing. Look for "Principal" or "Senior" in titles. |
| **Netflix** | [jobs.netflix.com](https://jobs.netflix.com/search) | Custom | Very clean site. Search param: `?q=Product%20Manager`. L6 is standard Senior level. |
| **Nvidia** | [nvidia.wd5.myworkdayjobs.com](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite) | Workday | *Hard to scrape via standard web search.* Usually requires `playwright` or direct Workday JSON API queries. |
| **OpenAI** | [openai.com/careers](https://openai.com/careers/search) | Greenhouse | Usually embedded Greenhouse forms (`boards.greenhouse.io/openai`). Easy to parse. |
| **Anthropic** | [anthropic.com/careers](https://www.anthropic.com/careers) | Lever | Embedded Lever board (`jobs.lever.co/anthropic`). Easy to parse. |
| **Uber** | [uber.com/us/en/careers/list](https://www.uber.com/us/en/careers/list/) | iCIMS/Custom | Filter by job family "Product". |
| **DoorDash** | [careers.doordash.com](https://careers.doordash.com/jobs) | Greenhouse | Easy to parse. Levels are clearly stated (L6/L7). |
| **Intuit** | [jobs.intuit.com](https://jobs.intuit.com/search-jobs) | Custom ATS | Search category "Product Management". |
| **Coupang** | [rock.coupang.com](https://rock.coupang.com/en/jobs/) | Greenhouse (typically) | Can vary by region, but US/Global roles are usually on standard ATS platforms. |

## Navigation Tips

1. **Greenhouse & Lever**: These are the easiest to scan. They rarely block basic automation and Google usually indexes their child pages well. E.g., `site:boards.greenhouse.io/openai`.
2. **Workday**: Extremely difficult to scan with simple web searches because the content is heavily gated behind aggressive single-page JS routing and anti-bot measures. If `search_web` fails on a Workday URL (like NVIDIA), strongly prefer spinning up `playwright_automator`.
3. **Levels**:
   - `L6` at Meta/Netflix/Amazon = "Senior" or "Principal" depending on the mapping
   - `L7` at Meta/Amazon = "Principal"
   - You may need to read the snippet text (years of experience reqs) to verify seniority if the title just says "Product Manager".
