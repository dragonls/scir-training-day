#!/bin/sh
# 统计"2.dat"文件中的不包含".txt"的行的行数并输出
n=`grep '.*\.txt' 2.dat -c`
s=`grep '.*' 2.dat -c`
r=`expr $s - $n`
echo $r
