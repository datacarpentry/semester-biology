---
layout: page
element: notes
title: Joins
language: SQL
---

> Remember to
>
> *  download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * connect `portal_mammals.sqlite` to SQLite Manager.
> * display a fully joined version of the Portal data using:  
> `SELECT * FROM surveys JOIN species ON surveys.species_id = species.species_id JOIN plots ON surveys.plot_id = plots.plot_id;`

### Why use multiple tables

* It is often not efficient to include all information of interest in a single
table.
* Redundant information makes it more difficult to update or revise data.
    * If something changes we want to be able to change it in one place, not
    hundreds of places.
* Use multiple tables
* Each table contains a single kind of information
    * `surveys`: information about individuals
    * `species`: information about species
    * `plots`: information about plots
* If a species name changes we only need to change it in the `species` table
* Connect tables using joins to describe relationships between tables
(*"relational" database*)


### Basic join

* [`JOIN`](http://www.w3schools.com/sql/sql_join.asp) 
    * combine rows from multiple tables
    * based on condition
  
```
SELECT DISTINCT year, month, day, plot_type 
FROM surveys
JOIN species ON surveys.plot_id = plots.plot_id
```

* This query selects `year`, `month`, and `day` from `surveys` and 
`plot_type` from the `plots` table.
    * The query links the `plot_id` from `surveys` with `plot_id` from `plots`.
* `ON` basically works like `WHERE`
    * It represents a matching identifier between two tables
    * In fact, you can even use `WHERE` instead
    * If you don't limit the join using `ON`, bad things happen, because the
      JOIN combines each row in `surveys` with every row in `plots`

    ```
    SELECT DISTINCT year, month, day, plot_type
    FROM surveys
    JOIN plots
    ```

* One way to think about this join is that it adds the information in
  `plots` to the `surveys` table

> Do [Exercise 9 - Basic Join]({{ site.baseurl }}/exercises/Advanced-queries-basic-join-SQL/).

* We can also use `USING` as short hand in cases where the column names are the
same across tables.

```
SELECT year, month, day, genus, species
FROM surveys
JOIN species USING (species_id);
```

### Multi-table join

* Use multiple `JOIN`s to link multiple tables.

```
SELECT year, month, day, taxa plot_type
FROM surveys
JOIN species ON surveys.species_id = species.species_id
JOIN plots ON surveys.plot_id = plots.plot_id;
```

### Multi-table join with abbreviations

* The previous `SELECT` statement works because each of the fields are uniquely named.
* It is safer to write a query that links fields to their table. 

```
SELECT surveys.year, surveys.month, surveys.day, species.taxa, plots.plot_type
FROM surveys
JOIN species ON surveys.species_id = species.species_id
JOIN plots ON surveys.plot_id = plots.plot_id;
```

* Use abbreviations to help with readability.

```
SELECT sv.year, sv.month, sv.day, sp.taxa, p.plot_type
FROM surveys sv
JOIN species sp  ON sv.species_id = sp.species_id
JOIN plots p ON sv.plot_id = p.plot_id;
```

> Do [Exercise 10 - Multi-table Join]({{ site.baseurl }}/exercises/Advanced-queries-multi-table-join-SQL/).


### Combining joins with WHERE, ORDER BY, and aggregation

* Joins can be combined with everything else we've learned about SQL

```
SELECT sp.genus, sp.species, COUNT(*) as number
FROM surveys sv
JOIN species sp  ON sv.species_id = sp.species_id
JOIN plots p ON sv.plot_id = p.plot_id
WHERE p.plot_type = 'Rodent Exclosure'
GROUP BY sp.genus, sp.species
HAVING number > 50
ORDER BY number;
```

* To build of big queries like this start small and then expand
* Test each step

> Do [Exercise 11 - Filtered Join]({{ site.baseurl }}/exercises/Advanced-queries-filtered-join-SQL/).
