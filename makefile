all : most_common_hands.txt evolution_of_nut.csv theo_actual_nut.csv pct_vs_time.csv best_hole_cards.csv
	Rscript analyses.R > output.txt
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

theo_actual_nut.csv :
	python theo_actual_nut.py > theo_actual_nut.csv

pct_vs_time.csv :
	echo 'villain,iter,stage,pct' > pct_vs_time.csv
	python pct_vs_time.py >> pct_vs_time.csv &
	python pct_vs_time.py >> pct_vs_time.csv &
	python pct_vs_time.py >> pct_vs_time.csv &
	python pct_vs_time.py >> pct_vs_time.csv
	sleep 2

clean :
	rm -f most_common_hands.txt
	rm -f evolution_of_nut.csv
	rm -f theo_actual_nut.csv
	rm -f best_hole_cards.csv

cleanoutputs :
	rm -f Rplots.pdf
	rm -f output.txt

cleanhard :
	rm -f pct_vs_time.csv

cleaneasy : clean cleanoutputs

cleanall : clean cleanoutputs cleanhard

backup :
	cp pct_vs_time.csv bak/
	cp most_common_hands.txt bak/
	cp Rplots.pdf bak/
	cp output.txt bak/
	cp evolution_of_nut.csv bak/
	cp theo_actual_nut.csv bak/
	cp best_hole_cards.csv bak/

test :
	python2.7 range.py 15
	python2.7 count_hands.py
	python2.7 one_time_eval.py as8sqdtc
# add other interactive ones here: omaha.py, python outs_odds_quiz.py,
# source outs_loop.sh
