'''
Created on Feb 26, 2021

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
    response = os.system('nslookup ' + hostname)
    print(response)
