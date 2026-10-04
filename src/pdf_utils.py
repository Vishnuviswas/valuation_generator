from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder, dpi=200):
    os.makedirs(output_folder, exist_ok=True)

    # 👇 VERY IMPORTANT FOR WINDOWS FIX
    poppler_path = r"C:\Release-26.02.0-0\poppler-26.02.0\Library\bin"

    pages = convert_from_path(
        pdf_path,
        dpi=dpi,
        poppler_path=poppler_path
    )

    paths = []
    for i, page in enumerate(pages):
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        page.save(img_path, "PNG")
        paths.append(img_path)

    return paths
