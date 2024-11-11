import tkinter as tk

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


    root.mainloop()

create_gui()