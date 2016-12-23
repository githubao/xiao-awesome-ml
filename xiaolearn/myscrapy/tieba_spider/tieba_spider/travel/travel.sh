#!/bin/sh
# @Author: anchen
# @Date:   2016-11-11 16:01:59
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-11 16:56:42

# dir='/home/kongdeqian/conversation/original_conversation'
dir='C:\\Users\\BaoQiang\\Desktop\\test'

cd $dir
i=0
for file in `ls $dir`
do
    if [ -d $file ]
    then
    for sub in $file/*
    do
        echo "start $file $sub"

        if [[ $sub =~ "processed" ]]
        then
        echo ""
        continue
        fi
        final=${sub: -3}
        if [ "$final" != "txt" ]
        then
        echo ""
        continue
        fi

        cat $sub | grep "\"source\":\"摄影\"" >> ~/tieba_shenghuo.txt
        i=$(($i+1))
        echo "end $file $sub"
        echo "process $i"
        echo ""

    done

    fi

done


