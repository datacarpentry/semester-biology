---
layout: page
element: notes
title: Basic Queries
language: SQL
---

> Remember to
>
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * connect `portal_mammals.sqlite` to SQLite Manager.

> Introduce the Portal Project database

### Database Queries

* Data is separate from manipulations of the data
* Tables - store the data
* Queries - store questions about the data
    * If we update the data, the query asks the same question of the new data.

### Using SQLite Manager

* Use `Execute SQL` tab
* Run SQL w/ keyboard shortcut `command` + `;`

### Selecting columns

* Choose which columns to return.

```
SELECT year, month, day
FROM surveys;
```

* They can occur in any order.

```
SELECT month, day, year
FROM surveys;
```

* If we want to get all of the columns we can use `*`, which is a wildcard that
means "all".

```
SELECT *
FROM surveys;
```

* For unique values use `DISTINCT`.

```
SELECT DISTINCT year, month, day
FROM surveys;
```

* We can also do calculations in the `SELECT`.

```
SELECT species_id, hindfoot_length/1000.0
FROM surveys;
```

* We can also use functions.

```
SELECT species_id, ROUND(hindfoot_length/1000.0, 2)
FROM surveys;
```

> Do [Exercise 1 - SELECT]({{ site.baseurl }}/exercises/Basic-queries-select-SQL).
> Don't worry if you don't know how to save it yet, we'll cover that in a
> minute.

### Saving queries for future use

* Views save queries to run again.
* Create them by using `Create View` in the `View` menu, or by adding `CREATE
  VIEW *viewname* AS` to the beginning of a query.

```
CREATE VIEW hindfoots_m AS
SELECT species_id, ROUND(hindfoot_length/1000.0, 2)
FROM surveys;
```

> Save the results of Exercise 1 as a new view.


### Filtering

* Use `WHERE` to select only the rows meeting certain criteria.
    * Follow `WHERE` with a conditional statement
        * General form: column, condition, value
        
        `=`       | equals
        `>`  `<`  | greater / less than
        `>=` `<=` | greater / less than or equal to
        `!=` `<>` | not equals (`!=` *consistent with other languages*)

```
SELECT hindfoot_length
FROM surveys
WHERE species_id = 'DS';
```

```
SELECT species_id
FROM surveys
WHERE hindfoot_length >= 30;
```

* To combine two or more conditions use `AND` and `OR`.

```
SELECT year, month, day, species_id, hindfoot_length
FROM surveys
WHERE species_id = 'DS' AND year > 1990;
```

* The red cells are NULL values, in this case instances were no hind foot
  measure was taken. We can use `WHERE` to remove them by asking SQL to only
  give us non-NULL values.

```
SELECT year, month, day, species_id, hindfoot_length
FROM surveys
WHERE species_id = 'DS' AND year > 1990 
  AND hindfoot_length IS NOT NULL;
```

* If you want only NULL values, use `IS NULL` instead

> Do [Exercise 2 - WHERE]({{ site.baseurl }}/exercises/Basic-queries-where-SQL).


### Style

* SQL generally doesn't care about capitalization or line breaks. So it will run
a query like this.

```
seLEcT year, MONTH, dAY, WEIght FrOm SURveyS wheRe hindfoot_LENGTH > 30 aND spECIes_ID = 'DM';
```

* This is difficult to read so we follow style rules for writing SQL code
    * Capitalize SQL commands
    * Lowercase variable names
	* One clause/line


### Sorting

* Use `ORDER BY` to sort data.

```
SELECT genus, species
FROM species
ORDER BY genus;
```

* Use `DESC` to sort in descending order.

```
SELECT genus, species
FROM species
ORDER BY genus DESC;
```

* Use a list to sort by multiple columns.

```
SELECT genus, species
FROM species
ORDER BY taxa, genus, species;
```

> Do [Exercise 3 - ORDER BY]({{ site.baseurl }}/exercises/Basic-queries-order-by-SQL).


### Comments

* Even with good style it can quickly become difficult to remember exactly what
  a long query is doing. To help us remember/understand what the code is doing 
  we can use comments.

```
-- Get post-2000 weight data on Kangaroo Rats
SELECT year, month, day, species_id, weight
FROM surveys
WHERE year > 2000 AND species_id IN ('DO', 'DM', 'DS');
```

* `IN` is a short way to check a single variable against multiple conditions. In
  this case `species_id = 'DO' OR species_id = 'DM' OR species_id = 'DS'`.
