import streamlit as st


st.header("📝 Datos de Trazabilidad")


import pandas as pd 
# Ruta local del archivo
ruta_csv = "df_etl_cito.csv"  # Cambia esto a la ruta de tu archivo CSV

# Leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)
    
    # Crear un expander para mostrar los primeros valores
    with st.expander("Ver los primeros valores del CSV"):
        st.write("Primeros 5 valores:")
        st.dataframe(df.head())
    
    

except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {ruta_csv}")



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Título de la aplicación
st.title("Comparador de Columnas en Gráficos de Barras")

# Ruta local del archivo


# Leer el archivo CSV
try:
    df = pd.read_csv(ruta_csv)

    # Expander para mostrar los datos del archivo CSV
    with st.expander("Ver los datos del archivo CSV"):
        st.dataframe(df)
    
    # Permitir al usuario seleccionar dos columnas
    columnas = df.columns.tolist()
    col1 = st.selectbox("Selecciona la columna para el eje X:", columnas)
    col2 = st.selectbox("Selecciona la columna para el color del gráfico (hue):", columnas)
    
    # Verificar que las columnas seleccionadas sean válidas
    if col1 and col2:
        with st.expander("Ver gráfico generado"):
            # Crear un gráfico con Seaborn
            st.write(f"Gráfico de barras: {col1} vs {col2}")
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=col1, hue=col2)
            plt.xticks(rotation= 90)
            plt.title(f"Distribución de {col1} vs {col2}")
            plt.tight_layout()

            # Mostrar el gráfico en Streamlit
            st.pyplot(plt)
    else:
        st.warning("Por favor, selecciona dos columnas para generar el gráfico.")
except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {ruta_csv}")