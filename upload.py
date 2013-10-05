#!/usr/bin/python
import json
import time
import couchdb
import csv
import sys

class referid:

  ## connect to db
  def __init__(self):
    DATABASE = sys.argv[1]
    try:
      server = couchdb.Server()
      self.db = server.create(DATABASE) # if database doesn't exist
    except Exception:
      self.db = server[DATABASE] # assuming database exists
  
  ## upload from csv
  def upload(self):
    CSVFILE = sys.argv[2]
    with open(CSVFILE, 'rb') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      headers = csvreader.next() # get first row of headers
      for values in csvreader:
        doc = dict(zip(headers,values))
        print(doc) # display it
        self.db.save(doc) # add it
  
  ## get single document
  def get(self):
    docfile = raw_input('Enter Doc key to GET: ')
    doc = self.db[docfile]
    print(doc)
  
  ## single document
  def delete(self):
    docfile = raw_input('Enter Doc key to DELETE: ')
    doc = self.db[docfile]
    self.db.delete(doc)
    print(doc)
    
  ## all documents in database
  def purge(self):
    for docfile in self.db:
      doc = self.db[docfile]
      self.db.delete(doc)
      print(doc)
      
if __name__ == '__main__':
  session = referid()
  session.upload()
