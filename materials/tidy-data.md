---
layout: page
element: notes
title: Tidy Data
language: SQL
---

The main goal of tidy data is making it easy for a computer to work with the
data. Let's start by looking at some messy data and thinking about what makes it
messy and what we could do to improve it.

> Do the exercise on [Improving Messy Data]({{ site.baseurl }}/exercises/Tidy-data-improving-messy-data-SQL).
>
> * Put the data up on the screen
> * Ask the class for things they would improve and how to fix them
> * Start a list of the rules they come up with on the board
> * Talk through anything that can be improved about their answers
> * Add in any rules that are missing from the list below at the end

### General rules

1. Be consistent
2. Make it a rectangle
3. One row for each data point
4. One column per type of information
5. Every cell contains one value
6. Minimize redundancy using multiple tables
7. Don't use colors, fonts, or anything purely visual as data
8. Use good null values (not -999, blanks good, some prefer NA etc. but language
   specific)
9. Save data in plain text files
10. Use good names
