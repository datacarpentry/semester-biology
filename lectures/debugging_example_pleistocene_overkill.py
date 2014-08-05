import numpy as np

def mean_mass(masses):
    """Return the mean of a list of masses"""
    mean_mass = np.mean(masses)
    return mean_mass

all_data = np.genfromtxt('MOMv3.3.txt', delimiter='\t', dtype=None,
                          names=['continent', 'status', 'order', 'family',
                                 'genus', 'species', 'log10mass', 'mass', 'ref'])

continents = all_data['continent']
status = all_data['status']
masses = all_data['mass']

unique_continents = np.unique(continents)
results = []
for continent in unique_continents:
    extinct_masses = masses[(status=='extinct') & (continents==continent)]
    extant_masses = masses[(status=='extant') & (continents==continent)]
    avg_extinct_mass = mean_mass(extinct_masses)
    avg_extant_mass = mean_mass(extant_masses)
    diff = avg_extant_mass - avg_extinct_mass
    results.append([continent, avg_extant_mass, avg_extinct_mass, diff])
    
for line in results:
    print line