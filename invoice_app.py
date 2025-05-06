import streamlit as st
from fpdf import FPDF
import datetime

st.title("🧾 Invoice Otomatis untuk Freelancer")

# Input data
client = st.text_input("Nama Klien")
project = st.text_input("Nama Proyek")
date = st.date_input("Tanggal Invoice", datetime.date.today())
amount = st.number_input("Jumlah Pembayaran (Rp)", step=10000)
notes = st.text_area("Catatan Tambahan")

# Tombol Generate
if st.button("🔻 Download Invoice PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Invoice Freelancer", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Tanggal: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Untuk: {client}", ln=True)
    pdf.cell(200, 10, txt=f"Proyek: {project}", ln=True)
    pdf.cell(200, 10, txt=f"Jumlah: Rp {amount:,.0f}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(200, 10, txt=f"Catatan:\n{notes}")

    filename = f"Invoice_{client.replace(' ', '_')}.pdf"
    pdf.output(filename)

    with open(filename, "rb") as f:
        st.download_button(
            label="📥 Klik di sini untuk mengunduh PDF",
            data=f,
            file_name=filename,
            mime="application/pdf"
        )
