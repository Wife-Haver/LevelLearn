import tkinter as tk
from tkinter import *

import customtkinter as ctk



task_list = []  # Global list of tasks


class TaskClass:
    def __init__(self, title, desc, diff):
        self.title = title
        self.desc = desc
        self.diff = diff


class Tasks:
    def __init__(self, parent,main_app):
        self.frame = tk.Frame(parent, bg='white')
        self.main_app = main_app
        self.selected_task = None
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure([0, 1, 2], weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Frames
        frame1 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)
        frame2 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)
        frame3 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)

        frame3a = tk.Frame(frame3, bg="#f0f0f0", borderwidth=0.5, relief="solid", width=200,height=200)
        frame3b = tk.Frame(frame3, bg="#f0f0f0", borderwidth=0.5, relief="solid", width=200,height=200)

        frame1.grid_propagate(False)
        frame2.grid_propagate(False)
        frame3.grid_propagate(False)
        frame3a.pack_propagate(False)
        frame3b.pack_propagate(False)

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")
        frame3a.pack(side=TOP, fill="both", expand=True)
        frame3b.pack(side=BOTTOM, fill="both", expand=True)

        # Frame1 - Task Creation
        tk.Label(frame1, text="New Task", bg="white").grid(row=0, column=1, pady=10)
        title_textfield = ctk.CTkEntry(frame1, width=200, placeholder_text="Enter Task Title:")
        title_textfield.grid(row=1, column=1)

        tk.Label(frame1, text="Task Description:", bg="white").grid(row=2, column=1)
        body_textfield = ctk.CTkTextbox(frame1, height=100, width=200, corner_radius=6, border_width=2)
        body_textfield.grid(row=3, column=1)

        tk.Label(frame1, text="Task Difficulty:", bg="white").grid(row=4, column=1)
        difficulty_buttons = ctk.CTkSegmentedButton(frame1, values=["Simple", "Moderate", "Complex"])
        difficulty_buttons.set("Simple")
        difficulty_buttons.grid(row=5, column=1)

        def clear_fields():
            title_textfield.delete(0, tk.END)
            body_textfield.delete("1.0", tk.END)

        ctk.CTkButton(frame1, text="CLEAR", width=80, command=clear_fields).grid(row=6, column=1, pady=10)

        def add_task():
            title = title_textfield.get().strip()
            desc = body_textfield.get("1.0", "end").strip()
            difficulty = difficulty_buttons.get().lower()

            if title:
                # Add the new task
                new_task = TaskClass(title, desc, difficulty)
                task_list.append(new_task)
                self.display_task_in_list(new_task)  # Display new task in the list
                clear_fields()


            else:
                print("Title is required!")

        ctk.CTkButton(frame1, text="ADD", width=80, fg_color="green", command=add_task).grid(row=7, column=1, pady=10)

        # Frame2 - Task List
        tk.Label(frame2, text="Ongoing Tasks", bg="white").pack(pady=5)
        self.task_canvas = tk.Canvas(frame2, background="#f0f0f0")
        self.tasks_scrollbar = ctk.CTkScrollbar(frame2, command=self.task_canvas.yview)
        self.task_frame = tk.Frame(self.task_canvas, bg="#f0f0f0")

        self.task_canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.task_canvas.configure(yscrollcommand=self.tasks_scrollbar.set)

        self.task_canvas.pack(side="left", fill="both", expand=True)
        self.tasks_scrollbar.pack(side="right", fill="y")

        # Frame3a - Task Details
        self.details_label = tk.Label(frame3a, text="Select a task to view details.", wraplength=250, bg="#f0f0f0")
        self.details_label.pack(pady=10)

        # Frame3b - Mark as Done
        self.mark_as_done_button = ctk.CTkButton(frame3b, text="DONE", width=80, fg_color="green",
                                                 command=self.mark_task_as_done)
        self.mark_as_done_button.pack()

        self.selected_task = None  # To keep track of the selected task

    def display_task_in_list(self, task):
        # Task item container
        task_item_frame = ctk.CTkFrame(self.task_frame, fg_color="#f0f0f0")

        # Color indicator for difficulty
        color_indicator = tk.Label(task_item_frame, text=" ", width=2, height=1)
        if task.diff == "simple":
            color_indicator.configure(bg="green")
        elif task.diff == "moderate":
            color_indicator.configure(bg="orange")
        elif task.diff == "complex":
            color_indicator.configure(bg="red")
        color_indicator.grid(row=0, column=0, padx=5, pady=5)

        # Task title
        task_label = tk.Label(task_item_frame, text=task.title, anchor="w", bg="#f0f0f0")
        task_label.grid(row=0, column=1, sticky="w", padx=5)

        # Bind task click event
        task_label.bind("<Button-1>", lambda e, t=task: self.show_task_details(t))

        # Pack task item in the task list
        task_item_frame.pack(fill="x", padx=5, pady=5)

    def show_task_details(self, task):
        self.selected_task = task
        self.details_label.config(
            text=f"Title: {task.title}\n\nDescription: {task.desc}\n\nDifficulty: {task.diff.capitalize()}")

    def mark_task_as_done(self):
        if self.selected_task:

            difficulty = self.selected_task.diff
            self.main_app.add_xp(difficulty)
            task_list.remove(self.selected_task)
            self.selected_task = None

            # Clear task frame and re-display tasks
            for widget in self.task_frame.winfo_children():
                widget.destroy()
            for task in task_list:
                self.display_task_in_list(task)

            self.details_label.config(text="Task marked as done. Select another task to view details.")

    def get_frame(self):
        return self.frame
