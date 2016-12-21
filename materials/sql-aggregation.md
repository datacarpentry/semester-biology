---
layout: page
element: notes
title: Aggregation
language: SQL
---

> Remember to
>
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * connect `portal_mammals.sqlite` to SQLite Manager.

### Aggregation

* Aggregation lets us combine rows into groups based on their values and
calculate combined values for each group.

```
SELECT COUNT(*)
FROM surveys;
```

* Other aggregation functions include `MIN`, `MAX`, `AVG`, and `SUM`.

```
SELECT MIN(weight), MAX(weight), AVG(weight)
FROM surveys;
```

* We can use `GROUP BY` to calculate these values for different groups. For
  example, to get the min, max, and average weight for each species.

```
SELECT species_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
GROUP BY species_id;
```

* We can group by multiple columns as well.

```
SELECT species_id, plot_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
GROUP BY species_id, plot_id;
```

* Aggregation functions remove null values from the calculations.

> Do [Exercise 7 - COUNT]({{ site.baseurl }}/exercises/Aggregation-count-SQL).

### `HAVING`

* To filter by an outcome of an aggregation use `HAVING`

```
SELECT species_id, plot_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
GROUP BY species_id, plot_id
HAVING MIN(weight) IS NOT NULL;
```

* This works after aggregation, whereas `WHERE` works before aggregation

```
SELECT species_id, plot_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
WHERE weight > 10
GROUP BY species_id, plot_id
HAVING MIN(weight) IS NOT NULL;
```

### Only grouped or aggregated fields in `SELECT`

* When using `GROUP BY` only fields that are in the `GROUP BY` clause or
aggregated fields should be used in the `SELECT`

```
SELECT species_id, plot_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
WHERE weight IS NOT NULL
GROUP BY species_id, plot_id;
```

* Using fields that aren't grouped or aggregated results in counter intuitive
  results.

```
SELECT species_id, plot_id, MIN(weight), MAX(weight), AVG(weight)
FROM surveys
WHERE weight IS NOT NULL
GROUP BY species_id;
```
