import sqlite3
from sqlite3 import Error


class DatabaseConnection:

    #Create a database connection to a SQLite database 
    def connect_toDB():   
        conn = sqlite3.connect('shop.db')   
        try:
            conn
        except Error as e:
            print(e)
        
        return conn

    def create_customer(customerName, customerNumber):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()  
        d.execute('INSERT INTO Customer(CustomerName, CustomerNumber) VALUES(?,?)', [customerName, customerNumber])
        conn.commit()

    def delete_customer(customerNumber):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor() 
        d.execute('DELETE FROM Customer WHERE CustomerNumber=(?)', [customerNumber])
        conn.commit()

    def update_customer(customerOldName, customerNewName):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('UPDATE Customer SET CustomerName=(?) WHERE CustomerName=(?)', [customerNewName, customerOldName])
        conn.commit()

    #Check admin authorization with username and password
    def admin_check(username, password):
        #username = "Admin"
        #password = "1234"
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('SELECT AdminName from Admin WHERE AdminName=(?) AND AdminPassword=(?)', [username, password])
        if not d.fetchone(): 
            print("Login failed")
            return False
        else:
            print("Welcome Admin")
            return True
        
    def add_products(productName, productPrice):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('INSERT INTO Product(ProductName, ProductPrice) VALUES(?,?)', [productName, productPrice])
        conn.commit()

    #Delete product
    def delete_product(removeProduct):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('DELETE FROM Product WHERE ProductName=(?)', [removeProduct])
        conn.commit()

    #Update product name and price
    def update_product(oldProductName, newProductName):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('UPDATE Product SET ProductName=(?) WHERE ProductName=(?)', [newProductName, oldProductName])
        conn.commit()

    def select_all_products():
        try:
            conn = DatabaseConnection.connect_toDB()
            d = conn.cursor()
            sqlite_select_query = ("SELECT * FROM Product")
            d.execute(sqlite_select_query)
            rows = d.fetchall()

            for row in rows:
                print(row)       
            d.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

    def add_to_basket(productName):
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute('INSERT INTO Basket (BasketProductID, BasketProduct, BasketPrice) SELECT * FROM Product WHERE ProductName=(?)', [productName])
        conn.commit()

    def all_basket_items():
      
        try:
            conn = DatabaseConnection.connect_toDB()
            d = conn.cursor()
            sqlite_select_query = ("SELECT * FROM Basket")
            d.execute(sqlite_select_query)
            rows = d.fetchall()

            for row in rows:
                print(row)       
            d.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

    def print_bill():
        conn = DatabaseConnection.connect_toDB()
        d = conn.cursor()
        d.execute("SELECT * FROM Basket")
        with open('Lasku.txt', 'w') as f:
            for line in d:
                f.write(f"{line}\n")
        print('Lasku luotu')

    if __name__ == '__main__':
        connect_toDB()

