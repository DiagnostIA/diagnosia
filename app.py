import streamlit as st
import openai
import os

# Clé API OpenAI sécurisée via secrets Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_medical_sheet(pathologie):
    prompt = f"""Fais une fiche médicale claire et intuitive sur : {pathologie.upper()}

Structure de la fiche :
- Définition (cliniques, pas robotisée)
- Étiologies
- Clinique typique
- Biologie
- Imagerie (avec scores spécifiques s’il y en a)
- Étude de cas (facultatif mais pertinent)

Sois pédagogique, fluide, avec des phrases naturelles pour un étudiant en médecine."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un professeur de médecine très pédagogue."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"❌ Une erreur est survenue : {e}"

# Interface Streamlit
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("🧠 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

# Sélection du module
module = st.sidebar.selectbox("🔍 Choisis un module", ["🧠 Générer une fiche médicale!"])

if module == "🧠 Générer une fiche médicale!":
    patho_input = st.text_input("Entrez le nom de la pathologie :", "")
    if st.button("📄 Générer la fiche"):
        if patho_input.strip() == "":
            st.warning("Veuillez entrer une pathologie.")
        else:
            with st.spinner("🧪 Résultat pour " + patho_input):
                result = generate_medical_sheet(patho_input.strip())
                st.write(result)
