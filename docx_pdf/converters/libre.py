import subprocess
from pathlib import Path
from docx_pdf.utils.detector import get_libre_path


def convert(input_file: str) -> Path:
    input_file = Path(input_file).resolve()

    libre = get_libre_path()
    if not libre:
        raise RuntimeError("LibreOffice not found")

    subprocess.run([
        libre,
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        str(input_file.parent),
        str(input_file)
    ], check=True)

    return input_file.with_suffix(".pdf")