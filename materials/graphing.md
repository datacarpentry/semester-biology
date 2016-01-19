---
layout: page
title: Graphing in Python
---

# Graphing

Most of the necessary information for learning how to make basic plots in Python
is in the [IPython notebook](http://nbviewer.ipython.org/urls/github.com/weecology/progbio/raw/master/ipynbs/matplotlib.ipynb),
but there are a few tips and tricks that are worth mentioning.


## Show

```
import numpy as np
import matplotlib as plt

x = np.array(range(20))
y = 3 + 0.5 * x + np.random.randn(20)
plt.plot(x, y)
```

In Python, sometimes, new figures won't display by default. Python waits until
you tell it to display those figures by using the ``.show()`` method in
``matplotlib.pyplot``. In most environments you should be able to either use
``plt.show()`` as many times as you want, or just at the end of the code, but if
you're running into problems where only the first graph displays then this can
be fixed by only using a single ``plt.show()`` at the end of your code.


## New Figures

``plt.figure()`` will start a new figure.


## Hold

* ``plt.hold(True)`` will set the figure to add new data rather than overwrite
* ``plt.hold(False)`` will set the figure to overwrite the existing data
* ``plt.hold()`` will switch back and forth, but this requires that you know
the current state so I prefer explictly using ``True`` and ``False``.

```
z = 2 + 0.75 * x + np.random.randn(20)
```

## Making Graphing Easier

Making nice looking graphs can sometimes take a lot of work. There are a couple
of modules that make this easier.

```
import pandas as pd
import seaborn as sns

data = pd.DataFrame(x, columns=["x"])
data["y"] = y

sns.lmplot('x', 'y', data)
plt.show()
```

[ggplot for Python](https://github.com/yhat/ggplot)
