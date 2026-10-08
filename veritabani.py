# -*- coding: utf-8 -*-
#
# GUESTER - Veritabanı Yapılandırma ve Başlatma Betiği
#
import sqlite3

baglanti = sqlite3.connect("guester.db")
imlec = baglanti.cursor()

# Tabloyu sıfırdan kurallara uygun oluşturuyoruz
imlec.execute("""
CREATE TABLE IF NOT EXISTS kullanicilar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_soyad TEXT,
    sifre TEXT,
    email TEXT UNIQUE
)
""")

baglanti.commit()
baglanti.close()

print("Veritabanı başarıyla optimize edildi ve oluşturuldu.")