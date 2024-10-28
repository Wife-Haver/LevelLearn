# xp_bar.py

import tkinter as tk
import customtkinter as ctk


class XPBar(tk.Frame):
        def __init__(self, parent, max_xp = 100,**kwargs):

            super().__init__(parent, **kwargs)
            self.current_xp = 0

            self.frame = tk.Frame(self,bg="#0486ba")
            self.frame.pack()


            self.progressbar = ctk.CTkProgressBar(self.frame,width=100,height=20,corner_radius=10,
                                                  progress_color=   "#5cf25c")
            self.progressbar.start()
            self.progressbar.pack(padx =20 )
