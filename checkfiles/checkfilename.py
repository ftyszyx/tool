#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8 

import os,sys
import os.path
checkpath="D:\work\MCardClient\Env"

for dirpath, dirnames, filenames in os.walk(checkpath):
    for filename in filenames:
        if filename.count(" ")>0:
            errpath=os.path.join(dirpath, filename)
            print errpath