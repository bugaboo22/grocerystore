import sqlite3
from sqlite3 import Error
from KauppaDAO import *

class Tables:

        conn = DatabaseConnection.connect_toDB()
           
        try:    

            queries = ('''
                    DROP TABLE IF EXISTS Customer;
                    DROP TABLE IF EXISTS Product;
                    DROP TABLE IF EXISTS Basket;
                    DROP TABLE IF EXISTS Admin;

                    PRAGMA foreign_keys;
                    PRAGMA foreign_keys = ON;

                    CREATE TABLE Admin (
                        AdminID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        AdminName   TEXT,
                        AdminPassword TEXT
                    );

                    CREATE TABLE Customer (
                        CustomerID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        CustomerName   TEXT,
                        CustomerNumber TEXT
                    );
                    CREATE TABLE Product (
                        ProductID  INTEGER PRIMARY KEY,
                        ProductName   TEXT,
                        ProductPrice TEXT
                    );
                    CREATE TABLE Basket (
                        BasketID INTEGER PRIMARY KEY,
                        BasketProductID INTEGER,
                        BasketProduct TEXT,
                        BasketPrice TEXT
                    );
                    ''')
    
            #CREATE TABLES
            conn.executescript(queries)

            try:
                conn
                print('Uudelleenluonti onnistui')        
            except Error as e:
                print(e)
                               
            #DATA TO DATABASE
            d = conn.cursor()
            d.executescript('''INSERT INTO Product (ProductName, ProductPrice)
                            VALUES  ('Juusto', '2e'),
                                    ('Maito', '2e'),
                                    ('Leipä', '2e'),
                                    ('Megaforce', '1e'),
                                    ('Euroshopper energy drink', '5e'),
                                    ('Mutakakku', '7e'),
                                    ('Mansikkakakku', '12e')
                                    ''') 

            d.executescript('''INSERT INTO Admin (AdminName, AdminPassword)
                            VALUES  ('Admin', 1234)
                                    ''') 

            d.executescript('''INSERT INTO Customer (CustomerName, CustomerNumber)
                            VALUES  ('John', 040392123), 
                                    ('Pekka', 023232323),
                                    ('Jussi', 0231233332),
                                    ('Pirkko', 0231441132),
                                    ('Jerome', 0214412132),
                                    ('Otto', 0232323425),
                                    ('Pavel', 0231551342)
                                    ''') 

            try:
                d
                print('Datan lisäys onnistui')      

            except Error as e:
                print(e)    
                
        except Error as e:
                print(e)

 