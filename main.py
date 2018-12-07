
from tkinter import Tk,ttk
from src.MainView import MainView

if __name__ == "__main__":
    root = Tk()
    style = ttk.Style(root)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1024x720")
    root.title('ICACCI Information App')
    root.mainloop()