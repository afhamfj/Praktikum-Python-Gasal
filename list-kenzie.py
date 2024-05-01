# Inisialisasi list kosong
keluarga = []

# Menambahkan anggota keluarga ke list
keluarga.append("Budi")
keluarga.append("Sari")
keluarga.append("Adi")
keluarga.append("Yanti")

# Menampilkan isi list keluarga
print("Anggota keluarga:", keluarga)

# Menghitung jumlah anggota keluarga
jumlah_anggota = len(keluarga)
print("Jumlah anggota keluarga:", jumlah_anggota)

# Mengganti anggota keluarga berdasarkan indeks
keluarga[1] = "Indah"
print("Anggota keluarga setelah diubah:", keluarga)

# Menghapus anggota keluarga berdasarkan nama
keluarga.remove("Yanti")
print("Anggota keluarga setelah menghapus Yanti:", keluarga)

# Menambahkan anggota keluarga ke posisi tertentu
keluarga.insert(2, "Dika")
print("Anggota keluarga setelah menambahkan Dika:", keluarga)

# Mencari indeks anggota keluarga berdasarkan nama
indeks_adi = keluarga.index("Adi")
print("Indeks anggota keluarga Adi:", indeks_adi)

# Memeriksa anggota keluarga berdasarkan nama apakah ada di list atau tidak
if "Yanti" in keluarga:
    print("Yanti ada di list keluarga.")
else:
    print("Yanti tidak ada di list keluarga.")