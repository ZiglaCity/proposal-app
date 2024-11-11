import tkinter as tk
import random


#define a fixed style to be used for all the widgets
label_style = {
    "font": ("Arial", 14, "italic"),
    "bg": "#e6e6e6",
    "fg": "#2b2b2b",
    "padx": 8,
    "pady": 8
}

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#BBBBBB",
    "fg": "#333333",
    "bd": 3,
    "relief": "ridge"
}

entry_style = {
    "font": ("Times New Roman", 12),
    "bg": "#ffffff",
    "fg": "#000000",
    "bd": 2,
    "relief": "solid"
}
frame_style = {
    "bg": "#e0e0e0",
    "bd": 2,
    "relief": "sunken"
}

#define a funciton which applies the styles to their respective widgets
def apply_styles(widget):
    if isinstance(widget, tk.Button):
        widget.config(**button_style)
    elif isinstance(widget, tk.Label):
        widget.config(**label_style)
    elif isinstance(widget, tk.Entry):
        widget.config(**entry_style)
    elif isinstance(widget, tk.Frame):
        widget.config(**frame_style)

    for child in widget.winfo_children():
        apply_styles(child)


def move_button(event):
    width = root.winfo_width()
    heigth = root.winfo_height()
    n = random.randint(0, width - no_button.winfo_width())
    m = random.randint(0, heigth - no_button.winfo_height())

    no_button.place(x=n, y=m)


def Yes():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    thanks_label = tk.Label(root, text="AWWW... THANKS! I LOVE YOU TOO❤")
    thanks_label.pack(pady=100)

    exit_button = tk.Button(root, text="EXIT", command=Exit)
    exit_button.pack(pady=50, padx=30)

    apply_styles(root)


def create_gui():
    global root, no_button 
    root = tk.Tk()
    root.title("Zigla's Proposal App")
    root.geometry("500x500")
    root.resizable(False, False)

    welcome_label = tk.Label(root, text="ZIGLA'S PROPOSAL TO YOU")
    welcome_label.pack(pady=20)

    propasal_label = tk.Label(root, text="DO YOU LOVE ME?")
    propasal_label.pack(pady=20)


    yes_button = tk.Button(root, text="YES!", command=Yes)
    yes_button.pack(padx=20)
  
    no_button = tk.Button(root, text="NO!")
    no_button.pack(padx=20)

    no_button.bind("<Enter>", move_button)


    apply_styles(root)

    root.mainloop()

create_gui()