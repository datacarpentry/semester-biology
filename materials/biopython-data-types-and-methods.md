---
layout: page
element: notes
title: Biopython Data Types & Methods
language: Python
---

Sequence objects

from Bio.Seq import Seq

my_seq = Seq('ATTAGC')

>>> len(my_seq)

6

 

#### Slicing

>>> my_seq[1:4]

Seq('TTA', Alphabet())

 

#### Methods

my_seq.complement()

my_seq.reverse_complement()

my_seq.transcribe()

my_seq.translate()

 

### Sequence Record objects

from Bio.SeqRecord import SeqRecord

my_seq_id = 'AC12345'

my_seq_record = SeqRecord(my_seq, id=my_seq_id)
