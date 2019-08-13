#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8 

import os.path
import codecs
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#一些变量定义
replace_param1="(###)"#用来替换名字
replace_param2="(***1)"#用来指明声明位置
replace_param3="(***2)"#用来指明触发函数代码位置
replace_param4="(***3)" #json文件名


#控件变量声明函数
view_statment="self.view.(###)=self.widget"
view_statment_repeat=":getChildByName(\"(###)\")"
click_addlistener_stence="self.view.(###):addTouchEventListener(on(###)Click)\r\n"
checkbox_addlistener_stence="self.view.(###):addEventListenerCheckBox(on(###)Click)\r\n"


#点击处理函数
clickfun_statment_normal="""
local function on(###)Click(sender, eventType)
	if eventType == ccui.TouchEventType.ended then
	end
end
"""

clickfun_statment_checkbox="""
local function on(###)Click(sender, eventType)
 	if eventType == ccui.CheckBoxEventType.selected then
	elseif eventType == ccui.CheckBoxEventType.unselected then
	end
end
"""


#遍历子节点，
#找出tag=0的表示要导出的，touchable的：可触摸的。
def get_statement_string(fatherlist,elementname):
	statment1=view_statment.replace(replace_param1,elementname)
	for	element in fatherlist:
		fatherstring=view_statment_repeat.replace(replace_param1,element)
		statment1=statment1+fatherstring
	statment1+=view_statment_repeat.replace(replace_param1,elementname)
	return statment1


def getListString(element,fatherlist):
	global statmentstring
	global clickfuncString
	templist=[]
	templist=fatherlist[:]
	classname=element["classname"]
	tag=element["options"]["tag"]
	touchenable=element["options"]["touchAble"]
	elementname=element["options"]["name"]
	mychildren=element["children"]
	#if tag==0:
		#print templist,elementname
		#statmentstring+="\t"+get_statement_string(fatherlist,elementname)+"\n"
	#elif touchenable==True and (classname!="Panel"):
		#print templist,elementname
		#statmentstring+="\t"+get_statement_string(fatherlist,elementname)+"\n"
	if touchenable==True and (classname!="Panel") and (classname!="ScrollView"):
		if classname=="CheckBox":
			statmentstring+="\t"+checkbox_addlistener_stence.replace(replace_param1,elementname)
			clickfuncString+=clickfun_statment_checkbox.replace(replace_param1,elementname)
		else:
			statmentstring+="\t"+click_addlistener_stence.replace(replace_param1,elementname)
			clickfuncString+=clickfun_statment_normal.replace(replace_param1,elementname)
	if len(mychildren)!=0:
		templist.append(elementname)
		getChildren(mychildren,templist)


def getChildren(children,fatherlist):
	templist=[]
	templist=fatherlist
	for element in children:
		getListString(element,templist)

			



#获取当前路径
curpath=os.getcwd()
print "curpath:",curpath

#输入文件名
wgname=raw_input("please input your wg name:")
jsonname=raw_input("please input json file name:")
isclass=raw_input("do you want to geterate a class(y:get a class,n:not class):")


#读模板文件
inputflag=True
if isclass=='y':
	temple_file=open(curpath+'\\'+"wg_temple_class.lua","r")
elif isclass=='n':
	temple_file=open(curpath+'\\'+"wg_temple.lua","r")
else:
	print("error input !!")
	inputflag=False

if inputflag==True:
	temple_text=temple_file.read()
	temple_text=temple_text.replace(replace_param1,wgname)
	temple_text=temple_text.replace(replace_param4,jsonname)
	temple_file.close()

	if jsonname!="":
		jsonfile=open(curpath+'\\'+jsonname+".json","r")
		jsontext=jsonfile.read()
		jsonobj=json.loads(jsontext)
		children=jsonobj["widgetTree"]["children"]
		statmentstring=""  #声明语句
		clickfuncString="" #点击函数语句
		getChildren(children,[])
		temple_text=temple_text.replace(replace_param2,statmentstring)
		temple_text=temple_text.replace(replace_param3,clickfuncString)
		jsonfile.close()
	else:
		temple_text=temple_text.replace(replace_param2,"")
		temple_text=temple_text.replace(replace_param3,"")


	#写输出文件
	outputFileName=wgname+"_wg.lua"
	output_file = open(curpath+'\\'+outputFileName, 'w',)
	output_file.write(temple_text)
	output_file.close()

	print("file is output to "+curpath+'\\'+outputFileName)
os.system("pause")


