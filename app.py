import streamlit as st
from PIL import Image

st.title('Mi primera Aplicación')

st.header("En este espacio comienzo a desarrollar mis aplicaciones para Interfaces Multimodales")
st.write('Carlos Benitez')
image = Image.open('broccoli-8174625.jpg')

st.image(image, caption= 'Interfaces Multimodales')

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp ) st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal de tu interfaz", ('Visual','Auditiva','Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('')
