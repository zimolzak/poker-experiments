library(ggplot2)
X = read.delim('~/Desktop/poker-stats/hand_ranks.txt', header=FALSE)
qplot(x=V1, fill=V2, data=X) + labs(x = "Hand rank", fill = "Hand type")
table(X$V2) / length(X$V2) * 100
