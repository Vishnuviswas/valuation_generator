from src.pdf_utils import pdf_to_images
from src.ocr.tesseract_english import ocr_english
from src.nlp.field_extractor import extract_all_fields
import json

pdf = r"E:\vishnu viswas\ai_valuation\TIR - K K Suja.pdf"

images = pdf_to_images(pdf, "output_pages")

for img_path in images:
    print("\n==============================")
    print("Processing Page:", img_path)
    print("==============================")

    text = ocr_english(img_path)

    print("\n--- OCR (English) Result ---\n")
    print(text)

    fields = extract_all_fields(text)

    print("\n--- Extracted Fields ---\n")
    print(json.dumps(fields, indent=2))
