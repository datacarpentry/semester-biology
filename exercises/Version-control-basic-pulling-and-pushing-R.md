---
layout: exercise
topic: Version Control Basic
title: Pulling and Pushing
language: R
---

This is a follow up to
[Pushing Changes]({{ site.baseurl }}/exercises/Version-control-basic-pushing-changes-R).

**STOP: Make sure you sent your teacher an email following the last exercise
with a link to your Github repository and wait until your teacher has told you
they've updated your repository before doing this one.**

While you were working on your vectorized GC-content function, Dr. Granger (*who
has suddenly developed some pretty impressive computational skills*) wrote some
code to generate a `data.frame` with `dplyr`. To get it you'll need to `pull`
the most recent changes from Github.

1. On the `Git` tab click on the `Pull` button with the blue arrow. You should
   see some text that looks like:

   ```
   From github.com:ethanwhite/gryffindorforever
      1e24ac8..815e600  master     -> origin/master
   Updating 1e24ac8..815e600
   Fast-forward
    testme.txt | 1 +
    1 file changed, 1 insertion(+)
   create mode 100644 youareawesome.txt
   ```

2. Click `OK`.
3. You should see the new lines of code in your `houseelf-analysis.R.

   ```
   library(dplyr)
   
   data_size_class <-
     data %>% 
     rowwise() %>% 
     transmute(id = id, earlengthcat = get_ear_len_cat(earlength, 10))
   ``` 

4. Modify the code to add a `gccontent` column to the `data.frame` that includes
   the `id` and `earlengthcat` for each individual. The `gccontent` column
   should hold the results of your GC-content function.
5. Save this data frame as a `CSV` file using `write.csv()`
6. Commit the new code and the resulting `CSV` file and push the results to
   Github.
