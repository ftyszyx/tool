#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
# vim:expandtab:ts=4:sw=4:
# 
#   打包流程参见 buildApp
#
alipy_rate=0.042;
total_money=135000;
delete_per=total_money/48;
tax_money=13000


def clac_pay(month):
	return 0.0023*total_money*month;


def cla_alipy_money(month):
	global total_money
	global alipy_rate
	global delete_per
	getmoney=0;

	for x in range(1,month+1):
		remain=total_money-(x-1)*delete_per;
		getmoney=getmoney+((remain+tax_money)*alipy_rate/12)

	lastremina=total_money-(month-1)*delete_per+tax_money
	lastget=((lastremina+tax_money)*alipy_rate/12)
	return int(getmoney),int(lastremina),int(lastget);
	

for x in range(1,48):
	totalget,lastremina,lastget=cla_alipy_money(x);
	print("第%s月底：我给银行利息:%s,支付宝总到能得到的:%s,这个月能产生利息的本金:%s,这个月产生支付宝产生利息:%s" % (x,clac_pay(x),totalget,lastremina,lastget))
