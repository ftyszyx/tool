import os
import json

#dict_keys(['logcat', 'Brand', 'Model', 'pid', 'network info', 'memory info', 'App version', 'pname', 'Manufacturer', 'Rooted', 'open files', 'other threads', 'OS version', 'Kernel version', 'ABI list', 'Start time', 'foreground', 'Build fingerprint', 'App ID', 'Cras
#h type', 'API level', 'ABI', 'Crash time', 'Tombstone maker'])

def parseOneFile(filepath):
     dict={}
     uid=filepath.split("_")[1]
     dict["uid"]=uid
     with open(filepath,"r", encoding='utf8') as f:
            ftext=f.read()
            if ftext.startswith("{"):
                try:
                    ftext = ftext.replace("\n", '\\n')
                    #print(ftext[0:130])
                    filejson=json.loads(ftext)

                except Exception as e:
                    print(filepath,"解析错误:",e.__str__(),type(e))
                    exit(-1)
                else:
                    #print(filejson.keys())
                    return filejson

            else:
                print(filepath,"非json")
     return  None


def solvepath(filepath):
    g=os.walk(filepath)
    crashlist=[]
    #处理所有文件
    for path,dirlist,filelist in g:
        for filename in filelist:
            subfilepath=os.path.join(path,filename)
            print(subfilepath)
            crashitem=parseOneFile(subfilepath)
            if crashitem!=None:
                crashlist.append(crashitem)
    #生成excel

if __name__=="__main__":
    solvepath("C:\\Users\\zyx\\Desktop\\crash_202003272")