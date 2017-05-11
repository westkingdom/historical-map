import sqlite3 as sq
from sqlite3 import Error
from libs import sqlitedb as sqcl, wk
import json
import psycopg2
w = wk.WestKingdom
table = 'wkhist'

def sqlconnect(path):
    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: databasde file
        :return: Connection object or None
        """
    try:
        conn = sq.connect(path)
        return conn
    except Error as e:
        print(e)

    return None

# Create table
def sqlcreate(conn):
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


# close the connections after syncing the changes
def sqlclose(conn):
    conn.commit()
    conn.close()


# check the DB path
def dbcheck(path):
    conn = sqlconnect(path)
    c = conn.cursor()
    c.execute('''SELECT  name FROM sqlite_master WHERE type = 'table' AND name = 'table_name';''')
    return c


#Populate the database with initial data
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


 # insert data as it is retrieved
def insertgeo(conn,thing):
    c = conn.cursor()
    for th in thing:
        c.execute("INSERT INTO wkhist (fulladdr, lat, long) VALUES(?, ?, ?, ?)", th)

 # Look to see if the value is 'Need Data' return boolean
def check(conn, thing):
    c = conn.cursor()
    c.execute('SELECT * FROM {tn} WHERE id={cn}'.format(tn=table, cn=thing[3]))
    this = c.fetchall()
    if not this[0][26] == "Need Data":
        return True
    else:
        return False
 # Check to see if the value is a coordinate, or see if it is null
def checkcoor(conn, mycount):
    c = conn.cursor()
    c.execute('SELECT * FROM {tn} WHERE id={cn}'.format(tn=table, cn=mycount))
    this = c.fetchall()
    if not this[0][26]:
        return True
    elif this[0][26]:
        return False
 # Example function
def fetch_database(database, table, filter_dict, case=None):
    filter_dict = dict(filter_dict)
    keys_list = filter_dict.keys()
    statement = 'SELECT * FROM {}'.format(table)
    if len(keys_list) > 0:
        statement += ' WHERE '

        for keys in keys_list:
            if case is None:
                key = keys
            else:
                key = '{}({})'.format(case, keys)

            temp_data = filter_dict[keys]
            temp_size = len(temp_data)

            if keys_list.index(keys) != 0:
                statement += ' AND '

            if temp_size > 0:
                for data in temp_data:
                    if temp_data.index(data) == 0:
                        statement += '{}="{}"'.format(key, data)
                    else:
                        statement += ' OR {}="{}"'.format(key, data)

    return database.execute(statement).fetchall()

 # Query to obtain the points, full address, event name and society year
def getpoints(conn):
    c = conn.cursor()
    c.execute('SELECT {ev},{ye},{fa},{lat},{lng} FROM {tn} WHERE  {lng} IS NOT NULL AND {lng} != "Need Data"'
              ''.format(tn=table, ev='event', ye='year', fa='fulladdr', lat='lat', lng='long'))
    this = c.fetchall()
    return this
 # Generic function to turn the queried data to json
def pntstojson(query, args, conn):
    cur = conn.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
        for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

