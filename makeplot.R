library(ggplot2)
X = read.delim('~/Desktop/poker-stats/hand_ranks.txt', header=FALSE)
qplot(x=V1, fill=V2, data=X)
table(X$V2) / length(X$V2) * 100
