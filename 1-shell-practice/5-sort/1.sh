#!/bin/bash
# 有用户日志文件，每行记录了一个用户查询串，长度为1-255字节，共1千万行，请排出查询最多的前100条。
sort query_log.txt | uniq -c | sort -k1,1nr | head -100 | sed -n 's/^[ ]*[0-9]*[ ]//gp'
