"""Example for first day of class in Intro"""

import urllib2
import pandas as pd
import matplotlib.pyplot as plt


url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
web_data = urllib2.urlopen(url)
data = pd.read_table(web_data, sep='\t')
plt.loglog(data['mass(g)'], data['litter size'], 'bo')

data_by_family = data.groupby('family')
for fam, fam_data in data_by_family:
    if len(fam_data) > 10:
        plt.figure()
        plt.loglog(fam_data['mass(g)'], fam_data['litter size'], 'bo')
    else:
        print(str(fam) + "did not have enough data to analyze")