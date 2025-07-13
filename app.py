-import streamlit as st
from openai import OpenAI

# ✅ Clé API OpenAI (nouvelle version avec organisation)
client = OpenAI(
    api_key="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",
    organization="org-opwXQ0sAJdLmwoS4wkbgjP3U"
)

# ---------------- CONFIG ----------------
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")
menu = st.sidebar.selectbox("🔍 Choisis un module", ["📘 Cours", "🧠 Cas Cliniques", "ℹ️ À propos"])

# ---------------- MODULE COURS ----------------
if menu == "📘 Cours":
    st.header("📘 Module Cours")
    tab1, tab2 = st.tabs(["📚 Choisir un cours", "🧠 Générer une fiche IA"])

    with tab1:
        chapitre = st.selectbox("Choisis un chapitre :", [
            "Néoplasies intra-épithéliales cervicales (CIN)",
            "Sémiologie en urologie",
            "Cancers du sein",
            "Troubles hydro-électrolytiques"
        ])
        st.subheader(f"📑 Contenu du cours : {chapitre}")
        if chapitre == "Néoplasies intra-épithéliales cervicales (CIN)":
            st.markdown("### 🧬 Définition :")
            st.markdown("- CIN = anomalies des cellules épithéliales du col utérin (pré-cancer).")
            st.markdown("- Grades : **CIN I** (léger), **CIN II** (modéré), **CIN III** (sévère).")
            st.markdown("### 📈 Évolution :")
            st.markdown("- Les formes légères peuvent régresser spontanément.")
            st.markdown("- Risque de progression vers carcinome invasif si non traité.")

    with tab2:
        st.subheader("💡 Génère une fiche médicale intelligente à partir d'une pathologie")
        patho = st.text_input("Entrez le nom de la pathologie :")
        if patho:
            try:
                with st.spinner("Génération en cours..."):
                    prompt = f"""
Tu es un assistant médical expert. Rédige une fiche synthétique et pédagogique sur la pathologie suivante : {patho}. Organise la fiche avec ces sections claires :

1. 🧬 **Définition** (courte, simple, efficace)
2. 🧠 **Étiologies** (sous forme de tirets logiques et instinctifs)
3. 🩺 **Clinique typique** (signes majeurs, chronologie s’il y a)
4. 🧪 **Biologie** (examens clés, résultats typiques)
5. 🖼️ **Imagerie** (modalités, signes, scores si applicables)
6. 📌 **Étude de cas** (facultatif mais impactant)

Sois fluide, instinctif, sans jargon inutile. Objectif : **apprentissage rapide et mémorisation efficace**.
"""
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"❌ Une erreur est survenue : {e}")
