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

import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("vehicles_us.csv")


st.header("Análisis de vehículos en EE.UU.")


if st.button("Mostrar histograma por año del modelo"):
    fig_hist = px.histogram(
        df,
        x='model_year',
        nbins=30,
        title='Distribución de vehículos por año del modelo'
    )
    st.write("Histograma de vehículos por año del modelo:")
    st.plotly_chart(fig_hist)


if st.button("Mostrar gráfico de dispersión precio vs odómetro"):
    fig_scatter = px.scatter(
        df,
        x='odometer',
        y='price',
        color='type',  
        title='Precio vs Kilometraje'
    )
    st.write("Gráfico de dispersión: Precio vs Kilometraje")
    st.plotly_chart(fig_scatter)



import streamlit as st
import pandas as pd
import plotly.express as px


st.header("Análisis de vehículos en USA")


df = pd.read_csv("vehicles_us.csv")

if st.button("Mostrar histograma de años de modelos"):
    fig_hist = px.histogram(
        df,
        x="model_year",
        nbins=30,
        title="Distribución de vehículos por año del modelo"
    )
    st.write("Histograma de modelos por año:")
    st.plotly_chart(fig_hist)


if st.button("Mostrar gráfico de dispersión precio vs odómetro"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        color="type",
        title="Relación entre odómetro y precio",
        hover_data=["model", "model_year"]
    )
    st.write("Gráfico de dispersión de precio vs odómetro:")
    st.plotly_chart(fig_scatter)



import streamlit as st
import pandas as pd
import plotly.express as px


st.header("Análisis de vehículos en USA")


df = pd.read_csv("vehicles_us.csv")


if st.checkbox("Mostrar histograma de años de modelos"):
    fig_hist = px.histogram(
        df,
        x="model_year",
        nbins=30,
        title="Distribución de vehículos por año del modelo"
    )
    st.write("Histograma de modelos por año:")
    st.plotly_chart(fig_hist)


if st.checkbox("Mostrar gráfico de dispersión precio vs odómetro"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        color="type",
        title="Relación entre odómetro y precio",
        hover_data=["model", "model_year"]
    )
    st.write("Gráfico de dispersión de precio vs odómetro:")
    st.plotly_chart(fig_scatter)
