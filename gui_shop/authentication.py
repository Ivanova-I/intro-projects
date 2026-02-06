import json
import re
import tkinter as tk

from canvas import app
from helpers import clean_screen
from products import render_products_screen
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number"
    if not re.search(r"[*@!]", password):
        return False, "Password must contain at least one special character (*@!)"
    return True, ""


def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Email is invalid"
    return True, ""


def add_placeholder(entry, placeholder, is_password=False):
    entry.insert(0, placeholder)
    entry.config(fg='grey')
    show_char = "*" if is_password else ""

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black', show=show_char)

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey', show="")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def login(username, password):
    with open("db/user_credentials_db.txt") as f:
        for line in f:
            user, pwd = line.strip().split(", ")
            if user == username and pwd == password:
                with open("db/current_user.txt", "w") as cu:
                    cu.write(username)
                render_products_screen()
                return

    render_login_screen(error="Invalid username/password")


def render_login_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app, show="*")
    password.grid(row=1, column=0)

    def toggle_password():
        if password.cget("show") == "":
            password.config(show="*")
            toggle_btn.config(text="Show")
        else:
            password.config(show="")
            toggle_btn.config(text="Hide")

    toggle_btn = tk.Button(app, text="Show", command=toggle_password)
    toggle_btn.grid(row=1, column=1)

    add_placeholder(username, "Username")
    add_placeholder(password, "Password", is_password=True)

    tk.Button(app,
              text="Enter",
              bg="green",
              fg="black",
              command=lambda: login(username.get(), password.get())).grid(row=2, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=3, column=0)


def register(**user):
    if user["username"] == "" or user["password"] == "" or user["first_name"] == "" or user["last_name"] == "":
        render_register_screen(error="All fields are required!")
        return
    if user["username"] == user["password"]:
        render_register_screen(error="Username and password cannot be the same!")
        return
    if len(user["username"]) < 4:
        render_register_screen(error="Username must be at least 4 characters long!")
        return

    valid, msg = validate_password(user["password"])
    if not valid:
        render_register_screen(error=msg)
        return

    if len(user["first_name"]) < 2 or len(user["last_name"]) < 2:
        render_register_screen(error="First and last names must be at least 2 characters long!")
        return

    user.update({"products": []})
    with open("db/user_credentials_db.txt", "r+") as file:
        users = [line.strip().split(", ")[0] for line in file]
        if user["username"] in users:
            render_register_screen(error="Username already exists")
            return
        file.write(f'{user["username"]}, {user["password"]}\n')

    with open(f'db/users.txt', "a") as file:
        file.write(json.dumps(user) + "\n")

    render_login_screen()


def render_register_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)
    email = tk.Entry(app, width=40)
    email.grid(row=4, column=0)

    def toggle_password():
        if password.cget("show") == "":
            password.config(show="*")
            toggle_btn.config(text="Show")
        else:
            password.config(show="")
            toggle_btn.config(text="Hide")

    toggle_btn = tk.Button(app, text="Show", command=toggle_password)
    toggle_btn.grid(row=1, column=1)

    add_placeholder(username, "Username")
    add_placeholder(password, "Password", is_password=True)
    add_placeholder(first_name, "First Name")
    add_placeholder(last_name, "Last Name")
    add_placeholder(email, "Email")

    tk.Button(app,
              text="Register",
              bg="green",
              fg="black",
              command=lambda: register(
                  username=username.get(),
                  password=password.get(),
                  first_name=first_name.get(),
                  last_name=last_name.get(),
                  email=email.get()
              )).grid(row=5, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=6, column=0)


def render_main_enter_screen():
    clean_screen()

    tk.Button(
        app,
        text="Login",
        fg="white",
        bg="#2ECC71",
        command=render_login_screen
    ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        fg="black",
        bg="#5DADE2",
        command=render_register_screen
    ).grid(row=0, column=1)




