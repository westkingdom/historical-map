import json
from libs import wksql as sql

def getdump():
    json_output = json.dumps(jsonquery)
    jsonquery = sql.pntstojson("select * from wkhist limit %s", (3,))