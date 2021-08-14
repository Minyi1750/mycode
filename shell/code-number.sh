#!/bin/bash
# author : minyi
# create time: 2020年10月30日
# function : 实现当前目录下的C语言的代码行数的统计(不包含注释)
 

function get_total_code_number
{
	rm -rf /tmp/num.txt
	cd $1
	
	# -or -iname ".s"
	for s in `find . -name "*.c" -or -name "*.h"`
	do
		# 过滤以*或者/开头的代码
		cat $s | sed 's/[[:space:]]//g' |grep -v -e '^[\*|/]' -e '^$'| wc -l >> /tmp/num.txt
	done

	#echo "current directory: $(pwd)"
	awk -v d=$(pwd) 'BEGIN{sum=0}{sum+=$1}END{printf("%s %-10d\n", d, sum)}' /tmp/num.txt
}

if [ $# -eq 0 ]
then
	echo "need code directory"
	echo "Usage: $0 <DIRECTORY>"
	exit
fi
 
get_total_code_number $1
