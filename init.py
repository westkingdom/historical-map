from libs import wkcsv as wcsv, wkgeo as wgeo, wkkml as wkml, wksql as wdb, globs as gl
path = gl.dbp
conn = gl.conn
refined = gl.refined
data = gl.data

def main():
    #cols = wcsv.prepdata(data) # turn data into lists
    #geod = wgeo.geomain(cols, bigframe=wcsv.impcsv())
    #wdb.sqlclose(conn)
    wkml.createkml()


def initialize(data):
    wdb.sqlcreate(path)
    data.to_sql("wkhist",conn, if_exists="append")
    wdb.sqlclose(conn)

if __name__ == '__main__':
    main()
