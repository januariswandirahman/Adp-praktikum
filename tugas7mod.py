n = int(input(" Masukkan  banyak jumlah  data n ="))

def vt_dan_s(v0, a, t):
    vt = v0 + a * t
    s = v0 * t + 0.5 * a * t ** 2
    return vt, s

def input_data(n):
    data = [ ]
    for i in range(n):
        print(f" n ke-{i+1}:")
        v0 = float(input(" Kecepatan  awal (m/s): "))
        a = float(input(" Percepatan (m/s^2): "))
        t = float(input(" Waktu (s): "))
        Kecepatan_akhir, jarak = vt_dan_s(v0, a, t)
        data.append((v0, a, t, Kecepatan_akhir, jarak))
    return data

data = input_data(n)
print()
print('TABEL HASIL PERHITUNGAN  GLB DAN GLBB')
def print_data(data):
    print(" ------------------------------------------------------------------------")
    print(" | n | Kecepatan awal  | Percepatan | Waktu | Kecepatan Akhir | Jarak   |")
    print(" ------------------------------------------------------------------------")
    i = 1
    for kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak in data:
        print(f" | {i:<1} | {kecepatan_awal:<15.0f} | {percepatan:<10.0f} | {waktu:<5.0f} | {kecepatan_akhir:<15.0f} | {jarak:<6.0f} | ")
        i+=1 
    print(" ------------------------------------------------------------------------")

print_data(data)
