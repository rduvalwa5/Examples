'''
Created on Mar 27, 2015
https://docs.python.org/2/library/array.html?highlight=array#module-array
typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
Type code    C Type    Python Type    Minimum size in bytes
-- 'c'    char    character    1
'b'    signed char    int    1
'B'    unsigned char    int    1
'u'    Py_UNICODE    Unicode character    2 (see note)
'h'    signed short    int    2
'H'    unsigned short    int    2
'i'    signed int    int    2
'I'    unsigned int    long    2
'l'    signed long    int    4
'L'    unsigned long    long    4
'f'    float    float    4
'd'    double    float    8
class array.array(typecode[, initializer])
A new array whose items are restricted by typecode, and initialized from the optional initializer value, which must be a list,
 string, or iterable over elements of the appropriate type.

@author: rduvalwa2
'''
from array import *
from test.test_sys_settrace import raises

class arrayTypes:
    
    '''
    Demonstrates array creation    
    '''
    def createArray(self,theType,inList):
        print("in method")
        '''
        for member in inList:
            type(member)
            if not isinstance(member, type(theType)):
                return TypeError
                break
        '''
        anArray = array(theType,inList) # u is unicode character of size 2 bytes
        for item in anArray:
                print(item)
        return anArray
    
    def createFreeArray(self,theType,inList):
        print("in method")
        anArray = array(theType,inList) # u is unicode character of size 2 bytes
        for item in anArray:
                print(item)
        return anArray
    
if __name__ == '__main__':
#    import arrayTypes
    aa = arrayTypes()
    myList = ['a','b','c']
    myType = 'u'
    ch = array('u',myList)
    print("the list", myList)
#    print(arrayTypes.charArray(myList)) #

    print("ch is ",ch)
#    ch(['a','b','c']) 
    for c in ch:
        print(c , type(c))
    aray = aa.createArray(myType, myList)
    print(aray)

    myList = ['a','b','c',1]
    print(aa.createArray(myType, myList))
    
  
