#!bin/bash
# Purpose: 使用datax将数据从postgresql中导出为json文件
# Create Time: 2021.09.08 17:08


LogMsg()
{
        now=`date "+%D %T"`
        echo "[$now : INFO    : $*" | tee -a log.txt
}

time=`date "+%Y%m%d"`
current=`date "+%Y-%m-%d %H:%M:%S"`
timesec=`date -d "$current" +%s`
#start=`expr $timesec - $timesec % 86400 - 28800`
start=1608114644

work_dir=/hdfsdata/5/hddata/datax

LogMsg "----------------------------------------------"
LogMsg "$0: 数据导出脚本"
LogMsg "----------------------------------------------"
LogMsg "开始于: `date +%F' '%T`"

LogMsg "************************************"
LogMsg "正在执行数据导出...请稍等..."
LogMsg "************************************"
LogMsg "hd sync begin"
LogMsg "************************************"
LogMsg "增量数据开始时间: start=$start, 文件存放路径: /hdfsdata/5/hddata/new/$time"
#python ${work_dir}/bin/datax.py -p "-Dstart=$start -Dtime=$time" ${work_dir}/job/job.json
LogMsg "************************************"
LogMsg "hd sync completed"
