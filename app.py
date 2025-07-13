import streamlit as st
from openai import OpenAI

# 🔐 Mets ici ta clé OpenAI
client = OpenAI(api_key="sk-...")  # ← à remplacer par ta clé

# ------------------- CONFIG -------------------
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("📚 DiagnosIA – Assistant IA pour étudiants en médecine")
st.markdown("Une app intelligente pour apprendre, réviser et simuler des cas cliniques.")
menu = st.sidebar.selectbox("🔍 Choisis un module", ["🏫 Cours", "🧪 Cas Cliniques", "ℹ️ À propos"])

# ------------------- COURS -------------------
if menu == "🏫 Cours":
    st.header("📘 Module Cours")

    tab1, tab2 = st.tabs(["📚 Choisir un cours", "🧠 Générer une fiche IA"])

    with tab1:
        chapitre = st.selectbox("Choisis un chapitre :", [
            "Néoplasies intra-épithéliales cervicales (CIN)",
            "Sémiologie en urologie",
            "Cancers du sein",
            "Troubles hydro-électrolytiques"
        ])
        st.subheader(f"📖 Contenu du cours : {chapitre}")

        if chapitre == "Néoplasies intra-épithéliales cervicales (CIN)":
            st.markdown("""
            ### 🧬 Définition :
            - CIN = anomalies des cellules épithéliales du col utérin (pré-cancer).
            - Grades : CIN I (léger), CIN II (modéré), CIN III (sévère).

            ### 🧠 Étiologies :
            - Infections persistantes à HPV à haut risque (surtout 16 et 18)
            - Rapports sexuels précoces ou multiples
            - Tabagisme
            - Immunodépression (ex : VIH)

            ### 🩺 Clinique :
            - Souvent asymptomatique
            - Parfois : métrorragies post-coïtales

            ### 🧪 Biologie :
            - Frottis cervico-utérin : ASC-US, ASC-H
            - Typage HPV

            ### 🖼️ Imagerie :
            - Colposcopie ciblée
            - Pas de score spécifique mais cartographie des lésions

            ### 🧪 Étude de cas :
            Femme de 32 ans, antécédents de rapports précoces, frottis ASC-H → colposcopie positive.
            """)
        else:
            st.info("📄 Ce chapitre n’est pas encore disponible.")

    with tab2:
        st.markdown("### 💡 Génère une fiche médicale intelligente à partir d'une pathologie")
        pathologie = st.text_input("Entrez le nom de la pathologie :")

        if pathologie:
            with st.spinner("📡 Génération de la fiche en cours..."):
                prompt = f"""
Tu es un expert en pédagogie médicale. Rédige une fiche claire et mémorable sur la pathologie suivante : {pathologie}.

Structure obligatoire :
1. 🧬 Définition
2. 🧠 Étiologies principales (liste logique et intuitive)
3. 🩺 Clinique typique (ce que l’étudiant doit retenir)
4. 🧪 Biologie (anomalies et examens complémentaires)
5. 🖼️ Imagerie (apparence, scores ou signes utiles)
6. 🧪 Étude de cas rapide pour illustrer la pathologie

Le ton doit être structuré, fluide, pédagogique et adapté à un étudiant en médecine.
                """

                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=1000
                    )
                    fiche = response.choices[0].message.content
                    st.markdown("---")
                    st.markdown(fiche)
                except Exception as e:
                    st.error(f"❌ Une erreur est survenue : {e}")

# ------------------- CAS CLINIQUES -------------------
elif menu == "🧪 Cas Cliniques":
    st.header("🧪 Module Cas Cliniques")

    st.markdown("#### 🔍 Cas clinique n°1 : Femme de 35 ans, métrorragies post-coïtales")
    choix1 = st.radio("👉 Que fais-tu en premier ?", [
        "Observation", "Frottis cervico-utérin", "Échographie pelvienne", "Colposcopie"
    ])

    if choix1 == "Frottis cervico-utérin":
        st.success("✅ Bonne réponse. Tu passes à l'étape suivante.")
        choix2 = st.radio("👉 Le frottis revient ASC-H. Tu fais quoi ?", [
            "On refait un frottis", "Colposcopie", "Biopsie endométriale", "IRM pelvienne"
        ])
        if choix2 == "Colposcopie":
            st.success("✅ Bien joué. Tu progresses dans la démarche logique.")
        else:
            st.error("❌ Mauvaise réponse à cette étape.")
    else:
        st.error("❌ Ce n’est pas l’examen recommandé en première intention.")

# ------------------- À PROPOS -------------------
elif menu == "ℹ️ À propos":
    st.header("ℹ️ À propos de DiagnosIA")
    st.markdown("""
    DiagnosIA est un assistant IA médical conçu pour aider les étudiants à :
    - Mieux comprendre leurs cours
    - Générer des fiches personnalisées
    - S'entraîner à raisonner en cas clinique

    🧠 Version bêta — développé avec ❤️ en Python et Streamlit
    """)

st.markdown("---")
st.caption("© 2025 DiagnosIA — Prototype développé par Anapath")
