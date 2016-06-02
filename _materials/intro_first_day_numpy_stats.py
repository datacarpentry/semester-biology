"""Example for first day of class in Intro"""

import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
web_data = urllib2.urlopen(url)
data = np.genfromtxt(web_data, delimiter='\t', names=True, dtype=None, skip_footer=4)
#plt.loglog(data['massg'], data['litter_size'], 'bo')

families = np.unique(data['family'])
for fam in families:
    fam_data = data[data['family'] == fam]
    if len(fam_data) > 10:
        plt.figure()
        y = np.log10(fam_data['litter_size'])
        x = np.log10(fam_data['massg'])
        X = sm.add_constant(x, prepend=True)
        regression_results = sm.OLS(y, X).fit()
        plt.plot(x, y, 'bo')
        intercept, slope = results.params
        y_pred = intercept + slope * x
        plt.plot(x, y_pred, 'r-')
    else:
        print(str(fam) + "did not have enough data to analyze")