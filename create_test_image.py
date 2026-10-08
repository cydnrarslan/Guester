# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFont

def generate_guest_paper():
    width, height = 900, 1200
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Header / Title
    d.text((260, 40), "GUESTER - DAVETLI MASA LİSTESİ", fill=(0, 0, 0))
    d.line([(50, 90), (850, 90)], fill=(0, 0, 0), width=3)

    # 12 Newly Generated Guest Names with Table Numbers
    guests = [
        ("Kerem Yılmaz", "12"),
        ("Selin Aksoy", "5"),
        ("Tarkan Tevetoğlu", "1"),
        ("Beren Saat", "8"),
        ("Kivanc Tatlitug", "8"),
        ("Asli Enver", "14"),
        ("Serkan Çayoğlu", "14"),
        ("Eda Ece", "21"),
        ("Baris Arduc", "3"),
        ("Elcin Sangu", "3"),
        ("Engin Akyurek", "7"),
        ("Demez Ozdemir", "9")
    ]

    y = 130
    for idx, (name, table) in enumerate(guests, 1):
        line_str = f"{name} - Masa {table}"
        d.text((100, y), line_str, fill=(20, 20, 20))
        d.line([(80, y + 45), (820, y + 45)], fill=(220, 220, 220), width=1)
        y += 60

    img_path = "test_yeni_kagit.png"
    img.save(img_path)
    print(f"Başarıyla yeni synthetic davetli kağıdı oluşturuldu: {img_path}")

if __name__ == "__main__":
    generate_guest_paper()
