# modules/gri_donusum.py

import numpy as np

def gri_donusum_uygula(gorsel: np.ndarray) -> np.ndarray:
    """
    RGB formatındaki görüntüyü gri tonlamalı hale getirir.
    OpenCV fonksiyonları kullanılmadan, manuel olarak uygulanır.

    Args:
        gorsel (np.ndarray): RGB formatında giriş görüntüsü

    Returns:
        np.ndarray: Gri tonlamalı görüntü (tek kanallı değil, 3 kanallı RGB)
    """

    # R, G, B bileşenlerini ayır
    R = gorsel[:, :, 0]
    G = gorsel[:, :, 1]
    B = gorsel[:, :, 2]

    # Gri değeri hesapla
    gri = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

    # Tek kanal --> 3 kanal formatına dönüştür (Streamlit görselleştirmesi için)
    gri_3_kanal = np.stack((gri,)*3, axis=-1)

    return gri_3_kanal