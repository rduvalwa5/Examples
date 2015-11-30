'''
Created on Nov 3, 2012
this program takes as a parameter a directory path for archiving
it then archives only the files in that directory
pyArchive(String directory path)
returns the archive
@author: rduvalwa2
'''
import os, glob, zipfile

def pyArchive(directoryPath):
    currentPath = os.getcwd()
    fixPath = os.path.abspath(directoryPath)
    file_dir = os.path.split(fixPath)[1]
    os.chdir(os.path.split(fixPath)[0])
    archiveName = "archive.zip"
    zip_file = zipfile.ZipFile(archiveName, "w")
    fileNames = glob.glob(os.path.join(file_dir, "*"))
    for fn in fileNames:
            if os.path.isfile(fn):
                    zip_file.write(fn)
    zip_file.close()
    os.chdir(currentPath)
    return zip_file.namelist()
