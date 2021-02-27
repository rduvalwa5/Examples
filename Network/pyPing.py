'''
Created on Feb 26, 2021
https://pypi.org/project/pythonping/
@author: rduvalwa2
'''

import os

hostnames = [
    '10.0.0.1',
    'localhost',
    'MaxBookPro17OSX',
    'Osxair'
]

for hostname in hostnames:
    response = os.system('ping -c 1 ' + hostname)
    print(response)
    if response == 0:
        print (hostname, 'is up')
    else:
        print (hostname, 'is down')