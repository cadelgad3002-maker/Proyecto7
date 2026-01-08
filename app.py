import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Análisis de anuncios de vehículos en EE.UU.')

df = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma por año del modelo'):
    fig = px.histogram(
        df,
        x='model_year',
        nbins=30,
        title='Distribución de vehículos por año del modelo'
    )
    st.plotly_chart(fig)