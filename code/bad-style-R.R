func1<-function(sub_list, total_list) {
# calculates percent value of a group of interest. first vector arg is the group of interest, the second is the total population.
fraction<-sum(sub_list)/sum(total_list)
percent<-round(fraction,3)*100
return(percent)
}
trees<-read.csv("http://www.esapubs.org/archive/ecol/E090/251/datafiles/swamp_all_modern.txt", sep = '\t')
species<-read.csv("http://www.esapubs.org/archive/ecol/E090/251/datafiles/species_codes.txt", sep = '\t')
library(dplyr)
trees<-mutate(trees, Mass = 0.124*DBH**2.53)
trees_grouped<-group_by(trees, Year, Plot, Species)
tree_summary<-summarize(trees_grouped, col_1 = n(), col_2 = round(mean(DBH),2), col_3 = round(sum(Mass),0))
species_rank<-data.frame(year=c(), sp_code=c(), percent_ind=c(), percent_mass=c())
for (year in unique(tree_summary$Year)) { target_year <- filter(tree_summary, Year == year)
for (sp_code in unique(tree_summary$Species)) {
spp<-filter( target_year, Species==sp_code )
percent_ind<-func1( spp$col_1, target_year$col_1 )
percent_mass<-func1( spp$col_3, target_year$col_3 )
species_rank<-rbind( species_rank, data.frame(year, sp_code, percent_ind, percent_mass) )
}
}
species_rank <- left_join(species_rank, species, by = c("sp_code" = "SPCODE"))
library(ggplot2)
ggplot(species_rank, aes(x = percent_ind, y = percent_mass)) +
geom_point(aes(color = factor(SPECIES))) +
facet_grid(. ~ year) +
labs(x = "Percent Individuals", y = "Percent Mass", color = "Species")