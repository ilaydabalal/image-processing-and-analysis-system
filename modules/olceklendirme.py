# modules/olceklendirme.py

import numpy as np

def olceklendirme_uygula(gorsel: np.ndarray, oran: float = 0.5) -> np.ndarray:
    """
    Görüntüyü belirtilen oran kadar büyütür veya küçültür.
    Bu işlem en yakın komşu (nearest neighbor) yöntemiyle manuel yapılır.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        oran (float): Yaklaştırma (>1) veya uzaklaştırma (<1) oranı

    Returns:
        np.ndarray: Yeniden boyutlandırılmış görüntü
    """
    yukseklik, genislik = gorsel.shape[:2]

    yeni_yukseklik = int(yukseklik * oran)
    yeni_genislik = int(genislik * oran)

    yeni_gorsel = np.zeros((yeni_yukseklik, yeni_genislik, 3), dtype=np.uint8)

    for y in range(yeni_yukseklik):
        for x in range(yeni_genislik):
            eski_y = min(int(y / oran), yukseklik - 1)
            eski_x = min(int(x / oran), genislik - 1)

            yeni_gorsel[y, x] = gorsel[eski_y, eski_x]

    return yeni_gorsel