import tkinter as tk
import customtkinter as ctk

from notes import Notes  # Importing the Notes class from the notes module
from tasks import Tasks
from xp_bar import XPBar
class MainApp:
    def __init__(self, root):
        self.frames = None
        self.right_frame = None
        self.top_frame = None
        self.left_frame = None
        self.root = root
        self.root.title("LevelLearn")
        self.root.geometry("1000x600")
        self.root.configure(bg='#333333')
        
        # Create frames and UI layout
        self.create_left_frame()
        self.create_top_frame()
        self.create_right_frame()

        # Initialize default frame (Home)
        self.show_frame(self.frames['Tasks'])

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bg='#0486ba')
        self.left_frame.pack(side='left', fill='y')

        program_label = tk.Label(master=self.left_frame, text="LevelLearn", font=("Arial", 25), bg='#0486ba', fg='white')
        program_label.pack(pady=10)

        # Create buttons using a loop to reduce redundancy
        buttons = [
            ("Home", self.show_home_frame),
            ("Notes", self.show_notes_frame),
            ("Tasks", self.show_tasks_frame),
            ("Games", self.show_games_frame)
        ]
        for text, command in buttons:
            tk.Button(self.left_frame, text=text, font=("Arial", 15), bd=0, bg="#79ADDC", fg="white", width=7,
                      activebackground="#7990dc", activeforeground="white", command=command).pack(pady=10)

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.root,height=80,bg="#0486ba")
        self.top_frame.pack_propagate(False)

        level_label = tk.Label(self.top_frame,text="Lvl:1",bg="#0486ba")

        exp_bar = XPBar(self.top_frame)


        exp_bar.pack(side="right")
        level_label.pack(side= "right")
        self.top_frame.pack(side='top', fill="x")





    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bg='white')
        self.right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=20)

        self.frames = {'Home': self.create_home_frame(),
                       'Notes': Notes(self.right_frame).get_frame(),
                       'Tasks': Tasks(self.right_frame).get_frame(),
                       'Games': self.create_games_frame()
                       }


        # Place all frames on the right_frame (stacked on top of each other)
        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)

    def create_home_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        home_label = tk.Label(frame, text="Home Page", font=("Arial", 20), bg='white', fg='#333333')
        home_label.grid(row=0,column=0)

        frame1=ctk.CTkFrame(frame,width=200,height=200,corner_radius=4,border_width=3,bg_color="#f0f0f0")
        frame2=ctk.CTkFrame(frame,width=200,height=200,corner_radius=4,border_width=3,bg_color="#f0f0f0")
        frame3 = ctk.CTkFrame(frame, width=300, height=150, corner_radius=4, border_width=3, bg_color="#f0f0f0")
        frame4 = ctk.CTkFrame(frame, width=200, height=200, corner_radius=4, border_width=3, bg_color="#f0f0f0")

        # frame2.grid(row=1, column=3)
        # frame3.grid(row=2, column=0)
        # frame1.grid(row=1,column=1)
        # frame4.grid(row=2, column=2)




        return frame


    def create_games_frame(self):
        frame = tk.Frame(self.right_frame, bg='white')
        games_label = tk.Label(frame, text="Games Page", font=("Arial", 20), bg='white', fg='#333333')
        games_label.pack(pady=20)
        return frame

    @staticmethod
    def show_frame(frame):
        frame.tkraise()

    def show_home_frame(self):
        self.show_frame(self.frames['Home'])

    def show_notes_frame(self):
        self.show_frame(self.frames['Notes'])

    def show_tasks_frame(self):
        self.show_frame(self.frames['Tasks'])

    def show_games_frame(self):
        self.show_frame(self.frames['Games'])

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
