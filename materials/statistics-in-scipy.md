--- layout: post title: Statistics in Scipy created: 1290010593
categories: [] ---

#### Import

import scipy.stats as stat

#### Regression

stat.linregress(x, y) -\> (slope, intercept, r, p-value,
standard\_error)

xs = np.array([min(x), max(x)])

p.plot(xs, reg\_out[1] + xs \* reg\_out[0])

####  

#### T-tests

##### One sample against a theoretical mean

t, pval = stat.ttest\_1samp(x, mean) -\> 

##### Two samples against each other

t\_2samp, p\_2samp = stat.ttest\_ind(x, y)

 
