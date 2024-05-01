import requests
from bs4 import BeautifulSoup
import os

def download_instagram_profile_picture(username):
    # buat permintaan ke halaman instagram
    url = f'https://www.instagram.com/{username}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # temukan tautan ke gambar profil
    image_link = soup.find('meta', {'property': 'og:image'})['content']

    # buat permintaan ke tautan gambar dan dapatkan konten gambar
    image_content = requests.get(image_link).content

    # simpan gambar ke file
    with open(f'{username}_profile_picture.jpg', 'wb') as handler:
        handler.write(image_content)