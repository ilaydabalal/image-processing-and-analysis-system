# modules/renk_donusumleri.py

import numpy as np

def renk_donusum_uygula(gorsel: np.ndarray, tip: str = "rgb") -> np.ndarray:
    """
    RGB görüntüyü farklı bir renk uzayına dönüştürür.

    Args:
        gorsel (np.ndarray): RGB giriş görüntüsü
        tip (str): Dönüştürme tipi ("rgb", "grayscale", "hsv", "ycrcb")

    Returns:
        np.ndarray: Dönüştürülmüş görüntü
    """
    if tip == "rgb":
        # RGB görüntüyü ayrı kanallara böl
        R = gorsel[:, :, 0]
        G = gorsel[:, :, 1]
        B = gorsel[:, :, 2]
        
        # Her kanalı ayrı ayrı göster (diğer kanalları sıfır yaparak)
        R_kanal = np.stack((R, np.zeros_like(R), np.zeros_like(R)), axis=-1)
        G_kanal = np.stack((np.zeros_like(G), G, np.zeros_like(G)), axis=-1)
        B_kanal = np.stack((np.zeros_like(B), np.zeros_like(B), B), axis=-1)
        
        # Kanalları yan yana birleştir
        return np.hstack((R_kanal, G_kanal, B_kanal))
        
    elif tip == "grayscale":
        # Gri dönüşüm (renk uzayı mantığıyla)
        R = gorsel[:, :, 0]
        G = gorsel[:, :, 1]
        B = gorsel[:, :, 2]

        gri = (0.3 * R + 0.59 * G + 0.11 * B).astype(np.uint8)
        gri_3_kanal = np.stack((gri,) * 3, axis=-1)
        return gri_3_kanal
        
    elif tip == "hsv":
        # RGB'den HSV'ye dönüşüm
        R = gorsel[:, :, 0] / 255.0
        G = gorsel[:, :, 1] / 255.0
        B = gorsel[:, :, 2] / 255.0
        
        # V (Value) hesaplama
        V = np.maximum(np.maximum(R, G), B)
        
        # S (Saturation) hesaplama
        min_rgb = np.minimum(np.minimum(R, G), B)
        S = np.where(V == 0, 0, (V - min_rgb) / V)
        
        # H (Hue) hesaplama
        H = np.zeros_like(V)
        
        # R en büyükse
        mask = (V == R) & (V != G)
        H[mask] = 60 * (0 + (G[mask] - B[mask]) / (V[mask] - min_rgb[mask]))
        
        # G en büyükse
        mask = (V == G) & (V != B)
        H[mask] = 60 * (2 + (B[mask] - R[mask]) / (V[mask] - min_rgb[mask]))
        
        # B en büyükse
        mask = (V == B) & (V != R)
        H[mask] = 60 * (4 + (R[mask] - G[mask]) / (V[mask] - min_rgb[mask]))
        
        # Negatif değerleri düzelt
        H[H < 0] += 360
        
        # HSV değerlerini 0-255 aralığına getir
        H = (H / 2).astype(np.uint8)  # H: 0-180
        S = (S * 255).astype(np.uint8)  # S: 0-255
        V = (V * 255).astype(np.uint8)  # V: 0-255
        
        return np.stack((H, S, V), axis=-1)
        
    elif tip == "ycrcb":
        # RGB'den YCrCb'ye dönüşüm
        R = gorsel[:, :, 0]
        G = gorsel[:, :, 1]
        B = gorsel[:, :, 2]
        
        # Y (Luminance) hesaplama
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        
        # Cb (Blue Chrominance) hesaplama
        Cb = 128 + (-0.168736 * R - 0.331264 * G + 0.5 * B)
        
        # Cr (Red Chrominance) hesaplama
        Cr = 128 + (0.5 * R - 0.418688 * G - 0.081312 * B)
        
        # Değerleri 0-255 aralığına getir
        Y = np.clip(Y, 0, 255).astype(np.uint8)
        Cb = np.clip(Cb, 0, 255).astype(np.uint8)
        Cr = np.clip(Cr, 0, 255).astype(np.uint8)
        
        return np.stack((Y, Cr, Cb), axis=-1)

    else:
        raise ValueError("❌ Desteklenmeyen dönüşüm tipi. 'rgb', 'grayscale', 'hsv' veya 'ycrcb' seçin.")