#!/usr/bin/env python3
from pprint import pprint
import json
import http.client, urllib.parse

def http_get(connection, path, dict={}):
 dict['api_key'] = '80f279ddeac242af92b6796cd87cc357'
 dict['file_type'] = 'json'
 
 connection.request('GET', path + '?' + urllib.parse.urlencode(dict))
 response = connection.getresponse()

 if response.status == 200:
   data = response.read()
   return json.loads(data.decode('utf-8'))

 else:
   print ( response.status )
   raise Exception("HTTP call failed: " + response.reason)

url = 'api.stlouisfed.org'

connection = http.client.HTTPSConnection(url)

 

# get the children of the root category

children = http_get(connection, '/fred/category/children')
file = open("metadata.txt", "w")

for c in children['categories']:
    serieses = http_get(connection, '/fred/category/series',{'category_id': c.get('id')})
    for s in serieses['seriess']:
#        print(s)
        metadata = http_get(connection, '/fred/series', {'series_id':s.get('id')})
        for m in metadata['seriess']:
            print(m)
 # get the series in the given category

 # note: some category may not have any series

