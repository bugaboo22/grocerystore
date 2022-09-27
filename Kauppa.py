import sqlite3
from sqlite3 import Error
from turtle import hideturtle
from KauppaDAO import *

class Kauppa:

            s = int(input('Hei tervetuloa kauppaan. \n 1 kaikki tuotteet. \n 2 lisää asiakas, \n 3 lisää tuote. \n 4 poista asiakas. \n 5 muokkkaa asiakasta. \n 6 poista tuote \n 7 Lisää ostoskoriin.\n 8 Muokkaa tuotetta '))

            if s == 1:
                products = database_connection.select_all_products()
                print(products)
             
            if s == 2:
                nimi = input('Anna nimi: ')
                numero = input('Anna numero: ')
                m = database_connection.create_customer(nimi, numero)
                print('Asiakas ', {nimi}, {numero}, ' lisätty' )

            if s == 3:
                TuoteNimi = input('Lisää tuote: Nimi ')
                TuoteHinta = input('Lisää tuote: Hinta ')
                lt = database_connection.add_products(TuoteNimi, TuoteHinta)

            if s == 4:
                As_poista = input('Anna asiakkaan nimi, jonka haluat poistaa: ')
                Ap = database_connection.delete_customer(As_poista)
                print(As_poista, ' poistettiin')
            
            if s == 5:
                As_päivitä = input('Anna asiakkaan nimi, jota haluat päivittää: ')
                As_uusi = input('Anna nimi miksi haluat muuttaa: ')
                p = database_connection.update_customer(As_päivitä, As_uusi)

            if s == 6:
                products = database_connection.select_all_products()
                print(products)
                Tuote_poista = input('Poista tuote. Anna nimi: ')
                T_P = database_connection.delete_product(Tuote_poista)
                print(Tuote_poista, ' poistettiin')
                
            if s == 7:
                o = database_connection.select_all_products()
                print(o)
                T_nimi = str(input('Lisää koriin tuote: '))
                p = database_connection.add_to_basket(T_nimi)
                print(T_nimi, ' lisätty koriin: ')
                print('Korin sisältö ', o)

            if s == 8:
                o = database_connection.select_all_products()
                print(o)
                Tuote_päivitä = input('Anna tuotteen nimi, jota haluat päivittää: ')
                Tuote_uusi = input('Anna nimi miksi haluat muuttaa: ')
                g = database_connection.update_product(Tuote_päivitä, Tuote_uusi)

            else:
                print('Ei toimi')

    