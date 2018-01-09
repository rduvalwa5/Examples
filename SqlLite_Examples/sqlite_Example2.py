'''
Created on Dec 28, 2017
https://docs.python.org/2/library/sqlite3.html
@author: rduvalwa2
'''
# A minimal SQLite shell for experiments

# A minimal SQLite shell for experiments

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")
c.execute("""select * from stocks;""")
print (c.fetchall())
conn.commit()
#c.close()

print ("Enter your SQL commands to execute in sqlite3.")
print ("Enter a blank line to exit.")


while True:
    line = input()
    print("line is ",line)
    if line == "":
        print("Exiting")
        exit
    buffer += line

    
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print (cur.fetchall())
        except sqlite3.Error as e:
            print ("An error occurred:", e.args[0])
        buffer = ""
    
con.close()