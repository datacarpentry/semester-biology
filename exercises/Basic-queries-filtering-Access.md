---
layout: exercise
topic: Basic Queries
title: Filtering
language: Access
---

A population biologist (Dr. Undómiel) who studies the population
dynamics of *Dipodomys spectabilis* would like to use some data from
Portal, but she doesn't know how to work with large datasets. Being the
kind and benevolent person that you are, write a query to extract the
data that she needs. She wants only the data for her species of
interest, when each individual was trapped, and what sex it was. She
doesn't care about where it was trapped within the site because she is
going to analyze the entire site as a whole and she doesn't care about
the size of the individuals. Obviously she doesn't need the species
codes because you're only providing her with the data for one species,
and besides since she isn't actually looking at the database itself the
two character abbreviation would probably be confusing. Save this query
as `Spectabilis Population Data`.

Scroll through the results of your query. Do you notice anything that
might be an issue for the scientist to whom you are providing this data?
[you should] Think about what you should do in this situtation...

You decide that to avoid invoking her wrath, you'll send her a short
e-mail\* requesting clarification regarding what she would like you to
do regarding this complexity. Dr. Undómiel e-mails you back and asks
that you create two additional queries so that she can decided what to
do about this issue later. She would like you to add a query to the same
data as above, but only for cases where the sex is known to be male, and
an additional query with the same data, but only where the sex is known
to be female. Save these as `Spectabilis Population Data Males` and
`Spectabilis Population Data Females`.

\*Short for elven-mail
