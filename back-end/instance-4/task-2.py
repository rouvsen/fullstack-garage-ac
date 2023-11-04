# add mock values to file
with open("text.txt", "a") as f:
    f.write("Python\n")
    f.write("Java\n")
    f.write("JavaScript\n")
# get first and last letters of value
with open("text.txt", "r") as r:
    for el in r.readlines():
        print("first letter: " + el[0], "last letter: " + el[len(el) - 2])