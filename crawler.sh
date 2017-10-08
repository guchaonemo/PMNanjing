#!/usr/bin/bash
######################################################
#
# File Name:    crawl.sh
#
# Function:     
#
# Usage:        bash crawl
#
# Input:        total 
#
# Output:       none
#
# Author: guchao
#
# Create Time:    2016-12-05 16:18:10
#
######################################################
# TODO: 并行化任务执行
OK=0
ERR=1
COMMAND=1
# 工作目录
WORK_PATH=$(cd "$(dirname "$0")"; pwd)
lines=`ps -ef | grep python | wc -l`
while [ ${COMMAND} ]
do
    lines=`ps -ef | grep python | wc -l`
    if [ ${lines} -eq 2 ]
        then
        sleep 20
    else
        sleep 120
        `python PMDownloader.py &`
    fi
done

