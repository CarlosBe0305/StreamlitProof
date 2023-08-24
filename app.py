import streamlit as st
from PIL import Image

st.title('Mi primera Aplicación')

st.header("En este espacio comienzo a desarrollar mis aplicaciones para Interfaces Multimodales")
st.write('Carlos Benitez')
image = Image.open('broccoli-8174625.jpg')

st.image(image, caption= 'Interfaces Multimodales')
