import streamlit as st
import openai

# — CONFIGURATION GÉNÉRALE —
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

# — CLÉ API OPENAI (VALIDE) —
openai.api_key = "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"
openai.organization = "org-opwXQ0sAJdLmwoS4wkbgjP3U"

# — MENU LATÉRAL —
menu = st.sidebar.selectbox("🔎 Choisis un module", [
    "📚 Module Cours",
    "🧾 Générer une fiche IA",
    "🧠 QCM intelligents",
    "💡 Méthodo personnalisée",
    "❌ Analyse erreurs",
    "🖨️ Générer fiche PDF",
    "🎯 Mode ECN / Concours",
    "👨‍⚕️ Mode Jeune Médecin"
])

# — MODULE : Générateur de fiche IA —
if menu == "🧾 Générer une fiche IA":
    st.subheader("💡 Génère une fiche médicale intelligente à partir d'une pathologie")
    patho = st.text_input("Entrez le nom de la pathologie :")
    
    if st.button("📄 Générer la fiche") and patho:
        with st.spinner("Génération en cours..."):
            try:
                prompt = f"""
Tu es une IA médicale experte. Génère une fiche pédagogique sur la pathologie suivante : {patho}.
Structure-la ainsi :
🧬 Définition
🧠 Étiologies (logiques et mémorisables)
🩺 Clinique typique
🧪 Biologie
🖼️ Imagerie (signes ou scores utiles)
📚 Facultatif : un mini cas clinique d'application
Fais clair, fluide, synthétique mais impactant.
"""
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Tu es un assistant médical expert."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                fiche = response.choices[0].message.content
                st.success("✅ Fiche générée !")
                st.markdown(fiche)
            except Exception as e:
                st.error(f"❌ Une erreur est survenue : {e}")

# — PLACEHOLDERS pour les autres modules —
elif menu == "📚 Module Cours":
    st.subheader("📘 Module Cours")
    st.info("💡 Ce module contiendra les cours organisés par spécialité.")

elif menu == "🧠 QCM intelligents":
    st.subheader("🧠 QCM personnalisés")
    st.info("🛠️ Fonctionnalité en cours de développement.")

elif menu == "💡 Méthodo personnalisée":
    st.subheader("💡 Méthodologie intelligente")
    st.info("🧠 DiagnosIA adaptera les conseils selon ton profil cognitif.")

elif menu == "❌ Analyse erreurs":
    st.subheader("❌ Analyse de tes erreurs")
    st.info("🔍 DiagnosIA identifiera tes erreurs récurrentes pour t'aider à progresser.")

elif menu == "🖨️ Générer fiche PDF":
    st.subheader("🖨️ Générer des fiches PDF")
    st.info("📄 Tu pourras bientôt imprimer tes synthèses en un clic.")

elif menu == "🎯 Mode ECN / Concours":
    st.subheader("🎯 Mode simulation ECN")
    st.info("⏱️ Simulations d’épreuves avec chrono, auto-correction et feedback IA.")

elif menu == "👨‍⚕️ Mode Jeune Médecin":
    st.subheader("👨‍⚕️ Mode praticien")
    st.info("🧰 Outils pratiques post-diplôme : checklists, simulateurs, aides terrain.")
