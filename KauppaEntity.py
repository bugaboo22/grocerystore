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
                        As_Nimi    TEXT
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
                VALUES ('Juusto', '2e')''') 
            d.executescript('''INSERT INTO Asiakas (As_nimi)
                VALUES ('John')''') 

            try:
                d
                print('Datan lisäys onnistui')
            
            except Error as e:
                print(e)
            
        except Error as e:
                print(e)

 