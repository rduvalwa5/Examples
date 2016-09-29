'''
Created on Sep 25, 2016
http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/2.4/lib/tzinfo-examples.txt


https://docs.python.org/3/library/datetime.html

http://pytz.sourceforge.net   <----------
'''

from datetime import datetime, timedelta
from pytz import timezone
import pytz

class localtime_tzinfo(object):
    '''
    Localized times and date arithmetic
    https://pypi.python.org/pypi/pytz?
    http://pytz.sourceforge.net
    '''


    def __init__(self,yr,mon,d,h,m,s,country='US',region = 'Eastern'):
        '''
        Constructor
        '''
        self.region = country + '/' + region
#        print(self.region)
        self.fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        self.year = yr
        self.month = mon
        self.day = d
        self.hour = h
        self.min = m
        self.sec =s
        self.this_tzinfo = timezone(self.region)
        
    def set_utc(self):
        self.utc = pytz.utc
        return  self.utc
    
    def get_utc(self):
        return self.set_utc()
        
    def get_utc_zone(self):
        return  self.utc.zone
    
    def get_tzinfo(self):
        return  self.this_tzinfo
       
        
    def get_regionTimeZone_tzinfo(self):
        return  self.this_tzinfo
    
    def display_local_timezone(self):
        local_datetime = self.this_tzinfo.localize(datetime(self.year,self.month,self.day,self.hour,self.min,self.sec))
#        print(local_datetime.strftime(self.fmt))
        return local_datetime.strftime(self.fmt)
        
    def display_local_timezone1(self):
        name = timezone(self.region)
        loc_dt = name.localize(datetime(self.year,self.month,self.day,self.hour,self.min,self.sec))
        res = loc_dt.astimezone(name)
        return  res.strftime(self.fmt)
    
    def display_local_timezone2(self):
        return datetime(self.year,self.month,self.day,self.hour,self.min,self.sec, tzinfo = self.this_tzinfo ).strftime(self.fmt)
    
if __name__ == '__main__':
    eastLocal = localtime_tzinfo(2016,12,31,23,59,59,'US','Eastern')
    print(eastLocal.get_utc())
    print(eastLocal.get_regionTimeZone_tzinfo())

    centralLocal = localtime_tzinfo(2016,12,31,23,59,59,'US','Central')
    print(centralLocal.get_regionTimeZone_tzinfo())

    mountainLocal = localtime_tzinfo(2016,12,31,23,59,59,'US','Mountain')
    print(mountainLocal.get_regionTimeZone_tzinfo())

    westLocal = localtime_tzinfo(2016,12,31,23,59,59,'US','Pacific')
    print(westLocal.get_regionTimeZone_tzinfo())

    londonLocal = localtime_tzinfo(2016,12,31,23,59,59,'Europe','London')
    print(londonLocal.get_regionTimeZone_tzinfo())
    
    moscowLocal = localtime_tzinfo(2016,12,31,23,59,59,'Europe','Moscow')
    print(moscowLocal.get_regionTimeZone_tzinfo())

    hawaiiLocal = localtime_tzinfo(2016,12,31,23,59,59,'US','Hawaii')
    print(hawaiiLocal.get_regionTimeZone_tzinfo())
    
    print(moscowLocal.display_local_timezone())
    print(eastLocal.display_local_timezone())
    print(centralLocal.display_local_timezone())
    print(westLocal.display_local_timezone())
    print(londonLocal.display_local_timezone())
    print(londonLocal.display_local_timezone1())
    print(hawaiiLocal.display_local_timezone())
    print('alt1: ',hawaiiLocal.display_local_timezone1())
    print('alt2: ',hawaiiLocal.display_local_timezone2())