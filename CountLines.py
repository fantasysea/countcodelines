# -*- coding: utf-8 -*-
# 统计代码量
# 把代码的路径传递进去

import os

path = "d:/php"
filter=[".php",".html",".sql",".js",".css"]
print path

def countLines(path):
    count  = 0
    for parent, dirnames, filenames in os.walk(path):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for dirname in  dirnames:                       #输出文件夹信息
        #     print "parent is:" + parent
        #     print  "dirname is" + dirname
        # count = count+len(filenames)
        for filename in filenames:  # 输出文件信息
            # print "parent is:" + parent
            # print "filename is:" + filename
            # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            # if filename.endswith(".php"):
            # print os.path.splitext(filename)[1]
            if os.path.splitext(filename)[1] in filter:
                print "the full name of the file is:" + os.path.join(parent, filename)  # 输出文件路径信息
                count = count+len(open(os.path.join(parent, filename), 'rU').readlines())

    print "files = "+str(count)


if __name__ == '__main__':
    countLines(path)