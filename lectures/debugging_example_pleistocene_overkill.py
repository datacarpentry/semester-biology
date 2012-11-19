import numpy as np

def mean_mass(masses):
    """Return the mean of a list of masses"""
    mean_mass = np.mean(masses)
    return masses

all_data = np.genfromtxt('MOMv3.3.txt', delimiter='\t',
                          names=['continent', 'status', 'order', 'family',
                                 'genus', 'species', 'log10mass', 'mass', 'ref'])

all_data = all_data[all_data['mass'] != -999.0]
continents = all_data['continent']
status = all_data['status']
masses = all_data['mass']

results = []
for continent in continents:
    extinct_masses = masses[(status=='extinct') & (continents==continent)]
    extant_masses = masses[(status=='extant') & (continents==continent)]
    avg_extinct_mass = np.mean(extinct_masses)
    avg_extant_mass = np.mean(extant_masses)
    diff = avg_extant_mass - avg_extinct_mass
    results.append([continent, avg_extantmass, avg_extinctmass, diff])
    
for line in results:
    print line