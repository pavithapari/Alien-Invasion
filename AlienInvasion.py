import tkinter as tk
from tkinter import ttk
import sys
from PIL import Image, ImageTk
import my_first
import pygame
import closing_window
from settings import Settings

class Mainwindow:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alien Invasion")
        self.root.attributes('-fullscreen', True)
        
        self.setting = Settings()
        
        # Load images
        self.bg_image = Image.open("D:/myProjects/alienInvasion/assests/BG IMAGE.jpg")
        self.bg_image = self.bg_image.resize((self.setting.screen_width, self.setting.screen_height)) 
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.logo_image = Image.open("D:/myProjects/alienInvasion/assests/THE LOGO.png")
        self.photo = ImageTk.PhotoImage(self.logo_image)
        
        # Background
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Logo
        self.img_label = tk.Label(self.root, image=self.photo, bg="lightgreen")
        self.img_label.pack(pady=5)
         
        # Play Button
        self.play_button = tk.Button(self.root, text="PLAY", command=self.start_game,
                                     height=3, width=10, font=('Comic Sans MS', 24, "bold"), bg="blue")
        self.play_button.pack(pady=10)

        # Progress Bar
        self.loadings = ttk.Progressbar(self.root, orient="horizontal", length=300, mode='determinate')

        # Level Buttons
        self.level_frame = tk.Frame(self.root, bg="lightgreen")
        self.level_frame.pack(pady=10)

        self.level_buttons = []
        for i in range(1, 4):
            button = tk.Button(self.level_frame, text=f"LEVEL {i}",
                               command=lambda num=i: self.selected_level(num),
                               height=2, width=15, font=('Ariel', 20, "bold"), bg="blue")
            button.pack(side=tk.LEFT, padx=10)
            self.level_buttons.append(button)
        
        # Exit Button
        self.exit_button = tk.Button(self.root, text="EXIT", command=self.exit, height=3, width=10, font=('Comic Sans MS', 24, "bold"), bg="blue")
        self.exit_button.pack(pady=10)
        
        self.root.mainloop()

    def selected_level(self, num):
        """Handles Level Selection"""
        for i, button in enumerate(self.level_buttons, 1):
            if i == num:
                button.config(state=tk.DISABLED, bg="red")  # Disable selected level
            else:
                button.config(state=tk.NORMAL, bg="blue")  # Enable others

        if num == 1:
            self.setting.levOne()
        elif num == 2:
            self.setting.levTwo()
        elif num == 3:
            self.setting.levThree()

    def start_game(self):
        """Handles loading animation before starting the game."""
        self.play_button.pack_forget()
        self.loadings.pack(pady=20)
        self.root.after(100, self.loading_animation)

    def loading_animation(self):
        """Handles loading animation before starting the game."""
        if self.loadings['value'] < 100:
            self.loadings['value'] += 10
            self.root.after(100, self.loading_animation)
        else:
            self.loadings.pack_forget()
            self.run_game()

    def run_game(self):
        """Handles game startup properly."""
        self.game = my_first.AlienInvasion(self.setting)  # Start the game
        pygame.quit()  # Quit pygame to free up resource
        self.root.destroy()  # Destroy the main menu window before exit window appears
        self.end = closing_window.ExitWindow(self.game.re.score)


    def exit(self):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    mj = Mainwindow()
