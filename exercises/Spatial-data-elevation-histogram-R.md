---
layout: exercise
topic: Spatial Data
title: Species Occurrences Elevation Histogram
language: R
---

A colleague of yours is working on a project on deer mice ([*Peromyscus maniculatus*](http://animaldiversity.org/accounts/Peromyscus_maniculatus/)) and is interested in what elevations these mice tend to occupy in the continental United States. You offer to help them out by getting some coordinates for specimens of this species and looking up the elevation of these coordinates. 

1. Get deer mouse occurrences from GBIF, the [Global Biodiversity Information Facility](https://www.gbif.org/), using the `spocc` R package, which is designed to retrieve species occurrence data from various openly available data resources. Use the following code to do so: 

	```
	mouse_df = occ(query = "Peromyscus maniculatus", 
					from = "gbif")
	mouse_df = data.frame(mouse_df$gbif$data)
	```

2. With `dplyr`, rename the second and third columns of this dataset to `longitude` and `latitude`, and include only those specimens with a `basisOfRecord` that is `PRESERVED_SPECIMEN`. 

3. The `raster` package comes with some datasets, including one of global elevations, that can be retrieved with the `getData` function as follows: 

	```
	elevation = getData("alt", country = "US")
	elevation = elevation[[1]]
	```

4. Turn the occurrences dataframe into a spatial dataframe, making sure that its projection matches that of the elevation dataset. 

5. Extract the elevation values for all of the deer mouse occurrences and plot a histogram of them. 
