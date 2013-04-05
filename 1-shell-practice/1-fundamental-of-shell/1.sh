#!/bin/sh
# Practice 1
if [ $# -ne 1 ]; then
	echo error
else
	echo $1$1
fi
