import csv
import sqlite3

# ==================================================
# 1. ODA: CSV'DEN VERİYİ OKUMA VE TEMİZLEME (EXTRACT + TRANSFORM)
# ==================================================

veriler = []

with open('ogrenciler.csv', mode='r', encoding='utf-8') as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)  # Başlık satırını atla
    
    for satir in okuyucu:
        # Bekçi 1: Metinleri temizle ve standartlaştır
        isim = satir[0].strip().capitalize()
        sehir = satir[2].strip().capitalize()
        
        # Bekçi 2: İsmi olmayanları atla
        if not isim:
            print("Filtre: İsimsiz satır tespit edildi ve elendi.")
            with open('hatalar.log', mode='a', encoding='utf-8') as log_dosyasi:
                log_dosyasi.write("HATA: İsim alanı boş bırakılmış!\n")
            continue
            
        # Bekçi 3: Yaşı sayı olmayanları yakala ve atla
        try:
            yas = int(satir[1])
        except ValueError:
            print(f"Filtre: {isim} adlı kayıtta yaş sayısal değil ('{satir[1]}'), elendi.")
            with open("hatalar.log", mode='a', encoding='utf-8') as log_dosyasi:
                log_dosyasi.write(f"HATA: {isim} adlı kayıtta yaş sayısal değil ('{satir[1]}')\n")
            continue
            
        # Not ortalamasını ondalıklı sayıya çevir
        not_ort = float(satir[3])
        
        # 3 bekçiden de geçen temiz veriyi sepete at
        veriler.append((isim, yas, sehir, not_ort))

print(f"\nTemizlik Tamamlandı! Sepetteki temiz öğrenci sayısı: {len(veriler)}")

# ==================================================
# 2. ODA: VERİTABANINA AKTARMA (LOAD)
# ==================================================

baglanti = sqlite3.connect("okul.db")
cursor = baglanti.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT,
    yas INTEGER,
    sehir TEXT,
    not_ortalamasi REAL
)
""")

cursor.executemany("""
INSERT INTO ogrenciler (isim, yas, sehir, not_ortalamasi)
VALUES (?, ?, ?, ?)
""", veriler)

baglanti.commit()
baglanti.close()

print("Veritabanına aktarım başarılı!")