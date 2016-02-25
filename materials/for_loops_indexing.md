For Loops
=========
Using Range
-----------
Print the even numbers from 1 to 10

    numbers = range(1, 11)
    for number in numbers:
        if number % 2 == 0:
            print number

Simpler
-------
    for number in range(1, 11):
        if number % 2 == 0:
            print number

####Or
    for number in range(2, 11, 2):
        print number

Using Range to Loop Over Values in a List
-----------------------------------------
In many languages we can use for value in values so we use the indexes to loop over values in a list

    sequences = ['atg', 'gtc', 'atta']
    for i in range(len(sequences)):
        print sequences[i]

And we can use this in Python to loop over two lists simultaneously

    seqID = [27, 63, 42]
    sequences = ['atg', 'gtc', 'atta']
    for i in range(len(sequences)):
        print seqID[i], sequences[i]

Enumerate
---------
Alternatively we can use enumerate

    seqID = [27, 63, 42]
    sequences = ['atg', 'gtc', 'atta']
    for i, sequence in enumerate(sequences):
        print seqID[i], sequence
