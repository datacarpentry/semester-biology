---
layout: exercise
title: SQL - Sorting
---

The graduate students that work at the Portal site are hanging out late
one evening drinking... soda pop... and they decide it would be an
epically awesome idea to put together a list of the 100 largest rodents
ever sampled at the site. Since you're the resident "computer genius"
they text you, and since you're up late working and this sounds like a
lot more fun that than homework you're working on (which isn't really
saying much, if you know what I'm saying) you decide you'll make the
list of them.

The rules that the Portal students have come up with (and they did spend
a sort of disturbingly long time coming up with these rules; I guess you
just had to be there) are:

1.  Data needed include the species ID, year of capture, and the mass.
    These columns should be presented in this order.
2.  Individuals should be sorted in descending order with respect to
    mass.
3.  Since individuals often have the same mass ties should be settled by
    sorting next by hind foot length and finally by the year of capture.

You may find the SQL command LIMIT to be helpful. Save the final query
as `100 Largest Individuals`.
