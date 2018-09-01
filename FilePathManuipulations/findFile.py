#!/usr/local/bin/python

import glob
import os
import sys


def find_file(fil,path):
        ListFiles = []
        print('find ', fil, " in ", path)
        fileCount = 0
        for root, dirs, files in os.walk(path, topdown=True):
            for f in files:
                fileCount = fileCount + 1
                print(fileCount, "  " , f) # , "  ", root)            
                if os.path.isfile(os.path.join(root, f)):
                    if f == fil:
                        ListFiles.append(root + "/" + f) 
                        ListFiles.append(fileCount)    
 
        return (ListFiles, fileCount)
 
if __name__ == "__main__":

#    print(find_file(sys.argv[1],sys.argv[2]))
    print(find_file("findFile.py","/Users/rduvalwa2/python_workspace2017/Examples"))
    
    '''
    (['/Users/rduvalwa2/python_workspace2017/Examples/FilePathManuipulations/findFile.py', 332], 441)
    '''