#!/bin/bash

echo "Start train (local tag)"

echo "-c"
python makecrf.py -c train.t5.out train.crf.out > train.lc.crf

echo "-cp"
python makecrf.py -cp train.t5.out train.crf.out > train.lcp.crf

echo "-p"
python makecrf.py -p train.t5.out train.crf.out > train.lp.crf

echo "-cj"
python makecrf.py -cj train.t5.out train.crf.out > train.lcj.crf

echo "-cpj"
python makecrf.py -cpj train.t5.out train.crf.out > train.lcpj.crf

echo "-pj"
python makecrf.py -pj train.t5.out train.crf.out > train.lpj.crf

