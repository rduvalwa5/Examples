'''
Created on Oct 23, 2017
@author: rduvalwa2

get file type from specified directory
'''

import os,sys

class get_file_type():
    def __init__(self, root = '.',typ = 'txt'):
        self.path = root
        self.spec_dirs = os.listdir(self.path)
#        print(self.spec_dirs)
        self.path = root
        self.returnedSpecifiedPathDirs = []
        self.returnedSpecifiedPathFiles = []
        self.directories = []
        self.ListFiles = []
        self.fileType = typ

    def get_directory_specific(self):
#        dirs = os.listdir( self.path )
        for file in self.spec_dirs:
            if os.path.isdir(self.path + '/' + file):
                if ".DS_Store" in file or ".com.apple" in file:
                    continue
                else:
#                    print(file)
                    self.returnedSpecifiedPathDirs.append(file)
        return self.returnedSpecifiedPathDirs
                    
        
    def get_onlyFilesInDirecotry(self):
        for file in self.spec_dirs:
            if os.path.isfile(self.path + '/' + file):
                if ".DS_Store" in file or ".com.apple" in file:
                    continue
                else:
#                    print(file)
                    self.returnedSpecifiedPathFiles.append(file)
        return self.returnedSpecifiedPathFiles

    def get_onlyFilesTypesInDirecotry(self):
        returnedFilesTypes = []
        for file in self.spec_dirs:
            if os.path.isfile(self.path + '/' + file):
                if ".DS_Store" in file or ".com.apple" in file:
                    continue
                else:
#                    print(file)
                    if self.fileType in file:
                        returnedFilesTypes.append(file)
        return returnedFilesTypes 
        
    def walk_directory(self):
        '''
        https://www.tutorialspoint.com/python/os_walk.htm
        '''
        # listMusicDirecories
        print('Start walk!')
        for root, dirs, files in os.walk(self.path, topdown=True):
            for name in dirs:
#                print(os.path.join(root, name))
                if os.path.isdir(os.path.join(root, name)):
                        self.directories.append(name)
        for name in files:
                if os.path.isfile(os.path.join(root, name)):
                    if self.fileType in name:
                        self.ListFiles.append(name)

if __name__ == '__main__':
    pathWithFilesOnly = '/Users/rduvalwa2/Desktop/SafeItems'
    pth = '/Users/rduvalwa2/Desktop'
    print('input path: ',pth)
    t = 'jpg'
    
    
    fDir = get_file_type(pth,t)
    fDir.walk_directory()
    

    print("specif directories: ")
    for dd in fDir.get_directory_specific():
        print(dd)
        
    for ff in fDir.get_onlyFilesInDirecotry():
        print(ff)
    
    print('\n Only files types')    
    for ft in fDir.get_onlyFilesTypesInDirecotry():
        print(ft)
'''
    print('Directories are: ')
    for d in fDir.directories:
        print(d)
        
    print("Files are:")    
    for f in fDir.ListFiles:
        print(f)
    '''