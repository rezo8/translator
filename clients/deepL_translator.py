from langdetect import detect, LangDetectException
import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass
@dataclass
class PageTranslation:
    original_text: str
    language: str
    translated_text: str

load_dotenv()


api_key = os.getenv('DEEPL_API_KEY')

def translate_text(text: str, target_lang: str = 'EN') -> PageTranslation:
    """
    Translate text using DeepL API.
    Loads API key from .env file (DEEPL_API_KEY).
    """
    try:
        lang = detect(text) if text.strip() else None
    except LangDetectException:
        lang = None

    if(lang and lang.lower() != target_lang.lower()):
        translated = run_translation(text, 'EN')
    else:
        translated = None

    return PageTranslation(
        original_text=text,
        language=lang,
        translated_text=translated
    )




def run_translation(text: str, lang: str) -> str:
    if not api_key:
            raise ValueError('DEEPL_API_KEY not found in .env file')
    if not text.strip():
        return None
    url = 'https://api-free.deepl.com/v2/translate'
    headers = {'Authorization': f'DeepL-Auth-Key {api_key}'}
    data = {
        'text': text,
        'target_lang': 'EN'
    }
    # return text
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['translations'][0]['text']
    except Exception as e:
        print(f"Translation error: {e}")
        return None
