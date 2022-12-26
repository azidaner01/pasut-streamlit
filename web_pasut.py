import streamlit as st
import pickle
import numpy as np

# Import model
model_pasut = pickle.load(open('model_pasut.pkl', 'rb'))

# Membuat form
st.title('Prediksi Gelombang Pasang Surut')
Koefisien = st.text_input('Koefisien')
Tahun = st.text_input('Tahun')
 # Prediksi model
if st.button('Prediksi'):
    prediksi = model_pasut.predict([[Koefisien, Tahun]])
    output = round(prediksi[0],2)
    st.success('Ketinggian gelombang nya adalah {}'.format(output))