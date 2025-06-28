from gtts import gTTS
import os

def generate_audio(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    audio_path = os.path.join("audio", f"{filename}.mp3")
    tts.save(audio_path)
    return audio_path
