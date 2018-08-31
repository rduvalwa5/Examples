#!/usr/local/bin/python

import glob
import os
import sys

def find_dir_files(dir,path, sTxt):
        listDirs = []
        print(dir,  path)
        ListFiles = []
        ListOfSearchSuccess = []
        print('find ', sTxt , (path + "/" + dir))
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
        print("files ",ListFiles)
        for fi in ListFiles:
            f = open(fi,"r")
            if sTxt in f.read():
                print(sTxt + " in " + fi)
                ListOfSearchSuccess.append(fi)
                
        if len(ListOfSearchSuccess) > 0:
                return  ListOfSearchSuccess
        else:
                msg = sTxt + " not found in any file" 
                return msg
 
if __name__ == "__main__":

#    print(find_dir_files(sys.argv[1],sys.argv[2], sys.argv[3]))
    print(find_dir_files("Python_Utilities","/Users/rduvalwa2","os.walk"))
