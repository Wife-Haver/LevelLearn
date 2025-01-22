import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import os
from os.path import dirname

class Games:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")

        # Define the path to the .exe file
        EXE_FILE_PATH = ("games_folder/area_game/game1.exe")

        def launch_exe_program():
            try:
                # Get the absolute path to the .exe file
                exe_full_path = os.path.abspath(EXE_FILE_PATH)

                # Check if the file exists
                if not os.path.exists(exe_full_path):
                    raise FileNotFoundError(f"Executable file not found: {exe_full_path}")

                # Launch the .exe file
                subprocess.Popen(exe_full_path, close_fds=True)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch the game: {e}")

        # Create a button to launch the .exe file
        self.game1_btn = ctk.CTkButton(
            self.frame, text="Game 1", width=80, height=80, command=launch_exe_program
        )
        self.game1_btn.grid(row=1, column=0, padx=10, pady=10)

    def get_frame(self):
        return self.frame
