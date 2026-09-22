# modules/konvolusyon_mean.py

import numpy as np

def konvolusyon_mean_uygula(gorsel: np.ndarray, filtre_boyutu: int = 5) -> np.ndarray:
    """
    Görüntüye mean filter uygular (blur).
    Filtre boyutu tek sayı olmalıdır (3, 5, 7, ...).
    Bu işlem manuel olarak yapılır, OpenCV kullanılmaz.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        filtre_boyutu (int): Filtre boyutu (varsayılan: 5)

    Returns:
        np.ndarray: Blurlanmış görüntü
    """
    # Filtre boyutunun tek sayı olduğunu kontrol et
    if filtre_boyutu % 2 == 0:
        filtre_boyutu += 1  # Tek sayı yap
        
    yukseklik, genislik, kanal_sayisi = gorsel.shape
    sonuc = np.zeros_like(gorsel)
    
    # Kenar pikselleri için padding ekle
    pad = filtre_boyutu // 2
    padded_gorsel = np.pad(gorsel, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
    
    # Filtre ağırlıklarını oluştur (merkez piksel daha ağırlıklı)
    filtre = np.ones((filtre_boyutu, filtre_boyutu))
    merkez = filtre_boyutu // 2
    filtre[merkez, merkez] = 2  # Merkez piksel 2 kat ağırlıklı
    filtre = filtre / np.sum(filtre)  # Normalize et
    
    for y in range(pad, yukseklik + pad):
        for x in range(pad, genislik + pad):
            for k in range(kanal_sayisi):
                # Komşu bölgeyi al
                komsu_bolge = padded_gorsel[y-pad:y+pad+1, x-pad:x+pad+1, k]
                # Ağırlıklı ortalama hesapla
                ortalama = np.sum(komsu_bolge * filtre)
                sonuc[y-pad, x-pad, k] = ortalama

    return sonuc.astype(np.uint8)