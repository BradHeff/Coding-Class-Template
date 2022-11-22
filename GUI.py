# This is a template to be used for the students of 
# Horizon to practice / modify for learning purposes
# Copyright (C) 2022  Brad Heffernan


def Window(self):
    self.W, self.H = 450, 450
    self.title('Horizon Coding Class Template')
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    center_x = int(screen_width/2 - self.W / 2)
    center_y = int(screen_height/2 - self.H / 2)
    self.geometry(f'{self.W}x{self.H}+{center_x}+{center_y}')
    self.resizable(0, 0)
    self.attributes("-fullscreen", False)
    
def GUI_Window(self, tk):
    Window(self)
    
    padding = {
        'pady':10, 
        'padx':10
    }
    
    lbl1 = tk.Label(self, text="This is a Lable :D ")
    lbl1.pack(anchor=tk.N, fill=tk.X, **padding)
    
    btn1 = tk.Button(self, text="Click Me!", command=self.btn_clicked)
    
    btn1.pack(fill=tk.X, **padding)
    
    self.lbl2 = tk.Label(self, text="")
    self.lbl2.pack(anchor=tk.S, fill=tk.X, **padding)