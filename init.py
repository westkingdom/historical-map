import sys
import pandas as pd
from geopy.geocoders import Nominatim as geo
import wksql as db
import re
import time as ti
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
g = geo()
adds = []
cities = []
zips = []
data = {}
cols = {}
sudict = {"nan": "","na": ""}
geofied = []
cloc = "California. United States"
cards = []
key = ConfigSectionMap("APIS")['apikey']
colnames=[   # renaming the column headings to make more sane
    'event',
    'group',
    'date',
    'year',
    'location',
    'address',
    'city',
    'zip',
    'autocrat',
    'toilets',
    'potable',
    'showers',
    'camping',
    'feast',
    'eq',
    'arch',
    'war',
    'twengiht',
    'contact',
    'badParking',
    'costs',
    'attendance',
    'issues',
    'other'
]

def main():
    bigframe = pd.read_csv('./wkcsv.csv', names=colnames, index_col=False, header=0, na_values='.', dtype=str)
    data = openCsv(bigframe)
    listify(data)
    #mod = recombo(adds, cities, zips)
    #descr = prepDescr()
    refined = getGeo(cols, bigframe)
    todb(refined)
    #createKml(refined)


#Open the CSV file, create a Dataframe, Copy it
#To use later, return the copy
def openCsv(bigframe):
    data = pd.DataFrame.copy(bigframe , deep=True)
    return data


#take DataFrame make a dict
def listify(data):
    for col in data:
        cols[col] = data[col].tolist()

#take prepped data, extract addr return it
def getGeo(cols, bigframe):
    for i in range(0, int(bigframe.shape[0])):
        if "na" not in (str(cols["address"][i]), str(cols["city"][i]), str(cols["zip"][i])):
            try:
                qstring = ''.join(map(str, str(cols["address"][i]))) + ' ' + str(cols["city"][i]) + ' ' + str(cols["zip"][i]) #join each field together, for the query
                print(qstring)
                ststring = replace(qstring,sudict) #strip nan's
                result = g.geocode(ststring)
                geofied = str(cols["event"][i]), str(result.address), str(result.latitude), str(result.longitude)
                ti.sleep(1.0)
                print(geofied)
            except: Exception
            continue
        else:
            continue
    return geofied

def todb(refined):
    db.sqlconnect()
    db.sqlcreate()
    db.dbinstgeo(conn, thing=refined)
    db.sqlclose()



def replace(text,dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
if __name__ == '__main__':
    main()
