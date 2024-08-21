from mtranslate import translate

strings_to_translate = ['ஆன்லைனில் Google உள்ளீட்டு கருவியை முயற்சிக்கவும்']
target_language = 'en'

for text in strings_to_translate:
    translation = translate(text, target_language)
    print(text, '->', translation)


