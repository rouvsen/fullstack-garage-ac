try:
    enteredOperation = int(input('Daxil edin\nVurma (1), Çıxma (2), Toplama (3), Bölmə (4): '))
    enteredNum1 = int(input('Eded daxil edin: '))
    enteredNum2 = int(input('Eded daxil edin: '))
except:
    print('Xahis edirik yalniz reqem daxil edin')

def calculatorFunction():
    if enteredOperation == 1:
        print(f'{enteredNum1} * {enteredNum2} = ' + str((enteredNum1 * enteredNum2)))
    elif enteredOperation == 2:
        print(f'{enteredNum1} - {enteredNum2} = ' + str((enteredNum1 - enteredNum2)))
    elif enteredOperation == 3:
        print(f'{enteredNum1} + {enteredNum2} = ' + str((enteredNum1 + enteredNum2)))
    elif enteredOperation == 4:
        try:
            print(f'{enteredNum1} / {enteredNum2} = ' + str((enteredNum1 / enteredNum2)))
        except:
            print('Ededi sifira bolmek olmaz!')
    else:
        print('Bele bir emeliyyat movcud deyil..')

calculatorFunction()