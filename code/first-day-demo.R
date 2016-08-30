library(dplyr)
library(ggplot2)
library(raster)
library(ecoretriever)

if (!file.exists('bbs.sqlite')){
  ecoretriever::install('BBS', 'sqlite', 'bbs.sqlite')
}

bbs_db <- src_sqlite('bbs.sqlite')
surveys <- tbl(bbs_db, "bbs_counts")
sites <- tbl(bbs_db, "bbs_routes") %>%
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
  facet_wrap(~statenum)
