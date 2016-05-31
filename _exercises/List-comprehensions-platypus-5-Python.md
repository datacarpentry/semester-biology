---
layout: exercise
topic: List Comprehensions
title: Platypus 5
language: Python
---

Here's the platypus fecundity data from our first experiment (using the
simple Platypus class that we built in problems 1 and 2), stored
conveniently as a Python list:

```
[Platypus("perry", [3,2,4,1,2]),
Platypus("quacker", [100,1,3,1,2]),
Platypus("fishface", [0,1,3,1,2,1]),
Platypus("duckhead", [3,1,3,6,3]),
Platypus("waddles", [3,1,2,0,8,3]),
Platypus("professor quackington", [2,1,4,5,7]),
Platypus("bartholomew beavertail", [0,1,3,1,0,0,2]),
Platypus("syd", [3,1,3,1,3,5,5,2,1,3]),
Platypus("ovide", [2,0,10,0,0,0,0,0,0]),
Platypus("hexley", [3,1,2,3,1,0,0,1,1]),
Platypus("supafly", [19,1,2,1,0,0,0,1])]
```

Unfortunately, this data was collected by undergraduates, so it contains
some obvious clerical errors. Being an expert in platypus life history,
you reason that it's unlikely that a platypus would lay more than an
average of 3 eggs per breeding season.

Write a list comprehension that returns the names of individuals that
laid more than 3 eggs per breeding season, on average.
