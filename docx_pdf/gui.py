import threading
from tkinter import Label, Button, StringVar
from tkinterdnd2 import TkinterDnD, DND_FILES
from docx_pdf.converters.engine import convert


class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("DOCX → PDF Converter")
        self.geometry("600x400")
        self.configure(bg="#1e1e2f")

        self.file_path = StringVar()

        # Drop area
        self.label = Label(
            self,
            text="Drag & Drop file here",
            bg="#1e1e2f",
            fg="white",
            font=("Arial", 16, "bold"),
            height=5
        )
        self.label.pack(fill="both", expand=True, padx=20, pady=20)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind("<<Drop>>", self.drop_file)

        # Convert button
        self.convert_btn = Button(
            self,
            text="Convert to PDF",
            command=self.run_convert,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=10,
            pady=5

        )
        self.convert_btn.pack(pady=10)

        # Status label
        self.status = Label(
            self,
            text="",
            bg="#1e1e2f",
            fg="#00ffcc",
            font=("Arial", 10)
        )
        self.status.pack()

    # Drag & drop handler
    def drop_file(self, event):
        file = event.data
        file = file.replace("{", "").replace("}", "")
        self.file_path.set(file)
        self.label.config(text=file)

    # Button click (runs thread)
    def run_convert(self):
        if not self.file_path.get():
            self.status.config(text="❌ No file selected")
            return

        self.status.config(text="⏳ Converting...")
        threading.Thread(target=self._convert_file, daemon=True).start()


    def _convert_file(self):
        try:
            output = convert(self.file_path.get())
            self.status.config(text=f"✅ Done!\n{output}")

        except Exception as e:
            self.status.config(text=f"❌ Error: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()