import streamlit as st
import openai
import os

# 🔐 Récupération sécurisée de la clé API via les secrets Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🧠 Fonction de génération de fiche médicale
def generate_medical_sheet(pathologie):
    prompt = f"""
Génère une fiche médicale claire et intuitive sur : {pathologie.upper()}.

Structure de la fiche :
📘 Définition
🧬 Étiologies (logiques, pas robotisées)
🩺 Clinique typique
🧪 Biologie
🖼️ Imagerie (avec scores spécifiques s’il y en a)
📚 Étude de cas (facultatif mais pertinent)

Sois pédagogique, lisible, avec des phrases naturelles pour un étudiant en médecine.
"""

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"❌ Une erreur est survenue : {str(e)}"

# 🎛️ Interface Streamlit
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

# 🧾 Entrée utilisateur
module = st.sidebar.selectbox("🔍 Choisis un module", ["🧠 Générer une fiche médicale"])
if module == "🧠 Générer une fiche médicale":
    pathologie = st.text_input("Entrez le nom de la pathologie :")
    if st.button("📄 Générer la fiche") and pathologie:
        fiche = generate_medical_sheet(pathologie)
        st.markdown(f"### 🧾 Résultat pour **{pathologie}** :")
        st.write(fiche)
