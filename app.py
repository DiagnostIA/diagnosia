import openai

# 👉 Remplace ici par ta propre clé API OpenAI
openai.api_key = "sk-..."  # mets ta clé ici ou utilise st.secrets si tu déploies

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
1. 🧬 Définition (claire et pédagogique)
2. 🧠 Étiologies principales (listées de manière logique et intuitive)
3. 🩺 Clinique typique (signes à retenir absolument)
4. 🧪 Biologie (examens complémentaires, anomalies classiques)
5. 🖼️ Imagerie (comment apparaît la pathologie, scores ou signes utiles s’il y en a)
6. 🧪 Étude de cas rapide pour ancrer l’apprentissage

Le ton doit être simple, structuré, fluide et orienté mémorisation pour un étudiant en médecine.
                """

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=1000
                    )
                    fiche = response["choices"][0]["message"]["content"]
                    st.markdown("---")
                    st.markdown(fiche)
                except Exception as e:
                    st.error(f"❌ Une erreur est survenue : {e}")
