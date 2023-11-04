import os

clientAnswer = int(input("(1) TXT Faylini sil (2) Melumat Elave et: "))

if clientAnswer == 1:
    if os.path.exists("text.txt"):
        os.remove("text.txt")
        print("text.txt file deleted.")
    else:
        print("text.txt file yaradin, sonra silmek ucun cehd edin..")
elif clientAnswer == 2:
    with open("text.txt", "a") as f:
        f.write("Value\n")
        print("Deyer elave edildi")
else:
    print("Daxil edilen secim 1 ve ya 2 deyil !!")