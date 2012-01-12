#!/bin/bash

set -x

for f in `cat instances`
do
	dat=dev.$f.comp.tag
	score=dev.$f.match.scores
	echo "Exact match" > $score
	python word_match.py $dat >> $score
	echo "Head match" >> $score
	python head_match.py $dat >> $score
	echo "Tail match" >> $score
	./tail_match.sh $dat >> $score
done

set +x
