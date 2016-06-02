# For Loops

## Basic for loops

* Let us do the same thing for a number of different values

```
for item in list_of_items:
    commands
```

```
pets = ['spot', 'gigantor', 'fluffy']
for pet in pets:
    print "%s is the name of a class pet" % pet
```

## Lists

* lists hold multiple values of any type
* have methods to let us manipulate them
  * e.g., insert, append
* these methods return None, different from string methods

## Using loops with append

* a common thing to do with a loop is to do some calculations and store the
  resulting value
* the simplest way to do this is using a list and `.append()`

```
results = []
for name in pets:
    capitalized_name = name.upper()
	results.append(capitalized_name)
print results
```

* a common mistake is to forget that list methods work "in-place"

```
results = []
for name in pets:
    capitalized_name = name.upper()
	results = results.append(capitalized_name)
print results
```
