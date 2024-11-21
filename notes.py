# notes.py

import tkinter as tk
from tkinter import Scrollbar, Text, Entry

class Notes:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')

        # Tabs row for Save, Clear, and Exit
        tab_frame = tk.Frame(self.frame, bg='#f0f0f0')  # Light gray background for a Notepad-like look
        tab_frame.pack(fill="x")

        # Save Button (acting as a tab)
        save_button = tk.Button(
            tab_frame,
            text="SAVE",
            font=("Arial", 14),
            bg='#d3d3d3',  # Light gray color for buttons, matching Notepad
            fg='black',  # Black text for better contrast
            command=self.save_notes,
            relief="flat",
            bd=1,
            padx=15,
            pady=5
        )
        save_button.pack(side="left", padx=(5, 5))

        # Clear Button (acting as a tab)
        clear_button = tk.Button(
            tab_frame,
            text="CLEAR",
            font=("Arial", 14),
            bg='#d3d3d3',  # Light gray for buttons
            fg='black',
            command=self.clear_text,
            relief="flat",
            bd=1,
            padx=15,
            pady=5
        )
        clear_button.pack(side="left", padx=(0, 5))

        # Exit Button (acting as a tab)
        exit_button = tk.Button(
            tab_frame,
            text="EXIT",
            font=("Arial", 14),
            bg='#d3d3d3',  # Light gray
            fg='black',
            command=parent.quit,
            relief="flat",
            bd=1,
            padx=15,
            pady=5
        )
        exit_button.pack(side="left", padx=(0, 5))

        # Title Label and Entry
        title_label = tk.Label(self.frame, text="Title", font=("Arial", 14), bg='white', anchor="w")
        title_label.pack(fill="x", padx=10, pady=(10, 2))

        self.title_entry = Entry(self.frame, font=("Arial", 12), bg="#f9f9f9", bd=1, relief="solid", width=30)
        self.title_entry.pack(fill="x", padx=10, pady=(0, 10))

        # Notes Label and Text Area
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
            height=15,
        )
        self.text_area.pack(side="left", fill="both", expand=True)
        scroll_bar.config(command=self.text_area.yview)

    def clear_text(self):
        # Clear the content of the Title and Notes area
        self.text_area.delete(1.0, tk.END)
        self.title_entry.delete(0, tk.END)

    def save_notes(self):
        # Placeholder for saving notes functionality
        title = self.title_entry.get()
        content = self.text_area.get(1.0, tk.END)
        print(f"Saving Notes...\nTitle: {title}\nContent: {content}")

    def get_frame(self):
        return self.frame
