import streamlit as st
import openai
import os

# ✅ Imports modules perso
from modules.qcm_generator import run_qcm_generator
from modules.style_injector import inject_local_css
from modules.pdf_generator import create_pdf

# 🔽 Injection du style CSS personnalisé (propre)
inject_local_css()

# 🔐 Clé API sécurisée
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🧠 Fonction de génération de fiche médicale
def generate_medical_sheet(pathologie):
    prompt = f"""
Tu es une intelligence médicale experte, spécialisée dans la pédagogie clinique.

Ta mission : Génère une **fiche médicale complète, claire et ultra pédagogique** sur la pathologie suivante : **{pathologie.upper()}**.

Suis exactement cette structure :

1. 📌 **Définition** (clinique, humaine, non robotique)
2. 🧬 **Étiologies** (classées : infectieuses, tumorales, auto-immunes, iatrogènes, etc.)
3. 🩺 **Clinique typique** (symptômes d’appel, signes clés, formes fréquentes)
4. 🧪 **Biologie** (bilan de première intention, anomalies caractéristiques)
5. 🖼️ **Imagerie médicale** (examens utiles + éléments radiologiques typiques, scores s’il y en a)
6. ⚖️ **Diagnostic différentiel** (grands pièges à éliminer)
7. 🚨 **Complications** (à connaître absolument)
8. 💊 **Prise en charge** (urgence vs. à froid, médicaments, gestes ou chirurgie)
9. 📉 **Pronostic global**
10. 🧠 **Résumé express** (5 à 10 lignes max avec les points essentiels à retenir pour un QCM ou cas clinique)
11. 📚 **Cas clinique typique (optionnel mais pertinent)**

🎯 Style attendu :
- Clair, structuré, fluide, didactique
- Niveau ECN / externat
- Zéro blabla inutile, phrases simples, impact immédiat

📝 À la fin, ajoute un **tableau récapitulatif des points clés** pour la mémorisation rapide.
"""

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

# 🧠 Interface Streamlit
st.set_page_config(page_title="DiagnosIA", layout="centered")
st.title("🤖 DiagnosIA – L’intelligence médicale, entre tes mains")
st.caption("Une IA formée par des médecins pour les médecins.  \nFiches. Cas. QCM. Tout. En un clic.  \n_Rapide. Fiable. Brutalement efficace._")

# 📚 Choix du module
module = st.sidebar.selectbox(
    "🔍 Choisis un module",
    ["🧠 Générer une fiche médicale", "📝 Générer des QCM personnalisés"]
)

# ✅ Bloc 1 – Génération de fiche médicale
if module == "🧠 Générer une fiche médicale":
    patho_input = st.text_input("Entrez le nom de la pathologie :", "")
    
    if st.button("📄 Générer la fiche"):
        if patho_input.strip() == "":
            st.warning("⚠️ Veuillez entrer une pathologie.")
        else:
            st.markdown(f"<h2>📋 Résultat pour <strong>{patho_input.strip()}</strong> :</h2>", unsafe_allow_html=True)

            with st.spinner("🧠 Génération de la fiche en cours..."):
                fiche = generate_medical_sheet(patho_input.strip())
            
            if fiche.startswith("❌"):
                st.error(fiche)
            else:
                html_fiche = fiche.replace('\n', '<br>')
                st.markdown(f"<div class='result-box'>{html_fiche}</div>", unsafe_allow_html=True)

                if st.button("📥 Télécharger la fiche en PDF"):
                    pdf_path = create_pdf(fiche)
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="📄 Télécharger le PDF",
                            data=f,
                            file_name=f"{patho_input.strip().lower()}_fiche.pdf",
                            mime="application/pdf"
                        )
                    st.success("✅ Fiche prête à être téléchargée !")

# ✅ Bloc 2 – QCM personnalisés
elif module == "📝 Générer des QCM personnalisés":
    run_qcm_generator()
