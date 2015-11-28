'''
Created on May 1, 2013

import the following names from a "settings" module:

 RECIPIENTS   a list of (name, email-address) tuples
 STARTTIME    datetime.datetime object for first message
 DAYCOUNT    number of daily message generations

@author: rduvalwa2
'''

import datetime
YR = 2013
MNTH = 5
DY = 26

NAME = ""
EMAIL = ""
STARTTIME = datetime.datetime(YR,MNTH,DY) # figure out how to create a time stamp
RECIPIENTS = {("RDuval","rduvalwa5@hotmail.com"),("Randy","rduvalwa2@frontier.com"),("rduval","rduvalwag@gmail.com")}
# RECIPIENTS = {(NAME,EMAIL)}
DAYCOUNT = 2

MESSAGE = 'This is a test message.'

