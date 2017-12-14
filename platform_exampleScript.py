'''
Created on Feb 15, 2017
@author: rduvalwa2
https://docs.python.org/2/library/platform.html
'''
import os, sys, platform


"""
sys.platform
System            platform value
    Linux            'linux'
    Windows          'win32'
    Windows/Cygwin   'cygwin'
    Mac OS X         'darwin'
"""
print("platform is sys.platform ", sys.platform)

"""
Python version
"""
print("python version",platform.python_version())
print("version tuple ",platform.python_version_tuple())

"""
platform release
"""
print("release ", platform.release())
"""
platform system
"""
print(platform.system())
print(platform.system_alias(platform.system(),platform.release(),platform.python_version()))
"""
platform.version
"""
print(platform.version())
"""
platform.uname
(system, node, release, version, machine, processor)
"""
print(platform.uname())
names = ['sysname', 'nodename', 'release', 'version','machine' ]
for i in range(0,5):
    print("num is ", i, names[i] , platform.uname()[i])
    
"""
Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being a tuple (vm_name, vm_release, vm_vendor) 
and osinfo being a tuple (os_name, os_version, os_arch). Values which cannot be determined are set to the defaults 
given as parameters (which all default to '').
"""
print("Java ",platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')))
print("Windos 32 ",platform.win32_ver(release='', version='', csd='', ptype=''))
print("Mac OSX ",platform.mac_ver(release='', versioninfo=('', '', ''), machine=''))
print("Unix  ", platform.dist(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', ...)))
print("Linux ", platform.linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', ...), full_distribution_name=1))

"""
Tries to determine the libc version against which the file executable (defaults to the Python interpreter) is linked. 
Returns a tuple of strings (lib, version) which default to the given parameters in case the lookup fails.
Note that this function has intimate knowledge of how different libc versions add symbols to the executable is probably only 
usable for executables compiled using gcc.
The file is read and scanned in chunks of chunksize bytes.
"""
print(platform.libc_ver(executable=sys.executable, lib='', version='', chunksize=2048))
