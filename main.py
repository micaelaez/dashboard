import streamlit as st
import pandas as pd

st.set_page_config(page_title='Informacion de Libros',
                   page_icon='books',
                   layout="wide")

st.title(':books: Informacion de Libros')
st.subheader('¿Qué libros aprobados se encuentran en librerías?')
archivo_excel = 'Editoriales_aprobados.xlsx'
hoja_excel = 'BASE DE DATOS'

df_libros = pd.read_excel(archivo_excel, sheet_name=hoja_excel, usecols=list(range(4, 14)))

st.table(df_libros)

st.sidebar.header("opciones de filtro de tabla")
DEPARTAMENTO_SOLICITANTE=st.sidebar.multiselect(
    "seleccione el departamento:",
    options = df_libros['DEPARTAMENTO_SOLICITANTE'].unique(),
    default = df_libros['DEPARTAMENTO_SOLICITANTE'].unique()
)

st.sidebar.header("opciones de filtro de tabla")
NOMBRES_SOLICITANTE=st.sidebar.multiselect(
    "seleccione el solicitante:",
    options = df_libros['NOMBRES_SOLICITANTE'].unique(),
    default = df_libros['NOMBRES_SOLICITANTE'].unique()
)

st.sidebar.header("opciones de filtro de tabla")
TITULO =st.sidebar.multiselect(
    "seleccione el titulo:",
    options = df_libros['TITULO'].unique(),
    default = df_libros['TITULO'].unique()
)


df_opcion = df_libros.query("DEPARTAMENTO_SOLICITANTE == @DEPARTAMENTO  &  NOMBRES_SOLICITANTE== @nombre_solicitante &  TITULO==@titulo ")










