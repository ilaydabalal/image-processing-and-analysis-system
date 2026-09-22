import numpy as np

def kirpma_uygula(gorsel: np.ndarray, x1: int = None, y1: int = None, x2: int = None, y2: int = None) -> np.ndarray:
    """
    Görüntüyü belirtilen koordinatlara göre veya rastgele bir alan seçerek kırpar.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        x1, y1 (int or None): Kırpma alanının sol üst köşesi
        x2, y2 (int or None): Kırpma alanının sağ alt köşesi

    Returns:
        np.ndarray: Kırpılmış görüntü
    """
    yukseklik, genislik = gorsel.shape[:2]

    # Eğer koordinatlar verilmemişse rastgele üret
    if None in (x1, y1, x2, y2):
        # Minimum kırpma boyutu (örneğin 50x50)
        min_boyut = 50
        max_genislik = genislik - min_boyut
        max_yukseklik = yukseklik - min_boyut

        x1 = np.random.randint(0, max_genislik)
        y1 = np.random.randint(0, max_yukseklik)
        x2 = np.random.randint(x1 + min_boyut, genislik)
        y2 = np.random.randint(y1 + min_boyut, yukseklik)
    else:
        # Koordinatları sınırla
        x1 = max(0, min(x1, genislik))
        x2 = max(0, min(x2, genislik))
        y1 = max(0, min(y1, yukseklik))
        y2 = max(0, min(y2, yukseklik))

        # Koordinatların sırasını kontrol et
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Geçersiz kırpma koordinatları: x1 < x2 ve y1 < y2 olmalı.")

    kirpilmis = gorsel[y1:y2, x1:x2]
    return kirpilmis
