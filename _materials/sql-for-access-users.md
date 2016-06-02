---
layout: page
element: notes
title: SQL for Access Users
language: SQL
---

Side by Side Demonstrations
---------------------------

### Selecting

    SELECT day, month, year, species FROM surveys;

    SELECT * FROM surveys;

    SELECT DISTINCT year FROM surveys;

### Filtering

    SELECT * FROM surveys WHERE species="DM";

    SELECT * FROM surveys WHERE (year >= 2000) AND (species = "DM");

### Sorting

    SELECT * FROM species ORDER BY Genus ASC;
    SELECT * FROM species ORDER BY Genus DESC;
    SELECT * FROM species ORDER BY genus ASC, species ASC;

### Aggregation

Get the combined mass of all individuals in each year.

    SELECT year, SUM(wgt)
    FROM surveys
    GROUP BY year;

### Joins

    SELECT surveys.year, surveys.month, surveys.day, species.genus, species.species
    FROM surveys
    JOIN species ON surveys.species = species.species_id

### Combining it all

    SELECT surveys.year, species.genus, species.species, SUM(wgt / 1000.0)
    FROM surveys
    JOIN species ON surveys.species = species.species_id
    WHERE species.taxa="Rodent"
    GROUP BY surveys.year, species.genus, species.species
