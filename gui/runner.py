import streamlit as st
import numpy as np

# Gerekli modülleri içe aktar
from modules.gri_donusum import gri_donusum_uygula
from modules.renk_donusumleri import renk_donusum_uygula
from modules.histogram_germe import histogram_germe_uygula
from modules.aritmetik_islemler import aritmetik_islem_uygula
from modules.konvolusyon_mean import konvolusyon_mean_uygula
from modules.esikleme_tek import esikleme_uygula
from modules.kenar_bulma_prewitt import kenar_bul_prewitt
from modules.gurultu_ekleme import gurultu_ekle
from modules.gurultu_temizleme import gurultu_temizle
from modules.unsharp import unsharp_filter_uygula
from modules.kirpma import kirpma_uygula
# İşlem haritası: Emoji + Fonksiyon
ISLEM_HARITASI = {
    "🎨 Gri Dönüşüm": gri_donusum_uygula,
    "🌈 Renk Uzayı Dönüşümü": lambda img, tip="rgb": renk_donusum_uygula(img, tip=tip),
    "📊 Histogram Genişletme": histogram_germe_uygula,
    "➕ Aritmetik İşlemler Toplama": lambda img: aritmetik_islem_uygula(img, islem="toplama"),
    "➗ Aritmetik İşlemler Bölme": lambda img, faktor=2: aritmetik_islem_uygula(img, islem="bolme", faktor=faktor),
    "🧮 Konvolüsyon (Mean)": lambda img, filtre_boyutu=5: konvolusyon_mean_uygula(img, filtre_boyutu=filtre_boyutu),
    "🎚️ Tek Eşikleme": lambda img: esikleme_uygula(img, esik=128),
    "🖍️ Kenar Bulma (Prewitt)": kenar_bul_prewitt,
    "🌪️ Gürültü Ekleme": lambda img: gurultu_ekle(img, oran=0.02),
    "🧼 Gürültü Temizleme": lambda img: gurultu_temizle(img, yontem="median"),
    "🔪 Unsharp Filtresi": lambda img: unsharp_filter_uygula(img, alpha=1.0),
    "✂️ Görüntü Kırpma": lambda img: kirpma_uygula(img),

}

# Ana çalıştırma fonksiyonu
def islem_uygula(gorsel: np.ndarray, islem_adi: str, **kwargs) -> np.ndarray:
    """
    Seçilen işleme göre uygun fonksiyonu çalıştırır.
    
    Args:
        gorsel (np.ndarray): İşlenecek görüntü
        islem_adi (str): Uygulanacak işlemin adı
        **kwargs: İşleme özel ek parametreler
        
    Returns:
        np.ndarray: İşlenmiş görüntü
    """
    if islem_adi in ISLEM_HARITASI:
        try:
            return ISLEM_HARITASI[islem_adi](gorsel, **kwargs)
        except Exception as e:
            st.error(f"❌ Hata oluştu: {e}")
            return gorsel
    else:
        st.warning("⚠️ Bu işlem henüz tanımlanmadı.")
        return gorsel