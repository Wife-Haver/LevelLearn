# xp_bar.py

import tkinter as tk

class XPBar(tk.Frame):
    def __init__(self, parent, max_xp=100, **kwargs):
        super().__init__(parent, **kwargs)

        self.current_xp = 0
        self.max_xp = max_xp

        # Create canvas for XP bar

        self.canvas = tk.Canvas(self, width=200, height=30, bg="black")
        self.canvas.pack()

        # Create label to show current XP
        self.xp_label = tk.Label(self, text=f"XP: {self.current_xp}/{self.max_xp}",bg="#0486ba")
        self.xp_label.pack()


    def update_xp_bar(self):
        # Clear the previous bar and draw the new one
        self.canvas.delete("xp_bar")
        xp_width = (self.current_xp / self.max_xp) * 200  # Calculate width
        self.canvas.create_rectangle(0, 0, xp_width, 30, fill="green", tags="xp_bar")
        self.xp_label.config(text=f"XP: {self.current_xp}/{self.max_xp}")

    def gain_xp(self, amount=10):
        if self.current_xp < self.max_xp:
            self.current_xp += amount
            if self.current_xp > self.max_xp:  # Prevent overflow
                self.current_xp = self.max_xp
            self.update_xp_bar()

    def set_xp(self, current_xp):
        """ Set XP manually """
        self.current_xp = min(current_xp, self.max_xp)  # Cap at max_xp
        self.update_xp_bar()
