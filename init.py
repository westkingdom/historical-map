from libs import wkcsv as wcsv, wkgeo as wgeo, wkkml as wkml, wksql as wdb, globs as gl
import argparse
path = gl.dbp
conn = gl.conn
refined = gl.refined
data = gl.data

def main():
    parser = argparse.ArgumentParser(description="From WestKingdom Dataset to useable maps and interface")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("init", type=bool, help="Create Database")
    parser.add_argument("kml", type=bool, help="Create a KML file for use in Gmaps or Gearth")
    parser.add_argument("json", type=bool, help="Create Json for use in another interface")
    args = parser.parse_args()
    if args.init:
        initialize(data)
        build_dataset()
    elif args.kml:
        geocode_dataset(cols=gl.cols)
        build_kmlfile()
    elif args.json:
        geocode_dataset(cols=gl.cols)
        json_output()
    else:
        print("{}^{} == {}".format(args.x, args.y, answer))

def initialize(data):
    wdb.sqlcreate(path)
    data.to_sql("wkhist",conn, if_exists="append")
    wdb.sqlclose(conn)


def build_dataset():
    cols = wcsv.prepdata(data) # turn data into lists


def geocode_dataset(cols):
    geod = wgeo.geomain(cols, bigframe=wcsv.impcsv())
    wdb.sqlclose(conn)

def build_kmlfile():
    wkml.createkml()

def json_output():
     pass


if __name__ == '__main__':
    main()


