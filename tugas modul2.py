print("WELCOME TO XXI")
print("FILM YANG TERSEDIA:")
print(""" 
|KODE| JUDUL FILM      | HARGA TIKET |
|  1 | CAPTAIN AMERICA | 45.000      |
|  2 | LANGIT TERBELAH | 80.000      |
|  3 | TIGA LASKAR     | 50.000      |
|  4 | BERKAH RAMADAN  | 35.000      |
|  5 | KELUARGA CEMARA | 65.000      |
""")
nama = input('Masukkan nama Anda: ')
kode = int(input('Masukkan KODE FILM: '))
jumlah = int(input('Masukkan jumlah tiket: '))
if kode == 1:
    harga = 45000 * jumlah
    film = "CAPTAIN AMERICA"
elif kode == 2:
    harga = 80000 * jumlah
    film = "LANGIT TERBELAH"
elif kode == 3:
    harga = 50000 * jumlah
    film = "TIGA LASKAR"
elif kode == 4:
    harga = 35000 * jumlah
    film = "BERKAH RAMADAN"
elif kode == 5:
    harga = 65000 * jumlah
    film = "KELUARGA CEMARA"
else:
    print('Kode film tidak valid!')

print(f"Nama: {nama}")
print(f"Film yang dipilih: {film}")
print(f"Jumlah tiket: {jumlah}")
print(f"Total harga sebelum diskon: Rp. {harga}")

if harga >= 250000:
    diskon = harga * 0.35  
    print('Anda mendapatkan diskon 35%')
elif harga >= 100000:
    diskon = harga * 0.15  
    print('Anda mendapatkan diskon 15%')
else:
    diskon = 0  
total_bayar = harga - diskon
print(f"Total harga setelah diskon: Rp. {int(total_bayar)}")
