#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8 

#重命名文件
import sys
import os, os.path
import shutil

#获取当前路径 
curpath=os.getcwd()
print "curpath:",curpath

method=raw_input("add pre or del pre or replace?(add or del or replace):")


prename=""
wanttorepalce=""
replaceby=""
if method=="add":
    prename=raw_input("please input your pre name:")
elif method=="del":
    prename=raw_input("please input your pre name:")
elif method=="replace":
    wanttorepalce=raw_input("please input the string you want to replace:")
    replaceby=raw_input("please input the string you want to replaceby:")



#加前缀
def addpre():
    for dirpath, dirnames, filenames in os.walk(curpath):
        for filename in filenames:
            name,ext= os.path.splitext(filename)
            if ext!=".py":
                srcpath=os.path.join(dirpath, filename)
                print srcpath
                newfilename=prename+name+ext
                dstpath=os.path.join(dirpath,newfilename)
                os.rename(srcpath,dstpath)
#减前缀
def delpre():
    for dirpath, dirnames, filenames in os.walk(curpath):
        for filename in filenames:
            name,ext= os.path.splitext(filename)
            if ext!=".py":
                srcpath=os.path.join(dirpath, filename)
                print srcpath
                newfilename=filename.replace(prename,"")
                dstpath=os.path.join(dirpath,newfilename)
                os.rename(srcpath,dstpath)

#替换
def replacestring():
    for dirpath, dirnames, filenames in os.walk(curpath):
        for filename in filenames:
            name,ext= os.path.splitext(filename)
            if ext!=".py":
                srcpath=os.path.join(dirpath, filename)
                print srcpath
                newfilename=filename.replace(wanttorepalce,replaceby)
                dstpath=os.path.join(dirpath,newfilename)
                os.rename(srcpath,dstpath)

if method=="add":
    addpre()
elif method=="del":
    delpre()
elif method=="replace":
    replacestring()

os.system("pause")
