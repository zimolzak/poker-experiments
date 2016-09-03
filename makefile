all : hand_ranks.txt progression.csv freq_of_nut.csv aavjqs.csv
	Rscript makeplot.R > percentages.txt
	perl -pi -e 's/\n/\r\n/g' percentages.txt

hand_ranks.txt :
	python poker-stats.py > hand_ranks.txt

progression.csv :
	python flop_turn_river.py > progression.csv

freq_of_nut.csv :
	python theo_actual_nut.py > freq_of_nut.csv

aavjqs.csv :
	echo 'villain,iter,stage,pct' > aavjqs.csv
	python pct_vs_time.py >> aavjqs.csv &
	python pct_vs_time.py >> aavjqs.csv &
	python pct_vs_time.py >> aavjqs.csv &
	python pct_vs_time.py >> aavjqs.csv
	sleep 2

clean :
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
	rm -f percentages.txt
	rm -f progression.csv
	rm -f freq_of_nut.csv
	rm -f aavjqs.csv
