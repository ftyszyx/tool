# -*- coding: utf-8 -*-

import urllib2
import re
import os
import sys
import random
import time
reload(sys)
sys.setdefaultencoding('utf-8')
# print sys.getdefaultencoding()


# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

#解析第一层页面
def ParseDocUrl(html):
    reg = r'<li>[\s]*<a href="\.(.*\.html)".*title="(.*)">'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

#下载文件地址
def GetDocDownUrl(html):
    # reg = r'<a href="\.(.*\.doc)"[\s]class="h12">(.*\.doc)</a>'
    # url_re = re.compile(reg)
    url_lst = re.findall('<a href="\.(.*\.doc)"[\s]*.*>(.*\.doc)</a>',html)
    return(url_lst)




def getFile(url,downloadpath,subpath,filename):
    # print(url)
    if filename=="":
        filename = url.split('/')[-1]
    u = urllib2.urlopen(url)
    pathname=os.path.join(downloadpath,subpath)
    if os.path.exists(pathname)==False:
        os.mkdir(pathname)
   
    f = open(os.path.join(pathname,filename), 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + filename





def SaveFile1():
    baseurl="http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj"  #网址路径
    needSubPath=False  #是否要建子文件价
    filename_usetitle=False #是否要以标题命名
    flodername="download"  #保存的文件目录
    pagenum=25

    curpath=os.getcwd()
    downloadpath=os.path.join(curpath,flodername)
    if os.path.exists(downloadpath)==True:
        os.rmdir(downloadpath)
    os.mkdir(downloadpath)
    
    for pageindex in range(0,pagenum):
        url=""
        if pageindex==0:
            url=baseurl+"/index.html"
        else:
            url=baseurl+"/index_%d.html" % pageindex
        html = getHtml(url)
        reslist=ParseDocUrl(html)
        for docitem in reslist:
            docurl=baseurl+docitem[0]
            dochtml = getHtml(docurl)
            docpath=docitem[0].split("/")[1]
            doclist=GetDocDownUrl(dochtml)
            # print("doclist",doclist)
            for docitemurl in doclist:
                docdownurl=baseurl+"/"+docpath+docitemurl[0]
                if filename_usetitle==True:
                    if needSubPath==True:
                        getFile(docdownurl,downloadpath,docpath,docitemurl[1].encode('gb2312'))
                    else:
                        getFile(docdownurl,downloadpath,"",docitemurl[1].encode('gb2312'))
                else:
                    if needSubPath==True:
                        getFile(docdownurl,downloadpath,docpath,"")
                    else:
                        getFile(docdownurl,downloadpath,"","")

#pandoc https://github.com/jgm/pandoc/releases/tag/2.4
def converhtml2doc(html,outpath):
    curpath=os.getcwd()
    f = open(os.path.join(curpath,"temp.html"), 'wb')
    f.write(html)
    f.close()
    cmd= "pandoc -o %s.docx temp.html" % outpath
    ret = os.system( cmd )
    #ret = 0
    if ret != 0:
        print "save file error"+outpath
        return False
    else:
       print "save file ok"+outpath


def SaveFile2():
    baseurl="http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj"  #网址路径
    needSubPath=False  #是否要建子文件价
    flodername="download6"  #保存的文件目录
    pagenum=2

    curpath=os.getcwd()
    downloadpath=os.path.join(curpath,flodername)
    if os.path.exists(downloadpath)==True:
        os.rmdir(downloadpath)
    os.mkdir(downloadpath)
    
    for pageindex in range(0,pagenum):
        url=""
        if pageindex==0:
            url=baseurl+""
        else:
            url=baseurl+"/index_%d.htm" % pageindex
        print(url)
        html = getHtml(url)
        reslist=ParseDocUrl(html)
        for docitem in reslist:
            docurl=baseurl+docitem[0]
            doctitle=docitem[1]
            dochtml = getHtml(docurl)
            docpath=docitem[0].split("/")[1]
            htmltext = re.findall('(<div[\s]*class="content">[.\S\s]*)<div[\s]*class="foot">',dochtml)[0]
            filename=doctitle.encode('gb2312')
            subpath=downloadpath
            if needSubPath==True:
                subpath=os.join(downloadpath,docpath)
                if os.path.exists(subpath)==False:
                    os.mkdir(subpath)
            converhtml2doc(htmltext,os.path.join(subpath,filename))
               

if __name__ == '__main__':
    SaveFile2()
    print("ok")
        