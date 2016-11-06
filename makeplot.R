library(ggplot2)
options(width = 190)

X = read.delim('~/Desktop/local/poker-experiments/most_common_hands.txt', header=FALSE)
qplot(x=V1, fill=V2, data=X) + labs(x = "Hand rank", fill = "Hand type")
cat("Freq of various hands in 5 random cards\n========\n")
cat('n= ')
cat(dim(X)[1])
cat('\n')
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
cat('n= ')
cat(dim(Y)[1])
cat('\n')
print(rowpct(t1))
cat('\n')

Z = read.csv('~/Desktop/local/poker-experiments/freq_of_nut.csv')
cat("Number of players, by theoretical nut hand, by actual best on flop\n========\n\n")
cat('n= ')
cat(dim(Z)[1])
cat('(divided by [2, 3, 4, 5, 6])')
cat('\n')
for (n in 2:max(Z$num_players)){
    d = Z[Z$num_players == n, ]
    cat(n, 'players\n----\n')
    print(rowpct(table(d$nut_hand, d$flop_leader)))
    cat('\n')
}

T = read.csv('~/Desktop/local/poker-experiments/aavjqs.csv')
qplot(data = T[T$villain=='jqs',], x=stage, y=pct, color=as.factor(iter)) + geom_line() + labs(title='AA vs JQ suited', color='Iteration')
qplot(data = T[T$villain=='aks',], x=stage, y=pct, color=as.factor(iter)) + geom_line() + labs(title='AA vs AK suited', color='Iteration')
qplot(data = T[T$villain=='kqs',], x=stage, y=pct, color=as.factor(iter)) + geom_line() + labs(title='AA vs KQ suited', color='Iteration')
qplot(data = T[T$villain=='AKo v 77',], x=stage, y=pct, color=as.factor(iter)) + geom_line() + labs(title='AKo vs 77', color='Iteration')

cat("Winning cards/hand if all 9 players show down\n========\n\n")
R = read.csv('~/Desktop/local/poker-experiments/best_hole_cards.csv')
options(width = 100)
options(scipen=999)
cat('n= ')
cat(dim(R)[1] / 9)
cat('\n')
winvec = table(R$cards, R$wl)[,'w']
lossvec = table(R$cards, R$wl)[,'l']
round(sort(winvec / (winvec + lossvec) * 100, decreasing=TRUE), digits=2)
sort(table(R$winhand), decreasing=TRUE) / dim(R)[1] * 100
