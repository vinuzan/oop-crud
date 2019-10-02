import pyodbc

server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)
cursor = conn_nwdb.cursor()

rows = cursor.execute("SELECT * FROM orders WHERE ShipCity = 'Rio De Janeiro' OR ShipCity = 'Reims'").fetchall()
print(rows)