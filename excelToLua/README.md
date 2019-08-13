excelToLua
==========

将excel表格中的数据转成lua可读的表(python实现)


##使用方法

- 安装python2.7
- 安装第三方库xlrd
- 将excelToLua.py和要转换的excel表格放在同一目录下（excel表格名要英文，表格内每单元表的名字也要用英文)
- 双击excelToLua.py,程序将会在同一目录下生成lua文件

##表格内的格式如下：

![参考excel表格](https://github.com/ftyszyx/excelToLua/blob/master/table.jpg?raw=true)

第二行第一列是id所在列

第二行第二列是要导出的列

每三行是无效的，解释作用

第四行是每一列的名子，必须英文

从第五行开始是实际数据


##转换后的Lua文件如下：

![参考excel表格](https://github.com/ftyszyx/excelToLua/blob/master/deslua.jpg?raw=true)
