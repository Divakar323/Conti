import mysql.connector
import base64
from PIL import Image
import io 
  
# For security reasons, never expose your password
  
# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="studentdb"  # Name of the database
)
  
# Create a cursor object
cursor = mydb.cursor()
  
# Open a file in binary mode
file = open('Picture.png','rb').read()
  
# We must encode the file to get base64 string
file = base64.b64encode(file)
  
# Sample data to be inserted
args = ('100', 'Sample Name', file)
  
# Prepare a query
query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'
  
# Execute the query and commit the database.
cursor.execute(query,args)
mydb.commit()