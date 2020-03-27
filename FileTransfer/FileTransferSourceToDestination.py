'''
https://pypi.org/project/scp/

from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()

Created on Mar 21, 2020
@author: rduvalwa2
'''
#import paramiko
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

import os

sourceDir = r'/Users/rduvalwa2/test directory/'
#sourceDir2 = r'/Users/rduvalwa2/TestDirCopy/' cannot send directory
destDir = r'/Users/rduvalwa2/test directory/'
#destDir2 = r'/Users/rduvalwa2/TestDirCopy/' cannot send directory

#fileList = os.listdir(sourceDir)

port = 22 # default port for SSH
username = 'rduvalwa2'
password = 'blu4jazz'

theseHosts = ["BriaMBP", "OsxAir"]

sourceServer = theseHosts[0]
destinationServer = theseHosts[1] 

#print(len(fileList))


print(sourceServer +  ": " + sourceDir + "\t" +  destinationServer + ": " + destDir )
fileList = os.listdir(sourceDir)
try:
    t = paramiko.Transport((sourceServer,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.SFTP.
    sftp.put(sourceDir, sourceDir)
except paramiko.ssh_exception.AuthenticationException as e:
    print("connection error " ,e)
except FileNotFoundError as e:
    print("Found not found " ,e)
except Exception as e:
    print("Exception e: ", e)
finally:
    t.close()      