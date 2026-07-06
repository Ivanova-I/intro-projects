from docx_pdf.converters import libre, word
from docx_pdf.utils.detector import has_word, has_libreoffice


def convert(file_path: str):
    ext = file_path.lower().split(".")[-1]

    if ext not in ["docx", "odt", "doc"]:
        raise ValueError("Only docx, doc, odt supported")

    if has_word():
        return word.convert(file_path)

    if has_libreoffice():
        return libre.convert(file_path)

    raise RuntimeError("No converter found (Word or LibreOffice required)")