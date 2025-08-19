import pdfplumber
from typing import List, Dict, Any
from langdetect import detect, LangDetectException
import requests

from clients.deepL_translator import translate_text
class PDFPageIndexer:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.pages = []

    def index_pdf(self) -> List[Dict[str, Any]]:
        
        with pdfplumber.open(self.pdf_path) as pdf:
          for i, page in enumerate(pdf.pages):
            self.process_page(page, i)
        return self.pages

    def get_document_text(self) -> str:
        return '\n'.join(page['text'] for page in self.pages)

    def process_page(self, page, page_number):
        text = page.extract_text() or ''
        translationResult = translate_text(text, 'EN')
        self.pages.append({
          'page_number': page_number + 1,
          'text': text,
          'translated_text': translationResult.translated_text,
          'language': translationResult.language
        })

  
