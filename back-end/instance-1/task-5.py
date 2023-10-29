print('SATIRAM AZN , USD , EUR')
print('Aliram AZN , USD , EUR')

satiram = input('Satiram: ')
aliram = input('Aliram: ')

qiymet = int(input("Qiymet: "))

if satiram == 'USD' and aliram == 'AZN':
    qiymet = qiymet * 1.70
if satiram == 'AZN' and aliram == 'USD':
    qiymet = qiymet / 1.70
if satiram == 'USD' and aliram == 'EUR':
    qiymet = qiymet * 0.57
if satiram == 'EUR' and aliram == 'USD':
    qiymet = qiymet / 0.57
if satiram == 'AZN' and aliram == 'EUR':
    qiymet = qiymet / 5
if satiram == 'EUR' and aliram == 'AZN':
    qiymet = qiymet * 5

print(qiymet)