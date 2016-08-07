all : hand_ranks.txt progression.csv
	Rscript makeplot.R > percentages.txt

hand_ranks.txt :
	python poker-stats.py > hand_ranks.txt

progression.csv :
	python flop_turn_river.py > progression.csv

clean :
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
	rm -f percentages.txt
	rm -f progression.csv
