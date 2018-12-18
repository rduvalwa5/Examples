'''
Created on Dec 17, 2018
OS library information 
@author: rduvalwa2



'''

import os

'''
os.get_exec_path(env=None)
Returns the list of directories that will be searched for a named executable, similar to a shell, when launching a process. env, 
when specified, should be an environment variable dictionary to lookup the PATH in. By default, when env is None, environ is used.
['/usr/bin', '/bin', '/usr/sbin', '/sbin']
'''
print(os.get_exec_path())

'''
os.getegid()
Return the effective group id of the current process. This corresponds to the “set id” bit on the file being executed 
in the current process
returned id 20
'''
print(os.getegid())

'''
os.geteuid()
Return the current process’s effective user id.
'''
print(os.geteuid())

'''
os.getgid()
Return the real group id of the current process.
'''
print(os.getgid())

'''
os.getgrouplist(user, group)
Return list of group ids that user belongs to. If group is not in the list, it is included; typically, group is specified 
as the group ID field from the password record for user.
'''
print(os.getgrouplist('rduvalwa2',1))

'''
os.getgroups()
Return list of supplemental group ids associated with the current process.
'''
print(os.getgroups())

'''
os.getlogin()
Return the name of the user logged in on the controlling terminal of the process. For most purposes, it is more useful to 
use getpass.getuser() since the latter checks the environment variables LOGNAME or USERNAME to find out who the user is, 
and falls back to pwd.getpwuid(os.getuid())[0] to get the login name of the current real user id.
'''
print(os.getlogin())

'''
os.getpgrp()
Return the id of the current process group.
'''
print(os.getpgrp())

'''
os.getpid()¶
Return the current process id.
'''
print(os.getpid())

'''
os.getppid()
Return the parent’s process id. When the parent process has exited, on Unix the id returned is the one of the init process (1), 
on Windows it is still the same id, which may be already reused by another process.
'''
print(os.getppid())
