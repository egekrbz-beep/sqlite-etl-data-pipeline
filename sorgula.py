import sqlite3
baglanti = sqlite3.connect("okul.db")
cursor = baglanti.cursor()
cursor.execute("SELECT * FROM ogrenciler")
kayitlar = cursor.fetchall()
print("---OKUL.DB İÇİNDEKİ VERİLER---")
for satir in kayitlar:
    print(satir)
    baglanti.close()
