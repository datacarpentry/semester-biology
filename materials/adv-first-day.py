"""Example for first day of class in Intro"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import numpy as np

url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
data = pd.read_csv(url, sep='\t', na_values=-999.0)

plt.plot(data['mass(g)'], data['gestation(mo)'])

data['log_mass'] = np.log10(data['mass(g)'])
data['log_gestation'] = np.log10(data['gestation(mo)'])
plt.plot(data['log_mass'], data['log_gestation'], 'bo')

data_by_family = data.groupby('order')
for fam, fam_data in data_by_family:
    if len(fam_data) > 10:
        plt.figure()
        plt.plot(fam_data['log_mass'], fam_data['log_gestation'], 'bo')
        regr_results = sm.OLS.from_formula('log_gestation ~ log_mass', fam_data).fit()
        x = np.array([min(fam_data['log_mass']), max(fam_data['log_mass'])])
        y = regr_results.params.Intercept + regr_results.params.log_mass * x
        plt.plot(x, y, 'r-')

        sns.lmplot('log_mass', 'log_gestation', data=fam_data)
    else:
        print("%s did not have enough data to analyze" % fam)
        
plt.show()
