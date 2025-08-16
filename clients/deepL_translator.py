import requests
import os
from dotenv import load_dotenv

load_dotenv()

def translate_text(text: str, target_lang: str = 'EN') -> str:
    """
    Translate text using DeepL API.
    Loads API key from .env file (DEEPL_API_KEY).
    """
    print('TRANSLATING')
    api_key = os.getenv('DEEPL_API_KEY')
    if not api_key:
        raise ValueError('DEEPL_API_KEY not found in .env file')
    if not text.strip():
        return ''
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
        print(result)
        return result['translations'][0]['text']
    except Exception as e:
        print(f"Translation error: {e}")
        return ''
