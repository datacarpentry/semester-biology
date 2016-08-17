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

### Basic join

* [`JOIN`](http://www.w3schools.com/sql/sql_join.asp) 
    * combine rows from multiple tables
    * based on condition
  
```
SELECT year, month, day, genus, species
FROM surveys
JOIN species WHERE surveys.species_id = species.species_id;
```
* This query selects `year`, `month`, and `day` from `surveys` and 
`genus` and `species` from the `species` table.
    * The query links the `species_id` from `surveys` with `species_id` from `species`.
* When using `JOIN` it is more appropriate to set the condition using `ON`
    * `ON` represents a matching identifier between two tables
    * It is best to `JOIN` using at least one variable that is a unique record.
        * `species.species_id` values are unique.
        * `surveys.species_id` values occur in multiple records.

```
SELECT year, month, day, genus, species
FROM surveys
JOIN species ON species.species_id = surveys.species_id;
```

### Multi-table join

* Use multiple `JOIN` to link multiple tables.

```
SELECT year, month, day, genus, species, plot_type
FROM surveys
JOIN species ON surveys.species_id = species.species_id
JOIN plots ON surveys.plot_id = plots.plot_id;
```

### Multi-table join with abbreviations

* The previous `SELECT` statement works because each of the fields are uniquely named.
* It is safer to write a query that links fields to their table. 

```
SELECT surveys.year, surveys.month, surveys.day, species.genus, 
species.species, plots.plot_type
FROM surveys
JOIN species ON surveys.species_id = species.species_id
JOIN plots ON surveys.plot_id = plots.plot_id;
```

* Use abbreviations to help with readability.

```
SELECT sv.year, sv.month, sv.day, sp.genus, sp.species, p.plot_type
FROM surveys sv
JOIN species sp  ON sv.species_id = sp.species_id
JOIN plots p ON sv.plot_id = p.plot_id;
```

> Do Exercises 1-4 - [JOIN 1]({{ site.baseurl }}/exercises/Advanced-queries-join-1-SQL/), [JOIN 2]({{ site.baseurl }}/exercises/Advanced-queries-join-2-SQL/), [JOIN 3]({{ site.baseurl }}/exercises/Advanced-queries-join-3-SQL/), [JOIN 4]({{ site.baseurl }}/exercises/Advanced-queries-join-4-SQL/)
