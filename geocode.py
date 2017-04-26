#!/usr/bin/python

#
# Link: https://github.com/tiepologian/python-geocode
# Author: Gianluca Tiepolo
# Version: 0.1
# Description: Python module and command-line tool to get location coordinates from address using Google Maps API
#

import requests, json, sys


class Geocoder:
    def __init__(self, key):
        self.googleKey = key

    def findCoordinates(self, content):
        search = content.replace(" ", "+")
        payload = {'address': search, 'sensor': 'false', 'key': self.googleKey}
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        result = r.json()
        if result['status'] == 'OK':
            root = result['results'][0]
            return (root['geometry']['location']['lat'], root['geometry']['location']['lng'], root['formatted_address'])
        else:
            print
            "ERROR: " + result['error_message']
            sys.exit(1)


# main
def main():
    if len(sys.argv) < 3:
        print
        "Usage: geocode.py API_KEY SEARCH_TERMS"
        sys.exit(1)

    geo = Geocoder(sys.argv[1])
    result = geo.findCoordinates(sys.argv[2])
    print
    "Latitude: %f\nLongitude: %f\nFull Address: %s" % (result[0], result[1], result[2])


if __name__ == '__main__':
    main()
