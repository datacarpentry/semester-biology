--- layout: post title: Exporting tables and queries from OpenOffice
Base to csv created: 1288729701 categories: [] ---

#### Option 1 - Using Calc

1.  Drag and drop the table/query into the upper left corner cell of an
    open Calc worksheet
2.  Save the sheet as a CSV file

#### Option 2 - By executing SQL

Option 1 is the easiest approach, but if you need to export large
quantities of data it won't work. To do this you can use Base's ability
to execute HSQL directly (thanks to
[Sliderule](http://user.services.openoffice.org/en/forum/memberlist.php?mode=viewprofile&u=761)
at the [OpenOffice community
forum](http://user.services.openoffice.org/en/forum/index.php) for [this
solution](http://user.services.openoffice.org/en/forum/viewtopic.php?f=13&t=5009#p23249)).

1.  Open the query
2.  Access the underlying SQL
3.  Copy it to the clipboard
4.  In the menu bar of the main Base window click **Tools -\> SQL**
5.  Paste the SQL from the query into the **Command to execute** window
6.  Go the to beginning of the word FROM and type **INTO TEXT
    "name\_of\_output\_file"** followed by a space
7.  Press the execute button
8.  Your query will have been saved as a csv file named
    name\_of\_output\_file.csv in the same directory as your database

#### Option 3 - Wait

There should be an [export utility for
Base](http://wiki.services.openoffice.org/wiki/Export_Manager) available
relatively soon...
