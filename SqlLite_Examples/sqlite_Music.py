'''
Created on Jan 27, 2021
https://docs.python.org/3/library/sqlite3.html
https://www.thegeekstuff.com/2012/09/sqlite-command-examples/
https://sqlite.org/datatype3.html#expraff
https://www.kite.com/python/answers/how-to-list-tables-using-sqlite3-in-python

https://www.programiz.com/python-programming/list
https://www.tomordonez.com/get-schema-sqlite-python/

https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

@author: rduvalwa2

MySQL -------
INSERT INTO `type` (`type`, `type_idx`)
VALUES
    ('TestType',1),
    ('Download',2),
    ('Vinyl',3),
    ('CD',4),
    ('Tape',5),
    ('TestType',6);

-- Values stored as TEXT, INTEGER, INTEGER, REAL, TEXT.

sqlite> INSERT INTO type VALUES(1,'TestTYpe');

sqlite> select * from type;
1|TestTYpe

'''
import sqlite3
import csv, sys
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None   
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection complete")

              
    except Error as e:
        print(e)

    return conn

def get_data_tables(con):
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    myTables = cur.fetchall()
    print(myTables)
    allTables = []
    for tab in myTables:
        allTables.append(tab[0])
    print(allTables)
    return allTables
    
def describe_table(conn,table):
    """
    .schema table_name
    cur.execute("PRAGMA table_info('Courses')").fetchall()
    """
    cur = conn.cursor()
    print(table)
    print(cur.execute("PRAGMA table_info(" + table + ")").fetchall())
#    rows = cur.execute("PRAGMA table_info('artist_albums')").fetchall()
#    for row in rows:
#        print(row)
        

def insert_album_covers(conn):
#    cur = conn.cursor()
    filename = '/Users/rduvalwa2/git/Examples/SqlLite_Examples/Sqlite_Notes/album_covers.csv'
    print(filename)
    with open(filename, newline='') as f:
        reader = csv.reader(f)
    try:
        rowCount = 0
        for row in reader:
            if rowCount > 0:
                print(row[0], row[1], row[2], row[3])
            rowCount = rowCount + 1
            print(rowCount)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    
    
    
    
    
    """
    filename = '/Users/rduvalwa2/git/Examples/SqlLite_Examples/Sqlite_Notes/album_covers.csv'
    print(filename)
    #over_idx,"album_cover","album","description"
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            rowCount = 0
            for row in reader:
                if rowCount > 0:
                    print(row[0], row[1], row[2], row[3])
#                statement = "INSERT INTO album_covers VALUES(cover_idx,album_cover,album,description),(cover_idx,album_cover,album,description);)
#                    statement = "INSERT INTO album_covers VALUES(" + row[0]+ " \, " + row[1]+ "\, " + row[2] + "\, " + row[3] + ";"
#                    print(statement)
            rowCount = rowCount + 1
            print(rowCount)

        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    
#    cur.execute("SELECT * FROM type WHERE type like ?",(t,))
#    cur.execute("INSERT INTO album_covers VALUES('cover_idx','album_cover','album','description');"
#    sqlite> INSERT INTO type VALUES(1,'TestTYpe');

#    statement = "INSERT INTO album_covers VALUES(cover_idx,album_cover,album,description),(cover_idx,album_cover,album,description);)
#    cur.execute("INSERT INTO album_covers VALUES('cover_idx','album_cover','album','description');",(cover_idx,album_cover,album,description))
    
"""
def select_all_type(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM type;")

    rows = cur.fetchall()
    print("rows are ",rows)
    for row in rows:
        print(row)


def select_type_by_type(conn, t):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM type WHERE type like ?",(t,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
        



def main():
    database = r"/Users/rduvalwa2/Music.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        select_all_type(conn)
#        select_type_by_type(conn,'Vinyl')
#        allTables = get_data_tables(conn)
#        for tab in allTables:
#            print(tab)
#            describe_table(conn,tab)
        insert_album_covers(conn)


if __name__ == '__main__':
    main()
