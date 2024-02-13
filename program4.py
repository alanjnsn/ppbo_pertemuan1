angka= int(input('masukkan angka bilangan bulat positif: '))

faktor=[]

for i in range(1,angka+1):
    if angka%i == 0:
        faktor.append(i)

if len(faktor)==2:
    print(f'{angka} adalah angka prima')
else:
    print(f'{angka} bukanlah angka prima')