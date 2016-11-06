all : hand_ranks.txt progression.csv freq_of_nut.csv aavjqs.csv best_hole_cards.csv
	Rscript makeplot.R > percentages.txt
	perl -pi -e 's/\n/\r\n/g' percentages.txt

best_hole_cards.csv :
	echo 'cards,winhand,wl,n,i' > headers.csv
	python best_hole_cards.py > temp1.csv &
	sleep 0.5
	python best_hole_cards.py > temp2.csv &
	sleep 0.5
	python best_hole_cards.py > temp3.csv &
	sleep 0.5
	python best_hole_cards.py > temp4.csv
	sleep 2
	cat headers.csv temp*.csv > best_hole_cards.csv
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

clean : cleaneasy

cleanhard :
	rm -f aavjqs.csv

cleaneasy : 
	rm -f hand_ranks.txt
	rm -f Rplots.pdf
	rm -f percentages.txt
	rm -f progression.csv
	rm -f freq_of_nut.csv
	rm -f best_hole_cards.csv

backup :
	cp aavjqs.csv bak/
	cp hand_ranks.txt bak/
	cp Rplots.pdf bak/
	cp percentages.txt bak/
	cp progression.csv bak/
	cp freq_of_nut.csv bak/
	cp best_hole_cards.csv bak/
