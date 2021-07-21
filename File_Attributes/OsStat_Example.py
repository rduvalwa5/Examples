'''
 https://docs.python.org/3/library/stat.html
 https://www.tutorialspoint.com/python/os_stat.htm
 https://www.geeksforgeeks.org/python-os-stat-method/
 https://docs.python.org/3/library/stat.html?highlight=filemode
 
 https://kb.iu.edu/d/abdb
Permission    Number
Read (r)        4
Write (w)       2
Execute (x)     1
 
'''

# !/usr/bin/python

import os, sys

# showing stat information of file "a2.py"

fileName = 'OsStat_Example.py'
statinfo = os.stat(fileName)
print (statinfo)
print(statinfo[0])
print(oct(statinfo[0]))
#fMode = stat.ST_MODE(fileName) 
#print(stat.filemode(statinfo[0]))
os.stat

os.system("ls -l OsStat_Example.py")

'''
os.stat_result(st_mode=33188, st_ino=18058077, st_dev=16777228, st_nlink=1, st_uid=501, st_gid=20, st_size=725, st_atime=1621911217, st_mtime=1621911215, st_ctime=1621911215)
33188
0o100644
-rw-r--r--  1 rduvalwa2  staff  725 May 24 19:53 OsStat_Example.py
'''