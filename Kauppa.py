import sqlite3
from sqlite3 import Error
from KauppaDAO import *

class Kauppa:

    
        
            
            s = int(input('Hei tervetuloa kauppaan. Valitse 1 jo haluat nähdä kaikki tuotteet. Valitse 2 jos haluat lisätä asiakkuuden: '))

            if s == 1:
                products = database_connection.select_all_products()
                print(products)
        
    
        
            if s == 2:
                
                nimi = input('Anna nimi: ')
                m = database_connection.create_customer(nimi)

            if s == 3:
                

                    TuoteNimi = input('Lisää tuote: Nimi ')
                    TuoteHinta = input('Lisää tuote: Hinta ')
                    lt = database_connection.add_products(TuoteNimi, TuoteHinta)


            else:
                print('Ei toimi')

    