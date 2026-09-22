# helpers.py

import numpy as np
import cv2
from PIL import Image

def yukle_resim(dosya_yolu: str) -> np.ndarray:
    bgr_image = cv2.imread(dosya_yolu)
    if bgr_image is None:
        raise ValueError("Görsel yüklenemedi. Dosya yolu hatalı olabilir.")
    
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    return rgb_image

def kaydet_resim(resim: np.ndarray, kayit_yolu: str) -> None:
    # Emin olmak için uint8'e çevir
    if resim.dtype != np.uint8:
        resim = resim.astype(np.uint8)

    bgr_image = cv2.cvtColor(resim, cv2.COLOR_RGB2BGR)
    cv2.imwrite(kayit_yolu, bgr_image)

def numpy_to_pil(resim: np.ndarray) -> Image.Image:
    return Image.fromarray(resim)