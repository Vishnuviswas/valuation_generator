import pytesseract
from PIL import Image

def tesseract_ocr(image_array):
    text = pytesseract.image_to_string(
        Image.fromarray(image_array),
        lang='eng+mal'
    )
    return text
