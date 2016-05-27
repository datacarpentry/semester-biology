---
layout: exercise
topic: Version Control
title: Richness Merge Conflict
language: Python
---

This is a follow up question to [Richness Revert]({{ site.baseurl }}/exercises/Version-control-richness-revert-Python).

A colleague emails you to let you know that you need to change some of the
parameter values that are being used in `rich_pred.py`. Go to the line that
defines `sar_parameters` and change it to

```
sar_parameters = [[22.7, 0.3], [1.2, 0.163, 0.009],
                  [14.36, 21.16], [85.91, 42.57],
				  [1082.45, 1.59, 390000000]]
```

Now, follow these instructions carefully:

1.  Save the file and commit the change
2.  Email me to let me know you've changed the file
3.  I'll email you back and tell you to go ahead and try to push the change to
    your GitHub repository.
4.  You should get an error indicating that the commit failed because
    you aren't up to date with the repository (I've made changes since
    your last update).
5.  Pull those changes down, resolve any conflicts, and commit the resulting
    version of the file.
