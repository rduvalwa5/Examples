'''
Created on Sep 21, 2016

@author: rduvalwa2
'''
import datetime
class SimpleDateTime:
    '''
    https://docs.python.org/3/library/datetime.html
    '''


 #   def __init__(self):
 #       '''
 #       Constructor
 #       '''
    def get_system_time(self):
         current_time = datetime.datetime.now().time() 
         return current_time
    
    def getNowDateTime(self):
            return datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    def getNowTime(self):
            return datetime.datetime.now().strftime("%H:%M:%S")
        
    def getNowDay(self):
            return datetime.datetime.now().strftime("%d")
            
    def getToday(self):
            return datetime.date.today()
        
    def getWeekday(self,year,month,day):
            '''
            Return the day of the week as an integer, where Monday is 0 and Sunday is 6. 
            For example, date(2002, 12, 4).weekday() == 2, a 
            '''
            daysofweek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            index =  datetime.date(year,month,day).weekday()
#            print('index ',index)
            return daysofweek[index]
 
    def getIsoWeekday(self,year,month,day):
            '''
            Return the day of the week as an integer, where Monday is 1 and Sunday is 7. 
            For example, date(2002, 12, 4).isoweekday() == 3, a 
            '''
            ISOdaysofweek = ['Not Day of week','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            index =  datetime.date(year,month,day).isoweekday()
#            print('index ',index)
            return ISOdaysofweek[index]
        
if __name__ == '__main__':

    month = 6
    year = 1951
    day = 12
    print(month, day, year)
    simple = SimpleDateTime()
    print("System Time: ", simple.get_system_time())
    print("System Date and Time: ",simple.getNowDateTime())
    print("System time: ",simple.getNowTime())
    print("System day of the month: ",simple.getNowDay())
    print("System Today: ",simple.getToday())
    print("Day of the week for ", year,  month, day, " : ", simple.getWeekday(year, month, day))
    print(simple.getIsoWeekday(year, month, day))
    