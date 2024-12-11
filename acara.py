import streamlit as st
from streamlit_option_menu import option_menu
from halaman import show_home
from kenangan import kenangan
from Rundown import tampilkan_tabel_excel
import time

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    selected_page = option_menu(
        menu_title="Main Menu",
        options=["Home", "Kenangan", "Rundown", "Bagan", "Biaya"],  # Perbaikan nama menu
        icons=["house", "person", "key", "check-circle", "clipboard"],
        menu_icon="cast",
        default_index=0
    )

# Main Content Based on Sidebar Selection
if selected_page == "Home":
    show_home()

elif selected_page == "Kenangan":  # Sesuai dengan nama menu di sidebar
    kenangan()

elif selected_page == "Rundown":
    tampilkan_tabel_excel() # Placeholder untuk halaman "Rundown"

elif selected_page == "Agree":
    st.write("Agree Page: Placeholder content.")

elif selected_page == "Process Class":
    st.write("Process Class Page: Placeholder content.")

# Optional: Add Spinner for Initial Load
with st.sidebar:
    with st.spinner("Loading sidebar..."):
        time.sleep(1)
    st.success("Sidebar berhasil diakses.")
