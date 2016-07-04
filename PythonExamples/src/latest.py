'''
Created on Oct 28, 2012
latest.py
@author: rduvalwa2
'''
import glob
import os
import zipfile

def latest(num=1, path="."):
    files = glob.glob(os.path.join(path, "*"))
    dated_files = [(os.path.getmtime(fn),os.path.abspath(fn)) for fn in files]
    dated_files.sort()
    latest_files = [f for (d, f) in dated_files[-num:]]
    latest_files.reverse()
    return latest_files
"""
3. Analysis 
     A) latest() function a technique called "decorate-sort-undecorate"
         - file paths need to be sorted by date
             *  it builds a list of (date, filename) tuples
             *  Python can sort more easily
             *  the date is the "decoration", it isn't required in the result, even though it's necessary for sorting
             *  by default tuples are sorted into ascending order
                 -  paths of the most recent files will be located at the end
         -  revealed
             1.  files=glob.glob(os.path.join(path,"*"))
                      order is file.bak, files.new, files.old
             2.  decorated with file creation times
                  dated_files = [(os.path.getmtime(fn), os.path.abspath(fn)) for fn in files]
                       order  (2 sec ago, file.bak), (1 sec ago, file.new),(3 sec ago, file.old)
             3.  dated_files.sort()
                       order (3 sec ago, file.old), (2 sec ago, file.bak), (1 sec ago, file.new)
             4.  decorators removed
                  latest_files=[f for (d,f) in dated_files[-num:]]
                        order  file.old, file.bak, file.new
             5.  Reverse to put the most recent first
                  latest_files.reverse()
                         order  file.new, file.bak, file.old
      B) algorithm extracts just the filenames of the most recent files
            -  by using the negative index located in [for file_info in files_with_dates[-num:]] 
            -  -num makes it go backwards through values of num
            -  then reverses the result, placing the most recent files at the beginning
"""

def zip_latest(fn, num, path):
#    pass
    files_to_archive = latest(num,path)
    zf = zipfile.ZipFile(fn, "w", zipfile.ZIP_DEFLATED)
    for fn_to_archive in files_to_archive:
        zf.write(fn_to_archive)
    zf.close()
    