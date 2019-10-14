---
layout: page
element: notes
title: Googling for Help
language: R
---

> Check that top Google results haven't change and adjust as needed
> Current top hits 1, 2, and 5:
> 1. https://dplyr.tidyverse.org/reference/select.html
> 2. https://blog.exploratory.io/selecting-columns-809bdd1ef615
> 3. https://stackoverflow.com/questions/21502465/replacement-for-rename-in-dplyr

* Professional programmers use Google regularly
* Learning how to search, read, and apply online help is a key skill
* Requires
    * Vocabulary
        * Look for cheatsheets
    * Careful reading
    * Understanding
    * Testing


### Example

* How to change the name of columns in dplyr
* Search: `dplyr change name column`
    * Name of package (if not in a distinctly name package include `r` or
      `rstats`)
    * The thing you want to do using technical terms
    * Keep it simple
    * Sometimes first searches show you how to ask the question
* Switch to `dplyr rename column`
* Check the date
    * Older results might be out of date
    * Can restrict to newer posts in search (but often more advanced)

#### First hit

> https://dplyr.tidyverse.org/reference/select.html

* Documentation
* Start reading from top
* Not super clear
* Focus on examples
* `Ctrl-F`
* `petal_length` is in output, so it is the new name and `Petal.Length` is the old value

#### Second hit

> https://blog.exploratory.io/selecting-columns-809bdd1ef615

* Blog post
* Kind of long
* `Ctrl-F`
* `rename()` function, but what's the order
* Look at the setup: `github_issues`
* Scroll up and look at column names
* `assignee.login` is in the orginal setup, so that is the variable we are changing, `developer` is new name

#### Fifth hit

> https://stackoverflow.com/questions/21502465/replacement-for-rename-in-dplyr

* Question & Answer site
* Want `rename` so this seems good.
* Read question
* Check date - possible out of date
* Very clear statement of solution
* Check comments - it's so clear because someone helped
* Look at next answer - we could do this with select as well

#### Testing and modifying answers

* Test the example
* Modify the example
* But be careful
    * Malicious code examples exist
    * Do you trust the site
    * Does it have a lot of upvotes
    * Top of searches with lots of hits


### Tips (not taught, but should be highlighted in example)

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
