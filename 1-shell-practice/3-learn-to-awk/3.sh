#!/bin/bash
# 读入一个包含词性的文件3.dat，从中提取出原始句子。
#str = substr($x,0,i);\
#tmp = tmp str
#for(x=1;x<NF;x++)
awk '{ str = "" ; for(x=1;x<=NF;x++) {str = str substr($x,1,index($x, "_")-1)} print str}' 3.dat
