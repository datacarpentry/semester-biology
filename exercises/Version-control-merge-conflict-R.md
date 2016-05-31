---
layout: exercise
topic: Version Control
title: Merge Conflict
language: R
---

You decide to change the parameter values that are being used in
`logistic_growth.R`. Change the last 3 lines of the file to

```
print get_logistic_grwth_equil(10, 0.75, 1000)
print get_logistic_grwth_equil(10, 0.25, 5000)
print get_logistic_grwth_equil(5, 0.5, 100)
```

Now, follow these instructions carefully:

1.  Save the file, but ***do not*** commit the change
2.  Email me to let me know you've changed the file
3.  I'll email you back and tell you to go ahead and try to commit
4.  You should get an error indicating that the commit failed because
    you aren't up to date with the repository (I've made changes since
    your last update).
5.  Update, resolve any conflicts, and `commit` the resulting version of
    the file.
