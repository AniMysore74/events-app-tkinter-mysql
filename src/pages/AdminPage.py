from tkinter import Button
from src.pages.Page import Page
from src.TkStyles import buttonStyle

class AdminPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='pack', **kwargs)

        controls = {}
        controls['AddTalkPage'] = Button(self, text="Add a talk",**buttonStyle)
        controls['DeleteTalkPage'] = Button(self, text="Delete a talk",**buttonStyle)
        controls['MenuPage'] = Button(self, text="Logout",**buttonStyle)

        for control in controls:
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)
