from tkinter import Frame

from src.pages.MenuPage import MenuPage
from src.pages.SchedulePage import SchedulePage
from src.pages.TalksPage import TalksPage
from src.pages.MapPage import MapPage
from src.pages.SponsorsPage import SponsorsPage
from src.pages.LoginPage import LoginPage
from src.pages.AdminPage import AdminPage
from src.pages.AddTalkPage import AddTalkPage
from src.pages.DeleteTalkPage import DeleteTalkPage

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        self.data = {}
        Frame.__init__(self, *args, **kwargs)
        self.frames = {}
        self.frames['MenuPage'] = MenuPage(self)
        self.frames['SchedulePage'] = SchedulePage(self)
        self.frames['TalksPage'] = TalksPage(self)
        self.frames['MapPage'] = MapPage(self)
        self.frames['SponsorsPage'] = SponsorsPage(self)
        self.frames['LoginPage'] = LoginPage(self)
        self.frames['AdminPage'] = AdminPage(self)
        self.frames['AddTalkPage'] = AddTalkPage(self)
        self.frames['DeleteTalkPage'] = DeleteTalkPage(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        for frame in self.frames:
            self.frames[frame].place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.frames['MenuPage'].show()

    def showFrame(self, c):
        self.frames[c].tkraise()
