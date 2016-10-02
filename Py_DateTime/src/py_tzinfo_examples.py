'''
Created on Sep 25, 2016
http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/2.4/lib/tzinfo-examples.txt


https://docs.python.org/3/library/datetime.html

http://pytz.sourceforge.net   <----------
'''

from datetime import datetime, timedelta, time
from pytz import timezone, reference
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
        self.utc = pytz.utc
        self.this_tzinfo = timezone(self.region)
        self.utc_dt = datetime(self.year,self.month,self.day,self.hour,self.min,self.sec, tzinfo=self.utc)
        
    def get_utc(self):
        return self.utc_dt
        
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

    '''
    
    '''
    def convert_from_utc(self):
        '''
        The preferred way of dealing with times is to always work in UTC, converting to localtime only when generating output 
        to be read by humans.
        >>> utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
        >>> loc_dt = utc_dt.astimezone(eastern)
        >>> loc_dt.strftime(fmt)
        '2002-10-27 01:00:00 EST-0500'
        '''
        loc_dt = self.utc_dt.astimezone(self.this_tzinfo)
        return loc_dt.strftime(self.fmt)
        
        
    def get_new_date(self,delta):
        '''
        This library also allows you to do date arithmetic using local times, although it is more complicated than 
        working in UTC as you need to use the normalize() method to handle daylight saving time and other timezone transitions. 
        In this example, loc_dt is set to the instant when daylight saving time ends in the US/Eastern timezone.
        >>> before = loc_dt - timedelta(minutes=10)
        >>> before.strftime(fmt)
        '2002-10-27 00:50:00 EST-0500'
        >>> eastern.normalize(before).strftime(fmt)
        '2002-10-27 01:50:00 EDT-0400'
        >>> after = eastern.normalize(before + timedelta(minutes=20))
        >>> after.strftime(fmt)
        '2002-10-27 01:10:00 EST-0500'
        
        - takes away 
        
        '''
        name = timezone(self.region)
        n = (name.localize(datetime(self.year,self.month,self.day,self.hour,self.min,self.sec)))
        newdate = n + timedelta(minutes=delta)
        return newdate.strftime(self.fmt)

    def get_system_time(self):
        current_time = datetime.now().time() 
        return current_time
    
    def get_system_timezone(self,yr=0,mon=0,day=0,hr=0,min=0,sec=0):
        if yr == 0:
            today = datetime.now()
        else:
            today = datetime(yr,mon,day,hr,min,sec)
        localtime = reference.LocalTimezone()
        local_tz = localtime.tzname(today)
        return today.strftime(self.fmt) + local_tz
        
    
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
    print('convert_from uts ',moscowLocal.convert_from_utc())
    print(eastLocal.display_local_timezone())
    print(centralLocal.display_local_timezone())
    print(westLocal.display_local_timezone())
    print(londonLocal.display_local_timezone())
    print(londonLocal.display_local_timezone1())
    print(hawaiiLocal.display_local_timezone())
    print('alt1: ',hawaiiLocal.display_local_timezone1())
    print('alt2: ',hawaiiLocal.display_local_timezone2())
    
    # diff =  hawaiiLocal.get_new_date(60)
    print(hawaiiLocal.get_new_date(-60))
    print(hawaiiLocal.get_new_date(24 * 60))
    print(hawaiiLocal.get_new_date(24 * 60 * -1))
#    print(hawaiiLocal.subtract_new())
    print(hawaiiLocal.get_system_time())
    print(hawaiiLocal.get_system_timezone())
    print(hawaiiLocal.get_system_timezone(2016,11,6,1,55,10))
    print(hawaiiLocal.get_system_timezone(2016,11,6,2,0,0))