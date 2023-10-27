# Task - 2
username = 'test'
password = '12345'

usernameClient = input("Enter your username: ")
passwordClient = input("Enter your password: ")

if usernameClient == 'test' and passwordClient == '12345':
    print('Xosh geldiniz')

if usernameClient == '':
    print('Login daxil etmediniz')
if passwordClient == '':
    print('Parol daxil etmediniz')
if usernameClient != username and usernameClient != '':
    print('Login yanlishdir')
if usernameClient == '' and passwordClient == '':
    print('Login ve parol daxil etmediniz')
if passwordClient != password and passwordClient != '':
    print('Parol yanlishdir')
if (usernameClient != username and usernameClient != '') and (passwordClient != password and passwordClient != ''):
    print('Login ve parol yanlishdir')