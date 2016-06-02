---
layout: page
element: notes
title: Nested Queries
language: SQL
---

Basically anything in SQL can be replaced with a query. This includes tables,
conditions, and even values.

### Tables

What is the mass of the average species at the site? So, we want to first
determine the average mass of the individual in each species, and then take the
average of those averages.

First, write a query to determine the average mass of each species:

```
SELECT species, AVG(wgt) as spavgmass
FROM Main
WHERE species IS NOT NULL
GROUP BY species
```

The use that as the table for another query that takes the average of those values:

```
SELECT AVG(spavgmass)
FROM (SELECT species, AVG(wgt) as spavgmass
      FROM Main
      WHERE species IS NOT NULL
      GROUP BY species);
```

### Values

What is the relative abundance of the different species at the site?
Let's start by just counting how many individuals there are

```
SELECT species, COUNT(*)
FROM Main
WHERE species IS NOT NULL
GROUP BY species;
```

Then use a subquery to divide by the total number of individuals

```
SELECT species, COUNT(*)/(SELECT COUNT(*) FROM Main)
SELECT species, COUNT(*)*1.0/(SELECT COUNT(*) FROM Main)
SELECT species, COUNT(*)*1.0/(SELECT COUNT(*) FROM Main WHERE species  IS NOT NULL);
```

And even sort based on the results of the subquery

```
SELECT species, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Main)
FROM Main
WHERE species IS NOT NULL
GROUP BY species
ORDER BY COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Main) DESC;
```

### Conditions

```
SELECT yr, mo, dy, species
FROM Main
WHERE plot NOT IN (SELECT PlotID FROM Plots WHERE PlotTypeAlphaCode = 'CO');
```
