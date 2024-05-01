import pyshorteners

Link_asli = input("Masukkan Link")
shortener = pyshorteners.Shortener()
result = shortener.tinyurl.short(Link_asli)
print(result)