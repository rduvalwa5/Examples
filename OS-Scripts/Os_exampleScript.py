'''
Created on Feb 15, 2017
@author: rduvalwa2
https://docs.python.org/3/library/os.html#
'''
import os, sys

'''
posix, nt, java
'''
print("os type is os.name ",os.name)
'''
System    platform value
Linux    'linux'
Windows    'win32'
Windows/Cygwin    'cygwin'
Mac OS X    'darwin'
'''
print("platform is sys.platform ", sys.platform)
print("host name is os.uname()[1] ",os.uname()[1])
print("os.termid ",os.ctermid())
"""
os.environ
"""
print("os.environ ",os.environ)
osList = ['PATH','PYTHONPATH','SHELL','PYDEV_CONSOLE_ENCODING','APP_ICON_20207','PYTHONIOENCODING','USER','TMPDIR','JAVA_STARTED_ON_FIRST_THREAD_20207','SSH_AUTH_SOCK','PYTHONUNBUFFERED','XPC_FLAGS','__CF_USER_TEXT_ENCODING','Apple_PubSub_Socket_Render','LOGNAME','PYDEV_COMPLETER_PYTHONPATH','XPC_SERVICE_NAME','HOME']
for i in range(0,len(osList)):
    att = osList[i]
    print(att , os.environ[att])
"""
os.environb
"""
print(os.environb)
print(os.environb[b'PATH'])

names = ['sysname', 'nodename', 'release', 'version','machine' ]
for i in range(0,5):
    print("num is ", i, names[i] , os.uname()[i])

"""
https://docs.python.org/3/library/os.html#os-file-dir
os.chdir()
os.getcwd()
"""
path = '/Users/rduvalwa2/Documents'
os.chdir(path)
print("os.getcwd() ",os.getcwd())

"""
os.chflags(path, flags, *, follow_symlinks=True)
https://docs.python.org/3/library/stat.html#module-stat
"""


"""
os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
https://docs.python.org/3/library/stat.html#module-stat
"""

"""
os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
"""

"""
os.chroot(path)
"""