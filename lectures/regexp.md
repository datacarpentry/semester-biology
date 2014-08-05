Regular Expressions
===================

NOTES
-----
* Regular expressions first (since this is the hard part)
* Wed - Style, including list comprehensions
* Fri - Program Design (took out the Program Design as a 

Demo
----
Use example from this summer

Imports
-------
* Do imports using simple read from file

Example
-------
Do a basic demo to get students started on the Wikipedia mammal species list problem.

### Highlight

* import file using ``open()``
* inspecting lines that are ignored
* function for regular expression check

### Example

    import re

    def get_species(inputstring):
        species_re = "''\[\[(.*)\]\]''"
        species_search = re.search(species_re, inputstring)
        if species_search:
            return species_search.group(1)

    inputfile = open('wikipedia_rodents.txt')
    results = []
    nomatch = []
    for line in inputfile:
        species = get_species(line)
        if species:
            splitspecies = species.split()
            results.append(species)
        else:
            nomatch.append(line)