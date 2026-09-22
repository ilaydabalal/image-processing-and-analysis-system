# modules/esikleme_tek.py

import numpy as np

def esikleme_uygula(gorsel: np.ndarray, esik: int = 128) -> np.ndarray:
    """
    Görüntüye tekli eşikleme uygular.
    Piksel değeri eşikten büyükse 255, değilse 0 yapılır.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        esik (int): Eşikleme değeri (varsayılan 128)

    Returns:
        np.ndarray: Binary (siyah/beyaz) görüntü
    """
    # Gri tonlamaya dönüştür
    gri = (0.3 * gorsel[:, :, 0] + 0.59 * gorsel[:, :, 1] + 0.11 * gorsel[:, :, 2]).astype(np.uint8)

    # Eşikleme işlemi
    binary = np.where(gri >= esik, 255, 0).astype(np.uint8)

    # Tek kanal → 3 kanala dönüştür
    binary_rgb = np.stack((binary,) * 3, axis=-1)

    return binary_rgb