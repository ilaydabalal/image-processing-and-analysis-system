Kapsamlı Görüntü İşleme ve Analiz Sistemi (Comprehensive Image Processing and Analysis System)

Python ve OpenCV kütüphaneleri kullanılarak geliştirilmiş, Streamlit tabanlı interaktif bir Görüntü İşleme ve Analiz web uygulamasıdır. Proje; temel piksel dönüşümlerinden gelişmiş morfolojik analizlere, filtrelemeden renk uzayı manipülasyonlarına kadar geniş bir yelpazede bilgisayarla görü tekniklerini barındırmaktadır.

Özellikler ve Modüller (Features & Modules)

Temel İşlemler: Görüntü Döndürme, Kırpma, Ölçeklendirme (Yaklaştırma / Uzaklaştırma).

Görüntü İyileştirme: Kontrast Artırma, Histogram Germe, Unsharp Mask ve Gürültü Ekleme/Temizleme.

Filtreleme & Konvolüsyon: Mean filtresi ve konvolüsyon çekirdekleri.

Eşikleme ve Dönüşümler: Binary Dönüşüm, Gri Seviye ve Renk Uzayı Dönüşümleri (RGB, Grayscale, HSV, YCrCb).

Morfolojik İşlemler: Aşındırma (Erosion), Genişletme (Dilation), Açma (Opening) ve Kapama (Closing).

Aritmetik İşlemler: İki görsel üzerinde toplama ve bölme (faktör bazlı) işlemleri.

Raporlama: Yapılan işlemlerin süresini ve detaylarını içeren anlık PDF raporu oluşturma ve indirme.

Kullanılan Teknolojiler (Tech Stack)

Python (Programlama Dili)

Streamlit (Web Arayüzü)

OpenCV (cv2) (Görüntü İşleme Kütüphanesi)

NumPy (Matris ve Piksel İşlemleri)

FPDF (Otomatik PDF Raporlama)

Matplotlib / Pillow (Görsel İşleme Destekleri)

Kurulum ve Çalıştırma (Installation & Running)

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

Depoyu Klonlayın:

git clone https://github.com/kullaniciadi/goruntu_isleme_projesi.git
cd goruntu_isleme_projesi


Gerekli Kütüphaneleri Yükleyin:

pip install streamlit numpy opencv-python Pillow matplotlib fpdf


Uygulamayı Başlatın:

python -m streamlit run main.py


Proje Yapısı (Project Structure)

goruntu_isleme_projesi/
│
├── main.py                 # Ana Streamlit uygulama dosyası
├── gui/                    # Arayüz bileşenleri (Uploader, Selector, Preview, Runner)
├── modules/                # Görüntü işleme algoritmaları ve modülleri
│   ├── dondurme.py
│   ├── binary_donusum.py
│   ├── kontrast_artirma.py
│   ├── kirpma.py
│   ├── olceklendirme.py
│   ├── morfolojik_islemler.py
│   └── aritmetik_islemler.py
└── styles/                 # CSS stil dosyaları
