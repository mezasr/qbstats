library(dplyr)  # load dplyr package for data wrangling

# read csv file containing stats
print("Loading up Tom Brady's stats...")
tbrady <- read.csv(file="qb/tbrady.csv",header=T,sep=",")

# sort total yards by age
print("Sorting Yards by Age/Year...")
yards <- tbrady %>% group_by(Age) %>% filter(GS>=10) %>% select(Age,Year,Yds)
print(yards)