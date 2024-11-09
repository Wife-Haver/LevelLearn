# xp_bar.py

import tkinter as tk
import customtkinter as ctk




class XPBar(tk.Frame):
        def __init__(self, parent, max_xp = 100,**kwargs):

            super().__init__(parent, **kwargs)
            self.current_xp = 0

            self.frame = tk.Frame(self,bg="#0486ba")
            self.frame.pack()




            self.progressbar = ctk.CTkProgressBar(self.frame,width=150,height=20,corner_radius=0,
                                                  progress_color= "#5cf25c")
            self.progressbar.set(0)
            self.progressbar.pack(padx =20 )


            def  add_xp():
                progress = self.progressbar.get()
                if progress < 0.9:
                    self.progressbar.set(progress + 0.1)
                elif progress >= 0.9:
                    self.progressbar.set(0)
                self.current_xp = progress

            # self.btn = tk.Button(self.frame, text="increment", command=add_xp)
            # self.btn.pack()