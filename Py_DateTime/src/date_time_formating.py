'''
Created on Sep 22, 2016
These classes explain date time formating
https://docs.python.org/3/search.html?q=date+time&check_keywords=yes&area=default
https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/2.4/lib/tzinfo-examples.txt




'''
import datetime
from pytz import tzinfo

# import timezone

class TimeZoneExamples(object):
    '''
    http://pytz.sourceforge.net
    '''
    def __init__(self,):
        pass
    
    def print_tz(self):
        dt = datetime.timedelta(hours=8)
        print(dt)
        print(datetime.tzinfo.tzname('PDT'))
              
    def get_tz(self):
        pass

    

class ExamplesDateTimeFormat(object):
    '''
    classdocs
    '''


    def __init__(self, year,month,day,hour,minute,second):
        '''
        Constructor
        '''
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
#        self.timeZone = ,945813, tzinfo=<FixedOffset '+00:00' datetime.timedelta(0)>
#        self.tz = 
        self.dateObject = datetime.datetime(self.year,self.month,self.day,self.hour,self.minute,self.second)

 #       self.timeObject = datetime.time(self.hour,self.minute,self.second)
 #       self.timeObject = datetime.timezone(datetime.tzinfo)
    
    def getDateObject(self):
        return  self.dateObject
    
    def getObjectYear(self):
        return  self.dateObject.year

    def getObjectMonth(self):
        return  self.dateObject.strftime("%B")
    
    def getObjectDay(self):
        return  self.dateObject.strftime("%A")
 
    def getObjectTime(self):
        return  self.timeObject
        
    
    def display_min_max(self):
        min = datetime.MINYEAR
        max = datetime.MAXYEAR
        values = {'min':min,'max':max}
        return values
    
    
        
if __name__ == '__main__':
    myClass = ExamplesDateTimeFormat(1951, 6, 12, 20, 30, 59,)
#    myClassTime = myClass.getObjectTime()
    min_max = myClass.display_min_max()
    print("minimum datetime is: ", min_max.get('min'))
    print("maximum datetime is: ", min_max.get('max'))
    
    print(myClass.getDateObject())
    print(myClass.getObjectMonth())
    print(myClass.tzinfo())
#    print(myClassTime)

#    myTz =  TimeZoneExamples()
#    myTz.print_tz()