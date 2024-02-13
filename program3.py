import time
def input_NIU():
    niu=0
    try:
        int_niu=int(input('masukkan NIU (6 angka): '))
        if int_niu<100000 or int_niu>999999:
            print('NIU harus terdiri dari 6 angka')
            time.sleep(1)
            print('\033[F\033[K', end='', flush=True)
            print('\033[F\033[K', end='', flush=True)
            input_NIU()
        else:
            niu=int_niu
    except:
        print('NIU harus terdiri angka')
        time.sleep(1)
        print('\033[F\033[K', end='', flush=True)
        print('\033[F\033[K', end='', flush=True)
        input_NIU()
    return niu

def input_nilai(x):
    try:
        int_nilai=int(input(f'masukkan nilai {x} (0-100): '))
        if int_nilai<0 or int_nilai>100:
            print('hanya bisa menginputkan 0-100')
            time.sleep(1)
            print('\033[F\033[K', end='', flush=True)
            print('\033[F\033[K', end='', flush=True)
            return input_nilai(x)
        else:
            return int_nilai
        
    except:
        print('nilai harus terdiri angka')
        time.sleep(1)
        print('\033[F\033[K', end='', flush=True)
        print('\033[F\033[K', end='', flush=True)
        return input_nilai(x)
    


a=input_NIU()
tugas=input_nilai('tugas')
laporan=input_nilai('laporan')
k=(tugas+laporan)/2

if k<40:
    print(f'nilai peserta adalah K')
else:
    ujian=input_nilai('ujian')

    nilai_akhir= (tugas/4)+(laporan/4)+(ujian/2)

    if 80<=nilai_akhir<=100:
        print(f'nilai akhir adalah {nilai_akhir} (A)')
    elif 70<=nilai_akhir<80:
        print(f'nilai akhir adalah {nilai_akhir} (B)')
    elif 60<=nilai_akhir<70:
        print(f'nilai akhir adalah {nilai_akhir} (C)')
    elif 50<=nilai_akhir<60:
        print(f'nilai akhir adalah {nilai_akhir} (D)')
    else:
        print(f'nilai akhir adalah {nilai_akhir} (E)')
    

print()
print()
print()
print()