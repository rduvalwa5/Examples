"""This program fileTypeCounter.py reads in:
   1. the files in the local directory into a list
   2. it then counts the type of files
   3.  finally it prints out a report of the file types and each type count
"""
import glob
import os

def fileTypeCounter(path="."):
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
