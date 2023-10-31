myDict = {
    "id": "1",
    "name": "Test",
    "age": "0"
}
enteredNum = int(input("Enter a number, 1: Keys, 2: Values. Your choice is: "))
if enteredNum == 1:
    print('keys: ' + str(list(myDict.keys())))  # way1
elif enteredNum == 2:
    print('values: ' + ', '.join(myDict.values()))  # way2
else:
    print('You entered wrong num, please try again..')