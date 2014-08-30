# Using Python's built-in help

You can access Python's built-in help using the `help()` function with the name
of any function inside the parentheses:

```
>>>help(round)
Help on built-in function round in module __builtin__:

round(...)
    round(number[, ndigits]) -> floating point number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative.
```

This provides a basic description of what the function does as well as its
required and optional arguments. Anything inside the `()` but not inside the
`[]` is a required argument that needs to be provided in the appropriate
order. So, this help document tells us that `number` is required for round to
work and we could call round as

```
>>> round(10.9)
11.0
```

Anything inside the `[]` is an optional argument, so we don't have to include
it. If we want to include it, in this case to specify the number of digits to
round to, we can either include all of the optional arguments in order, or we
can give the name of the optional argument we want to specify followed by an
equals sign and the value we want to use.

```
>>> round(11.21, 1)
11.2

>>> round(11.21, ndigits=2)
11.2
```

Providing the name of the optional argument can make it easier to remember what
the function is doing and can also be useful if there are several optional
arguments and we want to use the default values for some of them.
