import streamlit as st
import openai
import os

# Titre de la page
st.set_page_config(
    page_title="🧠 DiagnosIA - Assistant Médical IA",
    layout="wide"
)

# Style CSS personnalisé
st.markdown("""
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1588776814546-ec7bdc45a1d6');
            background-size: cover;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            margin-top: 1rem;
        }
        h1, h2, h3 {
            color: #003366;
        }
        .stTextInput, .stSelectbox, .stTextArea {
            background-color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Chargement de la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Interface
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🧠 DiagnosIA — Assistant IA Médical")
st.write("Bienvenue sur DiagnosIA, votre outil intelligent pour résumer les cours et simuler des cas cliniques.")

mode = st.selectbox("Choisir un mode", ["Cours", "Cas clinique"])
if mode == "Cours":
    sujet = st.text_area("Entrez un sujet de cours (ex : embolie pulmonaire)")
    if st.button("📘 Résumer"):
        if sujet:
            with st.spinner("Génération du résumé..."):
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "Tu es un assistant médical qui résume les cours pour les étudiants en médecine."},
                            {"role": "user", "content": f"Fais un résumé complet, pédagogique, clair, structuré et adapté à un étudiant en médecine sur le sujet suivant : {sujet}"}
                        ]
                    )
                    st.markdown("### Résumé du cours")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Erreur : {e}")
        else:
            st.warning("Veuillez entrer un sujet.")
else:
    st.info("🚧 Le mode 'Cas clinique' sera bientôt disponible.")

st.markdown("</div>", unsafe_allow_html=True)