--- layout: post title: A brief introduction to Numpy created:
1289246953 categories: [] ---

### What is Numpy

[Numpy](http://numpy.scipy.org/) is the fundamental library for
scientific computing in Python. It contains list like objects that work
like arrays, matrices, and data tables. This is how scientists typically
expect data to behave. Numpy also provides linear algebra, Fourier
transforms, random number generation, and tools for integrating C/C++
and Fortran code.

 

### Numpy Arrays

#### Creating a Numpy array

\>\>\> import numpy as np

\>\>\> example\_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

\>\>\> example\_array

array([[1, 2, 3],\
       [4, 5, 6],\
       [7, 8, 9]])\

\

#### Indexing an array

\>\>\> example\_array[1, 1]

5

\

#### Slicing an array\

\>\>\> example\_array[:, 0]

array([1, 4, 7])

\>\>\> example\_array[1, :]

array([4, 5, 6])

\>\>\> example\_array[1:3, 1:3]

array([[5, 6]

       [8, 9]])

\

#### Subsetting  a Numpy array

\>\>\> array1 = np.array([1, 1, 1, 2, 2, 2, 1])

\>\>\> array2 = np.array([1, 2, 3, 4, 5, 6, 7])

\>\>\> array2[array1==1]

array([1, 2, 3, 7])

\>\>\> array3 = np.array(['a', 'a', 'a', 'b', 'b', 'b', 'b'])

\>\>\> array2[(array1==1) & (array3=='a')]

array([1, 2, 3])\

\

#### Selecting a column if columns are named

\>\>\> named\_array['column\_name']\

\

### Math\

#### Arrays let you do basic math on every element in the array\

\>\>\> array1 \* 2 + 1\

array([3, 3, 3, 5, 5, 5, 3])

\>\>\> array1 + array2

array([2, 3, 4, 6, 7, 8, 8])

\

#### Linear algebra can be done using matrices

\>\>\> matrix1 = np.matrix([[1, 2, 3], [4, 5, 6]])

\>\>\> matrix2 = np.matrix([1, 2, 3])

\>\>\> matrix1 \* matrix2.transpose()

matrix([[14],\
        [32]])

\

### Importing data

The numpy function
[genfromtxt](http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html)
is a powerful way to import text data. It can use different delimiters,
skip header rows, control the type of imported data, give columns of
data names, and a number of other useful goodies. See [the
documentation](http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html)
for a full list of features of run help(np.genfromtxt) from the Python
shell (after importing the module of course).\

#### Basic

\>\>\> data = np.genfromtxt('C:\\path\\to\\file\\datafile.csv',
delimiter=',')

#### Auto-detect data types by column

\>\>\> data = np.genfromtxt('C:\\path\\to\\file\\datafile.csv',
dtype=None, delimiter=',')

#### Naming columns

\>\>\> data = np.genfromtxt('C:\\path\\to\\file\\datafile.csv',
names=['column1', 'column2', 'column3'], delimiter=',')

#### Get column names from header row

\>\>\> data = np.genfromtxt('C:\\path\\to\\file\\datafile.csv',
names=True, delimiter=',')

\

### Exporting data

\>\>\> np.savetxt('C:\\path\\to\\file\\outputfile.csv', example\_matrix,
delimiter=',')

\

### Random number generation

#### Random uniform (0 to 1)\

\>\>\> np.random.rand(rows, cols)

#### Random normal (mean = 0, stdev = 1)\

\>\>\> np.random.randn(rows, cols)

#### Random integers

\>\>\> np.random.randint(min, max, [rows, cols])\

