from tkinter import Button,Label
from PIL import ImageTk, Image
from src.pages.Page import Page
from src.TkStyles import buttonStyle

class MapPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        image = Image.open('src/assets/map.png')
        photo = ImageTk.PhotoImage(image)
        img = Label(self, bg='white', image=photo)
        img.image = photo
        img.pack(fill='both',expand=1)

        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.pack()
