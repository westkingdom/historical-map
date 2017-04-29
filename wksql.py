import sqlite3

def sqlconnect():
    conn = sqlite3.connect('wk_history.db')
    return conn


# Create table
def sqlcreate(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wkhist
                 (event text, group text, date text, year text, location text, 
                 address text, city text, zip , autocrat text, toilets text, 
                 potable text, showers text, camping text, feast text, eq text, 
                 arch text, war text, twengiht text, contact text, 
                 badParking text, costs text, attendance text, issues text, 
                 other text, lat real, long real, fulladdr text)''')

def sqlclose(conn):
    conn.commit()
    conn.close()

def dbcheck(conn):
    c = conn.cursor()
    c.execute('''SELECT  name FROM sqlite_master WHERE type = 'table' AND name = 'table_name';''')
    return c

def dbpop(conn,cols):
    c = conn.cursor()
    c.executemany("INSERT INTO wkhist VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", cols)

def dbinstgeo(conn,thing):
    c = conn.cursor()
    for th in thing:
        c.execute("INSERT INTO wkhist VALUES(?, ?, ?, ?)", th)

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

