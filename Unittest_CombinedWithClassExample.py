'''
Created on Jun 1, 2013
Simple bunch class
This class does two things:
1) demonstrate argument input
2) demonstrate raise Attribute Error with out try
3) demonstrate Unit Test within the same file as the class
@author: rduvalwa2
'''
#import unittest

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            else:
                setattr(self, key, value)
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text

        
if __name__ == "__main__":
#    b = Bunch(name="Python 3", language="Python 3.0.1")
#    print(b.name)
#    print(b.language)
#    print(b.__dict__)
    import unittest
    class TestBunch(unittest.TestCase):
        def test_attributes(self):
            b = Bunch(name="Python 3", language="Python 3.0.1")
            self.assertEqual("Python 3", b.name)
            self.assertEqual("Python 3.0.1", b.language)

    unittest.main()
