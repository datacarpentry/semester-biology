---
layout: exercise
topic: Object Oriented Programming
title: Platypus 2
language: Python
---

Expand the Platypus class, giving it three methods:

`total_fecundity`, which returns the total number of eggs laid
`breeding_seasons`, which returns the number of breeding seasons in which the
platypus laid at least 1 egg `lay_eggs`, which adds the number of eggs laid to
the end of the list.

It should look something like this:

```
>>> perry = Platypus("perry", [3, 2, 4, 1, 2])
>>> perry.breeding_seasons()
5
>>> perry.total_fecundity()
12
>>> perry.lay_eggs(2)
>>> perry.total_fecundity()
14
```
