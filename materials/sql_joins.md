---
layout: page
element: notes
title: Joins
language: SQL
---

### Basic join

```
SELECT yr, mo, dy, scientificname
FROM Main
JOIN Species ON species = new_code;
```

### Multi-table join

```
SELECT yr, mo, dy, scientificname
FROM Main
JOIN Species ON species = new_code
JOIN Plots on plot = PlotID;
```

### Multi-table join with abbreviations

```
SELECT m.yr, m.mo, m.dy, s.scientificname
FROM Main m
JOIN Species s ON m.species = s.new_code
JOIN Plots p on m.plot = p.PlotID;
```

### No ON clause

```
SELECT species, scientificname
FROM Main
JOIN Species;
```

### Just like using WHERE:

```
SELECT species, scientificname
FROM Main
JOIN Species WHERE species = new_code;
```

> Do Exercises 1-4 - Joins [1]({{ site.baseurl }}/exercises/Advanced-queries-join-1-SQL/) \| [2]({{ site.baseurl }}/exercises/Advanced-queries-join-2-SQL/) \| [3]({{ site.baseurl }}/exercises/Advanced-queries-join-3-SQL/) \| [4]({{ site.baseurl }}/exercises/Advanced-queries-join-4-SQL/)
