import streamlit as st
import os
import cv2
import numpy as np
from datetime import datetime
import traceback

def sonucu_kaydet(gorsel):
    if st.button("💾 Görseli Kaydet"):
        try:
            if gorsel is None:
                st.error("❌ Görsel bulunamadı.")
                return
            if not isinstance(gorsel, np.ndarray):
                st.error("❌ Görsel geçerli bir NumPy dizisi değil.")
                return

            st.write(f"📷 Görsel boyutları: {gorsel.shape}")

            # Kullanıcının ana dizininde outputs klasörü oluştur
            klasor = os.path.join(os.path.expanduser("~"), "GorselIslemeCikti")
            os.makedirs(klasor, exist_ok=True)
            st.write(f"📁 Klasör oluşturuldu veya mevcut: {klasor}")

            # Dosya adını oluştur
            dosya_adi = f"sonuc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            tam_yol = os.path.join(klasor, dosya_adi)
            st.write(f"💾 Kaydedilecek dosya yolu: {tam_yol}")

            # Alfa kanalı varsa RGB'ye dönüştür
            if len(gorsel.shape) == 3 and gorsel.shape[-1] == 4:
                gorsel = cv2.cvtColor(gorsel, cv2.COLOR_RGBA2RGB)

            gorsel_bgr = cv2.cvtColor(gorsel, cv2.COLOR_RGB2BGR)
            cv2.imwrite(tam_yol, gorsel_bgr)

            st.success(f"✅ Görsel kaydedildi: {tam_yol}")
        except Exception as e:
            st.error(f"❌ Hata oluştu: {e}")
            st.write(f"📋 Hata detayları: {traceback.format_exc()}")