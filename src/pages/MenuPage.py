from tkinter import Button
from src.pages.Page import Page
from src.TkStyles import buttonStyle

class MenuPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self,logo='pack', *args, **kwargs)

        controls = {}
        controls['SchedulePage'] = Button(self,text="See Schedule",**buttonStyle)
        controls['MapPage'] = Button(self, text="View Map",**buttonStyle)
        controls['SponsorsPage'] = Button(self, text="Conference Sponsors",**buttonStyle)
        controls['LoginPage'] = Button(self, text="Login as Administrator",**buttonStyle)

        for control in controls:
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)