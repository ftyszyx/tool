import os
import json
import xlwt
import shutil

#dict_keys(['logcat', 'Brand', 'Model', 'pid', 'network info', 'memory info', 'App version', 'pname',
# 'Manufacturer', 'Rooted', 'open files', 'other threads', 'OS version', 'Kernel version', 'ABI list', 'Start time', 'foreground', 'Build fingerprint', 'App ID', 'Crash type',
# 'API level', 'ABI', 'Crash time', 'Tombstone maker'])

def parseOneFile(filepath):
     uid=os.path.basename(filepath).split("_")[1].split(".")[0]
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
                    filejson["uid"]=uid
                    return filejson

            else:
                print(filepath,"非json")
     return  None


def solvepath(filepath,outpath):
    if os.path.exists(outpath):
        shutil.rmtree(outpath, True)
    os.mkdir(outpath)
    excelpath=os.path.join(outpath,"outexcel.xls")
    g=os.walk(filepath)
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("sheet1")  # 在工

    sheet.write(0,0,"uid")
    sheet.write(0, 1, "crash_Type")
    sheet.write(0, 2, "version")
    sheet.write(0, 3, "device")
    sheet.write(0, 4, "ABI")

    # sheet.write(0, 4, "log")

    #处理所有文件
    row=0
    for path,dirlist,filelist in g:
        for filename in filelist:
            subfilepath=os.path.join(path,filename)
            print(subfilepath)
            crashitem=parseOneFile(subfilepath)
            if crashitem!=None:
                row+=1
                sheet.write(row, 0, crashitem["uid"])
                sheet.write(row, 1, crashitem["Crash type"])
                sheet.write(row, 2, crashitem["OS version"])
                sheet.write(row, 3,crashitem["Build fingerprint"])
                sheet.write(row, 4, crashitem["ABI"])
                logpath = os.path.join(outpath, (row+1).__str__()+"_.log")
                f=open(logpath,"w", encoding='utf8')
                f.write(crashitem["logcat"])
                f.close()

    workbook.save(excelpath)

    #生成excel

if __name__=="__main__":
    solvepath("C:\\Users\\zyx\\Desktop\\crash_202003272","C:\\Users\\zyx\\Desktop\\output")