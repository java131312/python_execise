#!/usr/bin/env bash
if [ $# < 1 ] ; then
echo "请输入标签名称"
exit 1;
fi

export tag_a=$1
export tag_m=$2
export rootDir=`pwd`
echo "当前文件夹:" $rootDir

for cDir in $(ls $rootDir)
do
    export currDir=$rootDir/${cDir}
    if [ -d $currDir ] ; then
        cd $currDir
        if [ -d $currDir/.git ] ; then
            echo "------------------------------------------------------"
            echo "Git目录：" $currDir "("$tag_a")"
            git tag -a $tag_a -m "$tag_m"
            git push origin $tag_a
        fi
    fi
done


