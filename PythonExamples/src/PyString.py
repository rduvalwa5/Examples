'''
Created on Mar 24, 2015
@author: rduvalwa2
https://docs.python.org/3/library/string.html?highlight=string#module-string
https://docs.python.org/3/library/stdtypes.html#string-methods

This is how to reverse a string
http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
'''

class py_string:
    def __init__(self,strng = "NoString"):
        self._inString = strng
        
    def reverse(self,text = "Not a string"):
        if len(text) <= 1:
            return text
        return self.reverse(text[1:]) + text[0]   
    
    def reverseSimple(self, text): 
        return text[::-1]
    
    def makeUpper(self,text):
        return text.upper()
    
    def makeLower(self, text):
        return text.lower()
    
    def makeCaps(self, text):
        return text.capitalize()
    
    def splitString(self, text, sep):
        return text.split(sep)
    
    def stringJoin(self,itr,seq): #list
        return itr.join(seq)

'''
s = "This is a string of words. It has punctuation! Does't it? But \"not this\"."
s1 = "1234567890ABcdefG{};:"
print(s)
print(s[0])
print(s[3:15])

for a in s:
    if a in {".","?","!","'","\""}:
            print(a)

print("upper " ,s.upper())
print("lower ", s.lower())
print("capitalize ",s.capitalize())
print(s.count("i"))
print(s.count("i",20,-1))
s = s + s1
print(s)

print("s[::-1]" ,s[::-1])
    
print("reverse(s)",reverse(s))
 '''
    
if __name__ == '__main__':
    myString = "New string with punctuation! What do you think? No way."
    
    s1 = py_string()
    print(s1._inString)
    print(s1.reverse())
    print(s1.reverseSimple(s1._inString))
    
    s2 = py_string(myString)
    print(s2._inString)
    print(s2.reverse(myString + "0987654321"))
    print(s2.reverse())
    
    print("double reverse ", s2.reverse(s2.reverseSimple(myString)))
    capString = "one two three four five.  Six seven eight?"
    print(capString)
    
    print("Capitilize",s2.makeCaps(capString))
    print("split", s2.splitString(capString, " "))
    splitString = s2.splitString(capString, " ")
    print("spliotString ", splitString)
    newString = ""
    for word in splitString:
        newString = newString + s2.makeCaps(word) + " "    
    print(newString)
    
    separator = "+"
    seq = ("one","two","three","four")
    print("Join ", s2.stringJoin(separator,seq))
    
    
        