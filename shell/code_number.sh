#!/bin/bash
# author     : minyi
# create time: 2020年10月30日
# function   : 实现当前目录下的C语言的代码行数的统计(不包含注释)

function get_total_code_number 
{
	# rm -rf /tmp/num.txt
	tmp_file=/tmp/num.txt.$(date +%s)
	cd $1
	#  -or -iname ".s"
	for s in `find . -name "*.c" -or -name "*.h"`
	do
		cat $s | \
			sed 's/[[:space:]]//g' | \
			grep -v \
				-e '^[\*|/]' \
				-e '^$' | \
			wc -l >> $tmp_file
	done

	#echo "current directory: $(pwd)"
	# $tmp_file　因为目录下可能没有源文件而导致　tmp_file为空
	# printf "%-20s|%s\n" "文件名" "数量"

	file_name=$(basename $(pwd))
	if [ -e $tmp_file ]
	then
		awk -v d=${file_name} \
			'BEGIN{sum=0}{sum+=$1}END{printf("%-20s|%-10d\n", d, sum)}' \
			$tmp_file
	else
			printf "%-20s|%-10d\n" ${file_name} 0

	fi
}

if [ $# -eq 0 ]
then
	echo "need code directory"
	echo "Usage: $0 <DIRECTORY>"
	exit
fi

get_total_code_number $1
rm -rf /tmp/num.txt*
