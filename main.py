import _mysql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# connect to db
db= _mysql.connect(host="localhost",user="root",passwd="ArkAngel",db="EVENTS")

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, background="white", *args, **kwargs)
    def show(self):
        self.lift()

class SchedulePage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        tk.Frame(master=self, width=1024, height=20, bg="#1769AA").grid(column=0, columnspan=20)

        intro = tk.Frame(master=self, width=1024, height=60, bg="#2196f3")
        intro.grid(column=0, columnspan=20)

        title = tk.Label(self, font=("-*-Courier-*-R0200-*-*-*-*-ISO8859-1", 20), background="#2196f3", foreground="white",text="International Conference on \nAdvances in Computing, Communications and Informatics".upper())
        title.grid(column=1, row=1, columnspan=20)

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

        eventLbl = []
        placeLbl = []
        timeLbl = []
        btns = []
        for i,event in enumerate(events):
            eventLbl.append(tk.Label(self, background="white", text=event['Name'],font=("-*-Times-Bold-R-*--*-200-*-*-*-*-ISO8859-1", 20)))
            eventLbl[i].grid(sticky="W", column=startcol, row=i+10)
            placeLbl.append(tk.Label(self, background="white", text=event['PlaceName'],))
            placeLbl[i].grid(sticky="W", column=(startcol+1), row=i+10)
            timeLbl.append(tk.Label(self, background="white", text=event['StartTime']))
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
        Page.__init__(self, *args, **kwargs)
        talkLbl= []
        eventNamelbl = tk.Label()
        backButton = tk.Button(self, background="white", text="Back", command=lambda: controller.showFrame('SchedulePage') )
        backButton.grid(column=1, row=10)

    def putData(self):
        query = 'select * from Event where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        event = list(r.fetch_row(maxrows=0,how=1))
        self.eventNamelbl = tk.Label(self,font=("Aial", 20),background="white", text=('      '+event[0]['Name'].decode()+'     '))
        self.eventNamelbl.grid(column = 0, row = 1)

        query = 'select * from Speaker NATURAL JOIN Talk where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        talks = list(r.fetch_row(maxrows=0,how=1))

        self.talkLbl = []
        for i,talk in enumerate(talks):
            self.talkLbl.append(tk.Label(self,background="white", text=' '+talk['Title'].decode()+' '))
            self.talkLbl[i].grid(column=10, row=i)
        
class MenuPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        btnConfig = { 
            'background': 'white',
            'height': 2,
            'width': 20,
            'font': ('Arial', 13)
        }

        image = Image.open('logo.png')
        image = image.resize((1024,280), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self,image=photo)
        img.image = photo
        img.pack(pady=(0,40))

        controls = {}
        controls['SchedulePage'] = tk.Button(self,text="See Schedule",**btnConfig)
        controls['LoginPage'] = tk.Button(self, text="Login as Administrator",**btnConfig)
        controls['MapPage'] = tk.Button(self, text="View Map",**btnConfig)
        controls['SponsorsPage'] = tk.Button(self, text="Conference Sponsors",**btnConfig)

        for i,control in enumerate(controls):
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)
    
class MapPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        btnConfig = { 
            'background': 'white',
            'height': 2,
            'width': 20,
            'font': ('Arial', 13)
        }

        image = Image.open('map.png')
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self,image=photo)
        img.image = photo
        img.pack(fill='both')


class SponsorsPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        btnConfig = { 
            'background': 'white',
            'height': 2,
            'width': 20,
            'font': ('Arial', 13)
        }
        query = 'select * from Sponsor'
        db.query(query)
        r = db.store_result()
        sponsors = list(r.fetch_row(maxrows=0,how=1))
        for i,sponsor in enumerate(sponsors):
            tk.Label(self, text=sponsor['SponsorName']).grid(row=i+2, column=2)
            tk.Label(self, text=sponsor['Role']).grid(row=i+2, column=3)
            

class LoginPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        btnConfig = { 
            'background': 'white',
            'height': 2,
            'width': 20,
            'font': ('Arial', 13)
        }

        image = Image.open('logo.png')
        image = image.resize((1024,280), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self,image=photo)
        img.image = photo
        img.pack(pady=(0,40))

        L1 = tk.Label(self,text="User Name")
        L1.pack()
        self.Username = tk.Entry(self,bd =5)
        self.Username.pack()
        L2 = tk.Label(self,text="Password")
        L2.pack()
        self.Password = tk.Entry(self,bd =5)
        self.Password.pack()

        SubmitButton = tk.Button(self,text='Login', **btnConfig, command=self.login)
        SubmitButton.pack()

    def login(self):
        if(self.Username.get()=='Admin' and self.Password.get()=='Pass'):
            self.controller.showFrame('AdminPage')
        else:
            pass
            tk.messagebox.showinfo("Incorrect Login!", "The username and password you entered are incorrect!")
class AdminPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)

        btnConfig = { 
            'background': 'white',
            'height': 2,
            'width': 20,
            'font': ('Arial', 13)
        }

        image = Image.open('logo.png')
        image = image.resize((1024,280), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self,image=photo)
        img.image = photo
        img.pack(pady=(0,40))

        controls = {}
        controls['AddSpeakerPage'] = tk.Button(self,text="Add new speaker",**btnConfig)
        controls['DeleteSpeakerPage'] = tk.Button(self, text="Delete a speaker",**btnConfig)
        controls['AddTalkPage'] = tk.Button(self, text="Add a talk",**btnConfig)
        controls['DeleteTalkPage'] = tk.Button(self, text="Delete a talk",**btnConfig)
        controls['MenuPage'] = tk.Button(self, text="Logout",**btnConfig)

        for i,control in enumerate(controls):
            controls[control].config(command=lambda page=control: self.controller.showFrame(page))
            controls[control].pack(fill='y',pady=5)


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

        buttonframe = tk.Frame(self)
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
