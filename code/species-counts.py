"""Count the number of individuals of each species in a data file

Input file format:

2013-03-22 bluejay 5
2013-03-22 mallard 9
2013-03-21 robin 1
2013-03-20 robin 30

"""

import fileinput

def get_raw_data():
    """Load data from stdin"""
    data = []
    for line in fileinput.input():
        data.append(line.strip().split())
    return data

def get_species_counts(data):
    """Count the number of individuals of each species"""
    species_counts = dict()
    for record in data:
        species = record[1]
        count = int(record[2])
        species_counts[species] = species_counts.get(species, 0) + count
    return species_counts

def main():
    data = get_raw_data()
    species_counts = get_species_counts(data)
    for species in species_counts:
        print(species + ' ' +  str(species_counts[species]))

if __name__ == '__main__':
    main()