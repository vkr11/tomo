# GLMix: Generalized Linear Mixed Models for Large-Scale Response Prediction
> *Reference Synthesis based on Zhang et al. (KDD 2016) and LinkedIn Engineering implementations.*

## 1. What is GLMix?
Before GLMix, standard machine learning models at LinkedIn treated all users and items using "global" features. If "Python" was a strong signal for a Software Engineering job, the model applied that weight globally across all candidates and recruiters.

GLMix changed this by introducing **ID-level Regression Coefficients**. The model trains:
1. **Global Coefficients:** How features perform across the entire platform.
2. **Per-User Coefficients:** How a specific user responds to specific features.
3. **Per-Item Coefficients:** How a specific job or recruiter interacts with specific features.

## 2. Why it Matters for LinkedIn Optimization (Recruiter Search)
This paper explains the "Personalization Layer" of LinkedIn Recruiter searches.

If two recruiters at two different companies (or even the same company) run the exact same search query (`"Product Manager" AND "Generative AI"` in San Francisco), **they will see entirely different rankings.**

### Why Rankings Diverge:
- **Recruiter A** historically sends InMails to candidates who have "Agentic Systems" in their profile, and those candidates tend to reply. They also tend to hire people who came from "Meta". 
- **Recruiter B** historically clicks on candidates with "Startup Founder" in their profile, and ignores candidates from big tech.

Under GLMix, the model automatically learns an *item-specific coefficient* for Recruiter A that massively weights the "Meta" company feature and "Agentic Systems" keyword feature, while down-weighting it for Recruiter B.

## 3. The Takeaway for Candidates
You cannot optimize for "the global algorithm" because the global algorithm is heavily overridden by the *recruiter's individual preferences*.

This is why **Tiered Keyword Strategy (Archetypes)** is critical. 
If you want to be hired by Frontier Labs (Archetype A), you must index heavily for *their* specific keywords (Model Alignment, Agentic Systems, Python/SQL) and avoid Enterprise GTM keywords. The GLMix coefficients for Anthropic recruiters are mathematically tuned to hunt for those specific research/builder keywords based on their past click history.

If your profile tries to be a "generalist PM" (blending startup, enterprise, and research keywords), the GLMix model won't strongly associate your embedding with *any* specific recruiter archetype, dropping you out of the top 50 results for all of them.
