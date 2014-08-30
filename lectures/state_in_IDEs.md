# State in Integrated Development Environments

In most integrated development environments (including Canopy) you can run code
in three different ways:

1. Typing code directly into the interpreter
2. Running sections of code from the editor
3. Running the entire file that is in the editor


## Typing code directly into the interpreter

When typing code directly into the interpreter any changes that code makes are
stored in the memory associated with the interpreter and can be accessed like we
would expect.

```
a = 26
print a
```


## Running sections of code from the editor

When we enter code into the editor we can run pieces of that code by
highlighting the code and using the `Run selected text` button, menu item, or
keyboard shortcut. In most IDEs this is equivalent to copying and pasting the
code into the interpreter, so it works just like typing the code in
directly. So, running

`print a`

this way after creating `a` in the interpreter works.


## Running the full file from the editor

We can also run all of the code in the editor by using the `Run current file`
button, menu item, or keyboard shortcut. In most IDEs this will run the file
separately from anything that has previously been entered into the
interpreter. It will do this by either restarting the interpreter so that it
contains nothing, or by running the file in a separate instance and then adding
the resulting variables to those in the interpreter.

This means that running code this way pays no attention to the state of the
interpreter before you run the code, so if we create `a` in the interpreter and
then run a file that contains

`print a`

We will see an error telling us that `a` doesn't exist.

This is a good thing because this way we know that our code is self-contained
and doesn't just happen to work because of something we had done earlier in the
day.


## Restarting the interpreter

If you want to get rid of everything that is stored in the interpreter there is
typically a menu item and/or keyboard shortcut to restart the interpreter.


## How should I develop my code

Typing code into the interpreter or running sections of code from the editor is
useful for helping to figure out how to accomplish bigger tasks and for
understanding bugs when things aren't working properly.

Once you think you have solved a problem you should always check that you've
really solved it by running the entire file.
