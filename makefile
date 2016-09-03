all : hand_ranks.txt progression.csv freq_of_nut.csv aavjqs.csv ringwinners.csv
	Rscript makeplot.R > percentages.txt
	perl -pi -e 's/\n/\r\n/g' percentages.txt

ringwinners.csv :
	echo 'cards,winhand,wl,n,i' > headers.csv
	python ring_game.py > temp1.csv &
	sleep 0.5
	python ring_game.py > temp2.csv &
	sleep 0.5
	python ring_game.py > temp3.csv &
	sleep 0.5
	python ring_game.py > temp4.csv
	sleep 2
	cat headers.csv temp*.csv > ringwinners.csv
	rm -f headers.csv temp*.csv

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

clean : cleanhard cleaneasy

cleanhard :
	rm -f aavjqs.csv

cleaneasy : 
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
	rm -f percentages.txt
	rm -f progression.csv
	rm -f freq_of_nut.csv
	rm -f ringwinners.csv
