'''
Created on Apr 14, 2021
Synchronization between processes
multiprocessing contains equivalents of all the synchronization primitives from threading. For instance one can use a 
lock to ensure that only one process prints to standard output at a time:
@author: rduvalwa2
'''
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()