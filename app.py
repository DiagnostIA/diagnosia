import streamlit as st
import openai

# ⛑️ Clé API OpenAI (attention à ne jamais l’exposer en public !)
openai.api_key = "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"

# 🧠 Fonction de génération de fiche médicale
def generate_medical_sheet(pathologie):
    prompt = f"""
    Génère une fiche médicale claire et intuitive sur : {pathologie.upper()}.

    Structure de la fiche :
    📘 Définition
    🧠 Étiologies (logiques, pas robotisées)
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
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"❌ Une erreur est survenue : {str(e)}"

# 🖥️ Interface Streamlit
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

menu = st.sidebar.selectbox("🔍 Choisis un module", [
    "📘 Module Cours",
    "🧠 Générer une fiche IA"
])

# 📚 MODULE FICHE IA
if menu == "🧠 Générer une fiche IA":
    st.header("💡 Génère une fiche médicale intelligente à partir d'une pathologie")
    patho = st.text_input("Entrez le nom de la pathologie :")
    if st.button("📄 Générer la fiche") and patho:
        with st.spinner("⏳ Génération de la fiche..."):
            fiche = generate_medical_sheet(patho)
            st.markdown(fiche)

# (Tu pourras ajouter les autres modules ici plus tard)
