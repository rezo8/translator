import os
from pdf_parser import PDFProcessor

PDFS_DIR = os.path.join(os.path.dirname(__file__), 'pdfs')

def process_all_pdfs():
    for filename in os.listdir(PDFS_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(PDFS_DIR, filename)
            print(f'Processing: {filename}')
            processedPdf = PDFProcessor(pdf_path)

            for page in processedPdf.pages:
                print(f"Page: {page['page_number']}")
                print(f"Text sample: {page['text'][:200]}")
                print('-' * 40)

if __name__ == "__main__":
    process_all_pdfs()
