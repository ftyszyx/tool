# coding=UTF8
# 第二行第一列是id的列索引
# 第二行第二列是有效列
# 表格从0开始索引 
import codecs
import xlrd
import os.path


def getTabelById(sheetname,rownum,idindex,outputfile,validcols,validcolsName,sheet):
	outputfile.write(sheetname+u"={\n")
	for rowindex in range(4,rownum):
		if sheet.cell_type(rowindex,idindex)==0:
			#说明是没有id的
			outputfile.write(u"{\n")
		else:
			id = int(sheet.cell_value(rowindex,idindex))
			outputfile.write(u"\t['"+unicode(id)+u"']={\n")
		
		colcount=0
		for colindex in validcols:
			#键名
			outputfile.write(u"\t\t['"+validcolsName[colcount]+u"'] = ")
			#键值 
			cellobj=sheet.cell_value(rowindex,colindex)
			cellstr=u""
			if type(cellobj)==unicode:
				cellstr=u"'"+cellobj+u"',"
			elif type(cellobj)==float:
				strlist=str(cellobj).split(".")
				if len(strlist)==1:
					cellstr=str(cellobj)+","
				elif strlist[1]=='0':
					cellstr=str(strlist[0])+","
				else:
					cellstr=str(cellobj)+","
			else:
				cellstr=u"'"+cellobj+u"',"
			outputfile.write(cellstr+u"\n")
			colcount=colcount+1
		if sheet.cell_type(rowindex,idindex)==0:
			#说明是没有id的
			outputfile.write(u"},\n")
		else:
			outputfile.write("\n\t},\n")	
	outputfile.write("\n};\n")


def getvectortable(sheetname,rownum,validcols,outputfile,validcolsName,sheet):
	outputfile.write(sheetname+u"={\n")
	colcount=0
	for colindex in validcols:
		#键名
		outputfile.write(u"\t\t['"+validcolsName[colcount]+u"'] ={\n")
		for rowindex in range(4,rownum):
			#键值 
			cellobj=sheet.cell_value(rowindex,colindex)
			cellstr=u"\t"
			if type(cellobj)==unicode:
				cellstr=cellstr+u"'"+cellobj+u"',"
			elif type(cellobj)==float:
				strlist=str(cellobj).split(".")
				if len(strlist)==1:
					cellstr=cellstr+str(cellobj)+","
				elif strlist[1]=='0':
					cellstr=cellstr+str(strlist[0])+","
				else:
					cellstr=cellstr+str(cellobj)+","
			else:
				cellstr=cellstr+u"'"+cellobj+u"',"
			outputfile.write(cellstr+u"\n")
		colcount=colcount+1
		outputfile.write("\n\t},\n")	
	outputfile.write("\n};\n")

#转换
def convertToLua(sourcetablepath,desluatablepath):
	table=xlrd.open_workbook(sourcetablepath)
	outputfile=codecs.open(desluatablepath,"w","utf-8")
	for sheet in table.sheets(): 
		rownum=sheet.nrows
		colnum=sheet.ncols
		sheetname=sheet.name

		print "sheetname:",sheetname
		print "rownum:",rownum
		print "colnum:",colnum

		if rownum<4 and colnum <2:
			print "sheet is empty"
			return

		#获取id所在的列,以及有效列
		idflag=False
		if type(sheet.cell_value(1,0))==float:
			idindex=int(sheet.cell_value(1,0))
			print "idindex:",idindex
			idflag=True

		validcols=[]
		for index in sheet.cell_value(1,1).split(","):
			validcols.append(int(index))
		
		print "validcols:",validcols
		#获取每列的名字
		validcolsName=[]
		for index in validcols:
			validcolsName.append(sheet.cell_value(3,index))
		print "validcolsName:",validcolsName
		if idflag==True:
			getTabelById(sheetname,rownum,idindex,outputfile,validcols,validcolsName,sheet)
		else:
			getvectortable(sheetname,rownum,validcols,outputfile,validcolsName,sheet)
		print("begin to write sheet"+sheetname)
		#写数据表名(带id)
	
	outputfile.close()



#获取当前路径 
curpath=os.getcwd()
print "curpath:",curpath

filenames=os.listdir(os.getcwd())
for filename in filenames:
	temp=filename.split('.')
	if len(temp)==2:
		if temp[1]=='xls':
			excelpath=curpath+'\\'+filename
			luapath=curpath+'\\'+temp[0]+'.lua'
			print "covert table :",excelpath," to lua table:",luapath
			convertToLua(excelpath,luapath)
os.system("pause")
