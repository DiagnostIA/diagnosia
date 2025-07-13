import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_medical_sheet(pathologie):
    prompt = f"""Génère une fiche médicale claire et intuitive sur : {pathologie.upper()}

Structure de la fiche :
- Définition
- Étiologies
- Clinique typique
- Biologie
- Imagerie (avec scores spécifiques s’il y en a)
- Étude de cas (facultatif mais pertinent)

Sois pédagogique, fluide, avec des phrases naturelles pour un étudiant en médecine."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un professeur de médecine très pédagogue."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Une erreur est survenue : {e}"
