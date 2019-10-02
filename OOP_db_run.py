from OOP_db_connect import *

server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
db_nw = Connect_ms_server(server, database, username, password)
print(db_nw)
print(db_nw.conn_nwdb)

rows = db_nw.cursor.execute('SELECT * FROM Products').fetchone()
print(rows)

print(db_nw.sql_query("SELECT * FROM Products").fetchone())

print(db_nw.avg_price_of_products())

print(db_nw.avg_price_of_products_2())