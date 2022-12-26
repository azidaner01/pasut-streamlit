import streamlit as st
import pickle
import numpy as np

# Import model
model_pasut = pickle.load(open('modelpasut.pkl', 'rb'))
# Membuat form
st.title('Prediksi Gelombang Pasang Surut')
Koef = st.text_input('Koefisien')
Tahun = st.text_input('Tahun')
# Submit
if st.button('Prediksi'):
    query = np.array([Koef, Tahun])
    query = query.reshape(1,2)
    st.title("Hasil prediksi :" + str(int(np.exp(model_pasut.predict(query)[0]))))