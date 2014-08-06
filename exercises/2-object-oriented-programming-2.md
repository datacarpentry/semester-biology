--- layout: post title: 2. Object Oriented Programming 2 created:
1319124137 categories: - !binary |- Ng== - !binary |- Ng== - !binary |-
YWR2 - !binary |- Ng== - !binary |- YWR2 - !binary |- Ng== - !binary |-
YWR2 ---

Expand the Platypus class, giving it three methods: \
\
*total\_fecundity*, which returns the total number of eggs laid\
*breeding\_seasons*, which returns the number of breeding seasons in
which the platypus laid at least 1 egg\
*lay\_eggs*, which adds the number of eggs laid to the end of the list\
\
It should look something like this:\
\
\>\> perry = Platypus("perry", [3, 2, 4, 1, 2])\
\>\> perry.breeding\_seasons()\
5\
\>\> perry.total\_fecundity()\
12\
\>\> perry.lay\_eggs(2)\
\>\> perry.total\_fecundity()\
14
