'''
Created on Dec 17, 2018

@author: rduvalwa2
'''
import os

print("os.name: ",os.name)
print("cpu_count: ",os.cpu_count())
print("ctermid ",os.ctermid())

print("current directory using os.curdir ")
print(os.curdir)
print("real current director")
os.system("pwd")

homePath = "/Users/rduvalwa2"
print("chdir /Users/rduvalwa2")
os.chdir(homePath)
print("system pwd: ")
os.system("pwd")


