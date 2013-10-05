#!/usr/bin/python
import json
import time
import couchdb
import csv

class referid:

  ## connect to db
  def __init__(self):
    database = raw_input("Enter database name: ")
    try:
      server = couchdb.Server()
      self.db = server.create(database) # if database doesn't exist
    except Exception:
      self.db = server[database] # assuming database exists
  
  ## upload from csv
  def upload(self):
    csvfile = raw_input('Enter CSV filename: ')
    with open(csvfile + '.csv', 'rb') as csvfile:
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
