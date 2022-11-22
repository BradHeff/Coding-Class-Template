# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan

import tkinter as tk # tkinter, Python library for OOP programming
import GUI # custom .py containing GUI code

class Base(tk.Tk): # set class argument as tkinter's Tk() function
    """
    The initializer function for the GUI
    initializing self as the window base variable
    """
    def __init__(self):
        '''
        Return a proxy object that delegates method calls to a parent or sibling class of type
        This is useful for accessing inherited methods that have been overridden in a class.
        Python3 introduced an a new hierachy to allow super to be called without empty.
        Example: 
        super().__init__()
        is the same as 
        super(classname, self).__init__()
        '''
        super(Base, self).__init__() # i still like to declare classname and self (makes compatible with python2 if people still use it)
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
    
    '''
    This function is called from the command= variable
    from button statement in GUI.py
    '''
    def btn_clicked(self):
        if(self.switch == 0):
            '''Set the text field of the label (this is made blank on initialization in GUI.py)'''
            self.lbl2['text'] = "You Clicked the Button :D "
            self.switch = 1 # set switch value to 1 (indicates the button has been clicked)
        else:
            '''Set the text field of the label (this is made blank on second click)'''
            self.lbl2['text'] = ""
            self.switch = 0 # set switch value to 0 (indicates a second click, resetting back to default)


'''Startup of the script'''
if __name__ == "__main__":
    app = Base() # initialize the class into a variable
    app.mainloop() # Call the mainloop() function of Tk() (tkinter's show Gui window)
    