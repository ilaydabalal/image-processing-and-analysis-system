import streamlit as st
import numpy as np
import cv2

def gorsel_yukle(key: str = "default") -> np.ndarray:
    """
    Kullanıcıdan görsel yüklemesini ister ve numpy dizisi olarak döndürür.
    Sadece görüntü okuma için OpenCV kullanılır.
    
    Args:
        key (str): Widget için benzersiz key
        
    Returns:
        np.ndarray: Yüklenen görsel (RGB formatında)
    """
    yuklenen_dosya = st.file_uploader("📂 Görsel Yükleyin", type=["jpg", "jpeg", "png"], key=f"file_uploader_{key}")
    
    if yuklenen_dosya is not None:
        # Dosyayı oku (sadece okuma için OpenCV kullanıyoruz)
        dosya_bytes = np.asarray(bytearray(yuklenen_dosya.read()), dtype=np.uint8)
        gorsel = cv2.imdecode(dosya_bytes, cv2.IMREAD_COLOR)
        
        # BGR'den RGB'ye manuel dönüşüm
        rgb_gorsel = np.zeros_like(gorsel)
        rgb_gorsel[:, :, 0] = gorsel[:, :, 2]  # R = B
        rgb_gorsel[:, :, 1] = gorsel[:, :, 1]  # G = G
        rgb_gorsel[:, :, 2] = gorsel[:, :, 0]  # B = R
        
        return rgb_gorsel
    return None