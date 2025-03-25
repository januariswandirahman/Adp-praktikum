x= int(input("Masukkan jumlah baris: "))
o = int(input("Masukkan jumlah kolom: "))
for i in range(x):
    for j in range(o):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()