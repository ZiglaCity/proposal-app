import tkinter as tk


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

    apply_styles(root)

    root.mainloop()

create_gui()