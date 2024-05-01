# Mengambil input user untuk jumlah list
jumlah_list = int(input("Masukkan jumlah list: "))

# Mengambil input user untuk setiap elemen dalam list
daftar_list = []
for i in range(jumlah_list):
    elemen_list = input(f"Masukkan elemen ke-{i+1} list: ")
    daftar_list.append(elemen_list.split())

# Memproses data menggunakan metode sort dan revers
daftar_list_diurutkan = []
for list in daftar_list:
    list.sort()
    list.reverse()
    daftar_list_diurutkan.append(list)

# Mencetak data setelah diproses
print("\nDaftar list setelah diurutkan dan dibalik: ")
for i, list in enumerate(daftar_list_diurutkan):
    print(f"List ke-{i+1}: {list}")