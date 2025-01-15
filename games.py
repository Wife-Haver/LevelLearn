

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
import os

from games_folder import area_game




class Games:
    def __init__(self,parent):

        self.frame = tk.Frame(parent,bg="white")
        PYGAME_FILE_PATH = "games_folder/area_game/game1.py"
        def launch_pygame_program():
            try:
                # Ensure the path is absolute
                pygame_full_path = os.path.abspath(PYGAME_FILE_PATH)
                subprocess.Popen([sys.executable, pygame_full_path])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch the game: {e}")

        self.game1_btn=ctk.CTkButton(self.frame,text="game 1",width=80,height=80,command=launch_pygame_program)
        self.game1_btn.grid(row=1,column=0,padx=10,pady=10)


    def get_frame(self):
        return self.frame