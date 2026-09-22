import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def histogram_uygula(gorsel):
    """
    Histogramı gösterir ve orijinal görseli geri döndürür (değişmez).
    """
    if len(gorsel.shape) == 3:
        gri = (0.3 * gorsel[:, :, 0] + 0.59 * gorsel[:, :, 1] + 0.11 * gorsel[:, :, 2]).astype(np.uint8)
    else:
        gri = gorsel

    plt.figure(figsize=(6, 3))
    plt.hist(gri.ravel(), bins=256, range=(0, 256), color='gray')
    plt.title("Histogram")
    plt.xlabel("Piksel Değeri")
    plt.ylabel("Frekans")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

    return gorsel  # çünkü işlenmiş görüntü yok, sadece gösterim