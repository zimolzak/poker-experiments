all : most_common_hands.txt evolution_of_nut.csv theo_actual_nut.csv pct_vs_time.csv best_hole_cards.csv tournament tournament.png
	Rscript analyses.R > output.txt
	perl -pi -e 's/\n/\r\n/g' output.txt

best_hole_cards.csv :
	echo 'cards,winhand,wl,n,i' > headers.csv
	python2.7 x_best_hole_cards.py > temp1.csv &
	sleep 0.5
	python2.7 x_best_hole_cards.py > temp2.csv &
	sleep 0.5
	python2.7 x_best_hole_cards.py > temp3.csv &
	sleep 0.5
	python2.7 x_best_hole_cards.py > temp4.csv
	sleep 2
	cat headers.csv temp*.csv > best_hole_cards.csv
	rm -f headers.csv temp*.csv

most_common_hands.txt :
	python2.7 x_most_common_hands.py > most_common_hands.txt

evolution_of_nut.csv :
	python2.7 x_evolution_of_nut.py > evolution_of_nut.csv

theo_actual_nut.csv :
	python2.7 x_theo_actual_nut.py > theo_actual_nut.csv

pct_vs_time.csv :
	echo 'villain,iter,stage,pct' > pct_vs_time.csv
	python2.7 x_pct_vs_time.py >> pct_vs_time.csv &
	python2.7 x_pct_vs_time.py >> pct_vs_time.csv &
	python2.7 x_pct_vs_time.py >> pct_vs_time.csv &
	python2.7 x_pct_vs_time.py >> pct_vs_time.csv
	sleep 2

tournament :
	python2.7 x_tournament.py 1 4 > t14.txt &
	python2.7 x_tournament.py 2 4 > t24.txt &
	python2.7 x_tournament.py 3 4 > t34.txt &
	python2.7 x_tournament.py 4 4 > t44.txt &

tournament.png : t14.txt t24.txt t34.txt t44.txt
	cat t14.txt t24.txt t34.txt t44.txt > cattd.txt
	python2.7 x_filt.py  > filtered.txt
	sort filtered.txt | uniq > uniq.txt
	echo 'digraph {' > tournament.dot
	cat uniq.txt >> tournament.dot
	echo '}' >> tournament.dot
	dot -Tpng tournament.dot > tournament.png
	cp tournament.png ~/Dropbox/poker_graph

clean :
	rm -f most_common_hands.txt
	rm -f evolution_of_nut.csv
	rm -f theo_actual_nut.csv
	rm -f best_hole_cards.csv
	rm -f cattd.txt filtered.txt tournament.dot tournament.png

cleanoutputs :
	rm -f Rplots.pdf
	rm -f output.txt

cleanhard :
	rm -f pct_vs_time.csv
	rm -f t14.txt t24.txt t34.txt t44.txt

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
	python2.7 omaha_nuts_quiz.py --test
	python2.7 outs_odds_quiz.py --test
	python3 fun_with_outs_odds.py

manytest : test
	python2.7 one_time_eval.py 3c4ckdqd 4d9s7d > /dev/null
	python2.7 one_time_eval.py 3c4ckdqh 4h9s7d > /dev/null
	python2.7 one_time_eval.py 4s4ckdqh ac9s7d > /dev/null
	python2.7 one_time_eval.py 6s7s15p > /dev/null
	python2.7 one_time_eval.py 6s7s15p 2s3s4d > /dev/null
	python2.7 one_time_eval.py 6s7s15p 8s9s4d > /dev/null
	python2.7 one_time_eval.py 6s7s5p 2s3s4d > /dev/null
	python2.7 one_time_eval.py 9h9d10p > /dev/null
	python2.7 one_time_eval.py 9h9d15p > /dev/null
	python2.7 one_time_eval.py 9h9d15p  > /dev/null
	python2.7 one_time_eval.py 9h9d15p asac3h > /dev/null
	python2.7 one_time_eval.py 9h9d15p asackc > /dev/null
	python2.7 one_time_eval.py 9h9d1p  > /dev/null
	python2.7 one_time_eval.py 9h9d28p > /dev/null
	python2.7 one_time_eval.py 9h9d2p > /dev/null
	python2.7 one_time_eval.py 9h9d4p > /dev/null
	python2.7 one_time_eval.py 9h9d6p > /dev/null
	python2.7 one_time_eval.py 9h9d7p > /dev/null
	python2.7 one_time_eval.py 9h9d80p > /dev/null
	python2.7 one_time_eval.py 9h9dahad asackc > /dev/null
	python2.7 one_time_eval.py 9h9dkskc  > /dev/null
	python2.7 one_time_eval.py ahac100p 3c9s7h > /dev/null
	python2.7 one_time_eval.py ahac40p 3c9s7h > /dev/null
	python2.7 one_time_eval.py as4ckdqh  > /dev/null
	python2.7 one_time_eval.py as4ckdqh 4h9s7d > /dev/null
	python2.7 one_time_eval.py asjd10p 3c9sjh > /dev/null
	python2.7 one_time_eval.py asjd10p 3c9sjhac > /dev/null
	python2.7 one_time_eval.py asjs10p 3c9sjh2s > /dev/null
	python2.7 one_time_eval.py asjs10p 3s9sjh2s > /dev/null
	python2.7 one_time_eval.py askd15p > /dev/null
	python2.7 one_time_eval.py askd4s4d > /dev/null
	python2.7 one_time_eval.py askd15p > /dev/null
	python2.7 one_time_eval.py asks15p > /dev/null
	python2.7 one_time_eval.py ksac11p > /dev/null
	python2.7 one_time_eval.py ksac28p > /dev/null
	python2.7 one_time_eval.py qsjd100p 3c9s7h > /dev/null
	python2.7 one_time_eval.py qsjd10p 3c9sjh > /dev/null
	python2.7 one_time_eval.py qsjd15p 3c9s7h > /dev/null
	python2.7 one_time_eval.py qsjd40p 3c9s7h > /dev/null
	python2.7 one_time_eval.py qsjd40p 3c9sjh > /dev/null
