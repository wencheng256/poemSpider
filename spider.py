# -*- coding: utf-8 -*-
import process
import sys
import db

t = 7239
i=15
while(i<t):
    process.processpage("http://so.gushiwen.org/type.aspx?p="+str(i))
    db.finish(i)
    i+=1