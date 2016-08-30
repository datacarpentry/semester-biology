---
layout: page
element: notes
title: Nested Queries
language: SQL
---

### Take Home Message

* Basically, any object or value following a query command statement in SQL 
(*including tables, conditions, and even values*) can be replaced with another 
query.

### Tables

* What is the mass of the average species at the site? 
    * Determine the average mass of the individuals in each species. 
    * Take the average of the average masses of each species.

* Write a query to determine the average mass of each species:

```
SELECT species, AVG(wgt) as spavgmass
FROM Main
WHERE species IS NOT NULL
GROUP BY species;
```

* Use the results of that query as the table for another query that takes the 
average of those values:

```
SELECT AVG(spavgmass)
FROM (SELECT species, AVG(wgt) as spavgmass
      FROM Main
      WHERE species IS NOT NULL
      GROUP BY species);
```

### Values

* What is the relative abundance of the different species at the site?
    * Count how many individuals there are per species.
    * Divide the count per species by the total number of individuals.

* Write a query to determine the number of individuals per species: 

```
SELECT species, COUNT(*)
FROM Main
WHERE species IS NOT NULL
GROUP BY species;
```

* Modify the query with a subquery to divide by the total number of individuals:

```
SELECT species, COUNT(*)/(SELECT COUNT(*) FROM Main);
```
```
SELECT species, COUNT(*) * 100.0/(SELECT COUNT(*) FROM Main);
```
```
SELECT species, COUNT(*) * 100.0/(SELECT COUNT(*) 
                                  FROM Main 
                                  WHERE species IS NOT NULL);
```

* This finished version of the query even sorts based on the results of the subquery:

```
SELECT species, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Main)
FROM Main
WHERE species IS NOT NULL
GROUP BY species
ORDER BY COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Main) DESC;
```

### Conditions

* List the sampling events for all plots that are not control plots:

```
SELECT yr, mo, dy, species
FROM Main
WHERE plot NOT IN (SELECT PlotID FROM Plots WHERE PlotTypeAlphaCode = 'CO');
```

> Assign [Exercise 5 - Nesting Queries]({{ site.baseurl }}/exercises/Advanced-queries-nesting-queries-SQL/).
