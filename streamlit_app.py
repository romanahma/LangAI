import streamlit as st
import joblib
from translate import Translator
import warnings
warnings.filterwarnings("ignore", message=".*ScriptRunContext.*")

@st.cache_resource
def load_model():
    return joblib.load('Detection_model.joblib')

model = load_model()

language_mapping = {
    'Estonian': 'et',
    'Swedish': 'sv',
    'Thai': 'th',
    'Tamil': 'ta',
    'Dutch': 'nl',
    'Japanese': 'ja',
    'Turkish': 'tr',
    'Latin': 'la',
    'Urdu': 'ur',
    'Indonesian': 'id',
    'Portugese': 'pt',
    'French': 'fr',
    'Chinese': 'zh',
    'Korean': 'ko',
    'Hindi': 'hi',
    'Spanish': 'es',
    'Pushto': 'ps',
    'Persian': 'fa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'English': 'en',
    'Arabic': 'ar'
}

st.title("Lang-AI")
user_input = st.text_area("Enter text to translate:", "My name is Roman Ahmad")

if user_input:
    detected_lang = model.predict([user_input])[0]
    st.write(f"Detected language: {detected_lang}")
    
    target_lang_name = st.selectbox(
        "Select target language:",
        sorted(language_mapping.keys()),
        index=list(language_mapping.keys()).index('Urdu')
    )
    
    if st.button("Translate"):
        try:
            translator = Translator(
                from_lang=language_mapping[detected_lang],
                to_lang=language_mapping[target_lang_name]
            )
            translation = translator.translate(user_input)
            st.success(translation)
        except Exception as e:
            st.error(f"Error: {str(e)}")