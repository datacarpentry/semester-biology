---
layout: exercise
title: SQL - Database Structure 2
---

*Before starting this problem make sure that you have a backup of your
database or that it has recently been committed to version control so
that you can revert the changes if necessary. In fact, when developing
the code it's probably best to work on a copy of the database that is
specifically just for development. Once it's working then apply it to
your actual database. Always, always, backup your databases before
messing with them in this manner. Seriously.*

The Species table in the Portal database has a structural problem in that the
`oldcode` column often contains multiple pieces of information in a single
cell. This means that we can't really run queries that use the `oldcode` field
effectively. Think about what the best structure would be for this table. It
might include splitting the table into two separate tables (wink, wink, nudge,
nudge). Feel free to check with Ethan to make sure you've got the right
idea. Using Python, restructure the database and store the new species table as
`PortalMammal_species`(i.e., the same name it has now; you may need to learn
about the [DROP TABLE](http://www.w3schools.com/sql/sql_drop.asp) command in
order to do this) and naming any new tables you create with easy to understand
names.
