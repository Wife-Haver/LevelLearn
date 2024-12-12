# flashcard_tool.py
import tkinter as tk
from tkinter import filedialog, messagebox


class FlashcardTool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="lightblue")

        # Initialize attributes
        self.flashcards = []
        self.current_index = 0

        # GUI elements for flashcards
        self.card_label = tk.Label(self.frame, text="", font=("Arial", 24), wraplength=400, bg="lightblue")
        self.card_label.pack(pady=20)

        self.definition_label = tk.Label(self.frame, text="", font=("Arial", 16), fg="gray", bg="lightblue")
        self.definition_label.pack(pady=10)

        self.show_button = tk.Button(self.frame, text="Show Definition", command=self.show_definition)
        self.show_button.pack(pady=5)

        self.next_button = tk.Button(self.frame, text="Next", command=self.next_card)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(self.frame, text="Previous", command=self.previous_card)
        self.prev_button.pack(pady=5)

        self.load_button = tk.Button(self.frame, text="Load Notes File", command=self.load_file)
        self.load_button.pack(pady=5)

        # Keyboard navigation
        parent.bind("<Right>", lambda event: self.next_card())
        parent.bind("<Left>", lambda event: self.previous_card())

    def get_frame(self):
        return self.frame

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Select Notes File", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                self.flashcards = [line.strip().split(":", 1) for line in file if ":" in line]

            if not self.flashcards:
                raise ValueError("No valid flashcards found in file.")

            self.current_index = 0
            self.display_card()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def display_card(self):
        if not self.flashcards:
            self.card_label.config(text="No flashcards available.")
            self.definition_label.config(text="")
            return

        term, _ = self.flashcards[self.current_index]
        self.card_label.config(text=term)
        self.definition_label.config(text="")

    def show_definition(self):
        if not self.flashcards:
            return
        _, definition = self.flashcards[self.current_index]
        self.definition_label.config(text=definition)

    def next_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.display_card()

    def previous_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.display_card()