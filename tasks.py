# tasks.py

import tkinter as tk


class Tasks:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure([0,1,2],weight = 1)
        self.frame.rowconfigure(0,weight = 1)

        frame1 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid")
        frame2 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid")
        frame3 = tk.Frame(self.frame, bg="white", borderwidth=0.5, relief="solid")

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame3.grid(row=0, column=2, sticky="nsew")

        new_label = tk.Label(frame1,text="New",bg = "white")
        ongoing_label = tk.Label(frame2, text="Ongoing", bg="white")
        done_label = tk.Label(frame3, text="Done", bg="white")



        new_label.pack(side = "top")
        ongoing_label.pack(side = "top")
        done_label.pack(side = "top")
    def get_frame(self):
        """Return the frame object to be used in the main application."""
        return self.frame
