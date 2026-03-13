# Google, Nvidia, and OpenAI

**Source**: https://stratechery.com/2025/google-nvidia-and-openai/

---

Google, Nvidia, and OpenAI – Stratechery by Ben Thompson
Skip to content
By Ben Thompson
About
Email/RSS
@benthompson
Explore
Concepts
Companies
Topics
Stratechery
Plus
Subscribe
Log In
Learn More
Member Forum
Menu
Search
×
Stratechery
Plus
Subscribe
Log In
Learn More
Member Forum
By Ben Thompson
About
Email/RSS
@benthompson
Explore
Concepts
Companies
Topics
More by Ben Thompson
Updates
Interviews
Year in Review
All Articles
Latest Podcast
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
Sharp China
|
Mar 12
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
Google, Nvidia, and OpenAI
Monday, December 1, 2025
Listen to Podcast
Watch on YouTube
Listen to this
post
:
Log in to listen
A common explanation as to why
Star Wars
was such a hit, and continues to resonate nearly half a century on from its release, is that it is a nearly perfect representation of the hero’s journey. You have Luke, bored on Tatooine, called to adventure by a mysterious message borne by R2-D2, that he initially refuses; a mentor in Obi-Wan Kenobi leads him across the threshold of leaving Tatooine and facing tests while finding new enemies and allies. He enters the cave — the Death Star — escapes after the ordeal of Obi-Wan’s death, and carries the battle station’s plans to the rebels while preparing for the road back to the Death Star. He trusts the force in his final test and returns transformed. And, when you zoom out to the entire original trilogy, it’s simply an expanded version of the story: this time, however, the ordeal is the entire second movie: the Empire Strikes Back.
The heroes of the AI story over the last three years have been two companies: OpenAI and Nvidia. The first is a startup called, with the release of ChatGPT, to be
the next great consumer tech company
; the other was best known as a gaming chip company
characterized by boom-and-bust cycles
driven by their visionary and endlessly optimistic founder, transformed into the most essential infrastructure provider for the AI revolution. Over the last two weeks, however, both have entered the cave and are facing their greatest ordeal: the Google empire is very much striking back.
Google Strikes Back
The first Google blow was Gemini 3, which scored better than OpenAI’s state of the art model on a host of benchmarks (even if actual real-world usage was a bit more uneven). Gemini 3’s biggest advantage is its sheer size and the vast amount of compute that went into creating it; this is notable because OpenAI has had difficulty creating the next generation of models beyond the
GPT-4
level of size and complexity. What has carried the company is a genuine breakthrough in reasoning that produces better results in many cases, but at the cost of time and money.
Gemini 3’s success seemed like good news for Nvidia, who
I listed as a winner from the release
:
This is maybe the most interesting one. Nvidia, which reports earnings later today, is on one hand a loser, because the best model in the world was not trained on their chips, proving once and for all that it is possible to be competitive without paying Nvidia’s premiums.
On the other hand, there are two reasons for Nvidia optimism. The first is that everyone needs to respond to Gemini, and they need to respond now, not at some future date when their chips are good enough. Google started its work on TPUs a decade ago; everyone else is better off sticking with Nvidia, at least if they want to catch up. Secondly, and relatedly, Gemini re-affirms that the most important factor in catching up — or moving ahead — is more compute.
This analysis, however, missed one important point: what if Google sold its TPUs as an alternative to Nvidia? That’s exactly what the search giant is doing, first with a deal with Anthropic, then a rumored deal with Meta, and third with the second wave of neoclouds, many of which started as crypto miners and are leveraging their access to power to move into AI. Suddenly it is Nvidia that is in the crosshairs, with fresh questions about their long term growth, particularly at their sky-high margins, if there were in fact
a legitimate competitor to their chips
. This does, needless to say, raise the pressure on OpenAI’s next pre-training, run on Nvidia’s Blackwell chips: the base model still matters, and OpenAI needs a better one, and Nvidia needs evidence one can be created on their chips.
What is interesting to consider is which company is more at risk from Google, and why? On one hand Nvidia is making tons of money, and if Blackwell is good, Vera Rubin promises to be even better; moreover, while
Meta might be a natural Google partner
, the other hyperscalers are not. OpenAI, meanwhile, is losing more money than ever, and is spread thinner than ever, even as the startup agrees to buy ever more compute with revenue that doesn’t yet exist. And yet, despite all that — and while still being quite bullish on Nvidia — I still like OpenAI’s chances more. Indeed, if anything my biggest concern is that I seem to like OpenAI’s chances better than OpenAI itself.
Nvidia’s Moats
If you go back a year or two, you might make the case that Nvidia had three moats relative to TPUs: superior performance, significantly more flexibility due to GPUs being more general purpose than TPUs, and CUDA and the associated developer ecosystem surrounding it. OpenAI, meanwhile, had the best model, extensive usage of their API, and the massive number of consumers using ChatGPT.
The question, then, is what happens if the first differentiator for each company goes away? That, in a nutshell, is the question that has been raised over the last two weeks: does Nvidia preserve its advantages if TPUs are as good as GPUs, and is OpenAI viable in the long run if they don’t have the unquestioned best model?
Nvidia’s flexibility advantage is a real thing; it’s not an accident that the fungibility of GPUs across workloads was focused on as a justification for increased capital expenditures by both Microsoft and Meta. TPUs are more specialized at the hardware level, and more difficult to program for at the software level; to that end, to the extent that customers care about flexibility, then Nvidia remains the obvious choice.
CUDA, meanwhile, has long been a critical source of Nvidia lock-in, both because of the low level access it gives developers, and also because there is a developer network effect: you’re just more likely to be able to hire low level engineers if your stack is on Nvidia. The challenge for Nvidia, however, is that the “big company” effect could play out with CUDA in the opposite way to the flexibility argument. While big companies like the hyperscalers have the diversity of workloads to benefit from the flexibility of GPUs, they also have the wherewithal to build an alternative software stack. That they did not do so for a long time is a function of it simply not being worth the time and trouble; when capital expenditure plans reach the hundreds of billions of dollars, however what is “worth” the time and trouble changes.
A useful analogy here is the rise of AMD in the datacenter. That rise has not occurred in on-premises installations or the government, which is still dominated by Intel; rather, large hyperscalers found it worth their time and effort to rewrite extremely low level software to be truly agnostic between AMD and Intel, allowing the former’s lead in performance to win the battle. In this case, the challenge Nvidia faces is that its market is a relatively small number of highly concentrated customers, with the resources — mostly as yet unutilized — to break down the CUDA wall, as they already did in terms of Intel’s differentiation.
It’s clear that Nvidia has been concerned about this for a long time; this is from
Nvidia Waves and Moats
, written at the absolute top of the Nvidia hype cycle after the 2024 introduction of Blackwell:
This takes this Article full circle: in the before-times, i.e. before the release of ChatGPT, Nvidia was building quite the (free) software moat around its GPUs; the challenge is that it wasn’t entirely clear who was going to use all of that software. Today, meanwhile, the use cases for those GPUs is very clear, and those use cases are happening at a much higher level than CUDA frameworks (i.e. on top of models); that, combined with the massive incentives towards finding cheaper alternatives to Nvidia, means both the pressure to and the possibility of escaping CUDA is higher than it has ever been (even if it is still distant for lower level work, particularly when it comes to training).
Nvidia has already started responding: I think that
one way to understand DGX Cloud
is that it is Nvidia’s attempt to capture the same market that is still buying Intel server chips in a world where AMD chips are better (because they already standardized on them); NIM’s are another attempt to build lock-in.
In the meantime, though, it remains noteworthy that Nvidia appears to not be taking as much margin with Blackwell as many may have expected; the question as to whether they will have to give back more in future generations will depend on not just their chips’ performance, but also on re-digging a software moat increasingly threatened by the very wave that made GTC such a spectacle.
Blackwell margins are doing just fine, I should note, as they should be in a world where everyone is starved for compute. Indeed, that may make this entire debate somewhat pointless: implicit in the assumption that TPUs might take share from GPUs is that for one to win the other must lose; the real decision maker may be TSMC, which makes both chips, and is positioned to be
the real brake on the AI bubble
.
ChatGPT and Moat Resiliency
ChatGPT, in contrast to Nvidia, sells into two much larger markets. The first is developers using their API, and —
according to OpenAI, anyways
— this market is much stickier and reticent to change. Which makes sense: developers using a particular model’s API are seeking to make a good product, and while everyone talks about the importance of avoiding lock-in, most companies are going to see more gains from building on and expanding from what they already know, and for a lot of companies that is OpenAI. Winning business one app by one will be a lot harder for Google than simply making a spreadsheet presentation to the top of a company about upfront costs and total cost of ownership. Still, API costs will matter, and here Google almost certainly has a structural advantage.
The biggest market of all, however, is consumer, Google’s bread-and-butter. What makes Google so dominant in search, impervious to both competition and regulation, is that billions of consumers choose to use Google every day — multiple times a day, in fact. Yes, Google helps this process along with
its payments to its friends
, but
that’s downstream from its control of demand, not the driver
.
What is paradoxical to many about this reality is that the seeming fragility of Google’s position — competition really is a click away! — is in fact its source of strength. From
United States v. Google
:
Increased digitization leads to increased centralization (the opposite of what many originally assumed about the Internet). It also provides a lot of consumer benefit — again, Aggregators win by building ever better products for consumers — which is why Aggregators are broadly popular in a way that traditional monopolists are not. Unfortunately, too many antitrust-focused critiques of tech have missed this essential difference…
There is certainly an argument to be made that Google, not only in Shopping but also in verticals like local search, is choking off the websites on which Search relies by increasingly offering its own results. At the same time, there is absolutely nothing stopping customers from visiting those websites directly, or downloading their apps, bypassing Google completely. That consumers choose not to is not because Google is somehow restricting them — that is impossible! — but because they don’t want to. Is it really the purview of regulators to correct consumer choices willingly made?
Not only is that answer “no” for philosophical reasons, it should be “no” for pragmatic reasons, as the ongoing Google Shopping saga in Europe demonstrates. As
I noted last December
, the European Commission keeps changing its mind about remedies in that case, not because Google is being impertinent, but because seeking to undo an Aggregator by changing consumer preferences is like pushing on a string.
The CEO of a hyperscaler can issue a decree to work around CUDA; an app developer can decide that Google’s cost structure is worth the pain of changing the model undergirding their app; changing the habits of 800 million+ people who use ChatGPT every week, however, is a battle that can only be fought individual by individual. This is ChatGPT’s true difference from Nvidia in their fight against Google.
The Moat Map and Advertising
This is, I think, a broader point: the naive approach to moats focuses on the cost of switching; in fact, however, the more important correlation to the strength of a moat is the number of unique purchasers/users.
This is certainly one of the simpler charts I’ve made, but it’s not the first in the moat genre; in 2018’s
The Moat Map
I argued that you could map large tech companies across two spectrums. First, the degree of supplier differentiation:
Second, the extent to which a company’s network effects were externalized:
Putting this together gave you the Moat Map:
What you see in the upper right are platforms; the lower left are Aggregators. Platforms like the App Store enable differentiated suppliers, which lets them profitably take a cut of purchases driven by those differentiated suppliers; Aggregators, meanwhile, have totally commoditized their suppliers, but have done so in the service of maximizing attention, which they can monetize through advertising.
It’s the bottom left that I’m describing with the simplistic graph above: the way to commoditize suppliers and internalize network effects is by having a huge number of unique users. And, by extension, the best way to monetize that user base — and to achieve a massive user base in the first place — is through advertising.
It’s so obvious the bottom left is where ChatGPT sits. At one point it didn’t seem possible to commoditize content more than Google or Facebook did, but that’s exactly what LLMs do: the answers are a statistical synthesis of all of the knowledge the model makers can get their hands on, and are completely unique to every individual; at the same time, every individual user’s usage should, at least in theory, make the model better over time.
It follows, then, that ChatGPT should obviously have an advertising model. This isn’t just a function of needing to make money: advertising would make ChatGPT a better product. It would have more users using it more, providing more feedback; capturing purchase signals —
not from affiliate links, but from personalized ads
— would create a richer understanding of individual users, enabling better responses. And, as an added bonus — and one that is very pertinent to this Article — it would dramatically deepen OpenAI’s moat.
Google’s Advantages
It’s not out of the question that Google can win the fight for consumer attention. The company has a clear lead in image and video generation, which is one reason why I wrote about
The YouTube Tip of the Google Spear
:
In short, while
everyone immediately saw how AI could be disruptive to Search
, AI is very much a sustaining innovation for YouTube: it increases the amount of compelling content in absolute terms, and it does so with better margins, at least in the long run.
Here’s the
million
billion
trillion dollar question: what is going to matter more in the long run, text or video? Sure, Google would like to dominate everything, but if it had to choose, is it better to dominate video or dominate text? The history of social networking that I documented above suggests that video is, in the long run, much more compelling to many more people.
To put it another way, the things that people in tech and media are interested in has not historically been aligned with what actually makes for the largest service or makes the most money: people like me, or those reading me, care about text and ideas; the services that matter specialize in videos and entertainment, and to the extent that AI matters for the latter YouTube is primed to be the biggest winner, even as the same people who couldn’t understand why Twitter didn’t measure up to Facebook go ga-ga over text generation and coding capabilities.
Google is also obviously capable of monetizing users, even if they haven’t turned on ads in Gemini yet (although they have in AI Overviews). It’s also worth pointing out,
as Eric Seufert did in a recent Stratechery Interview
, that Google started monetizing Search less than two years after its public launch; it is search revenue, far more than venture capital money, that has undergirded all of Google’s innovation over the years, and is what makes them a behemoth today. In that light OpenAI’s refusal to launch and iterate an ads product for ChatGPT — now three years old — is a dereliction of business duty, particularly as the company signs deals for over a trillion dollars of compute.
And, on the flip side, it means that Google has the resources to take on ChatGPT’s consumer lead with a World War I style war of attrition; OpenAI’s lead should be unassailable, but the company’s insistence on monetizing solely via subscriptions, with a degraded user experience for most users and price elasticity challenges in terms of revenue maximization, is very much opening up the door to a company that actually cares about making money.
To put it another way, the long-term threat to Nvidia from TPUs is margin dilution; the challenge of physical products is you do have to actually charge the people who buy them, which invites potentially unfavorable comparisons to cheaper alternatives, particularly as buyers get bigger and more price sensitive. The reason to be more optimistic about OpenAI is that an advertising model flips this on its head: because users don’t pay, there is no ceiling on how much you can make from them, which, by extension, means that the bigger you get the better your margins have the potential to be, and thus the total size of your investments. Again, however, the problem is that the advertising model doesn’t yet exist.
A Theory’s Journey
I started this Article recounting the hero’s journey, in part to make the easy leap to “The Empire Strikes Back”; however, there was a personal angle as well. The hero of this site has been
Aggregation Theory
and the belief that controlling demand trumps everything else; there Google was
my ultimate protagonist
. Moreover, I do believe in the innovation and velocity that comes from a founder-led company like Nvidia, and I do still worry about Google’s bureaucracy and disruption potential making the company less nimble and aggressive than OpenAI. More than anything, though, I believe in the market power and defensibility of 800 million users, which is why I think ChatGPT still has a meaningful moat.
At the same time, I understand why the market is freaking out about Google: their structural advantages in everything from monetization to data to infrastructure to R&D is so substantial that you understand why OpenAI’s founding was motivated by the fear of Google winning AI. It’s very easy to imagine an outcome where Google’s inputs simply matter more than anything else, which is to say one of my most important theories is being put to the ultimate test (which, perhaps, is why I’m so frustrated at OpenAI’s avoidance of advertising). Google is now my antagonist!
Google has already done this once: Search was the ultimate example of a company winning an open market with nothing more than a better product. Aggregators win new markets by being better; the open question now is whether one that has already reached scale can be dethroned by the overwhelming application of resources, especially when its inherent advantages are diminished by refusing to adopt an Aggregator’s optimal business model. I’m nervous — and excited — to see how far Aggregation Theory really goes.
I wrote a follow-up to this Article in
this Daily Update
.
Share
Share on Facebook (Opens in new window)
Facebook
Share on X (Opens in new window)
X
Share on LinkedIn (Opens in new window)
LinkedIn
Email a link to a friend (Opens in new window)
Email
Related
David Carr’s Doubt
Date
Friday, February 13, 2015
Dust in the Light
Date
Tuesday, June 2, 2020
What Steve Jobs Wouldn’t Have Done
Date
Friday, June 6, 2014
←
2025.47: Gemini! At The Disco
2025.49: Conflicts, Consternation, and Code Red
→
Search
×
Stratechery
Plus
Updates
An Interview with Robert Fishman About the Current State of Hollywood
Thursday, March 12, 2026
Oracle Earnings, Oracle’s Cloud Growth, Oracle’s Software Defense
Wednesday, March 11, 2026
Copilot Cowork, Anthropic’s Integration, Microsoft’s New Bundle
Tuesday, March 10, 2026
View All
Stratechery
Plus
Podcasts
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
Sharp China
|
Mar 12
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
MacBook Neo Review
Dithering
|
Mar 10
MacBook Neo Review
Tatum and the Team Test, The Spurs Continue to Defy Young Team Gravity, Russ Takes Aim at Kings Reporters
Greatest Of All Talk
|
Mar 9
Tatum and the Team Test, The Spurs Continue to Defy Young Team Gravity, Russ Takes Aim at Kings Reporters
Stratechery
Plus
Interviews
An Interview with Robert Fishman About the Current State of Hollywood
Thursday, March 12, 2026
An Interview with Gregory Allen About Anthropic and the U.S. Government
Thursday, March 5, 2026
An Interview with Bill Gurley About Runnin’ Down a Dream
Thursday, February 26, 2026
View All
Sharp Text
Articles
The End of the World As We Know It
Friday, March 6, 2026
The NBA’s Problems Are Structural, Cultural and Fixable
Friday, February 20, 2026
Takaichi, Tanking and Legalization Lessons
Friday, February 13, 2026
View All
More by Ben Thompson
Year in Review
The most popular and most important posts on Stratechery by year.
View All
All Articles
Explore all free articles on Stratechery
.
View All
All Content
Explore all posts on Stratechery
.
View All
Stratechery
Plus
UpdateS
An Interview with Robert Fishman About the Current State of Hollywood
Thursday, March 12, 2026
Oracle Earnings, Oracle’s Cloud Growth, Oracle’s Software Defense
Wednesday, March 11, 2026
Copilot Cowork, Anthropic’s Integration, Microsoft’s New Bundle
Tuesday, March 10, 2026
View All
Stratechery
Plus
Podcasts
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
Sharpchina
|
Mar 12
(Preview) The ‘Raising a Lobster’ Frenzy; Iran and US-China as Trump’s Visit Looms; Two Sessions Takeaways
MacBook Neo Review
Dithering
|
Mar 10
MacBook Neo Review
Tatum and the Team Test, The Spurs Continue to Defy Young Team Gravity, Russ Takes Aim at Kings Reporters
Greatest Of All Talk
|
Mar 9
Tatum and the Team Test, The Spurs Continue to Defy Young Team Gravity, Russ Takes Aim at Kings Reporters
Stratechery
Plus
Interviews
An Interview with Robert Fishman About the Current State of Hollywood
Thursday, March 12, 2026
An Interview with Gregory Allen About Anthropic and the U.S. Government
Thursday, March 5, 2026
An Interview with Bill Gurley About Runnin’ Down a Dream
Thursday, February 26, 2026
View All
©
Stratechery LLC
2026 |
Terms of Service
|
Privacy Policy
Designed with WordPress.
Hosted by Pressable.
Search results
Magnifying Glass
Search
Close search results
Filters
Show filters
Sort by:
Relevance
•
Newest
•
Oldest
No results found
Filter options
Close Search
Search powered by Jetpack