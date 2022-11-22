# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan

'''
Importing image base64 code from base64_logo.py
'''
from base64_logo import imageString
from base64_logo import logoString

'''
Set the window variables
'''
def Window(self):
    self.W, self.H = 520, 250 # Set the height and width of the window (variables declared in base.py init def)
    self.title('Horizon Coding Class Template') # Sets the title of the window
    ''''
    Get the screen width and height into variable to calculate window start position
    '''
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()    
    '''
    width of screen devide 2 = center screen
    minus
    width of tkinter window devide 2
    equals
    center of tkinter window is center of screen on X axis
    '''
    center_x = int(screen_width/2 - self.W / 2) # Calculate position X of the window start position (X = left | Right screen position)
    '''
    height of screen devide 2 = center screen
    minus
    height of tkinter window devide 2
    equals
    center of tkinter window is center of screen on Y axis
    '''
    center_y = int(screen_height/2 - self.H / 2) # Calculate position Y of the window start position (Y = top | bottom screen position)    
    self.geometry(f'{self.W}x{self.H}+{center_x}+{center_y}') # set size and position of window start. (width x height + positionX + positionY)    
    self.resizable(0, 0) # prevent window resize / maximize    
    self.attributes("-fullscreen", False) # prevent window fullscreen

'''
Set the icon of the window
'''
def windowIcon(self, tk):
    photo = tk.PhotoImage(data=logoString) # add base64 image string to Tk photoimage data variable
    self.wm_iconphoto(False, photo) # set the window icon with photoimage data variable

'''
Add image to top of window
'''
def header(self, tk):
    global header # declare header variable as global (This will save the image import of photoimage globally)
    header = tk.PhotoImage(data=imageString) # add base64 image sting to Tk photoimage data variable
    tk.Label(self, image = header).pack() # add the photoimage data variable to label and pack to window


'''
The main GUI function called from base.py init function
'''
def GUI_Window(self, tk):
    
    Window(self) # Set the window parameters
    windowIcon(self, tk) # Set the icon for the window
    
    header(self, tk) # Set the header logo inside the window
    
    ''' Set the default padding for the components'''
    padding = {
        'pady':10, 
        'padx':10
    }
    
    '''Create a Label to show at top of the window'''
    lbl1 = tk.Label(self, text="This is a Lable :D ")
    '''
    anchor the label at the top (N = north), make the label component
    fill the width of the available space
    '''
    lbl1.pack(anchor=tk.N, fill=tk.X, **padding) 
    
    '''
    Create a button
    text = the string to display on the button
    command = the function to run when button clicked. (Refer to base.py -> btn_clicked def)
    add default padding reference **padding replaces (padx=10, pady=10)
    '''
    btn1 = tk.Button(self, text="Click Me!", command=self.btn_clicked)    
    btn1.pack(fill=tk.X, **padding)
    
    '''
    Create label to show on button click
    anchor the label to bottom (S = south), make label component
    fill the width of available space
    add default padding reference **padding (padx=10, pady=10)
    '''
    self.lbl2 = tk.Label(self, text="")
    self.lbl2.pack(anchor=tk.S, fill=tk.X, **padding)