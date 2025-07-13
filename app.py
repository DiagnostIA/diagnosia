import streamlit as st
from openai import OpenAI
import os

# Remplace ici par ta vraie clé API OpenAI
client = OpenAI(
    api_key="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",  # <--- Mets ta vraie clé ici
    organization="org-opwXQ0sAJdLmwoS4wkbgjP3U"
)

def generate_medical_sheet(pathologie):
    prompt = f"""
    Génère une fiche médicale claire et intuitive sur : {pathologie.upper()}.

    Structure de la fiche :
    🧬 Définition
    🧠 Étiologies (logiques, pas robotisées)
    🩺 Clinique typique
    🧪 Biologie
    🖼️ Imagerie (avec scores spécifiques s’il y en a)
    📚 Étude de cas (facultatif mais utile si pertinent)

    Sois pédagogique, lisible, avec des phrases naturelles pour un étudiant en médecine.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# Interface Streamlit
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")

menu = st.sidebar.selectbox("🔎 Choisis un module", ["📘 Cours", "🧠 Générer une fiche IA"])

if menu == "🧠 Générer une fiche IA":
    st.header("💡 Génère une fiche médicale intelligente à partir d'une pathologie")
    patho = st.text_input("Entrez le nom de la pathologie :")

    if patho:
        try:
            fiche = generate_medical_sheet(patho)
            st.markdown(fiche)
        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")
