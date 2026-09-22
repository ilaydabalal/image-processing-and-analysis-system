import streamlit as st
import time
import numpy as np
import io
from datetime import datetime
from fpdf import FPDF
import cv2
import re

from gui.uploader import gorsel_yukle
from gui.selector import islem_sec
from gui.preview import gorsel_goster
from gui.runner import islem_uygula
from modules.dondurme import dondurme_uygula
from modules.binary_donusum import binary_donusum_uygula
from modules.kontrast_artirma import kontrast_artir
from modules.kirpma import kirpma_uygula
from modules.olceklendirme import olceklendirme_uygula
from modules.morfolojik_islemler import morfolojik_islem
from modules.aritmetik_islemler import aritmetik_islem_uygula

# Zaman biçimlendirme
def zamani_formatla(sure):
    if sure < 1:
        return f"{int(sure * 1000)} ms"
    else:
        return f"{sure:.2f} saniye"

# Unicode karakterleri ve Türkçe karakterleri temizleme
def temiz_nes(text):
    # Türkçe karakterleri ASCII'ye dönüştür
    turkce_to_ascii = {
        'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U',
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'İ': 'I',
        'ö': 'o', 'Ö': 'O',
        'ç': 'c', 'Ç': 'C'
    }
    for turkce, ascii in turkce_to_ascii.items():
        text = text.replace(turkce, ascii)
    # Emoji ve diğer Unicode karakterlerini kaldır
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

# PDF rapor oluşturma (dosyaya yazmak yerine bayt olarak döndür)
def pdf_olustur(algoritma, sure, fark, boyut):
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, temiz_nes("Goruntu Isleme Raporu"), ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Tarih: {tarih}", ln=1)
    pdf.cell(0, 10, f"Algoritma: {temiz_nes(algoritma)}", ln=1)
    pdf.cell(0, 10, f"Islem Suresi: {temiz_nes(sure)}", ln=1)
    pdf.cell(0, 10, f"Degisen Piksel: {fark}", ln=1)
    pdf.cell(0, 10, f"Gorsel Boyutu: {boyut[0]} x {boyut[1]}", ln=1)

    # PDF'yi bayt akışına dönüştür
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()

# Görüntüyü PNG baytlarına dönüştürme
def gorseli_bayta_cevir(gorsel):
    # RGB'den BGR'ye manuel dönüşüm
    bgr_gorsel = np.zeros_like(gorsel)
    bgr_gorsel[:, :, 0] = gorsel[:, :, 2]  # B = R
    bgr_gorsel[:, :, 1] = gorsel[:, :, 1]  # G = G
    bgr_gorsel[:, :, 2] = gorsel[:, :, 0]  # R = B
    
    # Sadece yazma için OpenCV kullanıyoruz
    _, buffer = cv2.imencode(".png", bgr_gorsel)
    return buffer.tobytes()

# Stil yükle
def stil_yukle():
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="📷 Görüntü İşleme Teknikleri", layout="wide")
stil_yukle()

st.title(" Görüntü İşleme Teknikleri Projesi")
st.markdown("Hoş geldiniz! Görsel yükleyin, işlem seçin ve sonucu görün.")

# Görsel yükleme
st.markdown("### Görsel Seçimi")
orijinal_gorsel = gorsel_yukle(key="orijinal")

if orijinal_gorsel is not None:
    yukseklik, genislik = orijinal_gorsel.shape[:2]
    st.info(f"Görsel Boyutu: {genislik} × {yukseklik} px")

    st.markdown("---")
    secilen_islem = islem_sec()
    sonuc = None
    sure = 0

    st.markdown("### Seçilen İşlem: " + secilen_islem)

    # İşlem uygulama
    if secilen_islem == " Görüntü Döndürme":
        derece = st.selectbox("🔁 Döndürme Açısı", [90, 180, 270])
        if st.button(" Uygula", key="btn_dondur"):
            start = time.time()
            sonuc = dondurme_uygula(orijinal_gorsel, derece)
            sure = time.time() - start
            st.success(f"⏱️ Süre: {zamani_formatla(sure)}")

    elif secilen_islem == "Binary Dönüşüm":
        esik = st.slider(" Eşik Değeri", 0, 255, 128)
        if st.button("Uygula", key="btn_binary"):
            start = time.time()
            sonuc = binary_donusum_uygula(orijinal_gorsel, esik)
            sure = time.time() - start
            st.success(f"Süre: {zamani_formatla(sure)}")

    elif secilen_islem == "Kontrast Artırma":
        alpha = st.slider("Kontrast Oranı", 0.5, 3.0, 1.5, step=0.1)
        if st.button(" Uygula", key="btn_kontrast"):
            start = time.time()
            sonuc = kontrast_artir(orijinal_gorsel, alpha)
            sure = time.time() - start
            st.success(f" Süre: {zamani_formatla(sure)}")

    elif secilen_islem == " Görüntü Kırpma":
        x1 = st.number_input("x1 (Sol)", 0, genislik, 50)
        x2 = st.number_input("x2 (Sağ)", 0, genislik, 250)
        y1 = st.number_input("y1 (Üst)", 0, yukseklik, 50)
        y2 = st.number_input("y2 (Alt)", 0, yukseklik, 250)
    
        # Koordinatlar geçerli mi kontrol et
        if x1 >= x2 or y1 >= y2:
            st.error("Geçersiz kırpma koordinatları: x1 < x2 ve y1 < y2 olmalı.")
        elif st.button("Uygula", key="btn_kirpma"):
            start = time.time()
            try:
                sonuc = kirpma_uygula(orijinal_gorsel, int(x1), int(y1), int(x2), int(y2))
                sure = time.time() - start
                st.success(f"⏱️ Süre: {zamani_formatla(sure)}")
            except ValueError as e:
                st.error(f"Hata: {e}")

    elif secilen_islem == "Yaklaştırma / Uzaklaştırma":
        oran = st.slider("Oran", 0.1, 2.0, 0.5, step=0.1)
        if st.button(" Uygula", key="btn_zoom"):
            start = time.time()
            sonuc = olceklendirme_uygula(orijinal_gorsel, oran)
            sure = time.time() - start
            st.success(f"Süre: {zamani_formatla(sure)}")

    elif secilen_islem == "Morfolojik İşlemler":
        secim = st.selectbox("İşlem Türü", ["erosion", "dilation", "opening", "closing"])
        if st.button("Uygula", key="btn_morfoloji"):
            start = time.time()
            sonuc = morfolojik_islem(orijinal_gorsel, secim)
            sure = time.time() - start
            st.success(f"Süre: {zamani_formatla(sure)}")
            
    elif secilen_islem == "Aritmetik İşlemler Toplama":
        st.markdown("### İkinci Görsel Seçimi")
        ikinci_gorsel = gorsel_yukle(key="ikinci_toplama")
        if ikinci_gorsel is not None:
            if st.button("Uygula", key="btn_aritmetik_toplama"):
                start = time.time()
                sonuc = aritmetik_islem_uygula(orijinal_gorsel, ikinci_gorsel, islem="toplama")
                sure = time.time() - start
                st.success(f"Süre: {zamani_formatla(sure)}")

    elif secilen_islem == "Aritmetik İşlemler Bölme":
        st.markdown("### İkinci Görsel Seçimi")
        ikinci_gorsel = gorsel_yukle(key="ikinci_bolme")
        if ikinci_gorsel is not None:
            st.markdown("### Bölme Faktörü")
            faktor = st.slider("Görüntüyü bölmek için kullanılacak faktör (1-10 arası)", 
                            min_value=1.0, 
                            max_value=10.0, 
                            value=2.0, 
                            step=0.1)
            if st.button(" Uygula", key="btn_aritmetik_bolme"):
                start = time.time()
                sonuc = aritmetik_islem_uygula(orijinal_gorsel, ikinci_gorsel, islem="bolme", faktor=faktor)
                sure = time.time() - start
                st.success(f" Süre: {zamani_formatla(sure)}")

    elif secilen_islem == "Renk Uzayı Dönüşümü":
        secim = st.selectbox("Dönüşüm Tipi", ["rgb", "grayscale", "hsv", "ycrcb"])
        if st.button(" Uygula", key="btn_renk_donusum"):
            start = time.time()
            sonuc = islem_uygula(orijinal_gorsel, secilen_islem, tip=secim)
            sure = time.time() - start
            st.success(f"⏱️ Süre: {zamani_formatla(sure)}")

    elif secilen_islem == " Konvolüsyon (Mean)":
        filtre_boyutu = st.slider("Filtre Boyutu", 3, 15, 5, 2)
        if st.button("️ Uygula", key="btn_konvolusyon"):
            start = time.time()
            sonuc = islem_uygula(orijinal_gorsel, secilen_islem, filtre_boyutu=filtre_boyutu)
            sure = time.time() - start
            st.success(f" Süre: {zamani_formatla(sure)}")

    else:
        if st.button("️ Uygula", key="btn_normal"):
            start = time.time()
            sonuc = islem_uygula(orijinal_gorsel, secilen_islem)
            sure = time.time() - start
            st.success(f" Süre: {zamani_formatla(sure)}")

    # Sonuç gösterimi ve indirme
    if sonuc is not None:
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Orijinal Görsel")
            gorsel_goster(orijinal_gorsel)
        with col2:
            st.markdown("#### İşlenmiş Görsel")
            gorsel_goster(sonuc)

        # Görüntüyü indirme
        st.markdown("###  İşlenmiş Görüntüyü İndir")
        gorsel_bayt = gorseli_bayta_cevir(sonuc)
        dosya_adi = f"sonuc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        st.download_button(
            label="Görüntüyü İndir",
            data=gorsel_bayt,
            file_name=dosya_adi,
            mime="image/png"
        )

        # PDF raporunu indirme
