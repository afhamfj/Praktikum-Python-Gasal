# 1. Buatlah variabel dengan nama kata benda
# 2. Isikan data pada variabel tersebut sejumlah 17 data
kata_benda = ["Kipas","Meja", "Kursi", "Bulpoin", "Buku", "Laptop", "Tas", "Botol", "Jam", "Lampu", "Kacamata", "Kertas", "Kabel", "Sapu", "Pel", "Pensil", "Baju"]

print("Daftar kata benda indeks ke-3 adalah: {}".format(kata_benda[3]))

# 3. 
kata_benda.append("Peci")

# 4. 
kata_benda.insert(3,"TWS")

# 5. Cetak variabel tersebut menggunakan fungsi for
print("Semua benda: ada {}".format(len(kata_benda)))
for benda in kata_benda:
    print (benda)



