
import streamlit as st
import openai

# Configuration de la page
st.set_page_config(
    page_title="🧠 DiagnosIA — Assistant IA Médical",
    page_icon="🧠",
    layout="wide",
)

# Style CSS personnalisé
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #0d1117;
            color: #ffffff;
        }
        .main {
            padding: 3rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stTextInput > div > div > input {
            background-color: #1f2937;
            color: white;
            border-radius: 10px;
            padding: 0.75rem;
        }
        .stTextArea textarea {
            background-color: #1f2937;
            color: white;
            border-radius: 10px;
            padding: 0.75rem;
        }
        .stSelectbox > div {
            background-color: #1f2937;
            color: white;
            border-radius: 10px;
            padding: 0.75rem;
        }
        .stButton > button {
            background-color: #2563eb;
            color: white;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 10px;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #1d4ed8;
        }
    </style>
""", unsafe_allow_html=True)

# Chargement de l'API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# En-tête
st.title("🧠 DiagnosIA — Assistant IA Médical")
st.markdown("Bienvenue sur **DiagnosIA**, votre outil intelligent pour résumer les cours et simuler des cas cliniques.")

# Choix du mode
mode = st.selectbox("Choisir un mode", ["Cours", "Cas clinique"])

# Champ de saisie
question = st.text_area("Entrez un sujet de cours (ex : embolie pulmonaire)", height=100)

# Résultat
if st.button("📄 Résumer" if mode == "Cours" else "🩺 Simuler le cas"):
    with st.spinner("Traitement en cours..."):
        if mode == "Cours":
            prompt = f"Fais-moi un résumé clair, structuré, pédagogique et synthétique sur : {question}"
        else:
            prompt = f"Simule un cas clinique interactif d'examen avec questions/réponses sur : {question}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un assistant médical pour étudiants en médecine."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success("✅ Résultat généré")
            st.markdown(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
