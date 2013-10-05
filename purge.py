#!/usr/bin/python
import json
import time
import couchdb
import csv
import sys

class referid:

  ## connect to db
  def __init__(self):
    print('CONNECTING TO DATABASE')
    DATABASE = sys.argv[1]
    try:
      server = couchdb.Server()
      self.db = server.create(DATABASE) # if database doesn't exist
    except Exception:
      self.db = server[DATABASE] # assuming database exists
    
  ## all documents in database
  def purge(self):
    print('PURGING DOCUMENTS')
    for docfile in self.db:
      doc = self.db[docfile]
      self.db.delete(doc)
      print(doc)
      
if __name__ == '__main__':
  session = referid()
  session.purge()
