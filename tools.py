import tkinter as tk
from tkinter import *

import customtkinter as ctk
from PIL import Image
import auto_flashcards
from auto_flashcards import FlashcardTool

class Tools:
    def __init__(self, parent):
        # Main container frame
        self.frame = tk.Frame(parent, bg="white")
        self.current_frame = None

        # Back button, initially hidden
        self.back_btn = ctk.CTkButton(self.frame, text="Back", command=self.show_selection)
        self.back_btn.pack(side="bottom", anchor="sw")
        self.back_btn.pack_forget()

        # Load tool icons and buttons
        self.load_tools()

    def load_tools(self):
        # Load the flashcard icon
        self.img_path = "assets/pics/Flash Card.png"
        self.flashcard_icon = Image.open(self.img_path).resize((100, 100))
        self.tool_icon = ctk.CTkImage(light_image=self.flashcard_icon,
                                      dark_image=self.flashcard_icon,
                                      size=(100, 100))

        # Flashcard button
        self.flashcard_btn = ctk.CTkButton(
            self.frame,
            image=self.tool_icon,
            text="",
            command=lambda: self.switch_frame(FlashcardTool)
        )
        self.flashcard_btn.pack(side="top", anchor="nw", padx=20, pady=20)

    def switch_frame(self, tool_class):
        # Hide the current frame (if any)
        if self.current_frame:
            self.current_frame.pack_forget()

        # Create and show the new frame
        self.current_frame = tool_class(self.frame).get_frame()
        self.current_frame.pack(fill="both", expand=True)

        # Hide main frame and show the back button
        #self.frame.pack_forget()
        self.back_btn.pack(side="bottom", anchor="sw")

    def show_selection(self):
        # Hide the current tool frame (if any)
        if self.current_frame:
            self.current_frame.pack_forget()
            self.current_frame = None

        # Show the main frame and hide the back button
        self.frame.pack(fill="both", expand=True)
        self.back_btn.pack_forget()

    def get_frame(self):
        return self.frame
