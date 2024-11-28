import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

class Notes:
    def __init__(self, parent):
        # Create the main frame for the Notes app
        self.frame = tk.Frame(parent, bg='white')

        # Tab header
        tab_frame = tk.Frame(self.frame, bg='#B4B4B4')
        tab_frame.pack(fill="x")

        # Button Tabs
        filebutton = tk.Menubutton(tab_frame, text="File", bg="#E0E0E0", relief="raised", width=5)
        filemenu = tk.Menu(filebutton, tearoff=False)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save as", command=self.save_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Exit", command=parent.quit)
        filebutton["menu"] = filemenu
        filebutton.pack(side="left", padx=5, pady=5)

        editbutton = tk.Menubutton(tab_frame, text="Edit", bg="#E0E0E0", relief="raised", width=5)
        editmenu = tk.Menu(editbutton, tearoff=False)
        editmenu.add_command(label="Cut", command=self.cut_text)
        editmenu.add_command(label="Copy", command=self.copy_text)
        editmenu.add_command(label="Paste", command=self.paste_text)
        editmenu.add_command(label="Clear", command=self.delete_text)
        editbutton["menu"] = editmenu
        editbutton.pack(side="left", padx=5, pady=5)

        # Text area for writing notes
        self.text_box = scrolledtext.ScrolledText(self.frame, wrap='word', bg="white", relief="flat",highlightthickness=0)
        self.text_box.pack(padx=5, pady=5, fill="both")

    # Definition methods
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:  # Ensure the user didn't cancel the dialog
            with open(file_path, 'w', encoding='utf-8') as file:
                # Remove the trailing newline added by tk.Text
                content = self.text_box.get("1.0", tk.END).rstrip("\n")
                file.write(content)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert("1.0", content)


    def copy_text(self):
        text_content = self.text_box.get("1.0", tk.END).strip()
        if text_content:
            self.text_box.clipboard_clear()
            self.text_box.clipboard_append(text_content)
    def cut_text(self):
        text_content = self.text_box.get("1.0", tk.END).strip()
        if text_content:
            self.text_box.clipboard_clear()
            self.text_box.clipboard_append(text_content)
            self.text_box.delete("1.0", tk.END)
    def delete_text(self):
        text_content = self.text_box.get("1.0", tk.END).strip()
        if text_content:
            self.text_box.delete("1.0", tk.END)
    def paste_text(self):
        try:
            clipboard_content = self.frame.clipboard_get()
            self.text_box.insert(tk.INSERT, clipboard_content)
        except tk.TclError:
            # Handle the case where clipboard is empty
            pass





    def get_frame(self):
        return self.frame

