# tasks.py

import tkinter as tk
from tkinter import *

import customtkinter as ctk











class Tasks:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure([0,1,2],weight = 1)
        self.frame.rowconfigure(0,weight = 1)

        frame1 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)
        frame2 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)
        frame3 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid", width=200)

        frame3.grid_columnconfigure([0, 1], weight=1)
        frame3.rowconfigure([0, 1, 2], weight=1)



        frame3a = tk.Frame(frame3,bg="#f0f0f0",borderwidth=0.5, relief="solid",width=200)
        frame3b = tk.Frame(frame3,bg="#f0f0f0",borderwidth=0.5, relief="solid")


        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")
        frame3.pack_propagate(False)

        frame3a.pack(side=TOP,fill="both",expand=True)
        frame3b.pack(side=BOTTOM,fill="both",expand=True)

        frame1.grid_columnconfigure([0,1,2],weight=1)



        ##FRAME 1 STUFF
        new_label = tk.Label(frame1,text="New Task",bg = "white")

        new_label.grid(row = 0,column = 1)

        title_textfield = ctk.CTkEntry(frame1, width=200,placeholder_text="Enter Task Title:")
        title_textfield.grid(row=1,column=1)

        body_label = ctk.CTkLabel(frame1,text="Task Description:",fg_color="transparent")
        body_label.grid(row=2,column=1)

        body_textfield = ctk.CTkTextbox(frame1,height=100,width=200,corner_radius=6,border_width=2)
        body_textfield.grid(row=3,column=1)


        difficulty_label = ctk.CTkLabel(frame1,text="Task Difficulty:")
        difficulty_label.grid(row=4,column=1)

        difficulty_buttons = ctk.CTkSegmentedButton(frame1,values=["Simple","Moderate","Complex"])
        difficulty_buttons.set("Simple")
        difficulty_buttons.grid(row=5,column=1)

        clear_button = ctk.CTkButton(frame1,text="CLEAR",width=80)
        clear_button.grid(row=6,column=1,pady=10)

        def add_task_func():
            task_title = title_textfield.get()
            task_description = body_textfield.get(1.0, "end")
            task_difficulty = difficulty_buttons.get().lower()#simple,moderate,complex
            print(task_title)
            print(task_description)
            print(task_difficulty)








        add_button = ctk.CTkButton(frame1, text="ADD", width=80,fg_color="green",command=add_task_func)
        add_button.grid(row=7,column=1,pady=10)



        #FRAME 2

        ongoing_label = ctk.CTkLabel(frame2,text="ongoing:")
        ongoing_label.pack()

        task_scrollbar = ctk.CTkScrollbar(frame2)
        task_scrollbar.pack(side=RIGHT, fill="y")

        task_listbox = tk.Listbox(frame2,bd=2,selectmode=tk.SINGLE,relief="solid",yscrollcommand=task_scrollbar.set)
        task_listbox.pack(padx=5,pady=5,fill="both",expand=True)
        task_scrollbar.configure(command=task_listbox.yview)

        task_listbox.insert(END,"mam paextend")




        #frame 3 a
        self.details_label = ctk.CTkLabel(frame3a, text="Select a task to view details.", wraplength=250,
                                          justify="left")
        self.details_label.pack(pady=10, padx=10)

        #frame3b
        self.finished_tasks_label=ctk.CTkLabel(frame3b,text="Finished tasks",wraplength=250)
        self.finished_tasks_label.pack(pady=10,padx=10)



    def get_frame(self):
        return self.frame




