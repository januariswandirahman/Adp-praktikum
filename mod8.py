def baca_data():
    inventaris = []
    try:
        with open('inventaris_buku.txt', 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if len(data) == 6: 
                    buku = {
                        'ISBN': data[0],
                        'Judul': data[1],
                        'Penulis': data[2],
                        'Stok': int(data[3]),
                        'Harga Beli': int(data[4]),
                        'Harga Jual': int(data[5])
                    }
                    inventaris.append(buku)
        print("Data buku berhasil dibaca dari inventaris_buku.txt")
        return inventaris
    except FileNotFoundError:
        print("Error: File inventaris_buku.txt tidak ditemukan!")
        return None

def hitung_keuntungan_dan_buat_laporan(inventaris):
    if not inventaris:
        print("Tidak ada data inventaris untuk diproses")
        return

    for buku in inventaris:
        buku['Potensi Keuntungan'] = (buku['Harga Jual'] - buku['Harga Beli']) * buku['Stok']
    
    try:
        with open('laporan_inventaris.txt', 'w') as file:
            header = "ISBN | Judul | Penulis | Stok | Harga Beli | Harga Jual | Potensi Keuntungan"
            file.write(header + "\n")
            for buku in inventaris:
                line = f"{buku['ISBN']} | {buku['Judul']} | {buku['Penulis']} | {buku['Stok']} | {buku['Harga Beli']} | {buku['Harga Jual']} | {buku['Potensi Keuntungan']}"
                file.write(line + "\n")
        print("Laporan berhasil dibuat: laporan_inventaris.txt")
    except IOError:
        print("Error: Gagal menulis laporan_inventaris.txt")

def analisis_inventaris(inventaris):
    if not inventaris:
        print("Tidak ada data untuk dianalisis")
        return
    buku_max = max(inventaris, key=lambda x: x['Potensi Keuntungan'])
    buku_min = min(inventaris, key=lambda x: x['Potensi Keuntungan'])
    total_inventaris = sum(buku['Stok'] * buku['Harga Beli'] for buku in inventaris)
    perlu_restock = [buku for buku in inventaris if buku['Stok'] < 5]
    print("\n=== HASIL ANALISIS ===")
    print(f"1. Buku dengan potensi keuntungan tertinggi:")
    print(f"   - Judul: {buku_max['Judul']}")
    print(f"   - Penulis: {buku_max['Penulis']}")
    print(f"   - Keuntungan: Rp{buku_max['Potensi Keuntungan']:,}")
    print(f"\n2. Buku dengan potensi keuntungan terendah:")
    print(f"   - Judul: {buku_min['Judul']}")
    print(f"   - Penulis: {buku_min['Penulis']}")
    print(f"   - Keuntungan: Rp{buku_min['Potensi Keuntungan']:,}")
    print(f"\n3. Total nilai inventaris: Rp{total_inventaris:,}")
    print("\n4. Buku yang perlu di-restock (stok < 5):")
    if perlu_restock:
        for buku in perlu_restock:
            print(f"   - {buku['Judul']} (Stok: {buku['Stok']})")
    else:
        print("   Tidak ada buku yang perlu di-restock")

def main():
    print("=== SISTEM INVENTARIS PUSTAKA KITA ===")
    inventaris = baca_data()
    
    if inventaris:
        hitung_keuntungan_dan_buat_laporan(inventaris)
        analisis_inventaris(inventaris)

if __name__ == "__main__":
    main()