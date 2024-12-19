import streamlit as st



st.header("👨🏻‍🔬 Programas Bioinformaticos")

mensaje = """
A continuación, se presenta la lista de programas y scripts desarrollados en el área, diseñados para resolver problemáticas biológicas o de gestión
"""

st.markdown(mensaje)


st.header("📝 Programas")

with st.expander("Extracthor"):
    
    st.image("extractor.jpeg", caption="Para extraer datos de informes de NGS")


