import re


def clean_common_ocr_errors(text):

    corrections = {
        'O': '0',
        'l': '1',
        'I': '1',
        '|': '1'
    }

    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)

    return text


def extract_text_only(ocr_results):

    lines = []

    for item in ocr_results:

        text = item.get("text", "")

        text = clean_common_ocr_errors(text)

        lines.append(text)

    return "\n".join(lines)


def filter_low_confidence(ocr_results, threshold=0.60):

    filtered = []

    for item in ocr_results:

        if item["confidence"] >= threshold:
            filtered.append(item)

    return filtered