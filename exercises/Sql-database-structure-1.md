---
layout: exercise
title: SQL - Database Structure 1
---

*Before starting this problem make sure that you have a backup of your
database or that it has recently been committed to version control so
that you can revert the changes if necessary. In fact, when developing
the code it's probably best to work on a copy of the database that is
specifically just for development. Once it's working then apply it to
your actual database. Always, always, backup your databases before
messing with them in this manner. Seriously.*

The Plots table in our version of the Portal database violates one of
the major rules of database structure (the whole gosh dang table is
redundant for Pete's sake!). Figure out a better design using one table
to link each plot number to a single experiemental code (save this as
`PlotsSingleCode`) and a second table that includes various versions
of each type of code (save this as `Experiments`). Create these tables
and add the appropriate data to them using Python to extract the
necessary information from the old table and insert it into the new
tables..

Using your new plot related tables write a query (in Python) that
determines the Plot Type Description and the number of plots of each
type. Print the results of this query to the screen.
