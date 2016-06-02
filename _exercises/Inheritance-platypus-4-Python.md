---
layout: exercise
topic: Inheritance
title: Platypus 4
language: Python
---

We just realized that in our first platypus experiment, some eggs were
poached or didn't hatch, and we didn't count those numbers. We want
those eggs included in `total_fecundity`, but we want to know how many
eggs actually hatched as well.

Create a second class, `BetterPlatypus`. It should be just like (inherit
from) our original Platypus class except that it takes two lists: one is
the original list of eggs laid, and the other is a list of eggs we just
found that didn't hatch. Override the `lay_eggs` method so that it takes
two numbers, the number of hatched and the number of unhatched eggs.
Override `total_fecundity` so that it incorporates both lists.

```
>>> perry = BetterPlatypus("perry", [3, 2, 4, 1, 2], [0,1,0,0,1])
>>> perry.total\_fecundity()
14
>>> perry.lay_eggs(2, 1)
>>> perry.total_fecundity()
17
```

Fun fact: did you know that the platypus is also venomous?
