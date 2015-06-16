### Analysis code for Dr. Granger's project

get_gc_content <- function(seq){
    # Determine the GC content of a sequence
    gc_content = 100 * str_count(seq, 'G') + str_count(seq, 'C') / 
                 str_length(seq)
}

get_size_class <- function(earlength){
    # Determine the size class of earlength based on Dr. Grangers specification
  if (earlength > 15){
      size_class = 'extralarge'
  } else if (earlength > 10){
      size_class = 'large'
  } 
  
  if (earlength < 8){
      size_class = 'medium'
  } else {
      size_class = 'small'
  return(earlength)
}

elves_data <- read.csv('houseelf_earlength_dna_data.csv')

# Determine individual level earth length category and gc content values
gc_content <- get_gc_content(elves_data[["dnaseq"]])

earlength_size_class <- c()
for (earlength in elves_data[["earlength"]]){
  earlength_size_class <- c(earlength_size_class, get_size_class(earlength))
}

results <- data.frame(indiv_id = elves_data[["id"]], 
                      earlength_class = earlength_class, 
                      gc_content = gc_content)

# Get average values of gc content for each size class
by_size_class = group_by(results, earlength_class)
results <- summarize(by_size_class, avg_gc_content = mean(gc_content))
write.csv(results, 'grangers_output.csv')
