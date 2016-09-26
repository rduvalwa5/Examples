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


    def __init__(self,country='US',region = 'Eastern'):
        '''
        Constructor
        '''
        self.region = country + '/' + region
#        print(self.region)
        self.fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        
        
    def set_utc(self):
        self.utc = pytz.utc
        return  self.utc
    
    def get_utc(self):
        return self.set_utc()
        
    def get_utc_zone(self):
        return  self.utc.zone
    
    def set_regionTimeZone(self):
        self.setRegion = timezone(self.region)
        return  self.setRegion.zone
        
    def get_regionTimeZone(self):
        return self.set_regionTimeZone()
    
    def get_local_tz(self):
#        loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
# >>> print(loc_dt.strftime(fmt))
        pass
        
    
if __name__ == '__main__':
    eastLocal = localtime('US','Eastern')
    print(eastLocal.get_utc())
    print(eastLocal.get_regionTimeZone())

    centralLocal = localtime('US','Central')
    print(centralLocal.get_regionTimeZone())

    mountainLocal = localtime('US','Mountain')
    print(mountainLocal.get_regionTimeZone())

    westLocal = localtime('US','Pacific')
    print(westLocal.get_regionTimeZone())

    londonLocal = localtime('Europe','London')
    print(londonLocal.get_regionTimeZone())
    
    moscowLocal = localtime('Europe','Moscow')
    print(moscowLocal.get_regionTimeZone())

    hawaiiLocal = localtime('US','Hawaii')
    print(hawaiiLocal.get_regionTimeZone())
    
        