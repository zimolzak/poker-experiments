hand_ranks.txt :
	python poker-stats.py > hand_ranks.txt

clean :
	rm -f hand_ranks.txt

