simulate_shake_of_the_magic_8_ball_and_get_answer <- function(shaketime=3, 
annotation=TRUE, answers_list=answers) { # This function simulates a shake of a Magic 8 Ball.
cat("Shaking... ")
Sys.sleep(shaketime/3)
cat("... ")
Sys.sleep(shaketime/3)
cat("Turning... ")
Sys.sleep(shaketime/3)
if(annotation==TRUE) {
cat(sub_function_1(sub_function_2(answers_list$full), answers_list))
} else {
cat(sub_function_2(answers_list$full))
}
}

library(stringr)
library(dplyr)
sub_function_1<-function(answer, answers_list=answers) { # Annotate
i <- select(answers_list %>% filter(full==answer), short)
if (i  ==  'Yes') {
new_answer<-paste(str_to_upper(answer),'!',sep='')
} else if (i  ==  'Maybe') {
new_answer <- paste(answer,'.',sep='')
} else if (i  ==  'No') {
new_answer<-paste(answer,'. ... :-(',sep ='')}
return(new_answer)
}

sub_function_2 <- function(answer_choices=answers$full) { #give it a vector of strings
ANS <- as.character(sample(answer_choices, 1))
return(ANS)
}

answers <- data.frame( 
full = c("It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",  "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"),
short = c("Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Maybe", "Maybe", "Maybe", "Maybe", "Maybe", "No", "No", "No", "No", "No")
)

positive_answers<-filter(answers,short=="Yes")# Rig the Magic_8 ball
simulate_shake_of_the_magic_8_ball_and_get_answer(answers_list=positive_answers)

### For Real
simulate_shake_of_the_magic_8_ball_and_get_answer()
