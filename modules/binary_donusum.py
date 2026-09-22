# modules/binary_donusum.py

import numpy as np

def binary_donusum_uygula(gorsel: np.ndarray, esik: int = 128) -> np.ndarray:
    """
    Giriş RGB görüntüsünü önce griye, sonra da binary hale getirir.
    İşlem manuel olarak yapılır. (OpenCV fonksiyonu kullanılmaz)

    Args:
        gorsel (np.ndarray): RGB formatında giriş görüntüsü
        esik (int): Eşik değeri (0-255)

    Returns:
        np.ndarray: Binary görüntü (3 kanallı)
    """

    # RGB'den gri tonlamaya geçiş
    gri = (0.299 * gorsel[:, :, 0] +
           0.587 * gorsel[:, :, 1] +
           0.114 * gorsel[:, :, 2]).astype(np.uint8)

    # Binary dönüştürme
    binary = np.where(gri >= esik, 255, 0).astype(np.uint8)

    # Tek kanallı görüntüyü 3 kanallı hale getir
    binary_3_kanal = np.stack((binary,) * 3, axis=-1)

    return binary_3_kanal