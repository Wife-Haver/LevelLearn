import tkinter as tk
from tkinter import  ttk
import customtkinter as ctk
from tasks import get_tasks
from tkinter import filedialog,messagebox
import os



class Home:
    def __init__(self,parent):
        self.task_item_frame = None
        self.frame = tk.Frame(parent, bg='white')
        quick_access_notes = tk.Label(self.frame, text="Notes quick acess",
                                      font=("Arial", 10), bg='white', fg='#333333')
        quick_access_notes.grid(row=0,column=0)

        #ongoing tasks for home page
        self.tasks_frame = ctk.CTkFrame(self.frame,fg_color="black")

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


    def get_frame(self):
        return self.frame




#