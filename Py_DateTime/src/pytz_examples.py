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


http://pytz.sourceforge.net
'''
from datetime import datetime, timedelta
from pytz import timezone
import pytz

def timeDate_Arithmetic_Example(year,month,day):
    print('Localized times and date arithmetic')
    utc = pytz.utc
    print(utc.zone)
    eastern = timezone('US/Eastern')
    print(eastern.zone)
    amsterdam = timezone('Europe/Amsterdam')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    tz = timezone('America/St_Johns')
    loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
    print(loc_dt.strftime(fmt))

    print('\nThe second way of building a localized time is by converting an existing localized time using the standard astimezone() method:')
    ams_dt = loc_dt.astimezone(amsterdam)
    print(ams_dt.strftime(fmt))

    print('\nUnfortunately using the tzinfo argument of the standard datetime constructors ‘’does not work’’ with pytz for many timezones.')
    print(datetime(2002, 10, 27, 12, 0, 0, tzinfo=amsterdam).strftime(fmt))
    # '2002-10-27 12:00:00 LMT+002   0'

    print('\nIt is safe for timezones without daylight saving transitions though, such as UTC:')
    print(datetime(2002, 10, 27, 12, 0, 0, tzinfo=pytz.utc).strftime(fmt))
    # '2002-10-27 12:00:00 UTC+0000'

    print('The preferred way of dealing with times is to always work in UTC, converting to localtime only when \ngenerating output to be read by humans.')
    utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
    loc_dt = utc_dt.astimezone(eastern)
    print(loc_dt.strftime(fmt))
    # '2002-10-27 01:00:00 EST-0500'

    print('\nThis library also allows you to do date arithmetic using local times, although it is more complicated \nthan working in UTC as you need to use the normalize() method to handle daylight saving time and other timezone transitions. \nIn this example, loc_dt is set to the instant when daylight saving time ends in the US/Eastern timezone.')
    before = loc_dt - timedelta(minutes=10)
    print(before.strftime(fmt))
    # '2002-10-27 00:50:00 EST-0500'
    print(eastern.normalize(before).strftime(fmt))
    # '2002-10-27 01:50:00 EDT-0400'
    after = eastern.normalize(before + timedelta(minutes=20))
    print(after.strftime(fmt))
    # '2002-10-27 01:10:00 EST-0500'
    
    print('\nCreating local times is also tricky, and the reason why working with local times is not recommended. \nUnfortunately, you cannot just pass a tzinfo argument when constructing a datetime (see the next section for more details)')
    dt = datetime(2002, 10, 27, 1, 30, 0)
    dt1 = eastern.localize(dt, is_dst=True)
    print(dt1.strftime(fmt))
    # '2002-10-27 01:30:00 EDT-0400'
    dt2 = eastern.localize(dt, is_dst=False)
    print(dt2.strftime(fmt))
    # '2002-10-27 01:30:00 EST-0500'

    print('\nConverting between timezones is more easily done, using the standard astimezone method.')
    utc_dt = utc.localize(datetime.utcfromtimestamp(1143408899))
    print(utc_dt.strftime(fmt))
    #'2006-03-26 21:34:59 UTC+0000'
    au_tz = timezone('Australia/Sydney')
    au_dt = utc_dt.astimezone(au_tz)
    print(au_dt.strftime(fmt))
    # '2006-03-27 08:34:59 AEDT+1100'
    utc_dt2 = au_dt.astimezone(utc)
    print(utc_dt2.strftime(fmt))
    # '2006-03-26 21:34:59 UTC+0000'
    print(utc_dt == utc_dt2)
    #True
    
    print('\nYou can take shortcuts when dealing with the UTC side of timezone conversions. \nnormalize() and localize() are not really necessary when there are no daylight saving time transitions to deal with.')
    utc_dt = datetime.utcfromtimestamp(1143408899).replace(tzinfo=utc)
    print(utc_dt.strftime(fmt))
    #'2006-03-26 21:34:59 UTC+0000'
    au_tz = timezone('Australia/Sydney')
    au_dt = au_tz.normalize(utc_dt.astimezone(au_tz))
    print(au_dt.strftime(fmt))
    # '2006-03-27 08:34:59 AEDT+1100'
    utc_dt2 = au_dt.astimezone(utc)
    print(utc_dt2.strftime(fmt))
    #'2006-03-26 21:34:59 UTC+0000'

 
 
 
    
def tzInfo_Example():
        print('\nThe tzinfo instances returned by the timezone() function have been extended to cope with ambiguous times by adding \nan is_dst parameter to the utcoffset(), dst() && tzname() methods.')
        tz = timezone('America/St_Johns')
        normal = datetime(2009, 9, 1)
        ambiguous = datetime(2009, 10, 31, 23, 30)
        print('The is_dst parameter is ignored for most timestamps. It is only used during DST transition ambiguous periods to resulve that ambiguity.\n')
        print(tz.utcoffset(normal, is_dst=True))
        # datetime.timedelta(-1, 77400)
        print(tz.dst(normal, is_dst=True))
        # datetime.timedelta(0, 3600)
        print(tz.tzname(normal, is_dst=True))
        # 'NDT'
        print(tz.utcoffset(ambiguous, is_dst=True))
        #datetime.timedelta(-1, 77400)
        print(tz.dst(ambiguous, is_dst=True))
        # datetime.timedelta(0, 3600)
        print(tz.tzname(ambiguous, is_dst=True))
        # 'NDT'
        print(tz.utcoffset(normal, is_dst=False))
        # datetime.timedelta(-1, 77400)
        print(tz.dst(normal, is_dst=False))
        # datetime.timedelta(0, 3600)
        print(tz.tzname(normal, is_dst=False))
        # 'NDT'
        print(tz.utcoffset(ambiguous, is_dst=False))
        # datetime.timedelta(-1, 73800)
        print(tz.dst(ambiguous, is_dst=False))
        # datetime.timedelta(0)
        print(tz.tzname(ambiguous, is_dst=False))
        #'NST'


if __name__ == '__main__':
    timeDate_Arithmetic_Example(1951,6,12)
    
    tzInfo_Example()