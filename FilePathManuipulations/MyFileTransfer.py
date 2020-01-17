'''
Created on Jan 16, 2020
https://stackoverflow.com/questions/12909334/how-to-transfer-files-from-client-to-server-computer-by-using-python-script
@author: rduvalwa2
'''
import paramiko

source = r'/Users/rduvalwa2/TestDir/FileTransfer.txt'
dest = r'/Users/rduvalwa2/TestDir/2FileTransfer.txt'
hostname = '10.0.0.57'
port = 22 # default port for SSH
username = 'rduvalwa2'
password = 'blu4jazz'


try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(source, dest)
#    t.close()  
except paramiko.ssh_exception.AuthenticationException as e:
    print("connection error " ,e)
except FileNotFoundError as e:
    print("Found not found " ,e)
except Exception as e:
    print("Exception e: ", e)
finally:
#    print("Success")
    t.close()  
     
