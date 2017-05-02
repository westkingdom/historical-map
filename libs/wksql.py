import sqlite3
from sqlite3 import Error

def sqlconnect(path):
    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: databasde file
        :return: Connection object or None
        """
    try:
        conn = sqlite3.connect(path)
        return conn
    except Error as e:
        print(e)

    return None

# Create table
def sqlcreate(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''CREATE TABLE `wkhist` (
	`id`	INTEGER PRIMARY KEY ,
	`event`	TEXT,
	`group`	TEXT,
	`date`	TEXT,
	`year`	TEXT,
	`location`	TEXT,
	`address`	TEXT,
	`city`	TEXT,
	`zip`	TEXT,
	`autocrat`	TEXT,
	`toilets`	TEXT,
	`potable`	TEXT,
	`showers`	TEXT,
	`camping`	TEXT,
	`feast`	TEXT,
	`eq`	TEXT,
	`arch`	TEXT,
	`war`	TEXT,
	`twengiht`	TEXT,
	`contact`	TEXT,
	`badParking`	TEXT,
	`costs`	TEXT,
	`attendance`	TEXT,
	`issues`	TEXT,
	`other`	TEXT,
	`lat`	TEXT,
	`long`	TEXT,
	`fulladdr`	TEXT
);''')
    print(sqlite3.version)

def sqlclose(conn):
    conn.commit()
    conn.close()

def dbcheck(path):
    conn = sqlconnect(path)
    c = conn.cursor()
    c.execute('''SELECT  name FROM sqlite_master WHERE type = 'table' AND name = 'table_name';''')
    return c

def dbpop(conn,list_con):
    c = conn.cursor()
    if list_con:
        try:
            c.execute("""UPDATE wkhist SET fulladdr=?, lat=?, long=? WHERE id=?""", (list_con[0], list_con[1], list_con[2], list_con[3]))
            conn.commit()
            return None
        except Error as e:
            print(e)
    else:
        last_row = "empty"
        return last_row

def dbinstgeo(conn,thing):
    c = conn.cursor()
    for th in thing:
        c.execute("INSERT INTO wkhist (fulladdr, lat, long) VALUES(?, ?, ?, ?)", th)

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

