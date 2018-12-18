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
os.getgrouplist OSError
[20, 401, 12, 61, 79, 80, 81, 98, 398, 101, 704, 701, 702, 33, 100, 204, 250, 395, 703]

OSXAir:Examples rduvalwa2$ groups rduvalwa2
staff com.apple.access_remote_ae everyone localaccounts _appserverusr admin _appserveradm _lpadmin com.apple.access_screensharing com.apple.access_ssh-disabled com.apple.sharepoint.group.4 com.apple.sharepoint.group.1 com.apple.sharepoint.group.2 _appstore _lpoperator _developer _analyticsusers com.apple.access_ftp com.apple.sharepoint.group.3
OSXAir:Examples rduvalwa2$ groups
staff com.apple.access_remote_ae everyone localaccounts _appserverusr admin _appserveradm _lpadmin com.apple.access_screensharing com.apple.access_ssh-disabled com.apple.sharepoint.group.4 com.apple.sharepoint.group.1 com.apple.sharepoint.group.2 _appstore _lpoperator _developer _analyticsusers com.apple.access_ftp com.apple.sharepoint.group.3
OSXAir:Examples rduvalwa2$ id
uid=503(rduvalwa2) gid=20(staff) groups=20(staff),401(com.apple.access_remote_ae),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),398(com.apple.access_screensharing),101(com.apple.access_ssh-disabled),704(com.apple.sharepoint.group.4),701(com.apple.sharepoint.group.1),702(com.apple.sharepoint.group.2),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),703(com.apple.sharepoint.group.3)
OSXAir:Examples rduvalwa2$ 
'''
try:
    print(os.getgrouplist('rduvalwa2', 20))
except OSError:
    print("os.getgrouplist OSError")
except TypeError:
    print("os.getgrouplist TypeError: getgrouplist() takes exactly 2 arguments (1 given)")
    
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
