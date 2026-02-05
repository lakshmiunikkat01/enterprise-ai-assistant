def validate_file(filename: str):
    allowed = ("pdf", "docx", "txt")
    ext = filename.split(".")[-1].lower()

    if ext not in allowed:
        raise ValueError("Unsupported file type")
