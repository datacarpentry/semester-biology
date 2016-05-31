--- layout: post title: Biopython Data Types & Methods created:
1291696272 categories: [] ---

Sequence objects

from Bio.Seq import Seq

my\_seq = Seq('ATTAGC')

\>\>\> len(my\_seq)

6

 

#### Slicing

\>\>\> my\_seq[1:4]

Seq('TTA', Alphabet())

 

#### Methods

my\_seq.complement()

my\_seq.reverse\_complement()

my\_seq.transcribe()

my\_seq.translate()

 

### Sequence Record objects

from Bio.SeqRecord import SeqRecord

my\_seq\_id = 'AC12345'

my\_seq\_record = SeqRecord(my\_seq, id=my\_seq\_id)
