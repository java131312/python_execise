#!/usr/bin/env bash
if [ $# != 1 ] ; then
echo "请输入分支名称"
exit 1;
fi

export beanchName=$1
export rootDir=`pwd`
echo "当前文件夹:" $rootDir

for cDir in $(ls $rootDir)
do
    export currDir=$rootDir/${cDir}
    if [ -d $currDir ] ; then
        cd $currDir
        if [ -d $currDir/.git ] ; then
            git add .
            git commit -am '自动合并'$beanchName
            git pull origin $beanchName
            git push origin $beanchName
        fi
    fi
done
