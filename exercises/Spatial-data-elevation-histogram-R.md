---
layout: exercise
topic: Spatial Data
title: Species Occurrences Elevation Histogram
language: R
---

A colleague of yours is working on a project on banner-tailed kangaroo rats ([*Dipodomys spectabilis*](https://animaldiversity.org/accounts/Dipodomys_spectabilis/)) and is interested in what elevations these mice tend to occupy in the continental United States. You offer to help them out by getting some coordinates for specimens of this species and looking up the elevation of these coordinates. 

1. Get banner-tailed kangaroo rat occurrences from GBIF, the [Global Biodiversity Information Facility](https://www.gbif.org/), using the `spocc` R package, which is designed to retrieve species occurrence data from various openly available data resources. Use the following code to do so: 

	```
	dipo_df = occ(query = "Dipodomys spectabilis", 
				from = "gbif",
				limit = 1000,
				has_coords = TRUE)
	dipo_df = data.frame(dipo_df$gbif$data)
	```

2. Clean up the data by:
	* Using the `rename` function from `dplyr` to rename the second and third columns of this dataset to `longitude` and `latitude`
	* Filter the data to only include those specimens with `Dipodomys_spectabilis.basisOfRecord` that is `PRESERVED_SPECIMEN` and a `Dipodomys_spectabilis.countryCode` that is `US`
	* Remove points with values of `0` for `latitude` or `longitude`
	* Remove all of the columns from the dataset except `latitude` and `longitude` using `select`
	* Use `head()` function to show the top few rows of this cleaned dataset

3. Do the following to display the locations of these points on a map of the United States:
	* Get data for a US map using `usmap = map_data("usa")`
	* Plot it using `geom_polygon`. In the aesthetic use `group = group` to avoid weird lines cross your graph. Use `fill = "white"` and `color = "black"`.
	* Plot the kangaroo rat locations
	* Use `coord_quickmap()` to automatically use a reasonable spatial projection


4. The `raster` package comes with some datasets, including one of global elevations, that can be retrieved with the `getData` function as follows: 

	```
	elevation = getData("alt", country = "US")
	elevation = elevation[[1]]
	```

	Create a new version of the graph from Part 3 that shows the elevation data as well. Plotting the elevation data may take a while because there are a lot of data points in the dataset. Pay attention to the order that the `geom_` objects are plotted in. The name of the elevation variable is `USA1_msk_alt`.

5. Turn the `dipo_df` dataframe into a `SpatialPointsDataframe`, making sure that its projection matches that of the elevation dataset, and extract the elevation values for all of the kangaroo rat occurrences. Turn this subset of elevation values into a dataframe and plot a histogram of the elevations. 

6. Part 5 showed us what the elevations where banner-tailed kangaroo rats occur, but without context it's hard to tell how important elevation is. Make a new graph that shows histograms for all elevations in the US in gray and the kangaroo rat elevations in red. Plot the kangaroo elevations on top of the full elevations and make them transparent so that you can see the overlap. To get the histograms on the same scale we need to plot the density of points instead of the total number of points. This can be done in `ggplot` using code like:

    ```
	ggplot() +
      geom_histogram(data = elevations, aes(x = USA1_msk_alt, y = ..density..))
	```
