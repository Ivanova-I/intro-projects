import os


LIBRE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"


def has_libreoffice():
    return os.path.exists(LIBRE_PATH)


def get_libre_path():
    if has_libreoffice():
        return LIBRE_PATH
    return None


def has_word():
    try:
        from win32com.client import Dispatch
        word = Dispatch("Word.Application")
        word.Quit()
        return True
    except Exception:
        return False