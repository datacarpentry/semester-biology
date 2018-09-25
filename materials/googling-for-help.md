---
layout: page
element: notes
title: Googling for Help
language: R
---

> Check that top Google results haven't change and adjust as needed
> Current top 3 hits:
> 1. https://blog.exploratory.io/selecting-columns-809bdd1ef615
> 2. https://dplyr.tidyverse.org/reference/select.html
> 3. https://stackoverflow.com/questions/21502465/replacement-for-rename-in-dplyr

* Professional programmers use Google regularly
* Learning how to search, read, and apply online help is a key skill
* Requires
    * Vocabulary
    * Careful reading
    * Understanding
    * Testing


### Example

* How to rename columns in dplyr
* Search: `dplyr rename column`

#### First hit

> https://blog.exploratory.io/selecting-columns-809bdd1ef615

* Blog post
* Kind of long
* `Ctrl-F`
* `rename()` function, but what's the order
* Look at the setup: `github_issues`
* Scroll up and look at column names
* `assignee.login` is in the orginal setup, so that is the variable we are changing, `developer` is new name

#### Second hit

> https://dplyr.tidyverse.org/reference/select.html

* Documentation
* Start reading from top
* Not super clear
* Focus on examples
* `Ctrl-F`
* `petal_length` is in output, so it is the new name and `Petal.Length` is the old value

#### Third hit

> https://stackoverflow.com/questions/21502465/replacement-for-rename-in-dplyr

* Want `rename` so this seems good.
* Read question
* Check date - possible out of date
* Very clear statement of solution
* Check comments - it's so clear because someone helped
* Look at next answer - we could do this with select as well
* Test and modify the example (but be careful)


### Tips

#### Search

* Get the vocabularly right
* Avoid extra words
* Specify the language

#### Results

##### Help sites

* Read the question
* Look at the setup
* Check the age
* Check the top 2-3 answers
* Glance at the comments
* Test & modify the example
    * But don't blindly paste things you don't understand
    * Reputation can help - e.g., StackOverflow w/lots of positive votes

##### Blog posts

* Read the question
* Look at the setup
* Use `Find`

##### Documentation

* Use `Find`
* Focus on the examples
