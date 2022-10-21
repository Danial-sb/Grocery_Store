import datetime
import mysql.connector

__mydb = None

def get_sql_connection():
  print("Opening mysql connection")
  global __mydb

  if __mydb is None:
    __mydb = mysql.connector.connect(user='root', password='########', database='grocery_store')

  return __mydb
