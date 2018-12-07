from tkinter import Frame,Button,Label
from src.pages.Page import Page
from src.TkStyles import buttonStyle,labelStyle
from src.DatabaseConnector import db

class SchedulePage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        self.cursor = db.cursor(dictionary=True)
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        Frame(master=self, width=1024, height=30, bg="white").grid(column=0, columnspan=20)
        
        header = []
        startcol = 9
        header.append(Label(self, background="white", text="Seminar Name",font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[0].grid(sticky="W", column=startcol, row=9)
        header.append(Label(self, background="white", text="Location", font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[1].grid(sticky="W", column=(startcol+1), row=9)
        header.append(Label(self, background="white", text="Time", font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[2].grid(sticky="W", column=(startcol+2), row=9)

        backButton = Button(self, text="Back", **buttonStyle, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row=20,column=10)
        eventLbl = []
        placeLbl = []
        timeLbl = []
        btns = []

        query = 'select * from Event NATURAL JOIN Location'
        self.cursor.execute(query)
        
        for i,event in enumerate(self.cursor.fetchall()):
            eventLbl.append(Label(self, text=event['Name'], **labelStyle))
            eventLbl[i].grid(sticky="W", column=startcol, row=i+10)
            placeLbl.append(Label(self, text=event['PlaceName'],**labelStyle))
            placeLbl[i].grid(sticky="W", column=(startcol+1), row=i+10)
            timeLbl.append(Label(self, text=event['StartTime'].ctime(), **labelStyle))
            timeLbl[i].grid(sticky="W", column=(startcol+2), row=i+10)
            e = event['EventId']
            btns.append(Button(self, background="white", text="Info", command=lambda p=e: self.go_to_page(p) ))
            btns[i].grid(column=(startcol+3), row=i+10)        

    def go_to_page(self, EventId): 
        self.controller.EventId = EventId
        self.controller.frames['TalksPage'].putData()
        self.controller.showFrame('TalksPage')
