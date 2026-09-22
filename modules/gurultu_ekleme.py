# modules/gurultu_ekleme.py

import numpy as np

def gurultu_ekle(gorsel: np.ndarray, oran: float = 0.02) -> np.ndarray:
    """
    Görüntüye Salt & Pepper gürültü ekler.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        oran (float): Gürültü oranı (varsayılan: %2)

    Returns:
        np.ndarray: Gürültülü görüntü
    """
    noisy = gorsel.copy()
    toplam_piksel = gorsel.shape[0] * gorsel.shape[1]
    gurultu_sayisi = int(oran * toplam_piksel)

    # Salt gürültüsü (beyaz)
    for _ in range(gurultu_sayisi // 2):
        y = np.random.randint(0, gorsel.shape[0])
        x = np.random.randint(0, gorsel.shape[1])
        noisy[y, x] = [255, 255, 255]

    # Pepper gürültüsü (siyah)
    for _ in range(gurultu_sayisi // 2):
        y = np.random.randint(0, gorsel.shape[0])
        x = np.random.randint(0, gorsel.shape[1])
        noisy[y, x] = [0, 0, 0]

    return noisy