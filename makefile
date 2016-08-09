all : hand_ranks.txt progression.csv freq_of_nut.csv
	Rscript makeplot.R > percentages.txt

hand_ranks.txt :
	python poker-stats.py > hand_ranks.txt

progression.csv :
	python flop_turn_river.py > progression.csv

freq_of_nut.csv :
	python theo_actual_nut.py > freq_of_nut.csv

clean :
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
	rm -f percentages.txt
	rm -f progression.csv
	rm -f freq_of_nut.csv
