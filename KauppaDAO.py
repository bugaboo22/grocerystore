import sqlite3
from sqlite3 import Error

class database_connection:

    #create a database connection to a SQLite database 
    def connect_toDB():   
        conn = sqlite3.connect('kauppa.db')   
        try:
            conn
            print('Yhteys onnistui')
        except Error as e:
            print(e)
        
        return conn
    
    def create_customer(cc):
        conn = database_connection.connect_toDB()
        d = conn.cursor()  
        d.execute('INSERT INTO Asiakas(As_nimi) VALUES(?)', [cc])
        conn.commit()

    def delete_customer(dc):
        conn = database_connection.connect_toDB()
        d = conn.cursor() 
        d = conn.execute()
        
    def add_products(m, s):
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        d.execute('INSERT INTO Tuote(Tuote_nimi, Tuote_hinta) VALUES(?,?)', [m, s])
        conn.commit()

    def select_all_products():

        try:
            conn = database_connection.connect_toDB()
            d = conn.cursor()
            sqlite_select_query = ("SELECT * FROM Tuote")
            d.execute(sqlite_select_query)
            rows = d.fetchall()

            for row in rows:
                print(row)       
            d.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

    if __name__ == '__main__':
        connect_toDB()

