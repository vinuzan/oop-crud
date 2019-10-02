import pyodbc #open source package used to connect databse.

# In this file we will make our connection

#Parameters/ variables for connection
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

#Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)

#Create a cursor
#Allows us to execute raeadonly queries on the database
cursor = conn_nwdb.cursor()

#using .execute on cursor
cursor.execute('SELECT * FROM Customers;')

#Fetch rows from cursor - .fetchone()
row = cursor.fetchone()


#.fetchall()
        #This is bad because if databse is too large, it can crash system
rows = cursor.execute('SELECT * FROM Customers').fetchall()
#print(rows) if this is a list, then:

rows = cursor.execute('SELECT * FROM Products').fetchall()
#We can iterate
for record in rows:
    print(record.UnitPrice) #We can access the column of a specific record

#However this is dangerous (limited amount of RAM), because we can clog our machine with too much data.
    #We can use while loops to be more efficient.

rows = cursor.execute('SELECT * FROM Products')

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

