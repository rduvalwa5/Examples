'''
Created on Dec 18, 2018
@author: rduvalwa2
python ./Os_GetFileAttributes.py "/Users/rduvalwa2/git"
'''
import os, sys
from os.path import join

class Os_GetFileAttributes:
    def __init__(self, path):
        self.mypath = path
        print("argument is ", self.mypath)
    
    def list_files_in_directories(self):
    # http://www.tutorialspoint.com/python/os_stat.htm
        for root, dirs, files in os.walk(self.mypath):
            print (root)
            print ("Python File Attributes")
            print("File",":",":","Mode",":","Size",":","Device",":","Userid",":","Group",":","Access_time",":","last_modtifiction","Meta Change")
            for name in files:
                file_info = os.stat(join(root, name))
                file_mode = file_info.st_mode
                file_size = file_info.st_size
                device =    file_info.st_dev
                file_userid = file_info.st_uid
                file_group = file_info.st_gid
                file_access_time = file_info.st_atime
                file_last_mod = file_info.st_mtime
                file_meta_chg = file_info.st_ctime
            print( name, ":",":",file_mode,":",file_size,":",device,":",file_userid,":",file_group,":",file_access_time,":",file_last_mod,":", file_meta_chg)

if __name__ == "__main__": 
    try:
        x = Os_GetFileAttributes(sys.argv[1])
        x.list_files_in_directories()
    except IndexError:
        print("IndexError encountered list out of range")
        exit