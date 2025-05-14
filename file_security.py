import os
import re
import magic  # Ensure python-magic is installed

MAX_FILE_SIZE_MB = 10


def is_file_size_safe(file_path):
    """Reject files over MAX_FILE_SIZE_MB."""
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    return size_mb <= MAX_FILE_SIZE_MB


def sanitize_filename(filename):
    """Remove suspicious characters and limit double extensions."""
    filename = re.sub(r'[^\w\-_.]', '_', filename)  # remove risky chars
    parts = filename.split(".")
    if len(parts) > 2:
        filename = "_".join(parts[:2]) + "." + parts[-1]  # collapse middle dots
    return filename


def is_file_safe(file_path):
    """Check if file type is allowed and not suspicious."""
    try:
        file_type = magic.from_file(file_path, mime=True)
        print(f"🔍 Scanned MIME type: {file_type}")

        allowed_types = [
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # .docx
            "text/plain",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",       # .xlsx
            "application/vnd.ms-excel",                                                # .xls
            "application/vnd.openxmlformats-officedocument.presentationml.presentation" # .pptx
        ]

        return file_type in allowed_types
    except Exception as e:
        print(f"❌ MIME check failed: {e}")
        return False
