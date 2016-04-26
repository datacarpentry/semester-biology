---
layout: page
title: Testing
---

What is testing?
----------------
* Testing checks to make sure if our code is doing what we think it is.
* Does so in a automated fashion
* So that once we tell the computer what to check for, it does the checking itself

Why test?
---------
1. Make sure that your code is giving you the correct output on simple cases
2. Prevent regressions
3. Prevent changes when someone else's code updates
4. **Don't publish the wrong answer because of a bug -> [like this](http://www.jstor.org/stable/25145087)**

Writing tests for Nose
----------------------
Create a file whose name begins with the word test (same directory as code to be tested)

Create new my_math.py file:

    def add(num1, num2):
        return num1 + num2

    def divide(numerator, denominator):
        return numerator / denominator

Create new test_my_math.py file

Import anything the code needs (including the module to be tested)

*Add*

    import my_math

Write functions beginning with test that assert something:

    def test_add_integers():
        assert add(2, 3) == 5

Running tests using nose
------------------------
* Run `nosetests` from the command line
    * Using -v for more explanation
* Use nose.run() from inside the function

    def test_add_ints_zero() == 2:
        assert add(2, 0) == 2

When tests fail
---------------
    def test_div_integers():
        assert divide(1, 4) == 0.25

*Run tests, fix integer division*

*Add*

    def test_div_integers_noneven():
        assert divide(1, 3) == 0.3333

*Run tests, add more 3s*

*Add*

    import nose
    nose.tools.assert_almost_equals(divide(1,3), 0.3333333)

Testing errors
--------------

We often want to know how to make sure that our code is throwing errors when
it should be. For example, if something goes wrong with a data file we don't
want the code to execute and potentially produce an incorrect result. However,
since all of our testing is based on errors any error in our code will typically
cause the test to fail. To address this an other issues nose has lots of useful
functions for testing (*walk through some examples*). The one we are looking for
here is ``nose.tools.assert_raises()``.

    def test_add_strings():
        nose.tools.assert_raises(ValueError, add, 'stuff', 'things')

Alternatively we can use the ``@raises`` decorator.

    @raises(TypeError)
    def test_add_lists():
        a = add([1, 2], [3, 4])

I often don't remember what the different error types are, so I will typically
trigger the error, make sure the error type makes sense, and then add it to my
test.

**Try adding a test for adding a string and a number**


Testing multiple values
---------------------------
There are some cases where we will want to test multiple values in a single test
rather than writing separate tests for each set of values. We could loop over
the values, but this will stop after the first failure. Instead, we can do this:

    def test_add_badvalues():
        values = [['teststring', 2], [0, 'teststring'], ['stuff', 'things']]
        for val1, val2 in values:
            yield check_badvalues, val1, val2

    def check_badvalues(val1, val2):
        nose.tools.assert_raises(ValueError, add, val1, val2)

We can see from the results that this runs and counts 3 separate tests. If one
of these tests fails, e.g., 

    def test_add_badvalues():
        values = [['teststring', 2], [2, 1], [0, 'teststring'], ['stuff', 'things']]
        for val1, val2 in values:
            yield check_badvalues, val1, val2

Not only will all of the other tests still run, but nose will tell us the
values that caused the test to fail.

###What is ``yield``
``yield`` is like return, but the function will return a generator. This means
that when you call the function, the code doesn't actually execute. Instead,
the function returns the generator object. The first time the function is run,
it will run until it hits yield, then it will return the first value of the
loop. Then, each additional call will run the loop in the function another time,
and return the next value, until there is no value to return. So, 
``test_add_badvalues()`` ends up being run once for every trip through the for
loop, which is why it doesn't stop at the first error.

Source: http://stackoverflow.com/a/231855/133513

Integration/regression testing
------------------------------
Calls higher level functionality and checks the results.
E.g., tax_resolve tests
