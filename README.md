# Translator Project

## Description
Takes in PDFs of text, translates and tags them for search.

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can generate one:
```bash
pip freeze > requirements.txt
```

### 4. Run the Script
```bash
python process_pdfs.py
```

### Notes
- Ensure you have the necessary API keys in your `.env` file.
- The script processes PDFs in the `pdfs/` directory and outputs translated text for each page.
