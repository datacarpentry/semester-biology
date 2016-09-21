---
layout: exercise
topic: Scientific
title: Mammal Body Size 2
language: R
---

This is a follow up to
[Mammal Body Size 1]({{ site.baseurl }}/exercises/Scientific-mammal-body-size-1-R).

Looking at the average mass of extinct and extant species overall is useful, but
there are lots of different processes that could cause size-biased extinctions
so it's not as informative as we might like.  However, if we see the exact same
pattern on each of the different continents that might really tell us
something. Repeat the analysis in
[Mammal Body Size 1]({{ site.baseurl }}/exercises/Scientific-mammal-body-size-1-R), but this time compare the mean masses within each of the different continents.

Using the `dplyr` and `tidyr` libraries, group the data by continent and status. 
Summarize the average mass for each group. Spread the groups by status and select the statuses extant and extinct. Calculate the difference in average 
masses between extant and extinct groups. 

Export your results to a `csv` file where the first entry on each line is the 
continent, the second entry is the average mass of the extant species on that 
continent, the third entry is the average mass of the extinct species on that 
continent, and the forth entry is the difference between the average extant and 
average extinct masses. Call the file `continent_mass_differences.csv`. If you 
notice anything strange think about what's going on and present the final data 
in the way that makes the most sense to you.

Because you’re working with real data, some things might look strange that are
not results but barriers to analysis. These inconsistencies in the data will 
require some cleaning. 

The unknown value used in the dataset is `-999`. R assumes your unknown value is 
`NA`, but `"NA"` in the data is the code for North America. 
Use the additional arguments `stringsAsFactors = FALSE, na.strings = "-999"` in 
`read.csv()` to get R to keep `"NA"` as a string and transform `-999` to `NA`. You will still need to remove the `NA` from the data before doing any averaging. 

You might also notice Africa is represented by both `"Af"` and `"AF"`. Be sure 
to chose one and use `str_replace_all()` to make the change.
