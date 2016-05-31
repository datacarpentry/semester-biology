# Python + SQL

## Connecting to the database

```
import sqlite3 as dbapi
con = dbapi.connect('C:\Users\student\Desktop\portal_mammals.sqlite')
cur = con.cursor()
```

## Querying the database

### All records

```
cur.execute('SELECT mo, dy, yr, plot FROM PortalMammals_main WHERE yr=2002 AND species='SH'')
sh_query = cur.fetchall()
sh_query
```

### One record at a time (because it sometimes it's lots and lots of records)

```
cur.execute('SELECT mo, dy, yr, plot FROM PortalMammals_main WHERE yr=2002 AND species='SH'')
record = cur.fetchone()
while record:
    print(record)
    record = cur.fetchone()
```

## Using Python variables inside SQL

```
cur.execute('SELECT mo, dy, yr, plot FROM PortalMammals_main WHERE yr=? AND species=?', (2001, 'SH'))
sh_query = cur.fetchall()
sh_query
```

## Creating Tables

```
con = dbapi.connect('C:\Users\student\Desktop\newdatabase.sqlite')
cur = con.cursor()

CREATE TABLE Experiment(
    LoginID TEXT,
    Project TEXT,
    Experiment TEXT,
    Hours REAL,
    ExperimentDate NUM
)

CREATE TABLE Experiments(
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    LoginID TEXT NOT NULL,
    Project TEXT NOT NULL,
    Experiment TEXT NOT NULL,
    Hours REAL,
    ExperimentDate NUM
)

```

## Updating Tables

### Adding new records

```
INSERT INTO Experiment VALUES('epwhite', 'awesomeecology', 1, 18, 2011-11-09)
con.commit()
```

If not all values are being added

```
INSERT INTO Experiment (LoginID, Project, Experiment) VALUES('epwhite', 'awesomeecology', 2)
con.commit()
```

### Modifying existing records

```
UPDATE Experiment SET Hours=10, ExperimentDate=2011-11-08
WHERE LoginID='epwhite' AND Project='awesomeecology' AND Experiment=2
con.commit()
```

### Deleting records

```
DELETE Experiment
WHERE Project='awesomeecology' AND Experiment=2
con.commit()
```
