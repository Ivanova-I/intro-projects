import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
def rename_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    prefix = prefix_entry.get()
    if not prefix:
        messagebox.showwarning("Warning", "Please enter a prefix.")
        return
    files = os.listdir(folder_path)
    count = 1
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1]
            new_name = f"{prefix}_{count:03}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            count += 1
    messagebox.showinfo("Done", "Files have been renamed!")
def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        if os.name == 'nt':
            os.startfile(folder_path)
        elif os.name == 'posix':
            subprocess.Popen(['xdg-open', folder_path])
 # GUI
window = tk.Tk()
window.title("File Renamer Tool")
window.geometry("300x200")
label = tk.Label(window, text="Prefix (e.g. photo):")
label.pack(pady=5)
prefix_entry = tk.Entry(window)
prefix_entry.pack(pady=5)
rename_button = tk.Button(window, text="Choose folder and rename", command=rename_files)
rename_button.pack(pady=10)
open_button = tk.Button(window, text="Open folder", command=open_folder)
open_button.pack(pady=5)
window.mainloop()