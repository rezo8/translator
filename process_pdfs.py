import os
from pdf_parser import PDFPageIndexer

PDFS_DIR = os.path.join(os.path.dirname(__file__), 'pdfs')

def process_all_pdfs():
    for filename in os.listdir(PDFS_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(PDFS_DIR, filename)
            print(f'Processing: {filename}')
            indexer = PDFPageIndexer(pdf_path)
            pages = indexer.index_pdf()

            for page in pages:
                print(f"Page: {page['page_number']}")
                print(f"Text sample: {page['text'][:200]}")
                print('-' * 40)

if __name__ == "__main__":
    process_all_pdfs()
