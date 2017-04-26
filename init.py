import sys
import pandas as pd
from geopy.geocoders.googlev3 import GoogleV3 as geo
import re
import time as ti
key="AIzaSyDqNjKIDLMRsBlOC8wlSdgWPET36uSsJjk"
g = geo(key)
adds = []
cities = []
zips = []
data = {}
cols = {}
descrf = []
geofied = []
cloc = "California. United States"
cards = []
colnames=[
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
    createKml(refined)


#Open the CSV file, prep the data, return it
def openCsv(bigframe):
    data = pd.DataFrame.copy(bigframe , deep=True)
    return data

def listify(data):
    for col in data:
        cols[col] = data[col].tolist()


#combine prepped data, in a way we can use
#def recombo(adds,cities,zips) :
#    frames =[adds, cities, zips]
#    rec = pd.concat(frames,axis=1, join='inner')
#   clean = rec.to_records(index='False')
#   return clean

#take prepped data, extract addr return it
def getGeo(cols, bigframe):
    for i in range(0, int(bigframe.shape[0])):
        y = ''.join(map(str, str(cols["address"][i]))) + ' ' + str(cols["city"][i]) + ' ' + str(cols["zip"][i]) + ' ' + cloc
        x = re.sub('^[0-9]|(nan)','',y)
        clean = g.geocode(x)
        geofied = "", str(cols["event"][i]), str(cols["address"][i]), str(cols["zip"][i]), "USA", str(clean.latitude), str(clean.longitude)
        ti.sleep(.25)
        print(geofied)
    return geofied


def createKml(refined) :
   for n in refined :
       templates = [('  <Placemark>\n   <name>{}</name>\n', 'location'),
                    ('   <description>\n    {}\n', 'image'),
                    ('     {}\n', 'address'),
                    ('     {}\n', 'postcode'),
                    ('     {}\n', 'country'),
                    ('     Year: AS <span class="year">{}</span>\n', 'year'),
                    ('     Autocrat: <span class="autocrat">{}</span>\n', 'autocrat'),
                    ('   </description>\n   <Point>\n    <coordinates>{},', 'lat'),
                    ('{}</coordinates>\n   </Point>\n  </Placemark>\n', 'lng')]
       value = lambda field, array: array[refined.index(field)].lstrip().rstrip()
       print
       '''<?xml version="1.0" encoding="UTF-8"?>
       <kml xmlns="http://www.opengis.net/kml/2.2">
        <Document>'''
       # insert values into xml
       for row in refined:
           for t, f in templates:
               print
               t.format(value(f, row)),

       print
       ' </Document>\n</kml>'
if __name__ == '__main__':
    main()
