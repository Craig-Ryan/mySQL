import os
import datetime
import pymysql

# Get username
# Just follow for tutorial purposes
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
      cursor.execute("UPDATE Friends SET age = 22 WHERE Name = 'Bob';")
      connection.commit()
finally:
  # Close the connection
  connection.close()