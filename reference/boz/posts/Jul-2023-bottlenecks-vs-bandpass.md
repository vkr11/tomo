# Bottlenecks vs Bandpass

*Source: https://boz.com/articles/bandpass*

# Bottlenecks vs Bandpass

Work of any meaningful substance is likely to require many disciplines, more
than any one person can manage on their own. Some people are focused on
building the feature itself. They are from disciplines such as research,
engineering, and design. We often refer to these teams as vertical teams. Other
people [work across many products](https://boz.com/articles/stars-guardians) to
ensure decisions made locally within the feature don’t cause a bad result for
the rest of the product globally. They are from disciplines such as security,
legal, and design (many disciplines are represented in both camps.) We refer
to these teams as horizontal teams because they work across vertical teams.

Vertical teams generally benefit from very clear goals and can take
[greedy](https://en.wikipedia.org/wiki/Greedy_algorithm) approaches. But
Horizontal teams face a tougher challenge. They are only partially involved in
each project and often have the unhappy job of applying constraints to vertical teams in the name of balancing higher level objectives.

A common best practice is to have a clear planning process at the outset of a
new vertical program that establishes clear expectations with respect to each
horizontal to start with. But even when done well, there is some upper bound
on the effectiveness of early alignment due to the dynamic nature of product
work. The product definition inevitably evolves over the course of development
and sometimes even the global landscape the horizontal teams are managing can
change. So another common practice is to add additional checkpoints along the
way.

I submit to you that these **bottlenecks are an antipattern** to be avoided.

The natural consequence of these bottlenecks is that your team of horizontal
experts spends a majority of their time reviewing work that doesn’t represent
any threat to the global optimum, because most vertical teams are mostly
aligned with those things already. That also means the experts have less time
to focus on the really tricky situations that do deserve their attention.
Bottlenecks inevitably become a source of slowdowns that sacrifice real value
for consumers and the company. And the more you try to hire to solve the
bottleneck the more coordination overhead slows things down even further.

There is a better way.

In signal processing there is something called **bandpass** which allows
certain signals to pass through unencumbered while others are attenuated or
blocked. Instead of spreading themselves thin trying to examine every aspect
of every vertical product, horizontal teams should create clear fast paths
within which vertical teams can execute safely and with confidence. With tools
like design guidelines, privacy standards, security protocols, and legal
guardrails a majority of work can be untethered from expensive processes. In
turn, those products which do require novel consideration will have much more
bandwidth from their horizontal partners to work through the problems.
Resulting lessons can be further integrated into the design guidelines to
encode those lessons for future teams and allow everyone to move more quickly
in the future.

PublishedJul 3, 2023