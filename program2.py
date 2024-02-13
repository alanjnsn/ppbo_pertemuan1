suhu= float(input('masukkan suhu: '))

if suhu<0:
    print('Membeku')
elif 0<=suhu<10:
    print('Sangat Dingin') 
elif 10<=suhu<20:
    print('Sejuk')
elif 20<=suhu<30:
    print('Hangat')
elif 30<=suhu<40:
    print('Panas')
else:
    print('Sangat Panas')

print()
print()
print()
print()
