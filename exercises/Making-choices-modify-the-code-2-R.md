---
layout: exercise
topic: Making Choices
title: Modify the Code 2
language: R
---

The following function is intended to check if two geographic points are close
to one another. If they are it should return `TRUE`. If they aren't, it should
return `FALSE`. Two points are considered near to each other if the absolute
value of the difference in their latitudes is less than one and the absolute
value of the difference in their longitudes is less than one.

1. Fill in the `_________` in the function to make it work.

   ``` 
   near <- function(lat1, long1, lat2, long2){
       # Check if two geographic points are near each other 
       if ((abs(lat1 - lat2) < 1) & (_________){
           near <- TRUE
       } else {
           near <- _________
       }
       return(near)
   }
   ```

2. Improve the documentation for the function so that it is clear what near
   means and what output the user should expect.
3. Check if Point 1 (latitude = 29.65, longitude = -82.33) is near 
   Point 2 (latitude = 41.74, longitude = -111.83).
4. Check if Point 1 (latitude = 29.65, longitude = -82.33) is near 
   Point 2 (latitude = 30.5, longitude = -82.8).
5. Create a new version of the function that improves it by allowing the user to
   pass in a parameter that sets what "near" means. To avoid changing the
   existing behavior of the function (since some of your lab mates are using it
   already) give the parameter a default value of 1.
6. Improve the documentation for the new function so that it reflects this new
   behavior
7. Check if Point 1 (latitude = 48.86, longitude = 2.35) is near
   Point 2 (latitude = 41.89, longitude = 2.5), when near is set to 7.
