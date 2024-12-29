import tkinter as tk
from tkinter import filedialog, messagebox

#Adding a new file to editor
def new_file():
    text_area.delete(1.0,tk.END)

#Adding a open file option
def open_file():
    file_path = filedialog.askopenfilename(filetype=[("Text Files","*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path,"r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error",f"Could not open file: {e}")
