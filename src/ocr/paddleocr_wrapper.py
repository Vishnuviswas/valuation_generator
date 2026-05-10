from paddleocr import PaddleOCR

# Initialize PaddleOCR for English (works best)
ocr = PaddleOCR(lang='en')

def paddle_ocr(image_path):
    results = ocr.ocr(image_path)
    extracted = []

    for res in results:
        for line in res:
            try:
                # Normal PaddleOCR format:
                # line = [ [bbox], [ text, score ] ]
                text = line[1][0]
                score = line[1][1]
            except Exception:
                # Fallback — handle cases where detection is weird
                # Convert entire line to string
                text = str(line)
                score = None

            extracted.append((text, score))

    return extracted
