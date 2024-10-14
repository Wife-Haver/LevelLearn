# notes.py

import tkinter as tk
from tkinter import Scrollbar, Text

class Notes:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')

        # Scrollbar
        scroll_bar = Scrollbar(self.frame)
        scroll_bar.pack(side="right", fill="y")

        # Text Area
        self.text_area = Text(self.frame, wrap=tk.WORD, yscrollcommand=scroll_bar.set)
        self.text_area.pack(fill="both", expand=True)
        scroll_bar.config(command=self.text_area.yview)

        # Clear button
        clear_button = tk.Button(self.frame, text="CLEAR", font=("Arial", 15), bg='white', fg='#333333', command=self.clear_text, bd=0)
        clear_button.pack(side="bottom")

    def clear_text(self):
        """Clear the text area content."""
        self.text_area.delete(1.0, tk.END)

    def get_frame(self):
        """Return the frame object to be used in the main application."""
        return self.frame
