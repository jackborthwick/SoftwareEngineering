#!/usr/bin/env python3

from pprint import pprint
import xml.etree.ElementTree as ET
import sys
import http.client, urllib.parse


#find good functional programming for element tree

def get_protein_id():
    try:
        return sys.argv[1]
    except:
        pass
    
def http_get(connection, proteinID):
 path = "/uniprot/" + proteinID + ".xml"
 connection.request('GET', path ) 
 response = connection.getresponse()

 if response.status == 200:
   data = response.read()
   #pprint (data)
   #file = open("xmlFileUniprot.xml", "w")
   #file.write(data.decode("utf-8"))
   #file.close()
   tree = ET.fromstring(data)
   return tree

 else:
   print ("this failed because there seemingly was not a protein for that protein id")
   print ( response.status )
   raise Exception("HTTP call failed: " + response.reason)

url = 'www.uniprot.org'
connection = http.client.HTTPConnection(url)
protein_id = get_protein_id()
proteinXML = http_get(connection, protein_id)
for neighbor in proteinXML.iter('{http://uniprot.org/uniprot}gene'):
    for neighbor2 in neighbor.iter('{http://uniprot.org/uniprot}name'):
        print (neighbor2.text)


































