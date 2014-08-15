--- layout: post title: 6. Making Choices 3 [problem] created:
1317157601 categories: - !binary |- NA== - !binary |- aW50cm8= - !binary
|- NA== - !binary |- aW50cm8= - !binary |- NA== - !binary |- aW50cm8= -
!binary |- aW50cm8= - !binary |- aW50cm8= - !binary |- NQ== - !binary |-
aW50cm8= - !binary |- NQ== - !binary |- aW50cm8= - !binary |- NQ== -
!binary |- aW50cm8= - !binary |- NQ== - !binary |- aW50cm8= ---

Write a function, dna\_or\_rna(sequence), that determines if a sequence
of base pairs is DNA, RNA, or if it is not possible to tell given the
sequence provided. This function should work with both upper and lower
case letters. Since all the function will know about the material is the
sequence the only way to tell the difference between DNA and RNA is that
RNA has the base Uracil (U) instead of the base Thymine (T). Have the
function return one of three outputs: 'DNA', 'RNA', or 'UNKNOWN'. Use
the function and a for loop to print the type of the sequences in the
following list.

    sequences = ['ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg',
                 'gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau',
                 'gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc',
                 'guuuccuacaguauuugaugagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu',
                 'GAUAAGGAAGAUGAAGACUUUCAGGAAUCUAAUAAAAUGCACUCCAUGAAUGGAUUCAUGUAUGGGAAUCAGCCGGGUC']
