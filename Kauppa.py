
from sqlite3 import Error
from KauppaDAO import *

class Kauppa:

        while True:

            s = int(input('Hei tervetuloa kauppaan. '
                        '\n 1 Kaikki tuotteet: \n 2 Liity asiakkaaksi: '
                        '\n 3 lisää tuote: '
                        '\n 4 Poista asiakas. \n 5 Muokkaa asiakastietojasi'
                        '\n 6 Poista tuote '
                        '\n 7 Lisää ostoskoriin.\n 8 Muokkaa tuotetta. '
                        '\n 9 Kaikki korin esineet. \n 10 Tilaa lasku. \n ' ))
            try:
                
                if s == 1:
                    print('Store selection')
                    DatabaseConnection.select_all_products()
                    input('Paina enter poistuaksesti valikoimasta')

                elif s == 2:

                    nimi = input('Anna nimi: ')
                    numero = input('Anna numero: ')  
                    DatabaseConnection.create_customer(nimi, numero)
                    print('Asiakas ', {nimi}, {numero}, ' lisätty' )
                    input('Paina enter palataksesi kauppaan')

                elif s == 3:
        
                    adminName = input('Anna Admin käyttäjänimi: ')
                    adminPassword = input('Anna salasana: ')
                    confirmAdmin = DatabaseConnection.admin_check(adminName, adminPassword)
                    
                    if confirmAdmin is True:

                        tuoteNimi = input('Lisää tuote: Nimi ')
                        tuoteHinta = input('Lisää tuote: Hinta ')
                        DatabaseConnection.add_products(tuoteNimi, tuoteHinta)
                        print('Tuote ', tuoteNimi, tuoteHinta, ' lisättiin.' )
                        input('Paina enter palataksesi kauppaan')  

                    else:
                        print('Väärä salasana')

                elif s == 4:

                    asiakasPoista = input('Anna asiakkaan nimi, jonka haluat poistaa: ')
                    DatabaseConnection.delete_customer(asiakasPoista)
                    print(asiakasPoista, ' poistettiin')
                
                elif s == 5:
                    Asiakas = int(input('Valitse 1 jos haluat muokata nimeäsi. Valitse 2 jos haluat poistaa käyttäjäsi. Valitse 3 jos haluat perua'))
                    if Asiakas == 1:
                        As_päivitä = input('Anna asiakkaan nimi, jota haluat päivittää: ')
                        As_uusi = input('Anna nimi miksi haluat muuttaa: ')
                        DatabaseConnection.update_customer(As_päivitä, As_uusi)
                    elif Asiakas == 2:
                        Poista_asiakas = int(input('Anna numerosi, jotta käyttäjäsi poistetaan: '))
                        DatabaseConnection.delete_customer(Poista_asiakas)
                        print(Poista_asiakas, ' poistettiin')
                    else:
                        print('Peruttu')

                elif s == 6:

                    adminName = input('Anna Admin käyttäjänimi: ')
                    adminPassword = input('Anna salasana: ')
                    confirmAdmin = DatabaseConnection.admin_check(adminName, adminPassword)

                    if confirmAdmin is True:
                        DatabaseConnection.select_all_products()
                        removeProduct = input('Poista tuote. Anna nimi: ')
                        DatabaseConnection.delete_product(removeProduct)
                        print(removeProduct, ' poistettiin')
                    else:
                        print('Väärä numero')

                elif s == 7:
                    DatabaseConnection.select_all_products()
                    tuoteNimi = input('Lisää koriin tuote: ')
                    DatabaseConnection.add_to_basket(tuoteNimi)
                    print(tuoteNimi, ' lisätty koriin: ')
                    

                elif s == 8:

                    adminName = input('Anna Admin käyttäjänimi: ')
                    adminPassword = input('Anna salasana: ')
                    confirmAdmin = DatabaseConnection.admin_check(adminName, adminPassword)
                    if confirmAdmin is True:
                        DatabaseConnection.select_all_products()
                        tuotevanhanimi = input('Anna tuotteen nimi, jota haluat päivittää: ')
                        tuoteuusinimi = input('Anna nimi miksi haluat muuttaa: ')
                        DatabaseConnection.update_product(tuotevanhanimi, tuoteuusinimi)
                        print('Nimeksi muutettiin', tuoteuusinimi)
                    else:
                        print('Väärä numero')

                elif s == 9:
                    print('Kaikki korin esineet: \n' )
                    DatabaseConnection.all_basket_items()
                    
                elif s == 10:
                    DatabaseConnection.print_bill()

            except Error as e:
                print(e) 

