#!/bin/sh
# 从4.dat中提取并格式输出
var=`grep 'Total:' 4.dat`
while [ ${#var} -gt 20 ]; do
# 竟然只能用sh，不能用bash，好多限制啊。。。
	var=${var#*P}
#	varOut=${var:0:5}
	varOut=`expr substr "$var" 2 5`
#	varOut=${var#\=*(}
	printf "P=%.2f " "$varOut"
	var=${var#*R}
#	varOut=${var:0:5}
	varOut=`expr substr "$var" 2 5`
#	varOut=${var#=*(}
	printf "R=%.2f " "$varOut"
	var=${var#*F}
#	varOut=${var:0:5}
	varOut=`expr substr "$var" 2 5`
#	varOut=${var#=*\n}
	printf "F=%.2f\n" "$varOut"
done

