# Inisialisasi pesantren sebagai kamus untuk menyimpan data santri
pesantren = {}

while True:
    print("\nMenu:")
    print("1. Tambah Data Santri")
    print("2. Lihat Data Santri")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        Nama = input("Masukkan Nama Santri: ")
        Usia = int(input("Masukkan Usia Santri: "))
        Kelas = input("Masukkan Kelas Santri: ")
        pesantren[Nama] = {'Usia': Usia, 'Kelas': Kelas}
        print(f"Data Santri {Nama} telah ditambahkan")

    elif pilihan == '2':
        if len(pesantren) == 0:
            print("Tidak ada Data Santri yang tersedia")
        else:
            print("\nData Santri:")
            for Nama, data in pesantren.items():
                print(f"Nama: {Nama}, Usia: {data['Usia']}, Kelas: {data['Kelas']}")

    elif pilihan == '3':
        print("Terima Kasih, Program Selesai")
        break

    else:
        print("Pilihan tidak valid. Silahkan pilih 1, 2, atau 3.")
