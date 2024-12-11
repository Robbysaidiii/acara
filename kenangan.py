import streamlit as st
import pandas as pd

def kenangan():
    st.title("Moment Makrab")

    # Dropdown untuk memilih acara
    option = st.selectbox(
        "Pilih momen yang ingin ditampilkan:",
        ("Acara 1", "Acara 2", "Acara 3"),
    )
    st.write("Anda memilih:", option)

    # Menampilkan foto dan video berdasarkan pilihan
    if option == "Acara 1":
        st.image("image/budi.jpg", caption="Acara 1: Kegiatan A", use_column_width=True)
        st.video("vidio/daus.mp4")
    elif option == "Acara 2":
        st.image("image/jawa.jpg", caption="Acara 2: Kegiatan B", use_column_width=True)
        st.video("vidio/farhan.mp4")
    elif option == "Acara 3":
        st.image("image/dedy.jpg", caption="Acara 3: Kegiatan C", use_column_width=True)
        st.video("vidio/daus.mp4")


# Main Program
if __name__ == "__main__":
    # Memanggil fungsi kenangan
    kenangan()

 