
nilai = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'E']
indeks = [4.00, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0.00]
konversi = dict(zip(nilai, indeks))

jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))
jumlah_matkul = int(input("Jumlah mata kuliah: "))

data_mahasiswa = []

for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    
    nilai_matkul = []
    for j in range(jumlah_matkul):
        while True:
            n = input(f"Nilai Mata_Kuliah-{j+1}: ").strip().upper()
            if n in konversi:
                nilai_matkul.append(n)
                break
            print(f"Input salah! Gunakan: {', '.join(nilai)}")
    
    ip = sum(konversi[n] for n in nilai_matkul) / jumlah_matkul
    data_mahasiswa.append([ip, nama, nilai_matkul])

data_mahasiswa.sort(reverse=True)

print("\nHasil Perhitungan IP Mahasiswa:")
print("="*60)
print(f"{'No':<3} {'Nama':<15} {'Nilai':<25} {'IP':<5}")
print("-"*60)
for idx, mhs in enumerate(data_mahasiswa, 1):
    print(f"{idx:<3} {mhs[1]:<15} {', '.join(mhs[2]):<25} {mhs[0]:.2f}")
print("="*60)