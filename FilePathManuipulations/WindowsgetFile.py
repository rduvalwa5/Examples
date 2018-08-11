'''
Created on Aug 10, 2018

@author: RDuval
'''
'''
Created on Aug 6, 2018

@author: RDuval
'''
'''
https://stackoverflow.com/questions/27196143/get-file-attributes-hidden-readonly-system-archive-in-python

https://docs.python.org/3/library/os.path.html
https://www.w3resource.com/python-exercises/python-basic-exercise-107.php
'''
import glob
import os
import time

class getFile:
    def __init__(self, path = "."):
        self.path = '.'
        self.fileStats = []
        self.foundFiles = []
        self.fileSplits=[]
        
    def get_File(self,path="."):
        allFiles = glob.glob(os.path.join(self.path,"*"))
        for file in allFiles:
            if os.path.isfile(file):
                self.foundFiles.append(file)
        return self.foundFiles

    def get_File_stats(self):
        for file in glob.glob(os.path.join(self.path,"*")):
            if os.path.isfile(file):
                self.fileStats.append((file, os.stat(file)))
        return self.fileStats

    def get_File_Split(self):
        for file in glob.glob(os.path.join(self.path,'*')):
                self.fileSplits.append(os.path.split(file)[1])
        return  self.fileSplits
 
    def get_Specific_File(self, fName):
        fileList = self.get_File_Split()
        print(fileList)
        if fName in fileList:
            print("Found ", fName)
        else:
            print(fName, " Not Found")
            
 
if __name__ == '__main__':
    getFileObj = getFile()
    getFileResult = getFileObj.get_File()
    print("getFileResult", getFileResult)
    
    getStats = getFileObj.get_File_stats()
    print("getStats",getStats)
    
    getSplits = getFileObj.get_File_Split()
    print("getSplits", getSplits)
    
    getFileObj.get_Specific_File(".\getFileTypes.py")
    getFileObj.get_Specific_File("getFileTypes.py")
