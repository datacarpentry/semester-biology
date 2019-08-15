---
layout: page
element: notes
title: First Day Demo
---

* Quickly show some of the sorts of things we'll be able to do by the end of the
  course
* Use data from the Breeding Bird Survey of North America
* Continental scale community science project where thousands of birders count
  birds at locations across North America
* Look at how the number of species at a site responsds to environmental factors
* We only have a few minutes, so I'm going to move quickly and use tools you
  won't have installed yet, so this is the one day of the course where I won't
  encourage you to code along with me.
* The goal today isn't to understand everything, it's to see where we're going.

### Demo

* First we need to load some packages to leverage code that others have written
  to make our lives easier

```
library(dplyr)
library(ggplot2)
library(raster)
library(rdataretriever)
library(DBI)
```

* Now let's download the BBS data and install it in a database
* This data is distributed as ~100 different files that need to be combined in
  various ways
* It's also pretty large, making a database a good option 

```
  rdataretriever::get_updates()
  rdataretriever::install('breed-bird-survey', 'sqlite', 'bbs.sqlite')
```

* This takes a little time
* So instead of installing it every time we run our code let's check to see if
  the database we just created exists, and only do this step if it isn't there
  already

```
if (!file.exists('bbs.sqlite')){
  rdataretriever::get_updates()
  rdataretriever::install('breed-bird-survey', 'sqlite', 'bbs.sqlite')
}
```

* If we rerun the code we see that it doesn't rerun this step

* Now let's connect from R to the database

```
bbs_db <- dbConnect(RSQLite::SQLite(), 'bbs.sqlite')
```

* Once we've done this we can use tables in the database in R

```
surveys <- tbl(bbs_db, "breed_bird_survey_counts")
sites <- tbl(bbs_db, "breed_bird_survey_routes") %>%
  data.frame()
```

* *Show tables*
* Surveys: data on how many individuals of each species are sampled at each site
* Sites: information on where each site is

* First, let's convert the surveys data into numbers of species at each site

```
rich_data <- surveys %>%
  filter(year == 2015) %>%
  group_by(statenum, route) %>%
  summarize(richness = n()) %>%
  collect()
```

* Second, we need to get environmental data for each site

```
bioclim <- getData('worldclim', var = 'bio', res = 10)
sites_spatial <- SpatialPointsDataFrame(sites[c('longitude', 'latitude')], sites)
plot(bioclim$bio12)
```

* Let's see where our sites are located

```
plot(sites_spatial, add = TRUE)
```

* Extract environmental data for each site

```
bioclim_bbs <- extract(bioclim, sites_spatial) %>%
  cbind(sites)
```

* Combine this data with our species richness data

```
richness_w_env <- inner_join(rich_data, bioclim_bbs)
```

* Now let's see how richness relates to the precipitation
* Annual precipition is stored in `bio12`

```
ggplot(richness_w_env, aes(x = bio12, y = richness)) +
  geom_point()
```

* It looks like there's a pattern here, so let's fit a model through it

```
ggplot(richness_w_env, aes(x = bio12, y = richness)) +
  geom_point() +
  geom_smooth()
```

* Low bird richess in really dry areas, peak at intermediate precips, drop at
  really high precips
* Maybe we want to use this kind of information to inform conservation decisions at the state level, in which case we'd want to understand these patterns within each state

```
ggplot(richness_w_env, aes(x = bio12, y = richness)) +
  geom_point() +
  geom_smooth() +
  facet_wrap(~statenum, scales = 'free')
```