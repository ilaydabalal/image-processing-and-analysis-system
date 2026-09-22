import streamlit as st

def islem_sec():
    islemler = [
        "🎨 Gri Dönüşüm",
        "⚫⚪ Binary Dönüşüm",
        "🔄 Görüntü Döndürme",
        "✂️ Görüntü Kırpma",
        "🔍 Yaklaştırma / Uzaklaştırma",
        "🌈 Renk Uzayı Dönüşümü",
        "📊 Histogram Genişletme",
        "➕ Aritmetik İşlemler Toplama",
        "➗ Aritmetik İşlemler Bölme",
        "🌗 Kontrast Artırma",
        "🧮 Konvolüsyon (Mean)",
        "🎚️ Tek Eşikleme",
        "🖍️ Kenar Bulma (Prewitt)",
        "🌪️ Gürültü Ekleme",
        "🧼 Gürültü Temizleme",
        "🔪 Unsharp Filtresi",
        "🧱 Morfolojik İşlemler"
    ]
    return st.selectbox("🛠️ Uygulamak İstediğiniz İşlemi Seçin:", islemler)