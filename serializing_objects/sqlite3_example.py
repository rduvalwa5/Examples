import sqlite3
'''
con = sqlite3.connect(":memory:") shows error probably because a connection factory is used
'''
from sqlite3.dbapi2 import sqlite_version_info
from test import test_sqlite
print("sqlite versions is ", sqlite_version_info)
print(test_sqlite)
print(sqlite3.version_info)
print(sqlite3.__dict__)
con = sqlite3.connect(":memory:")

#(":memory:")

# enable extension loading
#con.enable_load_extension(True)

# Load the fulltext search extension
#con.execute("select load_extension('./fts3.so')")

# alternatively you can load the extension using an API call:
# con.load_extension("./fts3.so")

# disable extension loading again
#con.enable_load_extension(False)

# example from SQLite wiki
con.execute("create virtual table recipe using fts3(name, ingredients)")
con.executescript("""
    insert into recipe (name, ingredients) values ('broccoli stew', 'broccoli peppers cheese tomatoes');
    insert into recipe (name, ingredients) values ('pumpkin stew', 'pumpkin onions garlic celery');
    insert into recipe (name, ingredients) values ('broccoli pie', 'broccoli cheese onions flour');
    insert into recipe (name, ingredients) values ('pumpkin pie', 'pumpkin sugar flour butter');
    """)
for row in con.execute("select rowid, name, ingredients from recipe where name match 'pie'"):
    print(row)