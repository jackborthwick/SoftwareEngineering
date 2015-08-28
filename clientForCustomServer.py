#!/usr/bin/env python
import http.client, urllib.parse
from pprint import pprint
url = 'localhost:8000'
connection = http.client.HTTPConnection(url)
connection.request('POST', "/lets/post/it?definitely=always", "I am changing stuff again") 
response = connection.getresponse()
pprint(response.read())