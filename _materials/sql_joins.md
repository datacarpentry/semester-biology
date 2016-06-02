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
