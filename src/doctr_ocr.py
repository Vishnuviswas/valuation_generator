from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Load once (important for Streamlit performance)
_DOCTR_MODEL = None

def get_doctr_model():
    global _DOCTR_MODEL
    if _DOCTR_MODEL is None:
        _DOCTR_MODEL = ocr_predictor(
            det_arch="db_resnet50",
            reco_arch="crnn_vgg16_bn",
            pretrained=True
        )
    return _DOCTR_MODEL


def doctr_ocr_pdf(pdf_path):
    """
    OCR a PDF using DocTR and return plain text
    """
    model = get_doctr_model()

    doc = DocumentFile.from_pdf(pdf_path)
    result = model(doc)

    lines = []

    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                text = " ".join(word.value for word in line.words)
                if text.strip():
                    lines.append(text)

    return "\n".join(lines)
