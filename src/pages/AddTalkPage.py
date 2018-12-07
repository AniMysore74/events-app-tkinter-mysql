from tkinter import Button,Label,Entry,messagebox, StringVar, OptionMenu
from src.pages.Page import Page
from src.TkStyles import buttonStyle, labelStyle, entryStyle, optionsStyle
from src.DatabaseConnector import db

class AddTalkPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        titleLabel = Label(self,text="Talk Title", **labelStyle)
        titleLabel.grid(row = 3, column = 8)
        self.title = Entry(self, **entryStyle)
        self.title.grid(row = 3, column = 10)
        timeLabel = Label(self,text="Start Time", **labelStyle)
        timeLabel.grid(row = 4, column = 8)
        self.time = Entry(self, **entryStyle)
        self.time.grid(row = 4, column = 10)
        spkrLabel = Label(self,text="Speaker Name", **labelStyle)
        spkrLabel.grid(row = 5, column = 8)
        self.spkr = Entry(self, **entryStyle)
        self.spkr.grid(row = 5, column = 10)
        
        options = [  
            'Computer Vision and the Internet (VisionNet-18)', 
            'Natural Language Processing (NLP-18)' , 
            'Artificial Intelligence',  
            'Machine Learning/Data Engineering'
        ]

        optionLabel = Label(self,text="Select Event", **labelStyle)
        optionLabel.grid(row = 6, column = 8)

        self.var = StringVar(self)
        self.var.set(options[0])
        
        option = OptionMenu(self, self.var, *options)
        option.grid(row = 6, column = 10)
        option.config(**optionsStyle)

        SubmitButton = Button(self,text='Add Talks', **buttonStyle, command=self.addTalk)
        SubmitButton.grid(row = 7, column = 8)
        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('AdminPage'))
        backButton.grid(row = 7, column = 10)

    def addTalk(self):
        query = 'insert into Speaker(SpeakerName) values("'+self.spkr.get()+'");'
        db.query(query)
        query = 'select SpeakerId from Speaker where SpeakerName="'+self.spkr.get()+'";'
        db.query(query)
        r = db.store_result()
        spkrid = int(r.fetch_row(how=1)[0]['SpeakerId'])
        
        query = 'select EventId from Event where Name="'+self.var.get()+'"'
        db.query(query)
        self.event = int(db.store_result().fetch_row(how=1)[0]['EventId'])
        query = 'insert into Talk(Title,StartTime,SpeakerId,EventId) values('
        query += '"'+self.title.get()+'",'
        query += '"'+self.time.get()+'",'
        query += str(spkrid)+','
        query += str(self.event)
        query += ');'
        db.query(query)

        messagebox.showinfo(title="Talk added!", message="Added "+self.title.get()+" to database.")