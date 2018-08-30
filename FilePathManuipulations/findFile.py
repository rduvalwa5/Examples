#!/usr/local/bin/python

import glob
import os
import sys


def find_file(fil,path):
        ListFiles = []
        print('find ', fil)
        for root, dirs, files in os.walk(path, topdown=True):
#            print(files.__len__())
            for f in files:
                if os.path.isfile(os.path.join(root, f)):
#                    print(root)
                    if f == fil:
                        ListFiles.append(root + "/" + f)     
#        print("files ",self.ListFiles)
#        print("Total files ",self.ListFiles.__len__())
        return ListFiles

 
if __name__ == "__main__":

#    fil = sys.argv[1]
#    path = sys.argv[2]
    print(find_file(sys.argv[1],sys.argv[2]))
    
    