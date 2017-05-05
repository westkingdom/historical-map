import configparser,os
from libs import wksql as wdb

Config = configparser.ConfigParser()
Config.read(os.path.expanduser('./config.ini'))
key = Config.get('APIS', 'apikey')
dbp = Config.get('DBS', 'db_path')
conn = wdb.sqlconnect(dbp)
table = Config.get('DBS', 'db_table')
sudict = {"nan": "", "na": ""}
refined = []
data = {}
cols = {}
colnames = ['event', 'group', 'date',
    'year',  'location', 'address',
    'city', 'zip', 'autocrat',
    'toilets', 'potable', 'showers',
    'camping', 'feast', 'eq',
    'arch', 'war', 'twengiht',
    'contact', 'badParking', 'costs',
    'attendance', 'issues', 'other'
]
kml = Config.get('KML','kml_path')