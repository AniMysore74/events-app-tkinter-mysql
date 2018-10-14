import _mysql
import tkinter as tk
from PIL import ImageTk, Image

# connect to db
db= _mysql.connect(host="localhost",user="root",passwd="ArkAngel",db="EVENTS")


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, background="white", *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        #label.pack(side="top", fill="both", expand=True)

        query = 'select * from Event NATURAL JOIN Location'
        db.query(query)
        r = db.store_result()
        events = list(r.fetch_row(maxrows=0,how=1))

        eventLbl = []
        placeLbl = []
        btns = []
        for i,event in enumerate(events):
            eventLbl.append(tk.Label(self, background="white", text=event['Name'],font=("Helvetica", 16)))
            eventLbl[i].grid(column=10, row=i)
            placeLbl.append(tk.Label(self, background="white", text=event['PlaceName']))
            placeLbl[i].grid(column=11, row=i)
            e = event['EventId']
            btns.append(tk.Button(self, background="white", text="Info", command=lambda e=e: self.go_to_page(e) ))
            btns[i].grid(column=12, row=i)

        image = Image.open('map.png')
        photo = ImageTk.PhotoImage(image)
        img = tk.Label(self,image=photo)
        img.image = photo
        img.grid(column=1,row=20, columnspan = 20)

    def go_to_page(self, EventId): 
        self.controller.EventId = EventId
        self.controller.frames[1].putData()
        self.controller.showFrame(1)

class Page2(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, **kwargs)
        talkLbl= []
        eventNamelbl = tk.Label()
        backButton = tk.Button(self, background="white", text="Back", command=lambda: controller.showFrame(0) )
        backButton.grid(column=1, row=10)

    def putData(self):
        query = 'select * from Event where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        event = list(r.fetch_row(maxrows=0,how=1))
        self.eventNamelbl = tk.Label(self,font=("Helvetica", 16),background="white", text=('      '+event[0]['Name'].decode()+'     '))
        self.eventNamelbl.grid(column = 0, row = 1)

        query = 'select * from Speaker NATURAL JOIN Talk where EventId = ' + self.controller.EventId 
        db.query(query)
        r = db.store_result()
        talks = list(r.fetch_row(maxrows=0,how=1))

        self.talkLbl = []
        for i,talk in enumerate(talks):
            self.talkLbl.append(tk.Label(self,background="white", text=' '+talk['Title'].decode()+' '))
            self.talkLbl[i].grid(column=10, row=i)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.data = {}
        tk.Frame.__init__(self, *args, **kwargs)
        self.frames = []
        self.frames.append(Page1(self))
        self.frames.append(Page2(self))
#        self.p3 = Page3(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames[0].place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.frames[1].place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.frames[0].show()
    def showFrame(self, c):
        self.frames[c].tkraise()

if __name__ == "__main__":
    
    root = tk.Tk()

    menubar = tk.Menu(root)
    menubar.add_command(label='Welcome to XYZ Conference')
    root.config(menu=menubar)
    
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("630x460")
    root.title('Conference Information App')
    root.mainloop()
