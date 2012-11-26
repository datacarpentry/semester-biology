Advanced Queries in Access
==========================

So far we've learned about basic SELECT queries in Access,
but there are several other kinds.

Make table queries
------------------

One thing we often want to do is make new tables using queries.
This is particularly useful for restructuring an existing database.

1. Make the query that produces the results you want
2. On the **Design** tab change the **Query Type** to **Make Table**
3. Give the new table a name
4. Press **Run**
5. Click **Yes**

Append queries
--------------

If we want to add new data to an existing table, we can use an Append query.
This is useful for carefully adding new data,
because we can import the data into a temporary table,
make sure everything is good, and then add it with to the main table.

1. Make the query that produces the results you want to add to the existing table
2. On the **Design** tab change the **Query Type** to **Append**
3. Tell Access what table you want to append the data to
4. Click **Run**
5. Click **Yes**

Update queries
--------------

If we want to change the data in an existing table we can use an Update query.

1. Create a new query
2. On the **Design** tab change the **Query Type** to **Update**
3. Select the fields you want to change
4. Indicate the value that those fields should be changed to in the **Update To** box
5. Add the Criteria under which to make the change
6. Click **Run**
7. Click **Yes**

The combined Criteria apply to all fields and do not need to include the field(s) being updated.

### Example

If we realized that all individuals identified as DM between 1990 and 1992
were actually DO we could do an update query to correct this.

Crosstab queries
----------------

Sometimes we want classic crosstab data for analysis,
where the rows group by one variable, the columns group by another variable,
and the cells contain values for each unique combination of row and column values.
For example, a common example of this in biology is a Site by Species matrix,
where the rows are different species, the columns are different sites,
and the values are counts.

1. Create a new query
2. On the **Design** tab change the **Query Type** to **Crosstab**
3. Add the grouping fields for the rows and columns and the value field
4. In the **Total** row indicate which fields to group by and how to calculate
the appropriate value (i.e., is it a Count, a Sum, etc.)
5. In the **Crosstab** row indicate which field is the Column Heading,
which is the Row Heading, and which is the value

### Example
* Portal Species by Plots matrix
* Then change from Count to Biomass