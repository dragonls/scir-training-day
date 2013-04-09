#!/bin/bash
# 输出一个文件所有的偶数行，数据1.dat
awk '{if (NR % 2 == 0){print $0}}' 1.dat
