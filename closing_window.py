from tkinter import ttk
import tkinter as tk
import sys
from PIL import Image, ImageTk
from settings import Settings
from reset import GameStatics
# type: ignore

class ExitWindow:
    def __init__(self, score):
        self.score = score
        self.root = tk.Tk()
        self.root.title("Exit")
        self.root.attributes('-fullscreen', True)
        self.setting = Settings()
       
        

        self.root.configure(bg='#FF0678')
        # Create frame for widgets
        self.frame = tk.Frame(self.root, bg="yellow", padx=40, pady=40)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label = tk.Label(self.frame, text="Wanna play again?", bg="blue", fg="white", 
                               font=('Comic Sans MS', 24, "bold"), pady=10)
        self.label.pack()
        
        # Progress bar for loading effect
        self.eloadings = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
        
        # Buttons Frame
        self.button_frame = tk.Frame(self.frame, bg="lightgreen")
        self.button_frame.pack(pady=20)

        self.button = tk.Button(self.button_frame, text="PLAY AGAIN", command=self.loading, height=2, width=20, 
                                font=('Comic Sans MS', 18, "bold"), bg="green", fg="white")
        self.button.grid(row=0, column=0, padx=10, pady=10)

        self.extbutton = tk.Button(self.button_frame, text="Exit", command=self.exit, height=2, width=20, 
                                   font=('Comic Sans MS', 18, "bold"), bg="red", fg="white")
        self.extbutton.grid(row=0, column=1, padx=10, pady=10)
        
        self.label1 = tk.Label(self.frame, text=f"YOUR SCORE\n{self.score}", font=('Comic Sans MS', 20, "bold"), 
                                bg="blue", fg="white", pady=10)
        self.label1.pack()

        self.root.mainloop()

    def loading(self):
        self.label.configure(text="Loading...")
        self.eloadings.pack(pady=20)
        self.root.after(100, self.playagain)

    def playagain(self):
        if self.eloadings['value'] < 100:
            self.eloadings['value'] += 10
            self.root.after(100, self.playagain)
        else:
            self.root.destroy()
            self.play_game()

    def play_game(self):
        from AlienInvasion import Mainwindow
        mj=Mainwindow()


        

    
    def exit(self):
        sys.exit()





