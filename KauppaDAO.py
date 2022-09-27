import sqlite3
from sqlite3 import Error


class database_connection:

    #create a database connection to a SQLite database 
    def connect_toDB():   
        conn = sqlite3.connect('kauppa.db')   
        try:
            conn
        except Error as e:
            print(e)
        
        return conn

    def tables(self, Asiakas, Tuote, Ostoskori, Lasku): 
        self.Asiakas = Asiakas
        self.Tuote = Tuote
        self.Ostoskori = Ostoskori
        self.Lasku = Lasku   
    
    def create_customer(As_nimi, As_num):
        conn = database_connection.connect_toDB()
        d = conn.cursor()  
        d.execute('INSERT INTO Asiakas(As_nimi, As_numero) VALUES(?,?)', [As_nimi, As_num])
        conn.commit()

    def delete_customer(self, As_nimi):
        conn = database_connection.connect_toDB()
        d = conn.cursor() 
        d.execute('DELETE FROM Asiakas WHERE As_nimi=(?)', [As_nimi])
        conn.commit()

    def update_customer(uc, un):
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        d.execute('UPDATE Asiakas SET As_nimi=(?) WHERE As_nimi=(?)', [un, uc])
        conn.commit()

    def add_products(m, s):
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        d.execute('INSERT INTO Tuote(Tuote_nimi, Tuote_hinta) VALUES(?,?)', [m, s])
        conn.commit()

    def delete_product(dp):
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        d.execute('DELETE FROM Tuote WHERE Tuote_nimi=(?)', [dp])
        conn.commit()
    
    def update_product(Vanha_nimi, Uusi_nimi):
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        d.execute('UPDATE Tuote SET Tuote_nimi=(?) WHERE Tuote_nimi=(?)', [Uusi_nimi, Vanha_nimi])
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

    def add_to_basket(Tuote_nimi):
        Tuotteet = database_connection.select_all_products()
        conn = database_connection.connect_toDB()
        d = conn.cursor()
        query = 'INSERT INTO Ostoskori (Ostoskori_sisältö) SELECT * FROM Tuote (Tuote_nimi) WHERE Tuote_nimi=(?)', [Tuote_nimi]
        d.executemany(query)
        conn.commit

    def all_basket_items():
      
        try:
            conn = database_connection.connect_toDB()
            d = conn.cursor()
            sqlite_select_query = ("SELECT * FROM Ostoskori")
            d.execute(sqlite_select_query)
            rows = d.fetchall()

            for row in rows:
                print(row)       
            d.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

    if __name__ == '__main__':
        connect_toDB()

