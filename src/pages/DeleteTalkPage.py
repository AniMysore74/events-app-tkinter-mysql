from tkinter import Button, Label, messagebox, StringVar, OptionMenu
from src.pages.Page import Page
from src.TkStyles import buttonStyle, labelStyle, optionsStyle
from src.DatabaseConnector import db

class DeleteTalkPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        eventLabel = Label(self,text="Choose the event", **labelStyle)
        eventLabel.grid(row = 3, column = 8)
        
        self.eventsList = [  
            'Computer Vision and the Internet (VisionNet-18)', 
            'Natural Language Processing (NLP-18)' , 
            'Artificial Intelligence',  
            'Machine Learning/Data Engineering'
        ]

        eventVar = StringVar(self)
        eventVar.set(self.eventsList[0])
        
        eventOptions = OptionMenu(self, eventVar, *self.eventsList, command=self.updateChoice)
        eventOptions.grid(row = 3, column = 10)
        eventOptions.config(**optionsStyle)

        talkLabel = Label(self,text="Pick Talk", **labelStyle)
        talkLabel.grid(row = 4, column = 8)

        self.talksList = ['']

        self.talksVar = StringVar(self)
        self.talksVar.set(self.talksList[0])
        
        self.talksOptions = OptionMenu(self, self.talksVar, *self.talksList)
        self.talksOptions.grid(row = 4, column = 10)
        self.talksOptions.config(**optionsStyle)
        
        SubmitButton = Button(self,text='Delete selected talk', **buttonStyle, command=self.deleteTalk)
        SubmitButton.grid(row = 7, column = 8)
        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('AdminPage'))
        backButton.grid(row = 7, column = 10)

    def updateChoice(self,event):
        query = 'select title from Talk T, Event E where E.EventId = T.EventId and Name = "' + event + '"'
        db.query(query)
        r = db.store_result()
        self.talksList = []
        for row in list(r.fetch_row(maxrows=0,how=0)):
            self.talksList.append(row[0].decode('utf'))

        self.talksVar.set(self.talksList[0])
        self.talksOptions['menu'].delete(0,"end")
        for talky in self.talksList:
            self.talksOptions['menu'].add_command(label=talky, 
                             command=lambda value=talky: self.talksVar.set(value))


    def deleteTalk(self):
        query = 'delete from Talk where title= "'+self.talksVar.get()+'";'
        db.query(query)
        messagebox.showinfo(title='Deleted!',message='Deleted talk titled '+self.talksVar.get())
        self.controller.showFrame('AdminPage')
