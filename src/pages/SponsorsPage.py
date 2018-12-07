from tkinter import Button,Label
from src.pages.Page import Page
from src.TkStyles import buttonStyle, labelStyle, headerStyle
from src.DatabaseConnector import db

class SponsorsPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        self.cursor = db.cursor(dictionary=True)
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        query = 'select * from Sponsor'
        self.cursor.execute(query)
        
        Label(self, text='Sponsor Name', **headerStyle).grid(row=1, column='9', sticky='W')
        Label(self, text='Role', **headerStyle).grid(row=1, column='11', sticky='W')
        
        for i,sponsor in enumerate(self.cursor.fetchall()):
            Label(self, text=sponsor['SponsorName'], **labelStyle).grid(row=i+2, column='9', sticky='W')
            Label(self, text=sponsor['Role'], **labelStyle).grid(row=i+2, column='11', sticky='W')
        
        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row=20,column=10)
