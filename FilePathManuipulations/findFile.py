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
#                print(fileCount, "  " , f) # , "  ", root)            
                if os.path.isfile(os.path.join(root, f)):
                    if f == fil:
                        ListFiles.append(root + "/" + f) 
                        ListFiles.append(fileCount)     
        return (ListFiles, fileCount)
 
if __name__ == "__main__":
    import platform
    print(find_file(sys.argv[1],sys.argv[2]))
#    print(find_file("hosts.txt","/Users/rduvalwa2/"))


'''
findFile locates a file within a path and returns a list of locations and the number of files examined 
to find it.

OSXAir:Python_Utilities rduvalwa2$ ./findFile.py "hosts.txt" "/Users/rduvalwa2/"
('find ', 'hosts.txt', ' in ', '/Users/rduvalwa2/')
(['/Users/rduvalwa2//hosts.txt', 23, '/Users/rduvalwa2/Workspace/hosts.txt', 135461, '/Users/rduvalwa2/Public/hosts.txt', 225931, '/Users/rduvalwa2/Public/Magic/hosts.txt', 225944], 345277)
OSXAir:Python_Utilities rduvalwa2$ 
    '''