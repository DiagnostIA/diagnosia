
import streamlit as st
import openai

# Configuration
st.set_page_config(
    page_title="DiagnosIA — Assistant IA Médical",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a modern look
st.markdown(
    """
    <style>
        body {
            background-color: #0f1116;
            color: #f1f1f1;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #f78fb3;
        }
        .stSelectbox > div {
            background-color: #262730;
            color: #f1f1f1;
            padding: 0.5rem;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #1e1f26;
            color: white;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.header("🧠 DiagnosIA")
mode = st.sidebar.selectbox("Choisir un mode", ["Cours", "Cas Cliniques"])

# Mode: Cours
if mode == "Cours":
    st.title("📘 Mode Cours")
    st.markdown("Entrez votre cours pour en obtenir un résumé clair et structuré.")
    user_input = st.text_area("Copiez-collez votre cours ici", height=300)

    if st.button("📄 Résumer"):
        if user_input.strip():
            openai.api_key = st.secrets["OPENAI_API_KEY"]

            with st.spinner("Analyse et résumé en cours..."):
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Tu es un expert médical. Résume clairement ce cours pour un étudiant."},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )

                st.success("Résumé généré :")
                st.markdown(response.choices[0].message.content)
        else:
            st.warning("Merci de coller un cours pour générer un résumé.")

# Mode: Cas Cliniques (en cours de développement)
elif mode == "Cas Cliniques":
    st.title("🩺 Mode Cas Cliniques")
    st.info("Cette fonctionnalité sera disponible prochainement. Restez à l'écoute !")
