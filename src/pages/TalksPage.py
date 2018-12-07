from tkinter import Frame,Button,Label
from src.pages.Page import Page
from src.TkStyles import buttonStyle,labelStyle,headerStyle
from src.DatabaseConnector import db

class TalksPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        self.cursor = db.cursor(dictionary=True)
        Page.__init__(self, *args, logo='grid',**kwargs)
        self.cleared = True
        Frame(master=self, width=1024, height=30, bg="white").grid(column=0, columnspan=20)

        backButton = Button(self, **buttonStyle, text="Back", command=lambda: controller.showFrame('SchedulePage') )
        backButton.grid(column=9, row=20)

    def clear(self):
        if not self.cleared:
            self.eventNamelbl.destroy()
            self.inchargeName.destroy()
            self.inchargeContact.destroy()
            self.place.destroy()
            for column in [self.talkLbl, self.spkrLbl, self.timeLbl]:
                for row in column:
                    row.destroy()

    def putData(self):
        self.clear()
        self.cleared = False
        query = "select * from Location NATURAL JOIN Event NATURAL JOIN Incharge where EventId = %s"
        self.cursor.execute(query,(self.controller.EventId,))
        event = self.cursor.fetchone()
        self.eventNamelbl = Label(self,font=("Arial", 20), background="white", text=('Session: '+event['Name']+''))
        self.eventNamelbl.grid(column = 4, row = 2, pady=(15,0), columnspan=10)

        self.inchargeName = Label(self,font=('Arial',15), background="white", text=('Incharge: '+event['InchargeName']+'')) 
        self.inchargeName.grid(column=4, row=3, columnspan=10)

        self.inchargeContact = Label(self,font=('Arial',15), background="white", text=('Contact No: '+str(event['ContactNo'])+'')) 
        self.inchargeContact.grid(column=4, row=4, columnspan=10)

        self.place = Label(self,font=('Arial',15), background="white", text=('Venue : '+event['PlaceName']+'')) 
        self.place.grid(column=4, row=5,  pady=(0,20), columnspan=10)

        query = "select * from Speaker NATURAL JOIN Talk where EventId = %s"
        self.cursor.execute(query,(self.controller.EventId,))
        
        self.header = []
        startcol = 8
        self.header.append(Label(self, text="Talk Title", **headerStyle))
        self.header[0].grid(sticky="W", column=startcol, row=6)
        self.header.append(Label(self,text="Speaker", **headerStyle))
        self.header[1].grid(sticky="W", column=(startcol+1), row=6)
        self.header.append(Label(self, text="Time", **headerStyle))
        self.header[2].grid(sticky="W", column=(startcol+2), row=6)

        self.talkLbl = []
        self.spkrLbl = []
        self.timeLbl = []
        for i,talk in enumerate(self.cursor.fetchall()):
            self.talkLbl.append(Label(self, text=' '+talk['Title']+' ', **labelStyle))
            self.talkLbl[i].grid(column=startcol, row=i+8,
             sticky='W')
            self.spkrLbl.append(Label(self, text=' '+talk['SpeakerName']+' ', **labelStyle))
            self.spkrLbl[i].grid(column=startcol+1, row=i+8, sticky='W')
            self.timeLbl.append(Label(self, text=' '+talk['StartTime'].ctime()+' ', **labelStyle))
            self.timeLbl[i].grid(column=startcol+2, row=i+8, sticky='W')
