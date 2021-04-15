'''
Created on Mar 13, 2021

@author: rduvalwa2
'''
import paramiko

ip='10.0.0.58'
port=22
username='rduvalwa2'
password='blu4jazz'

artist = []

#cmd='ls -l  /Users/rduvalwa2/iTunes/iTunes Media/Music' 
cmd='ls "iTunes/iTunes Media/Music"' 
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
outlines
#print(outlines)
for ar in outlines:
    a = ar.replace("\n","")
#    artist.append(ar)
    artist.append(a)
    
print(artist)
#resp=''.join(outlines)
#print(resp)


#stdin,stdout,stderr=ssh.exec_command(cmd)
#outlines=stdout.readlines()
#print(outlines)

#resp=''.join(outlines)
#print(resp)


#print(artist)