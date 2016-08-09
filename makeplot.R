library(ggplot2)
options(width = 190)

X = read.delim('~/Desktop/local/poker-experiments/hand_ranks.txt', header=FALSE)
qplot(x=V1, fill=V2, data=X) + labs(x = "Hand rank", fill = "Hand type")
cat("Freq of various hands in 5 random cards\n========\n")
table(X$V2) / length(X$V2) * 100
cat('\n')

rowpct = function(t1){
    t2 = t1
    for (i in 1:dim(t1)[1]){
        for (j in 1:dim(t1)[2]){
            t2[i,j] = round(t1[i,j] / sum(t1[i,]) * 100, 1)
        }
    }
    return(t2)
}

Y = read.csv('~/Desktop/local/poker-experiments/progression.csv')
t1 = table(Y$flop, Y$river)
cat("Nuts on flop becomes what nut on river?\n========\n")
print(rowpct(t1))
cat('\n')

Z = read.csv('~/Desktop/local/poker-experiments/freq_of_nut.csv')
cat("Number of players, by theoretical nut hand, by actual best on flop\n========\n\n")
for (n in 2:max(Z$num_players)){
    d = Z[Z$num_players == n, ]
    cat(n, 'players\n----\n')
    print(rowpct(table(d$nut_hand, d$flop_leader)))
    cat('\n')
}
