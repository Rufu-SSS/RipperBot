from googletrans import Translator

def translate_text(language: str, text: str) -> str:
    """Traduir text a l'idioma especificat.

    Args:
        language (str): El codi d'idioma al qual es vol traduir (ex. 'es' per espanyol).
        text (str): El text que es vol traduir.

    Returns:
        str: El text traduït o un missatge d'error si hi ha problemes.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, dest=language)
        return f"**Original**: {text}\n**Translated to {language}**: {translated.text}"
    except Exception as e:
        return f"Sorry, I couldn't translate the text. Error: {e}"
