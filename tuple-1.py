# Definisi data
data_pegawai = [("John", "Manager", 3000000), ("Alice", "Staff", 2500000), ("Bob", "Staff", 2500000)]

# Menghitung total gaji
total_gaji = 0
for nama, jabatan, gaji in data_pegawai:
    total_gaji += gaji
    print(f"{nama} ({jabatan}): Rp{gaji}")

print(f"Total Gaji: Rp{total_gaji}")

# Dalam contoh ini, kita menggunakan tuple untuk menyimpan data pegawai yang terdiri dari nama, jabatan, dan gaji. 
# Kemudian, kita menggunakan perulangan for untuk menghitung total gaji dan mencetak nama, jabatan, dan gaji tiap pegawai.

# Untuk menjalankan program ini, kita bisa menjalankan baris kode yang ada di bawah definisi data. 
# Dalam contoh ini, kita menggunakan data pegawai yang berisi tiga pegawai: "John" sebagai manager, "Alice" sebagai staff, dan "Bob" sebagai staff. 
# Gaji tiap pegawai diambil dari nilai yang ada di tuple.