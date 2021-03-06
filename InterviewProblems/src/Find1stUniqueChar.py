'''
Created on May 2, 2015
This problem was posed as a Java program white board task for Staples 
@author: rduvalwa2

http://pyunit.sourceforge.net/pyunit.html
http://docs.python-guide.org/en/latest/writing/tests/
'''

"""
    This method can be used to find the first unique character in a string
"""
class returnUnique:

    def uniquechar(self,seq):
        returnVal = "no unique character"
        for i in seq:
            ch = i
            chCount = seq.count(ch)
            if chCount == 1:
                returnVal = ch
                break
        return returnVal

if __name__ == '__main__':
    print("Start test**********")
    testString = "abcdefabcde"
    
    s1 = returnUnique()
        
    testString = "abcdefabcde"
    print("Expect \"f\" Return value is ",s1.uniquechar(testString))        
    testString = "abcdefabcdef"
    print("Return value is ",s1.uniquechar(testString))
    testString = "abcdefabef"
    print("Expect \"c\" Return value is ",s1.uniquechar(testString))

