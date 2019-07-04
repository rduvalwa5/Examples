'''
Created on Jan 18, 2019
^
(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after 
each newline.
'''
import re

testString = "The quick brown fox \
jumped over the \
lazy fox hound."

print(testString)

print(re.match(r'^>The',testString))
#  re.compile(r'^>([^\n\r]+)[\n\r]([A-Z\n\r]+)', re.MULTILINE
print(re.match('jumped',testString))

mtch = re.match('^lazy',testString)
print(mtch)
