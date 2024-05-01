# Mendapatkan Waktu Saat Ini
import time

localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", time.strftime("%Y-%m-%d %H:%M:%S", localtime))

#Mendapatkan Waktu yang berformat
import time

localtime = time.asctime(time.localtime(time.time()))
print("Waktu lokal saat ini :", localtime)