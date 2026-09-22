import streamlit as st
from PIL import Image

def gorsel_goster(gorsel, baslik=""):
    if gorsel is not None:
        st.image(gorsel, caption=baslik, use_container_width=True)