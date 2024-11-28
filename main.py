import tkinter as tk
from tkinter import Label
from xml.etree.ElementTree import tostring

import customtkinter as ctk

from notes import Notes  # Importing the Notes class from the notes module
from tasks import Tasks
from tools import Tools
from xp_bar import XPBar

class MainApp:
    def __init__(self, root):
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
        self.show_frame(self.frames['Tasks'])

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
            tk.Button(self.left_frame, text=text, font=("Arial", 15), bd=0, bg="#79ADDC", fg="white", width=7,
                      activebackground="#7990dc", activeforeground="white", command=command).pack(pady=10)

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.root, height=80, bg="#0486ba")
        self.top_frame.pack_propagate(False)

        self.level_label = tk.Label(self.top_frame, text="Lvl:1", bg="#0486ba")
        self.current_level = 0

        self.level_label.config(text=f"Level:{self.current_level}")
        self.exp_bar = ctk.CTkProgressBar(self.top_frame, width=150, height=20, corner_radius=0,
                                          progress_color="#5cf25c")
        self.exp_bar.set(0)

        self.exp_bar.pack(side="right", padx=10)
        self.level_label.pack(side="right")
        self.top_frame.pack(side='top', fill="x")

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bg='white')
        self.right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=20)

        self.frames = {
            'Home': self.create_home_frame(),
            'Notes': Notes(self.right_frame).get_frame(),
            'Tasks': Tasks(self.right_frame).get_frame(),
            'Games': self.create_games_frame(),
            'Tools': Tools(self.right_frame).get_frame(),  # Adding Tools frame
        }

        # Place all frames on the right_frame (stacked on top of each other)
        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)

    def create_home_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        home_label = tk.Label(frame, text="Home Page", font=("Arial", 20), bg='white', fg='#333333')
        home_label.grid(row=0, column=0)

        def add_xp(dif):
            exp_value = None

            if dif == "simple":
                exp_value = 0.1
            elif dif == "moderate":
                exp_value = 0.3
            elif dif == "complex":
                exp_value = 0.5

            current_xp = self.exp_bar.get()
            if current_xp < 0.9:
                self.exp_bar.set(current_xp + exp_value)
            elif current_xp >= 0.9:
                self.current_level += 1
                self.level_label.config(text=f"Level:{self.current_level}")
                self.exp_bar.set(0)

            self.current_xp = current_xp

        diff = "simple"
        btn = ctk.CTkButton(frame, text="click", command=lambda: add_xp(diff))
        btn.grid(row=1, column=2)

        return frame

    def create_games_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        games_label = tk.Label(frame, text="Games Page", font=("Arial", 20), bg='white', fg='#333333')
        games_label.pack(pady=20)
        return frame

    def create_tools_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        tools_label = tk.Label(frame, text="Tools Page", font=("Arial", 20), bg='white', fg='#333333')
        tools_label.pack(pady=20)
        return frame

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
