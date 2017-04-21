#!/usr/bin/env bash
export rootDir=`pwd`
echo "当前文件夹:" $rootDir

for cDir in $(ls $rootDir)
do
    export currDir=$rootDir/${cDir}
    if [ -d $currDir ] ; then
        cd $currDir
        if [ -d $currDir/.git ] ; then
            echo ""
            echo "------------------------------------------------------------------------------------------------"
            echo $currDir
            git branch
        fi
    fi
done
