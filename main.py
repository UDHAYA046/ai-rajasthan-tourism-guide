# main.py

import streamlit as st
from deep_translator import GoogleTranslator
from utils.info_gen import get_place_info
from utils.tts import generate_audio

# Language display names to gTTS language codes
lang_display = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Malayalam": "ml",
    "Punjabi": "pa"
}

st.set_page_config(page_title="AI Rajasthan Tourism Guide", page_icon="🏜️")
st.title("🏯 AI Rajasthan Tourism Guide")
st.markdown("### Speak with the Desert 🌵 | Multilingual Tourist Assistant")

# User inputs
place = st.text_input("Enter a place in Rajasthan:")
st.caption("Type any Rajasthan tourist location. For best results, use correct spelling (e.g., Jhalawar, Alwar, Shekhawati).")

# Smart auto-append
if place and "rajasthan" not in place.lower():
    place += ", Rajasthan"

selected_lang = st.selectbox("Select your language:", list(lang_display.keys()))
tts_lang = lang_display[selected_lang]

# Generate output
if st.button("Get Tourist Info"):
    info = get_place_info(place)

    if info:
        if isinstance(info, str):
            # Info from Wikipedia, translate to target language
            try:
                translated_text = GoogleTranslator(source='en', target=tts_lang).translate(info)
            except Exception:
                translated_text = info  # fallback to English if translation fails
        else:
            # Info from internal dictionary
            translated_text = info.get(tts_lang, info.get('en') or next(iter(info.values())))

        # Display and generate audio
        st.markdown(f"**Tourist Info ({selected_lang}):**")
        st.write(translated_text)

        audio_path = generate_audio(
            text=translated_text,
            lang=tts_lang,
            filename=f"{place.lower().replace(' ', '_')}_{tts_lang}"
        )
        st.audio(audio_path)

    else:
        st.error("Sorry, we couldn't find tourist info for that place.")
