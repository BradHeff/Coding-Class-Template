# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan

import tkinter as tk
import GUI

class Base(tk.Tk):
    """The initializer function for the GUI"""
    def __init__(self):
        super(Base, self).__init__()
        self.W = 0
        self.H = 0
        
        GUI.GUI_Window(self)

    
if __name__ == "__main__":
    app = Base()
    app.mainloop()
    