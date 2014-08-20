---
layout: page
title: Reports in Access
---

In the same way that Forms are simple controllable ways to enter data in tables,
**Reports** are simple controllable ways to present the results of queries.
They can be used for accomplishing repeated tasks like:

* Permit applications
* Reports to permitting agencies
* Reports to funding agencies

Creating a Basic Report
-----------------------

1. Create a query that contains the information you want
2. Save the query
3. Highlight the query
4. On the **Create** tab in the **Reports** section click the **Report** button

### Example
Counts in each year for a chosen species

This is great, but if we want to do this for each species we'd have to edit the query to change the criteria.

Taking input in queries
-----------------------
Instead of editing the query each time we create a report, we can just have Access ask us which species we want.

1. Make a query
2. In the criteria row insert [], this tells Access that we want to enter the criteria when we run the query
3. *Optionally* enter some text to be displayed explaining what information is desired, this goes inside the []

### Example
Change query to take species name as input

Using the Report Wizard
-----------------------

If we want to exercise a little more control over the Report we can use the **Report Wizard**.
The initial process is the same:

1. Create a query that contains the information you want
2. Save the query
3. Highlight the query

but then instead of using the **Report** button we:

1. Click the **Report Wizard** button
2. Select the fields that you want to display
3. Select any grouping fields
    * These should be fields that use Group By in the query
    * Instead of being displayed as columns they will 
4. Select sort orders for any of the fields
5. Select a layout

### Example
Just display year and count without species name

Modifying a Report
------------------
We can modify reports using the **Design View**.

1. Move things around
2. Change fonts, formats, etc.
3. Add new information that is in the query, but not currently display. E.g.,
    1. Add a new text box using the button in the **Design** tab
    2. Select it
    3. Use the **Control Source** box in the **Data** tab of the **Property Sheet** to chose the data

### Example
Add species name to the header

An example with Grouping
------------------------
Let's look at another example.
Let's say that our reporting requirments involve presenting the data for all species.
To do this we would:

1. Write a query that gives us the information we need.
2. Use the **Report Wizard** to create a Report
3. On the **Grouping fields** screen select species

Just getting started
--------------------
There are *lots* of more advanced things that can be accomplished using Reports.
Hopefully this is enough to get you started.
