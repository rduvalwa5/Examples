'''
Created on May 3, 2015

@author: rduvalwa2
'''

class py_string:
    def __init__(self,strng = "NoString"):
        self._inString = strng
        
    def reverse(self, text = "NoString"):
        if len(text) <= 1:
            return text
#        print("text is ", text[1:] + text[0])
        """
        http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
        recursion:
         reverse(hello)
         = reverse(ello) + h           # The recursive step
         = reverse(llo) + e + h
         = reverse(lo) + l + e + h
         = reverse(o) + l + l + e + h  # Base case
         = o + l + l + e + h
         = olleh
        """
        return self.reverse(text[1:]) + text[0]   
    
    def reverseSimple(self, text): 
        return text[::-1]
    
    def reverseList(self,text):
        aR = ""
        textList = list(text)
        textList.reverse()
        for c in textList:
            aR = aR + c
        return aR

        """        
        >>> a = 'abcd'
        >>> aL = list(a)
        >>> aL
        ['a', 'b', 'c', 'd']
        >>> print(str(aL))
        ['a', 'b', 'c', 'd']
        >>> aL.reverse()
        >>> aL
        ['d', 'c', 'b', 'a']
         >> aR = ""
        >>> for c in aL:
        ...    aR = aR + c
        ... 
        >>> aR
        'dcba'
        >>> 
"""

if __name__ == '__main__':
    
    myString = "New string with punctuation! What do you think? No way."
    s1 = py_string()
    testString = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    print("reverse ", s1.reverse("abcdefg"))
    print("reverse simple  " ,s1.reverseSimple(s1._inString))
    print("reverse simple  " ,s1.reverseSimple(testString))
    print("reverse length 1",s1.reverse("a"))
    print("reverse using list ", s1.reverseList(testString))