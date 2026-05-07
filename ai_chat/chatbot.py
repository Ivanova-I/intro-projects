import customtkinter as ctk
from openai import OpenAI
import os
from dotenv import load_dotenv
import threading
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": (
            "You are a smart, fast, friendly AI assistant. "
            "Reply naturally and conversationally."
        )
    }
]

loading = False
thinking_label = None



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Seeley AI")
app.geometry("600x700")
app.configure(fg_color="#1a1d26")


chat_container = ctk.CTkScrollableFrame(
    app,
    width=560,
    height=550,
    fg_color="#1f2330"
)
chat_container.pack(pady=10)



def add_message(text, sender="user"):
    if sender == "user":
        color = "#6c5cff"
        text_color = "white"
        anchor = "e"
    else:
        color = "#2a2f3d"
        text_color = "#e6e6e6"
        anchor = "w"

    frame = ctk.CTkFrame(chat_container, fg_color=color, corner_radius=12)
    frame.pack(fill="x", pady=5, padx=10, anchor=anchor)

    label = ctk.CTkLabel(
        frame,
        text=text,
        wraplength=400,
        justify="left",
        text_color=text_color,
        font=("Arial", 14)
    )
    label.pack(padx=10, pady=8)

    return label



def animate_loading():
    global loading, thinking_label

    frames = ["✈️", ".✈️", "..✈️", "...✈️"]
    i = 0

    while True:
        if not loading:
            break

        time.sleep(0.4)
        i = (i + 1) % len(frames)

        if thinking_label and loading:
            app.after(0, lambda f=frames[i]: thinking_label.configure(text=f))



def get_ai_response():
    global loading, thinking_label

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages)

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    loading = False
    time.sleep(0.1)

    def update():
        if thinking_label:
            thinking_label.configure(text=reply)

    app.after(0, update)



def send_message():
    global loading, thinking_label

    user_text = entry.get()
    if not user_text:
        return

    add_message(user_text, "user")
    entry.delete(0, "end")

    messages.append({"role": "user", "content": user_text})

    loading = True

    thinking_label = add_message("✈️", "assistant")

    threading.Thread(target=animate_loading, daemon=True).start()
    threading.Thread(target=get_ai_response, daemon=True).start()



input_frame = ctk.CTkFrame(app, fg_color="#1a1d26")
input_frame.pack(pady=10, fill="x")

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Message Seeley...",
    fg_color="#2a2f3d",
    text_color="white"
)
entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)



button = ctk.CTkButton(
    input_frame,
    text="📩",
    width=60,
    fg_color="#6c5cff",
    hover_color="#8a7bff",
    command=send_message
)
button.pack(side="right", padx=10)


def on_enter(e):
    button.configure(text="📬")   # open letter

def on_leave(e):
    button.configure(text="📩")   # closed letter


button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)



entry.bind("<Return>", lambda e: send_message())



add_message("Hi! I am Seeley 👋 Your AI Assistant", "assistant")

app.mainloop()