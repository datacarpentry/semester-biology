---
layout: page
element: notes
title: Exporting data from Python
language: Python
---

#### List of lists into CSV file

import csv

output_file = open('C:path/to/file', 'w')

datawriter = csv.writer(output_file)

datawriter.writerows(data)

output_file.close()

 

#### Numpy array into CSV file

import numpy

numpy.savetxt('C:path/to/file', X, delimiter = ',')
