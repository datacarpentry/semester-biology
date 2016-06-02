---
layout: page
element: notes 
title: Updating Tables
language: SQL
---

### Adding new records

Adding new records into an existing table is done using the [INSERT
INTO](http://www.w3schools.com/sql/sql_insert.asp) command. If values
for all fields are being added the command is as simple as:

```
INSERT INTO MyTable VALUES (value1, value2, value3)
```

If you are only adding values for some of the possible fields then you
need to indicate which fields the values correspond to:

```
INSERT INTO MyTable (column1, column2, column3) 
VALUES (value1, value2, value3)
```

### Modifying existing records

Modifying existing records is done using the
[UPDATE](http://www.w3schools.com/sql/sql_update.asp) command. In this
command we tell the database which table we want to update, what we want
to set the values of any or all of the fields to, and under what
conditions we should update the values:

```
UPDATE MyTable SET column1=value1, column2=value2 
WHERE SomeColumn=SomeValue
```

Be care to not forget the WHERE clause or the update statement will
update *all* of the records in the database.

### Deleting records

Deleting records is done using the
[DELETE](http://www.w3schools.com/sql/sql_delete.asp) command, with
information about which table we want to delete records from, and what
conditions specify which records should be deleted.

```
DELETE FROM MyTable WHERE SomeColumn=SomeValue
```

Again, don't forget the WHERE clause or all of the rows in the table
will be deleted.
