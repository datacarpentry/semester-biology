---
layout: exercise
title: R-SQL 1
subtitle: Connect and Query
language: R
---

This is a follow up to the [SQL Filtering]({{ site.baseurl }}/exercises/Sql-filtering) problem.

It is clear Dr. Undómiel appreciates your skill working with large databases and 
she seems to expect you will maintain your benevolence. (*Such is a fair 
expectation of a true wizard*). This time though, she's looking for some extra 
detail in her queries. She's curious if desert rodents are [dimorphic](https://en.wikipedia.org/wiki/Sexual_dimorphism) in size.

1. Download a new copy of the [Portal database](http://files.figshare.com/2292171/portal_mammals.sqlite). 
2. Connect to `portal_mammals.sqlite` using the `RSQLite` package.
3. Start by reminding yourself about which tables are in the database using
`dbListTables()`
4. Then remind yourself of the fields in the `surveys` and `plots` tables using
   `dbListFields()`.
5. Select and print out the average hind foot length and average weight of:
    - all *Dipodomys spectabilis* individuals on the *control* plots
    - male *D. spectabilis* on the *control* plots
    - female *D. spectabilis* on the *control* plots
