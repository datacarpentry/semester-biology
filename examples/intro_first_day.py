"""Example for first day of class in Intro"""

import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
data = pd.read_csv(url, delimiter="\t")
plt.loglog(data['massg'], data['litter_size'], 'bo')

data_by_family = data.groupby('family')
for fam, fam_data in data_by_family:
    if len(fam_data) > 10:
        plt.figure()
        plt.loglog(fam_data['massg'], fam_data['litter_size'], 'bo')
    else:
        print(str(fam) + "did not have enough data to analyze")