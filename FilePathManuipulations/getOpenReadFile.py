#!/usr/local/bin/python

import glob
import os
import sys

def find_open_read_file(path, fil):
        ListFiles = []
        print('get file',fil , path)
        for root, dirs, files in os.walk(path, topdown=True):
                for name in files:
                        if os.path.isfile(os.path.join(root, name)):
#                            print(name)
                            if name == fil:
                                f = os.path.join(root, name)
                                ListFiles.append(f)
        if len(ListFiles) > 0:
            for fi in ListFiles:
                print(fi)
                f = open(fi,"r")
                print(f.read())
        else:
            print("File Not found")
 
if __name__ == "__main__":

    print(find_open_read_file(sys.argv[1],sys.argv[2]))
#    find_open_read_file("/Users/rduvalwa2/python_workspace2017","Os_exampleScript.py")
