#!/bin/bash

set -x

cut -f 2 $1 |
	python de_newline.py |
	sed 's|B\(I*\)|\1B|g' |
	rev |
	python do_newline.py > $1.gold

cut -f 3 $1 |
	python de_newline.py |
	sed 's|B\(I*\)|\1B|g' |
	rev |
	python do_newline.py > $1.tag

paste $1.gold $1.gold $1.tag > $1.rev

python head_match.py $1.rev

rm $1.gold $1.tag $1.rev

set +x
