from tkinter import Button,Label,Entry,messagebox
from src.pages.Page import Page
from src.TkStyles import buttonStyle, labelStyle, entryStyle

class LoginPage(Page):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        Page.__init__(self, *args, logo='grid', **kwargs)

        L1 = Label(self,text="User Name", **labelStyle)
        L1.grid(row = 3, column = 8)
        self.Username = Entry(self, **entryStyle)
        self.Username.grid(row = 3, column = 10)
        L2 = Label(self,text="Password", **labelStyle)
        L2.grid(row = 4, column = 8)
        self.Password = Entry(self, **entryStyle, show="*")
        self.Password.grid(row = 4, column = 10)

        SubmitButton = Button(self,text='Login', **buttonStyle, command=self.login)
        SubmitButton.grid(row = 5, column = 8)
        backButton = Button(self, text="Back", **buttonStyle ,command = lambda :self.controller.showFrame('MenuPage'))
        backButton.grid(row = 5, column = 10)


    def login(self):
        if(self.Username.get()=='Admin' and self.Password.get()=='Pass'):
            self.controller.showFrame('AdminPage')
        else:
            pass
            messagebox.showinfo("Incorrect Login!", "The username and password you entered are incorrect!")