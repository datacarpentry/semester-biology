---
layout: page
element: notes
title: SQL for dplyr users
language: SQL
---

> Remember to
>
> * Install DB Browser
> * Set font sizes to larger values under:
> * Preferences -> Data Browers -> Font size
> * Preferences -> SQL -> SQL editor font size & SQL log font size
> * Download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/11188550).
> * Open `portal_mammals.sqlite` in DB Browser.

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

* `Database Structure` - what is in this database
* `Browse Data` - use dropbox to view data in tables + filter for data checks
* `Execute SQL` - where we write queries
* Run SQL using play button (or w/ `Ctrl/command` + `Enter`)

### Selecting columns

* Choose which columns using `SELECT`
* If we want to get all of the columns we can use `*`, which is a wildcard that
means "all".

```sql
SELECT *
FROM surveys;
```

* To select specific columns we list them by name
* Just like `dplyr`, but with different formatting

```sql
SELECT year, month, day
FROM surveys;
```

* For unique values use `DISTINCT`.

```sql
SELECT DISTINCT year, month, day
FROM surveys;
```

* We can also do calculations and use functions
* Just like in `dplyr`

```sql
SELECT year, month, day, species_id, hindfoot_length/10
FROM surveys;
```

```sql
SELECT year, month, day, species_id, ROUND(hindfoot_length/10)
FROM surveys;
```

### Filtering

* The equivalent of `filter` in SQL is `WHERE`
  * Follow `WHERE` with a conditional statement
  * Unlike in R `=` not `==` for equality

```sql
SELECT year, month, day, species_id, ROUND(hindfoot_length/10)
FROM surveys
WHERE species_id = 'DS';
```

* To combine two or more conditions use `AND` and `OR`.

```sql
SELECT year, month, day, species_id, ROUND(hindfoot_length/10)
FROM surveys
WHERE species_id = 'DS' AND year > 1990;
```

* The red cells are NULL values, in this case instances were no hind foot
  measure was taken. We can use `WHERE` to remove them by asking SQL to only
  give us non-NULL values.

```sql
SELECT year, month, day, species_id, ROUND(hindfoot_length/10)
FROM surveys
WHERE species_id = 'DS' AND year > 1990 AND hindfoot_length IS NOT NULL;
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
* Create them by clicking button next to log and selecting `Save as view`
* If you need to replace a view first do `Database Structure` -> Right click on view -> `Delete View`

> Do the [Simple WHERE]({{ site.baseurl }}/exercises/Basic-queries-simple-where-SQL) exercise.

### Sorting

* Use `ORDER BY` to sort data.
* Equivalent of `arrange` in `dplyr` is `ORDER BY`.

```sql
SELECT genus, species
FROM species
ORDER BY genus;
```

* Use `DESC` to sort in descending order.

```sql
SELECT genus, species
FROM species
ORDER BY genus DESC;
```

* Use a list to sort by multiple columns.

```sql
SELECT genus, species
FROM species
ORDER BY taxa, genus, species;
```

### Aggregation

* Like in `dplyr` we use `GROUP BY` to calculate values for different groups.

```sql
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

### Order matters

> Nemonic from: https://twitter.com/statsnam/status/1149431249511075840

Select - So  
From - Few  
Where - Workers  
Group by - Go  
Having - Home  
Order by - On time

### Basic join

* Find the unique dates that each plot type was sampled on
* `inner_join` is `JOIN` or `INNER JOIN`
* `USING` specifies the columns to join on if the tables share column names (like `by` in `dplyr`)

```sql
SELECT DISTINCT year, month, day, plot_type 
FROM surveys
JOIN plots USING (plot_id);
```

* Unlike in `dplyr` you must specify the columns to join on (or things go badly)

```sql
SELECT year, month, day, plot_type
FROM surveys
JOIN plots
```

* If the column names don't match between tables use `ON`

```sql
SELECT DISTINCT year, month, day, plot_type
FROM surveys
JOIN species on surveys.species_id = species.species_id;
```

### Multi-table join

* To join multiple tables do multiple joins

```sql
SELECT year, month, day, taxa, plot_type
FROM surveys
JOIN species USING (species_id)
JOIN plots USING (plot_id)
```

> Do [Basic Join]({{ site.baseurl }}/exercises/Advanced-queries-basic-join-SQL/).
>
> Do [Multi-table Join]({{ site.baseurl }}/exercises/Advanced-queries-multi-table-join-SQL/).
