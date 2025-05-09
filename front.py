import streamlit as st
from PIL import Image
from editor import  editor_img
import io
import cv2

st.markdown("# Editor de Imagens do Claret")

uploaded_file = st.file_uploader("Upload a imagem a ser editada", type=["jpg", "jpeg", "png"])

st.markdown("## Redimensionar Imagem?")

redimensionar_img = st.toggle("Redimensionar Imagem", key="toggle_exemplo")

new_largura = 0
new_altura = 0 

if redimensionar_img:
    largura = st.text_input("Digite a largura em px", value="0")
    altura = st.text_input("Digite a altura em px", value="0")
    try:
        new_largura = float(largura.replace(",", "."))
        new_altura = float(altura.replace(",", "."))
        if new_largura <= 0 or new_altura <= 0:
            st.warning("🔴 Largura e altura devem ser maiores que zero.")
    except:
        st.error("⚠️ Digite apenas números válidos com vírgula (ex: 1024,5)")
    

st.markdown("## Escolha quais filtros você quer aplicar na sua imagem:")


opcoes_filtros = ["Escala de Cinza", "Invertar Cores", "Aumentar o Contraste", "Blur", "Nitidez", "Detectar as Bordas"]
cols = st.columns(len(opcoes_filtros))

filtros_selecionados = []

for i, filtro in enumerate(opcoes_filtros):
    with cols[i]:
        if st.checkbox(filtro, key=f"check_{filtro}"):
            filtros_selecionados.append(filtro)

st.markdown("---")
st.success(f"Filtros Selecionados: {', '.join(filtros_selecionados) if filtros_selecionados else 'Nenhum'}")


if uploaded_file:
    image = Image.open(uploaded_file)
    img_nova = editor_img(image, new_largura, new_altura, filtros_selecionados, redimensionar_img)

    img_download = cv2.cvtColor(img_nova, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_download)
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")

    st.download_button(
        label="📥 Baixar imagem editada",
        data=buf.getvalue(),
        file_name="imagem_editada.png",
        mime="image/png"
    )
else:
    st.markdown("Nenhuma Imagem selecionada")