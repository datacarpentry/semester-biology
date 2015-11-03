---
layout: exercise
title: Version Control Basic 4
subtitle: Multiple files, one commit
language: R
---

This is a follow up to
[Version Control Basic 3]({{ site.baseurl }}/exercises/Version-control-basic-3-R)


After talking with Dr. Granger you realize that
`houseelf_earlength_dna_data.csv` is only the first of many files to come. To
help keep track of the files you'll need to number them, so rename the current
file `houseelf_earlength_dna_data_1.csv` and change your R code to reflect this
name change.

*Git will initially think you've deleted `houseelf_earlength_dna_data.csv` and
created a new file `houseelf_earlength_dna_data_1.csv`. But once you click on
both the old and new files to stage them, git will recognize what's been done
and indicate that it is renaming the files and indicate this with an `R`.*

In a single commit, add renaming of the data file and the changes to the R file.
