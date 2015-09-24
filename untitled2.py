# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:34:26 2015

@author: lilun
"""

f=open('test.txt')
print f.read()
f.close()

f=open('test2.txt', 'w')
s='aaaaaaaaaaaaaaaaaaaaaa\n'
f.write(s)
f.close()