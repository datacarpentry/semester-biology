Databases Week 2 - Joins, Nested Queries, and Database Structure
================================================================

Monday - Joins
--------------

### Intro
Slides on Joins

###Basic Example
* Join main table to species table
* Show species and scientific name side by side
* Show distinct
* Filter by weight > 100 g

###What joins actually do
* Join species and plots tables

###Joins are part of the Query, not the database
* Save query
* Close query
* Open new query - shows no joins

###In Access they can be permanent - Relationships
* Save relationships
* Open new query - show joins
* Show that you can remove joins


Wednesday - Database Structure
------------------------------
Database Structure slides

Friday - Nested queries
-----------------------
Demonstrate by doing a query to get the number of trapping periods in each year.

* First GROUP BY yr and COUNT period
* Then GROUP BY yr and period
* Save that query
* Nest it to count the unique periods
