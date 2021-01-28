'''
Created on Jan 27, 2021
https://docs.python.org/3/library/sqlite3.html
https://www.thegeekstuff.com/2012/09/sqlite-command-examples/
https://sqlite.org/datatype3.html#expraff
@author: rduvalwa2
'''
import sqlite3

con = sqlite3.connect(":Music.db:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

conn = sqlite3.connect("Music.db")
c = conn.cursor()
#c.execute('''create table stocks
#(date text, trans text, symbol text,
# qty real, price real)''')
#c.execute("""insert into stocks
#          values ('2006-01-05','BUY','RHAT',100,35.14)""")
c.execute("tables")
print (c.fetchall())
conn.commit()

conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from type')
# <sqlite3.Cursor object at 0x7f4e7dd8fa80>
r = c.fetchone()
type(r)
# <type 'sqlite3.Row'>
r
# (u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14)
len(r)
# 5
r[2]
# u'RHAT'
r.keys()
# ['date', 'trans', 'symbol', 'qty', 'price']
r['qty']
# 100.0
for member in r:
    print( member)