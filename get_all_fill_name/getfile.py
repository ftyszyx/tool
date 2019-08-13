#!/usr/bin/env python2
#-*-encoding:utf-8-*-

import os,sys
def listdir(dir,file):
    file.write(dir + '\n')
    fielnum = 0
    list = os.listdir(dir)  #列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(dir,line)
        if os.path.isdir(filepath):  #如果filepath是目录，则再列出该目录下的所有文件
            file.write('   ' + line + '//'+'\n')
            for li in os.listdir(filepath):
                file.write('     '+li + '\n')
                fielnum = fielnum + 1
        elif os.path:   #如果filepath是文件，直接列出文件名
            if line.find(".cpp")!=-1:
                file.write('\t\t\t\t../../Classes/Utility/zlib/'+line + '\\\n') 
                fielnum = fielnum + 1
                print line
            if line.find(".c")!=-1:
                file.write('\t\t\t\t../../Classes/Utility/zlib/'+line + '\\\n') 
                fielnum = fielnum + 1
                print line
    file.write('all the file num is '+ str(fielnum))
dir = raw_input('please input the path:')
myfile = open('d:\\list.txt','w')
listdir(dir,myfile)
myfile.close()