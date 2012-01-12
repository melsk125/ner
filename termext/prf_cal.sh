#!/bin/bash

cut -f 2-3 $1 | sed 's|[BI]|W|g' > $1.tmp

match=`grep -c '^W	W$' $1.tmp`
ref=`grep -c '^W' $1.tmp`
model=`grep -c 'W$' $1.tmp`
wprec=`echo "scale=4; $match.0/$model.0" | bc`
wrec=`echo "scale=4; $match.0/$ref.0" | bc`

echo "W	0$wprec	0$wrec	`echo \"scale=5; ($wprec+$wrec)/2\" | bc`"

match=`grep -c '^O	O$' $1.tmp`
model=`grep -c '^O' $1.tmp`
ref=`grep -c 'O$' $1.tmp`
oprec=`echo "scale=4; $match.0/$model.0" | bc`
orec=`echo "scale=4; $match.0/$ref.0" | bc`

echo "O	0$oprec	0$orec	`echo \"scale=5; ($oprec+$orec)/2\" | bc`"

aprec=`echo "scale=5; ($wprec+$oprec)/2" | bc`
arec=`echo "scale=5; ($wrec+$orec)/2" | bc`
echo "a	0$aprec	0$arec	`echo \"scale=5; ($aprec+$arec)/2\" | bc`"

rm $1.tmp
