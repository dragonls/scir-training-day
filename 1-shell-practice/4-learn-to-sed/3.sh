#!/bin/bash
# 批量去拓展名.raw
for i in `ls` ; do
	echo $i > 3.tmp;
	for j in `sed -n "s/\.raw$//gp" 3.tmp`; do
		mv $i $j;
	done;
done;
rm 3.tmp
