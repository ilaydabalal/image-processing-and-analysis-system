# modules/gurultu_temizleme.py

import numpy as np

def gurultu_temizle(gorsel: np.ndarray, yontem: str = "median") -> np.ndarray:
    """
    Gürültü temizleme işlemi uygular (median veya mean filtresi).

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        yontem (str): "median" veya "mean"

    Returns:
        np.ndarray: Temizlenmiş görüntü
    """
    Y, X, C = gorsel.shape
    sonuc = np.zeros_like(gorsel)

    for y in range(1, Y - 1):
        for x in range(1, X - 1):
            for c in range(C):
                bolge = gorsel[y-1:y+2, x-1:x+2, c]

                if yontem == "mean":
                    deger = np.mean(bolge)
                elif yontem == "median":
                    deger = np.median(bolge)
                else:
                    raise ValueError("Yöntem 'mean' veya 'median' olmalı")

                sonuc[y, x, c] = deger

    return sonuc.astype(np.uint8)