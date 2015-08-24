# Analysis of mass and litter size in mammals

library(ggplot2)
library(dplyr)

url = "http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt"
data = read.csv(url, sep = "\t")
qplot(x = mass.g., y = litter.size, data = data, log = "xy")

data_by_family <- group_by(data, family)
n_by_family <- summarize(data_by_family, n_species = length(species))
high_n_families <- filter(n_by_family, n_species > 25)
plot_data <- semi_join(data_by_family, high_n_families)

qplot(x = mass.g., y = litter.size, data = plot_data, log = "xy",
      geom = c("point", "smooth"), method = "lm") + facet_wrap(~ family, ncol = 3)
