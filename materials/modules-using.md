# Using Modules

## Definition

Modules/packages/libraries are collections of related functions (and other
things). They given programming languages a way to store code in separate
pieces.

Some languages make a lot of functionality available without importing modules
(like R) and others keep most functionality in separate modules (like
Python). So, in Python, we need to import a module to even do fairly basic math.


## Importing modules

To load or import modules in Python we use `import`.

`>>> import math`

This loads the functions from the `math` module into memory.


## Using functions in modules

By default, if we want to use the functions in a module in Python we say which
module the function is located in by listing the module name, followed by a
period (referred to as a dot), followed by the function name.

```
>>> import math
>>> math.sqrt(16)
4
```

If we just use the name of the function we will get an error.

```
>>> sqrt(16)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-a69d70ec25ee> in <module>()
----> 1 sqrt()

NameError: name 'sqrt' is not defined
```

The module name is referred to as a namespace.

## Importing functions without namespacing

You can import all of the contents of a module without namespacing.

```
>>> from math import sqrt
>>> sqrt(16)
4
```

But this is generally a bad idea. The reason is that if we import several
modules this way and they have functions with the same name, then it will be
very difficult to tell which function we are actually using. This can cause very
difficult to track down bugs. Since we can't reasonably know the names of every
function in every module/package namespaces keep us safe.


## Importing specific functions without namespacing

We can import specific functions without namespacing by explicitly listing out
the functions we want to import.

```
>>> from math import log
>>> log(20)
2.995732273553991
```


## Aliases

We can also give a module a shorter and easier to type name.

```
>>> import math as m
>>> m.log10(10)
1.0
```

There are several common aliases in use in scientific Python programming.

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
