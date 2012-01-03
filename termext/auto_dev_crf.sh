#!/bin/bash

echo "Start dev (local tag)"

echo "-c"
python makecrf.py -c dev.t5.out dev.crf.out > dev.lc.crf

echo "-cp"
python makecrf.py -cp dev.t5.out dev.crf.out > dev.lcp.crf

echo "-p"
python makecrf.py -p dev.t5.out dev.crf.out > dev.lp.crf

echo "-cj"
python makecrf.py -cj dev.t5.out dev.crf.out > dev.lcj.crf

echo "-cpj"
python makecrf.py -cpj dev.t5.out dev.crf.out > dev.lcpj.crf

echo "-pj"
python makecrf.py -pj dev.t5.out dev.crf.out > dev.lpj.crf

