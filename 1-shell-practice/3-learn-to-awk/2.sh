#!/bin/bash
# 对于一个保存 单词 频率 的文件，要同时计算它的累积频率，并将它填在第三列。输入为2.dat
awk '{count = count + $2; print $1,$2,count}' 2.dat
