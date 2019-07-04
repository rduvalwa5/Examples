'''
Created on Dec 29, 2018
@author: https://docs.python.org/3/library/re.html

'''
import re

testString = "The quick brown fox \
jumped over the \
lazy fox hound." 

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))
# 'def'
m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))
# 'egg'


matchObj = re.match( r'(.*)jumped', testString, re.M)
print("m1 ",matchObj)

matchObj = re.match(r'(.*)jumped(.?)', testString, re.M)
print("m2 ",matchObj)


m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))       # The entire match
# 'Isaac Newton'
print(m.group(1))       # The first parenthesized subgroup.
#'Isaac'
print(m.group(2))       # The second parenthesized subgroup.
#'Newton'
print(m.group(1, 2))    # Multiple arguments give us a tuple.
#('Isaac', 'Newton')
try:
    print(m.group(3)) 
except IndexError as noSuchGroup:
    print(noSuchGroup)