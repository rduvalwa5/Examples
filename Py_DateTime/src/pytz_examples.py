'''
Created on Sep 24, 2016

Created on Sep 22, 2016
These classes explain date time formating
https://docs.python.org/3/search.html?q=date+time&check_keywords=yes&area=default
https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone
https://docs.python.org/2.4/lib/tzinfo-examples.txt
https://docs.python.org/3/library/datetime.html?highlight=timezone#datetime.timezone

pytz Install:
https://pypi.python.org/pypi/pytz?
https://pypi.python.org/pypi/pytz?#downloads

C1246895-osx:3.5 rduvalwa2$ cd bin
C1246895-osx:bin rduvalwa2$ ls
2to3            idle3            pip3.5            python3            python3.5        python3.5m        pyvenv-3.5
2to3-3.5        idle3.5            pydoc3            python3-32        python3.5-32        python3.5m-config
easy_install-3.5    pip3            pydoc3.5        python3-config        python3.5-config    pyvenv
C1246895-osx:bin rduvalwa2$ sudo easy_install-3.5  ~/Downloads/pytz-2016.6.1-py3.5.egg
Processing pytz-2016.6.1-py3.5.egg
Copying pytz-2016.6.1-py3.5.egg to /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages
Adding pytz 2016.6.1 to easy-install.pth file

Installed /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytz-2016.6.1-py3.5.egg
Processing dependencies for pytz==2016.6.1
Finished processing dependencies for pytz==2016.6.1
C1246895-osx:bin rduvalwa2$ 

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


if __name__ == '__main__':
    pass