import wikipedia

from wikipedia import summary
from googletrans import Translator

translator = Translator()

# Supported language codes (aligned with your TTS + UI dropdown)
lang_codes = {
    "en", "hi", "ta", "te", "kn", "bn", "gu", "mr", "ml", "pa"
}



def get_place_info(place):
    try:
        # Add ", Rajasthan" for better targeting
        if "rajasthan" not in place.lower():
            place += ", Rajasthan"

        # Try to get the summary directly
        return wikipedia.summary(place, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        # Pick the first suggested page
        try:
            return wikipedia.summary(e.options[0], sentences=2)
        except:
            return None

    except wikipedia.exceptions.PageError:
        return None

    except Exception:
        return None

