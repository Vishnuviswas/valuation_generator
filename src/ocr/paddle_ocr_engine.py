from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import tempfile
import cv2

# Initialize once only
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en'
)


def paddle_ocr_extract(image_array):

    # Save temporary image
    with tempfile.NamedTemporaryFile(
        suffix='.png',
        delete=False
    ) as temp:

        cv2.imwrite(temp.name, image_array)

        results = ocr.ocr(temp.name)

    extracted_lines = []

    if results:

        for res in results:

            if res is not None:

                for line in res:

                    try:
                        text = line[1][0]
                        score = float(line[1][1])

                        extracted_lines.append({
                            "text": text,
                            "confidence": round(score, 3)
                        })

                    except:
                        continue

    return extracted_lines