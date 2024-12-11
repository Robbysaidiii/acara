import streamlit as st
import pandas as pd

def tampilkan_tabel_excel():
    st.title("Rundown acara")

    try:
        # Membaca file Excel langsung dari path
        file_path = 'Rundown.xlsx'  # Ganti dengan path file Excel Anda
        df = pd.read_excel(file_path)
        
        # Menampilkan tabel interaktif
        st.write("Tabel Data:")
        st.dataframe(df)

       
    except FileNotFoundError:
        st.error(f"File '{file_path}' tidak ditemukan. Pastikan file ada di direktori yang benar.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")

# Menjalankan aplikasi
if __name__ == "__main__":
    tampilkan_tabel_excel()
