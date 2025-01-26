from googletrans import Translator

def translate_description(description, language):
    translator = Translator()

    if language == 'en':
        return description

    match language:
        case 'uk' | 'ru':
            return translator.translate(description, dest='uk').text
        case _:
            # Otherwise, translate to the desired language
            return translator.translate(description, dest=language).text