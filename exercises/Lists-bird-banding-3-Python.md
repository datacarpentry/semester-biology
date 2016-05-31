---
layout: exercise
topic: Lists
title: Bird Banding 3
language: Python
---

This is a follow up to the [Bird Banding 1]({{ site.baseurl }}/exercises/Lists-bird-banding-1-Python) and [Bird Banding 2]({{ site.baseurl }}/exercises/Lists-bird-banding-2-Python) problems.

When last we left you, our intrepid hero, you had created the following
updated list of bird abundances across sites:

```
number_of_birds = [28, 32, 1, 0, 10, 22, 30, 19, 145, 27, 36, 25, 9, 
                   38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32,
                   90, 33, 14, 39, 56, 81, 29, 38, 1, 0, 143, 37, 98,
                   77, 92, 83, 34, 98, 40, 45, 51, 17, 22, 37, 48, 38,
                   91, 73, 54, 46, 102, 273, 60, 10, 11, 27, 24, 16, 
                   9, 23, 39, 102, 0, 14, 3, 9, 93, 64]
```

For your research on bird counts you need to not only know what many
birds are at a single site, but also how many birds occur on groups of
sites.

Use slices to answer the following questions:

​1. What is the total number of birds for 5 sites starting at site 10?

​2. What is the total number of birds at the last 6 sites? Have Python
figure out what the last six sites are, don't just type in their
positions.

You're going to be doing a lot of this sort of analysis, so it's
probably better to have a function that does it for you rather than
doing the slicing yourself each time. Cut and paste the following
function into your code:

```
def n_site_count(bird_counts, start_site, number_of_sites):
    """Count the total number of birds at a given number of sites starting
    at a given start site."""
    start_site = start_site - 1 #convert start site to Python index
    sub_sites = bird_counts[start_site:start_site + number_of_sites]
    number_of_birds = sum(sub_sites)
    return number_of_birds
```

Use the function to calculate and return the total count of all birds
for the n sites starting at the start site. For example, if there are 5
sites and number\_of\_birds\_list = [5, 5, 10, 10, 8], then if
starting\_site = 2 and number\_of\_sites = 3 then the function should
return the value 25 (5 + 10 + 10). Use the data on the number of birds
given in the list above (just copy and paste it into your code) to
answer the following questions.

​3. What is the total number of birds for 5 sites starting at site 10?

​4. What is the total number of birds for 7 sites starting at site 1?

​5. What is the total number of birds for 1 site starting at site 23?

​6. Think about what the funtion should do if asked for the total number
of birds for 10 sites starting at site 70 (Note: there are only 74
sites). Print out a sentence that explains what it actually does.
