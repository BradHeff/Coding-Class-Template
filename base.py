# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan

import tkinter as tk
import GUI

class Base(tk.Tk):
    """The initializer function for the GUI"""
    def __init__(self):
        super(Base, self).__init__()
        """ 
        This is a place holder to set the height and width of app in the GUI.py
        """
        self.W = 0
        self.H = 0
        
        """ 
        This is a switch toggle from 0 -> 1
        On Button click if switch = 0 we make switch = 1 and back again.        
        """
        
        self.switch = 0
        
        GUI.GUI_Window(self, tk)
    
    def btn_clicked(self):
        if(self.switch == 0):
            self.lbl2['text'] = "You Clicked the Button :D "
            self.switch = 1
        else:
            self.lbl2['text'] = ""
            self.switch = 0


if __name__ == "__main__":
    app = Base()
    app.mainloop()
    