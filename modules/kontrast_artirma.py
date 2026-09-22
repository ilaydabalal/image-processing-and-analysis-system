# modules/kontrast_artirma.py

import numpy as np

def kontrast_artir(gorsel: np.ndarray, alpha: float = 1.5) -> np.ndarray:
    """
    Görüntünün kontrastını artırır veya azaltır.
    Bu işlem manuel olarak yapılır (OpenCV kullanılmadan).

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        alpha (float): Kontrast oranı (>1 artırır, <1 azaltır)

    Returns:
        np.ndarray: Kontrastı ayarlanmış görüntü
    """
    # 128 merkezli normalleştir, alpha ile çarp, tekrar 128 ekle
    sonuc = (gorsel.astype(np.float32) - 128) * alpha + 128
    sonuc = np.clip(sonuc, 0, 255).astype(np.uint8)

    return sonuc