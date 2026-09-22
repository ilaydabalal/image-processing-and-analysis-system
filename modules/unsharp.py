# modules/unsharp.py

import numpy as np

def unsharp_filter_uygula(gorsel: np.ndarray, alpha: float = 4.0) -> np.ndarray:
    """
    Görüntünün keskinliğini artırmak için unsharp filtresi uygular.
    Adımlar:
    1. Orijinal görüntüyü bulanıklaştır
    2. Orijinal görüntüden bulanık görüntüyü çıkar (kenar ve detay bilgisi)
    3. Bu farkı alpha ile çarp
    4. Çarpılmış farkı orijinal görüntüye ekle

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        alpha (float): Keskinlik katsayısı (varsayılan: 4.0)

    Returns:
        np.ndarray: Keskinleştirilmiş görüntü
    """
    # Orijinal görüntüyü float32'ye çevir (daha hassas hesaplama için)
    orijinal = gorsel.astype(np.float32)
    Y, X, C = orijinal.shape
    
    # Bulanıklaştırma için ağırlık matrisi
    agirlik = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]) / 9.0  # Basit ortalama için normalize et
    
    # Padding ekle
    padded = np.pad(orijinal, ((1, 1), (1, 1), (0, 0)), mode='edge')
    bulanık = np.zeros_like(orijinal)
    
    # Bulanıklaştırma
    for y in range(Y):
        for x in range(X):
            for c in range(C):
                bolge = padded[y:y+3, x:x+3, c]
                bulanık[y, x, c] = np.sum(bolge * agirlik)
    
    # Kenar ve detay bilgisini çıkar
    kenar_bilgisi = orijinal - bulanık
    
    # Keskinleştirme
    keskin = orijinal + alpha * kenar_bilgisi
    
    # Değerleri 0-255 aralığına getir ve uint8'e çevir
    keskin = np.clip(keskin, 0, 255).astype(np.uint8)
    
    return keskin