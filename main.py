import sqlite3

baglanti = sqlite3.connect("veriler.db")
imlec = baglanti.cursor()

# Tabloyu sıfırdan temiz açıyoruz
imlec.execute("DROP TABLE IF EXISTS ogrenciler")
imlec.execute("CREATE TABLE ogrenciler (isim TEXT, notu INTEGER)")

# 5 farklı öğrenci ekliyoruz
ogrenci_listesi = [
    ("Ayşe", 95) ,
    ("Ahmet", 88) ,
    ("Zeynep",82),
    ("Burak", 74),
    ("Can", 88) ,
    ("Elif", 91),
    ("Murat", 65) ,       
]
imlec.executemany("INSERT INTO ogrenciler VALUES (?,?)" , ogrenci_listesi)
baglanti.commit()

# Notu en yüksek İLK 3 kişiyi çekiyoruz
imlec.execute("SELECT * FROM ogrenciler ORDER BY notu DESC LIMIT 3")
ilk_uc = imlec.fetchall()

print("--- EN YÜKSEK NOT ALAN İLK 3 ÖĞRENCİ (TOP 3) ---")
sira = 1
for ogrenci in ilk_uc:
    print(f"{sira}. {ogrenci[0]} - Notu: {ogrenci[1]}")
    sira += 1

baglanti.close()