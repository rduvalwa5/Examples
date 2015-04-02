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
import unittest
from array_examples import arrayTypes
from array import array


class test_arrays(unittest.TestCase):
    
    def test_array_unicode(self):
        aType = 'u'
        l_List = ('a','b','c')
        aa = arrayTypes()
        theArray = aa.createArray(aType,l_List)
        for member in theArray:
            self.assertTrue(isinstance(member, str))
#            self.assertTrue(isinstance(member,(str,unicode)))

    def test_array_int(self):
        aType = 'i'
        l_List = (1,2,3)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, int))
            
    def test_array_signedLong(self):
        aType = 'l'
        l_List = (-1000000000,-20000000000,+300000000000,+4000000000000,-5000000000000000001)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, int))  
                     
    def test_array_UnsignedLong(self):
        aType = 'L'
        l_List = (1000000000001,200000000000001,3000000000000001,40000000000000001,5000000000000000001)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, int)) 
 
    def test_array_Float(self):
        aType = 'f'
        l_List = (0.1000000000001,0.200000000000001)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, float)) 
 
 
    def test_array_DoubleFloat(self):
        aType = 'd'
        l_List = (0.1000000000001,0.20000000000000000000000000000001)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, float)) 
 
    '''
    Overflow Error
    '''
    def test_array_UnsignedLongOverflowError(self):
        aType = 'L'
        l_List = (100000000001,50000000000000000011)
        aa = arrayTypes()
        self.assertRaises(OverflowError,aa.createFreeArray,aType,l_List)
#        print(aa.createFreeArray(aType,l_List))
                          
    def test_array_Short(self):
        aType = 'h'
        l_List = (-10001,+20002) #,200001,300001,400001,500001)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, int))   
            
    def test_array_UnsignedShort(self):
        aType = 'H'
        l_List = (10001,20002)
        aa = arrayTypes()
        theArray = aa.createFreeArray(aType,l_List)
        print("Array is ",theArray)
        for member in theArray:
            self.assertTrue(isinstance(member, int))                           
    '''
    Test raises TypeError
    https://docs.python.org/2/tutorial/errors.html
    http://stackoverflow.com/questions/2525845/proper-way-in-python-to-raise-errors-while-setting-variables
    '''
    def test_array_TypeError(self):
        aType = 'u'
        l_List = ('a','b','c',1)
        aa = arrayTypes()
        self.assertRaises(TypeError,aa.createArray,aType,l_List)

                       
if __name__ == "__main__":
    unittest.main()