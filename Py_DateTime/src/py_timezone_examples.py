'''
Created on Sep 25, 2016

utc = pytz.utc
>>> utc.zone
'UTC'
>>> eastern = timezone('US/Eastern')
>>> eastern.zone
'US/Eastern'
>>> amsterdam = timezone('Europe/Amsterdam')
>>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'
'''

from datetime import datetime, timedelta
from pytz import timezone
import pytz

class localtime(object):
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
        
    def set_utc(self):
        self.utc = pytz.utc
        return  self.utc
    
    def get_utc(self):
        return self.set_utc()
        
    def get_utc_zone(self):
        return  self.utc.zone
    
    def set_regionTimeZone(self):
        self.setRegion = timezone(self.region)
#        return  self.setRegion.zone
        return  self.setRegion
        
    def get_regionTimeZone(self):
        return self.set_regionTimeZone()
    
    def get_local(self):
        local_datetime = self.set_regionTimeZone().localize(datetime(self.year,self.month,self.day,self.hour,self.min,self.sec))
#        print(local_datetime.strftime(self.fmt))
        return local_datetime.strftime(self.fmt)
        
    def alt_timezone(self):
        '''
        >> loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
        >>> print(loc_dt.strftime(fmt))
            2002-10-27 06:00:00 EST-0500
        The second way of building a localized time is by converting an existing localized time using the standard astimezone() method:
        >>> ams_dt = loc_dt.astimezone(amsterdam)
        >>> ams_dt.strftime(fmt)
        '2002-10-27 12:00:00 CET+0100'
        '''
        name = timezone(self.region)
        loc_dt = name.localize(datetime(self.year,self.month,self.day,self.hour,self.min,self.sec))
        res = loc_dt.astimezone(name)
        return "alt: " + res.strftime(self.fmt)
    
if __name__ == '__main__':
    eastLocal = localtime(2016,12,31,23,59,59,'US','Eastern')
    print(eastLocal.get_utc())
    print(eastLocal.get_regionTimeZone())

    centralLocal = localtime(2016,12,31,23,59,59,'US','Central')
    print(centralLocal.get_regionTimeZone())

    mountainLocal = localtime(2016,12,31,23,59,59,'US','Mountain')
    print(mountainLocal.get_regionTimeZone())

    westLocal = localtime(2016,12,31,23,59,59,'US','Pacific')
    print(westLocal.get_regionTimeZone())

    londonLocal = localtime(2016,12,31,23,59,59,'Europe','London')
    print(londonLocal.get_regionTimeZone())
    
    moscowLocal = localtime(2016,12,31,23,59,59,'Europe','Moscow')
    print(moscowLocal.get_regionTimeZone())

    hawaiiLocal = localtime(2016,12,31,23,59,59,'US','Hawaii')
    print(hawaiiLocal.get_regionTimeZone())
    
    print(moscowLocal.get_local())
    print(eastLocal.get_local())
    print(centralLocal.get_local())
    print(westLocal.get_local())
    print(londonLocal.get_local())
    print(londonLocal.alt_timezone())
    print(hawaiiLocal.get_local())
    print(hawaiiLocal.alt_timezone())
