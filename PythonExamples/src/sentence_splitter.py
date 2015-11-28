'''
Created on Mar 8, 2013

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" better_sentence_splitter.py 
Simpler program to list words of a string"""
s = input("Enter a string: ")
print(s)
words = s.strip().split()  
""" strip(s[, chars]) Return a copy of the string with leading and trailing characters removed. 
If chars is omitted or None, whitespace characters are removed. """

for word in words:
    print(word)