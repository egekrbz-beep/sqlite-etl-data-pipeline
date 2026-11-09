import csv

veriler = []  # 1. Boş sepeti masaya koyduk

with open('ogrenciler.csv', mode='r', encoding='utf-8') as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)  # 2. Başlığı çöpe attık
    
    for satir in okuyucu:
        veriler.append(satir)  # 3. Her öğrenciyi sepete attık

# 4. Döngü bitti, sepetin son halini ekrana basalım:
print("Döngü bitti! Sepetin içindeki toplam öğrenci sayısı:", len(veriler))
print("Sepetin tam içeriği:")
print(veriler)