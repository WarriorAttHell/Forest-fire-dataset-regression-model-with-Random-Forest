import joblib as jb
import numpy as np
import streamlit as st
import os
from joblib import dump, load


model = jb.load('modelo_RF.pkl')

st.header('Modelo de Regressão')
st.markdown('Insira as informações para descobrir o tamanho da área em chamas')

def predict_forest(ffmc,dmc,dc,isi):
    input=np.array([[ffmc,dmc,dc,isi]]).astype(np.float64)
    prediction = model.predict(input)
    pred='{0:.{1}f}'.format(prediction [0],2)
    return float(pred)

def main():
    
    ffmc = st.slider('FFMC', 18.70, 96.20)
    st.write(ffmc)

    dmc = st.slider('DMC', 1.10, 291.30)
    st.write(dmc)

    dc = st.slider('DC', 7.90, 860.60)
    st.write(dc)

    isi = st.slider('ISI', 0.0, 56.10)
    st.write(isi)

    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Floresta segura</h2>
       </div>
    """

    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Floresta em perigo</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(ffmc,dmc,dc,isi)
        st.success('Probabilidade do tamanho da área em incendio é: {} M²'.format(output))

        if output > 0.40:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()