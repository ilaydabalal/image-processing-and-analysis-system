import numpy as np
def histogram_germe_uygula(gorsel: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    """
    Histogram germe işlemi ve ardından gamma düzeltmesi ile kontrast arttırma.
    RGB görüntülerde her kanal için ayrı ayrı uygulanır.
    """
    if len(gorsel.shape) == 2:  # Gri görüntü
        min_val = np.min(gorsel)
        max_val = np.max(gorsel)
        if max_val == min_val:
            return gorsel.copy()
        # Histogram germe
        sonuc = (gorsel - min_val) * 255.0 / (max_val - min_val)
        # Gamma düzeltmesi
        sonuc = np.power(sonuc / 255.0, gamma) * 255.0
        return np.clip(sonuc, 0, 255).astype(np.uint8)

    elif len(gorsel.shape) == 3:  # Renkli görüntü
        sonuc = np.zeros_like(gorsel)
        for c in range(3):  # R, G, B kanalları için
            kanal = gorsel[:, :, c]
            min_val = np.min(kanal)
            max_val = np.max(kanal)
            if max_val != min_val:
                # Histogram germe
                kanal_gerilmis = (kanal - min_val) * 255.0 / (max_val - min_val)
                # Gamma düzeltmesi
                kanal_gerilmis = np.power(kanal_gerilmis / 255.0, gamma) * 255.0
                sonuc[:, :, c] = np.clip(kanal_gerilmis, 0, 255)
            else:
                sonuc[:, :, c] = kanal  # Değişiklik yapma
        return sonuc.astype(np.uint8)
    else:
        raise ValueError("Geçersiz görüntü boyutu.")
