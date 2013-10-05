#!/usr/bin/env python
# UPLOAD DATABASE
import json
import time
import couchdb
import csv
import sys

class referid:

  ## connect to db
  def __init__(self):
    DATABASE = str(sys.argv[1])
    try:
      server = couchdb.Server()
      self.db = server.create(DATABASE) # if database doesn't exist
    except Exception:
      self.db = server[DATABASE] # assuming database exists
  
  ## upload from csv
  def upload(self):
    CSVFILE = sys.argv[2]
    with open(CSVFILE, 'rb') as csvfile:
      csvreader = csv.reader(csvfile, delimiter='|', quotechar='`')
      headers = csvreader.next() # get first row of headers
      for values in csvreader:
        doc = dict(zip(headers,values))
        doc['manufacture_date'] = str(time.time())
        print(doc) # display it
        try:
          self.db.save(doc) # add it
        except Exception:
          self.db.update(doc)
      
if __name__ == '__main__':
  session = referid()
  session.upload()
