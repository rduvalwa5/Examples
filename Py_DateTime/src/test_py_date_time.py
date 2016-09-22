'''
Created on Sep 21, 2016

@author: rduvalwa2
'''
import unittest
import datetime
from py_date_time import SimpleDateTime

class Test_py_date_time(unittest.TestCase):
    '''
    print(simple.getWeekday(year, month, day))
    print(simple.getIsoWeekday(year, month, day))
    '''

    def setUp(self):
        global month
        month = 6
        global year
        year = 1951
        global day
        day = 12
        global testClass
        testClass = SimpleDateTime() 

    
    def test_getWeekday(self):
        expected = 'Tuesday'
        observed = testClass.getWeekday(year, month, day)
        self.assertEqual(expected, observed, 'Weekday is not Tuesday')

    def test_getIsoWeekday(self):
        expected = 'Tuesday'
        observed = testClass.getIsoWeekday(year,month,day)
        self.assertEqual(expected, observed, 'Weekday is not Tuesday')
        
    def test_getToday(self):
        expected = datetime.date.today()
        observed = testClass.getToday()
        self.assertEqual(expected, observed, 'Today is not ' + str(observed) + " should be " + str(expected))
        
    def test_getTodayFail(self):
#        expected = datetime.date.today()
        expectedFail = datetime.date(year,month, day)
#        print(str(expectedFail))
        observed = testClass.getToday()
        self.assertNotEqual(expectedFail, observed, 'Today is not ' + str(observed) + " should be " + str(expectedFail))        
        
if __name__ == "__main__":
    unittest.main()