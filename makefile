all : most_common_hands.txt evolution_of_nut.csv freq_of_nut.csv aavjqs.csv best_hole_cards.csv
	Rscript makeplot.R > output.txt
	perl -pi -e 's/\n/\r\n/g' output.txt

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

most_common_hands.txt :
	python most_common_hands.py > most_common_hands.txt

evolution_of_nut.csv :
	python evolution_of_nut.py > evolution_of_nut.csv

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
	rm -f most_common_hands.txt
	rm -f Rplots.pdf
	rm -f output.txt
	rm -f evolution_of_nut.csv
	rm -f freq_of_nut.csv
	rm -f best_hole_cards.csv

backup :
	cp aavjqs.csv bak/
	cp most_common_hands.txt bak/
	cp Rplots.pdf bak/
	cp output.txt bak/
	cp evolution_of_nut.csv bak/
	cp freq_of_nut.csv bak/
	cp best_hole_cards.csv bak/
