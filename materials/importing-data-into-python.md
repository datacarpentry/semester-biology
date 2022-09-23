---
layout: page
element: notes
title: Importing data
language: Python
---

### From files

#### CSV files into list of lists

```python
datafile = open('C:\\path\\to\\file, 'r')
data = []
for row in datafile:
    data.append(row.strip().split(','))
```
 

#### CSV files into list of lists using the csv module

```python
import csv

datafile = open('C:\\path\\to\\file, 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)
```
 

#### CSV files into numpy array {style="margin-bottom: 0in; font-weight: normal;"}

```python
import numpy

data = numpy.genfromtxt('C:\\path\\to\\file', delimiter = ',') OR data =
numpy.loadtxt('C:\\path\\to\\file', delimiter = ',')
```
 

#### GenBank

```python
from Bio import SeqIO

gb_file = open('C:\\path\\to\\genbankfile', 'r')
gb_record = SeqIO.read(gb\_file, "genbank")
```

### From the web

#### CSV files into list of lists using csv module

```python
import csv
import urllib

url = "http://www.example.com/data.csv"
webpage = urllib.urlopen(url)
datareader = csv.reader(webpage)
data = []
for row in datareader:
    data.append(row)
```
 
#### GenBank

```python
from Bio import Entrez, SeqIO

Entrez.email = "my.email@whereever.edu"  #this lets NCBI know who you are if your program causes them problems
gb_web_file = Entrez.efetch(db="nucleotide", id="281371607", rettype="gb")
gb_record = SeqIO.read(gb\_web\_file, "genbank")
```