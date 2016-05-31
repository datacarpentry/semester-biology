## Regression

```
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
colnames = ['order', 'family', 'genus', 'species', 'mass', 'gestation', 'newborn_mass',
            'weaning_time', 'wean_mass', 'AFR',	'max_life_span', 'litter_size', 'litters_year', 'refs']
data = pd.read_csv(url, delimiter='\t', names=colnames, header=1, na_values=['-999', '-999.99'])

plt.loglog(data['mass'], data['max_life_span'], 'bo')

regr_results = smf.ols('np.log(max_life_span) ~ np.log(mass)', data).fit()
print regr_results.summary()
```
