import streamlit as st 
from PIL import Image 

st.header('Welcome to HR Analysis Program')

img = Image.open('HR.jpg')
st.image(img)

with st.expander('Decription '):
    st.markdown('Aplikasi ini adalah aplikasi pendeteksi karyawan anda akan termasuk karyawan loyal atau tidak.')
    st.markdown('Coba masukan ciri-ciri karyawan yang ingin anda analisa di page model')
