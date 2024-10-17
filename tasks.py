# tasks.py

import tkinter as tk


class Tasks:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')


        # Text Area
        label = tk.Label(self.frame,text="tasks")


        label.pack()
    def get_frame(self):
        """Return the frame object to be used in the main application."""
        return self.frame
