import numpy as np

def gorsel_boyut_ayarla(gorsel1: np.ndarray, gorsel2: np.ndarray) -> tuple:
    """
    İki görüntüyü aynı boyuta getirir. Küçük olan görüntüyü büyük olanın boyutuna getirir.
    
    Args:
        gorsel1 (np.ndarray): İlk görüntü
        gorsel2 (np.ndarray): İkinci görüntü
        
    Returns:
        tuple: (gorsel1, gorsel2) - Aynı boyuta getirilmiş görüntüler
    """
    h1, w1 = gorsel1.shape[:2]
    h2, w2 = gorsel2.shape[:2]
    
    # Hedef boyutları belirle (en küçük boyutları kullan)
    hedef_h = min(h1, h2)
    hedef_w = min(w1, w2)
    
    # Görüntüleri yeniden boyutlandır
    def yeniden_boyutlandir(gorsel, hedef_h, hedef_w):
        h, w = gorsel.shape[:2]
        yeni_gorsel = np.zeros((hedef_h, hedef_w, 3), dtype=np.uint8)
        
        # Oranları hesapla
        h_oran = hedef_h / h
        w_oran = hedef_w / w
        
        # En yakın komşu yöntemiyle yeniden boyutlandır
        for y in range(hedef_h):
            for x in range(hedef_w):
                # Orijinal görüntüdeki karşılık gelen pikselin koordinatlarını hesapla
                orj_y = min(int(y / h_oran), h - 1)
                orj_x = min(int(x / w_oran), w - 1)
                yeni_gorsel[y, x] = gorsel[orj_y, orj_x]
        
        return yeni_gorsel
    
    return (yeniden_boyutlandir(gorsel1, hedef_h, hedef_w),
            yeniden_boyutlandir(gorsel2, hedef_h, hedef_w))

def gri_tonlama(gorsel: np.ndarray) -> np.ndarray:
    """
    RGB görüntüyü gri tonlamaya dönüştürür.
    
    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        
    Returns:
        np.ndarray: Gri tonlamalı görüntü
    """
    h, w = gorsel.shape[:2]
    gri_gorsel = np.zeros((h, w), dtype=np.uint8)
    
    # Her piksel için gri tonlama değerini hesapla
    for y in range(h):
        for x in range(w):
            # RGB değerlerini al
            r, g, b = gorsel[y, x]
            # Gri tonlama formülü: 0.299*R + 0.587*G + 0.114*B
            gri_deger = int(0.299 * r + 0.587 * g + 0.114 * b)
            gri_gorsel[y, x] = gri_deger
    
    return gri_gorsel

def aritmetik_islem_uygula(gorsel1: np.ndarray, gorsel2: np.ndarray = None, islem: str = "toplama", faktor: float = 1.0) -> np.ndarray:
    """
    İki görüntü arasında aritmetik işlem (toplama, bölme) uygular.
    Eğer ikinci görüntü verilmezse, ilk görüntü ile kendisi arasında işlem yapar.
    Bölme işlemi için görüntüler önce gri tonlamaya dönüştürülür.

    Args:
        gorsel1 (np.ndarray): İlk RGB giriş görüntüsü
        gorsel2 (np.ndarray, optional): İkinci RGB giriş görüntüsü
        islem (str): "toplama" veya "bolme"
        faktor (float): Bölme için bir faktör, varsayılan olarak 1.0 (bölme için)

    Returns:
        np.ndarray: İşlenmiş görüntü
    """
    if gorsel2 is None:
        gorsel2 = gorsel1.copy()

    # Görüntülerin boyutlarını kontrol et ve gerekirse ayarla
    if gorsel1.shape != gorsel2.shape:
        gorsel1, gorsel2 = gorsel_boyut_ayarla(gorsel1, gorsel2)

    if islem == "toplama":
        sonuc = gorsel1.astype(np.int16) + gorsel2.astype(np.int16)
    elif islem == "bolme":
        # Görüntüleri gri tonlamaya dönüştür
        gri_gorsel1 = gri_tonlama(gorsel1)
        gri_gorsel2 = gri_tonlama(gorsel2)
        
        # Sıfıra bölmeyi önle
        gri_gorsel2 = np.where(gri_gorsel2 == 0, 1, gri_gorsel2)
        
        # Bölme işlemini uygula
        sonuc = gri_gorsel1.astype(np.float32) / gri_gorsel2.astype(np.float32)
        sonuc = sonuc * faktor
        
        # Sonucu 3 kanallı görüntüye dönüştür
        h, w = sonuc.shape
        sonuc_rgb = np.zeros((h, w, 3), dtype=np.uint8)
        for y in range(h):
            for x in range(w):
                deger = int(sonuc[y, x])
                sonuc_rgb[y, x] = [deger, deger, deger]
        
        sonuc = sonuc_rgb
    else:
        raise ValueError("İşlem tipi 'toplama' veya 'bolme' olmalı.")

    # Değerleri 0-255 aralığına getir
    sonuc = np.clip(sonuc, 0, 255).astype(np.uint8)

    return sonuc
