---
layout: exercise
topic: Spatial Data
title: Species Occurrences Map
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
