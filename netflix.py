import pandas as pd
import numpy as np
import streamlit as st
import codecs
import re

st.title('Netflix App')

DATA_URL = 'https://raw.githubusercontent.com/asunawesker/netflix/main/movies.csv'

@st.cache
def cargar_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

@st.cache
def cargar_data_nombre(name):
    datafiltered = cargar_data(500)
    filtrar_data_nombre = datafiltered[datafiltered['name'].str.contains(name, flags=re.IGNORECASE)]  
    return filtrar_data_nombre

@st.cache
def cargar_data_director(director):
    data = cargar_data(500)
    filtrar_data_director = data[data['director'] == director]
    return filtrar_data_director

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos los filmes")
titulo = sidebar.text_input('Titulo del filme:')
btnFiltrarDirectorFilm = sidebar.button('Buscar filmes')
data = cargar_data(500)
selected = sidebar.selectbox("Selecciona director", data['director'].unique())
btnFiltrarDirector = sidebar.button('Filtrar por Director')

if agree:
    estado = st.text('Cargando...')
    data = cargar_data(500)
    estado.text("¡Cargado! (usando st.cache)")
    st.dataframe(data)

if btnFiltrarDirectorFilm:
    st.write ("Titulo buscado: "+ titulo)
    filtrar = cargar_data_nombre(titulo)
    filas = filtrar.shape[0]
    st.write(f'Total de peliculas: {filas}')
    st.dataframe(filtrar)

if btnFiltrarDirector: 
    st.write("Peliculas dirigidas por "+selected)
    filtrar = cargar_data_director(selected)
    filas = filtrar.shape[0]
    st.write(f'Total de peliculas: {filas}')
    st.dataframe(filtrar)