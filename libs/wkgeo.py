import time as ti
from geopy.geocoders import Nominatim as geo
from libs import wksql as wdb, wkcsv as wcs, globs as gl

g = geo()

#take prepped data, extract addr return it
def getgeo(cols, bigframe):
    for i in range(0, int(bigframe.shape[0])):
        if "na" not in (str(cols["address"][i]), str(cols["city"][i]), str(cols["zip"][i])):
            try:
                mycount = i
                qstring = ''.join(map(str, str(cols["address"][i]))) + ' ' + str(cols["city"][i]) + ' ' + str(cols["zip"][i]) #join each field together, for the query
                ststring = replace(qstring,gl.sudict) #strip nan's
                result = g.geocode(ststring) #run the gecoding
                list_con = geofied(result, mycount) #build values for SQL query, avoiding SQL injections
                wdb.dbpop(gl.conn,list_con) #add to DB
                ti.sleep(1.0) #be nice to our apis
            except ValueError as e:
                print(e)
        else:
            wdb.sqlclose(gl.conn) #close the DB
            continue
    return None

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
