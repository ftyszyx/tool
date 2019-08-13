#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8 
#压缩json数据
import os,sys
import os.path
import json
reload(sys)
sys.setdefaultencoding('utf8')
workpath="D:\\work\\MCardClient\\Env\\UI"
#workpath="D:\\work\\test"
#压缩json文件
def jsoncompress(path):
     for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                name,ext= os.path.splitext(filename)
                jsonpath=os.path.join(dirpath, filename)
                if ext==".json" or ext==".ExportJson":
                    filesize=os.path.getsize(jsonpath)
                    print "src jsonpath:"+jsonpath+" filesize:"+str(filesize)
                    #print("process ExportJson: "+jsonpath)
                    jsonreadfile=open(jsonpath,"r")
                    jsontext=jsonreadfile.read()
                    jsonreadfile.close()
                    jsonobj=json.loads(jsontext)
                    jsonstring=json.dumps(jsonobj,indent = None,ensure_ascii=False,separators=(',',':'))
                    jsonwritefile=open(jsonpath,"w")
                    jsonwritefile.write(jsonstring)
                    jsonwritefile.close()
                    filesize=os.path.getsize(jsonpath)
                    print "compress jsonpath:"+jsonpath+" filesize:"+str(filesize)

jsoncompress(workpath)
os.system("pause")