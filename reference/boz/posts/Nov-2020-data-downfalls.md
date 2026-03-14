# Data Downfalls

*Source: https://boz.com/articles/data-downfalls*

# Data Downfalls

The first year I was at Facebook we always knew what to build. Most of us were
recent college graduates like our users, so building for ourselves was a
reasonable proxy. That era ended quickly as the product expanded globally.
Data became our best tool to understand the products we built and how people
use them. But data can mislead us. Forewarned is forearmed, so I want to raise
awareness of some of the pitfalls.

### Focalism

In the wake of the News Feed launch people were surprised we were willing to
cannibalize our page view numbers. Which was funny because in all the myriad
of discussions we had it never came up once; we just didn’t care about that
metric. We wanted people engaging and posting more content and as it turns
out, that’s exactly what happened. Activity doubled almost overnight and never
regressed.

I wonder what product we would have built instead if page views had been our
main metric.

Focalism is a cognitive bias that causes people to place too much importance
on one element of a decision rather than considering all the data. People
buying cars tend to focus on the odometer and year of the car rather than
maintenance records or a mechanical inspection. People building products tend
to focus on a small number of metrics when what makes a good or bad product
may be more holistic.

These are hard problems but we need to make sure we don’t let one rogue metric
dominate the discussion. Balancing many metrics that potentially compete seems
like a pretty good way to avoid myopic optimization. Deltoid is one example
of a tool designed to help unwind that complexity.

### Hard to Measure Success, Easy to Measure Failure

In the beginning looking through a photo album required an entire page load
for each new photo. We developed a new feature called photostream which
allowed people to browse photos much more quickly without reloading the page.
But as that meant the ad wouldn’t change it would negatively impact
advertising revenue. It was a hard debate to resolve because the hit to page
views and ad revenue was measurable while the benefit of the unlaunched
feature was not. But we launched it because we had a strong sense that the
value we were creating was greater than what we were losing.

There are a lot of situations where the cost of something is clear and easy to
measure but the benefit is difficult to measure (or vice versa). In such
situations, it can be pretty easy to let the data you do have outweigh the
data that you don’t have, but that doesn’t mean it is actually the right
course of action. Focalism is particularly difficult to avoid when there is
little else to focus on.

Fortunately, this is one we actually have done pretty well on, at least at a
strategic level. Consider our relentless focus on building user value (hard to
measure)
first and advertiser value (easier to measure) second. We believe the former
subsumes the latter in the long run. I think having a leader who is willing to
push teams beyond their local optima is crucial.

### Pareto Efficiency

When our site is faster our users spend more time on it overall. But certain
features can also cause our users to spend more time. How do we handle the
case where an engaging feature trades off against site speed? If we insist
that no metric ever decreases then we may be at a stalemate — the feature can
not expand without slowing the site down and the site can’t speed up without
limiting the feature.

When optimizing a global system with nonlinear interactions, some of the
subsystems are likely in suboptimal states. Each individual product, taken on
its own, might be better with purpose built controls. In contrast, the best
thing for the user, and Facebook, may be to use standard controls that are
visually consistent across all products and more performant.

In economics, a system of allocating resources that can not be changed without
making the allocation worse for at least one individual is said to be Pareto
Optimal. Sometimes we have to take leaps and accept that some things will get
worse in order to find a better overall balance of value.

### Complex Data

When developing Messenger we were lucky to have a user research team that
identified the dramatically different modalities of how people interact with
messaging products. Some people read everything and aggressively delete
messages, others just skim subjects and use search to navigate. If you looked
at data for average inbox size or number of read messages you would find
numbers that accurately described neither group, and if you built towards that
you would be building a solution that nobody likes.

It can be compelling to make data out to be simpler than it is. Normal curves
are so easy to understand and widely applicable that we can easily assume all
data fits such a model. The reality is that there are many cases where data is
multimodal or distributions are heavily weighted. Even for data that appears
to fit simple models, we can be deceived. Consider Simpson’s Paradox where a
trend observed in two different sample groups is reversed when the groups are
combined.

Vigilance is the only known solution to this issue.

### Analysis Paralysis

Sometimes data just doesn’t give us the answers. While we must be cautious
about letting our intuition misguide us, we must be willing to admit when it
is the best we have. There is a point where the marginal value of information
is below the value of immediate action. Being willing to launch quickly and
iterate is crucial here because it is the basis for future data.

I think this affects us a lot more than we recognize at Facebook. I have
personally been a part of countless discussions that debated the merit of a
feature for longer than it would have taken to build. We get caught up on hard
to agree upon questions like “how good is it?” as opposed to just building
something and then asking “how can we make it better?” We need to remember
that we settle arguments here with data one way or another, and if there is no
existing data the best way to get some is to build something. Launching gives
us an opportunity to be data driven.

At the same time, if you’re going to move ahead with no data you have to own
what comes. You can’t be surprised later if there’s something you could have
known with a little more due diligence.

### Bias

[Bias](https://en.wikipedia.org/wiki/List_of_cognitive_biases) is a pretty
obvious thing to be aware of when dealing with data but it bears mention.
There is a really long list of these for those who are interested, but here
are a few favorites:

Selection Bias - When we weigh what Facebook employees think of a product as
representative of our users. Novelty Effect - The tendency for metrics to
initially improve when new technology is deployed but not because of interest
in the technology itself but rather the novelty of it. Priming - We go to
great lengths to avoid this but it may still sneak in. If I hear a product is
bad before I use it I’m likely to react more negatively. If I know a friend of
mine worked on it I may be more likely to think it is good.

### Conclusion

Make no mistake, the only way to make progress as an organization in the long
term is to be data driven. I raise these pitfalls not to deter us but rather
to ensure we have the humility to avoid falling into the trap of False
Precision. We should be cautious about believing we understand things better
than we do. All of our data, our analysis, and our understanding thereof are
limited. Often, they are the best tool we have and we should use them but we
shouldn’t delude ourselves in believing that we can quantify and understand
everything that is going on. We should always make a best effort when it comes
to drawing on data, but accept that sometimes there are no easy answers when
charting new territories.

*(first written in 2010, updated for 2020)*

PublishedNov 18, 2020