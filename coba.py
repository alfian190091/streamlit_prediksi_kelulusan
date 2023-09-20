import pickle
import streamlit as st

st.title('Sistem Prediksi Kelulusan Tepat Waktu dan Tidak Tepat Waktu semangat')

nim = st.number_input("Masukkan NIM", 0)
ipk1 = st.number_input("Masukkan IPK Semester 1", 0)
ipk2 = st.number_input("Masukkan IPK Semester 2", 0)
ipk3 = st.number_input("Masukkan IPK Semester 3", 0)
ipk4 = st.number_input("Masukkan IPK Semester 4", 0)
ipk5 = st.number_input("Masukkan IPK Semester 5", 0)
ipk6 = st.number_input("Masukkan IPK Semester 6", 0)
sks1 = st.number_input("Masukkan SKS Semester 1", 0)
sks2 = st.number_input("Masukkan SKS Semester 2", 0)
sks3 = st.number_input("Masukkan SKS Semester 3", 0)
sks4 = st.number_input("Masukkan SKS Semester 4", 0)
sks5 = st.number_input("Masukkan SKS Semester 5", 0)
sks6 = st.number_input("Masukkan SKS Semester 6", 0)
cek = st.button("Cek Hasil Prediksi")

#tombol prediksi
if st.button("Hasil Prediksi")
