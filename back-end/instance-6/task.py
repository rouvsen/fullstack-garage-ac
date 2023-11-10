#NOTE: Open Sqlite viewer and terminal, watch and enjoy #rouvsen

import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE if not exists User (name varchar(55), surname varchar(70), cart_balance BIGINT, cart_pincode INTEGER)')
cursor.execute("insert into User (name, surname, cart_balance, cart_pincode) values ('Rouvsen', 'Zuckbereng', 99009, 7733)")
connection.commit()

while(True):

    operation = int(input("""
    Dear Rouvsen, currently you\'re in the system. What do you want?
    1 - Kartdan pul cixart
    2 - Karta medaxil et
    3 - Balansi yoxla
    4 - Pin kodu deyis
    5 - Cixis et
    Seciminiz: """))
    
    if(operation == 1):
        mebleg = int(input("Kartdan ne qeder pul cixarmaq isdeyirsiniz? "))
        cursor.execute(f"update User set cart_balance = cart_balance - {mebleg} where name = 'Rouvsen'")
        connection.commit()
        print(f"Balansinizdan {mebleg} azn cixarish etdiniz")
        continue

    elif(operation == 2):
        mebleg = int(input("Karta ne qeder pul medaxil etmek isdeyirsiniz? "))
        cursor.execute(f"update User set cart_balance = cart_balance + {mebleg} where name = 'Rouvsen'")
        connection.commit()
        print(f"Balansiniza {mebleg} azn elave etdiniz")
        continue

    elif(operation == 3):
        mebleg = cursor.execute("select cart_balance from User where name = 'Rouvsen'").fetchone()
        print(f"Sizin cari balansiniz: {mebleg}.")
        continue

    elif(operation == 4):
        newPinCode = int(input("Yeni pin kodunuzu daxil edin: "))
        cursor.execute(f"update User set cart_pincode = {newPinCode} where name = 'Rouvsen'")
        connection.commit()
        print(f"Pin kodunuz yenilendi: {newPinCode}")
        continue

    else:
        print("Sistemden cixish etdiniz..")
        break

connection.close()