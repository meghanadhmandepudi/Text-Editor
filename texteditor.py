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
# Initialize the main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")
root.iconbitmap('')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Dark Mode", command=toggle_dark_mode)

# Create a text area
text_area = tk.Text(root, wrap=tk.WORD, undo=True, font=("Arial", 14))
text_area.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)

# Add scrollbars
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Start the main loop
root.mainloop()