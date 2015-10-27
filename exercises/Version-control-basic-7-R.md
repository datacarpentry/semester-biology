---
layout: exercise
title: Version Control Basic 7
subtitle: Pulling and pushing
language: R
---

This is a follow up to
[Version Control Basic 6]({{ site.baseurl }}/exercises/Version-control-basic-6-R).

**STOP: Wait until your teacher has told you they've updated your repository 
following the last exercise before doing this one.**

While you were working on your vectorized GC-content function, Dr. Granger (*who
has suddenly developed some pretty impressive computational skills*) has been
writing a ***vectorized ear length categorizer***. To get it you'll need to `pull` the
most recent changes from Github.

1\. On the `Git` tab click on the `Pull` button with the blue arrow. You should
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

2\. Click `OK`.

3\. You should see the new function in your repository.

```
gc_content <- function(seq){
   #Calculate the GC-content for one or more sequences
   ear_lengths <- ifelse(seq > 10, "large", "small")
   return(ear_lengths)
}
``` 

4\. Write some new code that creates a data frame with information about the
individual ID, the earth length class, and the gc-content for each individual.

5\. Save this data frame as a csv file using `write.csv()`

6\. Commit the new code and the resulting .CSV file and push the results to Github.
