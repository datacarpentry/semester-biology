--- layout: post title: Running BLAST from Python created: 1291669337
categories: [] ---
\# Import the modules for interfacing with BLAST and parsing the output
from Bio.Blast import NCBIWWW, NCBIXML
 
\# Blast the sequence of interest (in this case using the accession
number
result\_handle = NCBIWWW.qblast("blastn", "nr", "8332116")
 
\# Parse the resulting output
blast\_record = NCBIXML.read(result\_handle)
 
\# Loop over the alignments printing some output of interest
E\_VALUE\_THRESH = 0.004
for alignment in blast\_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect \< E\_VALUE\_THRESH:
            print
            print '\*\*\*\*Alignment\*\*\*\*'
            print 'sequence:', alignment.title
            print 'length:', alignment.length
            print 'e value:', hsp.expect
            print hsp.query[0:75] + '...'
            print hsp.match[0:75] + '...'
            print hsp.sbjct[0:75] + '...'
