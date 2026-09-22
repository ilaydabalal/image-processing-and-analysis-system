<div align="center">

# Kapsamlı Görüntü İşleme ve Analiz Sistemi

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

</div>

---

## Proje Hakkında 
Python ve OpenCV kütüphaneleri kullanılarak geliştirilmiş, **Streamlit** tabanlı interaktif bir **Görüntü İşleme ve Analiz** web uygulamasıdır. Proje; temel piksel dönüşümlerinden gelişmiş morfolojik analizlere, filtrelemeden renk uzayı manipülasyonlarına kadar geniş bir yelpazede bilgisayarla görü tekniklerini barındırmaktadır.

---

## Özellikler ve Modüller

* **Temel İşlemler:** Görüntü Döndürme, Kırpma, Ölçeklendirme (Yaklaştırma / Uzaklaştırma).
* **Görüntü İyileştirme:** Kontrast Artırma, Histogram Germe, Unsharp Mask ve Gürültü Ekleme/Temizleme.
* **Filtreleme & Konvolüsyon:** Mean filtresi ve özelleştirilebilir konvolüsyon çekirdekleri.
* **Eşikleme ve Dönüşümler:** Binary Dönüşüm, Gri Seviye ve Renk Uzayı Dönüşümleri (`RGB`, `Grayscale`, `HSV`, `YCrCb`).
* **Morfolojik İşlemler:** Aşındırma (Erosion), Genişletme (Dilation), Açma (Opening) ve Kapama (Closing).
* **Aritmetik İşlemler:** İki görsel üzerinde toplama ve faktör bazlı bölme işlemleri.
* **Raporlama:** Yapılan işlemlerin süresini ve detaylarını içeren anlık PDF raporu oluşturma ve indirme.

---

## Kullanılan Teknolojiler

| Teknoloji | Açıklama |
| :--- | :--- |
| **Python** | Temel programlama dili |
| **Streamlit** | İnteraktif web arayüzü ve UI bileşenleri |
| **OpenCV (`cv2`)** | Görüntü işleme ve bilgisayarla görü motoru |
| **NumPy** | Matris ve piksel tabanlı yüksek performanslı hesaplamalar |
| **FPDF** | Otomatik PDF rapor çıktısı üretme |
| **Matplotlib / Pillow** | Görsel işleme ve destekleyici kütüphaneler |

---

## Kurulum ve Çalıştırma 

Projeyi kendi bilgisayarınızda yerel ortamda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/kullaniciadi/goruntu_isleme_projesi.git
cd goruntu_isleme_projesi
```

### 2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install streamlit numpy opencv-python Pillow matplotlib fpdf
```

### 3. Uygulamayı Başlatın
```bash
python -m streamlit run main.py
```

---

