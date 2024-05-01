import instaloader
ig = instaloader.Instaloader()
uname = input("Masukkan username: ")
ig.download_profile(uname, profile_pic_only = True)