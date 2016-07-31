library(ggplot2)
X = read.delim('~/Desktop/poker-stats/hand_ranks.txt', header=FALSE)
qplot(X$V1)
