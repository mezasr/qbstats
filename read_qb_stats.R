library(dplyr)  # load dplyr package for data wrangling

# read csv file containing stats
tbrady <- read.csv(file="qb/tbrady.csv",header=T,sep=",")

print("Tom Brady stats loaded!")