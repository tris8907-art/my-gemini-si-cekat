import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. Konfigurasi Halaman
st.set_page_config(page_title="SI-CEKAT", page_icon="🤖")

# 2. Mengambil API Key dari Streamlit Secrets
# Pastikan di Advanced Settings > Secrets Anda sudah menulis: GOOGLE_API_KEY = "KUNCI_ANDA"
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API Key tidak ditemukan. Pastikan sudah memasukkan GOOGLE_API_KEY di Secrets Streamlit.")

# 3. Fungsi untuk mendapatkan respon dari Gemini
def get_gemini_response(input_text, image=None):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if image:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(input_text)
    return response.text

# 4. Antarmuka Pengguna (UI)
st.header("Sistem Informasi Cekat (SI-CEKAT)")
st.write("Asisten AI siap membantu Anda.")

# Input teks
input_prompt = st.text_input("Masukkan pertanyaan atau instruksi: ", key="input")

# Input gambar (opsional)
uploaded_file = st.file_uploader("Pilih gambar jika ada (opsional)...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah.", use_column_width=True)

# Tombol Submit
submit = st.button("Tanya SI-CEKAT")

if submit:
    if input_prompt:
        with st.spinner('Sedang berpikir...'):
            try:
                response = get_gemini_response(input_prompt, image if uploaded_file else None)
                st.subheader("Respon SI-CEKAT:")
                st.write(response)
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")