from gtts.tts import gTTS
import functools, os, sys, re


def speak(text, language, slow=False):
    if not os.path.exists('saved'):
        os.makedirs('saved')

    if not os.path.exists("saved/" + language):
        os.makedirs("saved/" + language)

    code2lang = {
        'af': 'Afrikaans', 
        'sq': 'Albanian', 
        'ar': 'Arabic', 
        'hy': 'Armenian', 
        'bn': 'Bengali', 
        'bs': 'Bosnian', 
        'ca': 'Catalan', 
        'hr': 'Croatian', 
        'cs': 'Czech', 
        'da': 'Danish', 
        'nl': 'Dutch', 
        'en': 'English', 
        'eo': 'Esperanto', 
        'et': 'Estonian', 
        'tl': 'Filipino', 
        'fi': 'Finnish', 
        'fr': 'French Normal', 
        'de': 'German', 
        'el': 'Greek', 
        'gu': 'Gujarati', 
        'hi': 'Hindi', 
        'hu': 'Hungarian', 
        'is': 'Icelandic', 
        'id': 'Indonesian', 
        'it': 'Italian', 
        'ja': 'Japanese', 
        'jw': 'Javanese', 
        'kn': 'Kannada', 
        'km': 'Khmer', 
        'ko': 'Korean', 
        'la': 'Latin', 
        'lv': 'Latvian', 
        'mk': 'Macedonian', 
        'ml': 'Malayalam', 
        'mr': 'Marathi', 
        'my': 'Myanmar', 
        'ne': 'Nepali', 
        'no': 'Norwegian', 
        'pl': 'Polish', 
        'pt': 'Portuguese', 
        'ro': 'Romanian', 
        'ru': 'Russian', 
        'sr': 'Serbian', 
        'si': 'Sinhala', 
        'sk': 'Slovak', 
        'es': 'Spanish', 
        'su': 'Sundanese', 
        'sw': 'Swahili', 
        'sv': 'Swedish', 
        'ta': 'Tamil', 
        'te': 'Telugu', 
        'th': 'Thai', 
        'tr': 'Turkish', 
        'uk': 'Ukrainian', 
        'ur': 'Urdu', 
        'vi': 'Vietnamese', 
        'cy': 'Welsh', 
        'zh-cn': 'Mandarin', 
        'zh-tw': 'Chinese (Mandarin/Taiwan)', 
        'en-us': 'English (US)', 
        'en-ca': 'English (Canada)', 
        'en-uk': 'English (UK)', 
        'en-gb': 'English (UK)', 
        'en-au': 'English (Australia)',
        'en-gh': 'English (Ghana)', 
        'en-in': 'English (India)', 
        'en-ie': 'English (Ireland)', 
        'en-nz': 'English (New Zealand)', 
        'en-ng': 'English (Nigeria)', 
        'en-ph': 'English (Philippines)', 
        'en-za': 'English (South Africa)', 
        'en-tz': 'English (Tanzania)', 
        'fr-ca': 'French (Canada)', 
        'fr-fr': 'French', 
        'pt-br': 'Portuguese (Brazil)', 
        'pt-pt': 'Portuguese (Portugal)', 
        'es-es': 'Spanish', 
        'es-us': 'Spanish (United States)'
    }

    lang2code = {v: k for k, v in code2lang.items()}
    
    try:
        gTTS(text, lang=lang2code[language], slow=slow).save(os.path.join("saved", language, functools.reduce(lambda a, b: a + "_" + b, re.sub(r'[^\w\s]', "", text.lower()).split()) + '.mp3'))
    except ValueError:
        print ("Connectivity Error! Try Again.")


if len(sys.argv) > 3:
    speak(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    speak(sys.argv[1], sys.argv[2])