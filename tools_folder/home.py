import tkinter as tk
from tkinter import  ttk
import customtkinter as ctk

class Home:
    def __init__(self,parent):
        self.frame = tk.Frame(parent, bg='white')
        home_label = tk.Label(self.frame, text="Home Page", font=("Arial", 20), bg='white', fg='#333333')
        home_label.grid(row=0, column=0)


    def get_frame(self):
        return self.frame


