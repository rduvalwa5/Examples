'''
Created on May 31, 2015
...    data driven example
...    pybot py_string_test_data_driven.txt
...    keyword driven example
...    pybot py_string_test_keyword_example.txt
@author: rduvalwa2
'''
#from PyString import py_string
from PyString import py_string

class PyStringLibrary(object):
    """Test library for testing Calculator business logic.

    Interacts with the calculator directly using its `push` method.
    """

    def __init__(self):
        self._pystring = py_string()
        self._result = ''

    def make_upper(self,text):
        """ Takes string in and returns upper case 
            version of that String      
            Example:
            |Make Upper  | abc |
        """
        self._result = self._pystring.makeUpper(text)
        return self._result
    
    def make_lower(self,text):
        """ Takes string in and returns upper case 
            version of that String
            Example:
            |Make Lower  | ABC |
        """
        self._result = self._pystring.makeLower(text)
        return self._result
    
    def make_reverse(self,text):
        """ Takes string in and returns upper case 
            version of that String
            Example:
            |Make Lower  | ABC |
        """
        self._result = self._pystring.reverse(text)
        return self._result
    
    def result_should_be(self, expected):
        """Verifies that the current result is `expected`.
        Example:
        | Ret Upper     | abc |
        | Result Should Be | ABC  |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))
        
