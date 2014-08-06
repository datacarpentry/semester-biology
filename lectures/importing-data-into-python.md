--- layout: post title: Importing data into Python created: 1288801032
categories: [] ---

### From files

#### CSV files into list of lists

datafile = open('C:\\path\\to\\file, 'r')

data = []

for row in datafile:

    data.append(row.strip().split(','))

 

#### CSV files into list of lists using the csv module

import csv

datafile = open('C:\\path\\to\\file, 'r')

datareader = csv.reader(datafile)

data = []

for row in datareader:

    data.append(row)

 

#### CSV files into numpy array {style="margin-bottom: 0in; font-weight: normal;"}

import numpy

data = numpy.genfromtxt('C:\\path\\to\\file', delimiter = ',') OR data =
numpy.loadtxt('C:\\path\\to\\file', delimiter = ',')

 

#### GenBank

from Bio import SeqIO

gb\_file = open('C:\\path\\to\\genbankfile', 'r')

gb\_record = SeqIO.read(gb\_file, "genbank")

###  

### From the web

#### CSV files into list of lists using csv module {style="font-size: 14px; margin-top: 0px; margin-right: 0px; margin-bottom: 0.5em; margin-left: 0px; font-weight: normal; line-height: 14px; color: #535353; padding: 0px;"}

import csv

import urllib

url = "http://www.example.com/data.csv"

webpage = urllib.urlopen(url)

datareader = csv.reader(webpage)

data = []

for row in datareader:

    data.append(row)

 

#### GenBank {style="font-size: 14px; margin-top: 0px; margin-right: 0px; margin-bottom: 0.5em; margin-left: 0px; font-weight: normal; line-height: 14px; color: #535353; padding: 0px;"}

from Bio import Entrez, SeqIO

Entrez.email = "my.email@whereever.edu" \#this lets NCBI know who you
are if your program causes them problems

gb\_web\_file = Entrez.efetch(db="nucleotide", id="281371607",
rettype="gb")

gb\_record = SeqIO.read(gb\_web\_file, "genbank")
