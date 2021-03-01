'''
Created on Mar 26, 2020
@author: rduvalwa2

https://www.pythonforbeginners.com/python/dns-lookup-python
https://docs.python.org/3/library/socket.html

'''
import socket
hosts = ("www.google.com","www.comcast.net","osxair","www.verizon.net","www.github.com")
for h in hosts:
    addr1 = socket.gethostbyname(h)
# socket.getaddrinfo(host, port, family, type, proto, flags)
    print("address for " + h + " is " + addr1)