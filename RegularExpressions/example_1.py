'''
Created on Jan 20, 2019

@author: rduvalwa2
'''

import re

'''
prog = re.compile(pattern)
result = prog.match(string)
is equivalent to

result = re.match(pattern, string)
but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used 
several times in a single program.

Note The compiled versions of the most recent patterns passed to re.compile() and the module-level matching functions are cached, 
so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.

'''

str = "This is a long string for using a regular expression against.  This is  a shorter string for same purpose."

mtch = re.match(r'(.*).',str)
print(mtch)

mtch = re.match(r'(.*)a',str)
print(mtch)

matchObj = re.match( r'(.*)long', str, re.M)
print("m1 ",matchObj)

matchObj2 = re.match('(.*)long', str)
print("m2  ",matchObj2.group())
print("m2 0",matchObj2.group(0))
print("m2 1",matchObj2.group(1))

matchObj3 = re.match('(.*)purpose', str)
print("m3  ",matchObj3.group())
print("m3 0",matchObj3.group(0))
print("m3 1",matchObj3.group(1))