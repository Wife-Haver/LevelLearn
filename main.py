import tkinter as tk
from tkinter import ttk, Scrollbar, Text
from PIL import Image, ImageTk
import os


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Demo Program")
        self.root.geometry("800x600")
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

        program_label = tk.Label(master=self.left_frame, text="Program", font=("Arial", 25), bg='#0486ba', fg='white')
        program_label.pack(pady=10)

        # Create buttons using a loop to reduce redundancy
        buttons = [
            ("Home", self.show_home_frame),
            ("Notes", self.show_notes_frame),
            ("Tasks", self.show_tasks_frame),
            ("Games", self.show_games_frame)
        ]
        for text, command in buttons:
            tk.Button(self.left_frame, text=text, font=("Arial", 15), bd=0, bg="#79ADDC", fg="white", width=7,
                      activebackground="#7990dc", activeforeground="white", command=command).pack(pady=10)

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.root, bg='#0486ba', height=80)
        self.top_frame.pack(side='top', fill="x")

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bg='#ffffff')
        self.right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=20)

        self.frames = {}

        # Create frames for different sections
        self.frames['Home'] = self.create_home_frame()
        self.frames['Notes'] = self.create_notes_frame()
        self.frames['Tasks'] = self.create_tasks_frame()
        self.frames['Games'] = self.create_games_frame()

        # Place all frames on the right_frame (stacked on top of each other)
        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)

    def create_home_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        home_label = tk.Label(frame, text="Home Page", font=("Arial", 20), bg='white', fg='#333333')
        home_label.pack(pady=20)
        return frame

    def create_notes_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side="right", fill="y")

        self.text_area = Text(frame, wrap=tk.WORD, yscrollcommand=scroll_bar.set)
        self.text_area.pack(fill="both", expand=True)

        scroll_bar.config(command=self.text_area.yview)

        # Clear button
        clear_button = tk.Button(frame, text="CLEAR", font=("Arial", 15), bg='white', fg='#333333', command=self.clear_text, bd=0)
        clear_button.pack(side="bottom")
        
        return frame

    def create_tasks_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        
        create_task = tk.Frame(frame, bg="white", highlightbackground="black", highlightthickness="1")
        create_task.place(relwidth=0.33, relheight=1, relx=0, rely=0)

        ongoing_task = tk.Frame(frame, bg="white", highlightbackground="black", highlightthickness="1")
        ongoing_task.place(relwidth=0.33, relheight=1, relx=0.33, rely=0)
        
        return frame

    def create_games_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        games_label = tk.Label(frame, text="Games Page", font=("Arial", 20), bg='white', fg='#333333')
        games_label.pack(pady=20)
        return frame

    def show_frame(self, frame):
        frame.tkraise()

    def show_home_frame(self):
        self.show_frame(self.frames['Home'])

    def show_notes_frame(self):
        self.show_frame(self.frames['Notes'])

    def show_tasks_frame(self):
        self.show_frame(self.frames['Tasks'])

    def show_games_frame(self):
        self.show_frame(self.frames['Games'])

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
