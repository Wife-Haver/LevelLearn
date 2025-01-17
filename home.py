import tkinter as tk
from tkinter import  ttk
import customtkinter as ctk
from tasks import get_tasks
from tkinter import filedialog,messagebox
import os
from tasks import TaskClass

import pickle


class Home:
    def __init__(self,parent):
        self.frame = tk.Frame(parent, bg='white')
        #sample tasks
        task_list = get_tasks()
        task_list.append(TaskClass("New Task", "Sample Task", "simple"))

        #ongoing tasks
        self.tasks_frame = None
        self.tasks_frame = ctk.CTkFrame(self.frame, fg_color="white")
        self.tasks_frame.grid(row=1,column=1)
        tasks_label = tk.Label(self.tasks_frame, text="All Tasks", bg="white", font=("Arial", 10))
        tasks_label.pack(padx = 10)
        self.task_canvas = tk.Canvas(self.tasks_frame, background="#f0f0f0")
        self.tasks_scrollbar = ctk.CTkScrollbar(self.tasks_frame, command=self.task_canvas.yview)

        self.task_frame = tk.Frame(self.task_canvas, bg="#f0f0f0")
        self.task_canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.task_canvas.configure(yscrollcommand=self.tasks_scrollbar.set)

        self.task_canvas.pack(side="left", fill="both", expand=True)
        self.tasks_scrollbar.pack(side="right", fill="y")

        # Populate tasks from the global task list
        self.populate_tasks()

        # Bind canvas resize
        self.task_frame.bind("<Configure>", self.on_frame_configure)

        # quick access notes
        quick_access_notes = tk.Label(self.frame, text="Notes quick acess",
                                      font=("Arial", 10), bg='white', fg='#333333')
        quick_access_notes.grid(row=0,column=0)

    def populate_tasks(self):
        tasks = get_tasks()  # Get the global task list
        for task in tasks:
            self.add_task_to_canvas(task)

    def add_task_to_canvas(self, task):
        task_item_frame = ctk.CTkFrame(self.task_frame, fg_color="#f0f0f0")

        color_indicator = tk.Label(task_item_frame, text=" ", width=2, height=1)
        if task.diff == "simple":
            color_indicator.configure(bg="green")
        elif task.diff == "moderate":
            color_indicator.configure(bg="orange")
        elif task.diff == "complex":
            color_indicator.configure(bg="red")
        color_indicator.grid(row=0, column=0, padx=5, pady=5)

        task_label = tk.Label(task_item_frame, text=task.title, anchor="w", bg="#f0f0f0")
        task_label.grid(row=0, column=1, sticky="w", padx=5)

        task_item_frame.pack(fill="x", padx=5, pady=5)

    def on_frame_configure(self, event=None):
        self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all"))

        # Store the shortcuts and their file paths
        self.shortcuts = {}

        # Listbox to display shortcuts
        self.listbox = tk.Listbox(self.frame, width=50, height=15,borderwidth=5)
        self.listbox.grid(row=1,column=0)

        self.listbox.bind('<Double-1>', self.open_selected_file)

        self.open_button = tk.Button(self.frame, text="Open Notepad File", command=self.open_file)
        self.open_button.grid(row=2,column=0)

        self.clear_button = tk.Button(self.frame, text="Remove Selected Shortcut", command=self.remove_selected)
        self.clear_button.grid(row=3,column=0)

    def open_file(self):
            # Open file dialog to choose a file
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", ".txt"), ("All Files", ".*")]
        )
        if file_path:
            # Add file name and path to the listbox and dictionary
            filename = os.path.basename(file_path)
            if filename not in self.shortcuts:
                self.shortcuts[filename] = file_path
                self.listbox.insert(tk.END, filename)
            else:
                messagebox.showinfo("Info", "File shortcut already exists.")

    def open_selected_file(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_file = self.listbox.get(selected_index)
            file_path = self.shortcuts.get(selected_file)
            if file_path:
                    try:
                        os.startfile(file_path)
                    except Exception as e:
                        messagebox.showerror("Error", f"Could not open file: {e}")

    def remove_selected(self):
        # Remove selected items from the listbox and dictionary
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            selected_file = self.listbox.get(index)
            if selected_file in self.shortcuts:
                del self.shortcuts[selected_file]
            self.listbox.delete(index)

        # ongoing tasks for home page




    def get_frame(self):
        return self.frame