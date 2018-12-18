'''
Created on Nov 25, 2015
@author: rduvalwa2
'''
import glob
import os
# import os
from os.path import join, getsize
    
def os_env():
    """
        Get local environment and return it
    """
    env = os.environ
#    print("env \n" , env)
    return env

def get_os_name():
    return os.name

def get_cpu_count():
    cpus = os.cpu_count()
    return cpus

def get_cur_dir():
    current_dir =  os.curdir
    return  current_dir

def number_of_bytes_in_directories():
#    import os
#    from os.path import join, getsize
    for root, dirs, files in os.walk('../'):
        print (root, "consumes")
        print (sum(getsize(join(root, name)) for name in files))
        print ("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

def list_files_in_directories(path = '../'):
    # http://www.tutorialspoint.com/python/os_stat.htm
    for root, dirs, files in os.walk(path):
        print (root)
        print ("Python File Attributes")
        print("\t","File",":",":","Mode",":","Size",":","Device",":","Userid",":","Group",":","Access_time",":","last_modtifiction","Meta Change")
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
            print("\t", name, ":",":",file_mode,":",file_size,":",device,":",file_userid,":",file_group,":",file_access_time,":",file_last_mod,":", file_meta_chg)

if __name__ == "__main__":
    thisOs = os
    thisEnv =  os_env()
    print(thisEnv,'\n')
    print(thisOs.getcwd())
#    print(thisEnv['_'])
    print(thisEnv['HOME'])
#    print(thisEnv['JAVAHOME'])
    print(thisEnv['LOGNAME']) 
    print("Should be posix ", get_os_name())
    print("CPU count ", get_cpu_count())
    print("Current directory", get_cur_dir(), "\n")
    
    number_of_bytes_in_directories()
    print("list_files_in_directories \n")
    list_files_in_directories()
    
'''
C1246895-Air:src rduvalwa2$ python3.5 Os_examples.py
environ({
'ANT_HOME': '~/Ant/bin', 
'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.KX1MxshOjP/Listeners', 
'GLASSFISH_HOME': '/usr/local/glassfish4-3/bin',
'XPC_SERVICE_NAME': '0', 
'TMPDIR': '/var/folders/yv/dbpkqmlj30b5h2f7xxvn1fw40000gq/T/', 
'LANG': 'en_US.UTF-8', 'SHELL': '/bin/bash', 'XPC_FLAGS': '0x0', 
'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.wvH288mh0u/Render', 
'OLDPWD': '/Users/rduvalwa2/new_git/File_Handling', 
'TERM': 'xterm-256color', 
'TERM_PROGRAM': 'Apple_Terminal', 
'LOGNAME': 'rduvalwa2', 
'SHLVL': '1', 
'__PYVENV_LAUNCHER__': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 
'PWD': '/Users/rduvalwa2/new_git/File_Handling/src', 
'_': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 
'MAVEN_HOME': '/usr/bin', 
'HOME': '/Users/rduvalwa2', 
'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home', 
'PATH': '/Library/Frameworks/Python.framework/Versions/3.5/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/git/bin:/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home:~/Ant/bin:/usr/local/glassfish4-3/bin', '__CF_USER_TEXT_ENCODING': '0x1F7:0x0:0x0', 'TERM_SESSION_ID': 'DEB6163D-995E-4E2F-8B38-42DB9E920438', 'USER': 'rduvalwa2', 'TERM_PROGRAM_VERSION': '361'})

/Users/rduvalwa2/new_git/File_Handling/src
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
/Users/rduvalwa2
/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home
rduvalwa2
C1246895-Air:src rduvalwa2$ 


'''