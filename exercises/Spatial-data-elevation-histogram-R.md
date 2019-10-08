---
layout: exercise
topic: Spatial Data
title: Species Occurrences Elevation Histogram
language: R
---

This is a follow up to [Species Occurrences Map]({{ site.baseurl }}/exercises/Spatial-data-map-R).

Now that you've mapped some species occurrence data you want to understand how
environmental factors influnece the species distribution.


1. The `raster` package comes with some datasets, including one of global elevations, that can be retrieved with the `getData` function as follows: 

	```
	elevation = getData("alt", country = "US")
	elevation = elevation[[1]]
	```

    Create a new version of the map from [Species Occurrences
   Map]({{site.baseurl }}/exercises/Spatial-data-map-R) that shows the elevation
   data as well. Plotting the elevation data may take a while because there are
   a lot of data points in the dataset. Pay attention to the order that the
   `geom_` objects are plotted in. The name of the elevation variable is
   `USA1_msk_alt`. *If the website is down you can download a copy from the
   course site by downloading
   <http://www.datacarpentry.org/semester-biology/data/wc10.zip> and unzipping
   it into your home directory (`/home/username` on Mac and Linux,
   `C:\Users\username\Documents` on Windows) and using the command
   `elevation = getData("alt", country = "US", path = ".")`*

2. Turn the `dipo_df` dataframe from [Species Occurrences Map]({{ site.baseurl }}/exercises/Spatial-data-map-R) into a `SpatialPointsDataframe`, making sure that its projection matches that of the elevation dataset, and extract the elevation values for all of the kangaroo rat occurrences. Turn this subset of elevation values into a dataframe and plot a histogram of the elevations.

3. Part 2 showed us the elevations where banner-tailed kangaroo rats occur, but without context it's hard to tell how important elevation is. Make a new graph that shows histograms for all elevations in the US in gray and the kangaroo rat elevations in red. Plot the kangaroo elevations on top of the full elevations and make them transparent so that you can see the overlap. To get the histograms on the same scale we need to plot the density of points instead of the total number of points. This can be done in `ggplot` using code like:

    ```
	ggplot() +
      geom_histogram(data = elevations, aes(x = USA1_msk_alt, y = ..density..))
	```
Lable the x axis elevation and add the title "Kangaroorat habitat elevation relative to background".