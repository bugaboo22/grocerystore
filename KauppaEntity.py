import sqlite3
from sqlite3 import Error
from KauppaDAO import *

class Tables:

        conn = database_connection.connect_toDB()
           
        try:    

            queries = ('''
                    DROP TABLE IF EXISTS Asiakas;
                    DROP TABLE IF EXISTS Tuote;
                    DROP TABLE IF EXISTS Ostoskori;
                    DROP TABLE IF EXISTS Lasku;

                    CREATE TABLE Asiakas (
                        As_ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        As_Nimi    TEXT,
                        As_numero TEXT
                    );
                    CREATE TABLE Tuote (
                        Tuote_ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Tuote_nimi    TEXT,
                        Tuote_hinta   TEXT
                    );
                    CREATE TABLE Ostoskori (
                        Ostoskori_ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Asiakas_ID    INTEGER NOT NULL,
                        Ostoskori_sisältö TEXT
                    );
                    CREATE TABLE Lasku (
                        Lasku_ID  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Ostoskori_ID  INTEGER NOT NULL,
                        Lasku_sisältö TEXT
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
            d.executescript('''INSERT INTO Tuote (Tuote_nimi, Tuote_hinta)
                            VALUES  ('Juusto', '2e'),
                                    ('Maito', '2e'),
                                    ('Leipä', '2e'),
                                    ('Megaforce', '1e'),
                                    ('Euroshopper energy drink', '5e'),
                                    ('Mutakakku', '7e'),
                                    ('Kakku', '12e')
                                    ''') 

            d.executescript('''INSERT INTO Asiakas (As_nimi, As_numero)
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

 