--- layout: post title: Using Python to Interface with Databases
created: 1318107057 categories: [] ---

We will use [SQLite](http://sqlite.org/) to discuss how to use Python
with databases, but most other major systems work in the same way, just
with a different library.

### Importing the library

We need to tell Python that we're going to be working with SQLite, so we
start by importing the [sqlite3
library](http://docs.python.org/library/sqlite3.html). By importing
using a generic name (e.g., dbapi) if we ever decide to change the
database system that we're using we can simply change the library name
in this single line of code (in concept; in practice subtle differences
between database systems may break things):

import sqlite3 as dbapi

### Connecting to the database

Next, we need to connect to the database using the database library's
connect method. With SQLite this is as simple as first making the
connect:

con = dbapi.connect('/path/to/database.sqlite')

and then getting a cursor which will let us execute SQL commands:

cur = con.cursor()

If the database does not currently exist then creating the connection
will create it.\

### Querying the database

We can now execute any SQL commands that we want in the database using
the cursor's execute method. Querying the database simply involves
writing the appropriate SQL and placing it inside a string in the
execute method call:

cur.execute('SELECT \* FROM mytable WHERE myfield = myvalue')

To get the results into Python we then use either the fetchone method to
fetch one record at a time (it returns None when there are no more
records to fetch so that you know when to stop) or the fetchall method
to return all of the records into a list. Each record is returned as a
tuple of values, one value per field.

myqueryrecords = cur.fetchall()

or

record = cur.fetchone()

while record:

    do\_something\_to(record)

    record = cur.fetchone()

If you want the database to return regular strings instead of unique
strings (indicated by the u in front of every string) you can do this
using the following command 

con.text\_factory = str

### Modifying the database

Modifications can also be made to the database using the execute
function. For example,

cur.execute('INSERT INTO mytable VALUES (value1, value2, value3')

cur.execute('DELETE FROM mytable WHERE myfield = myvalue')

In order for these changes to actually be made to the database we need
to commit them by calling

con.commit()

This protects us if something goes wrong with our program because the
changes won't be finalized until the point where we commit them.

### Using Python variables inside SQL queries

Often when working with databases in Python we will want to include
variables from our Python code as part of the query. To do this we place
a ? where each value should be inserted into the SQL statement and then
include a tuple with the values to be inserted as a second argument in
the execute statement.

cur.execute('INSERT INTO mytable VALUES (?, ?, ?)', (variable1,
variable2, variable3))
