'''
Created on Aug 10, 2016
    https://docs.python.org/3/library/os.path.html
@author: rduvalwa2
'''

import os

class os_env:
    '''
    URL:  https://docs.python.org/3/library/os.path.html
    Functions:
    os.path.abspath(path)         os.path.basename(path)    os.path.commonpath(paths)
    os.path.commonprefix(list)    os.path.dirname(path)     os.path.exists(path)
    os.path.lexists(path)         os.path.expanduser(path)  os.path.expandvars(path)
    os.path.getatime(path)        os.path.getmtime(path)    os.path.getctime(path)
    os.path.getsize(path)         os.path.isabs(path)       os.path.isfile(path)
    os.path.isdir(path)           os.path.islink(path)      os.path.ismount(path)
    os.path.join(path,*paths)     os.path.normcase(path)    os.path.normpath(path)
    os.path.realpath(path)        os.path.relpath(path,start=os.curdir)
    os.path.samefile(path1,path2) os.path.sameopenfile(fp1, fp2)
    os.path.samestat(stat1,stat2) os.path.split(path)       os.path.splitdrive(path)
    os.path.splitext(path)        os.path.splitunc(path)
    Deprecated since version 3.1: Use splitdrive instead.
    os.path.supports_unicode_filenames¶
    '''


    def get_expandvars(self,path):
        '''
        os.path.expandvars(path)
        Return the argument with environment variables expanded. Substrings of the form $name or ${name} are 
        replaced by the value of environment variable name. Malformed variable names and references to 
        non-existing variables are left unchanged.
        On Windows, %name% expansions are supported in addition to $name and ${name}.
        '''
        return  os.path.expandvars(path)
         
    def print_docstring(self):
        '''
        print_docstring()
        https://www.python.org/dev/peps/pep-0257/
        Python documentation strings (or docstrings) provide a convenient way of
        associating documentation with Python modules, functions, classes, and methods. 
        Example:
        print (my_function.__doc__)
            '''
        return  self.__doc__
    
    def get_env_varibles(self):
        '''
        def get_env_varibles`
        get environment variables using os.environ
        '''
        varKeys = []
        for key in os.environ:
            varKeys.append(key)
        return varKeys
        
    def env_var_exist(self,var):
        '''
        env_var_exist
        verify environment variable exist
        a.env_var_exist('HOME')
        '''
        variables = os.environ
#        if var in self.get_env_varibles():
        if var in variables:
            print(var)
            return True
        else:
            return False

    def set_env_varible(self,name, value):
        '''
        https://docs.python.org/3/library/os.html
        Example: os.environ["DEBUSSY"] = '1'
        '''
        os.environ[name] = value
        
    def unset_subproc_var(self,name): 
        '''
        os.unsetenv(key)
        Unset (delete) the environment variable named key. Such changes to the environment affect subprocesses started with os.system(), 
        popen() or fork() and execv().
        When unsetenv() is supported, deletion of items in os.environ is automatically translated into a corresponding call to 
        unsetenv(); however, calls to unsetenv() don’t update os.environ, so it is actually preferable to delete items of os.environ.   
        '''
        os.unsetenv(name)
    
    def unset_env_variable(self,name):
        '''
            os.environ.pop("PYTHONHOME")
            del(os.environ["PYTHONHOME"])
        '''
        os.environ.pop(name)

        
if __name__ == '__main__':
    a = os_env()
    print('expandvars $HOME/Documents', a.get_expandvars('$HOME/Documents'))
    print('expandvars $USER', a.get_expandvars('$USER'))
    print('expandvars $SHELL', a.get_expandvars('$SHELL'))
    
    print('Does HOME exist',a.env_var_exist('HOME'))
    print('Does JAVA_HOME exist', a.env_var_exist('JAVA_HOME'))
    a.set_env_varible("JAVA_HOME", "/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home")
    print('Does JAVA_HOME exist Now', a.env_var_exist('JAVA_HOME'))
    print('Does PWD exist', a.env_var_exist('PWD'))
    eKeys = a.get_env_varibles()
    for key in eKeys:
        print(key  , a.get_expandvars('$' + key))
    
    a.unset_subproc_var("JAVA_HOME")
    print('Does JAVA_HOME exist now, should be true', a.env_var_exist('JAVA_HOME'))
    a.unset_env_variable("JAVA_HOME")
    print('Does JAVA_HOME exist now, should be false', a.env_var_exist('JAVA_HOME'))
    a.print_docstring()
    print(a.get_env_varibles.__doc__)