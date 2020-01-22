#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

'''
Created on Jan 16, 2020
https://stackoverflow.com/questions/12909334/how-to-transfer-files-from-client-to-server-computer-by-using-python-script
@author: rduvalwa2
'''
import paramiko
import os

sourceDir = r'/Users/rduvalwa2/SharedSourceData/'
#sourceDir2 = r'/Users/rduvalwa2/TestDirCopy/' cannot send directory
destDir = r'/Users/rduvalwa2/SharedDestData/'
#destDir2 = r'/Users/rduvalwa2/TestDirCopy/' cannot send directory

fileList = os.listdir(sourceDir)

port = 22 # default port for SSH
username = 'rduvalwa2'
password = 'blu4jazz'

theseHosts = ["RandalluvalsMBP", "C1246895-OSX","OsxAir"]
print(len(fileList))
if len(fileList) > 1:
    for fil in fileList:
        for hostname in theseHosts:
            for fil in fileList:
                if fil != ".DS_Store":
                    sourceFile = sourceDir + fil
                    destFile = destDir + fil
                    print(hostname + ": " + sourceFile + " and " + destFile)
                    try:
                        t = paramiko.Transport((hostname,port))
                        t.connect(username=username, password=password)
                        sftp = paramiko.SFTPClient.from_transport(t)
                        sftp.put(sourceFile, destFile)
                    except paramiko.ssh_exception.AuthenticationException as e:
                            print("connection error " ,e)
                    except FileNotFoundError as e:
                            print("Found not found " ,e)
                    except Exception as e:
                        print("Exception e: ", e)
                    finally:
                        t.close()  
else:
    print('the list is empty')
    exit                