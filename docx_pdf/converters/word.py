from pathlib import Path
from win32com.client import Dispatch
from docx_pdf.utils.detector import has_word

PDF_FORMAT = 17


def convert(input_file: str) -> Path:
    input_file = Path(input_file).resolve()

    if not input_file.exists():
        raise FileNotFoundError(input_file)

    output_file = input_file.with_suffix(".pdf")

    word = Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0

    try:
        doc = word.Documents.Open(str(input_file))
        doc.SaveAs(str(output_file), FileFormat=PDF_FORMAT)
        doc.Close()
    finally:
        word.Quit()

    return output_file