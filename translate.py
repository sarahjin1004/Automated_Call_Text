lang = {"af": "Afrikaans",
              "sq": "Albanian",
              "am": "Amharic",
              "ar": "Arabic",
              "hy": "Armenian",
              "az": "Azerbaijani",
              "eu": "Basque",
              "be": "Belarusian",
              "bn": "Bengali",
              "bs": "Bosnian",
              "bg": "Bulgarian",
              "ca": "Catalan",
              "ceb": "Cebuano",
              "ny": "Chichewa",
              "zh-CN": "Chinese",
              "co": "Corsican",
              "hr": "Croatian",
              "cs": "Czech",
              "da": "Danish",
              "nl": "Dutch",
              "en": "English",
              "eo": "Esperanto",
              "et": "Estonian",
              "tl": "Filipino",
              "fi": "Finnish",
              "fr": "French",
              "fy": "Frisian",
              "gl": "Galician",
              "ka": "Georgian",
              "de": "German",
              "el": "Greek",
              "gu": "Gujarati",
              "ht": "Haitian Creole",
              "ha": "Hausa",
              "haw": "Hawaiian",
              "iw": "Hebrew",
              "hi": "Hindi",
              "hmn": "Hmong",
              "hu": "Hungarian",
              "is": "Icelandic",
              "ig": "Igbo",
              "id": "Indonesian",
              "ga": "Irish",
              "it": "Italian",
              "ja": "Japanese",
              "jw": "Javanese",
              "kn": "Kannada",
              "kk": "Kazakh",
              "km": "Khmer",
              "rw": "Kinyarwanda",
              "ko": "Korean",
              "ku": "Kurdish (Kurmanji)",
              "ky": "Kyrgyz",
              "lo": "Lao",
              "la": "Latin",
              "lv": "Latvian",
              "lt": "Lithuanian",
              "lb": "Luxembourgish",
              "mk": "Macedonian",
              "mg": "Malagasy",
              "ms": "Malay",
              "ml": "Malayalam",
              "mt": "Maltese",
              "mi": "Maori",
              "mr": "Marathi",
              "mn": "Mongolian",
              "my": "Myanmar (Burmese)",
              "ne": "Nepali",
              "no": "Norwegian",
              "or": "Odia (Oriya)",
              "ps": "Pashto",
              "fa": "Persian",
              "pl": "Polish",
              "pt": "Portuguese",
              "pa": "Punjabi",
              "ro": "Romanian",
              "ru": "Russian",
              "sm": "Samoan",
              "gd": "Scots Gaelic",
              "sr": "Serbian",
              "st": "Sesotho",
              "sn": "Shona",
              "sd": "Sindhi",
              "si": "Sinhala",
              "sk": "Slovak",
              "sl": "Slovenian",
              "so": "Somali",
              "es": "Spanish",
              "su": "Sundanese",
              "sw": "Swahili",
              "sv": "Swedish",
              "tg": "Tajik",
              "ta": "Tamil",
              "tt": "Tatar",
              "te": "Telugu",
              "th": "Thai",
              "tr": "Turkish",
              "tk": "Turkmen",
              "uk": "Ukrainian",
              "ur": "Urdu",
              "ug": "Uyghur",
              "uz": "Uzbek",
              "vi": "Vietnamese",
              "cy": "Welsh",
              "xh": "Xhosa",
              "yi": "Yiddish",
              "yo": "Yoruba",
              "zu": "Zulu"
              }
def languages(preferred):
    l = {v: k for k, v in lang.items()}
    l["Cantonese"] = "zh-CN"
    l["Mandarin"] = "zh-CN"
    return l[preferred]

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate


    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    input = result["input"]
    translated = result["translatedText"]
    deteced_language = result["detectedSourceLanguage"]
    return translated

t = translate_text("ko","hello")
print(t)
#print(translate_text(languages["Korean"], "hello"))
    

