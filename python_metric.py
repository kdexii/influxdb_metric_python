import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import influxdb

dbName = 'jmeter'

config = {
        'host':     '127.0.0.1',
        'port':     8086,
        'database': 'jmeter'
    }
client = InfluxDBClient(**config)
dfclient = DataFrameClient(host='127.0.0.1', port='8086', database=dbName)
def createQuery():
    client = InfluxDBClient(host='127.0.0.1', port=8086)
    client.create_database(dbName)
def show_db():
    res = client.query('SHOW DATABASES')
    print(res)
print(dfclient)

test = dfclient.query(f'''select * from "jmeter"''')
test['jmeter']