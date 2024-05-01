import random

# Membuat list kosong
angka_acak = []

# Menambah 10 angka acak ke dalam list
for i in range(10):
    angka_acak.append(random.randint(1, 100))

# Menghapus angka acaka dari list
angka_acak.remove(random.choice(angka_acak))

# Mencetak angka2 acak yang ada di dalam list
print("Angka2 acak yang ada di dalam list: ")
for angka in angka_acak:
    print(angka)