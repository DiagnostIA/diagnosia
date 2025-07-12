
import streamlit as st
import openai

st.set_page_config(page_title="🧠 DiagnosIA — Assistant IA Médical", layout="wide")

# Chargement des secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Styles personnalisés pour améliorer l'esthétique
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
        }
        .stSelectbox > div {
            font-weight: bold;
            font-size: 18px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .css-1aumxhk {
            font-size: 18px !important;
        }
        .css-1d391kg {
            font-size: 20px;
            color: #2c3e50;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 DiagnosIA — Assistant IA Médical")
st.subheader("Une IA conçue pour aider les étudiants en médecine à apprendre plus efficacement.")

mode = st.selectbox("🎯 Choisir un mode", ["Cours", "Cas clinique", "QCM"])

prompt = st.text_area("✍️ Entrez votre demande ici :", height=200, placeholder="Exemples :
- Résume le cours sur le diabète
- Simule un cas clinique avec diagnostic différentiel
- Crée 5 QCM sur l’hypertension avec explications")

if st.button("Lancer l’analyse 🧬"):
    if prompt:
        with st.spinner("⏳ Génération en cours..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"Tu es un assistant intelligent spécialisé en médecine. Mode sélectionné : {mode}."},
                        {"role": "user", "content": prompt},
                    ]
                )
                st.markdown("### 📋 Résultat généré")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Erreur lors de l’appel à l’API : {str(e)}")
    else:
        st.warning("Veuillez entrer une question ou un texte à analyser.")
