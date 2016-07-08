---
layout: page
element: notes
title: Joins
language: SQL
---

### Basic join

* [`JOIN`](http://www.w3schools.com/sql/sql_join.asp) 
    * combine rows from multiple tables
    * based on condition
* This query selects `species` records in the `PortalMammals_main` table and 
  `scientificname` found in the `PortalMammals_species` table.
    * The query links the `species` with `new_code` from `PortalMammals_species`.
  
```
SELECT species, scientificname
FROM PortalMammals_main
JOIN PortalMammsls_species WHERE species = new_code;
```

* When using `JOIN` it is more appropriate to set the condition using `ON`
    * `ON` represents a matching identifier between two tables
    * It is best to `JOIN` using at least one variable that is a unique record.
        * `new_code` values are unique across `PortalMammals_species`.
        * `species` values occur in multiple records across `PortalMammals_main`.

```
SELECT yr, mo, dy, scientificname
FROM PortalMammals_main
JOIN PortalMammals_species ON species = new_code;
```

### Multi-table join

* Use multiple `JOIN` to link multiple tables.

```
SELECT yr, mo, dy, scientificname, PlotTypeAlphaCode
FROM PortalMammals_main
JOIN PortalMammals_species ON species = new_code
JOIN PortalMammals_plots ON plot = PlotID;
```

### Multi-table join with abbreviations

* The previous query works because each of the fields are uniquely named.
* It is safer to write a query that links fields to their table. 

```
SELECT PortalMammals_main.yr, PortalMammals_main.mo, 
PortalMammals_main.dy, PortalMammals_species.scientificname, 
PortalMammals_plots.PlotTypeAlphaCode
FROM PortalMammals_main
JOIN PortalMammals_species 
ON PortalMammals_main.species = PortalMammals_species.new_code
JOIN PortalMammals_plots 
ON PortalMammals_main.plot = PortalMammals_plots.PlotID;
```

* Use abbreviations to help with readability.

```
SELECT m.yr, m.mo, m.dy, s.scientificname, p.PlotTypeAlphaCode
FROM PortalMammals_main m
JOIN PortalMammals_species s ON m.species = s.new_code
JOIN PortalMammals_plots p on m.plot = p.PlotID;
```

> Do Exercises 1-4 - [JOIN 1]({{ site.baseurl }}/exercises/Advanced-queries-join-1-SQL/), [JOIN 2]({{ site.baseurl }}/exercises/Advanced-queries-join-2-SQL/), [JOIN 3]({{ site.baseurl }}/exercises/Advanced-queries-join-3-SQL/), [JOIN 4]({{ site.baseurl }}/exercises/Advanced-queries-join-4-SQL/)
