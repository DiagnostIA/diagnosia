import streamlit as st
import openai
import os
from PIL import Image
from modules.qcm_generator import run_qcm_generator  # Module QCM

# Clé API OpenAI sécurisée
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === STYLE CSS PERSONNALISÉ ===
with open("diagnosia_custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === LOGO (optionnel, tu peux le supprimer si pas encore dispo) ===
# logo = Image.open("logo_diagnosia.png")
# st.image(logo, width=100)

# === TITRE ===
st.markdown("<h1>🧠 DiagnosIA – Assistant IA pour étudiants en médecine</h1>", unsafe_allow_html=True)
st.caption("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

# === SÉLECTEUR DE MODULE ===
module = st.sidebar.selectbox(
    "🔍 Choisis un module",
    ["🧠 Générer une fiche médicale", "📝 Générer des QCM personnalisés"]
)

# === GÉNÉRATION DE FICHE MÉDICALE ===
def generate_medical_sheet(pathologie):
    prompt = f"""Génère une fiche médicale claire et intuitive sur : {pathologie.upper()}

Structure de la fiche :
- Définition (cliniques, pas robotiques)
- Étiologies
- Clinique typique
- Biologie
- Imagerie (avec scores spécifiques s’il y en a)
- Étude de cas (facultatif mais pertinent)

Sois pédagogique, fluide, avec des phrases naturelles pour un étudiant en médecine."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un professeur de médecine très pédagogue."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Une erreur est survenue : {e}"

# === MODULE : Fiche Médicale ===
if module == "🧠 Générer une fiche médicale":
    patho_input = st.text_input("Entrez le nom de la pathologie :", placeholder="ex : embolie pulmonaire")
    if st.button("📄 Générer la fiche"):
        if patho_input.strip() == "":
            st.warning("⚠️ Veuillez entrer une pathologie.")
        else:
            st.markdown(f"## 📋 Résultat pour **{patho_input.strip()}** :")
            result = generate_medical_sheet(patho_input.strip())
            st.write(result)

# === MODULE : QCM Personnalisés ===
elif module == "📝 Générer des QCM personnalisés":
    run_qcm_generator()
