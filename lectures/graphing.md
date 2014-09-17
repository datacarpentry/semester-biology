---
layout: lecture
title: Graphing in Python
---

# Graphing

Most of the necessary information for learning how to make basic plots in Python
is in the [IPython notebook](http://nbviewer.ipython.org/urls/github.com/weecology/progbio/raw/master/ipynbs/matplotlib.ipynb),
but there are a few tips and tricks that are worth mentioning.


## Show

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
