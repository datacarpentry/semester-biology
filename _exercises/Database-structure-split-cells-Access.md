---
layout: exercise
topic: Database Structure 
title: Split Cells
language: Access
---

The Species table in the Portal database has a structural problem in
that the `oldcode` column often contains multiple pieces of
information in a single cell. This means that we can't really run
queries that use the `oldcode` field effectively. Think about what the
best structure would be for this table. It might include splitting the
table into two separate tables (wink, wink, nudge, nudge). Feel free to
check with Ethan to make sure you've got the right idea. Restructure the
database storing the new species table as `Species - better` and
naming any new tables you create with easy to understand names.
