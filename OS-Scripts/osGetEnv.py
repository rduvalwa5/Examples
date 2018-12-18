'''
Created on Dec 17, 2018

@author: rduvalwa2

os.environ
A mapping object representing the string environment. For example, environ['HOME'] is the pathname of your home directory 
(on some platforms), and is equivalent to getenv("HOME") in C.
This mapping is captured the first time the os module is imported, typically during Python startup as part of processing site.py. 
Changes to the environment made after this time are not reflected in os.environ, except for changes made by modifying os.environ 
directly.
If the platform supports the putenv() function, this mapping may be used to modify the environment as well as query the 
environment. putenv() will be called automatically when the mapping is modified.

On Unix, keys and values use sys.getfilesystemencoding() and 'surrogateescape' error handler. Use environb if you would like to 
use a different encoding.

Note Calling putenv() directly does not change os.environ, so it’s better to modify os.environ.
Note On some platforms, including FreeBSD and Mac OS X, setting environ may cause memory leaks. Refer to the system documentation 
for putenv().
If putenv() is not provided, a modified copy of this mapping may be passed to the appropriate process-creation functions to cause
 child processes to use a modified environment.

If the platform supports the unsetenv() function, you can delete items in this mapping to unset environment variables. unsetenv() 
will be called automatically when an item is deleted from os.environ, and when one of the pop() or clear() methods is called.

os.environb
Bytes version of environ: a mapping object representing the environment as byte strings. environ and environb are synchronized 
(modify environb updates environ, and vice versa).

environb is only available if supports_bytes_environ is True.

os.getenv(key, default=None)
Return the value of the environment variable key if it exists, or default if it doesn’t. key, default and the result are str.

On Unix, keys and values are decoded with sys.getfilesystemencoding() and 'surrogateescape' error handler. Use os.getenvb() 
if you would like to use a different encoding.

Availability: most flavors of Unix, Windows.

os.getenvb(key, default=None)
Return the value of the environment variable key if it exists, or default if it doesn’t. key, default and the result are bytes.

getenvb() is only available if supports_bytes_environ is True.

'''
import os

print("os.env: ", os.environ())

#print("getenv: ", os.getenv('PATH'))

#print("getenvb: ", os.getenvb("PATH"))