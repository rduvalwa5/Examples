'''
Created on Nov 25, 2015
@author: rduvalwa2
'''
import glob
import os

def os_env():
    """
        Get local environment and return it
    """
    env = os.environ
#    print("env \n" , env)
    return(env)


if __name__ == "__main__":
#    import os_env
    thisEnv =  os_env()
    print(thisEnv,'\n')
    print(thisEnv['PWD'])
    print(thisEnv['_'])
    print(thisEnv['HOME'])
    print(thisEnv['JAVA_HOME'])
    print(thisEnv['LOGNAME'])
    
    
    
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