import tkinter as tk

def create_app():
    root = tk.Tk()
    root.title("Shopp")
    root.geometry("700x600+150+150")
    root.resizable(True, True)
    root.configure(background="#D8BFD8")

    return root

app = create_app()

