import tkinter as tk
from tkinter import  ttk
import customtkinter as ctk
from tasks import get_tasks


class Home:
    def __init__(self,parent):
        self.frame = tk.Frame(parent, bg='white')
        home_label = tk.Label(self.frame, text="Home Page", font=("Arial", 20), bg='white', fg='#333333')
        home_label.grid(row=0, column=0)

        #ongoing tasks for home page
        self.tasks_frame = ctk.CTkFrame(self.frame,fg_color="white")

        def display_task_in_list(self, task):
            # Task item container
            task_item_frame = ctk.CTkFrame(self.tasks_frame, fg_color="#f0f0f0")

            # Color indicator for difficulty
            color_indicator = tk.Label(task_item_frame, text=" ", width=2, height=1)
            if task.diff == "simple":
                color_indicator.configure(bg="green")
            elif task.diff == "moderate":
                color_indicator.configure(bg="orange")
            elif task.diff == "complex":
                color_indicator.configure(bg="red")
            color_indicator.grid(row=0, column=0, padx=5, pady=5)

        self.tasks = get_tasks()

        for task in self.tasks:
            pass




    def get_frame(self):
        return self.frame


