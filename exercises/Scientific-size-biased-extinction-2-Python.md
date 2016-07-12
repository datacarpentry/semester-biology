---
layout: exercise
topic: Scientific
title: Size-biased Extinction 2
language: Python
---

This is a follow up to [Size-biased Extinction 1]({{ site.baseurl }}/exercises/Scientific-size-biased-extinction-1-Python).

Looking at the average mass of extinct and extant species overall is
useful, but there are lots of different processes that could cause
size-biased extinctions so it's not as informative as we might like.
However, if we see the exact same pattern on each of the different
continents that might really tell us something. Repeat the analysis in
the Numpy 1 problem, but this time compare the mean masses within each
of the different continents. Export your results to a `csv` file where the
first entry on each line is the continent, the second entry is the
average mass of the extant species on that continent, the third entry is
the average mass of the extinct species on that continent, and the forth
entry is the difference between the average extant and average extinct
masses. Use you handy export\_to\_csv() function:

```
def export_to_csv(data, filename):
    """Export list of lists to comma delimited text file"""
    outputfile = open(filename, 'wb')
    datawriter = csv.writer(outputfile)
    datawriter.writerows(data)
    outputfile.close()
```

Call the file continent\_mass\_differences.csv. If you notice anything
strange think about what's going on and present the final data in the
way that makes the most sense to you.
