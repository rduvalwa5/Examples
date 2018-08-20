'''
Created on Aug 10, 2018

@author: RDuval

https://stackoverflow.com/questions/27196143/get-file-attributes-hidden-readonly-system-archive-in-python

https://docs.python.org/3/library/os.path.html
https://www.w3resource.com/python-exercises/python-basic-exercise-107.php
'''
import glob
import os
import time

class getFile:
    def __init__(self, path = ".", typ = "py"):
        self.path = path
        self.fileStats = []
        self.foundFiles = []
        self.fileSplits=[]
        self.directories = []
        self.ListFiles = []
        self.fileType = typ
        
    def get_File(self,path="."):
        print("path ", self.path)
        allFiles = glob.glob(os.path.join(self.path,"*"))
        print(allFiles)
        for file in allFiles:
            if os.path.isfile(file):
                try:
                    self.foundFiles.append(file)
                except IOError:
                    print(file, " file not found")
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
            

    def get_file_by_type(self, typ):
        listByType = []
        fileList = self.get_File_Split()
        for fil in fileList:
            if typ in fil:
                listByType.append(fil)
                
        if len(listByType) == 0:
                notFoundMessage = "No file of type " + typ + " found."
                return notFoundMessage
        else:   
                return listByType

    def file_Split(self):
        for file in glob.glob(os.path.join(self.path,"*")):
                print(os.path.split(file))

    def walk_directory(self,path):
        '''
        https://www.tutorialspoint.com/python/os_walk.htm
        '''
        # listMusicDirecories
        print('Start walk!')
        for root, dirs, files in os.walk(path, topdown=True):
            for name in dirs:
#                print(os.path.join(root, name))
                if os.path.isdir(os.path.join(root, name)):
                        self.directories.append(name)
            for name in files:
                if os.path.isfile(os.path.join(root, name)):
                    if self.fileType in name:
                        self.ListFiles.append(name)
        print("Directories",self.directories)
        print("files ",self.ListFiles)
                                              


 
if __name__ == '__main__':
    import platform
    
    print("Node :", platform.uname().node)
    if (platform.uname().node == 'C1246895-XPS'):
            getFileObj = getFile("C:\\Users\\RDuval.C1246895-XPS\\git\PyExamples\\FilePathManuipulations\\","txt")
    else:
            getFileObj = getFile("/Users/rduvalwa2/Desktop","sql")
        
    filwTypeFailed = "txt"
    getFileResult = getFileObj.get_File()
    print("getFileResult", getFileResult)
    
    getStats = getFileObj.get_File_stats()
    print("getStats",getStats)
    
    getSplits = getFileObj.get_File_Split()
    print("getSplits", getSplits)
    
    getFileObj.get_Specific_File(".\getFileTypes.py")
    getFileObj.get_Specific_File("getFileTypes.py")
    
    fileType = "py"
    pyTypeFiles = getFileObj.get_file_by_type(fileType)
    print(pyTypeFiles)
    
    fileType = "txt"
    failedFindType = getFileObj.get_file_by_type(fileType)
    print(failedFindType)
    
    fileType = "Windows"
    WinFindType = getFileObj.get_file_by_type(fileType)
    print(WinFindType)
    
    getFileObj.file_Split()
    
    if (platform.uname().node == 'C1246895-XPS'):
            path = "C:\\Users\\RDuval.C1246895-XPS\\git\PyExamples"
    else:
            path = "/Users/rduvalwa2/Desktop"
    getFileObj.walk_directory(path)