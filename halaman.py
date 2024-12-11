import streamlit as st

def show_home():
    st.title("Selangkah Treakhir mengukir cerita dan kenangan  ")

    st.markdown(
        """
       Selangkah Terakhir: Menyatukan Cerita, Mengukir Kenangan" menggambarkan momen akhir dari perjalanan kebersamaan dalam kelas . Judul ini merepresentasikan langkah terakhir yang diambil bersama, 
       di mana setiap individu menyatukan cerita dan pengalaman mereka menjadi satu rangkaian kenangan yang berarti. Makrab terakhir ini bukan sekadar acara perpisahan, tetapi juga simbol penghargaan atas kebersamaan yang telah terjalin, sekaligus kesempatan untuk mengukir memori yang tak terlupakan sebelum melangkah menuju masa depan masing-masing  
       
       ### Latar Belakang
         Kebersamaan dalam sebuah organisasi atau kelompok adalah salah satu elemen penting yang membangun rasa solidaritas dan kekeluargaan. Selama perjalanan kebersamaan, berbagai momen telah tercipta, mulai dari tantangan, keberhasilan, hingga kenangan indah yang mempererat hubungan antaranggota.

        Makrab (Malam Keakraban) telah menjadi tradisi tahunan yang tidak hanya bertujuan untuk mempererat hubungan, tetapi juga memberikan ruang untuk merefleksikan perjalanan yang telah dilalui.
          Dalam makrab terakhir ini, momen spesial ini akan menjadi kesempatan untuk mengakhiri perjalanan dengan kenangan yang manis dan meninggalkan warisan kebersamaan yang bermakna.

        Sebagai makrab terakhir, acara ini dirancang dengan harapan dapat menjadi momen penutup yang berkesan bagi seluruh anggota, menyatukan cerita, serta memberikan penghargaan atas kontribusi setiap individu.
          Dengan semangat kekeluargaan dan rasa syukur, acara ini juga menjadi ajang untuk saling mendukung dalam menapaki langkah selanjutnya di luar kebersamaan ini.

        Oleh karena itu, melalui proposal ini, kami bermaksud mengadakan makrab terakhir yang penuh makna, sebagai simbol perpisahan yang indah sekaligus pengingat bahwa ikatan yang telah terjalin tidak akan mudah terlupakan.
        
       ### Tujuan Acara

        1. Mempererat Hubungan Kekeluargaan
            Menjadi momen untuk mempererat rasa kebersamaan dan kekeluargaan antaranggota sebelum berpisah dari perjalanan bersama.
        2. Mengapresiasi Perjalanan yang Telah Dilalui
            Memberikan ruang refleksi untuk mengenang dan menghargai perjalanan, kontribusi, serta pencapaian yang telah diraih bersama.
        3. Mengukir Kenangan yang Berkesan
            Menciptakan momen-momen yang penuh makna sebagai kenangan indah yang akan dikenang di masa mendatang.
        4. Memberikan Penutup yang Bermakna
            Mengakhiri masa kebersamaan dengan cara yang positif dan berkesan sebagai simbol ikatan persaudaraan yang tidak mudah terlupakan.
        5. Menanamkan Nilai dan Harapan
            Menanamkan nilai-nilai kekeluargaan dan harapan agar ikatan emosional yang terjalin selama ini tetap terjaga, meskipun perjalanan bersama telah selesai.
         
         ### info fila:
               """,
        unsafe_allow_html=True
    )

    
    st.graphviz_chart("""
        digraph {
           "penanngung jawab
        parhan dan agung "-> "ketua pelaksana"
          "ketua pelaksana"-> "bendahara dan sekertaris","schedule"
          "schedule"->"keamanan"
          "bendahara dan sekertaris"->"logistik"
         "logistik"->"masak "
        "schedule"->"dokumentasi"
                          
            
        
            
        }
    """)