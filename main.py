import _mysql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# connect to db
db= _mysql.connect(host="localhost",user="root",passwd="ArkAngel",db="EVENTS")


btnConfig = { 
    'background': 'white',
    'height': 2,
    'width': 20,
    'font': ('Arial', 13)
}

lblConfig = { 
    'bg' : 'white',
    'font': ('Helvetica', 15),
    'pady': 15
}

headerLbl = {
    'bg' : 'white',
    'font': ('Helvetica', 20, 'bold underline'),
    'pady': 20,
    'bd': 1,
}

entryCfg = {
    'font': ('Helvetica', 15),
} 

optionsConfig = {
    'background': 'white',
    'font': ('Helvetica', 15),
}
# Superclass that all other pages derive from
class Page(tk.Frame):
    def __init__(self,  *args, **kwargs):
        tk.Frame.__init__(self, background="white", *args)
        
        # add ICACCI logo to top of page if (logo='pack') or (logo='grid')  is passed in constructor
        # use pack or grid accordingly
        if 'logo' in kwargs:
            image = Image.open('logo.png')
            image = image.resize((1024,280), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            img = tk.Label(self,image=photo)
            img.image = photo
            if kwargs['logo'] == 'pack':
                img.pack(pady=(0,40))
            if kwargs['logo'] == 'grid':
                img.grid(row=0,column=0,columnspan=20)
            
    def show(self):
        self.lift()

class SchedulePage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)

        tk.Frame(master=self, width=1024, height=30, bg="white").grid(column=0, columnspan=20)

        query = 'select * from Event NATURAL JOIN Location'
        db.query(query)
        r = db.store_result()
        events = list(r.fetch_row(maxrows=0,how=1))

        header = []
        startcol = 9
        header.append(tk.Label(self, background="white", text="Seminar Name",font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[0].grid(sticky="W", column=startcol, row=9)
        header.append(tk.Label(self, background="white", text="Location", font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[1].grid(sticky="W", column=(startcol+1), row=9)
        header.append(tk.Label(self, background="white", text="Time", font=("-*-Times-Bold-R-*--*-250-*-*-*-*-ISO8859-1", 20)))
        header[2].grid(sticky="W", column=(startcol+2), row=9)

        backButton = tk.Button(self, text="Back", **btnConfig, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row=20,column=10)
        eventLbl = []
        placeLbl = []
        timeLbl = []
        btns = []
        for i,event in enumerate(events):
            eventLbl.append(tk.Label(self, text=event['Name'], **lblConfig))
            eventLbl[i].grid(sticky="W", column=startcol, row=i+10)
            placeLbl.append(tk.Label(self, text=event['PlaceName'],**lblConfig))
            placeLbl[i].grid(sticky="W", column=(startcol+1), row=i+10)
            timeLbl.append(tk.Label(self, text=event['StartTime'], **lblConfig))
            timeLbl[i].grid(sticky="W", column=(startcol+2), row=i+10)
            e = event['EventId']
            btns.append(tk.Button(self, background="white", text="Info", command=lambda e=e: self.go_to_page(e) ))
            btns[i].grid(column=(startcol+3), row=i+10)
        

    def go_to_page(self, EventId): 
        self.controller.EventId = EventId
        self.controller.frames['TalksPage'].putData()
        self.controller.showFrame('TalksPage')

class TalksPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid',**kwargs)
        self.cleared = True
        tk.Frame(master=self, width=1024, height=30, bg="white").grid(column=0, columnspan=20)

        backButton = tk.Button(self, **btnConfig, text="Back", command=lambda: controller.showFrame('SchedulePage') )
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
        query = 'select * from Location NATURAL JOIN Event NATURAL JOIN Incharge where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        event = list(r.fetch_row(maxrows=0,how=1))
        self.eventNamelbl = tk.Label(self,font=("Arial", 20), background="white", text=('Session: '+event[0]['Name'].decode()+''))
        self.eventNamelbl.grid(column = 4, row = 2, pady=(15,0), columnspan=10)

        self.inchargeName = tk.Label(self,font=('Arial',15), background="white", text=('Incharge: '+event[0]['InchargeName'].decode()+'')) 
        self.inchargeName.grid(column=4, row=3, columnspan=10)

        self.inchargeContact = tk.Label(self,font=('Arial',15), background="white", text=('Contact No: '+event[0]['ContactNo']+'')) 
        self.inchargeContact.grid(column=4, row=4, columnspan=10)

        self.place = tk.Label(self,font=('Arial',15), background="white", text=('Venue : '+event[0]['PlaceName'].decode()+'')) 
        self.place.grid(column=4, row=5,  pady=(0,20), columnspan=10)

        query = 'select * from Speaker NATURAL JOIN Talk where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        talks = list(r.fetch_row(maxrows=0,how=1))

        self.header = []
        startcol = 8
        self.header.append(tk.Label(self, text="Talk Title", **headerLbl))
        self.header[0].grid(sticky="W", column=startcol, row=6)
        self.header.append(tk.Label(self,text="Speaker", **headerLbl))
        self.header[1].grid(sticky="W", column=(startcol+1), row=6)
        self.header.append(tk.Label(self, text="Time", **headerLbl))
        self.header[2].grid(sticky="W", column=(startcol+2), row=6)

        self.talkLbl = []
        self.spkrLbl = []
        self.timeLbl = []
        for i,talk in enumerate(talks):
            self.talkLbl.append(tk.Label(self, text=' '+talk['Title'].decode()+' ', **lblConfig))
            self.talkLbl[i].grid(column=startcol, row=i+8,
             sticky='W')
            self.spkrLbl.append(tk.Label(self, text=' '+talk['SpeakerName'].decode()+' ', **lblConfig))
            self.spkrLbl[i].grid(column=startcol+1, row=i+8, sticky='W')
            self.timeLbl.append(tk.Label(self, text=' '+talk['StartTime']+' ', **lblConfig))
            self.timeLbl[i].grid(column=startcol+2, row=i+8, sticky='W')

class MenuPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self,logo='pack', *args, **kwargs)

        controls = {}
        controls['SchedulePage'] = tk.Button(self,text="See Schedule",**btnConfig)
        controls['MapPage'] = tk.Button(self, text="View Map",**btnConfig)
        controls['SponsorsPage'] = tk.Button(self, text="Conference Sponsors",**btnConfig)
        controls['LoginPage'] = tk.Button(self, text="Login as Administrator",**btnConfig)

        for i,control in enumerate(controls):
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)
    
class MapPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        image = Image.open('map.png')
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self, bg='white', image=photo)
        img.image = photo
        img.pack(fill='both',expand=1)

        backButton = tk.Button(self, text="Back", **btnConfig, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.pack()

class SponsorsPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        query = 'select * from Sponsor'
        db.query(query)
        r = db.store_result()

        tk.Label(self, text='Sponsor Name', **headerLbl).grid(row=1, column='9', sticky='W')
        tk.Label(self, text='Role', **headerLbl).grid(row=1, column='11', sticky='W')
        
        sponsors = list(r.fetch_row(maxrows=0,how=1))
        for i,sponsor in enumerate(sponsors):
            tk.Label(self, text=sponsor['SponsorName'], **lblConfig).grid(row=i+2, column='9', sticky='W')
            tk.Label(self, text=sponsor['Role'], **lblConfig).grid(row=i+2, column='11', sticky='W')
        
        backButton = tk.Button(self, text="Back", **btnConfig, command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row=20,column=10)

class LoginPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)

        L1 = tk.Label(self,text="User Name", **lblConfig)
        L1.grid(row = 3, column = 8)
        self.Username = tk.Entry(self, **entryCfg)
        self.Username.grid(row = 3, column = 10)
        L2 = tk.Label(self,text="Password", **lblConfig)
        L2.grid(row = 4, column = 8)
        self.Password = tk.Entry(self, **entryCfg, show="*")
        self.Password.grid(row = 4, column = 10)

        SubmitButton = tk.Button(self,text='Login', **btnConfig, command=self.login)
        SubmitButton.grid(row = 5, column = 8)
        backButton = tk.Button(self, text="Back", **btnConfig ,command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row = 5, column = 10)


    def login(self):
        if(self.Username.get()=='Admin' and self.Password.get()=='Pass'):
            self.controller.showFrame('AdminPage')
        else:
            pass
            tk.messagebox.showinfo("Incorrect Login!", "The username and password you entered are incorrect!")
class AdminPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='pack', **kwargs)

        controls = {}
        controls['AddTalkPage'] = tk.Button(self, text="Add a talk",**btnConfig)
        controls['DeleteTalkPage'] = tk.Button(self, text="Delete a talk",**btnConfig)
        controls['MenuPage'] = tk.Button(self, text="Logout",**btnConfig)

        for i,control in enumerate(controls):
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)

class AddTalkPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        titleLabel = tk.Label(self,text="Talk Title", **lblConfig)
        titleLabel.grid(row = 3, column = 8)
        self.title = tk.Entry(self, **entryCfg)
        self.title.grid(row = 3, column = 10)
        timeLabel = tk.Label(self,text="Start Time", **lblConfig)
        timeLabel.grid(row = 4, column = 8)
        self.time = tk.Entry(self, **entryCfg)
        self.time.grid(row = 4, column = 10)
        spkrLabel = tk.Label(self,text="Speaker Name", **lblConfig)
        spkrLabel.grid(row = 5, column = 8)
        self.spkr = tk.Entry(self, **entryCfg)
        self.spkr.grid(row = 5, column = 10)
        
        options = [  
            'Computer Vision and the Internet (VisionNet-18)', 
            'Natural Language Processing (NLP-18)' , 
            'Artificial Intelligence',  
            'Machine Learning/Data Engineering'
        ]

        optionLabel = tk.Label(self,text="Select Event", **lblConfig)
        optionLabel.grid(row = 6, column = 8)

        self.var = tk.StringVar(self)
        self.var.set(options[0])
        
        option = tk.OptionMenu(self, self.var, *options)
        option.grid(row = 6, column = 10)
        option.config(**optionsConfig)

        SubmitButton = tk.Button(self,text='Add Talks', **btnConfig, command=self.addTalk)
        SubmitButton.grid(row = 7, column = 8)
        backButton = tk.Button(self, text="Back", **btnConfig, command = lambda :self.controller.showFrame('AdminPage'))
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

        tk.messagebox.showinfo(title="Talk added!", message="Added "+self.title.get()+" to database.")

class DeleteTalkPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)
        
        eventLabel = tk.Label(self,text="Choose the event", **lblConfig)
        eventLabel.grid(row = 3, column = 8)
        
        self.eventsList = [  
            'Computer Vision and the Internet (VisionNet-18)', 
            'Natural Language Processing (NLP-18)' , 
            'Artificial Intelligence',  
            'Machine Learning/Data Engineering'
        ]

        eventVar = tk.StringVar(self)
        eventVar.set(self.eventsList[0])
        
        eventOptions = tk.OptionMenu(self, eventVar, *self.eventsList, command=self.updateChoice)
        eventOptions.grid(row = 3, column = 10)
        eventOptions.config(**optionsConfig)

        talkLabel = tk.Label(self,text="Pick Talk", **lblConfig)
        talkLabel.grid(row = 4, column = 8)

        self.talksList = ['']

        self.talksVar = tk.StringVar(self)
        self.talksVar.set(self.talksList[0])
        
        self.talksOptions = tk.OptionMenu(self, self.talksVar, *self.talksList)
        self.talksOptions.grid(row = 4, column = 10)
        self.talksOptions.config(**optionsConfig)
        
        SubmitButton = tk.Button(self,text='Delete selected talk', **btnConfig, command=self.deleteTalk)
        SubmitButton.grid(row = 7, column = 8)
        backButton = tk.Button(self, text="Back", **btnConfig, command = lambda :self.controller.showFrame('AdminPage'))
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
        tk.messagebox.showinfo(title='Deleted!',message='Deleted talk titled '+self.talksVar.get())
        self.controller.showFrame('AdminPage')

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.data = {}
        tk.Frame.__init__(self, *args, **kwargs)
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

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        for frame in self.frames:
            self.frames[frame].place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.frames['MenuPage'].show()

    def showFrame(self, c):
        self.frames[c].tkraise()

if __name__ == "__main__":
    
    root = tk.Tk()
    style = ttk.Style(root)

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1024x720")
    root.title('ICACCI Information App')
    root.mainloop()
