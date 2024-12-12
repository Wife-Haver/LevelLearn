import tkinter as tk
from tkinter import messagebox, scrolledtext

import customtkinter as ctk

class Alphabetize:
    def __init__(self,parent):
        self.frame =tk.Frame(parent,bg='lightblue')

        # Input Text Area
        self.input_label = ctk.CTkLabel(self.frame, text="Input Text:")
        self.input_label.pack(pady=(10, 5))

        self.input_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=70, height=15)
        self.input_text.pack(padx=20, pady=5)

        # Separator Selection
        self.separator_label = ctk.CTkLabel(self.frame, text="Select Separator:")
        self.separator_label.pack(pady=(10, 5))

        self.separator_var = tk.StringVar(value="lines")
        self.lines_radio = ctk.CTkRadioButton(
            self.frame,
            text="By Lines",
            variable=self.separator_var,
            value="lines"
        )
        self.lines_radio.pack()

        self.comma_radio = ctk.CTkRadioButton(
            self.frame,
            text="By Comma",
            variable=self.separator_var,
            value="comma"
        )
        self.comma_radio.pack()

        self.dash_radio = ctk.CTkRadioButton(
            self.frame,
            text="By Dash",
            variable=self.separator_var,
            value="dash"
        )
        self.dash_radio.pack()

        # Sort Button
        self.sort_button = ctk.CTkButton(
            self.frame,
            text="Sort Alphabetically",
            command=self.sort_text
        )
        self.sort_button.pack(pady=10)

        # Output Text Area
        self.output_label = ctk.CTkLabel(self.frame, text="Sorted Text:")
        self.output_label.pack(pady=(10, 5))

        self.output_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=70, height=15)
        self.output_text.pack(padx=20, pady=5)

    def sort_text(self):
        # Get input text
        global items
        input_text = self.input_text.get("1.0", tk.END).strip()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter some text to sort.")
            return

        # Determine separator and split
        if self.separator_var.get() == "lines":
            items = input_text.split('\n')
        elif self.separator_var.get() == "comma":
            items = [item.strip() for item in input_text.split(',')]
        elif self.separator_var.get() == "dash":
            items = [item.strip() for item in input_text.split('-')]

        # Remove empty items and sort
        items = [item for item in items if item]
        sorted_items = sorted(items, key=str.lower)

        # Clear and populate output
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, '\n'.join(sorted_items))

    def get_frame(self):
        return self.frame


