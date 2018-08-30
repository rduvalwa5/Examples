#!/usr/local/bin/python

import sys
import math

def hello(a,b):
    print ('hello and thats your sum:')
    result = a * b
    print (result)

if __name__ == "__main__":
    hello(int(sys.argv[1]), int(sys.argv[2]))
