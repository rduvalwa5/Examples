'''
Created on Mar 26, 2020
@author: rduvalwa2

https://www.pythonforbeginners.com/python/dns-lookup-python
https://docs.python.org/3/library/socket.html

'''
import socket

addr1 = socket.gethostbyname("WWW.google.com")
# socket.getaddrinfo(host, port, family, type, proto, flags)

print(addr1)