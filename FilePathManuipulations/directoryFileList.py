#!/usr/local/bin/python

import glob
import os
import sys

def find_dir_files(dir,path):
        listDirs = []
        print(dir,  path)
        ListFiles = []
        print('find ', (path + "/" + dir))
        for root, dirs, files in os.walk(path, topdown=False):
                for name in dirs:
                        if os.path.isdir(os.path.join(root, name)):
                            listDirs.append(name)
        if dir in listDirs:
            print("found ", dir)
            newPath = os.path.join(root, dir)
            for root, dirs, files in os.walk(newPath, topdown=False):
                for f in files:
                    if os.path.isfile(os.path.join(root, f)):
                        ListFiles.append(root + "/" + f)     
#        print("files ",ListFiles) 
        return  ListFiles    
 
if __name__ == "__main__":

#    uncomment below and comment out the next line to make a command line run script
#    print(find_dir_files(sys.argv[1],sys.argv[2]))
    print(find_dir_files("Python_Utilities","/Users/rduvalwa2"))