'''
Created on Mar 20, 2013
Example of a Python generator
Generators functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
@author: rduvalwa2
'''
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
sum_of_first_n = sum(firstn(12))
print(type(sum_of_first_n))
print(sum_of_first_n)