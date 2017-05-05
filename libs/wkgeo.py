import time as ti
from geopy.geocoders import Nominatim as Geo
from geopy.exc import GeocoderTimedOut
from libs import wksql as wdb, globs as gl
conn = gl.conn
g = Geo()

# take prepped data, extract addr return it


def geomain(cols, bigframe):
    for i in range(0, int(bigframe.shape[0])):
        if "na" not in (str(cols["address"][i]), str(cols["city"][i]), str(cols["zip"][i])):
            try:
                mycount = i
                go = wdb.checkcoor(conn, mycount)
                if go:
                    print(mycount)
                    qstring = combine(cols, i)
                    ststring = replace(qstring, gl.sudict)  # strip nan's
                    result = getgeo(ststring)  # run the gecoding
                    list_con = geofied(result, mycount)  # build values for SQL query, avoiding SQL injections
                    #stop = wdb.check(conn, list_con)
                    #if not stop:
                    wdb.dbpop(conn, list_con)  # add to DB
                    print(str("Added new event" + str(list_con[0])))
                    conn.commit()
                    #else:
                    #    continue
                    ti.sleep(1.0)  # be nice to our apis
            except ValueError as e:
                print(e)
        else:
            continue
    wdb.sqlclose(gl.conn)  # close the DB


def geofied(result, mycount):
    list_con=[]
    if result:
        try:
            if result.address: list.append(list_con, str(result.address))
            else: list.append(list_con,"Need Data")
            if result.latitude: list.append(list_con, str(result.latitude))
            else: list.append(list_con,"Need Data")
            if result.longitude: list.append(list_con, str(result.longitude))
            else: list.append(list_con, "Need Data")
            list.append(list_con, mycount)
        except ValueError as e:
            print(e)
        return list_con
    else:
        list.append(list_con, "Need Data")
        list.append(list_con, "Need Data")
        list.append(list_con, "Need Data")
        list.append(list_con, mycount)
        return list_con

def replace(text,dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def combine(cols, i):
    qstring = ''.join(map(str, str(cols["address"][i]))) + ' ' + str(cols["city"][i]) + ' ' + str(
        cols["zip"][i])  # join each field together, for the query
    return qstring

def getgeo(ststring):
    try:
        result = g.geocode(ststring, timeout=2)
        return result
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s with message %s" % (ststring, e.msg))