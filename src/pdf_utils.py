import os
import fitz  # PyMuPDF

def pdf_to_images(pdf_path, output_dir, dpi=300):
    os.makedirs(output_dir, exist_ok=True)
    image_paths = []
    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=dpi)
            out = os.path.join(output_dir, f"page_{i}.png")
            pix.save(out)
            image_paths.append(out)
    return image_paths