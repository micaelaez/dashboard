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

st.sidebar.header("opciones de filtro de tabla")
DEPARTAMENTO_SOLICITANTE=st.sidebar.multiselect(
    "seleccione el departamento:",
    options = df_libros['DEPARTAMENTO_SOLICITANTE'].unique(),
    default = df_libros['DEPARTAMENTO_SOLICITANTE'].unique()
)

NOMBRES_SOLICITANTE=st.sidebar.multiselect(
    "seleccione el solicitante:",
    options = df_libros['NOMBRES_SOLICITANTE'].unique(),
    default = df_libros['NOMBRES_SOLICITANTE'].unique()
)


TITULO =st.sidebar.multiselect(
    "seleccione el titulo:",
    options = df_libros['TITULO'].unique(),
    default = df_libros['TITULO'].unique()
)


df_opcion = df_libros.query("DEPARTAMENTO_SOLICITANTE == @DEPARTAMENTO_SOLICITANTE &  DISTRITO_SOLICITANTE == @DISTRITO_SOLICITANTE   &  NOMBRES_SOLICITANTE == @NOMBRES_SOLICITANTE  &  TITULO == @TITULO")

libro_max_copias = df_opcion.iloc[df_opcion['TIRAJE'].idxmax()]
titulo_libro_max_copias = libro_max_copias['TITULO']
distritos = df_opcion.iloc[df_opcion['DISTRITO_SOLICITANTE'].idxmax(), df_opcion.columns.get_loc('DISTRITO_SOLICITANTE')]

left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Distritos con mas pedidos:")
    st.subheader(f"{distritos}")

with right_column:
    st.subheader("libro con mas copias producidas:")
    st.subheader(f" libro {titulo_libro_max_copias}, Copias producidas {libro_max_copias['TIRAJE']}")

st.markdown("---------------------")
st.dataframe(df_opcion)


#para realizar la grafica de tablas de barra


libros = (df_opcion.groupby(by=['DISTRITO_SOLICITANTE'])).sum()[['TIRAJE']].sort_values(by="TIRAJE")

fig_libro=px.bar(
    libros,
    x='TIRAJE',
    y=libros.index,
    orientation='h',
    title="<b> cantidad de libros aprovados <b> ",
    color_discrete_sequence=["#0000FF"] * len(libros),
     template='plotly_white',
)

libros2 = (df_opcion.groupby(by=['NOMBRES_SOLICITANTE'])).sum()[['TITULO']].sort_values(by="TITULO")

fig_libro_2 = px.bar(
    libros2,
    x='TITULO',
    y=libros2.index,
    title="<b> Titulos aprobados <b>",
    color_discrete_sequence=["#0000FF"] * len(libros),
    orientation='v',
     template='plotly_white',
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_libro, use_container_width= True)
right_column.plotly_chart(fig_libro_2, use_container_width= True)










