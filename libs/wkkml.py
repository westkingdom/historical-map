from libs import wksql as sql, globs as gl
import simplekml
kmlpath = gl.kml
conn = gl.conn

def createkml():
    biglist = sql.getpoints(conn)
    k = simplekml.Kml(name="West Kingdom History")
    k.newpoint(name="Start", coords=[(37.2733521,-121.8664598,0)])
    for item in biglist:
        la = float(item[3])
        ln = float(item[4])
        reals = ln,la
        n = str(item[0])
        c = [reals]
        d = ''.join(map(str, ' AS: ' + str(item[1]) + ' \n' + str(item[2])))
        pnt = k.newpoint()
        pnt.name = n
        pnt.description = d
        pnt.coords = c
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/sunny.png'
        pnt.style.labelstyle.color = simplekml.Color.greenyellow

    k.save(kmlpath)


 #   ev = 'event', ye = 'year', fa = 'fulladdr', lat = 'lat', lng = 'long'
