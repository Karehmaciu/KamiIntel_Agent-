import os
import fitz  # PyMuPDF
from docx import Document


def extract_text_from_file(filepath):
    if not os.path.exists(filepath):
        return "❌ File does not exist."

    ext = os.path.splitext(filepath)[1].lower()

    try:
        if ext == ".txt":
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        elif ext == ".docx":
            doc = Document(filepath)
            return "\n".join([p.text for p in doc.paragraphs])

        elif ext == ".pdf":
            doc = fitz.open(filepath)
            return "\n".join([page.get_text() for page in doc])

        else:
            return f"❌ Unsupported file format: {ext}"

    except Exception as e:
        return f"⚠️ Error reading file: {e}"
