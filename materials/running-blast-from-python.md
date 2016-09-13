--- 
layout: page
element: notes
title: Running BLAST
language: Python
---

# Import the modules for interfacing with BLAST and parsing the output
from Bio.Blast import NCBIWWW, NCBIXML
 
# Blast the sequence of interest (in this case using the accession
number
result_handle = NCBIWWW.qblast("blastn", "nr", "8332116")
 
# Parse the resulting output
blast_record = NCBIXML.read(result_handle)
 
# Loop over the alignments printing some output of interest
E_VALUE_THRESH = 0.004
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print
            print '****Alignment****'
            print 'sequence:', alignment.title
            print 'length:', alignment.length
            print 'e value:', hsp.expect
            print hsp.query[0:75] + '...'
            print hsp.match[0:75] + '...'
            print hsp.sbjct[0:75] + '...'
