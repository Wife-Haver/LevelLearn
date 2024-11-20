# notes.py

import tkinter as tk
from tkinter import Scrollbar, Text, Entry

class Notes:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')

        # Save Button (placed at the top like a tab)
        save_button = tk.Button(self.frame, text="SAVE", font=("Arial", 12), bg='#4caf50', fg='white', command=self.save_notes, relief="flat", bd=0)
        save_button.pack(fill="x", padx=10, pady=(10, 5))

        title_label = tk.Label(self.frame, text="Title", font=("Arial", 14), bg='white', anchor="w")
        title_label.pack(fill="x", padx=10, pady=(10, 2))

        self.title_entry = Entry(self.frame, font=("Arial", 12), bg="#f9f9f9", bd=1, relief="solid", width=30)
        self.title_entry.pack(fill="x", padx=10, pady=(0, 10))

        notes_label = tk.Label(self.frame, text="Notes", font=("Arial", 14), bg='white', anchor="w")
        notes_label.pack(fill="x", padx=10, pady=(0, 2))

        text_frame = tk.Frame(self.frame, bg="white")
        text_frame.pack(fill="x", padx=10, pady=(0, 10))

        scroll_bar = Scrollbar(text_frame)
        scroll_bar.pack(side="right", fill="y")

        self.text_area = Text(
            text_frame,
            wrap=tk.WORD,
            yscrollcommand=scroll_bar.set,
            font=("Arial", 12),
            bg="#f9f9f9",
            bd=1,
            relief="solid",
            height=10,
            width=30  # Restricted width of the text box
        )
        self.text_area.pack(side="left", fill="x", expand=True)
        scroll_bar.config(command=self.text_area.yview)

        button_frame = tk.Frame(self.frame, bg='white')
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        # Clear Button
        clear_button = tk.Button(button_frame, text="CLEAR", font=("Arial", 12), bg='#f44336', fg='white', command=self.clear_text, relief="flat", bd=0)
        clear_button.pack(side="left", padx=5, pady=5)

        button_frame.pack_propagate(False)
        button_frame.config(height=40)

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)
        self.title_entry.delete(0, tk.END)

    def save_notes(self):
        pass

    def get_frame(self):
        return self.frame
