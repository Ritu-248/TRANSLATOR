import streamlit as st
from utils.translator import translate_text
from utils.tts import text_to_speech
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Text Translator & TTS", page_icon="🌍", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2F4F4F;'>🌍 Translate & Speak</h1>", unsafe_allow_html=True)
st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)

# Input Section
input_text = st.text_area("Enter Text", placeholder="Type something...", height=150)
target_lang = st.selectbox("Select Target Language", ["fr", "de", "hi", "es", "zh", "ja", "ar"])

if st.button("Translate and Convert to Speech"):
    if input_text:
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text, target_lang)
            st.success("Translation Complete")
            st.text_area("Translated Text", translated_text, height=150)
        
        with st.spinner("Generating Audio..."):
            audio_file = text_to_speech(translated_text, target_lang)
            st.audio(audio_file)
            st.download_button("Download Audio", audio_file, file_name="speech.mp3")
    else:
        st.warning("Please enter some text to translate.")
