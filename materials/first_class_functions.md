---
layout: page
title: First Class Functions
---

* Functions aren't special they can be
  * assigned to variables
  * added to lists
  * passed to other functions

```
def area(radius):
    area = 3.14159 * radius ** 2
	return area

print area(1)
a = area
print a(1)

def diameter(radius):
    return radius * 2

functions = [area, diameter]

for function in functions:
    print function(2)
```

```
def do_all(func, values):
    result = []
	for value in values:
	    temp = func(value)
		result.append(temp)
	return result

values = [1, 2, 3]
print do_all(radius)
print do_all(diameter)
```

In fact, there's actually a built-in Python function that does this: `map()`.
