from docxtpl import DocxTemplate
import os

def generate_report(template_path, output_path, context):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found: {template_path}")

    doc = DocxTemplate(template_path)

    # DEBUG: prove context is correct
    print("\n===== DOCXTPL CONTEXT =====")
    for k, v in context.items():
        print(f"{k}: {v}")
    print("===========================\n")

    # Render template
    doc.render(context)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)

    print("✅ Report generated using docxtpl")
