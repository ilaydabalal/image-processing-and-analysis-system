# modules/morfolojik_islemler.py

import numpy as np

def morfolojik_islem(gorsel: np.ndarray, islem: str = "erosion") -> np.ndarray:
    """
    Görüntüye morfolojik işlemler uygular: erosion, dilation, opening, closing.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        islem (str): "erosion", "dilation", "opening", "closing"

    Returns:
        np.ndarray: İşlenmiş görüntü
    """
    # Gri → Binary'e dönüştür
    gri = (0.3 * gorsel[:, :, 0] + 0.59 * gorsel[:, :, 1] + 0.11 * gorsel[:, :, 2]).astype(np.uint8)
    binary = np.where(gri >= 128, 255, 0).astype(np.uint8)

    Y, X = binary.shape
    sonuc = binary.copy()

    def erosion(img):
        yeni = np.zeros_like(img)
        for y in range(1, Y - 1):
            for x in range(1, X - 1):
                bolge = img[y-1:y+2, x-1:x+2]
                yeni[y, x] = 255 if np.all(bolge == 255) else 0
        return yeni

    def dilation(img):
        yeni = np.zeros_like(img)
        for y in range(1, Y - 1):
            for x in range(1, X - 1):
                bolge = img[y-1:y+2, x-1:x+2]
                yeni[y, x] = 255 if np.any(bolge == 255) else 0
        return yeni

    if islem == "erosion":
        sonuc = erosion(binary)
    elif islem == "dilation":
        sonuc = dilation(binary)
    elif islem == "opening":
        sonuc = dilation(erosion(binary))
    elif islem == "closing":
        sonuc = erosion(dilation(binary))
    else:
        raise ValueError("İşlem tipi geçersiz. Seçenekler: erosion, dilation, opening, closing")

    # Geri 3 kanallı hale getir
    sonuc_rgb = np.stack((sonuc,) * 3, axis=-1)

    return sonuc_rgb