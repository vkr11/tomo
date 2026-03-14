# Failure Theory

*Source: https://boz.com/articles/failure-theory*

# Failure Theory

I proposed to my wife at the top of Mt Shasta. It was my first time climbing a
mountain. We joined a group climb and early one morning, roped ourselves to
each other and headed up. Not too far below us we could see a very long and
very deep crevasse in the ice. We made it to the top. She said yes. And the
rest is history.

Years later I read the book [Deep
Survival](https://www.amazon.com/Deep-Survival-Who-Lives-Dies/dp/0393326152)
which discusses human survival in extreme conditions. One point the book makes
is that climbers tethering themselves together is a dubious value proposition.
On one hand, if one person slips and cannot arrest their fall there is a
chance that the collective efforts of everyone on the line can save them. On
the other hand, the chance that somebody who did not slip is pulled down is
also much greater.

Furthermore, it is much harder to arrest a large number of people falling at
odd angles than it is for an individual person to arrest themselves. And of
course if tragedy strikes and the entire group falls into the crevasse there
is nobody left to coordinate a rescue. Effectively the chances of small
failures has decreased slightly but the chances of catastrophic failures has
gone way up.

I think of this example all the time in my work.

Most failures are totally unremarkable. We fix a bug. We slip a schedule. We
change a feature. But sometimes there are catastrophic failures with long
lasting consequences. And when we investigate those failures they are almost
always the consequence of a chain of minor failures linked together in ways we
often didn’t understand at the time.

It has always struck me that the more edifice you build to prevent minor
failures the larger the capacity you create for catastrophic ones, just like
climbers roped together on a mountaintop. Years later I finally stumbled upon
a formal framing of this phenomena in a paper from the University of Chicago
titled “[How Complex Systems Fail](https://how.complexsystems.fail/).” It was
ostensibly written for the medical community but the lessons it contains are
universal. One particularly salient observation is that we value the speed and
production of these complex systems which push us towards greater risk until a
failure pushes us the other way. Humans are both the greatest threat and the
greatest opportunity for stability.

I am not suggesting we stop trying to prevent failures. Indeed there are well
known counterexamples worth considering. Air travel has gotten almost
monotonically safer over time. However I do think one reason for that is the
stability of the underlying systems, as air travel hasn’t significantly
changed in almost 60 years. The pressure I mention above to increase output
has been balanced not just through effective regulation but also economics.

Cars have also gotten safer though that story is more complicated than it
seems. When seat belts became legally required the number of fatalities went
down meaningfully. But the number of accidents and injuries actually went up.
People felt safer and as a consequence took more risk. That’s almost certainly
a good trade but it does speak to the degree to which humans adjust their
activities relative to risk which makes it hard for failure to be eliminated.

My concern is that many of the efforts we have to defend against failure
create catastrophic complexity without meaningfully reducing failure at all.
For example after a rare failure we may introduce daily complexity in spite of
the fact that failure was already acknowledged to be rare. I recall the story
of the nuclear meltdown at 3 Mile Island where a sensor was installed to
detect a rare but serious condition. Unfortunately the nature of the condition
made it impossible for the sensor to be very reliable but the engineers
figured better to have false positives than miss the condition. But that
backfired because the operators became habituated to that signal being faulty
so they ignored it when it wasn’t. Had no sensor been installed at all it is
very likely they would have noticed other conditions precipitating the
disaster and prevented it.

This is the reason why I tend to prefer less structure in organizations. There
is more chaos but failures tend to be less correlated and less catastrophic.
Instead of protecting my teams from change I try to ensure they are
[antifragile](https://boz.com/articles/antifragile). Instead of preventing all
mistakes I focus more on preventing a small number of major mistakes. Instead
of enforcing stronger processes I try to give more latitude to people on the
ground.

This is a post I expect to refer back to quite a bit in the future at times
when I propose a high level framework which begs for more specific detail to
operationalize. While I never intend to be vague I do prefer leaving the last
mile of work to those closer to the work who have more visibility into how it
impacts them.

PublishedMay 11, 2021