library(dplyr)
library(ggplot2)
library(raster)
library(rdataretriever)
library(DBI)

if (!file.exists('bbs.sqlite')){
  rdataretriever::get_updates()
  rdataretriever::install('breed-bird-survey', 'sqlite', 'bbs.sqlite')
}

bbs_db <- dbConnect(RSQLite::SQLite(), 'bbs.sqlite')
surveys <- tbl(bbs_db, "breed_bird_survey_counts")
sites <- tbl(bbs_db, "breed_bird_survey_routes") %>%
  data.frame()

rich_data <- surveys %>%
  filter(year == 2015) %>%
  group_by(statenum, route) %>%
  summarize(richness = n()) %>%
  collect()

bioclim <- getData('worldclim', var = 'bio', res = 10)
sites_spatial <- SpatialPointsDataFrame(sites[c('longitude', 'latitude')], sites)
plot(bioclim$bio12)
plot(sites_spatial, add = TRUE)

bioclim_bbs <- extract(bioclim, sites_spatial) %>%
  cbind(sites)
richness_w_env <- inner_join(rich_data, bioclim_bbs)

ggplot(richness_w_env, aes(x = bio12, y = richness)) +
  geom_point() +
  geom_smooth() +
  facet_wrap(~statenum, scales = 'free')
