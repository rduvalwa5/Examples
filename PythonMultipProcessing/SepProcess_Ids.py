'''
Created on Apr 14, 2021

@author: rduvalwa2
'''
import os
from multiprocessing import Pool

def f():
    response = os.system('ps')
    print(response)

if __name__ == '__main__':
    with Pool(5) as p:
#        print(p.map(f, [1, 2, 3]))
        f()

#for hostname in hostnames:
#    response = os.system('nslookup ' + hostname)
#    print(response)
