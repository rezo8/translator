import pdfplumber
from typing import List, Dict, Any
from langdetect import detect, LangDetectException
import requests

from clients.deepL_translator import translate_text
class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.process_pdf()


    def process_pdf(self) -> List[Dict[str, Any]]:
        with pdfplumber.open(self.pdf_path) as pdf:
            self.pages = [self.process_page(page, i) for i, page in enumerate(pdf.pages)]
    

    def process_page(self, page, page_number):
        text = page.extract_text() or ''
        translationResult = translate_text(text, 'EN')
        analyzed_page = {
          'page_number': page_number + 1,
          'text': text,
          'translated_text': translationResult.translated_text,
          'language': translationResult.language
        }
        return analyzed_page
