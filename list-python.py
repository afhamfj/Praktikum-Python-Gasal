# inisialisasi list kosong
angka_fibonacci = []

# menambahkan angka pertama ke list
angka_fibonacci.append(0)

# menambahkan angka kedua ke list
angka_fibonacci.append(1)

# membuat 20 angka fibonacci
for i in range(2, 10):
    # menghitung angka baru berdasarkan rumus fibonacci
    angka_baru = angka_fibonacci[i-1] + angka_fibonacci[i-2]

    # menambahkan angka baru ke list
    angka_fibonacci.append(angka_baru)

# menampilkan list angka fibonacci
print(angka_fibonacci)