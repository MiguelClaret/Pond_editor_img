import streamlit as st
from PIL import Image
from funcoes import *
import numpy as np
import cv2




def editor_img(image, new_largura, new_altura, filtros_selecionados, redimensionar_img):
    image = np.array(image)
    img_redimensionada = image

    if redimensionar_img:
        img_redimensionada = redimensionar_img_func(image, new_largura, new_altura)
    
    for filtro in filtros_selecionados:
        if filtro == "Escala de Cinza":
            img_redimensionada = escala_cinza(img_redimensionada)
        if filtro == "Invertar Cores":
            img_redimensionada = invert_cores(img_redimensionada)
        if filtro == "Aumentar o Contraste":
            img_redimensionada = aumenta_contraste(img_redimensionada)
        if filtro == "Blur":
            img_redimensionada = blur(img_redimensionada)
        if filtro == "Nitidez":
            img_redimensionada = nitidez(img_redimensionada)
        if filtro == "Detectar as Bordas":
            img_redimensionada = detecta_bordar(img_redimensionada)


    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Imagem Original")

    with col2:
        st.image(img_redimensionada, caption="Imagem Editada")



