import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tools_folder.auto_flashcards import FlashcardTool
from tools_folder.alphabetize import Alphabetize


class Tools:
    def __init__(self, parent):
        # Main container frame
        self.frame = tk.Frame(parent, bg="white")
        self.current_frame = None

        # Load tool icons and buttons
        self.load_tools()

    def load_tools(self):
        # Load the flashcard icon
        self.img_path = "assets/pics/Flash Card.png"
        self.flashcard_icon = Image.open(self.img_path).resize((100, 100))
        # self.tool_icon = ctk.CTkImage(light_image=self.flashcard_icon,
        #                               dark_image=self.flashcard_icon,
        #                               size=(100, 100))

        # Flashcard button
        self.flashcard_btn = ctk.CTkButton(
            self.frame,
            #image=self.tool_icon
            text="flashcards",  # Added text to clarify button purpose
            command=self.open_flashcards
        )
        self.flashcard_btn.pack(side="top", anchor="nw", padx=20, pady=20)

        #Sort alphabetically tool
        self.sorter_btn = ctk.CTkButton(
            self.frame,
            #image=
            text="sorter",
            command=self.open_alphabetical
        )
        self.sorter_btn.pack(side="top", anchor="nw", padx=20, pady=20)

    def open_flashcards(self):
        # Create a new top-level window for flashcards
        flashcard_window = tk.Toplevel(self.frame)
        flashcard_window.title("Flashcard Tool")
        flashcard_window.geometry("500x600")

        # Create FlashcardTool instance in the new window
        flashcard_app = FlashcardTool(flashcard_window)

        # Pack the frame
        flashcard_app.get_frame().pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    def open_alphabetical(self):
        sorter_window = tk.Toplevel(self.frame)
        sorter_window.title("Sort by alphabet tool")
        sorter_window.geometry("500x600")

        sorter_app = Alphabetize(sorter_window)

        sorter_app.get_frame().pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def get_frame(self):
        return self.frame