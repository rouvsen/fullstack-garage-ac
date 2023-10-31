mySet1 = {
    "red",
    "black",
    "yellow"
}
mySet2 = {
    "red",
    "gray",
    "yellow",
    "green"
}

sameElements = []

for el in mySet1:
    for ell in mySet2:
        if el == ell:
            sameElements.append(el)
print(sameElements)