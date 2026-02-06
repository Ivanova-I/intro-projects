import tkinter as tk
from canvas import app

def clean_screen():
    for el in app.grid_slaves():
        el.destroy()


def get_current_user():
    with open("db/current_user.txt") as file:
        return file.read().strip()