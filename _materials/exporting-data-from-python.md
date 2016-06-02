--- layout: post title: Exporting data from Python created: 1288905276
categories: [] ---

#### List of lists into CSV file

import csv

output\_file = open('C:\\path\\to\\file', 'w')

datawriter = csv.writer(output\_file)

datawriter.writerows(data)

output\_file.close()

 

#### Numpy array into CSV file

import numpy

numpy.savetxt('C:\\path\\to\\file', X, delimiter = ',')
