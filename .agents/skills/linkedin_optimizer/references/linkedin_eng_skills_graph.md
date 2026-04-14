Building LinkedIn's Skills Graph to Power a Skills-First World





[Skip to main content](#lithograph-app)

[Skills Graph](https://www.linkedin.com/blog/engineering/skills-graph)

# Building LinkedIn's Skills Graph to Power a Skills-First World

![Sofus Macskássy](https://media.licdn.com/dms/image/v2/D5603AQHILv18AE2lNw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1724184179333?e=2147483647&v=beta&t=ftWL5KBLdcvfA0HQ7BW4U6lDQLsRY-RQXlKlHtMHphY)

[Authored bySofus Macskássy](https://www.linkedin.com/in/sofusmacskassy)

Building \_the\_ platform for Context and Semantics for Enterprise AI.

November 30, 2022

![](https://media.licdn.com/dms/image/v2/D4D08AQGup-0wthDlig/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1700687614555?e=2147483647&v=beta&t=w0qTkV5BvkrE-qF9I7455QoChBbzXB9hFR6VjyU2p98)

*Co-authors: [Sofus Macskássy](https://www.linkedin.com/in/sofusmacskassy/), [Yi Pan](https://www.linkedin.com/in/yi-pan-35771a15/), [Ji Yan](https://www.linkedin.com/in/curiousitylens/), [Yanen Li,](https://www.linkedin.com/in/yanen-li-6a3b438/) [Di Zhou,](https://www.linkedin.com/in/dizhou/) [Shiyong Lin](https://www.linkedin.com/in/shiyong-lin-68908b9/)*

As industries rapidly evolve, so do the skills necessary for success. Skill sets for jobs globally [have changed by 25% since 2015](https://www.linkedin.com/pulse/skills-first-blueprint-better-job-outcomes-karin-kimbrough/) and this number is expected to double by 2027. Yet, we’ve long relied on insufficient and unequal signals when evaluating talent and predicting success - who you know, where you went to school, or who your last employer was. If we look at the labor market instead through the lens of skills - the skills you have and the skills a role or industry demands - we can create a transparent and fair job matching process that drives better outcomes for employers and employees.

This new reality requires a common understanding of skills, backed by better data. For nearly a decade, our [Economic Graph](https://economicgraph.linkedin.com/) has helped leaders benchmark and compare labor markets and economies across the world. A critical element of this analysis is the insight provided by LinkedIn’s Skills Graph, which creates a common language around skills to help us all better understand the skills that power the global workforce. The Skills Graph does this by dynamically mapping the relationships between 39K skills, 875M people, 59M companies, and other organizations globally.

It also drives relevance and matching across LinkedIn – helping learners find content more relevant to their career path; helping job seekers find jobs that are a good fit; and helping recruiters find the highest quality candidates. For example, these relationships between skills means we can detect that "cost management" in a job seekers' profile is relevant to a job posting that lists "project budgeting" as a required skill.

## Building the LinkedIn Skills Graph

At the heart of our Skills Graph lies our skills taxonomy. The taxonomy is a curated list of unique skills and their intertwined relationships, each with detailed information about those skills. It's built on a deep understanding of how skills power professional journeys, including what skills are required in a job, what skills a member has, and how members move from one position to the next.

Today, our taxonomy consists of over 39,000 skills spanning 26 languages, over 374,000 aliases (different ways to refer to the same skill - e.g., "data analysis" and "data analytics"), and more than 200,000 links between skills. Even more important than the volume of data, the key to unlocking the power of skills lies in the structure and relationships between the skills. To create a stronger network of connected skills in our taxonomy, we utilize a framework we call, “Structured Skills.” This framework increases our understanding of every skill in our database by mapping the relationships it has to other skills around it, and creates richer, more accurate skill-driven experiences for our members and customers. For example,

* If a member knows about **Artificial Neural Networks**, the member knows something about **Deep Learning**, which means the member knows something about **Machine Learning**.
* If a job requires **Supply Chain Engineering**, having a skill in **Supply Chain Management** or **Industry Engineering** is definitely also relevant.

Creating meaningful and accurate relationships between skill sets is critical to getting the most out of our Structured Skills. To do this, our machine learning and artificial intelligence combs through massive amounts of data and suggests new skills and relations between them. As our Skills Graph continues to grow and learn with AI, we are committed to maintaining the high quality of the data and connections found in our taxonomy. We do this with the help of trained taxonomists on our team, who manually review our skills data and ensure that we can verify its integrity and relevancy.

![]()

*Structured skills consists of meaningful relationships between skills that empower deep reasoning to match members to relevant content such as jobs, learning material, and feed posts*

But, building the taxonomy and Structured Skills is meaningless without connecting these to the jobs and members on our platform. Together, the Structured Skills and mapping to our members and jobs make up our Skills Graph and both are needed to unlock the full potential of a skill-based job market.

![]()

*Structured skills enrich the set of skills for both members and jobs to ensure we can find all the relevant jobs for a member. We show the skill overlap so that members can see which of their skills are a match and also potential skill gaps that they might want to address for their own career growth*

## Leveraging Machine Learning to map skills to members and jobs

Although millions of LinkedIn members have added skills to their profile, many have not added their most relevant skills to their skills sections or kept their skills section up to date. Instead, they list relevant skills in their summary sections, within the job experience descriptions in their profiles or on the resumes they submit. On the other hand, many jobs on LinkedIn don’t comprehensively describe what skills are needed. Many listings also come through an online job posting that a recruiter has submitted but are ingested from our customers’ websites. In these scenarios where skills are not explicitly provided, it’s critical to pull skills data from the job descriptions, summaries, and more, to create a tool that drives reliable insights.

As you can imagine, this process requires processing a lot of text. So, we have built machine learning models that leverage natural language understanding, deep learning, and information extraction technologies. To help train these models, our human labelers use AI to connect text found across jobs, profiles, and learning courses, to specific skills in our taxonomy. Our system then learns to recognize different ways to refer to the same type of skill. Combined with natural language processing, we extract skills from many different types of text - with a high degree of confidence - to make sure we have high coverage and high precision when we map skills to our members and job posts.

We also leverage various clustering and machine learning algorithms to identify the core skills relating to a given job or function. We do this by applying these tools to all member histories and all job descriptions on our platform, which identify the skills that are likely associated with a job post or member job experience. These techniques, together with Structured Skills, create a holistic picture of skills a member has and skills needed to do a job.

![]()

*When hirers create a job post on the LinkedIn platform, we use machine learning and Structured skills to suggest explicit skills that we can tag the post with to increase discoverability*

These models are designed to continuously improve and learn over time based on engagement from members on the LinkedIn platform, job seekers, hirers, and learners. For example, when a hirer posts a new job on our platform and the hirer types in the job description, our machine learning model automatically suggests the skills that are associated with that job posting. The hirer can refine the selection of skills that best represent the qualification of this job by removing and adding these suggested skills manually.

## Looking forward

Beyond streamlining the hiring process, understanding members’ skills allows us to surface more relevant posts in their feed, suggest people they should connect with, and companies to follow. It also helps sales and marketing professionals on Linkedin be more effective by using skills for ads targeting and provides insights to our sales and marketing customers by sharing details on the skill sets of those who engage with their content. As our Skills Graph continues to evolve in parallel with the global workforce, it will only become smarter and deliver better outcomes for hirers, learners, job seekers, customers, and members.

Realizing a more equitable and efficient future of work will rely on building a deeper understanding of peoples’ abilities and potential. To keep up, some companies are already utilizing skills to identify qualified candidates – more than [40% of hirers](https://www.linkedin.com/pulse/skills-new-currency-ryan-roslansky/) on LinkedIn explicitly use skills data to fill their roles.

As our CEO Ryan Roslansky stated at LinkedIn’s Talent Connect event this year, “We can build a world where everyone has access to opportunity not because of where they were born, who they know, or where they went to school, but because of their actual skills and ability.” Our Skills Graph will continue to be a critical part of how we help make a skills-based labor market a reality. We’re excited to share updates as our work continues on this journey.

---

Related articles
