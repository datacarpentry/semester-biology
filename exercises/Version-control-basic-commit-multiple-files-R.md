---
layout: exercise
topic: Version Control Basic
title: Commit Multiple Files
language: R
---

This is a follow up to
[Second Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-second-solo-commit-R).

After talking to a colleague, you realize that
`Gaeta_etal_CLC_data.csv` is only the first in a series of similar files that you will receive. To help keep track of files, you decide to number them. Rename the `Gaeta_etal_CLC_data.csv` file to `Gaeta_etal_CLC_data_1.csv` manually, using the Files tab in RStudio. You’ll also need to change the first line of `fish-analysis.R` so that the script will still work. 

To include all of these changes in a single commit, stage both data files and the saved R script and then commit with a good commit message. 

*Git will initially think you've deleted `Gaeta_etal_CLC_data.csv` and
created a new file `Gaeta_etal_CLC_data_1.csv`. But once you click on
both the old and new files to stage them, git will recognize this by making the two files into one and marking this with an `R`.*
