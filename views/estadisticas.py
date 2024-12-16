import streamlit as st

st.header("👨🏻‍🔬 Analisis de la Trazabilidad 2024")

mensaje = """
Los datos analizados fueron tomados de la planilla de trazabilidad 2024, ya que esta resulta ser la más completa para el análisis. Esta planilla no solo incluye información básica como el tipo de estudio, médico, y obra social, sino que también contiene columnas de gran interés, como el Importe, las fechas de extracción, envío, y entrega de resultados, así como también datos clave que indican si el estudio es confirmatorio o no. Esta riqueza de datos permite realizar un análisis detallado y profundo, orientado a generar conclusiones relevantes y fundamentadas.
"""

st.markdown(mensaje)


st.header("📝 Campos mas importantes en el analisis")



with st.expander("Frecuencia de las Obras Sociales"):
    
    st.image("obrasocial.jpeg", caption="La mayor parte de los pacientes del IGeHM no cuentan con obra social")


with st.expander("Origen de la muestra"):
    
    st.image("origenmuestra.jpeg", caption="La mayor parte proviene del IGeHM")




with st.expander("Laboratorio de Destino"):
    
    st.image("labdestino.jpeg", caption="La mayor parte se envia a Manlab")

with st.expander("Tipo de Estudio"):
    
    st.image("tipoestudio.jpeg", caption="La mayor parte son paneles")


with st.expander("Enfermedad"):
    
    st.image("enfermedad.jpeg", caption="La mayor parte son canceres")

with st.expander("Confirmado"):
    
    st.image("confirmado.jpeg", caption="La mayor parte son NO confirmados")


with st.expander("Importe vs Lab vs Confirmado"):
    
    st.image("importe-lab-conf.jpeg", caption="La mayor parte son NO confirmados de Manlab")


with st.expander("Dias de Procesamiento"):
    
    st.image("diasprocesamiento.jpeg", caption="Generalemente tarda 100 dias")


with st.expander("Medicos vs Confirmacion"):
    
    st.image("confirmado-medico.jpeg", caption="La mayoria de los estudios de Espindola son no confirmatorios")


with st.expander("Importe vs Confirmacion"):
    
    st.image("Importe-conf.jpeg", caption="40 millones fue el monto que se perdio en estudios")


with st.expander("Fecha de Cotizacion vs Importe"):
    
    st.image("fechacotizacion-importe.jpeg", caption="Hay mucho variacion con varios picos")