---
layout: page
element: notes
title: 3-day Introduction to Databases
language: SQL
---


Monday
------

### Intro
Basic intro lecture

### Intro to SQLite Manager
* Install
* Executing SQL
* Navigation
* Saving queries - Views
* Imports

### Intro to SQL
Quick example of Selecting, Filtering, and Sorting

Wednesday
---------

### Aggregation
* Basic joins
* Filter on aggregate vs. raw values
* Show how joins work
    * Join main table to species table
    * Show species and scientific name side by side
    * Show distinct
    * Filter by weight > 100 g

### Joins


Friday
------

### Missing data

### Nesting queries

    SELECT yr, COUNT(period)
    FROM (SELECT yr, period FROM PortalMammals_main GROUP BY yr, period)
    GROUP BY yr;