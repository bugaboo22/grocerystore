from sqlite3 import Error
from unicodedata import name
from KauppaDAO import *

class Shop:

        while True:

            s = int(input('Hei tervetuloa kauppaan. '
                        '\n 1 Kaikki tuotteet: \n 2 Liity asiakkaaksi: '
                        '\n 3 lisää tuote: '
                        '\n 4 Muokkaa asiakastietojasi'
                        '\n 5 Poista tuote '
                        '\n 6 Lisää ostoskoriin.'
                        '\n 7 Muokkaa tuotetta. '
                        '\n 8 Kaikki korin esineet.'
                        '\n 9 Tilaa lasku. \n ' ))
            try:
                
                if s == 1:
                    print('Store selection')
                    DatabaseConnection.select_all_products()
                    input('Paina enter poistuaksesti valikoimasta')

                elif s == 2:
                    name = input('Anna nimi: ')
                    number = input('Anna numero: ')  
                    DatabaseConnection.create_customer(name, number)
                    print('Asiakas ', name, number, ' lisätty' )
                    input('Paina enter palataksesi kauppaan')

                elif s == 3:
                    adminName = input('Anna Admin käyttäjänimi: ')
                    adminPassword = input('Anna salasana: ')
                    confirmAdmin = DatabaseConnection.admin_check(adminName, adminPassword)
                    
                    if confirmAdmin is True:
                        productName = input('Lisää tuote: Nimi ')
                        productPrice = input('Lisää tuote: Hinta ')
                        DatabaseConnection.add_products(productName, productPrice)
                        print('Tuote ', productName, productPrice, ' lisättiin.' )
                        input('Paina enter palataksesi kauppaan ')  

                    else:
                        print('Väärä salasana')

                elif s == 4:
                    customer = int(input('Valitse 1 jos haluat muokata nimeäsi. Valitse 2 jos haluat poistaa käyttäjäsi. Valitse 3 jos haluat perua '))
                    if customer == 1:
                        customerUpdate = input('Anna asiakkaan nimi, jota haluat päivittää: ')
                        customerNewName = input('Anna nimi miksi haluat muuttaa: ')
                        DatabaseConnection.update_customer(customerUpdate, customerNewName)
                    elif customer == 2:
                        removeCustomer = int(input('Anna numerosi, jotta käyttäjäsi poistetaan: '))
                        DatabaseConnection.delete_customer(removeCustomer)
                        print(removeCustomer, ' poistettiin')
                    else:
                        print('Peruttu')

                elif s == 5:
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

                elif s == 6:
                    DatabaseConnection.select_all_products()
                    productName = input('Lisää koriin tuote: ')
                    DatabaseConnection.add_to_basket(productName)
                    print(productName, ' lisätty koriin: ')
                    
                elif s == 7:
                    adminName = input('Anna Admin käyttäjänimi: ')
                    adminPassword = input('Anna salasana: ')
                    confirmAdmin = DatabaseConnection.admin_check(adminName, adminPassword)
                    if confirmAdmin is True:
                        DatabaseConnection.select_all_products()
                        productOldName = input('Anna tuotteen nimi, jota haluat päivittää: ')
                        productNewName = input('Anna nimi miksi haluat muuttaa: ')
                        DatabaseConnection.update_product(productOldName, productNewName)
                        print('Nimeksi muutettiin', productNewName)
                    else:
                        print('Väärä numero')

                elif s == 8:
                    print('Kaikki korin esineet: \n' )
                    DatabaseConnection.all_basket_items()
                    
                elif s == 9:
                    print('Sinun laskusi tulostettiin: \n' )
                    DatabaseConnection.print_bill()

            except Error as e:
                print(e) 

