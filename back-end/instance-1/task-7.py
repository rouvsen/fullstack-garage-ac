adlar = []
inpAd = input('Ad daxil edin: ')

if inpAd == '':
    print('Ad daxil etmediniz')
elif len(inpAd) > 15:
    print('Ad cox uzundur maksimum 15 herf')
else:
    adlar.append(inpAd)
    print('Ad Bazaya ugurla elave olundu')