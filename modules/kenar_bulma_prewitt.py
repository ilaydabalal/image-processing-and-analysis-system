# modules/kenar_bulma_prewitt.py

import numpy as np

def kenar_bul_prewitt(gorsel: np.ndarray) -> np.ndarray:
    """
    Prewitt filtresi ile kenar tespiti yapar.
    Bu işlem manuel olarak gerçekleştirilir.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü

    Returns:
        np.ndarray: Kenar görüntüsü (siyah/beyaz)
    """
    # Griye çevir
    gri = (0.3 * gorsel[:, :, 0] + 0.59 * gorsel[:, :, 1] + 0.11 * gorsel[:, :, 2]).astype(np.uint8)

    Y, X = gri.shape
    sonuc = np.zeros_like(gri)

    # Prewitt maskeleri
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    for y in range(1, Y - 1):
        for x in range(1, X - 1):
            bolge = gri[y-1:y+2, x-1:x+2]

            gx = np.sum(prewitt_x * bolge)
            gy = np.sum(prewitt_y * bolge)

            g = np.sqrt(gx**2 + gy**2)

            sonuc[y, x] = min(255, int(g))

    # 3 kanallı hale getir
    kenar_rgb = np.stack((sonuc,)*3, axis=-1)

    return kenar_rgb