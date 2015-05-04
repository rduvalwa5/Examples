'''
Created on May 3, 2015
@author: rduvalwa2
'''
import unittest
from reverseString import py_string
'''
    global class variable
'''
testString = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
expected = 'ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa'
s1 = py_string()

class Test(unittest.TestCase):
    
    def testRecursiveRevervse(self):
        self.assertEqual(expected, s1.reverse(testString), "Reverse failed")
        
    def testSimpeRevervse(self):
        self.assertEqual(expected, s1.reverseSimple(testString), "Reverse Simple failed")
        
    def testRevervseAsList(self):
        self.assertEqual(expected, s1.reverseList(testString), "Reverse as List failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()