import streamlit as st
import math

# Konfigurasi Halaman Website
st.set_page_config(page_title="Kalkulator Saintifik", page_icon="📐", layout="centered")

# Header Website
st.title("📐 Kalkulator Saintifik Interaktif")
st.write("Website kalkulator sederhana yang dibuat menggunakan Python dan Streamlit.")
st.divider()

# Membuat dua tab untuk memisahkan kalkulator dasar dan saintifik
tab1, tab2 = st.tabs(["🔢 Kalkulator Dasar", "🔬 Kalkulator Saintifik"])

# --- TAB 1: KALKULATOR DASAR ---
with tab1:
    st.subheader("Operasi Aritmatika Dasar")
    
    # Membuat 3 kolom agar input sejajar
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        angka1 = st.number_input("Angka Pertama", value=0.0, step=1.0, key="d1")
    with col2:
        operasi = st.selectbox("Operasi", ["+", "-", "×", "÷", "^ (Pangkat)"], key="d2")
    with col3:
        angka2 = st.number_input("Angka Kedua", value=0.0, step=1.0, key="d3")

    if st.button("Hitung Dasar", type="primary", key="btn1"):
        hasil = 0
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "×":
            hasil = angka1 * angka2
        elif operasi == "÷":
            hasil = "Error: Pembagian dengan nol tidak diizinkan!" if angka2 == 0 else angka1 / angka2
        elif operasi == "^ (Pangkat)":
            hasil = math.pow(angka1, angka2)

        if isinstance(hasil, str):
            st.error(hasil)
        else:
            st.success(f"Hasil: {hasil}")

# --- TAB 2: KALKULATOR SAINTIFIK ---
with tab2:
    st.subheader("Operasi Matematika Lanjutan")
    
    col_op, col_num = st.columns([1, 2])
    with col_op:
        operasi_sci = st.selectbox("Pilih Fungsi", [
            "sin", "cos", "tan", 
            "Akar Kuadrat (√)", "Logaritma (log10)", 
            "Log Natural (ln)", "Faktorial (!)", "Derajat ke Radian"
        ])
    with col_num:
        angka_sci = st.number_input("Masukkan Angka", value=0.0, step=1.0, key="s1")

    # Catatan untuk fungsi trigonometri
    if operasi_sci in ["sin", "cos", "tan"]:
        st.info("💡 Angka yang dimasukkan akan dianggap sebagai nilai **Derajat**.")

    if st.button("Hitung Saintifik", type="primary", key="btn2"):
        hasil_sci = 0
        try:
            if operasi_sci == "sin":
                hasil_sci = math.sin(math.radians(angka_sci))
            elif operasi_sci == "cos":
                hasil_sci = math.cos(math.radians(angka_sci))
            elif operasi_sci == "tan":
                hasil_sci = math.tan(math.radians(angka_sci))
            elif operasi_sci == "Akar Kuadrat (√)":
                hasil_sci = math.sqrt(angka_sci)
            elif operasi_sci == "Logaritma (log10)":
                hasil_sci = math.log10(angka_sci)
            elif operasi_sci == "Log Natural (ln)":
                hasil_sci = math.log(angka_sci)
            elif operasi_sci == "Faktorial (!)":
                hasil_sci = math.factorial(int(angka_sci))
            elif operasi_sci == "Derajat ke Radian":
                hasil_sci = math.radians(angka_sci)
            
            # Membulatkan hasil trigonometri yang mendekati nol akibat float
            if operasi_sci in ["sin", "cos", "tan"] and abs(hasil_sci) < 1e-10:
                hasil_sci = 0.0

            st.success(f"Hasil: {hasil_sci}")
        except Exception as e:
            # Menangkap error jika user memasukkan input tidak logis (misal akar negatif)
            st.error("⚠️ Terjadi kesalahan! Pastikan angka valid untuk operasi matematika tersebut (Contoh: faktorial harus bilangan bulat, akar tidak boleh negatif).")
