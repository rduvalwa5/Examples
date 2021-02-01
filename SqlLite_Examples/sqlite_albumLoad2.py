'''
Created on Jan 31, 2021
insert records from CSV file into sqlite music databse
@author: rduvalwa2
'''
import sqlite3
import csv, sys
from sqlite3 import Error


filename = '/Users/rduvalwa2/git/Examples/SqlLite_Examples/Sqlite_Notes/artist_albums.csv'
database = r"/Users/rduvalwa2/Music.db"
#database = r"/Users/rduvalwa2/git/Examples/SqlLite_Examples/Music.db"


conn = None
try:
    conn = sqlite3.connect(database)
    print("connection complete")          
except Error as e:
        print(e)

with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        rowCount = 0
        for row in reader:
            if rowCount > 0:
#                print(row[0], row[1], row[2], row[3])
#  statement = "INSERT INTO album_covers VALUES(cover_idx,album_cover,album,description),(cover_idx,album_cover,album,description);)
                statement = "INSERT INTO artist_albums VALUES(\"" + row[0]+ "\",\"" + row[1]+ "\",\"" + row[2] + "\",\"" + row[3] +"\",\"" + row[4] + "\",\"" + row[5] + "\",\"" + row[6] +"\");"
#insertStatement = "INSERT into Music.album_covers(album_cover,cover_idx,album,description)  values(\"" + cov + "\"," + str(idx)  + "," + "\"iTunesImages\"" + "," + "\"none\" " + ");"
                print(statement)
                cur = conn.cursor()
                cur.execute(statement)  
            
            rowCount = rowCount + 1
#            print(rowCount)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        
    cur.execute("commit;")
    