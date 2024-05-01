#Contoh sederhana pembuatan tuple pada bahasa pemrograman python

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = ()

#Cara mengakses nilai tuple

print ("tup1[0]: ", tup1[2])
print ("tup2[1:3]: ", tup2[1:3])

tup5 = (12, 34.56)
tup6 = ('abc', 'xyz')

tup7 = tup5 + tup6
print (tup7)

tup = ('fisika', 'kimia', 1993, 2017)
print(tup)

# hapus tuple dengan statement del

del tup

# lalu buat kembali tuple yang baru dengan elemen yang diinginkan

tup = ('Bahasa', 'Literasi', 2020)
print("Setelah menghapus tuple :", tup)