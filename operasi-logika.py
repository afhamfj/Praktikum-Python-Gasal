Tahun = int(input("Masukkan Tahun: "))
if(Tahun % 4 == 0 and Tahun % 100 !=0 ) or Tahun % 400 == 0:
    print (f"{Tahun} adalah Tahun kabisat")
else:
    print (f"{Tahun} adalah bukan Tahun kabisat")
