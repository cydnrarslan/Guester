# 🥂 GUESTER - Akıllı Davetli Yönetim ve OCR Etkinlik Paneli

**Guester**, düğün, kına, nişan, lansman ve kurumsal organizasyonlar için geliştirilmiş; PDF, Word, Görsel (JPEG/PNG) formatındaki davetli listelerini **Akıllı OCR (Optik Karakter Tanıma)** teknolojisi ile otomatik olarak dijital sisteme aktaran ve etkinlik günü **Hostes / Kapı Kontrol Paneli** ile misafir karşılamayı kolaylaştıran modern bir SaaS web uygulamasıdır.

---

## 🌟 Öne Çıkan Özellikler

- 📸 **Akıllı OCR Liste İçe Aktarımı**: El yazısı veya dijital formatlı davetli listesi görsellerini, PDF veya Word belgelerini yükleyin; isim ve masa numaraları otomatik algılansın.
- 🎯 **Fuzzy Matching & Otomatik Düzeltme**: RapidFuzz ve Türkçe karakter optimizasyonu ile hatalı okunan isimleri veri havuzundaki isimlerle akıllıca eşleştirir.
- 📋 **Excel / CSV / JSON İçe Aktarım & Dışa Aktarım**: Davetli listelerinizi tek tıkla yükleyin veya Excel/CSV formatında indirin.
- 🔑 **Hostes & Kapı Giriş Paneli**: Kapı görevlilerine özel şifreli giriş linki ile davetlileri isim veya masa numarasına göre anında aratıp "Geldi / Gelmedi" olarak işaretleyin.
- 👑 **Süper Yönetici & Müşteri Paneli**: Sistem yöneticileri için müşteri ve davetiye yönetimi, hesap aktifleştirme ve şifre sıfırlama sistemleri.
- ✉️ **E-posta İle Şifre Sıfırlama**: Güvenli Google SMTP entegrasyonu ile e-posta onay kodlu şifre sıfırlama.
- 📱 **Mobil Uyumlu Modern Arayüz**: Tüm akıllı telefon, tablet ve bilgisayarlarla %100 uyumlu duyarlı (responsive) UI.

---

## 🚀 Kurulum ve Çalıştırma

### 1. Yerel Geliştirme Ortamı (Local Development)

```bash
# 1. Depoyu klonlayın
git clone https://github.com/kullaniciadi/guester.git
cd guester

# 2. Sanal ortam (venv) oluşturun ve aktifleştirin
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 4. Çevre değişkenlerini ayarlayın (.env.example dosyasını .env olarak kopyalayın)
cp .env.example .env

# 5. Veritabanını başlatın ve uygulamayı çalıştırın
python veritabani.py
python app.py
```

Uygulama varsayılan olarak `http://127.0.0.1:5000` adresinde çalışacaktır.

---

## ⚙️ Çevre Değişkenleri (.env)

Proje kök dizininde bir `.env` dosyası oluşturarak aşağıdaki yapılandırmaları tanımlayabilirsiniz:

```env
SECRET_KEY=guester_gizli_anahtar_buraya
SMTP_PASSWORD=google_uygulama_sifreniz
SUPER_ADMIN_USERNAME=admin
SUPER_ADMIN_PASSWORD=admin_sifreniz
```

---

## 🛠️ Kullanılan Teknolojiler

- **Backend**: Python 3.10+, Flask
- **Veritabanı**: SQLite3
- **OCR Engine**: EasyOCR, OpenCV, RapidFuzz
- **Belge İşleme**: `pdfplumber`, `python-docx`
- **Frontend**: HTML5, CSS3, JavaScript (ES6+), FontAwesome
- **Deployment**: PythonAnywhere, Docker / WSGI hazır

---

## 📂 Proje Dizin Yapısı

```text
guester/
├── app.py                   # Ana Flask Web Uygulaması ve API Uç Noktaları
├── guester_ocr.py           # Guester Akıllı OCR Motoru ve Algoritmaları
├── veritabani.py            # SQLite Veritabanı Oluşturucu ve Şema Betiği
├── templates/               # HTML Arayüz Şablonları
├── static/                  # CSS, JS ve Görsel Varlıkları
├── test_files/              # Örnek Test Listeleri (PDF / JPEG)
├── scripts/                 # Hata Ayıklama Betikleri
├── requirements.txt         # Python Bağımlılıkları
├── README.md                # Proje Dokümantasyonu
└── KURULUM_KILAVUZU.txt     # PythonAnywhere Bulut Kurulum Rehberi
```

---

## 📜 Lisans

Bu yazılım **Ticari Ürün** olarak lisanslanmıştır. İzin almadan çoğaltılamaz ve izinsiz dağıtılamaz.
