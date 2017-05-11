import simplekml

from libs import wksql as sql, globs as gl

kmlpath = gl.kml
conn = gl.conn

###
# Connect to db, get all the results with coords
# return in a tuple
# add a point for each thing
###

def createkml():
    biglist = sql.getpoints(conn)
    k = simplekml.Kml(name="West Kingdom History")
    k.newpoint(name="Start", coords=[(37.2733521, -121.8664598, 0)])
    for item in biglist:
        la = float(item[3])  # Stored as a string, convert to float
        ln = float(item[4])  # Stored as a string, convert to float
        reals = ln, la  # make a tuple
        n = ''.join(map(str, ' AS: ' + str(item[1]) + ' ' + str(item[0])))  # get name
        c = [reals]  # assign tuple
        d = str(item[2])  # make nice string for description
        pnt = k.newpoint()  # initialize a new point object
        pnt.name = n  # assign name
        pnt.description = d  # assign description
        pnt.coords = c  # assign coordinates
        pnt.style.iconstyle.icon.href = 'http://heralds.westkingdom.org/WebsiteImages/wk_westkingdom.png'  # grab a vaugley western icon
        pnt.style.labelstyle.color = simplekml.Color.greenyellow  # make labels !ugly

    k.save(kmlpath)  # save the file