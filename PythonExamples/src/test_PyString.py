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
        inpt = "one two three four five.  four five six."
        expected = "One two three four five.  four five six."
        self.assertEqual(expected,s1.makeCaps(inpt))
        
    def testSplitString(self):
        s1 = PyString.py_string()
        inpt = "one two three four five.  Six seven eight?"
        expected = ['one', 'two', 'three', 'four', 'five.', '', 'Six', 'seven', 'eight?']
        self.assertEqual(expected, s1.splitString(inpt, " "))
        
    def testStrngJoin(self):
        s1 = PyString.py_string()
        separator = "+"
        seq = ("one","two","three","four")
        expected = "one+two+three+four"
        self.assertEqual(expected,s1.stringJoin(separator,seq))
        
    def testStringReplace(self):
        s1 = PyString.py_string()
        original = "two"
        replacement = "twelve"
        maxreplace = 2
        text = "one two three four five two.  Six seven eight two?"
        expected = "one twelve three four five twelve.  Six seven eight two?"
        self.assertEqual(expected,s1.stringReplace(text, original, replacement, maxreplace))
        
if __name__ == "__main__":
    unittest.main()