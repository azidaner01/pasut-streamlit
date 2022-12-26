from multiprocessing.spawn import import_main_path
import streamlit as st
import pickle
import numpy as np

# Import model
model_pasut = pickle.load(open('modelpasut.pkl', 'rb'))

def main():
    # Membuat form
    st.title('Prediksi Gelombang Pasang Surut')
    Bulan = st.selectbox('Bulan', [1,2,3,4,5,6,7,8,9,10,11,12])
    Tahun = st.text_input('Tahun')
    # Prediksi model
    if st.button('Prediksi'):
        prediksi = model_pasut.predict([[Bulan, Tahun]])
        output = round(prediksi[0],2)
        st.success('Ketinggian gelombang nya adalah {}'.format(output))

if __name__=='__main__':
    main()