---
layout: page
element: notes
title: SQL for dplyr users
language: SQL
---

> Remember to
>
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/11188550).
> * connect `portal_mammals.sqlite` to SQLite Manager.

### Why Databases

* Good place to store data
* Lots of existing data is stored in them (which you might want to use)
* Support real-time collaboration on adding and updating data
* Handle out of memory computation

### Database Queries

* Data is separate from manipulations of the data
* Tables - store the data
* Queries - store questions about the data
    * If we update the data, the query asks the same question of the new data.

### Using DB Browser

* Use `Execute SQL` tab
* Run SQL w/ keyboard shortcut `command` + `;`

### Selecting columns

* Choose which columns using `SELECT`
* Just like `dplyr`, but with different formatting

```
SELECT year, month, day
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

* We can also do calculations and use functions
* Just like in `dplyr`

```
SELECT species_id, ROUND(hindfoot_length/10, 1)
FROM surveys;
```

### Filtering

* The equivalent of `filter` in SQL is `WHERE`
    * Follow `WHERE` with a conditional statement
    * Unlike in R `=` not `==` for equality

```
SELECT hindfoot_length
FROM surveys
WHERE species_id = 'DS';
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

### Style

* SQL generally doesn't care about capitalization or line breaks. So it will run
a query like this.
* To make the code readable follow style rules for writing SQL code
    * Capitalize SQL commands
    * Lowercase variable names
	* One clause/line

### Saving queries for future use

* Views save queries to run again.
* Create them by adding `CREATE VIEW name AS` to top of query
* If you need to replace a view first run `DROP VIEW name`

> Do the [Simple WHERE]({{ site.baseurl }}/exercises/Basic-queries-simple-where-SQL) exercise.


### Sorting

* Use `ORDER BY` to sort data.
* Equivalent of `arrange` in `dplyr` is `ORDER BY`.

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


### Aggregation

* Like in `dplyr` we use `GROUP BY` to calculate values for different groups.

```
SELECT species_id, AVG(weight), COUNT(species_id)
FROM surveys
GROUP BY species_id;
```

* We can group by multiple columns as well.

<pre>
SELECT species_id, <b>plot_id,</b> AVG(weight), COUNT(species_id)
FROM surveys
GROUP BY species_id<b>, plot_id</b>;
</pre>

* Aggregation functions remove null values from the calculations.
* `COUNT(species_id)` counts the number of individuals identified to species
* To count the number of individuals with weights

<pre>
SELECT species_id, plot_id, AVG(weight), COUNT(<b>weight</b>)
FROM surveys
GROUP BY species_id, plot_id;
</pre>

* Using `*` counts any row with at least one non-null value
* We can name aggregated columns using `as`

<pre>
SELECT species_id, plot_id, AVG(weight) as avg_weight, COUNT(weight) as num_indiv
FROM surveys
GROUP BY species_id, plot_id;
</pre>

> Do the [COUNT]({{ site.baseurl }}/exercises/Aggregation-count-SQL) exercise.


### Basic join

* Find the unique dates that each plot type was sampled on
* `inner_join` is `JOIN` or `INNER JOIN`
* `USING` specifies the columns to join on if the tables share column names

```
SELECT DISTINCT year, month, day, plot_type 
FROM surveys
JOIN plots USING (plot_id);
```

* Unlike in `dplyr` you must specify the columns to join on (or things go badly)

    ```
    SELECT year, month, day, plot_type
    FROM surveys
    JOIN plots
    ```

* If the column names don't match between tables use `ON`

```
SELECT DISTINCT year, month, day, plot_type 
FROM surveys
JOIN species on surveys.species_id = species.species_id;
```

### Multi-table join

* To join multiple tables do multiple joins

```
SELECT year, month, day, taxa, plot_type
FROM surveys
JOIN species USING (species_id)
JOIN plots USING (plot_id)
```

> Do [Basic Join]({{ site.baseurl }}/exercises/Advanced-queries-basic-join-SQL/).
>
> Do [Multi-table Join]({{ site.baseurl }}/exercises/Advanced-queries-multi-table-join-SQL/).
