'''
https://www.w3resource.com/python-exercises/python-basic-exercise-107.php
'''
import glob
import os
#from numpy import size
import time

class filesAttributes:
    
    def fileTypeCounter(self,path="./"):
        counts =   {}  
        files = glob.glob(os.path.join(path, "*")) # get all files in path
        for file in files:
            if os.path.isfile(file):
                path_ext = os.path.splitext(file)
                if path_ext[1] in counts:
                    counts[path_ext[1]] += 1
                else:
                    counts[path_ext[1]] = 1
        print("File Extensions in:",os.path.abspath(path))         
        for i in counts:
                print(i,":", counts[i])
        return counts

    def get_File(self,path="."):
        foundFiles = []
        allFiles = glob.glob(os.path.join(path,"*"))
        for file in allFiles:
#            print(file)
            if os.path.isfile(file):
                foundFiles.append(file)
        return foundFiles

    def get_File_stats(self,path="."):
        fileStats=[]
        for file in glob.glob(os.path.join(path,"*")):
#            print(file)
            if os.path.isfile(file):
                fileStats.append((file, os.stat(file)))
        return fileStats
        
if __name__ == '__main__':
    pathFiles = '/Users/rduvalwa2/Music/iTunes/iTunes Media/Music/Alvin Lee/In Tennessee'
    extension = ".mp3"
    fileObj = filesAttributes()
    results = fileObj.fileTypeCounter(pathFiles)
    print(results)
    
#    for file in fileObj.get_File(pathFiles):
#        print(file,os.path.getsize(file), time.ctime(os.path.getmtime(file)))
    
#    for file in fileObj.get_File(pathFiles):
#        print(file, os.stat(file))
        
    fileStats =  fileObj.get_File_stats(pathFiles) 
    for stat in fileStats:
        print(stat)
        