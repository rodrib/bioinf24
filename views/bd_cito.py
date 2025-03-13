import streamlit as st
import duckdb
import pandas as pd

st.header("📝 Base de datos de Citogenetica")

ruta_csv = "df_etl_cito.csv"

try:
    df = pd.read_csv(ruta_csv)
    con = duckdb.connect(database=':memory:')
    con.register('tabla_citogenetica', df)

    # -----------------------------------------------
    # 1. Expander con primeros valores
    # -----------------------------------------------
    with st.expander("🔍 Ver primeros valores del CSV"):
        st.dataframe(df.head())
    
    # -----------------------------------------------
    # 2. Estadísticas predefinidas
    # -----------------------------------------------
    st.subheader("📊 Estadísticas por Procedencia")

    
    query_procedencia = """
        SELECT 
            Procedencia,
            COUNT(*) AS total_pacientes,
            SUM(CASE WHEN Patologia LIKE '%TRISOMIA 21 (SME DE DOWN)%' THEN 1 ELSE 0 END) AS Patologia
        FROM tabla_citogenetica
        GROUP BY Procedencia
    """
    result_procedencia = con.execute(query_procedencia).fetchdf()
    st.dataframe(result_procedencia)
    
    # -----------------------------------------------
    # 3. Consulta SQL Interactiva (¡Corregido aquí!)
    # -----------------------------------------------
    st.subheader("🔎 Consulta SQL Personalizada")
    
    # Área de texto PARA ESCRIBIR LA CONSULTA (debe estar en este nivel de indentación)
    user_query = st.text_area(
        "Escribe tu consulta SQL aquí (usa 'tabla_citogenetica' como nombre de tabla):",
        height=150,
        placeholder="Ejemplo: SELECT * FROM tabla_citogenetica WHERE Procedencia = 'Hospital General'"
    )
    
    # Botón para ejecutar (también en mismo nivel)
    if st.button("🚀 Ejecutar Consulta", type="primary"):
        if user_query.strip():
            try:
                result = con.execute(user_query).fetchdf()
                st.success("✅ ¡Consulta exitosa!")
                st.dataframe(result)
                
                # Botón de descarga
                st.download_button(
                    label="💾 Descargar Resultados",
                    data=result.to_csv(index=False).encode('utf-8'),
                    file_name='resultado.csv',
                    mime='text/csv'
                )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ ¡Escribe una consulta antes de ejecutar!")

    # Cerrar conexión
    con.close()

except FileNotFoundError:
    st.error(f"Archivo no encontrado: {ruta_csv}")