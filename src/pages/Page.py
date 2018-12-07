import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# Superclass that all other pages derive from
class Page(tk.Frame):
    def __init__(self,  *args, **kwargs):
        tk.Frame.__init__(self, background="white", *args)
        
        # add ICACCI logo to top of page if (logo='pack') or (logo='grid')  is passed in constructor
        # use pack or grid accordingly
        if 'logo' in kwargs:
            image = Image.open('src/assets/logo.png')
            image = image.resize((1024,280), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            img = tk.Label(self,image=photo)
            img.image = photo
            if kwargs['logo'] == 'pack':
                img.pack(pady=(0,40))
            if kwargs['logo'] == 'grid':
                img.grid(row=0,column=0,columnspan=20)
            
    def show(self):
        self.lift()
