#!/bin/bash
# 去掉文件中的空行，数据1.dat
sed -n '/^$/! p' 1.dat
