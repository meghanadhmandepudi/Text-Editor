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
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path,"w") as file:
                content = text_area.get(1.0, tk.END)
                File.write(content.strip())
                messagebox.showinfo("success", "file saved successfully!")
        except Exception as e:
            messagebox.showerror("error",f"could not save file: {e}")
def toggle_dark_mode():
    current_bg = text_area.cget("background")
    if current_bg == "white":
        text_area.config(background="black", foreground="white", insertbackground="white")
    else:
        text_area.config(background="white", foreground="black", insertbackground="black")