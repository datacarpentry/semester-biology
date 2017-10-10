---
layout: exercise
topic: Version Control Basic
title: Commit Multiple Files
language: R
---

This is a follow up to
[Second Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-second-solo-commit-R).

After talking to a colleague, you realize that
`Gaeta_etal_CLC_data.csv` is only the first of many files to come. To
help keep track of the files you'll need to number them, so rename the current
file `Gaeta_etal_CLC_data_1.csv` and change your R code to reflect this
name change.

*Git will initially think you've deleted `Gaeta_etal_CLC_data.csv` and
created a new file `Gaeta_etal_CLC_data_1.csv`. But once you click on
both the old and new files to stage them, git will recognize what's been done
and indicate that it is renaming the files and indicate this with an `R`.*

In a single commit, add renaming of the data file and the changes to the R file.
