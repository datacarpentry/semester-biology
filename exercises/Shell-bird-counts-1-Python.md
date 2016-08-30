---
layout: exercise
topic: Shell
title: Bird Counts 1
language: Python
---

We have data on bird communities that we've collected that we need to
analyze. The data has three columns, a date, a common name, and a count of the
number of individuals.

```
2013-03-22 bluejay 5
2013-03-22 mallard 9
2013-03-21 robin 1
```

Download one of these files using the `curl` command:

`curl -O {{ site.url }}/data/data-drycanyon-2013.txt`

If we wanted to find the least common species in the data file and store that
information we could do something like:

```
sort data-drycanyon-2013.txt -k 3 -n > sorted-counts.txt
head -1 sorted-counts.txt > least-common-species.txt
```

Now we want to get the most common species at the site. You can do this using
the `tail` command. Since we don't need the intermediate `sorted_counts.txt`
file, use a pipe instead of creating the intermediate file.

Save both the curl command and the one line command for storing the least common
species in a text file called `get-most-common-species.sh`.
