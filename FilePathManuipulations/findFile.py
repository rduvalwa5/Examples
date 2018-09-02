'''
findFile locates a file within a path and returns a list of locations and the number of files examined to find it.
'''
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
#    print(find_file(sys.argv[1],sys.argv[2]))

    if platform.uname().node == 'OSXAir.home.home':
        print(find_file("findFile.py","/Users/rduvalwa2/eOxigen-workspace/Examples"))
    elif platform.uname().node == 'C1246895-osx.home':
        print(find_file("findFile.py","/Users/rduvalwa2/python_workspace2017/Examples"))
    elif platform.uname().node ==  'C1246895-XPS':    
        print(find_file("findFile.py","C:\\Users\\RDuval.C1246895-XPS\\git\\PyExamples"))
    else: 
        print(find_file("findFile.py","/Users/rduvalwa2/eOxigen-workspace/Examples"))
    
    '''
    (['/Users/rduvalwa2/python_workspace2017/Examples/FilePathManuipulations/findFile.py', 332], 441)

    '''