from googletrans import Translator

def translate_description(description, language):
    translator = Translator()

    if language == 'en':
        return description

    # Otherwise, translate to the desired language
    return translator.translate(description, dest=language).text