'''
Created on Jan 30, 2021

@author: rduvalwa2
'''
import csv, sys


filename = '/Users/rduvalwa2/git/Examples/SqlLite_Examples/Sqlite_Notes/album_covers.csv'

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