'''
Created on Aug 13, 2016

This class is for managing environment variables.

https://docs.python.org/3/library/os.html#os.open
This module provides a portable way of using operating system dependent functionality. 
    If you just want to read or write a file see open(), 
    if you want to manipulate paths, see the os.path module, and 
    if you want to read all the lines in all the files on the command line see the fileinput module. 
    For creating temporary files and directories see the tempfile module, 
    and for high-level file and directory handling see the shutil module.
@author: rduvalwa2
'''
import os

class Manage_Variables:

    def get_env_varibles(self):
        '''
        Os Misc
        '''
        varKeys = []
        for key in os.environ:
            varKeys.append(key)
        return varKeys
        
    def is_var_exist(self,var):
        '''
        https://docs.python.org/3/library/os.html
        A mapping object representing the string environment. For example, environ['HOME'] is the pathname of 
        your home directory (on some platforms), and is equivalent to getenv("HOME") in C.
        '''
        if var in self.get_env_varibles():
            print(var)
            return True
        else:
            return False
        
    def put_environment_variable(self,key,value):
        print('trying to set ', key)
        keyResult = os.getenv(key, default=False)
        print('result ', keyResult)
        if self.is_var_exist(key) == False:
                os.environ.update({key:value})
#                print("JavaHome ",os.environ)
        else:
            print('key exist ', os.getenv(key, default=None))
            
    def delete_variable(self,key):
        if key in os.environ: 
            del os.environ[key]
        else:
            print('key does not exist ', os.getenv(key, default=None))
        
    def update_variable_value(self,key,value):
        if key in os.environ: 
                os.environ.update({key:value})
        else:
            print('key does not exist ', os.getenv(key, default=None))
                    
    def get_variable_value(self,key):
        if key in os.environ: 
                return os.getenv(key, default=None)
        else:
            print('key does not exist ', os.getenv(key, default=None))  
            return    'key does not exist '       
        
if __name__ == '__main__':
    testKey = 'JAVA_HOME'
    testValue = '/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home'
    updateValue = '/Java/bin'
    a = Manage_Variables()
    print(a.is_var_exist('USER'))
    print(a.get_env_varibles())
    a.put_environment_variable(testKey, testValue)
    print (testKey + ' exist ',a.is_var_exist(testKey))
    print(a.get_variable_value(testKey))
    a.update_variable_value(testKey, updateValue)
    print(a.get_variable_value(testKey))
    if testKey in os.environ: 
        del os.environ[testKey]
    print ('getenv ' + testKey, os.getenv(testKey))
    