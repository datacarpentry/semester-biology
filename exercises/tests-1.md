--- layout: post title: 2. Tests 1 [problem] created: 1318968843
categories: - !binary |- YWR2 - !binary |- YWR2 - !binary |- YWR2 -
!binary |- NQ== - !binary |- YWR2 - !binary |- NQ== - !binary |- YWR2 -
!binary |- NQ== - !binary |- YWR2 ---

This is a follow up to the [Debugging 1
problem](http://www.programmingforbiologists.org/1-debugging-problem).

Write tests for your granger\_analysis\_code for the following cases and
save it in a file called test\_granger\_analysis\_code.py (remember that
the file has to start with test\_ for nose to find it). Make any
corrections/improvements that need to be made to the code so that all of
your tests pass.:

#### gc\_content()

1.  Sequence represented by upper case string
2.  Sequence represented by lower case string
3.  Sequence represented by mixed case string
4.  Sequence represented by multiline string

#### get\_size\_class()

In an email accompanying your "updated" code, Dr. Granger indicated that
the specifications for the earlength size classes were:

1.  extralarge: earlength \>= 15
2.  large: 10 \<= earlength \< 15
3.  medium: 8 \<= earlength \< 10
4.  small: earlength \< 8

Write tests to check:

1.  That each case is working when the numbers are in the range
2.  The edgecases of 8, 10, and 15
3.  What happens if non-numerical values are passed to the function
    (e.g., a string from a header row that didn't get removed)

Modify the main code so that all of your tests pass.


