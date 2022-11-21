# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan


def Window(self):
    self.W, self.H = 850, 450
    self.title('Horizon Coding Class Template')
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    center_x = int(screen_width/2 - self.W / 2)
    center_y = int(screen_height/2 - self.H / 2)
    self.geometry(f'{self.W}x{self.H}+{center_x}+{center_y}')
    self.resizable(0, 0)
    self.attributes("-fullscreen", False)
    
def GUI_Window(self):
    Window(self)