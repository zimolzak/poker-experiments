all : hand_ranks.txt
	Rscript makeplot.R > percentages.txt

hand_ranks.txt :
	python poker-stats.py > hand_ranks.txt

clean :
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
