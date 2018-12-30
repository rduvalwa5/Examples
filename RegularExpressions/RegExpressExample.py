'''
Created on Dec 29, 2018
@author: https://docs.python.org/3/library/re.html

'''
import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))
# 'def'
m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))
# 'egg'