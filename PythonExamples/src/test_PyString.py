'''
Created on Mar 26, 2015
@author: rduvalwa2
'''
import PyString
import unittest

class Test_PyrString(unittest.TestCase):
    def testReverseSimple(self):
        s1 = PyString.py_string()
        inpt = "aBcDeF123"
        expected = "321FeDcBa"
        self.assertEqual(expected,s1.reverseSimple(inpt))
        
    def testReverse(self):
        s1 = PyString.py_string()
        inpt = "ZyXwVuTs9876"
        expected = "6789sTuVwXyZ"
        self.assertEqual(expected,s1.reverse(inpt))
        
    def testMakeUpper(self):
        s1 = PyString.py_string()
        inpt = "ZyXwVuTs9876"
        expected = "ZYXWVUTS9876"
        self.assertEqual(expected,s1.makeUpper(inpt))
        
    def testMakeLower(self):
        s1 = PyString.py_string()
        inpt = "ZyXwVuTs9876"
        expected = "zyxwvuts9876"
        self.assertEqual(expected,s1.makeLower(inpt))
        
    def testMakeCaps(self):
        s1 = PyString.py_string()
        inpt = "one two three four five."
        expected = "One two three four five."
        self.assertEqual(expected,s1.makeCaps(inpt))
if __name__ == "__main__":
    unittest.main()