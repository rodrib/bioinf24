import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/nosotros.py",
    title="Sobre Nosotros",
    icon=":material/account_circle:",
    default=True,
)


project_2_page = st.Page(
    "views/estadisticas.py",
    title="Estadisticas",
    icon=":material/smart_toy:",
)

project_3_page = st.Page(
    "views/programas.py",
    title="Programas",
    icon=":material/bar_chart:",
)

project_4_page = st.Page(
    "views/estadisticasdin.py",
    title="Estadistica Dinamica",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projectos": [ project_2_page, project_4_page,project_3_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.markdown("Made with ❤️ by [Rfeb](https://www.linkedin.com/in/rodrigo-bogado-a64b4925b/)")


# --- RUN NAVIGATION ---
pg.run()