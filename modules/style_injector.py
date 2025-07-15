import streamlit as st

def inject_local_css(file_path=".streamlit/style.css"):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Fichier CSS non trouvé : {file_path}")
