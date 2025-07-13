import streamlit as st

# --------------------- CONFIG GÉNÉRALE ---------------------
st.set_page_config(page_title="DiagnosIA", layout="centered")

st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")

# --------------------- MENU PRINCIPAL ---------------------
menu = st.sidebar.selectbox("🔍 Choisis un module", ["🏫 Cours", "🧪 Cas Cliniques", "ℹ️ À propos"])

# --------------------- MODULE COURS ---------------------
if menu == "🏫 Cours":
    st.header("📘 Module Cours")
    chapitre = st.selectbox("Choisis un chapitre :", [
        "Néoplasies intra-épithéliales cervicales (CIN)",
        "Sémiologie en urologie",
        "Cancers du sein",
        "Troubles hydro-électrolytiques"
    ])

    st.subheader(f"Chapitre sélectionné : {chapitre}")
    st.markdown("🔍 *Contenu pédagogique simplifié*")

    if chapitre == "Néoplasies intra-épithéliales cervicales (CIN)":
        st.markdown("""
        ### 🔬 Définition :
        - **CIN** = anomalies des cellules épithéliales du col utérin (pré-cancer).
        - Grades : **CIN I (léger)**, **CIN II (modéré)**, **CIN III (sévère)**.

        ### 📈 Évolution :
        - Spontanément régressif en 60% des cas pour CIN I.
        - Risque de progression vers carcinome si non traité.

        ### 🧪 Dépistage :
        - Frottis cervico-utérin.
        - Typage HPV si anomalies.

        ### 💡 À retenir pour les QCM :
        - CIN ≠ cancer invasif.
        - CIN III = risque ++ de progression.
        - Traitement = exérèse locale si persistance.
        """)
    
    else:
        st.info("Le contenu de ce chapitre n’a pas encore été ajouté.")

# --------------------- MODULE CAS CLINIQUES ---------------------
elif menu == "🧪 Cas Cliniques":
    st.header("🧪 Module Cas Cliniques")

    st.markdown("#### 🔍 Cas clinique n°1 : Femme de 35 ans, métrorragies post-coïtales")
    st.write("Question 1 : Que fais-tu en premier ?")

    choix1 = st.radio("👉 Choix 1 :", ["Observation", "Frottis cervico-utérin", "Échographie pelvienne", "Colposcopie"])
    if choix1 == "Frottis cervico-utérin":
        st.success("✅ Bonne réponse. Tu passes à l'étape suivante.")
        st.write("Question 2 : Le frottis revient ASC-H. Tu fais quoi ?")

        choix2 = st.radio("👉 Choix 2 :", ["On refait un frottis", "Colposcopie", "Biopsie endométriale", "IRM pelvienne"])
        if choix2 == "Colposcopie":
            st.success("✅ Bien joué. Tu progresses dans la démarche logique.")
        else:
            st.error("❌ Ce n’est pas l’étape recommandée en 1ère intention.")
    else:
        st.error("❌ Ce n’est pas l’examen recommandé en première intention dans ce contexte.")

# --------------------- MODULE À PROPOS ---------------------
elif menu == "ℹ️ À propos":
    st.header("ℹ️ À propos de DiagnosIA")
    st.markdown("""
    DiagnosIA est un assistant IA médical conçu par un étudiant pour des étudiants.
    
    Objectifs :
    - T’aider à **comprendre** les cours et pas juste les mémoriser.
    - T’entraîner sur des **cas cliniques interactifs** comme en ECOS.
    - Te faire gagner du temps avec une IA **adaptée à la médecine**.

    🧠 Développé en Streamlit + Python  
    📍 Projet en cours — version bêta 0.1
    """)

# --------------------- FOOTER ---------------------
st.markdown("---")
st.caption("© 2025 DiagnosIA – Prototype by Anapath ✨")
