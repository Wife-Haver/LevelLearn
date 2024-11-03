# tasks.py

import tkinter as tk
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

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")

        frame1.grid_columnconfigure([0,1,2],weight=1)


        new_label = tk.Label(frame1,text="New Task",bg = "white")
        ongoing_label = tk.Label(frame2, text="Ongoing", bg="white")
        done_label = tk.Label(frame3, text="Done", bg="white")

        new_label.grid(row = 0,column = 1)


        title_textfield = ctk.CTkEntry(frame1, width=200,placeholder_text="Enter Task Title:")
        title_textfield.grid(row=1,column=1)

        body_label = ctk.CTkLabel(frame1,text="Task Description:",fg_color="transparent")
        body_label.grid(row=2,column=1)

        body_textfield = ctk.CTkTextbox(frame1,height=100,width=200,corner_radius=6,border_width=2)
        body_textfield.grid(row=3,column=1)

        difficulty_label = ctk.CTkLabel(frame1,text="Task Difficlty:")
        difficulty_label.grid(row=4,column=1)

        difficulty_buttons = ctk.CTkSegmentedButton(frame1,values=["Simple","Moderate","Complex"])
        difficulty_buttons.grid(row=5,column=1)

        clear_button = ctk.CTkButton(frame1,text="CLEAR",width=80)
        clear_button.grid(row=6,column=1,pady=10)

        add_button = ctk.CTkButton(frame1, text="ADD", width=80,fg_color="green")
        add_button.grid(row=7,column=1,pady=10)

        def task_title():
            title: str = title_textfield.get()
            print(title)

        tst = tk.Button(frame1,text="print",command = task_title)
        #tst.pack()








    def get_frame(self):
        return self.frame
