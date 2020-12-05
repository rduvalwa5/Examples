'''
Created on Nov 30, 2020

@author: rduvalwa2
'''

class InitExample:
    def __init__(self):
        self.a = 1
        print("self a is ", self.a)
        
    def add_one(self):
        print("self.a in add one is ",self.a)
        self.a = 1 + self.a
        print("after adding one ",self.a)
        
    def printA(self):
        print("printA ",self.a)
        
if __name__ == '__main__':
    Ini = InitExample()
    Ini.printA()
    Ini.add_one()
    Ini.printA()