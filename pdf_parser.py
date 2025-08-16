import pdfplumber
from typing import List, Dict, Any

class PDFPageIndexer:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.pages = []

    def index_pdf(self) -> List[Dict[str, Any]]:
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ''
                self.pages.append({
                    'page_number': i + 1,
                    'text': text
                })
        return self.pages

    def get_document_text(self) -> str:
        return '\n'.join(page['text'] for page in self.pages)
