---
layout: page
title: Debugging with a Debugger
---

Why
---
* Like a print statement but better
* Doesn't accidentally get left in the code
* Contains a complete snapshot of the status of the program
* Let's you walk through the code dynamically

Break points
------------
1. Insert breakpoint
2. Press Debug
3. Program runs until breakpoint and stops (before executing the line of code)
4. Stack Data gives the current values for all variables (Local vs. Global)
5. Pressing Debug again continues to the next breakpoint

Stepping
--------
* Step Into – goes line by line through the code including entering functions
* Step Over – does not enter functions
* Step Out – leaves the current function and return to whatever called it

Conditional breakpoints (Pro and other debuggers)
------------------------------------------
* Breakpoints can be made conditional
* Only stop the program if certain conditions are met
* Right click the breakpoint and add condition

Example - Pleistocene Overkill
------------------------------

### Mistakes
* Looping over all continents instead of unique
* Missing underscores in results.append()
* Missing dtype=None in import

### Process
1. Run, get error
2. Run debugger, highlights line with error, show Stack Data
3. Fix missing underscores
4. Restart
5. Lots of nan's, likely a problem with the data so look at it
6. Fix missing dtype=None and rerun
7. That fixed one of our problems, but now too many lines, not easy to see, so
8. Set a break point at start of loop
9. Demo step in/over/out
10. Use unique not actual

### Code

    import numpy as np

    def mean_mass(masses):
        """Return the mean of a list of masses"""
        mean_mass = np.mean(masses)
        return masses

    all_data = np.genfromtxt('MOMv3.3.txt', delimiter='\t', dtype=None,
                              names=['continent', 'status', 'order', 'family',
                                     'genus', 'species', 'log10mass', 'mass', 'ref'])

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
