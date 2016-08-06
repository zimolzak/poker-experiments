library(ggplot2)
X = read.delim('~/Desktop/local/poker-stats/hand_ranks.txt', header=FALSE)
qplot(x=V1, fill=V2, data=X) + labs(x = "Hand rank", fill = "Hand type")
table(X$V2) / length(X$V2) * 100

Y = read.csv('~/Desktop/local/poker-stats/progression.csv')
t1 = table(Y$flop, Y$river)
t2 = t1
for (i in 1:dim(t1)[1]){
    for (j in 1:dim(t1)[2]){
    	t2[i,j] = round(t1[i,j] / sum(t1[i,]) * 100, 2)
    }
}

print(t1)
print(t2)
