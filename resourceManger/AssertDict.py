#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8 

import os,sys
from xml.etree import ElementTree as ET
import json
import codecs

# resources path
rs_path = "\\UI\\"

#需要提前处理的图片路径
action_path=[]
action_path.append("\\UI\\action")
action_path.append("\\UI\\action_speff")

#输出文件名
outputFileName="resource.json"

#用于缓存图片
texture_list=[]
plist_list=[]
texture_inPlist=[]

#用于验证是否有重复
picdic={}
plistdic={}


#图片类型
PLISTTYPE=2
PLIST_PIC_TYPE=3
NORMAL_PIC_TYPE=1



#处理特殊的图片
def processSpecialFiles():
    curpath=os.getcwd()
    for path in action_path:
        processpath=curpath+path
        #print("process files in: "+processpath)
        for dirpath, dirnames, filenames in os.walk(processpath):
            for filename in filenames:
                name,ext= os.path.splitext(filename)
                #print(name,ext)
                #先处理plist

                if ext==".plist":
                    #替换掉plist中的key
                    writePlistFlag=False
                    plistpath=os.path.join(dirpath, filename)
                    #print("process plist: "+plistpath)
                    tree=ET.parse(plistpath)
                    root = tree.getroot()
                    if root[0][0].text == "frames":   
                        for elem in root[0][1]:
                            if elem.tag == "key":
                                beforeTextTemp=elem.text
                                elem.text=elem.text.replace("/","_")
                                if beforeTextTemp!=elem.text:
                                    writePlistFlag=True

                                #print(elem.text)
                    if writePlistFlag==True:
                        tree.write(plistpath)
                        print("write plist: "+plistpath)
                elif ext==".ExportJson":
                    #替换掉exportjson中的key
                    writePlistFlag=False

                    jsonpath=os.path.join(dirpath, filename)
                    #print("process ExportJson: "+jsonpath)
                    jsonreadfile=open(jsonpath,"r")
                    jsontext=jsonreadfile.read()
                    jsonreadfile.close()
                    jsonobj=json.loads(jsontext)
                    for bone_data in jsonobj["armature_data"][0]["bone_data"]:
                        if bone_data.has_key("display_data")==True:
                            for displaydata in bone_data["display_data"]:
                                beforeTextTemp=displaydata["name"]
                                displaydata["name"]=displaydata["name"].replace("/","_")
                                if beforeTextTemp!=displaydata["name"]:
                                    writePlistFlag=True
                        else:
                            print("Error:bone_data in "+jsonpath+" layername:"+bone_data["name"]+" have not display_data")        
                    for texture in jsonobj["texture_data"]:
                        beforeTextTemp=texture["name"]
                        texture["name"]=texture["name"].replace("/","_")
                        if beforeTextTemp!=texture["name"]:
                            writePlistFlag=True
                    if writePlistFlag==True:
                        jsonstring=json.dumps(jsonobj,indent = 4,ensure_ascii=False)
                        jsonwritefile=open(jsonpath,"w")
                        jsonwritefile.write(jsonstring)
                        jsonwritefile.close()
                        print("write ExportJson: "+jsonpath)
# 初始化方法
def getAllTexture():
    # 填充所有目录和文件名称
    curpath=os.getcwd()
    for dirpath, dirnames, filenames in os.walk(rs_path):
        # 填充 texture
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext == ".plist":
                plist_list.append(os.path.join(dirpath, filename))
            elif ext == ".png" or ext==".jpg":
                texture_list.append(os.path.join(dirpath,filename))



def getItemNode(path,type,itemnode):
    filename=os.path.basename(path)
    name,ext=os.path.splitext(filename)
    itemnode["key"]=name
    pathstring=path.replace(rs_path,"")
    itemnode["path"]=pathstring.replace("\\","/")
    itemnode['type']=type
    if type==PLISTTYPE:
        if plistdic.has_key(name)==True:
            print "plist Key:"+name+" is conflict"
        else:
            plistdic[name]=itemnode
    elif type==NORMAL_PIC_TYPE:
        if picdic.has_key(name)==True:
            print "picture Key:"+name+" is conflict"
        else:
            picdic[name]=itemnode



#增加plist里面的图片引用
def  addPlistpic(plistpath,pictrues):
    root = ET.parse(plistpath).getroot()
    if root[0][0].text == "frames":                
        for elem in root[0][1]:
            if elem.tag == "key":
                itemtemp={}
                filename=os.path.basename(elem.text)
                name,ext=os.path.splitext(filename)
                itemtemp["key"]=name
                plistname,plistext=os.path.splitext(os.path.basename(plistpath))
                itemtemp["path"]=plistname
                itemtemp['type']=PLIST_PIC_TYPE
                #print "itemtemp:",itemtemp
                pictrues.append(itemtemp)
                #print(pictrues)
                if picdic.has_key(name)==True:
                    print "plist Key:"+name+" is conflict"
                else:
                    picdic[name]=itemtemp


# 生成配置文件，字典
def generate_json():
    pictrues=[]
    
    #plist
    for plist in plist_list:
        itemtemp={}
        getItemNode(plist,PLISTTYPE,itemtemp)
        pictrues.append(itemtemp)
        addPlistpic(plist,pictrues)
        
    #pic
    for pictrue in texture_list:
        itemtemp={}
        getItemNode(pictrue,NORMAL_PIC_TYPE,itemtemp)
        pictrues.append(itemtemp)
                            
    json_file = {
        "pictrues": pictrues
    }
    
    curpath=os.getcwd()
    
    output_file=codecs.open(curpath+'\\'+outputFileName,"w","utf-8")
    jsonstring=json.dumps(json_file,indent = 4,ensure_ascii=False)
    output_file.write(jsonstring)
    output_file.close()

curpath=os.getcwd()
print "---------curpath:",curpath
rs_path=curpath+rs_path
print "-----------resource path:",rs_path

processSpecialFiles()
getAllTexture()   
generate_json()
print("-----------------enjoy--------------------")
os.system("pause")