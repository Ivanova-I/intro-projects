import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os
import sys


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class PDFMergerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("600x400")

        self.pdf_files = []

        self.create_widgets()


    def create_widgets(self):

        add_button = tk.Button(
            self.root,
            text="Add PDF Files here",
            command=self.add_files,
            width=20
        )
        add_button.pack(pady=10)


        self.listbox = tk.Listbox(
            self.root,
            width=80,
            height=12
        )
        self.listbox.pack(pady=10)


        merge_button = tk.Button(
            self.root,
            text="Merge PDFs",
            command=self.merge_files,
            width=20
        )
        merge_button.pack(pady=10)


        clear_button = tk.Button(
            self.root,
            text="Clear List",
            command=self.clear_files,
            width=20
        )
        clear_button.pack(pady=5)



    def add_files(self):

        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[
                ("PDF Files", "*.pdf")
            ]
        )

        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)

                self.listbox.insert(
                    tk.END,
                    file
                )



    def merge_files(self):

        if not self.pdf_files:
            messagebox.showwarning(
                "No Files",
                "Please add PDF files first."
            )
            return


        output_file = filedialog.asksaveasfilename(
            title="Save merged PDF",
            defaultextension=".pdf",
            filetypes=[
                ("PDF Files", "*.pdf")
            ]
        )


        if output_file:

            writer = PdfWriter()

            for pdf in self.pdf_files:
                writer.append(
                    pdf,
                    import_outline=False
                )


            with open(output_file, "wb") as f:
                writer.write(f)


            messagebox.showinfo(
                "Success",
                "PDF files merged successfully!"
            )



    def clear_files(self):

        self.pdf_files.clear()

        self.listbox.delete(
            0,
            tk.END
        )



if __name__ == "__main__":

    root = tk.Tk()

    # Load icon
    icon_path = resource_path("icon.ico")

    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    app = PDFMergerApp(root)

    root.mainloop()