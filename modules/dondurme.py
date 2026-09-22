# modules/dondurme.py

import numpy as np

def dondurme_uygula(gorsel: np.ndarray, derece: int = 90) -> np.ndarray:
    """
    Görüntüyü belirtilen dereceye göre döndürür.
    Bu işlem NumPy ile manuel olarak yapılır (OpenCV kullanılmaz).

    Args:
        gorsel (np.ndarray): RGB formatında giriş görüntüsü
        derece (int): Döndürme açısı (sadece 90, 180, 270 desteklenir)

    Returns:
        np.ndarray: Döndürülmüş görüntü
    """
    if derece == 90:
        # Saat yönünde 90 derece döndürme: Transpose + Flip yatay
        return np.flip(np.transpose(gorsel, (1, 0, 2)), axis=1)

    elif derece == 180:
        # 180 derece: Flip dikey + yatay
        return np.flip(np.flip(gorsel, axis=0), axis=1)

    elif derece == 270:
        # Saat yönünün tersine 90 derece: Transpose + Flip dikey
        return np.flip(np.transpose(gorsel, (1, 0, 2)), axis=0)

    else:
        raise ValueError("❌ Desteklenmeyen açı. Lütfen sadece 90, 180 veya 270 seçin.")