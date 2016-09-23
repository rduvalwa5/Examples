'''
Created on Sep 22, 2016
These classes explain date time formating
https://docs.python.org/3/search.html?q=date+time&check_keywords=yes&area=default
https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

'''
import datetime


class ExamplesDateTimeFormat(object):
    '''
    classdocs
    '''


#    def __init__(self, params):
#        '''
#        Constructor
#        '''
        
    def display_min_max(self):
        min = datetime.MINYEAR
        max = datetime.MAXYEAR
        values = {'min':min,'max':max}
        return values
    
    
        
if __name__ == '__main__':
    myClass = ExamplesDateTimeFormat()
    min_max = myClass.display_min_max()
    print("minimum datetime is: ", min_max.get('min'))
    print("maximum datetime is: ", min_max.get('max'))