import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# Set page layout
st.set_page_config(page_title="Visualisasi Saham", layout="wide")

# Tambahkan komponen Streamlit
st.title("📊 Dashboard Visualisasi Volume Saham LQ45")
st.markdown("Menggunakan Pygwalker Untuk Visualisasi")

# Load data
df = pd.read_csv("cleaned_data_saham.csv")

# Konversi pygwalker jadi HTML
html = pyg.to_html(df, spec="Final_Visualisasi_PyGWalker.json")

# Tampilkan dalam Streamlit sebagai komponen HTML
components.html(html, height=1000, scrolling=True)
