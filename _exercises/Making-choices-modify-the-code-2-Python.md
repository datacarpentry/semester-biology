---
layout: exercise
topic: Making Choices
title: Modify the Code 2
language: Python
---

The following function is intended to check if two geographic points are close
to one another. If they are it should return `True`. If they aren't, it should
return `False`. Two points are considered near to each other if the absolute
value of the difference in their latitudes is less than one and the absolute
value of the difference in their longitudes is less than one. 

Fill in the `_________` in the function to make it work and then use it to check 
if the following pairs of points are near or not and print out the answers.
   
```
def near(lat1, long1, lat2, long2):
    """Check if two geographic points are near each other""" 
    if (abs(lat1 - lat2) < 1) and (_________):
        near = True
    else:
        near = _________
    return near
```

1. Point 1: latitude = 29.65, longitude = -82.33. Point 2: latitude = 41.74,
   longitude = -111.83.
2. Point 1: latitude = 29.65, longitude = -82.33. Point 2: latitude = 30.5,
   longitude = -82.8.
3. Point 1: latitude = 48.86, longitude = 2.35. Point 2: latitude = 41.89,
   longitude = 2.5.
