from tkinter import Button,Label
from src.pages.Page import Page
from src.TkStyles import buttonStyle, labelStyle, headerStyle
from src.DatabaseConnector import db

class SponsorsPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        query = 'select * from Sponsor'
        db.query(query)
        r = db.store_result()

        Label(self, text='Sponsor Name', **headerStyle).grid(row=1, column='9', sticky='W')
        Label(self, text='Role', **headerStyle).grid(row=1, column='11', sticky='W')
        
        sponsors = list(r.fetch_row(maxrows=0,how=1))
        for i,sponsor in enumerate(sponsors):
            Label(self, text=sponsor['SponsorName'], **labelStyle).grid(row=i+2, column='9', sticky='W')
            Label(self, text=sponsor['Role'], **labelStyle).grid(row=i+2, column='11', sticky='W')
        
        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row=20,column=10)
