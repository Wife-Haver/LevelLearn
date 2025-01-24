import tkinter as tk
import customtkinter as ctk

from notes import Notes  # Importing the Notes class from the notes module
from tasks import Tasks
from tools import Tools
from games import Games
from home import Home


class MainApp:
    def add_xp(self, dif):
        exp_value = None

        # Determine the XP value based on difficulty
        if dif == "simple":
            exp_value = 0.1
        elif dif == "moderate":
            exp_value = 0.3
        elif dif == "complex":
            exp_value = 0.5

        # Update EXP and Level
        current_xp = self.exp_bar.get()
        if current_xp < 0.9:
            self.exp_bar.set(current_xp + exp_value)
        elif current_xp >= 0.9:
            self.current_level += 1
            self.level_label.config(text=f"Level:{self.current_level}")
            self.exp_bar.set(0)

        # Save progress to file
        self.save_progress()

    def save_progress(self):
        """Save the current level and experience to the save file."""
        with open("save.txt", "w") as file:
            file.write(f"Level:{self.current_level}\n")
            file.write(f"Exp:{self.exp_bar.get()}\n")

    def __init__(self, root):
        file_name = "save.txt"

        # Open and read the file
        with open(file_name, "r") as file:
            lines = file.readlines()

        # Initialize variables
        self.level = None
        self.exp = None

        # Parse each line to extract the variables
        for line in lines:
            key, value = line.strip().split(":")  # Split each line into key and value
            if key == "Level":
                self.level = int(value)  # Assign and convert to integer
            elif key == "Exp":
                self.exp = float(value)  # Assign and convert to float

        # Output only the numbers
        print(self.level)
        print(self.exp)

        self.level_label = None
        self.exp_bar = None
        self.frames = None
        self.right_frame = None
        self.top_frame = None
        self.left_frame = None
        self.root = root
        self.root.title("LevelLearn")
        self.root.geometry("1000x600")
        self.root.configure(bg='#333333')

        # Create frames and UI layout
        self.create_left_frame()
        self.create_top_frame()
        self.create_right_frame()

        # Initialize default frame (Home)
        self.show_frame(self.frames['Home'])

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bg='#0486ba')
        self.left_frame.pack(side='left', fill='y')

        program_label = tk.Label(master=self.left_frame, text="LevelLearn", font=("Arial", 25), bg='#0486ba', fg='white')
        program_label.pack(pady=10)

        # Create buttons using a loop to reduce redundancy
        buttons = [
            ("Home", self.show_home_frame),
            ("Notes", self.show_notes_frame),
            ("Tasks", self.show_tasks_frame),
            ("Games", self.show_games_frame),
            ("Tools", self.show_tools_frame),  # New Tools button
        ]
        for text, command in buttons:
            ctk.CTkButton(self.left_frame, text=text, text_color="black", font=("Arial", 20),
                          border_width=0, fg_color="white",
                          width=150, height=50, command=command, hover_color="white").pack(pady=15)

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.root, height=80, bg="#0486ba")
        self.top_frame.pack_propagate(False)

        self.LevelLearn_label = ctk.CTkLabel(self.top_frame, text="LevelLearn", bg_color="#0486ba")

        self.level_label = tk.Label(self.top_frame, text="Lvl:1", bg="#0486ba")
        self.current_level = self.level

        self.level_label.config(text=f"Level:{self.current_level}")
        self.exp_bar = ctk.CTkProgressBar(self.top_frame, width=150, height=20, corner_radius=0,
                                          progress_color="#5cf25c")
        self.exp_bar.set(self.exp)

        self.exp_bar.pack(side="right", padx=10)
        self.level_label.pack(side="right")
        self.top_frame.pack(side='top', fill="x")

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bg='white')
        self.right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=20)

        self.frames = {
            'Home': Home(self.right_frame).get_frame(),
            'Notes': Notes(self.right_frame).get_frame(),
            'Tasks': Tasks(self.right_frame, self).get_frame(),
            'Games': Games(self.right_frame).get_frame(),
            'Tools': Tools(self.right_frame).get_frame(),  # Adding Tools frame
        }

        # Place all frames on the right_frame (stacked on top of each other)
        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)

    @staticmethod
    def show_frame(frame):
        frame.tkraise()

    def show_home_frame(self):
        self.show_frame(self.frames['Home'])

    def show_notes_frame(self):
        self.show_frame(self.frames['Notes'])

    def show_tasks_frame(self):
        self.show_frame(self.frames['Tasks'])

    def show_games_frame(self):
        self.show_frame(self.frames['Games'])

    def show_tools_frame(self):  # New method to handle Tools frame
        self.show_frame(self.frames['Tools'])


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
