import streamlit as st



st.header("👨🏻‍🔬 Analisis Dinamico")

mensaje = """
Aqui se puede elegir y configurar de forma dinamica que otros datos son de interes
"""

st.markdown(mensaje)


st.header("📝 Campos mas importantes en el analisis")



with st.expander("Distribucion de las Enfermedades"):
    
    st.image("distribucion.jpeg", caption="La mayor parte de los pacientes se encuentran en Posadas")




# Cargar el contenido del archivo HTML
html_file_path = "pueblos_misiones_full.html"

try:
    with open(html_file_path, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    # Mostrar el HTML en Streamlit
    st.components.v1.html(html_content, height=600, scrolling=True)
except FileNotFoundError:
    st.error(f"El archivo '{html_file_path}' no se encontró. Asegúrate de que el archivo exista en el directorio.")
