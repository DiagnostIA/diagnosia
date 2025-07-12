
import streamlit as st
import openai
import os

st.set_page_config(page_title="DiagnosIA", page_icon="🧠")

st.title("🧠 DiagnosIA — Assistant IA Médical")

mode = st.sidebar.selectbox("Choisir un mode", ["Cours", "Cas clinique", "QCM"])

openai.api_key = st.secrets["OPENAI_API_KEY"]

if mode == "Cours":
    sujet = st.text_area("Entre un sujet de cours (ex : embolie pulmonaire)", height=150)
    if st.button("Résumer"):
        with st.spinner("Génération du résumé..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un professeur de médecine. Résume le sujet pour un étudiant de façon claire et pédagogique."},
                    {"role": "user", "content": sujet}
                ]
            )
            st.markdown(response["choices"][0]["message"]["content"])

elif mode == "Cas clinique":
    cas = st.text_area("Décris un cas clinique ou une suspicion (ex : homme 65 ans, douleur thoracique...)")
    if st.button("Analyser"):
        with st.spinner("Analyse du cas..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un médecin expert. Analyse le cas clinique en suivant une démarche diagnostique claire avec arbre décisionnel si utile."},
                    {"role": "user", "content": cas}
                ]
            )
            st.markdown(response["choices"][0]["message"]["content"])

else:
    question = st.text_area("Entre une question ou un QCM", height=150)
    if st.button("Analyser / Vérifier"):
        with st.spinner("Analyse..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un expert en pédagogie médicale. Aide à comprendre ou corriger ce QCM pour un étudiant."},
                    {"role": "user", "content": question}
                ]
            )
            st.markdown(response["choices"][0]["message"]["content"])
