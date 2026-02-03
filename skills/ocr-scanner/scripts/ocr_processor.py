"""
OCR Scanner - Text extraction from images
Usage: python ocr_processor.py [image_path] [--lang ko+eng] [--output json|txt|excel]
"""

import sys
import os
import json
import re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Check for OCR libraries
OCR_ENGINE = None
try:
    import easyocr
    OCR_ENGINE = 'easyocr'
except ImportError:
    try:
        import pytesseract
        from PIL import Image
        OCR_ENGINE = 'tesseract'
    except ImportError:
        print("Error: No OCR engine found.")
        print("Install one of:")
        print("  pip install easyocr")
        print("  pip install pytesseract Pillow (+ Tesseract-OCR)")

def ocr_with_easyocr(image_path, languages=['ko', 'en']):
    """OCR using EasyOCR (better for Korean)."""
    import easyocr
    reader = easyocr.Reader(languages, gpu=False)
    results = reader.readtext(image_path)

    # Extract text
    texts = [item[1] for item in results]
    full_text = '\n'.join(texts)

    # Extract with confidence
    detailed = [{'text': item[1], 'confidence': item[2]} for item in results]

    return full_text, detailed

def ocr_with_tesseract(image_path, lang='kor+eng'):
    """OCR using Tesseract."""
    import pytesseract
    from PIL import Image

    image = Image.open(image_path)

    # OCR with Korean + English
    text = pytesseract.image_to_string(image, lang=lang)

    # Get detailed data
    data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)

    detailed = []
    for i, txt in enumerate(data['text']):
        if txt.strip():
            detailed.append({
                'text': txt,
                'confidence': data['conf'][i]
            })

    return text, detailed

def extract_receipt_data(text):
    """Extract structured data from receipt text."""
    data = {
        'date': None,
        'store': None,
        'total': None,
        'card_last4': None,
        'items': []
    }

    # Date patterns
    date_patterns = [
        r'(\d{4}[-/.]\d{2}[-/.]\d{2})',
        r'(\d{2}[-/.]\d{2}[-/.]\d{2})',
    ]
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            data['date'] = match.group(1)
            break

    # Amount patterns (Korean Won)
    amount_pattern = r'합\s*계[:\s]*([\d,]+)\s*원?|총[액계][:\s]*([\d,]+)\s*원?|([\d,]+)\s*원'
    amounts = re.findall(amount_pattern, text)
    if amounts:
        # Get the largest amount as total
        all_amounts = []
        for match in amounts:
            for amt in match:
                if amt:
                    all_amounts.append(int(amt.replace(',', '')))
        if all_amounts:
            data['total'] = f"{max(all_amounts):,}원"

    # Card number (last 4 digits)
    card_pattern = r'\*{4}[-\s]?\*{4}[-\s]?\*{4}[-\s]?(\d{4})'
    match = re.search(card_pattern, text)
    if match:
        data['card_last4'] = match.group(1)

    return data

def process_image(image_path, output_format='txt'):
    """Process image and extract text."""
    print(f"\n{'='*60}")
    print(f"OCR Processing: {os.path.basename(image_path)}")
    print(f"Engine: {OCR_ENGINE}")
    print('='*60)

    # Perform OCR
    if OCR_ENGINE == 'easyocr':
        text, detailed = ocr_with_easyocr(image_path)
    elif OCR_ENGINE == 'tesseract':
        text, detailed = ocr_with_tesseract(image_path)
    else:
        print("No OCR engine available!")
        return None

    print(f"\n[Extracted Text]")
    print("-" * 40)
    print(text[:500] + "..." if len(text) > 500 else text)
    print("-" * 40)

    # Try to extract structured data (receipt)
    receipt_data = extract_receipt_data(text)

    if any(receipt_data.values()):
        print(f"\n[Extracted Data]")
        for key, value in receipt_data.items():
            if value:
                print(f"  {key}: {value}")

    # Save output
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs('Output', exist_ok=True)

    if output_format == 'json':
        output_path = f'Output/ocr_{timestamp}.json'
        output_data = {
            'source': image_path,
            'timestamp': timestamp,
            'raw_text': text,
            'extracted': receipt_data,
            'detailed': detailed
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

    elif output_format == 'txt':
        output_path = f'Output/ocr_{timestamp}.txt'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"Source: {image_path}\n")
            f.write(f"Date: {timestamp}\n")
            f.write("="*40 + "\n")
            f.write(text)

    else:  # excel
        try:
            import pandas as pd
            output_path = f'Output/ocr_{timestamp}.xlsx'
            df = pd.DataFrame([receipt_data])
            df.to_excel(output_path, index=False)
        except ImportError:
            output_path = f'Output/ocr_{timestamp}.txt'
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)

    print(f"\n[Saved]")
    print(f"  {output_path}")

    return text, receipt_data

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print(f"\nCurrent OCR Engine: {OCR_ENGINE or 'None installed'}")
        sys.exit(0)

    image_path = sys.argv[1]

    # Parse options
    output_format = 'txt'
    for i, arg in enumerate(sys.argv):
        if arg == '--output' and i + 1 < len(sys.argv):
            output_format = sys.argv[i + 1]

    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}")
        sys.exit(1)

    process_image(image_path, output_format)

if __name__ == "__main__":
    main()
