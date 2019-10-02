import pyodbc

#Concept of 'Strong Params'
    #Never ever does trust user inputs
    #Avoid SQL injections
    #Filter for SQL injections

class Connect_ms_server():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.__filter_query(query)

    def sql_query_fetchone(self, query):
        return self.sql_query(query).fetchone()

    def print_all_records_from_table(self, table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
                print(record)

    def avg_price_of_products(self):
        avg_price = self.__filter_query('SELECT AVG(Unitprice) FROM Products').fetchone()
        print(avg_price)

    def avg_price_of_products_2(self):
        query = self.__filter_query('SELECT * FROM Products')
        prices = []

        while True:
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
            return (sum(prices)/len(prices))



# CRUD

#Create 1 entry
    #use INSERT
    #the cursor cannot make transaction (go to documentation to check)

#Read all entries
    #fetch all record and return as a list or dictionaries
#Read one entry
    #fetch a specific record
    #get one value using ID


#Update one entry
    #the id of the record to update
    # Update the sepcific record

#Destroy / One entry
    #The id of specific record
    #Destroy the record