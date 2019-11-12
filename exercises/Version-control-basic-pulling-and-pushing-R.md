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

While you were working on your plot of size among lakes, your colleague (*who
has suddenly developed some pretty impressive computational skills*) wrote some
code to generate a histogram of scale lengths. To get it you'll need to `pull`
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
3. You should see the new lines of code in your `fish-analysis.R`.

   ```
ggplot(fish_data, aes(x = scalelength, fill = length_cat)) +
  geom_histogram()
   ``` 

4. Modify this code to look at narrower ranges of scale size classes by setting 
   the bins argument to 80. 
5. Save this plot as `scale_hist_by_length.jpg` using `ggsave`. 
6. Commit the new code and resulting .jpg file by adding both files to the stage and committing with a good commit message, then push this to GitHub. 
