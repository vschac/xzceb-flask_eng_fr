from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translate English text to French.
    """
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return frenchText


def french_to_english(french_text):
    """
    Translate French text to English.
    """
    englishText = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return englishText