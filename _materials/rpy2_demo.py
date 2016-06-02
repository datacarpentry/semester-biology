# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Rpy2 demonstration

# <headingcell level=2>

# by Dan McGlinn (danmcglinn@gmail.com), 11-07-12

# <headingcell level=3>

# Part 1: Import necessary modules

# <codecell>

import rpy2.robjects as robj
import rpy2.rinterface as ri
import rpy2.robjects.vectors as rv
from rpy2.robjects.packages import importr

import numpy as np

# <headingcell level=3>

# Part 2: Interact with the R interpreter by creating and calling R objects

# <codecell>

# Interact with R using strings
print robj.r('3 + 4')

robj.r('x = 3')
print robj.r('x')

# <codecell>

# Interact with R using attributes
print robj.r.x
print "why are the two subsequent calls to ls producing different results?"
print robj.r.ls
print robj.r.ls()

# <codecell>

# create a python vector and compute R stats on it
x = rv.IntVector(range(0,11))
print "why are the two subsequent calls to mean producing different results?"
print robj.r('mean(x)')
print robj.r.mean(x)

print "Here are some other stats"
print "Sum"
print robj.r.sum(x)
print "Variance"
print robj.r.var(x)

# <headingcell level=3>

# Part 3: Create and interact with multi-dimensional R objects

# <codecell>

# create R matrices
v = robj.FloatVector(robj.r.rnorm(20))
m = robj.r.matrix(v, ncol = 2)
print(m)
print "According to R the column sums are"
print robj.r.apply(m, 2, 'sum')

# convert matrix into a numpy array
m_np = np.array(m)
print(m_np)

# <codecell>

# read in data as an R data.frame
faithful = robj.DataFrame.from_csvfile('/media/sf_Dropbox/teaching/rpy/faithful.dat', sep=' ')
print type(faithful)
print faithful.names

# <codecell>

# subset columns
# extract as a DataFrame
col_one = faithful.rx(1)
print robj.r.head(col_one)
col_one = faithful.rx('eruptions')
print robj.r.head(col_one)

# <codecell>

# extract as a Vector
print faithful.rx2(1)[0:11]
print faithful.rx2('eruptions')[0:11]

# <codecell>

# subset rows
print faithful.rx(robj.IntVector(range(1,6)), True)

# <headingcell level=3>

# Part 4: Work with R and python functions

# <codecell>

# create an R function and call it in the Python interpreter
robj.r('''
       calc_area_r = function(radius, verbose=FALSE)
       {
           if (verbose) {
               cat("I am calling calc_area_r().\n")
           }
           return( 2 * pi * radius )
       }
       calc_area_r(3)
       ''')

print robj.r.calc_area_r(5, verbose='TRUE')

# Make the calc_area_r a callable python function
calc_area_py = robj.r.calc_area_r
print "Here is the result of calc_area_py()"
print calc_area_py(5)
print type(calc_area_py)

# <codecell>

# Rpy supports keyword arguments if there is no pythonic conflict
robj.r.rnorm(10, mean=2, sd=3)

# <codecell>

# this will draw an error
robj.r.rpois(10, lambda=3) 

# <codecell>

# creating a keyword argument dictionary solves the problem
robj.r.rpois(10, **{'lambda' : 3})

# <codecell>

# Make a python function and call it within R

ri.initr()

stats = importr('stats')

def quad_f(x):
    x = x[0]
    return x ** -2 + 0.5 * x
   
# wrap the function f so it can be exposed to R
quad_fr = ri.rternalize(quad_f)
    
# define the interval to find the minimum over
interval = rv.IntVector((0, 10))
 
# call R's optimize()
res = stats.optimize(quad_fr, interval)
print res

# <headingcell level=3>

# Part 5: Creating and exporting R graphics

# <codecell>

# plotting
x = robj.r.runif(10)
y = robj.r.rnorm(10)

robj.r.plot(x, y, xlab="runif rv", ylab="rnorm rv", col="red")

# <codecell>

# close that graphic
robj.r('dev.off()')

# <codecell>

# export the graphic as a pdf
robj.r.pdf('/media/sf_Dropbox/teaching/rpy/example_r_plot.pdf')
robj.r.plot(x, y, xlab="runif rv", ylab="rnorm rv", col="red")
robj.r('dev.off()')

# <headingcell level=3>

# Part 6: Importing R librairies and pythonizing R

# <codecell>

# import R libraries
vegan = importr('vegan')

comm_mat = robj.r.matrix(robj.r.rpois(100, 1), 10, 10)
ca = vegan.cca(comm_mat)
print ca

robj.r.plot(ca)

# <codecell>

# close the graphical device
robj.r('dev.off()')

# <codecell>

# make R pythonic by making it clear which functions are attributed to which packages
base = importr('base')
stats = importr('stats')
graphics = importr('graphics')

m = base.matrix(stats.rnorm(100), ncol = 5)
pca = stats.princomp(m)
graphics.plot(pca, main = "Eigen values")
stats.biplot(pca, main = "biplot")

