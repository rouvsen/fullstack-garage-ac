# Task - 1
name = input("Enter a name: ")
name = name.lower().strip()

if name == 'aslan':
    print('Aslan emi ogludur')
elif name == 'imran':
    print('Imran dayi ogludur')
elif name == 'afaq':
    print('Afaq bibi qizidir')
elif name == 'uzeyir':
    print('Uzeyir xala ogludur')
elif name == 'shahin':
    print('Shahin yaxin dostdur')
elif name == '':
    print('Siz ad daxil etmediniz')
else:
    print(f'{name} kimdir? Men onu tanimadim..')