import streamlit as st
import openai
import os

def run_qcm_generator():
    st.title("📝 Générateur intelligent de QCM")
    st.markdown("Crée automatiquement des QCM ciblés à partir de ton cours ou des notions à revoir.")

    contenu = st.text_area("✍️ Colle ici ton cours ou tes erreurs", height=300)
    nb_qcm = st.slider("🧪 Nombre de QCM à générer", 1, 20, 5)
    
    # 🔀 Nouvelle option d'affichage
    mode_affichage = st.radio(
        "📚 Mode d'affichage du corrigé :",
        ["➡️ Corrigé directement après chaque QCM", "➡️ Corrigé global à la fin"]
    )

    bouton = st.button("🔄 Générer les QCM")

    if bouton and contenu.strip():
        with st.spinner("Génération en cours... ⏳"):
            client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            # Prompt selon le mode choisi
            if mode_affichage == "➡️ Corrigé directement après chaque QCM":
                prompt = f"""
Tu es un expert en pédagogie médicale. À partir de ce qui est demaandé , génère {nb_qcm} QCM de type ECN avec une seule bonne réponse par question.

Après chaque question, donne :
- La bonne réponse (ex. **Réponse : B**)
- Une explication pédagogique courte (1 à 3 lignes)

Format :
**Question 1 :**
Quel est ... ?
- A. ...
- B. ...
- C. ...
- D. ...
**Réponse : B**
**Explication :** ...

Texte :
{contenu}
"""
            else:
                prompt = f"""
Tu es un expert en pédagogie médicale. À partir du texte suivant, génère {nb_qcm} QCM de type ECN avec une seule bonne réponse par question.

Affiche d'abord tous les QCM sans réponse.
Puis, en seconde partie, affiche les bonnes réponses avec une explication brève pour chacune.

Format :
**Partie 1 – QCM :**
...

**Partie 2 – Corrigé :**
Question 1 : Réponse B – Explication : ...

Texte :
{contenu}
"""

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un assistant médical expert en QCM pour étudiants."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )

            st.markdown("---")
            st.subheader("📋 Résultats :")
            st.markdown(response.choices[0].message.content)
